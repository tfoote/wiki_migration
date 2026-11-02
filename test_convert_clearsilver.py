import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import convert_to_markdown as ctm
from convert_to_markdown import postprocess, preprocess

NODE_API = """{{{
#!clearsilver CS/NodeAPI
name = explore
desc = Explores the map. See [[move_base]].
sub {
  0.name = costmap
  0.type = nav_msgs/OccupancyGrid
  0.desc = Map used for planning.
}
pub{
  0.name= ~frontiers
  0.type= visualization_msgs/MarkerArray
  0.desc= Frontier markers.
}
param {
  0.name = ~robot_base_frame
  0.type = string
  0.default = base_link
  0.desc = Base frame of the robot.
  1.name = ~quoted
  1.type = string
  1.default = `already code`
  1.desc << EOM
Multi-line
description.
EOM
  group.0 {
    name = Tuning
    desc = Tuning knobs.
    0.name = ~gain
    0.type = double
    0.desc = Gain.
  }
}
req_tf {
  0.from = map
  0.to = base_link
  0.desc = Robot pose.
}
srv_called.no_header = True
srv_called {
  0.name = ~clear
  0.type = std_srvs/Empty
  0.desc = Clears things.
}
}}}
"""

MULTI_NODE = """{{{
#!clearsilver CS/NodeAPI
node.0 {
  name = first_node
  desc = First.
  pub {
    0.name = out
    0.type = std_msgs/String
    0.desc = Output.
  }
}
node.1 {
  name = second_node
  srv {
    0.name = reset
    0.type = std_srvs/Empty
    0.desc = Reset.
  }
}
}}}
"""

TUTORIAL = """## note.0= [[ROS/Tutorials/UnderstandingTopics | understanding ROS topics]]
## title = Writing a Simple Publisher and Subscriber
## description = This tutorial covers writing nodes in C++.
## next =
## next.0.link= [[ROS/Tutorials/WritingServiceClient(c++)|Writing a service]]
## next.1.link=
## level= BeginnerCategory
## keywords = publisher, subscriber
####################################
<<IncludeCSTemplate(TutorialCSHeaderTemplate)>>
== Writing the Publisher Node ==
Body text.
"""


class TestHdfParser(unittest.TestCase):
    def test_parse_nested_dotted_and_multiline(self):
        data = ctm.parse_hdf(
            "name = n\nparam {\n 0.name = a\n 0.desc << EOM\nline 1\nline 2\nEOM\n}\n"
            "node.1 {\n  pub{\n    0.type = x/Y\n  }\n}\n"
        )
        self.assertEqual(data["name"], "n")
        self.assertEqual(data["param"]["0"]["name"], "a")
        self.assertEqual(data["param"]["0"]["desc"], "line 1\nline 2")
        self.assertEqual(data["node"]["1"]["pub"]["0"]["type"], "x/Y")


class TestNodeApi(unittest.TestCase):
    def render(self, text):
        return ctm.expand_clearsilver_blocks(text)

    def test_single_node_sections(self):
        out = self.render(NODE_API)
        self.assertNotIn("clearsilver", out)
        self.assertIn("=== explore ===", out)
        self.assertIn("Explores the map. See [[move_base]].", out)
        self.assertIn("==== Subscribed Topics ====", out)
        self.assertIn(" * {{{costmap}}} (<<MsgLink(nav_msgs/OccupancyGrid)>>): Map used for planning.", out)
        self.assertIn("==== Published Topics ====", out)
        self.assertIn(" * {{{~robot_base_frame}}} ({{{string}}}, default: {{{base_link}}}): Base frame of the robot.", out)
        self.assertIn("default: `already code`)", out)          # not double-wrapped
        self.assertIn(": Multi-line description.", out)          # EOM joined
        self.assertIn("===== Tuning =====", out)
        self.assertIn("Tuning knobs.", out)
        self.assertIn("==== Required tf Transforms ====", out)
        self.assertIn(" * {{{map}}} → {{{base_link}}}: Robot pose.", out)
        self.assertNotIn("Services Called", out)                  # no_header
        self.assertIn(" * {{{~clear}}} (<<SrvLink(std_srvs/Empty)>>): Clears things.", out)
        # Section order follows the wiki template.
        self.assertLess(out.index("Subscribed Topics"), out.index("Published Topics"))
        self.assertLess(out.index("Published Topics"), out.index("Parameters"))

    def test_values_with_markup_not_double_wrapped(self):
        out = self.render(
            "{{{\n#!clearsilver CS/NodeAPI\nprov_tf {\n"
            "  0.from = <value of ~frame> (typ: `base_link`)\n  0.to = odom\n  0.desc = d\n}\n"
            "param {\n  0.type = int\n  0.default = 0\n  0.desc = No name.\n}\n}}}\n")
        self.assertIn(" * <value of ~frame> (typ: `base_link`) → {{{odom}}}: d", out)
        self.assertIn(" * ({{{int}}}, default: {{{0}}}): No name.", out)

    def test_multiple_nodes(self):
        out = self.render(MULTI_NODE)
        self.assertIn("=== first_node ===", out)
        self.assertIn("=== second_node ===", out)
        self.assertLess(out.index("first_node"), out.index("second_node"))
        self.assertIn("==== Services ====", out)

    def test_end_to_end_markdown(self):
        pre, blocks = preprocess("== ROS API ==\n" + NODE_API, current_page="explore_lite")
        import subprocess
        md = postprocess(subprocess.run(["pandoc", "-f", "creole", "-t", "markdown"],
                                        input=pre.encode(), capture_output=True).stdout.decode(), blocks)
        self.assertIn("### explore", md)
        self.assertIn("#### Subscribed Topics", md)
        self.assertIn("`costmap`", md)
        self.assertIn("https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html", md)
        self.assertNotIn("```", md)


class TestTutorialHeader(unittest.TestCase):
    def test_header_rendered_from_fields(self):
        out = ctm.expand_tutorial_header(TUTORIAL)
        self.assertNotIn("IncludeCSTemplate", out)
        self.assertIn(" * '''Note:''' This tutorial assumes that you have completed the "
                      "previous tutorials: [[ROS/Tutorials/UnderstandingTopics | "
                      "understanding ROS topics]].", out)
        self.assertIn(" * '''Description:''' This tutorial covers writing nodes in C++.", out)
        self.assertIn(" * '''Keywords:''' publisher, subscriber", out)
        self.assertIn(" * '''Tutorial Level:''' BEGINNER", out)
        self.assertIn(" * '''Next Tutorial:''' [[ROS/Tutorials/WritingServiceClient(c++)|"
                      "Writing a service]]", out)

    def test_custom_note_and_no_level(self):
        out = ctm.render_tutorial_header("## note = Requires a robot\n## title = X\n")
        self.assertEqual(out, " * '''Note:''' Requires a robot.")

    def test_header_survives_preprocess(self):
        pre, _ = preprocess(TUTORIAL, current_page="pkg/Tutorials/Pub")
        self.assertIn("**Tutorial Level:** BEGINNER", pre)
        self.assertNotIn("## title", pre)
        # padded link "[[ target | label ]]" is normalized
        self.assertIn("[[ROS/Tutorials/UnderstandingTopics|understanding ROS topics]]", pre)


if __name__ == "__main__":
    unittest.main()
