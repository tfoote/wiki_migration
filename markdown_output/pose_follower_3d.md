## Overview

\'\'NOTE: This package is currently unreleased and contains experimental
code.\'\'

\`pose_follower_3d\` is based on the [pose_follower](pose_follower)
local planner and adheres to the \`nav_core::BaseLocalPlanner\`
interface found in the [nav_core](nav_core) package. It is supposed to
work as a local planner in accordance with the
[sbpl_lattice_planner_3d](sbpl_lattice_planner_3d) in
[move_base](move_base).

pose_follower_3d will try to follow the originally planned poses of the
path as close as possible, while performing 3D collision checks of the
robot\'s full kinematic configuration against a 3D map. This map should
be built and provided by [octomap_server](octomap_server). A
downprojected 2D map for [costmap_2d](costmap_2d) should be also
provided by octomap_server to perform fast checks agains the robot\'s
footprint.

## Documentation

### ROS API

```clearsilver
sub{
  0.name = odom
  0.type = nav_msgs/Odometry
  0.desc = The robot's odometry
  1.name = octomap_collision_object
  1.type = mapping_msgs/CollisionObject
  1.desc = Occupied cells for collision check from octomap_server
 }

pub{
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Holonomic velocity command for the base controller
}

srv_called{
  0.name = /environment_server/get_robot_state
  0.type = planning_environment_msgs/GetRobotState
  0.desc = Requests the robot's current kinematic state at the beginning of each plan
  }

param {
  0.name = ~k_trans
  0.type = float
  0.default = 1.5
  0.desc = Gain for translational velocity

  1.name = ~k_rot
  1.type = float
  1.default = 1.25
  1.desc = Gain for rotational velocity

  2.name = ~max_vel_lin
  2.type = float
  2.default = 0.5
  2.desc = Maximum linear velocity

  3.name = ~min_vel_lin
  3.type = float
  3.default = 0.1
  3.desc = Minimum linear velocity

  4.name = ~max_vel_th
  4.type = float
  4.default = 0.7
  4.desc = Maximum rotational velocity

  5.name = ~min_vel_th
  5.type = float
  5.default = 0.0
  5.desc = Minimum rotational velocity

  6.name = ~in_place_trans_vel
  6.type = float
  6.default = 0.0
  6.desc = Minimum threshold for linear velocity. If it is smaller, the robot rotates only on the spot.

  7.name = ~{trans,rot}_stopped_velocity
  7.type = float
  7.default = 1e-4
  7.desc = If odom reading is slower than this, then robot is stopped

  8.name = ~sim_time
  8.type = float
  8.default = 1.0
  8.desc = How many seconds to forward simulate the current trajectory rollout for collision checking

  9.name = ~sim_granularity
  9.type = float
  9.default = 0.1
  9.desc = How fine to test the forward simulation for collision checks (sim_time/sim_granularity checks will be made)

  10.name = ~samples
  10.type = int
  10.default = 5
  10.desc = How many times a colliding trajectory will be downsampled and checked again, in case it collides. This allows to approach obstacles more closely.

  10.name = ~tolerance_trans
  10.type = float
  10.default = 0.05
  10.desc = How close to follow the originally planned trajectory (translations)

  11.name = ~tolerance_rot
  11.type = float
  11.default = 0.1
  11.desc = How close to follow the originally planned trajectory (rotations)

  12.name = ~tolerance_timeout
  12.type = float
  12.default = 0.5
  12.desc = Timeout tolerance for reaching the goal
}
```
