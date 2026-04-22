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


    def test_youtube_params(self):
        content = "Some text <<Youtube(8Adrn29BVbM&rel=0)>> more text"
        preprocessed, code_blocks = preprocess(content)
        self.assertEqual(
            preprocessed,
            "Some text [[https://www.youtube.com/watch?v=8Adrn29BVbM&rel=0|Youtube]] more text",
        )

    def test_postprocess_extra_escapes(self):
        content = r"robot\_namespace, \`code\`, \<tag\>"
        processed = postprocess(content, [])
        self.assertEqual(processed, "robot_namespace, `code`, <tag>")


    def test_postprocess_code_block_spacing(self):
        content = "Some text PLACEHOLDER_CODE_BLOCK_0 more text"
        code_blocks = ["Code content"]
        
        processed = postprocess(content, code_blocks)
        
        self.assertEqual(processed, "Some text \n\n```\nCode content\n```\n\n more text")


    def test_msglink_conversion(self):
        content = "Some text <<MsgLink(sensor_msgs/JointState)>> more text"
        preprocessed, code_blocks = preprocess(content)
        self.assertEqual(
            preprocessed,
            "Some text [[https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html|sensor_msgs/msg/JointState]] more text",
        )


    def test_srvlink_conversion(self):
        content = "Some text <<SrvLink(std_srvs/Empty)>> more text"
        preprocessed, code_blocks = preprocess(content)
        self.assertEqual(
            preprocessed,
            "Some text [[https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html|std_srvs/srv/Empty]] more text",
        )


if __name__ == "__main__":
    unittest.main()
