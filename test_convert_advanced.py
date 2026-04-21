import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from convert_to_markdown import preprocess, postprocess


class TestAdvancedConversion(unittest.TestCase):

    def test_four_quotes(self):
        content = "Some text ''''bold mono'''' more text"
        preprocessed, code_blocks = preprocess(content)
        self.assertEqual(preprocessed, "Some text **{{{bold mono}}}** more text")

    def test_postprocess_escapes(self):
        content = "robot\\'s TF tree and \\\"manual\\\" mode"
        # Simulate postprocess call on text without code blocks
        processed = postprocess(content, [])
        self.assertEqual(processed, "robot's TF tree and \"manual\" mode")

    def test_postprocess_ignores_code_blocks(self):
        # Simulate content with a placeholder
        content = "Text with placeholder PLACEHOLDER_CODE_BLOCK_0"
        code_blocks = ["\nContent with \\'escapes\\' in code\n"]
        
        processed = postprocess(content, code_blocks)
        
        # The placeholder should be replaced with a fenced code block
        # And the content inside should keep its escapes!
        self.assertIn("```\nContent with \\'escapes\\' in code\n```", processed)


if __name__ == "__main__":
    unittest.main()
