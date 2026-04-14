## Overview

This package contains launch files for configuring different motion
planners for the PR2 robot. The planners that can be configured include:

-   probabilistic motion planners from the
    [OMPL planning library](ompl) 1. config/ompl_planning_configs.yaml
    contains information for configuring OMPL including assignment of
    specific planners to different sets of joints on the PR2 2.
    launch/ompl_planning.launch is a launch file for a ROS
    implementation of the OMPL library.
-   search based planners from the [SBPL planning library](sbpl)
-   a trajectory optimization based planner from the
    [CHOMP planning library](chomp_motion_planner) 1.
    config/pr2_right_arm_chomp_config.yaml configures CHOMP for the
    right arm of the PR2 robot. 2. launch/chomp_planning.launch launches
    the CHOMP planner node that provides the service for planning for
    the right arm of the PR2

## Stability

1\. Parts of the ROS API is REVIEWED but UNSTABLE (see individual
packages for more details) - We will make our best effort to keep the
ROS API stable.
