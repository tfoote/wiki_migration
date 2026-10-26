import argparse
import os
import re
import subprocess
import yaml

# Legacy bootstrap input: only used if none of the review queues exist.
input_file = "current_pages.yaml"
# Review queues: once these exist, only their entries are (re)converted.
queue_files = ["export_pages.yaml", "extend_pages.yaml"]
submitted_file = "submitted_pages.yaml"
output_dir = "markdown_output"


_UNSAFE_FS_CHARS = re.compile(rb"[^a-zA-Z0-9_]+")


def quote_wikiname_fs(wikiname):
    """Convert a wiki page name to its MoinMoin on-disk directory name.

    Mirrors MoinMoin's wikiutil.quoteWikinameFS: each run of characters other
    than [a-zA-Z0-9_] is hex-encoded in parentheses, e.g.
    "bond/Overview" -> "bond(2f)Overview", "a-b.c" -> "a(2d)b(2e)c",
    "Udev Rules" -> "Udev(20)Rules".
    """
    raw = wikiname.encode("utf-8")
    quoted = []
    location = 0
    for needle in _UNSAFE_FS_CHARS.finditer(raw):
        quoted.append(raw[location:needle.start()].decode("ascii"))
        quoted.append("(" + needle.group().hex() + ")")
        location = needle.end()
    quoted.append(raw[location:].decode("ascii"))
    return "".join(quoted)


def unquote_wikiname_fs(filename):
    """Inverse of quote_wikiname_fs (underscores are left as-is)."""
    return re.sub(
        r"\(([0-9a-fA-F]+)\)",
        lambda m: bytes.fromhex(m.group(1)).decode("utf-8", errors="ignore"),
        filename,
    )


def resolve_page_name(target, current_page=None):
    """Resolve relative MoinMoin page references ("/Sub", "../Sibling")."""
    if current_page:
        if target.startswith("/"):
            return current_page + target
        if target.startswith("../"):
            parts = current_page.split("/")
            while target.startswith("../"):
                target = target[3:]
                parts = parts[:-1]
            return "/".join(parts + [target]) if parts else target
    return target.lstrip("/")


def filter_versions(content):
    """Drop version sections unless they end in _and_newer or are noetic."""

    def version_repl(match):
        version_line = match.group(1)
        if version_line.endswith("_and_newer") or "noetic" in version_line:
            return match.group(0)  # Keep for Pandoc
        else:
            return ""  # Drop

    return re.sub(
        r"\{\{\{\#\!wiki\s+version\s+([^\n]+)\n(.*?)\n\}\}\}",
        version_repl,
        content,
        flags=re.DOTALL,
    )


def preprocess(content, current_page=None):
    # 0. Handle <<Include(arg)>> recursively (Moved to first step)
    def resolve_include(content, depth=0, max_depth=5, current_page=None):
        if depth > max_depth:
            print(f"Warning: Max include depth reached ({max_depth}).")
            return content

        def include_repl(match):
            # Only the first argument is the page name; further arguments
            # (heading, level, from=, to=, ...) are ignored.
            page_name = match.group(1).split(",")[0].strip().strip("\"'")
            if not page_name:
                return ""
            page_name = resolve_page_name(page_name, current_page)
            pages_dir = "pages"
            page_dir = os.path.join(pages_dir, quote_wikiname_fs(page_name))
            if not os.path.exists(os.path.join(page_dir, "current")):
                # Fall back to the literal name for already-encoded references.
                literal_dir = os.path.join(pages_dir, page_name)
                if os.path.exists(os.path.join(literal_dir, "current")):
                    page_dir = literal_dir
            current_file = os.path.join(page_dir, "current")

            if os.path.exists(current_file):
                with open(current_file, "r") as f:
                    revision = f.read().strip()
                revision_file = os.path.join(page_dir, "revisions", revision)
                if os.path.exists(revision_file):
                    with open(revision_file, "r", errors="ignore") as f_rev:
                        included_content = f_rev.read()
                        # Recursively resolve includes in the included content
                        return resolve_include(
                            included_content, depth + 1, current_page=page_name
                        )
                else:
                    print(f"Warning: Revision file {revision_file} not found.")
                    return f"[[Included page {page_name} not found (missing revision)]]"
            else:
                print(f"Warning: Current file {current_file} not found.")
                return f"[[Included page {page_name} not found]]"

        return re.sub(r"<<Include\(([^)]+)\)>>", include_repl, filter_versions(content))

    # Version sections are filtered per page (top-level and each included
    # page) *before* includes are expanded, so that code blocks pulled in from
    # included pages can't confuse the version-block regex.
    content = resolve_include(content, current_page=current_page)

    # Convert CRLF to LF
    content = content.replace("\r\n", "\n")

    # Append }}} if unclosed multiline code block at end of file
    if content.count("{{{") > content.count("}}}"):
        content += "\n}}}"

    # Remove MoinMoin comments (lines starting with ##)
    lines = content.split("\n")
    lines = [l for l in lines if not l.strip().startswith("##")]
    content = "\n".join(lines)

    # Extract multiline code blocks and replace with placeholders
    code_blocks = []

    def code_block_repl(match):
        code_blocks.append(match.group(1))
        return f"PLACEHOLDER_CODE_BLOCK_{len(code_blocks)-1}"

    # Match {{{ ... }}} where it's NOT inline (i.e. not followed by }}} on same line)
    content = re.sub(
        r"\{\{\{(?![^\n]*\}\}\})(.*?)\}\}\}", code_block_repl, content, flags=re.DOTALL,
    )

    # 3. Omit specified WikiMacros
    macros_to_omit = [
        "PackageHeader",
        "TOC",
        "StackHeader",
        "TableOfContents",
        "Version",
        "TracLink",
        "MenuNavi",
        "ManuNavi",
        "Buildsystem",
        "AnswersSearch",
        "Hits",
        "GitHubIssues",
        "KforgeTracLink",
        "FullSearch",
        "FullSearchWithDescriptionsCS",
        "Markdown",
        "CodeRef",
        "MsgSrvDoc",
        "MiniPage",
        "urdf_file",
        "NewPage",
        "RepoHeader",
        "sensor_source_package",
        "fusion_node",
        "move_base_navigation_stack",
        "FootNote",
        "Ticket",
        "Anchor",
    ]

    macros_regex = "|".join(macros_to_omit)
    pattern = re.compile(r"#?\s*<<(" + macros_regex + r")(\(.*\))?>>")
    content = pattern.sub("", content)

    # 4. Convert <<BR>> to \\
    content = content.replace("<<BR>>", "\\\\")

    # 5. Remove lines containing AUTOGENERATED or CategoryPackage
    lines = content.split("\n")
    lines = [l for l in lines if "AUTOGENERATED" not in l and "CategoryPackage" not in l]
    content = "\n".join(lines)

    # 6. Convert <<Youtube(video_id)>> to [[https://www.youtube.com/watch?v=video_id|Youtube]]
    content = re.sub(
        r"<<Youtube\((.*?)\)>>",
        r"[[https://www.youtube.com/watch?v=\1|Youtube]]",
        content,
    )

    # Convert <<MsgLink(package/Message)>> or <<SrvLink(package/Service)>> to Creole link
    def link_repl(match):
        macro_type = match.group(1)
        args = match.group(2)
        parts = args.split("/")
        if len(parts) == 2:
            pkg, name = parts
            type_str = "msg" if macro_type == "MsgLink" else "srv"
            return f"[[https://docs.ros.org/en/rolling/p/{pkg}/{type_str}/{name}.html|{pkg}/{type_str}/{name}]]"
        return match.group(0)

    content = re.sub(r"<<(MsgLink|SrvLink)\(([^)]+)\)>>", link_repl, content)

    # Handle MoinMoin 4-quote bold monospace
    content = re.sub(r"''''(.*?)''''", r"**{{{\1}}}**", content)

    # Handle MoinMoin 5-quote combined tags
    content = re.sub(r"'''''(.*?)'''(.*?)''", r"//**\1**\2//", content)
    content = re.sub(r"'''''(.*?)''(.*?)'''", r"**//\1//\2**", content)

    # Convert MoinMoin bold ''' to Creole **
    content = re.sub(r"'''(.*?)'''", r"**\1**", content)

    # Convert MoinMoin italic '' to Creole //
    content = re.sub(r"''(.*?)''", r"//\1//", content)

    return content, code_blocks




def postprocess(content, code_blocks):
    # Remove unnecessary backslashes before quotes in text
    content = content.replace(r"\'", "'")
    content = content.replace(r'\"', '"')
    content = content.replace(r"\_", "_")
    content = content.replace(r"\`", "`")
    content = content.replace(r"\<", "<")
    content = content.replace(r"\>", ">")

    # Restore code blocks from placeholders
    for i, block in enumerate(code_blocks):
        placeholder = f"PLACEHOLDER_CODE_BLOCK_{i}"
        # Pandoc might escape underscores! So we check for both!
        escaped_placeholder = placeholder.replace("_", r"\_")
        
        # We want to convert it to a fenced code block in Markdown!
        # If the block starts with #!, we can use it as language!
        lines = block.strip().split("\n")
        if lines and lines[0].startswith("#!"):
            lang = lines[0][2:].strip().split()[0]
            body = "\n".join(lines[1:])
            replacement = f"\n\n```{lang}\n{body}\n```\n\n"
        else:
            replacement = f"\n\n```\n{block.strip()}\n```\n\n"
            
        # Replace in content!
        content = content.replace(placeholder, replacement)
        content = content.replace(escaped_placeholder, replacement)

    # Rest of postprocess
    lines = content.split("\n")
    new_lines = []
    in_indented_block = False
    block_lines = []

    for line in lines:
        if line.startswith("    "):
            in_indented_block = True
            block_lines.append(line[4:])
        else:
            if in_indented_block:
                if block_lines and block_lines[0].startswith("#!"):
                    header = block_lines[0].strip()
                    if header.startswith("#!wiki version"):
                        body = block_lines[1:]
                        new_lines.extend(body)
                    elif header.startswith("#!wiki buildsystem"):
                        body = block_lines[1:]
                        new_lines.extend(body)
                    elif header.startswith("#!wiki"):
                        body = block_lines[1:]
                        quoted_body = [f"> {l}" for l in body]
                        new_lines.extend(quoted_body)
                    else:
                        lang = header[2:].strip().split()[0]
                        body = block_lines[1:]
                        new_lines.append(f"```{lang}")
                        new_lines.extend(body)
                        new_lines.append("```")
                else:
                    new_lines.extend([f"    {l}" for l in block_lines])

                in_indented_block = False
                block_lines = []

            new_lines.append(line)

    if in_indented_block:
        if block_lines and block_lines[0].startswith("#!"):
            header = block_lines[0].strip()
            if header.startswith("#!wiki version"):
                body = block_lines[1:]
                new_lines.extend(body)
            elif header.startswith("#!wiki buildsystem"):
                body = block_lines[1:]
                new_lines.extend(body)
            elif header.startswith("#!wiki"):
                body = block_lines[1:]
                quoted_body = [f"> {l}" for l in body]
                new_lines.extend(quoted_body)
            else:
                lang = header[2:].strip().split()[0]
                body = block_lines[1:]
                new_lines.append(f"```{lang}")
                new_lines.extend(body)
                new_lines.append("```")
        else:
            new_lines.extend([f"    {l}" for l in block_lines])

    return "\n".join(new_lines)


def convert_file(src_file):
    """Convert a MoinMoin revision file to Markdown. Returns the Markdown."""
    with open(src_file, "r", errors="ignore") as f_in:
        content = f_in.read()

    # src_file looks like pages/<encoded name>/revisions/<rev>
    page_dir_name = os.path.basename(os.path.dirname(os.path.dirname(src_file)))
    preprocessed_content, code_blocks = preprocess(
        content, current_page=unquote_wikiname_fs(page_dir_name)
    )

    process = subprocess.run(
        ["pandoc", "-f", "creole", "-t", "markdown"],
        input=preprocessed_content.encode("utf-8"),
        capture_output=True,
    )
    if process.returncode != 0:
        raise RuntimeError(process.stderr.decode("utf-8"))
    return postprocess(process.stdout.decode("utf-8"), code_blocks)


def git_modified_files(path):
    """Return the set of files under path with uncommitted git changes."""
    try:
        out = subprocess.run(
            ["git", "status", "--porcelain", "--", path],
            capture_output=True, text=True, check=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return set()
    return {line[3:].strip() for line in out.splitlines() if line.strip()}


def load_yaml(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return yaml.safe_load(f) or {}


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description=(
            "Convert MoinMoin wiki pages to Markdown. By default only entries "
            f"in {' and '.join(queue_files)} are converted; packages in "
            f"{submitted_file}, entries marked 'edited: true', and Markdown "
            "files with uncommitted git changes are never overwritten."
        )
    )
    parser.add_argument(
        "yaml_files", nargs="*",
        help=f"Queue YAML files to process (default: existing {queue_files}; "
             f"falls back to {input_file} if none exist).",
    )
    parser.add_argument(
        "--only", nargs="+", metavar="PKG",
        help="Only convert these packages.",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Report which Markdown files would change without writing.",
    )
    parser.add_argument(
        "--force-edited", action="store_true",
        help="Also overwrite entries marked 'edited: true' or with "
             "uncommitted changes (submitted packages are still skipped).",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    yaml_files = args.yaml_files or [f for f in queue_files if os.path.exists(f)]
    legacy_mode = False
    if not yaml_files:
        if not os.path.exists(input_file):
            print(f"Error: none of {queue_files} or {input_file} found.")
            return 1
        print(f"No review queues found; bootstrapping from {input_file}.")
        yaml_files = [input_file]
        legacy_mode = True

    os.makedirs(output_dir, exist_ok=True)
    submitted = set(load_yaml(submitted_file))
    dirty = git_modified_files(output_dir)
    only = set(args.only) if args.only else None

    stats = {"unchanged": 0, "updated": 0, "created": 0, "failed": 0,
             "skipped_submitted": 0, "skipped_edited": 0, "skipped_dirty": 0,
             "missing_source": 0}
    changed = []

    for yaml_file in yaml_files:
        data = load_yaml(yaml_file)
        for key, value in data.items():
            if only is not None and key not in only:
                continue
            if key in submitted:
                print(f"Skipping {key}: already submitted ({submitted_file}).")
                stats["skipped_submitted"] += 1
                continue

            dst_file = value.get("markdown_file") or os.path.join(
                output_dir, f"{key}.md"
            )
            if not args.force_edited:
                if value.get("edited"):
                    print(f"Skipping {key}: marked 'edited: true' in {yaml_file}.")
                    stats["skipped_edited"] += 1
                    continue
                if os.path.normpath(dst_file) in dirty:
                    print(f"Skipping {key}: {dst_file} has uncommitted changes.")
                    stats["skipped_dirty"] += 1
                    continue

            src_file = value.get("source_file")
            if not src_file or not os.path.exists(src_file):
                print(f"Warning: Source file {src_file} not found.")
                stats["missing_source"] += 1
                continue

            try:
                final_markdown = convert_file(src_file)
            except Exception as e:
                print(f"Error processing {src_file}: {e}")
                stats["failed"] += 1
                continue

            existing = None
            if os.path.exists(dst_file):
                with open(dst_file, "r") as f_old:
                    existing = f_old.read()
            if existing == final_markdown:
                stats["unchanged"] += 1
                continue

            stats["created" if existing is None else "updated"] += 1
            changed.append(dst_file)
            if not args.dry_run:
                with open(dst_file, "w") as f_out:
                    f_out.write(final_markdown)
            if legacy_mode:
                value["markdown_file"] = dst_file

        # Queue files are owned by review_packages.py / submit_prs.py and are
        # never rewritten here; only the legacy bootstrap updates its index.
        if legacy_mode and not args.dry_run:
            with open(yaml_file, "w") as f:
                yaml.dump(data, f, default_flow_style=False, sort_keys=True)

    verb = "Would change" if args.dry_run else "Changed"
    print(f"\n{verb} {len(changed)} file(s):")
    for path in changed:
        print(f"  {path}")
    print("Summary: " + ", ".join(f"{k}={v}" for k, v in stats.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
