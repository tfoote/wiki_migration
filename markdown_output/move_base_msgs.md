## Overview

This package contains the messages used to communicate with the
[move_base](move_base) node. These messages are auto-generated from the
`MoveBase.action` action specification. For more information on
actions see [ actionlib documentation](actionlib ), for more information
on the [move_base](move_base) node see
[ move_base documentation](move_base ).

## MoveBase.action



```
geometry_msgs/PoseStamped target_pose
---
---
geometry_msgs/PoseStamped base_position
```



The `target_pose` is the goal that the navigation stack attempts to
achieve. The `base_position` given as feedback is the current position
of the base in the world as reported by [tf](tf). For the
[move_base](move_base) node, the `target_pose` is projected into the
XY plane with the Z axis pointing up when attempting to achieve a goal.

<<MsgSrvDoc(move_base_msgs)>>
