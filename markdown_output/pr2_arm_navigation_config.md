## Overview

This package contains configuration files for the components of the arm
navigation stacks. These files configure the nodes in the stack
specifically for the PR2 robot. In particular, the config directory in
this package contains three files:

-   collision_checks_both_arms.yaml - This file sets up the collision
    environment for the robot using *ordered collision operations*. See
    the [planning_environment](planning_environment) package for more
    information. Also, see
    [planning_environment/YAML configuration](planning_environment/YAML configuration)
    for more information.
-   joint_limits.yaml - This file sets up the joint limits information
    for the PR2 robot. This information is used by the motion planners
    and also by the trajectory filters. See
    [joint limit configuration](trajectory_filter_server/YAML configuration)
    for more details on configuring this file.
-   planning_groups.yaml - This file contains definitions of *groups*.
    Groups are essentially a collection of joints and links that make it
    easier to work with the PR2 robot. See the
    [planning_environment](planning_environment) package for more
    information. Also, see
    [planning_environment/YAML configuration](planning_environment/YAML configuration)
    for more information.

## Stability

1\. ROS API is UNREVIEWED and UNSTABLE.
