import os
import sys
import unittest
from unittest.mock import mock_open, patch

# Add the directory containing the script to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from convert_to_markdown import (
    preprocess,
    quote_wikiname_fs,
    resolve_page_name,
    unquote_wikiname_fs,
)


class TestIncludeMacro(unittest.TestCase):
    @patch("os.path.exists")
    def test_include_success(self, mock_exists):
        # Setup mocks
        def exists_side_effect(path):
            if path == "pages/IncludedPage/current":
                return True
            if path == "pages/IncludedPage/revisions/00000002":
                return True
            return False

        mock_exists.side_effect = exists_side_effect

        mock_files = {
            "pages/IncludedPage/current": mock_open(read_data="00000002\n").return_value,
            "pages/IncludedPage/revisions/00000002": mock_open(
                read_data="Included Content"
            ).return_value,
        }

        def open_side_effect(path, *args, **kwargs):
            if path in mock_files:
                return mock_files[path]
            raise FileNotFoundError(path)

        with patch("builtins.open", side_effect=open_side_effect):
            content = "Some text <<Include(IncludedPage)>> more text"
            preprocessed, code_blocks = preprocess(content)

            self.assertEqual(
                preprocessed, "Some text Included Content more text"
            )

    @patch("os.path.exists")
    def test_include_missing_current(self, mock_exists):
        mock_exists.return_value = False

        content = "Some text <<Include(IncludedPage)>> more text"
        preprocessed, code_blocks = preprocess(content)

        self.assertIn(
            "[[Included page IncludedPage not found]]", preprocessed
        )

    @patch("os.path.exists")
    def test_include_recursive(self, mock_exists):
        def exists_side_effect(path):
            valid_paths = [
                "pages/PageA/current",
                "pages/PageA/revisions/00000001",
                "pages/PageB/current",
                "pages/PageB/revisions/00000002",
            ]
            return path in valid_paths

        mock_exists.side_effect = exists_side_effect

        mock_files = {
            "pages/PageA/current": mock_open(read_data="00000001\n").return_value,
            "pages/PageA/revisions/00000001": mock_open(
                read_data="Content A <<Include(PageB)>>"
            ).return_value,
            "pages/PageB/current": mock_open(read_data="00000002\n").return_value,
            "pages/PageB/revisions/00000002": mock_open(
                read_data="Content B"
            ).return_value,
        }

        def open_side_effect(path, *args, **kwargs):
            if path in mock_files:
                return mock_files[path]
            raise FileNotFoundError(path)

        with patch("builtins.open", side_effect=open_side_effect):
            content = "<<Include(PageA)>>"
            preprocessed, code_blocks = preprocess(content)

            self.assertEqual(preprocessed, "Content A Content B")

    @patch("os.path.exists")
    def test_include_infinite_loop(self, mock_exists):
        def exists_side_effect(path):
            valid_paths = [
                "pages/PageA/current",
                "pages/PageA/revisions/00000001",
                "pages/PageB/current",
                "pages/PageB/revisions/00000002",
            ]
            return path in valid_paths

        mock_exists.side_effect = exists_side_effect

        mock_files = {
            "pages/PageA/current": mock_open(read_data="00000001\n").return_value,
            "pages/PageA/revisions/00000001": mock_open(
                read_data="Content A <<Include(PageB)>>"
            ).return_value,
            "pages/PageB/current": mock_open(read_data="00000002\n").return_value,
            "pages/PageB/revisions/00000002": mock_open(
                read_data="Content B <<Include(PageA)>>"
            ).return_value,
        }

        def open_side_effect(path, *args, **kwargs):
            if path in mock_files:
                return mock_files[path]
            raise FileNotFoundError(path)

        with patch("builtins.open", side_effect=open_side_effect):
            content = "<<Include(PageA)>>"
            preprocessed, code_blocks = preprocess(content)

            self.assertTrue(len(preprocessed) > 0)

    @patch("os.path.exists")
    def test_include_subpage_encoded_path(self, mock_exists):
        valid_paths = [
            "pages/bond(2f)Overview/current",
            "pages/bond(2f)Overview/revisions/00000003",
        ]
        mock_exists.side_effect = lambda p: p in valid_paths
        file_data = {
            "pages/bond(2f)Overview/current": "00000003\n",
            "pages/bond(2f)Overview/revisions/00000003": "Bond overview",
        }

        def open_side_effect(path, *args, **kwargs):
            if path in file_data:
                return mock_open(read_data=file_data[path]).return_value
            raise FileNotFoundError(path)

        with patch("builtins.open", side_effect=open_side_effect):
            for macro in [
                "<<Include(bond/Overview)>>",
                '<<Include("bond/Overview", , from="x")>>',
                "<<Include(/Overview)>>",
            ]:
                preprocessed, _ = preprocess(macro, current_page="bond")
                self.assertEqual(preprocessed, "Bond overview", macro)


class TestWikinameQuoting(unittest.TestCase):
    @patch("os.path.exists", return_value=True)
    def test_include_in_dropped_version_block_not_expanded(self, _):
        included = "{{{#!clearsilver\nnode.0 {\n}\n}}}\nOLD DISTRO"

        def open_side_effect(path, *args, **kwargs):
            data = "00000001\n" if path.endswith("current") else included
            return mock_open(read_data=data).return_value

        content = (
            "Intro\n{{{#!wiki version diamondback\n<<Include(pkg/diamondback)>>\n}}}\n"
            "Outro"
        )
        with patch("builtins.open", side_effect=open_side_effect):
            preprocessed, _ = preprocess(content, current_page="pkg")
        self.assertNotIn("OLD DISTRO", preprocessed)
        self.assertNotIn("clearsilver", "".join(_))
        self.assertIn("Outro", preprocessed)
    def test_quote(self):
        self.assertEqual(quote_wikiname_fs("bond/Overview"), "bond(2f)Overview")
        self.assertEqual(
            quote_wikiname_fs("bond/Reviews/2010-07-28_API_Review"),
            "bond(2f)Reviews(2f)2010(2d)07(2d)28_API_Review",
        )
        self.assertEqual(
            quote_wikiname_fs("kobuki_ftdi/Tutorials/Udev Rules"),
            "kobuki_ftdi(2f)Tutorials(2f)Udev(20)Rules",
        )
        self.assertEqual(quote_wikiname_fs("a/-b"), "a(2f2d)b")

    def test_unquote(self):
        self.assertEqual(unquote_wikiname_fs("bond(2f)Overview"), "bond/Overview")

    def test_resolve_relative(self):
        self.assertEqual(resolve_page_name("/Sub", "a/b"), "a/b/Sub")
        self.assertEqual(resolve_page_name("../Sib", "a/b"), "a/Sib")
        self.assertEqual(resolve_page_name("Abs", "a/b"), "Abs")


if __name__ == "__main__":
    unittest.main()
