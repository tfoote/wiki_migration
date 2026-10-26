## Overview

This package holds a number of common configuration files for the
[move_base](move_base) node on the PR2 robot. In particular, it holds
parameter settings for the [base_local_planner](base_local_planner),
[costmap_2d](costmap_2d), and [move_base](move_base) components of the
[move_base](move_base) node that are shared between many different
configurations of the [navigation](navigation) stack run on the PR2.

## Configuration Files

- **`move_base/base_local_planner_params.yaml`**: Parameters for the
  [base_local_planner](base_local_planner) that work well on the PR2 and
  are shared between many different [move_base](move_base)
  configurations.
- **`move_base/costmap_common_params.yaml`**: Holds the sensor
  configuration for the [ costmap's](costmap_2d ) run on the PR2. This
  configuration assumes that the robot is being run with the sensors and
  filters specified in the
  [pr2_navigation_perception](pr2_navigation_perception) package.
- **`move_base/move_base_params.yaml`**: Holds the PR2 robot footprint
  specification and common parameters for [move_base](move_base).
