## Overview

This package contains launch files for two implementations of kinematics
for the PR2 robot arms:

-   pr2_ik_rarm_node.launch and pr2_ik_larm_node.launch contain launch
    configuration for the pr2_kinematics node from the
    [pr2_arm_kinematics package](pr2_arm_kinematics). This node provides
    both forward and inverse kinematics services.
-   right_arm_collision_free_ik.launch and
    left_arm_collision_free_ik.launch provide an implementation of
    collision free inverse kinematics from the
    [constraint aware kinematics](pr2_arm_kinematics_constraint_aware)
    package.

## API Stability

1\. ROS API is REVIEWED but UNSTABLE - We will make our best effort to
keep the ROS API stable.
