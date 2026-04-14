\'\'\'Note:\'\'\' This package has been integrated into the ROS
[navigation](navigation) stack as of E-Turtle.

## Overview

A modified version of [move_base](move_base) that runs the global
planner in parallel with the local planner (in a separate thread). The
two planners run on two user-defined frequencies. Running the global
planner on a clock is particularly useful in changing environments (or
environments that are only partially known in advance). It can also
recover quicker when the local planner deviates from the path too much,
since it doesn\'t need to stop while a new plan is made. The global
planner replans on a clock and the local planner always follows the most
recent path produced by the global planner. The hand-off is done with an
efficient triple-buffer system with pointer swapping. When the global
planner is not in use (like when the robot has arrived at the goal, or
if the user wants the node to behave like the original move_base) the
planner thread suspends itself until it is needed again.

## ROS API

This list only includes new parameters. The rest of the parameters (as
well as subscribers and publishers) can be found at the
[move_base](move_base) package this one is based on.

```clearsilver
param {
  0.name = planner_frequency
  0.default = 0.0
  0.type = double
  0.desc = This is the desired frequency for the global planner. If the value is less than or equal to 0, the node works like the original move_base (only plan when there is a new goal or the local planner fails). By default this node operates like the original move_base.
}
```
