## Overview

This package contains launch files for configuring and launching three
different nodes with the PR2 robot arms:

-   [move_arm](move_arm) - The move_arm node is a coordinating action
    that can coordinate motion planning, trajectory filtering and
    control to move a robot arm to a desired position in a collision
    free manner.
-   [environment_server](planning_environment) - The environment server
    is a monitoring node that uses sensor information to provide
    collision information about the world around the robot. This server
    can be used to check whether desired trajectories are in collision,
    violate constraints or violate joint limits.
-   [collision free trajectory controller](collision_free_arm_trajectory_controller) -
    This is a node with the same interface as the joint trajectory
    action. It will execute a desired trajectory only if the trajectory
    is not in collision with the environment.

All these nodes are configured for both the left and right arms of the
PR2 robot.

## Stability

1\. Parts of the ROS API is REVIEWED but UNSTABLE (see individual
packages for more details). We will make our best effort to keep the ROS
API stable.
