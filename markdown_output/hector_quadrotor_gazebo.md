## Overview

This package provides a quadrotor model based on
[hector_quadrotor_urdf](hector_quadrotor_urdf) that is usable in gazebo.
It currently supports the following features:

-   Colored COLLADA Quadrotor mesh model (.dae)
-   URDF description
-   Publishing of ground truth pose and simulated imu data
-   Spawnable in gazebo
-   Dedicated controller for use in gazebo simulation. The UAV can be
    controlled in gazebo using
    [geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)
    messages on the 'cmd_vel' topic (as used on may other robots, but
    with added climb rate).

## Use

For instructions on how to start simulation of the quadrotor please have
look at the following tutorials:
