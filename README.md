# ROS Wiki to Markdown Migration Tools

This repository contains scripts and data for migrating ROS 1 Wiki (`wiki.ros.org`) MoinMoin package pages into Markdown (`README.md`) files and correlating them with their upstream GitHub repositories in ROS Noetic.

## Overview

Many ROS packages historically maintained their primary documentation on the MoinMoin-based ROS Wiki rather than in their source repositories. This project provides an automated pipeline and interactive review workflow to:

1. **Discover** active package pages (`CategoryPackage`) from a local dump of the ROS Wiki.
2. **Convert** MoinMoin wiki syntax into clean GitHub-flavored Markdown using custom preprocessing/postprocessing and [Pandoc](https://pandoc.org/).
3. **Correlate** wiki pages with upstream source repositories, branches, and package subdirectories via `rosdistro` (targeting ROS Noetic) and the GitHub API.
4. **Classify** matched, non-archived packages into repositories missing a `README.md` (`export_pages.yaml`) and repositories that already have one (`extend_pages.yaml`).
5. **Review and edit** converted Markdown files interactively before submitting upstream pull requests.

---

## Prerequisites

### System Dependencies

- **Python 3** (3.8+)
- **Pandoc** (required by `convert_to_markdown.py` for Creole-to-Markdown conversion)
  ```bash
  sudo apt-get install pandoc
  ```

### Python Dependencies

Install the required Python libraries (`PyYAML` and `rosdistro`):

```bash
pip install pyyaml rosdistro
```

### GitHub Authentication (`GITHUB_TOKEN`)

Two scripts interact with the GitHub REST API and read the `GITHUB_TOKEN` environment variable:

1. **`correlate_packages.py` (Read-Only)**:
   - Queries public repository metadata, file trees, `package.xml`, and `README.md` files.
   - **Required scope**: None (any valid Personal Access Token with read access to public repositories increases the GitHub API rate limit from 60 to 5,000 requests/hour).
2. **`submit_prs.py` (Fork, Commit, and Pull Request Creation)**:
   - Forks upstream repositories into the `tfoote-ros-wiki-migration-forks` organization, creates branches, commits `README.md` changes to the fork, and opens pull requests on upstream repositories.
   - **Recommended Token Type**: **Personal Access Token (Classic)** (`ghp_...`). *(Fine-grained tokens are restricted to a single resource owner and cannot both write to an organization fork and open pull requests on arbitrary external repositories.)*
   - **Required Scopes (Classic PAT)**:
     - **`public_repo`** *(or full `repo`)* — Required to fork public repositories, create/update branch refs, commit `README.md` updates via the Contents API, and open pull requests against upstream public repositories.
     - **`read:org`** — Recommended so GitHub can verify your membership and permissions when creating forks inside the `tfoote-ros-wiki-migration-forks` organization.
   - **Organization Membership**: Your GitHub user account must be a member or owner of `tfoote-ros-wiki-migration-forks` (or the organization passed via `--fork-org`) with permission to create/fork repositories.

### Wiki Dump Data (`pages/`)

The initial discovery and conversion scripts expect a local MoinMoin wiki pages directory at `./pages/` (ignored by Git). Each page directory follows the standard MoinMoin on-disk layout:

```text
pages/
└── <PageName>/
    ├── current              # Plain-text file containing the active revision number (e.g., 00000014)
    └── revisions/
        └── 00000014         # Raw MoinMoin markup for that revision
```

> **Note:** Pre-generated `current_pages.yaml`, `export_pages.yaml`, `extend_pages.yaml`, and converted Markdown files in `markdown_output/` are already checked into this repository. You only need the `pages/` directory if you are re-running page discovery (`find_current_pages.py`) or reconverting from raw wiki source (`convert_to_markdown.py`).

---

## Repository Structure

| File / Directory | Description |
| :--- | :--- |
| `find_current_pages.py` | Scans `pages/` for top-level pages tagged with `CategoryPackage` and generates `current_pages.yaml`. |
| `find_macros.py` | Utility script that scans `current_pages.yaml` source files and reports MoinMoin `<<Macro>>` prevalence. |
| `convert_to_markdown.py` | Preprocesses MoinMoin syntax, runs `pandoc`, postprocesses output, writes `markdown_output/<pkg>.md`, and updates `current_pages.yaml`. |
| `correlate_packages.py` | Matches packages in a YAML file against the ROS Noetic `rosdistro` index and queries GitHub for `package.xml`, `README.md`, and archive status. |
| `count_results.py` | Read-only analysis script that summarizes correlation, review, and submission statistics across `current_pages.yaml`, `export_pages.yaml`, `extend_pages.yaml`, and `submitted_pages.yaml`. |
| `review_packages.py` | Interactive CLI tool for reviewing, editing, and tagging converted Markdown files for export. |
| `submit_prs.py` | Iterates through `export_pages.yaml` and `extend_pages.yaml` for `ready` packages, previews planned changes, forks into `tfoote-ros-wiki-migration-forks`, commits `README.md`, opens a PR, and moves entries to `submitted_pages.yaml`. |
| `current_pages.yaml` | Master dataset mapping all discovered package pages to their source revision, converted Markdown path, and upstream repository metadata. |
| `export_pages.yaml` | Active (matched, non-archived) packages that **do not** yet have a `README.md` in their upstream repository. |
| `extend_pages.yaml` | Active (matched, non-archived) packages that **already** have a `README.md` in their upstream repository. |
| `submitted_pages.yaml` | Tracks packages whose migration pull requests have been submitted via `submit_prs.py`. |
| `test_current_pages.yaml` | Small 3-package fixture (`amcl`, `roscpp`, `tf2`) for testing `correlate_packages.py`. |
| `markdown_output/` | Directory containing the converted `<package>.md` files. |
| `test_*.py` | Unit and integration test suites for conversion and review scripts. |

---

## Workflow & Usage

### 1. Discover Package Pages

If starting from a fresh `pages/` dump, generate the initial `current_pages.yaml` index:

```bash
python3 find_current_pages.py
```

- Skips subpages (directories containing `(2f)`).
- Reads `pages/<pkg>/current` to locate the latest revision file.
- Filters for pages containing `CategoryPackage`.

*(Optional)* Inspect macro usage across all discovered pages:

```bash
python3 find_macros.py
```

### 2. Convert Wiki Pages to Markdown

Convert all pages listed in `current_pages.yaml` into `markdown_output/<package>.md`:

```bash
python3 convert_to_markdown.py
```

**What the converter does:**
- **Preprocessing (`preprocess`)**:
  - Recursively resolves `<<Include(PageName)>>` macros (up to depth 5) from `pages/`.
  - Filters conditional `{{{#!wiki version ...}}}` blocks, keeping only blocks targeting `noetic` or ending in `_and_newer`.
  - Strips MoinMoin comments (`##`), `AUTOGENERATED` / `CategoryPackage` lines, and obsolete wiki macros (`PackageHeader`, `TOC`, `MsgSrvDoc`, `CodeRef`, `Markdown`, `GitHubIssues`, etc.).
  - Extracts multiline `{{{ ... }}}` code blocks into placeholders so Pandoc does not alter their contents.
  - Rewrites `<<Youtube(...)>>` to YouTube links and `<<MsgLink(pkg/Msg)>>` / `<<SrvLink(pkg/Srv)>>` to `docs.ros.org` links.
  - Translates MoinMoin bold/italic/monospace quote combinations (`''`, `'''`, `''''`, `'''''`) into Creole syntax.
- **Pandoc Conversion**:
  - Converts preprocessed text via `pandoc -f creole -t markdown`.
- **Postprocessing (`postprocess`)**:
  - Unescapes unnecessary backslash escapes (`\'`, `\"`, `\_`, `` \` ``, `\<`, `\>`) in prose.
  - Restores multiline code blocks as fenced Markdown code blocks (preserving `#!<lang>` syntax highlighting hints).
  - Normalizes remaining indented `#!wiki` blocks into blockquotes or fenced code blocks.

### 3. Correlate Packages with `rosdistro` and GitHub

Enrich a pages YAML file with upstream repository metadata from the ROS Noetic distribution and GitHub:

```bash
export GITHUB_TOKEN="ghp_your_personal_access_token"
python3 correlate_packages.py current_pages.yaml
```

> **Tip:** Set `GITHUB_TOKEN` in your environment before running `correlate_packages.py`. The script queries the GitHub API to check repository archive status and search file trees when a package subdirectory cannot be guessed directly; unauthenticated requests will hit GitHub rate limits quickly. For quick testing, run against `test_current_pages.yaml`:
> ```bash
> python3 correlate_packages.py test_current_pages.yaml
> ```

For each package, `correlate_packages.py` records:
- `repository`: Upstream Git URL from `rosdistro`.
- `branch`: Target branch (from `source_repository.version`, defaulting to `noetic`).
- `subdirectory`: Package path within the repository (verified by checking `<name>` in `package.xml`, falling back to a recursive GitHub tree search if needed).
- `package_xml_match`: Whether a matching `package.xml` was verified on GitHub.
- `readme_exists`: Whether `README.md` already exists in the package's subdirectory.
- `repository_archived`: Whether the GitHub repository is archived.
- `unmatched`: Set to `true` if the package is not present in the ROS Noetic `rosdistro` index.

### 4. Count and Summarize Results

Run the read-only summary script to inspect correlation counts, review progress, and submitted PR counts across the exported (`export_pages.yaml`), extended (`extend_pages.yaml`), and submitted (`submitted_pages.yaml`) groupings:

```bash
python3 count_results.py
```

By default, `count_results.py` reports a top-level `Submitted` count from `submitted_pages.yaml` and auto-detects any review keys recorded by `review_packages.py` to report `Ready`, `Ignored`, `Unreviewed`, and `Edited` counts for the remaining `Exported` and `Extended` queues. You can also filter by a specific review key:

```bash
python3 count_results.py --review-key <your_review_key>
```

### 5. Review and Edit Converted Pages

Use the interactive review script to inspect, edit, and mark converted Markdown files:

```bash
python3 review_packages.py export_pages.yaml --review-key <your_review_key>
```

- `input_file` defaults to `export_pages.yaml` if omitted.
- `--review-key` (required) specifies the YAML key under each package entry where your review decision is stored (allowing multiple review passes or reviewers).
- For each unreviewed package, the CLI displays the repository details and the first 10 lines of the generated Markdown file, then prompts for an action:
  - `[R]eady` — Marks `<review_key>: ready`.
  - `[S]kip` — Leaves the package unmarked and moves to the next entry.
  - `[I]gnore` — Marks `<review_key>: ignored`.
  - `[E]dit` — Opens the Markdown file in `$EDITOR` (defaults to `nano`) and sets `edited: true` upon saving.
  - `[Q]uit` — Saves all updates back to the YAML file and exits.

### 6. Submit Pull Requests

Once packages are marked `ready` under a review key, run `submit_prs.py` to preview and submit upstream pull requests (requires a Classic PAT with `public_repo` and `read:org` scopes; see [GitHub Authentication](#github-authentication-github_token)):

```bash
export GITHUB_TOKEN="ghp_your_personal_access_token"
python3 submit_prs.py --review-key <your_review_key>
```

For each package in `export_pages.yaml` and `extend_pages.yaml` with `<your_review_key>: ready`:
1. Displays a preview of the fork target, branch name, target `README.md` path, commit message, PR details, and Markdown content, then prompts `[Y]es / [S]kip / [Q]uit`.
2. Upon confirmation (`Y`):
   - Creates (or syncs) a fork of the repository in the `tfoote-ros-wiki-migration-forks` organization (parameterized via `FORK_ORG` / `--fork-org`).
   - Creates a new branch `ros-wiki-migration-<package>` off the declared branch in the YAML file.
   - Creates `README.md` in the package subdirectory if it does not exist, or appends the converted Markdown content to the existing `README.md`.
   - Commits the change with a message explaining the ROS Wiki origin.
   - Opens a pull request against the upstream repository's declared branch explaining the migration goal and noting that maintainers may merge, edit, or close it as *won't fix*.
   - If the declared branch differs from the repository's default branch, creates a second branch off the default branch (`ros-wiki-migration-<package>-<default_branch>`), applies the `README.md` change, and opens a second pull request against the default branch with a warning caveat at the top linking to the original PR and noting that the content is not confirmed up to date.
   - Removes the package entry from `export_pages.yaml` or `extend_pages.yaml` and records it in `submitted_pages.yaml` alongside the created PR URL(s).

---

## Development & Testing

Unit and integration tests are implemented with Python's built-in `unittest` module:

- `test_convert_markup.py` — Tests MoinMoin bold, italic, nested quotes, and code block placeholder extraction.
- `test_convert_include.py` — Tests `<<Include(...)>>` resolution, missing page fallbacks, nested includes, and recursion depth limits.
- `test_convert_advanced.py` — Tests 4-quote bold monospace, postprocess unescaping, code block spacing, and `Youtube` / `MsgLink` / `SrvLink` macros.
- `test_review_packages.py` — End-to-end CLI tests for `review_packages.py` (`Skip`, `Ready`, `Ignore`, and `Edit` flows).
- `test_count_results.py` — Tests for `count_results.py` review status aggregation, `--review-key` filtering, and read-only behavior.
- `test_submit_prs.py` — Tests for `submit_prs.py` preview/confirmation flow, creating vs. appending `README.md`, PR creation, and moving submitted entries to `submitted_pages.yaml`.

Run the full test suite with:

```bash
python3 -m unittest discover -s . -p "test_*.py"
```

---

## License

This project is licensed under the [Apache License 2.0](LICENSE).
