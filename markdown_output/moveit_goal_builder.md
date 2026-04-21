## Overview

`moveit_goal_builder` is a library for building
[MoveGroup action goals](http://docs.ros.org/api/moveit_msgs/html/action/MoveGroup.html).
This is useful for when you want to use the MoveGroup actionlib
interface directly, instead of using the MoveGroup class. This allows
you to poll when the action is done, which the normal MoveGroup
interface does not allow you to do.

## C++ example

To build a goal, create a new moveit_goal_builder::Builder, add a goal,
some constraints, and set other options. Then, call `Build()`:



```cplusplus
#include "moveit_goal_builder/builder.h"

moveit_goal_builder::Builder builder("base_link", "arms");
builder.AddPoseGoal("r_wrist_roll_link", pose);
builder.AddPathOrientationConstraint(orientation_constraint);
builder.planning_time = 10.0;
builder.num_planning_attempts = 2;
builder.can_replan = true;
builder.replan_attempts = 3;

moveit_msgs::MoveGroupGoal goal;
builder.Build(&goal);
```



## Python example



```python
from moveit_goal_builder import MoveItGoalBuilder

builder = MoveItGoalBuilder()
builder.set_pose_goal(pose_stamped)
builder.replan = True
builder.replan_attempts = 10
goal = builder.build()
```



## Differences between C++ and Python

The C++ and Python APIs are similar, but with a few differences:

-   The C++ version supports multi-arm goals, the Python version does
    not.
-   The Python version takes geometry_msgs/PoseStamped messages for the
    pose goal and transforms them when you call `build`. The C++
    version takes geometry_msgs/Pose messages, which are assumed to be
    in the planning frame.
