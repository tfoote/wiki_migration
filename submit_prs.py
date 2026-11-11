import argparse
import base64
import datetime
import email.utils
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import yaml

from review_packages import PREVIEW_LINES, print_markdown

FORK_ORG = "tfoote-ros-wiki-migration-forks"

MUTATING_METHODS = ("POST", "PUT", "PATCH", "DELETE")
# Minimum quiet gap (seconds) between consecutive mutating API calls to avoid
# tripping GitHub's secondary content-creation rate limits.
MUTATION_DELAY = 1.5
SECONDARY_BACKOFF_INITIAL = 60.0
SECONDARY_BACKOFF_MAX = 900.0
MAX_SECONDARY_RETRIES = 5

_last_mutation_time = 0.0

_THROTTLE_PHRASES = (
    "rate limit",
    "secondary rate",
    "abuse detection",
    "too quickly",
    "temporarily blocked",
    "too many requests",
)
_EXPLICIT_DURATION_RE = re.compile(
    r"(?<!\bper\s)(?<!/)(\d+(?:\.\d+)?)\s*(seconds?|secs?|minutes?|mins?|hours?|hrs?)\b",
    re.IGNORECASE,
)
_WORD_MINUTE_RE = re.compile(
    r"\b(?:wait|after|in|for)\s+(?:a|one)\s+minutes?\b", re.IGNORECASE
)
_WORD_HOUR_RE = re.compile(
    r"\b(?:wait|after|in|for)\s+(?:an|one)\s+hours?\b", re.IGNORECASE
)
_FEW_MINUTES_RE = re.compile(r"\ba\s+few\s+minutes\b", re.IGNORECASE)
_COUPLE_MINUTES_RE = re.compile(
    r"\ba\s+couple\s+(?:of\s+)?minutes\b", re.IGNORECASE
)
_FEW_SECONDS_RE = re.compile(r"\ba\s+few\s+seconds\b", re.IGNORECASE)
_UTC_TIMESTAMP_RE = re.compile(
    r"\b(\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2})(?:Z|\s*UTC)\b"
)


def parse_github_repo(repo_url):
    """Extract (owner, repo) from a GitHub repository URL."""
    if not repo_url or "github.com" not in repo_url:
        raise ValueError(f"Unsupported or non-GitHub repository URL: {repo_url}")
    cleaned = repo_url.rstrip("/")
    if cleaned.endswith(".git"):
        cleaned = cleaned[:-4]
    parts = cleaned.split("/")
    if len(parts) < 2:
        raise ValueError(f"Cannot parse owner/repo from URL: {repo_url}")
    return parts[-2], parts[-1]


def _get_header(headers, name):
    """Case-insensitive header lookup supporting both HTTPMessage and dict."""
    if not headers:
        return None
    val = headers.get(name)
    if val is not None:
        return val
    lower = name.lower()
    for k, v in headers.items():
        if k.lower() == lower:
            return v
    return None


def _parse_error_detail(raw_body):
    """Extract (detail_dict, combined_message_str) from a GitHub error body."""
    if not raw_body:
        return {}, ""
    try:
        detail = json.loads(raw_body)
        if not isinstance(detail, dict):
            return {}, ""
        parts = [detail.get("message", "")]
        parts += [
            err.get("message") or json.dumps(err)
            for err in detail.get("errors", [])
            if isinstance(err, dict)
        ]
        message = "; ".join(p for p in parts if p)
        return detail, message
    except Exception:
        return {}, ""


def parse_retry_after_header(value, now=None):
    """Parse a Retry-After header (seconds or HTTP-date) into seconds to wait."""
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    try:
        secs = float(text)
        return max(0.0, secs)
    except ValueError:
        pass
    try:
        dt = email.utils.parsedate_to_datetime(text)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=datetime.timezone.utc)
        if now is None:
            now = time.time()
        return max(0.0, dt.timestamp() - now)
    except Exception:
        return None


def parse_retry_after_body(detail, message, now=None):
    """Extract retry delay from JSON body fields or prose in the error message.

    Returns (seconds, is_explicit) where is_explicit is True for exact numbers
    or timestamps and False for fuzzy phrases like 'a few minutes'.
    """
    if isinstance(detail, dict) and detail.get("retry_after") is not None:
        try:
            return max(0.0, float(detail["retry_after"])), True
        except (TypeError, ValueError):
            pass

    if not message:
        return None, False

    ts_match = _UTC_TIMESTAMP_RE.search(message)
    if ts_match:
        try:
            raw_ts = ts_match.group(1).replace(" ", "T")
            dt = datetime.datetime.fromisoformat(raw_ts).replace(
                tzinfo=datetime.timezone.utc
            )
            if now is None:
                now = time.time()
            delta = dt.timestamp() - now
            if delta > 0:
                return delta + 5.0, True
        except ValueError:
            pass

    dur_match = _EXPLICIT_DURATION_RE.search(message)
    if dur_match:
        amount = float(dur_match.group(1))
        unit = dur_match.group(2).lower()
        if unit.startswith("h"):
            return amount * 3600.0, True
        if unit.startswith("m"):
            return amount * 60.0, True
        return amount, True

    if _WORD_HOUR_RE.search(message):
        return 3600.0, True
    if _WORD_MINUTE_RE.search(message):
        return 60.0, True
    if _FEW_MINUTES_RE.search(message):
        return 180.0, False
    if _COUPLE_MINUTES_RE.search(message):
        return 120.0, False
    if _FEW_SECONDS_RE.search(message):
        return 10.0, False

    return None, False


def compute_rate_limit_sleep(
    status_code, headers, detail, message, secondary_attempt=0, now=None
):
    """Determine (sleep_seconds, kind, description) for a 403/429 response.

    kind is 'primary', 'secondary', or None (when the error is not a rate limit,
    such as a repository permission error).
    """
    if status_code not in (403, 429):
        return None, None, None

    if now is None:
        now = time.time()

    remaining = _get_header(headers, "X-RateLimit-Remaining")
    reset_hdr = _get_header(headers, "X-RateLimit-Reset")
    retry_after_hdr = _get_header(headers, "Retry-After")

    header_wait = parse_retry_after_header(retry_after_hdr, now=now)
    body_wait, body_explicit = parse_retry_after_body(detail, message, now=now)

    # 1. Primary quota exhausted (X-RateLimit-Remaining == 0)
    if remaining is not None and str(remaining).strip() == "0" and reset_hdr:
        try:
            reset_wait = max(1.0, float(reset_hdr) - now + 5.0)
            candidates = [reset_wait]
            if header_wait is not None:
                candidates.append(header_wait)
            if body_explicit and body_wait is not None:
                candidates.append(body_wait)
            return (
                max(candidates),
                "primary",
                "Primary rate limit exhausted (X-RateLimit-Remaining: 0)",
            )
        except ValueError:
            pass

    # 2. Secondary / content-creation rate limit
    msg_lower = (message or "").lower()
    is_secondary = (
        status_code == 429
        or header_wait is not None
        or body_wait is not None
        or any(phrase in msg_lower for phrase in _THROTTLE_PHRASES)
    )
    if not is_secondary:
        return None, None, None

    if header_wait is not None and body_explicit and body_wait is not None:
        sleep_time = max(1.0, header_wait, body_wait)
        source = f"Retry-After / message body: {sleep_time:.0f}s"
    elif header_wait is not None:
        sleep_time = max(1.0, header_wait)
        source = f"Retry-After: {header_wait:.0f}s"
    elif body_wait is not None:
        scaled = min(SECONDARY_BACKOFF_MAX, body_wait * (2 ** secondary_attempt))
        sleep_time = max(1.0, scaled)
        source = (
            "message body"
            if secondary_attempt == 0
            else f"message body + backoff #{secondary_attempt + 1}"
        )
    else:
        scaled = min(
            SECONDARY_BACKOFF_MAX,
            SECONDARY_BACKOFF_INITIAL * (2 ** secondary_attempt),
        )
        sleep_time = max(1.0, scaled)
        source = f"exponential backoff #{secondary_attempt + 1}"

    return sleep_time, "secondary", f"Secondary rate limit hit ({source})"


def github_api_request(url, method="GET", data=None, token=None, accept_statuses=(200, 201, 202)):
    """Perform a GitHub REST API request with pacing and primary/secondary rate-limit handling."""
    global _last_mutation_time
    if token is None:
        token = os.environ.get("GITHUB_TOKEN")

    headers = {
        "User-Agent": "ros-wiki-migration",
        "Accept": "application/vnd.github+json",
    }
    if token:
        headers["Authorization"] = f"token {token}"

    body_bytes = None
    if data is not None:
        body_bytes = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"

    is_mutation = method.upper() in MUTATING_METHODS
    secondary_retries = 0

    while True:
        if is_mutation and MUTATION_DELAY > 0 and _last_mutation_time > 0:
            pace_wait = MUTATION_DELAY - (time.monotonic() - _last_mutation_time)
            if pace_wait > 0:
                time.sleep(pace_wait)

        req = urllib.request.Request(url, data=body_bytes, headers=headers, method=method)
        try:
            try:
                with urllib.request.urlopen(req) as response:
                    resp_body = response.read().decode("utf-8")
                    if response.status in accept_statuses:
                        return json.loads(resp_body) if resp_body else {}
                    raise RuntimeError(f"Unexpected status {response.status} from {url}")
            finally:
                if is_mutation:
                    _last_mutation_time = time.monotonic()
        except urllib.error.HTTPError as e:
            raw_err = ""
            try:
                raw_err = e.read().decode("utf-8", errors="replace")
            except Exception:
                pass
            detail, message = _parse_error_detail(raw_err)

            sleep_time, kind, desc = compute_rate_limit_sleep(
                e.code,
                e.headers,
                detail,
                message,
                secondary_attempt=secondary_retries,
            )
            if sleep_time is not None and (
                kind == "primary" or secondary_retries < MAX_SECONDARY_RETRIES
            ):
                wake_dt = datetime.datetime.fromtimestamp(
                    time.time() + sleep_time, tz=datetime.timezone.utc
                ).astimezone()
                wake_str = wake_dt.strftime("%H:%M:%S %Z")
                msg_part = f": {message}" if message else ""
                print(f"  {desc}{msg_part}", flush=True)
                if kind == "secondary":
                    secondary_retries += 1
                    print(
                        f"  Sleeping for {sleep_time:.1f}s (until {wake_str}, "
                        f"retry {secondary_retries}/{MAX_SECONDARY_RETRIES})...",
                        flush=True,
                    )
                else:
                    print(
                        f"  Sleeping for {sleep_time:.1f}s (until {wake_str})...",
                        flush=True,
                    )
                time.sleep(sleep_time)
                continue

            # Include GitHub's explanation (e.g. "Validation Failed: ...") in
            # the error, otherwise a 422 or non-retryable 403 is impossible to diagnose.
            if message:
                e.msg = f"{e.msg}: {message} ({method} {url})"
            raise e


def get_readme_path(subdirectory):
    """Return the repository-relative path to README.md."""
    subdir = (subdirectory or "").strip("/")
    return f"{subdir}/README.md" if subdir else "README.md"


def attachments_manifest_path(md_file):
    """Sidecar written by convert_to_markdown.py listing doc/ attachments."""
    return os.path.splitext(md_file)[0] + ".attachments.yaml"


def load_attachments(md_file):
    """Return {"doc/<name>": <local source path>} for a Markdown file."""
    if not md_file:
        return {}
    path = attachments_manifest_path(md_file)
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def get_attachment_repo_path(subdirectory, doc_key):
    """Repository path for an attachment key like 'doc/foo.png'."""
    subdir = (subdirectory or "").strip("/")
    return f"{subdir}/{doc_key}" if subdir else doc_key


def commit_attachments(
    fork_owner, fork_repo, branch, subdirectory, attachments, package, token
):
    """Commit attachment files into <subdirectory>/doc/ as a single commit.

    Files that already exist on the branch are left untouched. Returns
    (commit_sha or None, list of uploaded repo paths).
    """
    api = f"https://api.github.com/repos/{fork_owner}/{fork_repo}"
    encoded_branch = urllib.parse.quote(branch, safe="")

    tree_entries = []
    uploaded = []
    for doc_key, src in sorted(attachments.items()):
        repo_path = get_attachment_repo_path(subdirectory, doc_key)
        if not os.path.exists(src):
            print(f"  Warning: attachment source {src} not found; skipping.", flush=True)
            continue
        _, existing_sha = get_existing_file_on_branch(
            fork_owner, fork_repo, repo_path, branch, token
        )
        if existing_sha is not None:
            print(f"  Warning: {repo_path} already exists on {branch}; not overwriting.", flush=True)
            continue
        with open(src, "rb") as f:
            blob = github_api_request(
                f"{api}/git/blobs",
                method="POST",
                data={"content": base64.b64encode(f.read()).decode("ascii"),
                      "encoding": "base64"},
                token=token,
            )
        tree_entries.append(
            {"path": repo_path, "mode": "100644", "type": "blob", "sha": blob["sha"]}
        )
        uploaded.append(repo_path)

    if not tree_entries:
        return None, []

    print(f"  Committing {len(tree_entries)} attachment(s) to {branch}...", flush=True)
    ref = github_api_request(f"{api}/git/ref/heads/{encoded_branch}", token=token)
    parent_sha = ref["object"]["sha"]
    parent = github_api_request(f"{api}/git/commits/{parent_sha}", token=token)
    tree = github_api_request(
        f"{api}/git/trees",
        method="POST",
        data={"base_tree": parent["tree"]["sha"], "tree": tree_entries},
        token=token,
    )
    commit = github_api_request(
        f"{api}/git/commits",
        method="POST",
        data={
            "message": (
                f"Add {package} documentation attachments from wiki.ros.org\n\n"
                f"Images and files attached to the ROS Wiki page "
                f"https://wiki.ros.org/{package}, referenced from README.md."
            ),
            "tree": tree["sha"],
            "parents": [parent_sha],
        },
        token=token,
    )
    github_api_request(
        f"{api}/git/refs/heads/{encoded_branch}",
        method="PATCH",
        data={"sha": commit["sha"]},
        token=token,
    )
    return commit["sha"], uploaded


def build_commit_message(package, source_file, action):
    """Build the commit message explaining the origin of the content."""
    verb = "Add" if action == "create" else "Append"
    wiki_url = f"https://wiki.ros.org/{package}"
    msg = (
        f"{verb} {package} README.md migrated from wiki.ros.org\n\n"
        f"This content was automatically converted from the ROS Wiki page\n"
        f"{wiki_url}"
    )
    if source_file:
        msg += f" (source: {source_file})"
    msg += " into GitHub Markdown format."
    return msg


def build_pr_title(package):
    return f"Migrate {package} documentation from wiki.ros.org"


def build_pr_body(
    package,
    source_file,
    target_path,
    action,
    original_pr_url=None,
    declared_branch=None,
    default_branch=None,
):
    wiki_url = f"https://wiki.ros.org/{package}"
    action_desc = (
        f"creates `{target_path}`"
        if action == "create"
        else f"appends the converted wiki documentation to `{target_path}`"
    )
    caveat_header = ""
    if original_pr_url:
        caveat_header = (
            f"> [!WARNING]\n"
            f"> **CAVEAT: Duplicate PR targeting the default branch (`{default_branch}`)**\n"
            f">\n"
            f"> This pull request is a duplicate of {original_pr_url} "
            f"(which targets `{declared_branch}`), opened against the default branch "
            f"(`{default_branch}`) for better visibility. **The migrated content comes "
            f"from the ROS 1 Wiki and is not confirmed to be up to date for `{default_branch}`.**\n\n"
        )

    return (
        caveat_header
        + f"### Origin of this Pull Request\n\n"
        f"This pull request {action_desc} using content migrated from the "
        f"ROS Wiki page [{package}]({wiki_url})"
        + (f" (`{source_file}`)" if source_file else "")
        + ".\n\n"
        f"Project source with the scripts I'm using are at https://github.com/tfoote-ros-wiki-migration-forks"
        + ".\n\n"
        f"### Please Note\n\n"
        f"The goal of this effort is to provide the existing ROS Wiki documentation "
        f"in GitHub Markdown format directly inside the source repository so that it "
        f"remains accessible alongside the code.\n\n"
        f"Because this is part of a bulk migration across many ROS packages, **I will "
        f"not be able to iterate on changes in this PR**. Please feel free to edit this "
        f"branch, merge it as a starting point, or close this PR as *won't fix* if it "
        f"is not appropriate for your repository."
    )


def sync_and_get_branch_sha(owner, repo, fork_owner, fork_repo, branch, token):
    """Get upstream branch SHA, wait for fork branch ref, and sync fork branch with upstream."""
    encoded_branch = urllib.parse.quote(branch, safe="")
    upstream_ref_url = (
        f"https://api.github.com/repos/{owner}/{repo}/git/ref/heads/{encoded_branch}"
    )
    upstream_ref = github_api_request(upstream_ref_url, method="GET", token=token)
    base_sha = upstream_ref["object"]["sha"]

    fork_ref_url = (
        f"https://api.github.com/repos/{fork_owner}/{fork_repo}/git/ref/heads/{encoded_branch}"
    )
    for attempt in range(10):
        try:
            github_api_request(fork_ref_url, method="GET", token=token)
            break
        except urllib.error.HTTPError as e:
            if e.code in (404, 409) and attempt < 9:
                print("  Waiting for fork initialization...", flush=True)
                time.sleep(2)
            else:
                raise

    merge_upstream_url = (
        f"https://api.github.com/repos/{fork_owner}/{fork_repo}/merge-upstream"
    )
    try:
        github_api_request(
            merge_upstream_url,
            method="POST",
            data={"branch": branch},
            token=token,
            accept_statuses=(200, 201, 202, 409),
        )
    except urllib.error.HTTPError:
        pass

    return base_sha


def find_existing_fork(owner, repo, fork_org, token, max_pages=10):
    """Return the repo info of fork_org's existing fork of owner/repo, or None.

    GitHub's "create fork" endpoint does not reliably return an existing fork:
    calling it again for a repo already forked into the organization created
    duplicate forks named <repo>-1, <repo>-2, ... So look for the fork first.
    """
    upstream = f"{owner}/{repo}".lower()

    def is_our_fork(info):
        if not info.get("fork"):
            return False
        if info.get("owner", {}).get("login", "").lower() != fork_org.lower():
            return False
        parents = {(info.get(k) or {}).get("full_name", "").lower() for k in ("parent", "source")}
        return upstream in parents

    # Fast path: the fork has the same name as the upstream repo.
    try:
        info = github_api_request(f"https://api.github.com/repos/{fork_org}/{repo}", token=token)
        if is_our_fork(info):
            return info
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise

    # Slow path: the fork has another name (e.g. renamed); scan upstream's forks.
    for page in range(1, max_pages + 1):
        forks = github_api_request(
            f"https://api.github.com/repos/{owner}/{repo}/forks?per_page=100&sort=oldest&page={page}",
            token=token,
        )
        for f in forks:
            if f.get("owner", {}).get("login", "").lower() == fork_org.lower():
                # Listing entries lack parent info; fetch the full repo.
                return github_api_request(f["url"], token=token)
        if len(forks) < 100:
            break
    return None


def ensure_fork(owner, repo, fork_org, declared_branch, token):
    """Find or create the fork in fork_org.

    Returns (fork_owner, fork_repo, base_sha, default_branch).
    """
    print(f"  Ensuring fork of {owner}/{repo} in organization {fork_org}...", flush=True)
    fork_info = find_existing_fork(owner, repo, fork_org, token)
    if fork_info:
        print(f"  Using existing fork {fork_info.get('full_name')}.", flush=True)
    else:
        fork_info = github_api_request(
            f"https://api.github.com/repos/{owner}/{repo}/forks",
            method="POST",
            data={"organization": fork_org, "default_branch_only": False},
            token=token,
        )
    fork_owner = fork_info.get("owner", {}).get("login", fork_org)
    fork_repo = fork_info.get("name", repo)

    default_branch = (
        fork_info.get("parent", {}).get("default_branch")
        or fork_info.get("source", {}).get("default_branch")
        or fork_info.get("default_branch")
    )
    if not default_branch:
        repo_url = f"https://api.github.com/repos/{owner}/{repo}"
        repo_info = github_api_request(repo_url, method="GET", token=token)
        default_branch = repo_info.get("default_branch")

    base_sha = sync_and_get_branch_sha(
        owner, repo, fork_owner, fork_repo, declared_branch, token
    )

    return fork_owner, fork_repo, base_sha, default_branch


def create_or_reset_branch(fork_owner, fork_repo, new_branch, base_sha, token):
    """Create a new branch on the fork at base_sha (or reset it if it already exists)."""
    refs_url = f"https://api.github.com/repos/{fork_owner}/{fork_repo}/git/refs"
    print(f"  Creating branch '{new_branch}' at {base_sha[:8]}...", flush=True)
    try:
        github_api_request(
            refs_url,
            method="POST",
            data={"ref": f"refs/heads/{new_branch}", "sha": base_sha},
            token=token,
        )
    except urllib.error.HTTPError as e:
        if e.code == 422:
            # Branch already exists; reset it to base_sha
            encoded_branch = urllib.parse.quote(new_branch, safe="")
            update_ref_url = (
                f"https://api.github.com/repos/{fork_owner}/{fork_repo}/git/refs/heads/{encoded_branch}"
            )
            github_api_request(
                update_ref_url,
                method="PATCH",
                data={"sha": base_sha, "force": True},
                token=token,
            )
        else:
            raise


def get_existing_file_on_branch(owner, repo, path, branch, token):
    """Return (decoded_content, sha) if path exists on branch, else (None, None)."""
    encoded_path = "/".join(urllib.parse.quote(part, safe="") for part in path.split("/"))
    encoded_branch = urllib.parse.quote(branch, safe="")
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{encoded_path}?ref={encoded_branch}"
    try:
        resp = github_api_request(url, method="GET", token=token)
        content_b64 = resp.get("content", "")
        decoded = base64.b64decode(content_b64).decode("utf-8", errors="replace")
        return decoded, resp.get("sha")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None, None
        raise


def create_or_update_readme(
    fork_owner,
    fork_repo,
    target_path,
    new_branch,
    markdown_content,
    source_file,
    package,
    token,
):
    """Create README.md if it doesn't exist on new_branch, otherwise append to it."""
    existing_content, existing_sha = get_existing_file_on_branch(
        fork_owner, fork_repo, target_path, new_branch, token
    )

    if existing_sha is None:
        action = "create"
        final_content = markdown_content
        print(f"  Creating new file {target_path} on {new_branch}...", flush=True)
    else:
        action = "append"
        separator = "\n\n" if existing_content and not existing_content.endswith("\n\n") else ""
        if existing_content and existing_content.endswith("\n") and not existing_content.endswith("\n\n"):
            separator = "\n"
        final_content = (existing_content or "") + separator + markdown_content
        print(f"  Appending to existing file {target_path} on {new_branch}...", flush=True)

    commit_message = build_commit_message(package, source_file, action)
    encoded_path = "/".join(
        urllib.parse.quote(part, safe="") for part in target_path.split("/")
    )
    contents_url = f"https://api.github.com/repos/{fork_owner}/{fork_repo}/contents/{encoded_path}"

    payload = {
        "message": commit_message,
        "content": base64.b64encode(final_content.encode("utf-8")).decode("ascii"),
        "branch": new_branch,
    }
    if existing_sha is not None:
        payload["sha"] = existing_sha

    resp = github_api_request(contents_url, method="PUT", data=payload, token=token)
    commit_sha = resp.get("commit", {}).get("sha")
    return action, commit_sha


def create_pull_request(
    upstream_owner,
    upstream_repo,
    fork_owner,
    new_branch,
    base_branch,
    package,
    source_file,
    target_path,
    action,
    token,
    original_pr_url=None,
    declared_branch=None,
    fork_repo=None,
):
    """Create a pull request from fork_owner:new_branch to upstream_owner/upstream_repo:base_branch."""
    pulls_url = f"https://api.github.com/repos/{upstream_owner}/{upstream_repo}/pulls"
    title = build_pr_title(package)
    body = build_pr_body(
        package,
        source_file,
        target_path,
        action,
        original_pr_url=original_pr_url,
        declared_branch=declared_branch,
        default_branch=base_branch if original_pr_url else None,
    )
    payload = {
        "title": title,
        "head": f"{fork_owner}:{new_branch}",
        "base": base_branch,
        "body": body,
    }
    if fork_repo:
        # "owner:branch" alone is ambiguous when the owner has more than one
        # fork of the upstream repo; name the head repository explicitly.
        payload["head_repo"] = fork_repo
    print(
        f"  Creating PR against {upstream_owner}/{upstream_repo}:{base_branch}...",
        flush=True,
    )
    pr_resp = github_api_request(pulls_url, method="POST", data=payload, token=token)
    return pr_resp.get("html_url")


def execute_submission(package, info, fork_org, token):
    """Perform the fork, branch, commit, and PR workflow for a single package."""
    repo_url = info.get("repository")
    declared_branch = info.get("branch", "noetic")
    subdirectory = info.get("subdirectory", "")
    md_file = info.get("markdown_file")
    source_file = info.get("source_file", "")

    if not md_file or not os.path.exists(md_file):
        raise FileNotFoundError(f"Markdown file not found for {package}: {md_file}")

    with open(md_file, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    upstream_owner, upstream_repo = parse_github_repo(repo_url)
    target_path = get_readme_path(subdirectory)
    new_branch = f"ros-wiki-migration-{package}"

    fork_owner, fork_repo, base_sha, default_branch = ensure_fork(
        upstream_owner, upstream_repo, fork_org, declared_branch, token
    )
    create_or_reset_branch(fork_owner, fork_repo, new_branch, base_sha, token)
    action, commit_sha = create_or_update_readme(
        fork_owner,
        fork_repo,
        target_path,
        new_branch,
        markdown_content,
        source_file,
        package,
        token,
    )
    attachments = load_attachments(md_file)
    attachments_commit_sha, uploaded_attachments = None, []
    if attachments:
        attachments_commit_sha, uploaded_attachments = commit_attachments(
            fork_owner, fork_repo, new_branch, subdirectory, attachments,
            package, token,
        )
    pr_url = create_pull_request(
        upstream_owner,
        upstream_repo,
        fork_owner,
        new_branch,
        declared_branch,
        package,
        source_file,
        target_path,
        action,
        token,
        fork_repo=fork_repo,
    )

    result = {
        "pr_url": pr_url,
        "fork_repository": f"https://github.com/{fork_owner}/{fork_repo}.git",
        "submitted_branch": new_branch,
        "commit_sha": commit_sha,
        "action": action,
    }
    if uploaded_attachments:
        result["attachments"] = uploaded_attachments
        result["attachments_commit_sha"] = attachments_commit_sha

    if default_branch and default_branch != declared_branch:
        print(
            f"  Target branch '{declared_branch}' differs from default branch '{default_branch}'. "
            f"Opening a second PR targeting '{default_branch}'...",
            flush=True,
        )
        default_base_sha = sync_and_get_branch_sha(
            upstream_owner,
            upstream_repo,
            fork_owner,
            fork_repo,
            default_branch,
            token,
        )
        default_new_branch = f"ros-wiki-migration-{package}-{default_branch}"
        create_or_reset_branch(
            fork_owner, fork_repo, default_new_branch, default_base_sha, token
        )
        default_action, default_commit_sha = create_or_update_readme(
            fork_owner,
            fork_repo,
            target_path,
            default_new_branch,
            markdown_content,
            source_file,
            package,
            token,
        )
        if attachments:
            commit_attachments(
                fork_owner, fork_repo, default_new_branch, subdirectory,
                attachments, package, token,
            )
        default_pr_url = create_pull_request(
            upstream_owner,
            upstream_repo,
            fork_owner,
            default_new_branch,
            default_branch,
            package,
            source_file,
            target_path,
            default_action,
            token,
            original_pr_url=pr_url,
            declared_branch=declared_branch,
            fork_repo=fork_repo,
        )
        result["default_branch"] = default_branch
        result["default_branch_pr_url"] = default_pr_url
        result["default_submitted_branch"] = default_new_branch
        result["default_commit_sha"] = default_commit_sha
        result["default_action"] = default_action

    return result


def print_preview(package, info, source_yaml, fork_org):
    """Print a detailed preview of the planned fork, branch, commit, and PR."""
    repo_url = info.get("repository")
    declared_branch = info.get("branch", "noetic")
    subdirectory = info.get("subdirectory", "")
    md_file = info.get("markdown_file")
    source_file = info.get("source_file", "")
    readme_exists = bool(info.get("readme_exists", False))

    try:
        upstream_owner, upstream_repo = parse_github_repo(repo_url)
        fork_target = f"{fork_org}/{upstream_repo}"
    except ValueError:
        upstream_owner, upstream_repo = "unknown", "unknown"
        fork_target = f"{fork_org}/unknown"

    target_path = get_readme_path(subdirectory)
    new_branch = f"ros-wiki-migration-{package}"
    planned_action = "append" if readme_exists else "create"
    action_description = (
        f"Append content to existing {target_path}"
        if readme_exists
        else f"Create new {target_path}"
    )

    print("\n" + "=" * 60, flush=True)
    print(f"Submission Preview for Package: {package}", flush=True)
    print(f"Source Queue File: {source_yaml}", flush=True)
    print("-" * 60, flush=True)
    print(f"1. Fork Repository: {repo_url} -> https://github.com/{fork_target}", flush=True)
    print(
        f"2. Create Branch:   '{new_branch}' (off declared branch '{declared_branch}')",
        flush=True,
    )
    print(f"3. File Operation:  {action_description}", flush=True)
    attachments = load_attachments(md_file)
    if attachments:
        print(f"   Attachments:     {len(attachments)} file(s) committed separately:", flush=True)
        for doc_key, src in sorted(attachments.items()):
            print(f"     {get_attachment_repo_path(subdirectory, doc_key)}  <-  {src}", flush=True)
    print(
        f"4. Commit Message:\n   "
        + build_commit_message(package, source_file, planned_action).replace("\n", "\n   "),
        flush=True,
    )
    print(f"5. Pull Request:    {fork_org}:{new_branch} -> {upstream_owner}/{upstream_repo}:{declared_branch}", flush=True)
    print(f"   PR Title:        {build_pr_title(package)}", flush=True)
    print(
        f"   Note:            If '{declared_branch}' is not the default branch, a second PR with a caveat will also be opened against the default branch.",
        flush=True,
    )
    print("-" * 60, flush=True)

    if md_file and os.path.exists(md_file):
        print_markdown(md_file, max_lines=PREVIEW_LINES)
    else:
        print(f"Warning: Markdown file '{md_file}' not found!", flush=True)


def record_submitted_package(
    package, info, result_meta, yaml_file, data, submitted_file
):
    """Move a successfully submitted package from data/yaml_file to submitted_file."""
    submitted_data = {}
    if os.path.exists(submitted_file):
        with open(submitted_file, "r", encoding="utf-8") as f_sub:
            submitted_data = yaml.safe_load(f_sub) or {}

    submitted_entry = dict(info)
    submitted_entry.update(result_meta)
    submitted_entry["source_queue"] = yaml_file
    submitted_data[package] = submitted_entry

    del data[package]

    with open(submitted_file, "w", encoding="utf-8") as f_sub:
        yaml.dump(submitted_data, f_sub, default_flow_style=False, sort_keys=True)

    with open(yaml_file, "w", encoding="utf-8") as f_src:
        yaml.dump(data, f_src, default_flow_style=False, sort_keys=True)

    print(
        f"  Moved '{package}' from {yaml_file} to {submitted_file}.",
        flush=True,
    )


def format_batch_item(package, info, yaml_file):
    """Format a single-line summary for batch confirmation."""
    repo_url = info.get("repository", "")
    declared_branch = info.get("branch", "noetic")
    subdirectory = info.get("subdirectory", "")
    readme_exists = bool(info.get("readme_exists", False))
    try:
        owner, repo = parse_github_repo(repo_url)
        repo_disp = f"{owner}/{repo}"
    except ValueError:
        repo_disp = repo_url or "unknown"
    action = "append" if readme_exists else "create"
    target_path = get_readme_path(subdirectory)
    return (
        f"{package} -> {repo_disp}:{declared_branch} "
        f"({action} {target_path}) [{yaml_file}]"
    )


def process_batch(
    yaml_files,
    submitted_file,
    review_key,
    batch_size,
    fork_org=FORK_ORG,
    token=None,
):
    """Collect up to batch_size ready packages, confirm once, and submit non-interactively."""
    loaded_files = {}
    all_ready = []

    for yaml_file in yaml_files:
        if yaml_file in loaded_files or not os.path.exists(yaml_file):
            continue
        with open(yaml_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        loaded_files[yaml_file] = data
        for pkg, info in data.items():
            if (
                isinstance(info, dict)
                and str(info.get(review_key, "")).lower() == "ready"
            ):
                all_ready.append((yaml_file, pkg))

    if not all_ready:
        print(
            f"No packages marked ready for review key '{review_key}'.",
            flush=True,
        )
        return 0

    selected = all_ready[:batch_size]
    print(
        f"\nBatch submission: {len(selected)} of {len(all_ready)} ready package(s) "
        f"for review key '{review_key}':",
        flush=True,
    )
    for idx, (yaml_file, pkg) in enumerate(selected, 1):
        info = loaded_files[yaml_file][pkg]
        print(f"  {idx}. {format_batch_item(pkg, info, yaml_file)}", flush=True)

    while True:
        print(
            f"\nSubmit these {len(selected)} package(s)? [Y]es / [N]o: ",
            end="",
            flush=True,
        )
        line = sys.stdin.readline()
        if not line:
            print("\nAborted.", flush=True)
            return 0
        choice = line.strip().upper()
        if choice in ("Y", "YES"):
            break
        if choice in ("N", "NO", "Q", "QUIT"):
            print("Batch submission cancelled.", flush=True)
            return 0
        print("Invalid choice. Please enter Y or N.", flush=True)

    succeeded = 0
    failed = 0
    for idx, (yaml_file, package) in enumerate(selected, 1):
        data = loaded_files[yaml_file]
        info = data[package]
        print(
            f"\n[{idx}/{len(selected)}] Submitting {package} ({yaml_file})...",
            flush=True,
        )
        try:
            result_meta = execute_submission(
                package, info, fork_org=fork_org, token=token
            )
        except Exception as e:
            print(f"Error submitting PR for {package}: {e}", flush=True)
            failed += 1
            continue

        print(f"  Successfully created PR: {result_meta['pr_url']}", flush=True)
        if "default_branch_pr_url" in result_meta:
            print(
                f"  Successfully created default-branch PR: {result_meta['default_branch_pr_url']}",
                flush=True,
            )

        record_submitted_package(
            package, info, result_meta, yaml_file, data, submitted_file
        )
        succeeded += 1

    summary = f"\nBatch complete: {succeeded}/{len(selected)} package(s) submitted."
    if failed:
        summary += f" ({failed} failed)"
    print(summary, flush=True)
    return succeeded


def process_yaml_file(
    yaml_file,
    submitted_file,
    review_key,
    fork_org=FORK_ORG,
    token=None,
):
    """Iterate through ready entries in yaml_file, prompt for confirmation, submit PRs, and move to submitted_file."""
    if not os.path.exists(yaml_file):
        print(f"File {yaml_file} not found, skipping.", flush=True)
        return True

    with open(yaml_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    if not data:
        return True

    ready_packages = [
        pkg
        for pkg, info in data.items()
        if isinstance(info, dict)
        and str(info.get(review_key, "")).lower() == "ready"
    ]

    if not ready_packages:
        print(
            f"No packages marked ready for review key '{review_key}' in {yaml_file}.",
            flush=True,
        )
        return True

    print(
        f"Found {len(ready_packages)} ready package(s) in {yaml_file} for review key '{review_key}'.",
        flush=True,
    )

    for package in ready_packages:
        info = data[package]
        print_preview(package, info, yaml_file, fork_org)

        while True:
            print(
                "\nConfirm submission? [Y]es / [S]kip / [V]iew All / [Q]uit: ",
                end="",
                flush=True,
            )
            choice = sys.stdin.readline().strip().upper()

            if choice in ("Q", "QUIT"):
                print("Quitting.", flush=True)
                return False
            elif choice in ("S", "SKIP", "N", "NO"):
                print(f"Skipping {package}.", flush=True)
                break
            elif choice in ("Y", "YES"):
                try:
                    result_meta = execute_submission(
                        package, info, fork_org=fork_org, token=token
                    )
                except Exception as e:
                    print(f"Error submitting PR for {package}: {e}", flush=True)
                    break

                print(f"  Successfully created PR: {result_meta['pr_url']}", flush=True)
                if "default_branch_pr_url" in result_meta:
                    print(
                        f"  Successfully created default-branch PR: {result_meta['default_branch_pr_url']}",
                        flush=True,
                    )

                record_submitted_package(
                    package, info, result_meta, yaml_file, data, submitted_file
                )
                break
            elif choice in ("V", "VIEW"):
                md_file = info.get("markdown_file")
                if md_file and os.path.exists(md_file):
                    print(flush=True)
                    print_markdown(md_file)
                else:
                    print(f"Error: Markdown file '{md_file}' not found!", flush=True)
                # Loop back to the confirmation prompt
            else:
                print("Invalid choice. Please enter Y, S, V, or Q.", flush=True)

    return True


def _positive_int(value):
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"invalid int value: '{value}'")
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("--batch must be a positive integer")
    return ivalue


def main(argv=None):
    global MUTATION_DELAY
    parser = argparse.ArgumentParser(
        description="Submit pull requests for Ready packages in export_pages.yaml and extend_pages.yaml."
    )
    parser.add_argument(
        "--review-key",
        required=True,
        help="Review key to check for 'ready' status",
    )
    parser.add_argument(
        "--batch",
        type=_positive_int,
        default=None,
        metavar="N",
        help=(
            "Batch mode: confirm up to N ready packages upfront, then submit "
            "them without further prompts and exit"
        ),
    )
    parser.add_argument(
        "--export-file",
        default="export_pages.yaml",
        help="Path to export_pages.yaml (default: export_pages.yaml)",
    )
    parser.add_argument(
        "--extend-file",
        default="extend_pages.yaml",
        help="Path to extend_pages.yaml (default: extend_pages.yaml)",
    )
    parser.add_argument(
        "--submitted-file",
        default="submitted_pages.yaml",
        help="Path to submitted_pages.yaml (default: submitted_pages.yaml)",
    )
    parser.add_argument(
        "--fork-org",
        default=FORK_ORG,
        help=f"GitHub organization to create forks in (default: {FORK_ORG})",
    )
    parser.add_argument(
        "--mutation-delay",
        type=float,
        default=MUTATION_DELAY,
        help=(
            f"Minimum delay in seconds between mutating GitHub API calls "
            f"(default: {MUTATION_DELAY})"
        ),
    )
    args = parser.parse_args(argv)
    MUTATION_DELAY = max(0.0, args.mutation_delay)

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print(
            "Warning: GITHUB_TOKEN environment variable is not set. "
            "Confirming a submission will fail without GitHub authentication.",
            flush=True,
        )

    try:
        if args.batch is not None:
            process_batch(
                yaml_files=(args.export_file, args.extend_file),
                submitted_file=args.submitted_file,
                review_key=args.review_key,
                batch_size=args.batch,
                fork_org=args.fork_org,
                token=token,
            )
        else:
            for yaml_file in (args.export_file, args.extend_file):
                keep_going = process_yaml_file(
                    yaml_file=yaml_file,
                    submitted_file=args.submitted_file,
                    review_key=args.review_key,
                    fork_org=args.fork_org,
                    token=token,
                )
                if not keep_going:
                    break
    except KeyboardInterrupt:
        print("\nInterrupted by user.", flush=True)


if __name__ == "__main__":
    main()
