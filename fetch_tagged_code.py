"""Download the source files referenced by <<GetTaggedCode(...)>> macros.

Scans every page exported from export_pages.yaml / extend_pages.yaml
(including appended subpages and included pages) and saves each referenced
file into tagged_code_cache/ so convert_to_markdown.py can embed the tagged
snippets offline. Requires network access.

Usage:
    python3 fetch_tagged_code.py [--force]
"""
import argparse
import contextlib
import io
import os
import re
import sys
import urllib.request

import yaml

import convert_to_markdown as ctm


def referenced_urls():
    """Collect GetTaggedCode URLs from all exported pages."""
    urls = set()
    for queue in ctm.queue_files:
        for pkg, info in ctm.load_yaml(queue).items():
            src = info.get("source_file")
            if not src or not os.path.exists(src):
                continue
            stats = {}
            with contextlib.redirect_stdout(io.StringIO()):
                ctm.convert_file(src, stats=stats)
            for page in [pkg] + stats["subpages"]:
                text = ctm.read_page(page) or ""
                # include pages pulled in via <<Include>> as well
                for inc in re.findall(r"<<Include\(([^,)]+)", text):
                    text += ctm.read_page(ctm.resolve_page_name(inc.strip(), page)) or ""
                for args in ctm._GET_TAGGED_CODE.findall(text):
                    url = ctm.parse_get_tagged_code(args)[0]
                    if url:
                        urls.add(url)
    return sorted(urls)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--force", action="store_true", help="Re-download cached files.")
    args = parser.parse_args()

    urls = referenced_urls()
    print(f"Found {len(urls)} referenced source file(s).")
    failed = []
    for url in urls:
        path = ctm.tagged_code_cache_path(url)
        if os.path.exists(path) and not args.force:
            print(f"  cached   {url}")
            continue
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ros-wiki-migration"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
        except Exception as e:
            print(f"  FAILED   {url}: {e}")
            failed.append(url)
            continue
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(data)
        print(f"  fetched  {url} -> {path}")
    if failed:
        print(f"{len(failed)} file(s) could not be fetched; those macros will "
              "become links to the source.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
