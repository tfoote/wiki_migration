## Overview

\'\'NOTE: This package is currently unreleased and contains experimental
code.\'\'

\`sbpl_lattice_planner_3d\` is based on the
[sbpl_lattice_planner](sbpl_lattice_planner) global planner and adheres
to the \`nav_core::BaseGlobalPlanner\` interface found in the
[nav_core](nav_core) package. It is supposed to work as a global planner
in accordance with the [pose_follower_3d](pose_follower_3d) local
planner in [move_base](move_base).

sbpl_lattice_planner_3d applies sbpl planning while performing 3D
collision checks of the robot\'s full kinematic configuration against a
3D map. This map should be built and provided by
[octomap_server](octomap_server). A downprojected 2D map for
[costmap_2d](costmap_2d) should be also provided by octomap_server to
perform fast checks agains the robot\'s footprint.

## Documentation

### ROS API

```clearsilver
sub{
  0.name = octomap_collision_object
  0.type = mapping_msgs/CollisionObject
  0.desc = Occupied cells for collision check from octomap_server
  1.name = attached_collision_object
  1.type = mapping_msgs/AttachedCollisionObject
  1.desc = Attached object the robot may carry (experimental)
 }

srv_called{
  0.name = /environment_server/get_robot_state
  0.type = planning_environment_msgs/GetRobotState
  0.desc = Requests the robot's current kinematic state at the beginning of each plan
  }
```

#### Published Topics

See the documentation of [sbpl_lattice_planner](sbpl_lattice_planner)
(the private namespace changed to \`SBPLLatticePlanner3D\`)

#### Parameters

See the documentation of [sbpl_lattice_planner](sbpl_lattice_planner)
(the private namespace changed to \`SBPLLatticePlanner3D\`)
