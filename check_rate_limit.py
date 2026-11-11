"""Check GitHub API rate-limit quota and reset times for GITHUB_TOKEN.

Queries https://api.github.com/rate_limit (which does not consume any quota)
and prints remaining/total requests and reset countdowns per resource bucket.

Usage:
    python3 check_rate_limit.py [--all] [--json]
"""
import argparse
import datetime
import json
import os
import sys
import time
import urllib.error
import urllib.request

RATE_LIMIT_URL = "https://api.github.com/rate_limit"
PRIMARY_BUCKETS = ("core", "graphql", "search")


def fetch_rate_limit(token=None, url=RATE_LIMIT_URL):
    """Query GitHub's /rate_limit endpoint and return (payload_dict, headers_dict)."""
    if token is None:
        token = os.environ.get("GITHUB_TOKEN")

    headers = {
        "User-Agent": "ros-wiki-migration",
        "Accept": "application/vnd.github+json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(url, headers=headers, method="GET")
    with urllib.request.urlopen(req) as resp:
        body = json.loads(resp.read().decode("utf-8"))
        resp_headers = {k.lower(): v for k, v in resp.headers.items()}
    return body, resp_headers, bool(token)


def format_duration(seconds):
    """Format a delta in seconds as a compact human-readable countdown."""
    seconds = int(round(seconds))
    if seconds <= 0:
        return "now"
    hours, rem = divmod(seconds, 3600)
    minutes, secs = divmod(rem, 60)
    if hours > 0:
        return f"in {hours}h {minutes:02d}m {secs:02d}s"
    if minutes > 0:
        return f"in {minutes}m {secs:02d}s"
    return f"in {secs}s"


def format_timestamp(epoch_seconds, tz=None):
    """Format a Unix epoch timestamp in the local timezone (or given tz)."""
    dt = datetime.datetime.fromtimestamp(epoch_seconds, tz=datetime.timezone.utc)
    dt_local = dt.astimezone(tz)
    return dt_local.strftime("%Y-%m-%d %H:%M:%S %Z")


def select_buckets(resources, show_all=False):
    """Return ordered (name, info) pairs to display."""
    ordered = []
    seen = set()
    for name in PRIMARY_BUCKETS:
        if name in resources:
            ordered.append((name, resources[name]))
            seen.add(name)
    for name, info in sorted(resources.items()):
        if name in seen or not isinstance(info, dict):
            continue
        used = int(info.get("used", 0) or 0)
        remaining = int(info.get("remaining", 0) or 0)
        limit = int(info.get("limit", 0) or 0)
        if show_all or used > 0 or remaining < limit:
            ordered.append((name, info))
    return ordered


def print_report(payload, headers, authenticated, show_all=False, now=None, tz=None, out=sys.stdout):
    """Print a human-readable summary of token quota and reset times."""
    if now is None:
        now = time.time()

    if authenticated:
        print("Auth:          Authenticated (GITHUB_TOKEN)", file=out)
    else:
        print("Auth:          Unauthenticated (GITHUB_TOKEN not set; 60/hr IP limit)", file=out)

    scopes = headers.get("x-oauth-scopes")
    if scopes is not None:
        print(f"Token scopes:  {scopes or '(none)'}", file=out)

    expiration = headers.get("github-authentication-token-expiration")
    if expiration:
        print(f"Token expires: {expiration}", file=out)

    print(file=out)

    resources = payload.get("resources") or {}
    if not resources and "rate" in payload:
        resources = {"core": payload["rate"]}

    buckets = select_buckets(resources, show_all=show_all)
    header_line = (
        f"{'Resource':<26} {'Remaining / Limit':<22} {'Used':>6}   "
        f"{'Resets At':<25} {'Refresh'}"
    )
    print(header_line, file=out)
    print("-" * len(header_line), file=out)

    for name, info in buckets:
        limit = int(info.get("limit", 0) or 0)
        remaining = int(info.get("remaining", 0) or 0)
        used = int(info.get("used", max(0, limit - remaining)) or 0)
        reset_epoch = int(info.get("reset", 0) or 0)
        pct = f"({round(100 * remaining / limit)}%)" if limit else ""
        rem_str = f"{remaining} / {limit} {pct}".strip()
        reset_at = format_timestamp(reset_epoch, tz=tz) if reset_epoch else "n/a"
        refresh = format_duration(reset_epoch - now) if reset_epoch else "n/a"
        print(
            f"{name:<26} {rem_str:<22} {used:>6}   {reset_at:<25} {refresh}",
            file=out,
        )

    core = resources.get("core") or payload.get("rate") or {}
    core_remaining = int(core.get("remaining", 0) or 0)
    if authenticated and core_remaining > 0:
        print(
            "\nNote: If PR or fork creation is still throttled (HTTP 403/429) while "
            "'core' has quota remaining,\nGitHub is enforcing a secondary "
            "content-creation rate limit (~80 content requests/min, ~500/hr,\nor "
            "per-account PR creation burst caps), which is not reported by /rate_limit.",
            file=out,
        )


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Check GitHub API rate-limit quota and reset times."
    )
    parser.add_argument(
        "--token",
        default=None,
        help="GitHub token (defaults to GITHUB_TOKEN environment variable)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Show all rate-limit resource buckets, including unused ones",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print raw JSON output with computed reset metadata",
    )
    args = parser.parse_args(argv)

    try:
        payload, headers, authenticated = fetch_rate_limit(token=args.token)
    except urllib.error.HTTPError as e:
        detail = ""
        try:
            msg = json.loads(e.read().decode("utf-8") or "{}").get("message", "")
            if msg:
                detail = f": {msg}"
        except Exception:
            pass
        print(f"GitHub API error ({e.code} {e.reason}){detail}", file=sys.stderr)
        return 1
    except urllib.error.URLError as e:
        print(f"Network error contacting GitHub API: {e.reason}", file=sys.stderr)
        return 1

    if args.json:
        now = time.time()
        output = {
            "authenticated": authenticated,
            "scopes": headers.get("x-oauth-scopes"),
            "token_expiration": headers.get("github-authentication-token-expiration"),
            "checked_at": int(now),
            "resources": payload.get("resources", {}),
        }
        print(json.dumps(output, indent=2))
        return 0

    print_report(payload, headers, authenticated, show_all=args.all)
    return 0


if __name__ == "__main__":
    sys.exit(main())
