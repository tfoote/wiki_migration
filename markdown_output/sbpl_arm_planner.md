## Overview

This package contains a new search-based motion planning algorithm for
manipulation.

A detailed explanation of how the planner works can be found in the
following papers. ```
Benjamin Cohen, Gokul Subramanian, Sachin Chitta, and Maxim Likhachev, "Planning for Manipulation with Adaptive Motion Primitives, " Proceedings of the IEEE International Conference on Robotics and Automation (ICRA), 2011.

Benjamin Cohen, Sachin Chitta, and Maxim Likhachev, "Search-based Planning for Manipulation with Motion Primitives, " Proceedings of the IEEE International Conference on Robotics and Automation (ICRA), 2010.
```

One of the notable differences between this planner and the other
popular planning algorithms for manipulation is that the
sbpl_arm_planner plans to a desired goal pose constraint without solving
for an IK solution first. The joint configuration at the desired goal
pose will be determined by the cost function used by the planner.

### How to Use It

This planner is intended to be used with the
[sbpl_arm_planner_node](sbpl_arm_planner_node) interface.

### Videos

The following video shows the PR2 manipulating an 80cm stick through a
window that is 86cm wide.

[Youtube](https://www.youtube.com/watch?v=KrMsyDVWo8A)

The following video is somewhat repetitive. It\'s intended to show you
that the planner is robust in cluttered environments. First the PR2
plans a couple of paths to navigate the gripper between shelves of the
cabinet. Then, The PR2 navigates the gripper above and below a tabletop
with obstacles on it.

[Youtube](https://www.youtube.com/watch?v=AmpbvymDQwk)

## ROS API

### API Stability

-   ROS API is UNREVIEWED and UNSTABLE
-   C++ API is UNREVIEWED and UNSTABLE

### Shortcomings

-   This planner has been developed for the PR2 only. Some changes would
    have to be made to make it robot agnostic.
-   This planner cannot deal with path constraints.
-   This planner cannot deal with goal joint constraints (our main focus
    is in planning to goal pose constraints).
-   This planner cannot deal with goal region constraints besides a
    cube.
-   Until the grasping pipeline can handle pose constraints without
    using IK - this planner cannot be used with the grasping pipeline.

### ROS Topics

#### Subscribed Topics

```clearsilver
sub {
  no_header= True
  0.name= collision_map_occ
  0.type= mapping_msgs/CollisionMap
  0.desc= A 3D occupancy grid of the surrounding environment
  1.name= collision_object
  1.type= mapping_msgs/CollisionObject
  1.desc= Objects in the environment that are known. They get added to the collision map.
  2.name= attached_collision_object
  2.type= mapping_msgs/AttachedCollisionObject
  2.desc= Objects that were added to the robot model - usually objects that the robot grasped. They get added to the robot's collision model.
```

#### Published Topics

```clearsilver
pub {
  no_header= True
  0.name= visualization_marker
  0.type= visualization_msgs/Marker
  0.desc= The goal pose and if enabled, the pose(position and orientation) of each node in the graph expanded during the search. 
}
pub {
  no_header= True
  1.name= visualization_marker_array
  1.type= visualization_msgs/MarkerArray
  1.desc= The position of each node in the graph expanded during the search. If enabled, the path suggested by the heuristic function from the start position to the goal can be displayed.
}
```

### Services Offered

```clearsilver
srv{
 no_header= True
 0.name = /sbpl_planning/plan_path
 0.type = motion_planning_msgs/GetMotionPlan
 0.desc = This service accepts planning requests and returns trajectories. Note: In its current form the planner will only attempt to plan a path for a goal position constraint. Direct requests to the planner with pose constraints will be handled correctly but pose constraint requests to move_arm need to have the 'disable_ik' flag set to true to be forwarded to the planner service correctly.
}
```

### ROS Parameters

#### Planner

##### General

```clearsilver
param {
  no_header= True
  0.name= ~/planner/search_mode
  0.default= true
  0.type= bool
  0.desc= Return first solution found.
  1.name= ~/planner/epsilon
  1.default= 100.0
  1.type= double
  1.desc= The initial epsilon to be used by the planner. Epsilon is the bounds on the suboptimality of the solution.
  2.name= ~/planner/verbose
  2.default= false
  2.type= bool
  2.desc= If true, a lot of descriptive information is printed out before the search that describes the arm configuration, motion primitives, planner settings. A tolerable amount of data is printed out during the search.
  3.name= ~/planner/use_dijkstra_heuristic
  3.default= true
  3.type= bool
  3.desc= For the heuristic function, use the 3D distance to the goal calculated by Dijkstra's algorithm. If set to false, the Euclidean distance is used.
  4.name= ~/planner/use_research_heuristic
  4.default= true
  4.type= bool
  4.desc= For the heuristic function, use the 3D distance from the elbow position to any of the possible elbow poses when the end effector is at the goal pose.
  5.name= ~/planner/use_uniform_obstacle_cost
  5.default= false
  5.type= bool
  5.desc= If true, it doesn't include a "distance to the nearest obstacle" cost in the cost function. If false, it tries to stay away from obstacles (may take longer to plan).
  6.name= ~/planner/use_multiresolution_motion_primitives
  6.default= true
  6.type= bool
  6.desc= If true, use one set of primitives when at least ''n'' meters from the goal, and a different set (usually with smaller motions) when closer to the goal. If false, use the same for the entire search.
  7.name= ~/planner/arm_description_file
  7.default= 
  7.type= string
  7.desc= Path to the arm description text file.
  8.name= ~/planner/motion_primitive_file
  8.default= 
  8.type= string
  8.desc= Path to the motion primitive text file.
}
}
```

##### Research

```clearsilver
param {
  no_header= True
  0.name= ~/planner/research/solve_with_ik_threshold
  0.default= 0.10
  0.type= double
  0.desc= The distance (meters) from the goal to start trying to solve for the goal pose using IK. Note: IK is pretty fast to compute but checking for collisions along the interpolated path to the goal from the current node's configuration takes time and so IK should not be called too far from the goal in a cluttered environment.
  1.name= ~/planner/research/sum_heuristics
  1.default= false
  1.type= bool
  1.desc= If true, sum the end effector heuristic and elbow heuristic. If false, then take the maximum between the two.
  2.name= ~/planner/research/short_distance_mprims_threshold
  2.default= 0.2
  2.type= double
  2.desc= The distance in meters from the goal pose, when the search should switch to the short distance motion primitives.
}
```

##### Debug

```clearsilver
param {
  no_header= True
  0.name= ~/debug/print_out_path
  0.default= true
  0.type= bool
  0.desc= Print the path to the terminal.
}
```

#### Robot Model

```clearsilver
param {
  no_header= True
  0.name= ~robot_description
  0.default= robot_description
  0.type= string
  0.desc= The name of the ROS parameter that contains the URDF robot description of the robot.
  1.name= ~/robot/num_joints
  1.default= 7
  1.type= int
  1.desc= The number of joints that are being planned for.
  2.name= ~/robot/arm_name
  2.default= right_arm
  2.type= string
  2.desc= The name of the collision link group in the URDF that will be used for kinematic calculations and collision checking.
  3.name= ~planning_frame
  3.default= base_link
  3.type= string
  3.desc= The name of the reference frame used during planning. Note: At the moment, the collision map must be received in this frame as well.
  4.name= ~fk_service_name
  4.default= pr2_right_arm_kinematics/get_fk
  4.type= string
  4.desc= The name of the forward kinematics service.
  5.name= ~ik_service_name
  5.default= pr2_right_arm_kinematics/get_ik
  5.type= string
  5.desc= The name of the inverse kinematics service.
}
```

##### Collision Space

```clearsilver
param {
  no_header= True
  0.name= ~/collision_space/reference_frame
  0.default= base_link
  0.type= string
  0.desc= The reference frame used for the collision map.
  1.name= ~/collision_space/resolution
  1.default= 0.02
  1.type= double
  1.desc= The resolution of the occupancy grid.
  2.name= ~/collision_space/collision_map_topic
  2.default= collision_map_occ
  2.type= string
  2.desc= The topic of type mapping_msgs/CollisionMap, that the collision_map is being published on.
  3.name= ~/collision_space/occupancy_grid/origin_x
  3.default= -0.6
  3.type= double
  3.desc= x-coordinate of the origin of occupancy grid (cell 0,0,0) in meters.
  4.name= ~/collision_space/occupancy_grid/origin_y
  4.default= -1.25
  4.type= double
  4.desc= y-coordinate of the origin of occupancy grid (cell 0,0,0) in meters.
  5.name= ~/collision_space/occupancy_grid/origin_z
  5.default= -0.05
  5.type= double
  5.desc= z-coordinate of the origin of occupancy grid (cell 0,0,0) in meters.
  6.name= ~/collision_space/occupancy_grid/size_x
  6.default= 1.6
  6.type= double
  6.desc= size in meters of the occupancy grid in the x dimension.
  7.name= ~/collision_space/occupancy_grid/size_y
  7.default= 1.6
  7.type= double
  7.desc= size in meters of the occupancy grid in the y dimension.
  8.name= ~/collision_space/occupancy_grid/size_z
  8.default= 1.4
  8.type= double
  8.desc= size in meters of the occupancy grid in the z dimension.
}
```

#### Visualizations

```clearsilver
param {
  no_header= True
  0.name= ~/visualizations/heuristic
  0.default= false
  0.type= bool
  0.desc= Visualize the suggested 3D path from the start position to the goal pose in rviz.
  1.name= ~/visualizations/goal
  1.default= true
  1.type= bool
  1.desc= Visualize the goal pose as a sphere with an arrow.
  2.name= ~/visualizations/expanded_states
  2.default= false
  2.type= bool
  2.desc= Visualize the poses of the states expanded during the search in rviz. 
  3.name= ~/visualizations/trajectory
  3.default= false
  3.type= bool
  3.desc= Visualize the found trajectory (straight from the planner).
  4.name= ~/visualizations/trajectory_throttle
  4.default= 5
  4.type= double
  4.desc= Throttle the number of waypoints visualized (1: don't throttle).
  5.name= ~/visualizations/collision_model_trajectory
  5.default= false
  5.type= bool
  5.desc= Visualize the spherical collision model of the arm along the trajectory.
}
```

## Motion Primitives

The following text file format is how the motion primitives are inputted
into the planner. In the future, we plan on moving to a yaml format so
that we can put the primitives on the rosparam server.

```clearsilver
sub {
  no_header= True
  0.name= collision_map_occ
  0.type= mapping_msgs/CollisionMap
  0.desc= A 3D occupancy grid of the surrounding environment
  1.name= collision_object
  1.type= mapping_msgs/CollisionObject
  1.desc= Objects in the environment that are known. They get added to the collision map.
  2.name= attached_collision_object
  2.type= mapping_msgs/AttachedCollisionObject
  2.desc= Objects that were added to the robot model - usually objects that the robot grasped. They get added to the robot's collision model.
```0

The default primitive file can be found in config/pr2.mprim and looks
like this:

```clearsilver
sub {
  no_header= True
  0.name= collision_map_occ
  0.type= mapping_msgs/CollisionMap
  0.desc= A 3D occupancy grid of the surrounding environment
  1.name= collision_object
  1.type= mapping_msgs/CollisionObject
  1.desc= Objects in the environment that are known. They get added to the collision map.
  2.name= attached_collision_object
  2.type= mapping_msgs/AttachedCollisionObject
  2.desc= Objects that were added to the robot model - usually objects that the robot grasped. They get added to the robot's collision model.
```1

## Roadmap

See the [stack roadmap](sbpl_arm_planning/Roadmap) for more details.
