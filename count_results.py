import argparse
import collections
import os
import yaml

STANDARD_KEYS = {
    "branch",
    "edited",
    "markdown_file",
    "package_xml_match",
    "readme_exists",
    "repository",
    "repository_archived",
    "source_file",
    "subdirectory",
    "unmatched",
}


def summarize_group_reviews(group_data, review_key=None):
    """Count and summarize review statuses for a dictionary of packages."""
    total_group = len(group_data)
    edited_count = sum(
        1 for info in group_data.values() if info.get("edited") is True
    )

    if review_key:
        review_keys = [review_key]
    else:
        detected_keys = set()
        for info in group_data.values():
            for k in info:
                if k not in STANDARD_KEYS:
                    detected_keys.add(k)
        review_keys = sorted(detected_keys)

    reviews_summary = {}
    for rkey in review_keys:
        counts = collections.Counter()
        unreviewed = 0
        for info in group_data.values():
            if rkey not in info or info[rkey] is None:
                unreviewed += 1
            else:
                counts[str(info[rkey])] += 1

        reviews_summary[rkey] = {
            "ready": counts.pop("ready", 0),
            "ignored": counts.pop("ignored", 0),
            "other": dict(sorted(counts.items())),
            "unreviewed": unreviewed,
        }

    return {
        "total": total_group,
        "edited": edited_count,
        "reviews": reviews_summary,
    }


def print_group_summary(label, summary):
    """Print formatted review status counts for a package grouping."""
    print(f"{label}: {summary['total']}")
    print(f"  Edited: {summary['edited']}")
    if not summary["reviews"]:
        print(f"  Unreviewed: {summary['total']}")
    else:
        for rkey, rcounts in summary["reviews"].items():
            print(f"  Review [{rkey}]:")
            print(f"    Ready: {rcounts['ready']}")
            print(f"    Ignored: {rcounts['ignored']}")
            for other_status, count in rcounts["other"].items():
                print(f"    {other_status}: {count}")
            print(f"    Unreviewed: {rcounts['unreviewed']}")


def count_results(
    current_file="current_pages.yaml",
    export_file="export_pages.yaml",
    extend_file="extend_pages.yaml",
    review_key=None,
):
    with open(current_file, "r") as f:
        data = yaml.safe_load(f) or {}

    total = len(data)
    matched = 0
    unmatched = 0
    archived_count = 0

    export_data = {}
    extend_data = {}

    for k, v in data.items():
        is_unmatched = v.get("unmatched", False)
        is_archived = v.get("repository_archived", False)

        if is_unmatched:
            unmatched += 1
        elif "repository" in v:
            matched += 1
            if is_archived:
                archived_count += 1

        # Apply filter for lists: must be matched and not archived
        if not is_unmatched and not is_archived:
            if v.get("readme_exists") is True:
                extend_data[k] = dict(v)
            else:
                export_data[k] = dict(v)

    # Overlay review status from export_pages.yaml and extend_pages.yaml if present
    if export_file and os.path.exists(export_file):
        with open(export_file, "r") as f:
            disk_export = yaml.safe_load(f) or {}
        for k, v in disk_export.items():
            if k in export_data and isinstance(v, dict):
                export_data[k].update(v)
            elif isinstance(v, dict):
                export_data[k] = dict(v)

    if extend_file and os.path.exists(extend_file):
        with open(extend_file, "r") as f:
            disk_extend = yaml.safe_load(f) or {}
        for k, v in disk_extend.items():
            if k in extend_data and isinstance(v, dict):
                extend_data[k].update(v)
            elif isinstance(v, dict):
                extend_data[k] = dict(v)

    export_summary = summarize_group_reviews(export_data, review_key=review_key)
    extend_summary = summarize_group_reviews(extend_data, review_key=review_key)

    print(f"Total packages: {total}")
    print(f"Matched: {matched}")
    print(f"Unmatched: {unmatched}")
    print(f"Archived (among matched): {archived_count}")
    print_group_summary("Exported (no README)", export_summary)
    print_group_summary("Extended (has README)", extend_summary)

    return {
        "total": total,
        "matched": matched,
        "unmatched": unmatched,
        "archived": archived_count,
        "exported": export_summary,
        "extended": extend_summary,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Count and summarize package correlation and review status."
    )
    parser.add_argument(
        "--review-key",
        default=None,
        help="Optional review key to summarize (auto-detects all review keys if omitted)",
    )
    parser.add_argument(
        "--current-file",
        default="current_pages.yaml",
        help="Path to current_pages.yaml (default: current_pages.yaml)",
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
    args = parser.parse_args()

    count_results(
        current_file=args.current_file,
        export_file=args.export_file,
        extend_file=args.extend_file,
        review_key=args.review_key,
    )


if __name__ == "__main__":
    main()
