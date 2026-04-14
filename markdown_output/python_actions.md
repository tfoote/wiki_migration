## Overview

A module for creating Python [robot_actions](robot_actions)

Minimal example:

```
from python_actions import Action
from std_msgs.msg import Empty
from robot_actions.msg import NoArgumentsActionState

class TinyAction(Action):

  def execute(self, goal):
    self.feedback = Empty()
    count = 1
    while not self.isPreemptRequested() and (count <= 10):
      time.sleep(0.1)
      print "PYTHON HELLO, count is", count
      count += 1
      self.update()
    if self.isPreemptRequested():
      return python_actions.PREEMPTED
    else:
      return python_actions.SUCCESS

rospy.init_node("tiny")
w = TinyAction("tiny", Empty, NoArgumentsActionState, Empty)
w.run()
rospy.spin();
```
