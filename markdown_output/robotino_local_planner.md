## Overview

The `robotino_local_planner::RobotinoLocalPlanner` is a local planner
for Robotino which complies with the `nav_core::BaseLocalPlanner`
interface.

![](attachment:robotino_navigation_ros.png)

## The RobotinoLocalPlanner

The `robotino_local_planner::RobotinoLocalPlanner` is a simple local
planner that simply follows the path set by the global planner. The
`RobotinoLocalPlanner` looks for a next heading point on the global
plan (which can be set as a parameter. See below.) and calculates and
publishes linear and angular velocites for Robotino on the
`/robotino_cmd_vel` topic.

The collision avoidance is carried out by the `robotino_safety_node`
from the [robotino_safety](robotino_safety) package which is subscribed
to the `/robotino_cmd_vel` topic.

### Usage

The `robotino_local_planner::RobotinoLocalPlanner` is loaded as a
local planner plugin for the [move_base](move_base) node by default when
launching the `navigation.launch` file from the
[robotino_navigation](robotino_navigation) package.

### ROS Parameters

```clearsilver
param {
  no_header=True
  0.name = ~heading_lookahead
  0.default = 0.3
  0.type = double 
  0.desc = The minimum distance [m] between the center of Robotino and the next heading point from the global plan.
  1.name = ~max_linear_vel
  1.default = 0.3
  1.type = double
  1.desc = The maximum linear velocity [m/s] allowed for Robotino during navigation.
  2.name = ~min_linear_vel
  2.default = 0.1
  2.type = double
  2.desc = The minimum linear velocity [m/s] allowed for Robotino during navigation.
  3.name = ~max_rotation_vel
  3.default = 1.0
  3.type = double
  3.desc = The maximum rotational velocity [rad/s] allowed for Robotino during navigation.
  4.name = ~min_rotation_vel
  4.default= 0.3
  4.type = double
  4.desc = The minimum rotational velocity [rad/s] allowed for Robotino during navigation.
  5.name = ~yaw_goal_tolerance
  5.default= 0.05
  5.type = double
  5.desc = The tolerance in radians for the controller in yaw/rotation when achieving its goal.
  6.name = ~xy_goal_tolerance
  6.default= 0.10
  6.type = double
  6.desc = The tolerance in meters for the controller in the x & y distance when achieving a goal.
}
```
