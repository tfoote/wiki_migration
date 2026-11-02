import os
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import convert_to_markdown as ctm
import submit_prs


class WikiDumpTestCase(unittest.TestCase):
    """Runs each test inside a temp dir with a tiny pages/ dump."""

    def setUp(self):
        self.orig_cwd = os.getcwd()
        self.tmp = tempfile.TemporaryDirectory()
        os.chdir(self.tmp.name)
        for page, files in {
            "mypkg": ["diagram.png", "my file.pdf"],
            "mypkg(2f)Tutorials": ["diagram.png"],
        }.items():
            os.makedirs(f"pages/{page}/attachments")
            for name in files:
                with open(f"pages/{page}/attachments/{name}", "wb") as f:
                    f.write(b"\x89PNG data")
        with open("index_packages.yaml", "w") as f:
            f.write("rviz: [noetic]\ntf: [noetic]\nmypkg: [noetic]\n")
        ctm._index_packages = None

    def tearDown(self):
        ctm._index_packages = None
        os.chdir(self.orig_cwd)
        self.tmp.cleanup()


class TestRewriteLinks(WikiDumpTestCase):
    def rewrite(self, text, page="mypkg"):
        attachments = {}
        return ctm.rewrite_links(text, page, attachments), attachments

    def test_package_links_go_to_index(self):
        out, _ = self.rewrite("See [[rviz]] and [[tf#Tools|tf tools]].")
        self.assertEqual(
            out,
            "See [[https://index.ros.org/p/rviz|rviz]] and "
            "[[https://index.ros.org/p/tf|tf tools]].",
        )

    def test_non_package_and_self_links_untouched(self):
        for text in ["[[Industrial]]", "[[mypkg#section|here]]",
                     "[[http://x.org|x]]"]:
            self.assertEqual(self.rewrite(text)[0], text)

    def test_other_package_subpage_goes_to_owner_index_page(self):
        self.assertEqual(
            self.rewrite("[[rviz/DisplayTypes/Map|Map plugin]]")[0],
            "[[https://index.ros.org/p/rviz|Map plugin]]",
        )

    def test_attachment_image_and_link(self):
        out, att = self.rewrite(
            "{{attachment:diagram.png|The diagram|width=500}} "
            "[[attachment:my file.pdf|manual]]"
        )
        self.assertEqual(
            out, "{{doc/diagram.png|The diagram}} [[doc/my_file.pdf|manual]]"
        )
        self.assertEqual(att, {
            "doc/diagram.png": "pages/mypkg/attachments/diagram.png",
            "doc/my_file.pdf": "pages/mypkg/attachments/my file.pdf",
        })

    def test_attachment_name_collision_across_pages(self):
        out, att = self.rewrite(
            "{{attachment:diagram.png}} {{attachment:mypkg/Tutorials/diagram.png}}"
        )
        self.assertIn("doc/mypkg_Tutorials_diagram.png", out)
        self.assertEqual(len(att), 2)

    def test_missing_attachment_untouched(self):
        out, att = self.rewrite("{{attachment:nope.png}}")
        self.assertEqual(out, "{{attachment:nope.png}}")
        self.assertEqual(att, {})

    def test_image_as_link_label(self):
        out, _ = self.rewrite("[[rviz|{{attachment:diagram.png|alt}}]]")
        self.assertEqual(
            out, "[[https://index.ros.org/p/rviz|{{doc/diagram.png|alt}}]]"
        )

    def test_included_page_attachments_are_qualified(self):
        self.assertEqual(
            ctm.absolutize_attachments("{{attachment:diagram.png}}", "mypkg/Tutorials"),
            "{{attachment:mypkg/Tutorials/diagram.png}}",
        )

    def test_included_page_relative_links_are_qualified(self):
        self.assertEqual(
            ctm.absolutize_attachments(
                "[[/Timers|t]] [[../Other]] <<TutorialChain(/Basics)>> [[abs/page]]",
                "mypkg/Tutorials"),
            "[[mypkg/Tutorials/Timers|t]] [[mypkg/Other]] "
            "<<TutorialChain(mypkg/Tutorials/Basics)>> [[abs/page]]",
        )


def write_page(name, text, rev="00000001"):
    d = os.path.join("pages", ctm.quote_wikiname_fs(name))
    os.makedirs(os.path.join(d, "revisions"), exist_ok=True)
    with open(os.path.join(d, "current"), "w") as f:
        f.write(rev + "\n")
    with open(os.path.join(d, "revisions", rev), "w") as f:
        f.write(text)
    return os.path.join(d, "revisions", rev)


class TestAnchorsAndSubpages(WikiDumpTestCase):
    def test_moin_anchor_candidates(self):
        self.assertIn("image_proc/electric",
                      [c.replace(" ", "_") for c in
                       ctm.moin_anchor_candidates("image_proc.2BAC8-electric")])
        # include prefix "<page>." is stripped
        self.assertIn("Usage", ctm.moin_anchor_candidates("mypkg.2BAC8-sub.Usage"))
        self.assertIn("Usage", ctm.moin_anchor_candidates("Usage-2"))

    def test_github_slug(self):
        self.assertEqual(ctm.github_slug("The `foo_bar` Node (v2)!"), "the-foo_bar-node-v2")
        self.assertEqual(ctm.github_slug("[Link](http://x) here"), "link-here")

    def test_same_page_section_links_and_subpage_appending(self):
        ctm._all_page_names = None
        write_page("mypkg/Tutorials",
                   "= Tutorials =\n<<FullSearchWithDescriptionsCS(title:\"mypkg/Tutorials/\" TutorialCategory)>>\n"
                   "'''Create a new tutorial:''' <<NewPage(x)>>\n")
        write_page("mypkg/Tutorials/First Steps",
                   "## title = First Steps\n## description = Start here\nTutorialCategory\n"
                   "= Intro =\nBack to [[mypkg#Usage|usage]].\n")
        write_page("mypkg/Tutorials/Other", "Not a tutorial.\n")
        src = write_page("mypkg",
                         "== Usage ==\nSee [[#Usage|usage]], [[#jump|anchor]] and "
                         "[[/Tutorials|the tutorials]].\n<<Anchor(jump)>>\n== Usage ==\nagain\n")
        stats = {}
        with patch("builtins.print"):
            md = ctm.convert_file(src, stats=stats)
        self.assertEqual(stats["subpages"],
                         ["mypkg/Tutorials", "mypkg/Tutorials/First Steps"])
        self.assertIn("[usage](#usage)", md)
        self.assertIn("[anchor](#jump)", md)
        self.assertIn('<a id="jump"></a>', md)
        self.assertIn("[the tutorials](#tutorials)", md)
        self.assertIn("## Tutorials", md)
        self.assertIn("## First Steps", md)  # tutorial '## title =' used
        self.assertIn("[First Steps](#first-steps)", md)
        self.assertIn("Start", md)
        self.assertNotIn("### Tutorials", md)  # duplicate title dropped
        self.assertNotIn("TutorialCategory", md)
        self.assertIn("### Intro", md)  # subpage headings demoted
        self.assertNotIn("Create a new tutorial", md)
        self.assertNotIn("#wikianchor/", md)
        self.assertNotIn("Other", md)  # not in TutorialCategory

    def test_subpage_limit(self):
        for i in range(3):
            write_page(f"mypkg/S{i}", f"sub {i}\n")
        src = write_page("mypkg", "[[/S0]] [[/S1]] [[/S2]]\n")
        stats = {}
        with patch("builtins.print"):
            md = ctm.convert_file(src, max_subpages=2, stats=stats)
        self.assertEqual(stats["subpages"], ["mypkg/S0", "mypkg/S1"])
        self.assertEqual(stats["subpages_skipped"], ["mypkg/S2"])
        self.assertIn("## S1", md)
        self.assertNotIn("## S2", md)


class TestStandardSubpages(WikiDumpTestCase):
    def setUp(self):
        super().setUp()
        ctm._all_page_names = None

    def tearDown(self):
        ctm._all_page_names = None
        super().tearDown()

    def test_unlinked_tutorials_and_troubleshooting_are_appended(self):
        write_page("mypkg/Tutorials",
                   "<<FullSearchWithDescriptionsCS(title:\"mypkg/Tutorials/\" TutorialCategory)>>\n")
        write_page("mypkg/Tutorials/Basics",
                   "## title = The Basics\n## description = Learn the basics\nTutorialCategory\n"
                   "= Basics =\n" + "Some real tutorial content here. " * 5 + "\n")
        write_page("mypkg/Troubleshooting",
                   "No troubleshooting tips have been added for this package/stack.\n"
                   "== Error: it breaks ==\n" + "Restart the node and check the cable. " * 4 + "\n")
        write_page("mypkg/FAQ", "= FAQ =\n<<NewPage(x)>>\n")  # template only
        src = write_page("mypkg", "== Overview ==\nNo links to subpages here.\n")
        stats = {}
        with patch("builtins.print"):
            md = ctm.convert_file(src, stats=stats)
        self.assertEqual(stats["subpages"], [
            "mypkg/Tutorials", "mypkg/Troubleshooting", "mypkg/Tutorials/Basics"])
        self.assertIn("## Tutorials", md)
        self.assertIn("## The Basics", md)
        self.assertIn("## Troubleshooting", md)
        self.assertIn("Restart the node", md)
        self.assertNotIn("No troubleshooting tips", md)
        self.assertNotIn("## FAQ", md)

    def test_empty_standard_subpages_skipped(self):
        write_page("mypkg/Tutorials",
                   "<<FullSearchWithDescriptionsCS(title:\"mypkg/Tutorials/\" TutorialCategory)>>\n"
                   "'''Create a new tutorial:''' <<NewPage(x)>>\n")
        write_page("mypkg/Troubleshooting",
                   "No troubleshooting tips have been added for this package/stack.\n")
        self.assertFalse(ctm.has_real_content("mypkg/Tutorials"))
        self.assertFalse(ctm.has_real_content("mypkg/Troubleshooting"))
        self.assertFalse(ctm.has_real_content("mypkg/Missing"))

    def test_excluded_subpages(self):
        for rel in ["Reviews", "Reviews/2010-07-28_API_Review", "ChangeList",
                    "ChangeList/1.0", "cturtle", "Electric", "melodic",
                    "5-28-2009_API_Review", "Tutorials/Doc_Review"]:
            self.assertTrue(ctm.is_excluded_subpage(rel), rel)
        for rel in ["Tutorials", "Troubleshooting", "FAQ", "Plugins", "noetic",
                    "Tutorials/Getting Started"]:
            self.assertFalse(ctm.is_excluded_subpage(rel), rel)

    def test_excluded_subpage_links_not_appended(self):
        write_page("mypkg/Reviews", "Review notes " * 20 + "\n")
        write_page("mypkg/cturtle", "Old content " * 20 + "\n")
        src = write_page("mypkg", "See [[/Reviews]] and [[mypkg/cturtle]].\n")
        stats = {}
        with patch("builtins.print"):
            md = ctm.convert_file(src, stats=stats)
        self.assertEqual(stats["subpages"], [])
        self.assertNotIn("Review notes", md)
        # falls back to the package's index.ros.org page
        self.assertIn("https://index.ros.org/p/mypkg", md)


class TestCommitAttachments(WikiDumpTestCase):
    def test_single_commit_with_blobs(self):
        calls = []

        def fake_api(url, method="GET", data=None, token=None, accept_statuses=None):
            calls.append((method, url, data))
            if url.endswith("/git/blobs"):
                return {"sha": f"blob{len(calls)}"}
            if "/git/ref/heads/" in url:
                return {"object": {"sha": "parent"}}
            if url.endswith("/git/commits/parent"):
                return {"tree": {"sha": "basetree"}}
            if url.endswith("/git/trees"):
                return {"sha": "newtree"}
            if url.endswith("/git/commits"):
                return {"sha": "newcommit"}
            return {}

        attachments = {"doc/diagram.png": "pages/mypkg/attachments/diagram.png",
                       "doc/existing.png": "pages/mypkg/attachments/diagram.png"}

        def fake_existing(owner, repo, path, branch, token):
            return ("x", "sha") if path.endswith("existing.png") else (None, None)

        with patch("submit_prs.github_api_request", side_effect=fake_api), \
             patch("submit_prs.get_existing_file_on_branch", side_effect=fake_existing), \
             patch("builtins.print"):
            sha, uploaded = submit_prs.commit_attachments(
                "fork", "repo", "br", "pkg_dir", attachments, "mypkg", "tok")

        self.assertEqual(sha, "newcommit")
        self.assertEqual(uploaded, ["pkg_dir/doc/diagram.png"])
        tree_call = [c for c in calls if c[1].endswith("/git/trees")][0]
        self.assertEqual(tree_call[2]["base_tree"], "basetree")
        self.assertEqual([e["path"] for e in tree_call[2]["tree"]],
                         ["pkg_dir/doc/diagram.png"])
        self.assertEqual(calls[-1][0], "PATCH")
        self.assertEqual(calls[-1][2], {"sha": "newcommit"})

    def test_load_attachments_manifest(self):
        os.makedirs("markdown_output")
        with open("markdown_output/mypkg.attachments.yaml", "w") as f:
            yaml.safe_dump({"doc/a.png": "pages/mypkg/attachments/a.png"}, f)
        self.assertEqual(
            submit_prs.load_attachments("markdown_output/mypkg.md"),
            {"doc/a.png": "pages/mypkg/attachments/a.png"},
        )
        self.assertEqual(submit_prs.load_attachments("markdown_output/other.md"), {})
        self.assertEqual(
            submit_prs.get_attachment_repo_path("", "doc/a.png"), "doc/a.png")


if __name__ == "__main__":
    unittest.main()
