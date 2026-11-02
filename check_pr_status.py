"""Check the status of submitted wiki-migration pull requests.

Reads submitted_pages.yaml, queries GitHub for every recorded PR (the main
`pr_url` and, if present, the `default_branch_pr_url`), prints a listing and
a summary.

Usage:
    python3 check_pr_status.py [--submitted-file submitted_pages.yaml] [--json]

Set GITHUB_TOKEN for higher API rate limits (read-only access is enough).
"""
import argparse
import datetime
import json
import os
import re
import sys
import urllib.error
from collections import Counter

import yaml

from submit_prs import github_api_request

PR_URL = re.compile(r"https://github\.com/([^/]+)/([^/]+)/pull/(\d+)")


def parse_pr_url(url):
    m = PR_URL.match(url or "")
    if not m:
        raise ValueError(f"Not a GitHub pull request URL: {url}")
    return m.group(1), m.group(2), int(m.group(3))


def latest_review_state(reviews):
    """Most recent decisive review per reviewer, then the overall verdict."""
    per_user = {}
    for r in reviews:
        state = r.get("state")
        user = (r.get("user") or {}).get("login")
        if state in ("APPROVED", "CHANGES_REQUESTED"):
            per_user[user] = state
        elif state == "COMMENTED":
            per_user.setdefault(user, state)
    states = set(per_user.values())
    if "CHANGES_REQUESTED" in states:
        return "CHANGES_REQUESTED"
    if "APPROVED" in states:
        return "APPROVED"
    if "COMMENTED" in states:
        return "COMMENTED"
    return ""


def fetch_pr_status(url, token=None):
    owner, repo, number = parse_pr_url(url)
    api = f"https://api.github.com/repos/{owner}/{repo}/pulls/{number}"
    pr = github_api_request(api, token=token)
    try:
        reviews = github_api_request(f"{api}/reviews?per_page=100", token=token)
    except urllib.error.HTTPError:
        reviews = []
    if pr.get("merged_at"):
        state = "MERGED"
    elif pr.get("state") == "closed":
        state = "CLOSED"
    elif pr.get("draft"):
        state = "DRAFT"
    else:
        state = "OPEN"
    return {
        "url": url,
        "repo": f"{owner}/{repo}",
        "number": number,
        "state": state,
        "review": latest_review_state(reviews if isinstance(reviews, list) else []),
        "comments": int(pr.get("comments", 0)) + int(pr.get("review_comments", 0)),
        "base": (pr.get("base") or {}).get("ref", ""),
        "created_at": pr.get("created_at", ""),
        "updated_at": pr.get("updated_at", ""),
        "closed_at": pr.get("merged_at") or pr.get("closed_at") or "",
        "merged_by": (pr.get("merged_by") or {}).get("login", ""),
    }


def days_since(timestamp, now=None):
    if not timestamp:
        return None
    now = now or datetime.datetime.now(datetime.timezone.utc)
    then = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=datetime.timezone.utc)
    return (now - then).days


def collect(submitted, token=None):
    """Return a list of status rows, one per PR."""
    rows = []
    for package, info in sorted(submitted.items()):
        for kind, key in (("main", "pr_url"), ("default-branch", "default_branch_pr_url")):
            url = info.get(key)
            if not url:
                continue
            row = {"package": package, "kind": kind, "queue": info.get("source_queue", "")}
            try:
                row.update(fetch_pr_status(url, token))
            except (ValueError, urllib.error.HTTPError, urllib.error.URLError) as e:
                row.update({"url": url, "state": "ERROR", "error": str(e)})
            rows.append(row)
    return rows


def print_listing(rows, out=None):
    out = out or sys.stdout
    headers = ["Package", "PR", "Base", "State", "Review", "Cmts", "Age", "Idle"]
    table = []
    for r in rows:
        if r["state"] == "ERROR":
            table.append([r["package"], r["url"], "", "ERROR", r.get("error", "")[:40], "", "", ""])
            continue
        age = days_since(r["created_at"])
        idle = days_since(r["closed_at"] or r["updated_at"])
        table.append([
            r["package"] + (" (default)" if r["kind"] == "default-branch" else ""),
            f"{r['repo']}#{r['number']}",
            r["base"],
            r["state"],
            r["review"].replace("_", " ").lower() or "-",
            str(r["comments"]),
            f"{age}d" if age is not None else "",
            f"{idle}d" if idle is not None else "",
        ])
    widths = [max(len(h), *(len(row[i]) for row in table)) if table else len(h)
              for i, h in enumerate(headers)]
    fmt = "  ".join(f"{{:<{w}}}" for w in widths)
    print(fmt.format(*headers), file=out)
    print(fmt.format(*("-" * w for w in widths)), file=out)
    for row in table:
        print(fmt.format(*row), file=out)
    print("\nAge = days since opened; Idle = days since last update (or since merge/close).",
          file=out)


def print_summary(rows, submitted, out=None):
    out = out or sys.stdout
    ok = [r for r in rows if r["state"] != "ERROR"]
    states = Counter(r["state"] for r in ok)
    total = len(ok)
    print("\nSummary", file=out)
    print("=======", file=out)
    print(f"Packages submitted:   {len(submitted)}", file=out)
    print(f"Pull requests:        {len(rows)}"
          + (f" ({len(rows) - total} could not be checked)" if len(rows) != total else ""),
          file=out)
    for state in ("MERGED", "OPEN", "DRAFT", "CLOSED"):
        n = states.get(state, 0)
        pct = f" ({100 * n / total:.0f}%)" if total else ""
        print(f"  {state.capitalize() + ':':<20}{n}{pct}", file=out)

    by_pkg = {}
    for r in ok:
        by_pkg.setdefault(r["package"], []).append(r["state"])
    merged_pkgs = sorted(p for p, s in by_pkg.items() if "MERGED" in s)
    closed_pkgs = sorted(p for p, s in by_pkg.items() if s and all(x == "CLOSED" for x in s))
    print(f"Packages with a merged PR:          {len(merged_pkgs)}", file=out)
    print(f"Packages with all PRs closed (won't fix): {len(closed_pkgs)}"
          + (f": {', '.join(closed_pkgs)}" if closed_pkgs else ""), file=out)

    attention = [r for r in ok if r["state"] in ("OPEN", "DRAFT")
                 and r["review"] == "CHANGES_REQUESTED"]
    discussed = [r for r in ok if r["state"] in ("OPEN", "DRAFT") and r["comments"]
                 and r["review"] != "CHANGES_REQUESTED"]
    if attention:
        print("Changes requested (open):", file=out)
        for r in attention:
            print(f"  {r['package']}: {r['url']}", file=out)
    if discussed:
        print("Open with comments:", file=out)
        for r in discussed:
            print(f"  {r['package']}: {r['url']} ({r['comments']} comments)", file=out)
    open_rows = [r for r in ok if r["state"] in ("OPEN", "DRAFT")]
    if open_rows:
        oldest = max(open_rows, key=lambda r: days_since(r["created_at"]) or 0)
        print(f"Oldest open PR: {oldest['package']} "
              f"({days_since(oldest['created_at'])}d) {oldest['url']}", file=out)
    errors = [r for r in rows if r["state"] == "ERROR"]
    if errors:
        print("Could not check:", file=out)
        for r in errors:
            print(f"  {r['package']}: {r['url']} ({r.get('error', '')})", file=out)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--submitted-file", default="submitted_pages.yaml")
    parser.add_argument("--json", action="store_true", help="Print rows as JSON instead of a table.")
    args = parser.parse_args(argv)

    if not os.path.exists(args.submitted_file):
        print(f"Error: {args.submitted_file} not found.")
        return 1
    with open(args.submitted_file, "r", encoding="utf-8") as f:
        submitted = yaml.safe_load(f) or {}
    if not submitted:
        print("No submitted packages.")
        return 0

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Note: GITHUB_TOKEN not set; using unauthenticated GitHub API "
              "requests (60/hour).", file=sys.stderr)

    rows = collect(submitted, token)
    if args.json:
        print(json.dumps(rows, indent=1))
    else:
        print_listing(rows)
        print_summary(rows, submitted)
    return 0


if __name__ == "__main__":
    sys.exit(main())
