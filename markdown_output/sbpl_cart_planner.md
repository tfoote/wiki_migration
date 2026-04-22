## Overview

Provides a [move_base](move_base) global-planner plugin, that uses
anytime ARA\* search as implemented by the [sbpl](sbpl) motion planner.
In addition to finding a global plan for the base as required by move
base, it also publishes a corresponding plan for the cart. The planner
is currently configured to plan in (x,y,theta,cartangle) space where
(x,y,theta) is the position and orientation of the robot base. The cart
angle is the articulation angle of the cart about an (imaginary) pivot
point that can be configured using ROS parameters (below). Currently,
the planner plans only from and to states where the cart angle is zero.

## ROS interface

### Advertised topics

`sbpl_robot_cart_plan`
([cart_pushing_msgs/msg/RobotCartPath](https://docs.ros.org/en/rolling/p/cart_pushing_msgs/msg/RobotCartPath.html))
Whenever planning is done, a corresponding plan for the base and cart is
published on this topic.

`sbpl_plan_array`
([visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html))
This is used to visualize the plan as a series of arrows with green
arrows representing the path of the robot and red arrows representing
the path of the cart.

`sbpl_plan_footprint`
([visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html))
This is used to visualize the plan as a series of robot and cart
polygons. The visualizer_skip_poses parameter below affects the density
of waypoints displayed.

### Main ROS parameters

#### Cart parameters

These are in the `cart_pushing` namespace.

`{length, width}` cart dimensions `footprint_{x,y}_offset` offset
of cart reference point from corner `cart_init_pose/position` Initial
position of cart reference point.

#### Planner parameters

These are in the private namespace of the plugin.

`allocated_time` default: 10.0 Max time (seconds) the planner is
allowed to take `initial_epsilon` default: 3.0 Initial epsilon
parameter to ARA\* algorithm (higher epsilon means start off with a very
fast, suboptimal search) `environment_type` default: XYThetaLattice
This is currently the only option and should not be changed
`planner_type` default: ARAPlanner This is currently the only option
and should not be changed `forward_search` default: false If false,
backwards search will be performed to the goal. This is the preferable
mode. `cart_pivot_offset\\x` default: 0.6 The x offset of the
imaginary pivot point for the cart in the base_footprint frame of the
robot. This is the point around which the planner will articulate the
cart. `cart_pivot_offset\\y` default: 0.0 The y offset of the
imaginary pivot point for the cart in the base_footprint frame of the
robot. This is the point around which the planner will articulate the
cart. `visualizer_skip_poses` default: 10 This parameter controls the
number of waypoints that are displayed on the sbpl_plan_footprint topic.
A parameter value of 1 will display every single waypoint while a
parameter value of 10 will display every 10th waypoint.
`primitive_filename` default="\$(find
sbpl_cart_planner)/launch/pr2_cart_articulate.mprim" /> This is the
motion primitive filename. This parameter must point to a valid motion
primitive file.

#### Configuration file location

By default, these parameters are launched from the
sbpl_cart_planner/launch/move_base/sbpl_global_planner.yaml file.

### Configuring the motion primitives

There are currently two sets of motion primitive files available for
cart pushing.

-   sbpl_cart_planner/launch/pr2_cart_articulate.mprim - This set of
    primitives includes *articulation* primitives that allow the robot
    to articulate the cart about the articulation point defined by the
    parameters above.
-   sbpl_cart_planner/launch/pr2_cart.mprim - This set of primitives
    encodes basic motions of the PR2+cart system. It allows for forward,
    backwards, rotation in place and sideways strafing. It essentially
    models the robot+cart as a long robot with no articulation
    capabilities.

### Sample path

![width=10](attachment:sbpl_cart_plan.png)
