sbpl_3dnav_planner is a ROS wrapper for
[SBPL Full-Body Planner](http://www.ros.org/wiki/sbpl_full_body_planner)
library to provide 3D navigation with full-body collision checking to
[move_base](http://www.ros.org/wiki/move_base). It adheres to the
nav_core::BaseGlobalPlanner interface specified in
[nav_core](http://ros.org/wiki/nav_core).

**Source of SBPL Full-Body Planner:**

** (for ROS Electric only) **

**git clone
<https://sbpl.pc.cs.cmu.edu/redmine/people/mike/full-body-nav.git>**

## Overview

The \`sbpl_3dnav_planner::Sbpl3DNavPlanner\` is a global planner that
adheres to the nav_core::BaseGlobalPlanner interface found in the
[nav_core](http://www.ros.org/wiki/nav_core) package and can be used as
a global planner [plugin](http://www.ros.org/wiki/pluginlib) for the
[move_base](http://www.ros.org/wiki/move_base) node. It performs
three-dimensional full-body collision checking to compute paths that are
collision-free with the environment.

### The New Collision Model

The PR2 makes dancing look easy\...

![](attachment:pr2_shuffle.gif)

## Sbpl3DNavPlanner

### API Stability

-   The ROS API is unreviewed.
-   The C++ API is unreviewed.

### ROS Topics

```clearsilver
sub {
    0.name = collision_map_occ
    0.desc = The 3D collision map needed for collision checking against the environment; required since the Costmap2D supplied by [[http://www.ros.org/wiki/move_base|move_base]] is ignored
    0.type = arm_navigation_msgs/CollisionMap

    1.name = joint_states
    1.desc = The current status of all the joints of the robot
    1.type = sensor_msgs/JointState

    2.name = collision_object
    2.desc = Interface to allow individual insertion of collision objects into the 3D collision map
    2.type = arm_navigation_msgs/CollisionObject

    3.name = sbpl_attached_collision_object
    3.desc = Interface to allow insertion of attached collision objects into the robot's collision model
    3.type = arm_navigation_msgs/AttachedCollisionObject
}
```

### ROS Services

```clearsilver
srv {
    0.name = /sbpl_full_body_planning/collision_check
    0.desc = Service to perform collision checking using the robot's collision model and current view of the world
    0.type = sbpl_3dnav_planner/FullBodyCollisionCheck

    1.name = /sbpl_full_body_planning/find_base_poses
    1.desc = Service to compute a set of collision-free robot poses from which the robot can reach a specified object
    1.type = sbpl_3dnav_planner/GetBasePoses
}

srv_called {
    0.name = <left_fk_service_name> (see params)
    0.desc = The service called to compute forward kinematics for the left arm
    0.type = kinematics_msgs/GetPositionFK
    
    1.name = <right_fk_service_name> (see params)
    1.desc = The service called to compute forward kinematics for the right arm
    1.type = kinematics_msgs/GetPositionFK
}
```

### ROS Parameters

```clearsilver
param {
    no_header=True
    # planner params
    0.name    = ~planner/search_mode
    0.desc    = Whether to stop after finding the first solution
    0.type    = bool
    0.default = true    

    1.name    = ~planner/allocated_time
    1.desc    = Amount of time to allow for planning (in seconds)
    1.type    = double    
    1.default = 60.0

    2.name    = ~planner/object_radius
    2.desc    = TODO
    2.type    = double
    2.default = 0.10

    3.name    = ~planner/left_arm_description_file
    3.desc    = File describing the left arm; see package://sbpl_arm_planner/config/pr2_left_arm.cfg for details.
    3.type    = string
    3.default = ""

    4.name    = ~planner/right_arm_description_file
    4.desc    = File describing the right arm; see package://sbpl_arm_planner/config/pr2_right_arm.cfg for details.
    4.type    = string
    4.default = ""

    5.name    = ~planner/motion_primitive_file
    5.desc    = File describing the motion primitives allowed by the robot's arms
    5.type    = string
    5.default = ""

    6.name    = ~planner/base_motion_primitive_file
    6.desc    = File describing the motion primitives allowed by the robot's base
    6.type    = string
    6.default = ""

    7.name    = ~planner/use_shortened_path
    7.desc    = TODO
    7.type    = bool
    7.default = false

    # not used anymore
    #8.name    = ~planner/use_inner_circle_of_object
    #8.desc    = Unused
    #8.type    = bool
    #8.default = true

    # debug params
    9.name    = ~debug/print_out_path
    9.desc    = Whether to print the returned path to ROS_INFO; prints out joint angles and end effector poses for both arms and the (x, y, torso, theta) positions of the base
    9.type    = bool
    9.default = true

    10.name    = ~debug/succesors_logger_level
    10.desc    = Unused
    10.type    = string
    10.default = "info"

    # robot params
    11.name    = ~robot/waypoint_time
    11.desc    = The time it takes to move between waypoints on the returned path
    11.type    = double
    11.default = 0.2

    12.name    = ~robot/arm_name
    12.desc    = Unused
    12.type    = string
    12.default = "right_arm"

    13.name    = robot_description
    13.desc    = The URDF file for the robot
    13.type    = string
    13.default = None (required)

    14.name    = ~robot/num_joints
    14.desc    = The number of joints per arm
    14.type    = int
    14.default = 7

    15.name    = ~reference_frame
    15.desc    = The frame for the returned path and visualizations
    15.type    = string
    15.default = "map"

    16.name    = ~left_fk_service_name
    16.desc    = Name of the service call used to compute forward kinematics for the left arm
    16.type    = string
    16.default = "pr2_left_arm_kinematics/get_fk"

    17.name    = ~left_ik_service_name
    17.desc    = Name of the service call used to compute inverse kinematics for the left arm
    17.type    = string
    17.default = "pr2_left_arm_kinematics/get_ik"

    18.name    = ~right_fk_service_name
    18.desc    = Name of the service call used to compute forward kinematics for the right arm
    18.type    = string
    18.default = "pr2_right_arm_kinematics/get_fk"

    19.name    = ~right_ik_service_name
    19.desc    = Name of the service call used to compute inverse kinematics for the right arm
    19.type    = string
    19.default = "pr2_right_arm_kinematics/get_ik"

    20.name    = ~use_collision_map_from_sensors
    20.desc    = Whether to update the occupancy grid from the `collision_map_occ` topic
    20.type    = bool
    20.default = true

    21.name    = ~right_arm_pose_on_object_x
    21.desc    = The x offset from the right gripper's location to the object's location
    21.type    = double
    21.default = 0.0

    22.name    = ~right_arm_pose_on_object_y
    22.desc    = The y offset from the right gripper's location to the object's location
    22.type    = double
    22.default = -0.15

    23.name    = ~right_arm_pose_on_object_z
    23.desc    = The z offset from the right gripper's location to the object's location
    23.type    = double
    23.default = 0.0

    24.name    = ~left_arm_pose_on_object_x
    24.desc    = The x offset from the left gripper's location to the object's location
    24.type    = double
    24.default = 0.0

    25.name    = ~left_arm_pose_on_object_y
    25.desc    = The y offset from the left gripper's location to the object's location
    25.type    = double
    25.default = 0.15

    26.name    = ~left_arm_pose_on_object_z
    26.desc    = The z offset from the left gripper's location to the object's location
    26.type    = double
    26.default = 0.0

    27.name    = ~minimum_working_distance
    27.desc    = The minimum distance away the robot will be from the object when using the `/sbpl_full_body_planning/find_base_poses` service
    27.type    = double
    27.default = 0.3 (in meters)

    28.name    = ~maximum_working_distance
    28.desc    = The maximum distance away the robot will be from the object when using the `/sbpl_full_body_planning/find_base_poses` service (in meters)
    28.type    = double
    28.default = 0.7

    29.name    = ~yaw_steps
    29.desc    = The number of angles to sample when using the `/sbpl_full_body_planning/find_base_poses` service; samples will be made uniformly from 0 to 2*pi
    29.type    = int
    29.default = 16

    30.name    = ~radii_steps
    30.desc    = The number of radii to sample when using the `/sbpl_full_body_planning/find_base_poses` service; samples will be made uniformly along the available workspace of the robot (obeying the maximum and minimum working distances parameters)
    30.type    = int
    30.default = 16

    31.name    = ~collision_space/collision_map_topic
    31.desc    = Unused
    31.type    = string
    31.default = collision_map_occ

    32.name    = ~visualizations/goal
    32.desc    = Whether to visualize the goal using PViz when the planner is called
    32.type    = bool
    32.default = true

    33.name    = ~visualizations/expanded_states
    33.desc    = Whether to visualize the state expansions using AViz when the planner is called
    33.type    = bool
    33.default = true

    34.name    = ~visualizations/heuristic
    34.desc    = Whether to visualize the heuristic (the shortest path to the goal) using AViz when the planner is called
    34.type    = bool
    34.default = true

    35.name    = ~visualizations/voxel_size
    35.desc    = Unused
    35.type    = double
    35.default = 0.02

    36.name    = ~visualizations/trajectory
    36.desc    = Whether to visualize the trajectory using PViz when the planner is called
    36.type    = bool
    36.default = false

    37.name    = ~visualizations/end_effector_path
    37.desc    = Whether to visualize the path the end effector takes using AViz when the planner is called
    37.type    = bool
    37.default = false

    38.name    = ~visualizations/collision_model_trajectory
    38.desc    = Unused
    38.type    = bool
    38.default = false

    39.name    = ~visualizations/collision_model
    39.desc    = Whether to visualize the collision model of the robot
    39.type    = bool
    39.default = false

    40.name    = ~visualizations/trajectory_throttle
    40.desc    = Throttle for trajectory visualizations; e.g., a trajectory_throttle of 4 will make it so only every 4th pose will be displayed. Raise this to increase performance
    40.type    = int
    40.default = 4

    41.name    = ~visualizations/heuristic_grid
    41.desc    = Whether to visualize the heuristic grid using AViz when the planner is called; no actual planning will be done if this is set
    41.type    = bool
    41.default = false
}
```
