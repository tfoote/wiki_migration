import argparse
import os
import subprocess
import sys
import yaml


PREVIEW_LINES = 25
HEADER_BAR = "=" * 20
TRUNCATE_BAR = "V" * 20


def print_markdown(md_file, max_lines=None):
    """Print markdown content between matching headers, optionally truncated."""
    with open(md_file, "r", encoding="utf-8") as f_md:
        lines = f_md.readlines()

    label = "Markdown Preview" if max_lines is not None else "Markdown Full View"
    print(f"{HEADER_BAR} BEGIN {label}: {md_file} {HEADER_BAR}", flush=True)
    shown = lines if max_lines is None else lines[:max_lines]
    for line in shown:
        print(line.rstrip(), flush=True)
    remaining = len(lines) - len(shown)
    if remaining > 0:
        print(
            f"{TRUNCATE_BAR} Truncated {remaining} Lines {TRUNCATE_BAR}",
            flush=True,
        )
    print(f"{HEADER_BAR}  END  {label}: {md_file} {HEADER_BAR}", flush=True)


def main():
    parser = argparse.ArgumentParser(
        description="Review and edit export pages."
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        default="export_pages.yaml",
        help="Input YAML file (default: export_pages.yaml)",
    )
    parser.add_argument(
        "--review-key", required=True, help="Key to record review status under"
    )
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Error: File {args.input_file} not found.", flush=True)
        sys.exit(1)

    with open(args.input_file, "r") as f:
        data = yaml.safe_load(f)

    if not data:
        print("No data in YAML file.", flush=True)
        return

    updated = False
    editor = os.environ.get("EDITOR", "nano")

    try:
        for package, info in data.items():
            # Skip if review key already exists
            if args.review_key in info:
                print(
                    f"Skipping {package} (already processed for {args.review_key})",
                    flush=True,
                )
                continue

            repo = info.get("repository")
            branch = info.get("branch")
            subdir = info.get("subdirectory")
            md_file = info.get("markdown_file")

            show_details = True
            while True:
                if show_details:
                    print("\n" + "=" * 40, flush=True)
                    print(f"Package: {package}", flush=True)
                    print(f"Repository: {repo}", flush=True)
                    print(f"Branch: {branch}", flush=True)
                    print(f"Relative Path: {subdir}", flush=True)
                    print("-" * 20, flush=True)

                    if md_file and os.path.exists(md_file):
                        print_markdown(md_file, max_lines=PREVIEW_LINES)
                    else:
                        print(
                            f"Warning: Markdown file {md_file} not found or not specified.",
                            flush=True,
                        )
                show_details = True

                print(
                    "\nAction: [R]eady / [S]kip / [I]gnore / [E]dit / [V]iew All / [Q]uit: ",
                    end="",
                    flush=True,
                )
                choice = sys.stdin.readline().strip().upper()

                if choice == "Q":
                    print("Quitting.", flush=True)
                    raise StopIteration  # Easy way to break out of outer loop too
                elif choice == "S":
                    print("Skipping.", flush=True)
                    break
                elif choice == "I":
                    print(f"Ignoring {package}.", flush=True)
                    info[args.review_key] = "ignored"
                    updated = True
                    break
                elif choice == "R":
                    print(f"Marking {package} as ready.", flush=True)
                    info[args.review_key] = "ready"
                    updated = True
                    break
                elif choice == "E":
                    print(f"Opening editor {editor} for {md_file}...", flush=True)
                    if md_file and os.path.exists(md_file):
                        result = subprocess.call([editor, md_file])
                        if result == 0:
                            print("Editor returned successfully.", flush=True)
                            info["edited"] = True
                            updated = True
                        else:
                            print(
                                f"Editor returned non-zero exit code: {result}",
                                flush=True,
                            )
                    else:
                        print("Error: Markdown file not found.", flush=True)
                    # Continue in the loop to show preview and prompt again
                elif choice == "V":
                    if md_file and os.path.exists(md_file):
                        print(flush=True)
                        print_markdown(md_file)
                    else:
                        print("Error: Markdown file not found.", flush=True)
                    # Return directly to the Action prompt
                    show_details = False
                else:
                    print(
                        "Invalid choice. Please choose R, S, I, E, V, or Q.",
                        flush=True,
                    )

    except StopIteration:
        pass
    except KeyboardInterrupt:
        print("\nInterrupted by user.", flush=True)

    if updated:
        print(f"\nSaving updates to {args.input_file}...", flush=True)
        with open(args.input_file, "w") as f:
            yaml.dump(data, f, default_flow_style=False)
        print("Saved.", flush=True)
    else:
        print("\nNo updates to save.", flush=True)


if __name__ == "__main__":
    main()
