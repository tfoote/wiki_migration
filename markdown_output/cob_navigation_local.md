## Overview

This package contains launch and configuration files for the
[move_base](https://index.ros.org/p/move_base) node meant to be run in
an application that requires navigation in an odometric frame.

## Applications

- **`launch/2dnav_ros_tr.launch`**: Starts local navigation with the
  trajectory rollout local planner.
- **`launch/2dnav_ros_dwa.launch`**: Starts local navigation with the
  dynamic window approach local planner.

## Building Blocks

- **`launch/2dnav_ros_tr.xml`**: Holds a Care-O-bot specific
  configuration of the [move_base](https://index.ros.org/p/move_base)
  node designed for navigation without a map in an odometric frame. It
  uses the trajectory rollout local planner.
- **`launch/2dnav_ros_dwa.xml`**: Holds a Care-O-bot specific
  configuration of the [move_base](https://index.ros.org/p/move_base)
  node designed for navigation without a map in an odometric frame. It
  uses the trajectory dynamic window approach.

## Configuration Files

- **`config/global_costmap_params.yaml`**: Holds parameters for the
  global [costmap](https://index.ros.org/p/costmap_2d) used in the
  `2dnav_ros_tr.xml` and `2dnav_ros_dwa.xml` configuration files.
  This is the [costmap](https://index.ros.org/p/costmap_2d) used by the
  global planner and, in this case, operates in an odometric frame.
- **`config/local_costmap_params.yaml`**: Holds parameters for the
  local [costmap](https://index.ros.org/p/costmap_2d) used in the
  `2dnav_ros_tr.xml` and `2dnav_ros_dwa.xml` configuration file.
  This is the [costmap](https://index.ros.org/p/costmap_2d) used by the
  local planner, and operates in an odometric frame.
