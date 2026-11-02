import argparse
import os
import re
import subprocess
import urllib.parse
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


INDEX_PACKAGES_FILE = "index_packages.yaml"
INDEX_PACKAGE_URL = "https://index.ros.org/p/{}"
_index_packages = None


def get_index_packages():
    """Package names on index.ros.org (from fetch_index_packages.py)."""
    global _index_packages
    if _index_packages is None:
        if os.path.exists(INDEX_PACKAGES_FILE):
            with open(INDEX_PACKAGES_FILE, "r") as f:
                _index_packages = set(yaml.safe_load(f) or {})
        else:
            print(f"Warning: {INDEX_PACKAGES_FILE} not found; package links "
                  "will not be rewritten. Run fetch_index_packages.py.")
            _index_packages = set()
    return _index_packages


_ATTACHMENT_REF = re.compile(r"(\[\[|\{\{)(\s*)attachment:([^|\]\}]+)")


def absolutize_attachments(content, page):
    """Qualify page-relative references with the page they came from.

    Used for included pages, whose content is inlined into another page:
    bare attachment refs and relative links ([[/Sub]], [[../Sibling]],
    <<TutorialChain(/Sub)>>) must keep resolving against the included page.
    """

    def repl(match):
        ref = match.group(3).strip()
        if "/" not in ref:
            ref = f"{page}/{ref}"
        return f"{match.group(1)}{match.group(2)}attachment:{ref}"

    def rel_link_repl(match):
        return match.group(1) + resolve_page_name(match.group(2), page)

    def chain_repl(match):
        target = match.group(1).strip()
        if target.startswith(("/", "../")):
            target = resolve_page_name(target, page)
        return f"<<TutorialChain({target})>>"

    content = _ATTACHMENT_REF.sub(repl, content)
    content = re.sub(r"(\[\[\s*)((?:\.\./|/)[^|\]#\n]*)", rel_link_repl, content)
    content = re.sub(r"<<TutorialChain\((.*?)\)>>", chain_repl, content)
    return content


def attachment_link(ref, current_page, attachments):
    """Map attachment:[Page/]file to a doc/ path and record it.

    Returns the relative link, or None if the file isn't in the wiki dump.
    """
    owner, _, fname = ref.strip().rpartition("/")
    owner = resolve_page_name(owner, current_page) if owner else current_page
    if not owner or not fname:
        return None
    src = os.path.join("pages", quote_wikiname_fs(owner), "attachments", fname)
    if not os.path.exists(src):
        return None
    doc_name = fname.replace(" ", "_")
    key = f"doc/{doc_name}"
    if attachments.get(key, src) != src:
        # Same filename attached to a different page: disambiguate.
        doc_name = f"{owner.replace('/', '_')}_{doc_name}"
        key = f"doc/{doc_name}"
    attachments[key] = src
    return "doc/" + urllib.parse.quote(doc_name)


def read_page(name):
    """Return the current revision text of a wiki page, or None."""
    for page_dir in (os.path.join("pages", quote_wikiname_fs(name)),
                     os.path.join("pages", name)):
        current_file = os.path.join(page_dir, "current")
        if not os.path.exists(current_file):
            continue
        with open(current_file, "r") as f:
            revision = f.read().strip()
        revision_file = os.path.join(page_dir, "revisions", revision)
        if os.path.exists(revision_file):
            with open(revision_file, "r", errors="ignore") as f_rev:
                return f_rev.read()
    return None


# Maximum number of subpages appended to one README (None = unlimited).
MAX_SUBPAGES = None

# Subpages appended even when the page doesn't link them (MoinMoin's
# <<PackageHeader>> linked these automatically), if they have real content.
STANDARD_SUBPAGES = ["Tutorials", "Troubleshooting", "FAQ"]

# Subpages never appended: historical reviews, change lists, and pages for
# old ROS distributions (noetic content comes in via version blocks).
_OLD_DISTROS = ("boxturtle", "cturtle", "diamondback", "electric", "fuerte",
                "groovy", "hydro", "indigo", "jade", "kinetic", "lunar", "melodic")
_EXCLUDED_SUBPAGE = re.compile(
    r"^(reviews?\b|changelist\b|changelog\b|(" + "|".join(_OLD_DISTROS) + r")\b)"
    r"|(api|doc)_review",
    re.IGNORECASE,
)

# Boilerplate text that doesn't count as content.
_TEMPLATE_TEXT = [
    "No troubleshooting tips have been added for this package/stack.",
]


def is_excluded_subpage(rel_name):
    """True for subpages (relative to the package) that are never exported."""
    return any(_EXCLUDED_SUBPAGE.search(part) for part in rel_name.split("/"))


def has_real_content(page, min_chars=80):
    """True if a wiki page has more than headings, macros and boilerplate."""
    text = read_page(page)
    if text is None:
        return False
    expanded = expand_listing_macros(text, page)
    if expanded.count("[[") > text.count("[["):
        return True  # a tutorial listing that found existing pages
    text = expanded
    for phrase in _TEMPLATE_TEXT:
        text = text.replace(phrase, "")
    lines = []
    for line in text.replace("\r", "").split("\n"):
        s = line.strip()
        if (s.startswith("##") or re.match(r"^=+.*=+$", s)
                or re.match(r"^(\w*Category\w*\s*)+$", s) or s == "----"):
            continue
        lines.append(re.sub(r"<<[^>]*>>", "", s))
    return len(re.sub(r"\s+", "", "".join(lines))) >= min_chars


class DocContext:
    """Tracks which wiki pages end up in one generated README."""

    def __init__(self, root, max_subpages=MAX_SUBPAGES):
        self.root = root
        self.max_subpages = max_subpages
        self.subpages = []      # appended as sections, in order
        self.included = set()   # inlined via <<Include>>
        self.skipped = []       # subpages not appended (over the limit)

    def contains(self, page):
        return page == self.root or page in self.subpages or page in self.included

    def try_append_subpage(self, page):
        if not page.startswith(self.root + "/") or self.contains(page):
            return False
        if is_excluded_subpage(page[len(self.root) + 1:]):
            return False
        if read_page(page) is None:
            return False
        if self.max_subpages is not None and len(self.subpages) >= self.max_subpages:
            if page not in self.skipped:
                self.skipped.append(page)
            return False
        self.subpages.append(page)
        return True


_ANCHOR_MARKER = "#wikianchor/"


def anchor_marker(page, anchor):
    """In-page link placeholder resolved by finalize_document()."""
    return (_ANCHOR_MARKER + urllib.parse.quote(page, safe="") + "/"
            + urllib.parse.quote(anchor.strip(), safe=""))


def explicit_anchor_placeholder(name):
    return f"WIKIANCHORBEGIN{name.strip().encode('utf-8').hex()}WIKIANCHOREND"


_EXPLICIT_ANCHOR = re.compile(r"WIKIANCHORBEGIN([0-9a-f]*)WIKIANCHOREND")


def github_slug(heading_text):
    """Approximate GitHub's heading anchor for Markdown heading text."""
    text = re.sub(r"<[^>]+>", "", _EXPLICIT_ANCHOR.sub("", heading_text))
    text = re.sub(r"!?\[((?:[^\[\]]|\[[^\]]*\])*)\]\([^)]*\)", r"\1", text)
    text = text.replace("\\", "").replace("`", "").replace("*", "")
    text = re.sub(r"[^\w\- ]", "", text.strip().lower())
    return text.replace(" ", "-")


def _loose(slug):
    return re.sub(r"[\s_-]+", "-", slug.lower()).strip("-")


def moin_anchor_candidates(anchor):
    """Possible heading texts for a MoinMoin heading anchor.

    MoinMoin 1.9 builds heading ids as quote_plus(utf7(text)) with '%' -> '.'
    and '+' -> '_'; ids of included pages are prefixed with "<page>.", and
    duplicate ids get "-N" suffixes.
    """
    candidates = []
    segments = re.split(r"\.(?![0-9A-Fa-f]{2})", anchor)
    for raw in dict.fromkeys([anchor, segments[-1]]):
        for variant in dict.fromkeys([raw, re.sub(r"-\d+$", "", raw)]):
            candidates.append(variant)
            try:
                s = re.sub(r"\.([0-9A-Fa-f]{2})", r"%\1", variant).replace("_", " ")
                s = urllib.parse.unquote(s)
                candidates.append(s.encode("latin-1", "ignore").decode("utf-7"))
            except (UnicodeError, ValueError):
                pass
    return [c for c in dict.fromkeys(candidates) if c]


_ATX_HEADING = re.compile(r"^(#{1,6})[ \t]+(.*?)[ \t]*#*[ \t]*$")


def iter_headings(markdown):
    """Yield (line_index, level, text) for ATX headings outside code fences."""
    in_fence = False
    for i, line in enumerate(markdown.split("\n")):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = _ATX_HEADING.match(line)
        if m:
            yield i, len(m.group(1)), m.group(2)


def shift_headings(markdown, top_level):
    """Shift headings so the highest-level one becomes `top_level`."""
    headings = list(iter_headings(markdown))
    if not headings:
        return markdown
    shift = top_level - min(level for _, level, _ in headings)
    lines = markdown.split("\n")
    for i, level, text in headings:
        lines[i] = "#" * max(1, min(6, level + shift)) + " " + text
    return "\n".join(lines)


def finalize_document(parts, stats=None):
    """Join (page, markdown) parts and resolve in-page anchor markers.

    If `stats` is a dict, counts of resolved/unresolved anchors are added.
    """
    import hashlib

    counts = {}
    headings = []  # (page, slug, loose base slug, sha1 of text)
    for page, md in parts:
        for _, _, text in iter_headings(md):
            base = github_slug(text)
            n = counts.get(base, 0)
            counts[base] = n + 1
            plain = re.sub(r"[`*\\]", "", text).strip()
            headings.append((page, base if n == 0 else f"{base}-{n}", _loose(base),
                             hashlib.sha1(plain.encode("utf-8")).hexdigest()))
    first_heading = {}
    for page, slug, _, _ in headings:
        first_heading.setdefault(page, slug)

    full = "\n\n".join(md.rstrip("\n") for _, md in parts) + "\n"
    explicit = {bytes.fromhex(h).decode("utf-8", "ignore")
                for h in _EXPLICIT_ANCHOR.findall(full)}

    def resolve(page, anchor):
        if anchor:
            if anchor in explicit:
                return anchor
            if anchor.startswith("head-") and len(anchor) == 45:
                for _, slug, _, sha in headings:
                    if sha == anchor[5:]:
                        return slug
            wanted = [_loose(github_slug(c)) for c in moin_anchor_candidates(anchor)]
            for scope in ([h for h in headings if h[0] == page], headings):
                for w in wanted:
                    for _, slug, loose, _ in scope:
                        if loose == w:
                            return slug
        return first_heading.get(page) if page != parts[0][0] else None

    def link_repl(match):
        label, page, anchor = match.groups()
        slug = resolve(urllib.parse.unquote(page), urllib.parse.unquote(anchor))
        if stats is not None:
            key = "anchors_resolved" if slug else "anchors_unresolved"
            stats[key] = stats.get(key, 0) + 1
            if not slug:
                stats.setdefault("unresolved", []).append(
                    (urllib.parse.unquote(page), urllib.parse.unquote(anchor)))
        return f"[{label}](#{slug})" if slug else label

    full = re.sub(
        r"\[((?:[^\[\]]|\[[^\]]*\])*)\]\(" + re.escape(_ANCHOR_MARKER) + r"([^/)]*)/([^)]*)\)",
        link_repl, full,
    )
    full = _EXPLICIT_ANCHOR.sub(
        lambda m: '<a id="{}"></a>'.format(
            bytes.fromhex(m.group(1)).decode("utf-8", "ignore").replace('"', "")),
        full,
    )
    return full


def rewrite_link_target(target, current_page, doc=None):
    """Return a replacement URL for a wiki link target, or None to keep it.

    - Links into the current document (the page itself, pages included in it,
      or subpages appended to it) become in-page anchor markers that
      finalize_document() resolves to Markdown heading anchors.
    - Links to subpages of the document's root page are queued on `doc` so
      that convert_file() appends them as sections of the same README.
    - Links to packages on index.ros.org -> https://index.ros.org/p/<pkg>;
      links to subpages of *other* indexed packages -> that package's page.
    """
    target = target.strip()
    if re.match(r"^[A-Za-z][\w+.-]*:", target):
        return None  # URL, interwiki or attachment
    base, _, anchor = target.partition("#")
    base = base.strip()
    resolved = resolve_page_name(base, current_page) if base else current_page
    if not resolved:
        return None
    if doc is not None:
        if resolved == current_page or doc.contains(resolved):
            return anchor_marker(resolved, anchor)
        if doc.try_append_subpage(resolved):
            return anchor_marker(resolved, anchor)
    elif resolved == current_page:
        return None
    index = get_index_packages()
    if resolved in index:
        return INDEX_PACKAGE_URL.format(resolved)
    owner = resolved.split("/", 1)[0]
    if "/" in resolved and owner in index:
        return INDEX_PACKAGE_URL.format(owner)
    return None


def rewrite_links(content, current_page, attachments, doc=None):
    """Rewrite MoinMoin {{image}} and [[link]] targets.

    - attachment:file -> doc/file (recorded in `attachments`)
    - see rewrite_link_target() for page links
    """

    def image_repl(match):
        target, rest = match.group(1).strip(), match.group(2)
        if not target.startswith("attachment:"):
            return match.group(0)
        new = attachment_link(target[len("attachment:"):], current_page, attachments)
        if new is None:
            return match.group(0)
        alt = rest.lstrip("|").split("|")[0].strip() if rest else ""
        alt = alt or os.path.basename(target)
        return f"{{{{{new}|{alt}}}}}"

    def link_repl(match):
        target, rest = match.group(1).strip(), match.group(2)
        # [[target|label|params]]: keep the label (which may itself be an
        # image like {{doc/x.png|alt}}) and drop link params.
        label = None
        if rest:
            label_part = rest[1:]
            img = re.match(r"\s*\{\{.*?\}\}", label_part)
            label = img.group(0) if img else label_part.split("|")[0]
        if target.startswith("attachment:"):
            new = attachment_link(target[len("attachment:"):], current_page, attachments)
        else:
            new = rewrite_link_target(target, current_page, doc)
        if new is None:
            return match.group(0)
        if not label or not label.strip():
            base, _, anchor = target.partition("#")
            label = base.split("attachment:")[-1].rsplit("/", 1)[-1] or anchor
        return f"[[{new}|{label}]]"

    content = re.sub(r"\{\{(?!\{)([^|}\n]+)(\|[^}\n]*)?\}\}", image_repl, content)
    content = re.sub(r"\[\[([^|\]\n]+)(\|(?:[^\]\n]|\](?!\]))*)?\]\]", link_repl, content)
    return content


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


_all_page_names = None


def all_page_names():
    """All page names in the wiki dump (cached)."""
    global _all_page_names
    if _all_page_names is None:
        try:
            _all_page_names = sorted(unquote_wikiname_fs(d) for d in os.listdir("pages"))
        except OSError:
            _all_page_names = []
    return _all_page_names


def page_meta(name, content):
    """(title, description) from a tutorial page's '## title =' header."""
    def field(key):
        m = re.search(rf"^##\s*{key}\s*=\s*(.*?)\s*$", content, re.M)
        return m.group(1).strip() if m else ""
    return field("title") or name.rsplit("/", 1)[-1], field("description")


def page_list_markup(names):
    lines = []
    for name in names:
        content = read_page(name) or ""
        title, desc = page_meta(name, content)
        lines.append(f" * [[{name}|{title}]]" + (f": {desc}" if desc else ""))
    return "\n".join(lines)


def expand_listing_macros(content, current_page, max_items=20):
    """Statically expand tutorial listing macros that MoinMoin renders live.

    - <<FullSearch*(title:"pkg/Tutorials/" SomeCategory)>> -> list of the
      matching pages in the dump (name prefix + all category terms present)
    - <<TutorialChain(page)>> -> the page and its '## next.N.link' successors
    - the "Create a new tutorial: <<NewPage(...)>>" boilerplate is dropped
    """

    def fullsearch_repl(match):
        args = match.group(1)
        m = re.search(r'title:"([^"]+)"', args)
        if not m:
            return ""
        prefix = resolve_page_name(m.group(1), current_page)
        terms = [t for t in re.sub(r'title:"[^"]*"', "", args).split()
                 if re.match(r"^\w*Category\w*$", t)]
        names = []
        for name in all_page_names():
            if not name.startswith(prefix) or name == prefix.rstrip("/"):
                continue
            text = read_page(name)
            if text is None or not all(t in text for t in terms):
                continue
            names.append(name)
            if len(names) >= max_items:
                break
        return page_list_markup(names)

    def chain_repl(match):
        names = []
        page = resolve_page_name(match.group(1).strip().strip("\"'"), current_page)
        while page and page not in names and len(names) < max_items:
            text = read_page(page)
            if text is None:
                break
            names.append(page)
            nxt = re.search(r"^##\s*next\.\d+\.link\s*=\s*\[\[([^|\]]+)", text, re.M)
            page = resolve_page_name(nxt.group(1).strip(), page) if nxt else None
        return page_list_markup(names)

    content = re.sub(r"<<FullSearch\w*\((.*?)\)>>", fullsearch_repl, content)
    content = re.sub(r"<<TutorialChain\((.*?)\)>>", chain_repl, content)
    content = re.sub(r"^.*'''Create a new tutorial:'''.*$\n?", "", content, flags=re.M)
    return content


def preprocess(content, current_page=None, attachments=None, doc=None):
    """Preprocess MoinMoin markup into Creole for pandoc.

    If `attachments` is a dict, it is filled with {"doc/<name>": <source path>}
    for every attachment that was rewritten to a doc/ link. If `doc` is a
    DocContext, in-document links become anchor markers and linked subpages
    of the root page are queued for appending (see convert_file()).
    """
    if attachments is None:
        attachments = {}
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
                        if doc is not None:
                            doc.included.add(page_name)
                        # Attachments in an included page belong to that page.
                        included_content = absolutize_attachments(
                            included_content, page_name
                        )
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

    # Expand live tutorial listings into static link lists (before link
    # rewriting, so the listed subpages get appended to the document).
    if current_page:
        content = expand_listing_macros(content, current_page)

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

    # 2. Rewrite links to indexed packages and attachments (code blocks are
    # already extracted, so their contents are untouched).
    content = rewrite_links(content, current_page, attachments, doc)

    # Keep explicit <<Anchor(name)>> targets as <a id="name"> (restored in
    # finalize_document) so in-page links to them keep working.
    content = re.sub(
        r"<<Anchor\(([^)]*)\)>>",
        lambda m: explicit_anchor_placeholder(m.group(1)) if doc is not None else "",
        content,
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
        "IncludeCSTemplate",
        "xacro_file",
    ]

    macros_regex = "|".join(macros_to_omit)
    pattern = re.compile(r"#?\s*<<(" + macros_regex + r")(\(.*\))?>>")
    content = pattern.sub("", content)

    # 4. Convert <<BR>> to \\
    content = content.replace("<<BR>>", "\\\\")

    # 5. Remove lines containing AUTOGENERATED or CategoryPackage
    lines = content.split("\n")
    lines = [l for l in lines if "AUTOGENERATED" not in l and "CategoryPackage" not in l]
    # Drop lines that only contain wiki category tags (e.g. "TutorialCategory").
    lines = [l for l in lines if not re.match(r"^\s*(\w*Category\w*\s*)+$", l)]
    content = "\n".join(lines)
    for phrase in _TEMPLATE_TEXT:
        content = content.replace(phrase, "")

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


def convert_markup(content, page, attachments=None, doc=None):
    """Convert one page's MoinMoin markup to Markdown (no finalization)."""
    preprocessed_content, code_blocks = preprocess(
        content, current_page=page, attachments=attachments, doc=doc
    )
    process = subprocess.run(
        ["pandoc", "-f", "creole", "-t", "markdown"],
        input=preprocessed_content.encode("utf-8"),
        capture_output=True,
    )
    if process.returncode != 0:
        raise RuntimeError(process.stderr.decode("utf-8"))
    return postprocess(process.stdout.decode("utf-8"), code_blocks)


def convert_file(src_file, attachments=None, max_subpages=MAX_SUBPAGES, stats=None):
    """Convert a MoinMoin revision file to Markdown. Returns the Markdown.

    Subpages of the page (e.g. pkg/Tutorials) that it links to are appended
    as "## <subpage>" sections, and links to them, as well as same-page
    section links, become Markdown heading anchors.

    If `attachments` is a dict it is filled with {"doc/<name>": <source path>}
    for attachments referenced by the page (see attachments_manifest_path).
    """
    with open(src_file, "r", errors="ignore") as f_in:
        content = f_in.read()
    if attachments is None:
        attachments = {}

    # src_file looks like pages/<encoded name>/revisions/<rev>
    page_dir_name = os.path.basename(os.path.dirname(os.path.dirname(src_file)))
    root = unquote_wikiname_fs(page_dir_name)
    doc = DocContext(root, max_subpages=max_subpages)

    parts = [(root, convert_markup(content, root, attachments, doc))]
    # Pages MoinMoin's PackageHeader linked automatically (after the subpages
    # the page links explicitly, so the page's own ordering comes first).
    for name in STANDARD_SUBPAGES:
        page = f"{root}/{name}"
        if not doc.contains(page) and has_real_content(page):
            doc.try_append_subpage(page)
    i = 0
    while i < len(doc.subpages):  # may grow while subpages are converted
        page = doc.subpages[i]
        i += 1
        page_text = read_page(page) or ""
        body = convert_markup(page_text, page, attachments, doc)
        title = page[len(root) + 1:]
        meta_title, _ = page_meta(page, page_text)
        if re.search(r"^##\s*title\s*=", page_text, re.M):
            title = meta_title
        body = shift_headings(body, 3).strip("\n")
        # Drop the subpage's own top heading if it just repeats the title.
        first = next(iter_headings(body), None)
        if first and first[0] == 0 and _loose(github_slug(first[2])) in (
                _loose(github_slug(title)), _loose(github_slug(title.rsplit("/", 1)[-1]))):
            body = body.split("\n", 1)[1].lstrip("\n") if "\n" in body else ""
        parts.append((page, f"## {title}\n\n" + body))
    if doc.skipped:
        print(f"Warning: {root}: not appending {len(doc.skipped)} subpage(s) "
              f"over the limit of {max_subpages}: {', '.join(doc.skipped)}")
    if stats is not None:
        stats["subpages"] = list(doc.subpages)
        stats["subpages_skipped"] = list(doc.skipped)
    return finalize_document(parts, stats)


def attachments_manifest_path(markdown_file):
    """Sidecar listing the attachments a Markdown file links to under doc/.

    Format: {"doc/<name>": "pages/<page>/attachments/<file>"}. Read by
    submit_prs.py to commit the files into <package>/doc/.
    """
    return os.path.splitext(markdown_file)[0] + ".attachments.yaml"


def render_manifest(attachments):
    if not attachments:
        return None
    return yaml.safe_dump(dict(sorted(attachments.items())), default_flow_style=False)


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

            attachments = {}
            try:
                final_markdown = convert_file(src_file, attachments=attachments)
            except Exception as e:
                print(f"Error processing {src_file}: {e}")
                stats["failed"] += 1
                continue

            manifest_file = attachments_manifest_path(dst_file)
            manifest = render_manifest(attachments)
            old_manifest = None
            if os.path.exists(manifest_file):
                with open(manifest_file, "r") as f_old:
                    old_manifest = f_old.read()

            existing = None
            if os.path.exists(dst_file):
                with open(dst_file, "r") as f_old:
                    existing = f_old.read()
            if existing == final_markdown and old_manifest == manifest:
                stats["unchanged"] += 1
                continue

            stats["created" if existing is None else "updated"] += 1
            changed.append(dst_file)
            if not args.dry_run:
                with open(dst_file, "w") as f_out:
                    f_out.write(final_markdown)
                if manifest is not None:
                    with open(manifest_file, "w") as f_out:
                        f_out.write(manifest)
                elif old_manifest is not None:
                    os.remove(manifest_file)
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
