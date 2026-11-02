## Overview

This package contains configuration files for the
[move_base](https://index.ros.org/p/move_base) node meant to be run in
an application that requires navigation in an odometric frame. This
package also includes launch files that bring up
[rviz](https://index.ros.org/p/rviz) and [nav_view](nav_view) with local
navigation specific configurations.

## Applications

- **`rviz/rviz_move_base_local.launch`**: Starts
  [rviz](https://index.ros.org/p/rviz) with a local navigation friendly
  setup.
- **`nav_view/nav_view_move_base_local.launch`**: Starts
  [nav_view](nav_view) with a local navigation friendly setup.

## Building Blocks

- **`move_base_local.xml`**: Holds a PR2 specific configuration of the
  [move_base](https://index.ros.org/p/move_base) node designed for
  navigation without a map in an odometric frame.

## Configuration Files

- **`config/global_costmap_params.yaml`**: Holds parameters for the
  global [ costmap](https://index.ros.org/p/costmap_2d) used in the
  `move_base_local.xml` configuration file. This is the
  [ costmap](https://index.ros.org/p/costmap_2d) used by the
  [navfn](https://index.ros.org/p/navfn) planner and, in this case,
  operates in an odometric frame.
- **`config/base_local_planner_params.yaml`**: Holds parameters for
  the [base_local_planner](https://index.ros.org/p/base_local_planner)
  specific to local navigation on the PR2.
- **`config/local_costmap_params.yaml`**: Holds parameters for the
  local [ costmap](https://index.ros.org/p/costmap_2d) used in the
  `move_base_local.xml` configuration file. This is the
  [ costmap](https://index.ros.org/p/costmap_2d) used by the
  [base_local_planner](https://index.ros.org/p/base_local_planner)
  planner, and operates in an odometric frame.
- **`config/move_base_params.yaml`**: Holds local navigation specific
  parameters for the [move_base](https://index.ros.org/p/move_base)
  node.
