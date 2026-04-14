## Overview

This package contains launch files for configuring and launching the
perception components of the arm navigation pipeline for the PR2 robot.
The configuration files work with both the tilting laser sensor and the
stereo cameras on the PR2 robot. The configuration/launch files
currently in the directory are:

-   launch/collision_map_self_occ.launch - This launches an
    implementation of the collision_map node from the
    [collision_map](collision_map) package. This implementation takes
    self-occlusions into account, i.e. it retains parts of the collision
    map that may be temporarily occluded by the body parts of the robot.
-   launch/laser-perception.launch - This launches the \'\'laser
    pipeline\'\' that goes from raw laser scans to a complete collision
    map representation of the world taking self-occlusions into account.
-   launch/laser+stereo-perception.launch - This uses both laser and
    stereo information to go from raw laser scans to a complete
    collision map representation of the world taking self-occlusions
    into account.
-   tilt_laser_self_filter.launch - This launches a \'\'self filter\'\',
    i.e. a filter that removes the robot body parts from sensor
    information. The filter is located in the
    [robot_self_filter](robot_self_filter) package.
-   collision_map_sources.yaml - This file contains configuration
    information about the source of sensor data used for collision map
    generation.
-   self_filter.yaml - This file contains configuration information to
    configure the robot_self_filter for the PR2 robot.
-   shadow_filter.yaml - This file contains configuration information
    configure a \'\'shadow filter\'\', i.e. a filter that can remove
    noise in laser and stereo data due to sensor rays grazing object
    boundaries.

## Stability

1\. Parts of the ROS API is REVIEWED but UNSTABLE (see individual
packages for more details) - We will make our best effort to keep the
ROS API stable.
