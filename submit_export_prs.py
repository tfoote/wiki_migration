import argparse
import os
import sys
import yaml


def create_pr(repo, branch, subdirectory, content):
    # Stub implementation
    print(f"[STUB] Creating PR for {repo} on branch {branch} path {subdirectory}", flush=True)
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Submit export PRs or ignore packages."
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        default="export_pages.yaml",
        help="Input YAML file (default: export_pages.yaml)",
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
    try:
        for package, info in data.items():
            if info.get("submitted") or info.get("ignored"):
                print(f"Skipping {package} (already processed)", flush=True)
                continue

            repo = info.get("repository")
            branch = info.get("branch")
            subdir = info.get("subdirectory")
            md_file = info.get("markdown_file")

            print("\n" + "=" * 40, flush=True)
            print(f"Package: {package}", flush=True)
            print(f"Repository: {repo}", flush=True)
            print(f"Branch: {branch}", flush=True)
            print(f"Relative Path: {subdir}", flush=True)
            print("-" * 20, flush=True)

            if md_file and os.path.exists(md_file):
                print(f"Markdown Preview ({md_file}):", flush=True)
                with open(md_file, "r") as f_md:
                    # Preview first 10 lines
                    lines = f_md.readlines()
                    for line in lines[:10]:
                        print(line.rstrip(), flush=True)
                    if len(lines) > 10:
                        print("...", flush=True)
            else:
                print(
                    f"Warning: Markdown file {md_file} not found or not specified.",
                    flush=True,
                )

            print("=" * 40, flush=True)

            while True:
                print("\nAction: [P]roceed / [S]kip / [I]gnore / [Q]uit: ", end="", flush=True)
                choice = sys.stdin.readline().strip().upper()
                if choice in ["P", "S", "I", "Q"]:
                    break
                print("Invalid choice. Please choose P, S, I, or Q.", flush=True)

            if choice == "Q":
                print("Quitting.", flush=True)
                break
            elif choice == "S":
                print("Skipping.", flush=True)
                continue
            elif choice == "I":
                print(f"Ignoring {package}.", flush=True)
                info["ignored"] = True
                updated = True
            elif choice == "P":
                print(f"Proceeding with PR for {package}.", flush=True)
                if create_pr(repo, branch, subdir, ""):
                    print("PR submitted successfully.", flush=True)
                    info["submitted"] = True
                    updated = True
                else:
                    print("Failed to submit PR.", flush=True)

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
