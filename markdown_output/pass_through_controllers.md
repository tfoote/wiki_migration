## Overview

A package for ROS-controllers and HW Interface mechanisms to enable
forwarding of trajectories (both joint-based and Cartesian) to the robot
for interpolation.

## Rationale

The idea behind these controllers is to enable forwarding (pass through)
incoming trajectories directly to the robot and let the OEM driver-side
take care of interpolating between the waypoints. This is useful if your
application demands industrial scale trajectory execution, and you
prefer not to interpolate on the ROS side. Having the complete
trajectory available on the driver side can be beneficial regarding
smoothness of execution and avoid issues related to sending (streaming)
ad hoc commands, as is classically done with current ROS-control
approaches. The controllers implement simple action servers for
trajectory execution (both Cartesian and joint-based). They are meant to
be light-weight and their functionality is deliberately limited to
starting trajectories, canceling them, and providing real-time feedback
on progress.

Note that most of the work has to be done in the hardware abstraction of
the robot. And, unfortunately, this is very robot specific and hard to
generalize. It's somewhat similar to the `read()` and `write()`
functions of ROS-control, which need to implement robot-specific
protocols. This package provides the necessary HW interfaces to
implement this feature.

## Further information

For further information, especially how to integrate this into a RobotHW
interface, see the
[Documentation on GitHub](https://github.com/UniversalRobots/Universal_Robots_ROS_passthrough_controllers/blob/main/README.md)
