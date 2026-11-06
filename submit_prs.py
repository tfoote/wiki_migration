import argparse
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import yaml

from review_packages import PREVIEW_LINES, print_markdown

FORK_ORG = "tfoote-ros-wiki-migration-forks"


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


def github_api_request(url, method="GET", data=None, token=None, accept_statuses=(200, 201, 202)):
    """Perform a GitHub REST API request with rate-limit handling."""
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

    while True:
        req = urllib.request.Request(url, data=body_bytes, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req) as response:
                resp_body = response.read().decode("utf-8")
                if response.status in accept_statuses:
                    return json.loads(resp_body) if resp_body else {}
                raise RuntimeError(f"Unexpected status {response.status} from {url}")
        except urllib.error.HTTPError as e:
            if e.code in (403, 429):
                reset_time = e.headers.get("X-RateLimit-Reset")
                if reset_time:
                    sleep_time = int(reset_time) - time.time() + 5
                    if sleep_time > 0:
                        print(f"  Rate limit hit. Sleeping for {sleep_time:.1f}s...", flush=True)
                        time.sleep(sleep_time)
                        continue
            # Include GitHub's explanation (e.g. "Validation Failed: ...") in
            # the error, otherwise a 422 is impossible to diagnose.
            try:
                detail = json.loads(e.read().decode("utf-8") or "{}")
                parts = [detail.get("message", "")]
                parts += [err.get("message") or json.dumps(err)
                          for err in detail.get("errors", []) if isinstance(err, dict)]
                message = "; ".join(p for p in parts if p)
                if message:
                    e.msg = f"{e.msg}: {message} ({method} {url})"
            except Exception:
                pass
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

                # Load existing submitted_pages.yaml
                submitted_data = {}
                if os.path.exists(submitted_file):
                    with open(submitted_file, "r", encoding="utf-8") as f_sub:
                        submitted_data = yaml.safe_load(f_sub) or {}

                # Record entry in submitted_pages.yaml and remove from source yaml_file
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


def main():
    parser = argparse.ArgumentParser(
        description="Submit pull requests for Ready packages in export_pages.yaml and extend_pages.yaml."
    )
    parser.add_argument(
        "--review-key",
        required=True,
        help="Review key to check for 'ready' status",
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
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print(
            "Warning: GITHUB_TOKEN environment variable is not set. "
            "Confirming a submission will fail without GitHub authentication.",
            flush=True,
        )

    try:
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
