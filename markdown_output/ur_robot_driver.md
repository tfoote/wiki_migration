## Overview

This package contains the ROS driver for Universal Robots robotic arms
from the CB3- or e-Series.

[Youtube](https://www.youtube.com/watch?v=EfEfkXUJwP8)

## Compatibility

### Polyscope up to v1.8.x

This package does not support CB2 controllers.

For robots with Polyscope `v1.8.x` or older, please see whether
[ur_modern_driver](https://index.ros.org/p/ur_modern_driver) is
sufficient.

### Polyscope v3.x, v5.x and 10.x

Make sure the controller runs `v3.14.3` or newer for CB3, or
`v5.9.4` or newer for e-Series controllers. For PolyScope X, any
version is supported.

In general, we recommend updating the robot to the latest release
possible.

## Feature

- Works for all CB3 (with software version >= 3.14.3), e-Series
  (software >= 5.9.4) and all PolyScope X robots and uses the RTDE
  interface for communication, whenever possible.
- Factory calibration of the robot inside ROS to reach Cartesian targets
  precisely.
- Realtime-enabled communication structure to robustly cope with the 2ms
  cycle time of the e-Series. To use this, compile and run it on a
  kernel with the PREEMPT_RT patch enabled. (See the Real-time setup
  guide on how to achieve this)
- Transparent integration of the teach-pendant. Using the URCaps system,
  a program is running on the robot that handles control commands sent
  from ROS side. With this, the robot can be paused, stopped and resumed
  without restarting the ROS driver. This will in the future also enable
  the usage of ROS-components as part of a more complex UR-program on
  the teach pendant. ROS-control of the robot can be quit using a
  service call to continue program execution on the TP.
- Use the robot's speed-scaling. When speed scaling is active due to
  safety constraints or the speed slider is used, this gets correctly
  handled on the ROS side, as well slowing down trajectory execution
  accordingly.
  - Note: **Other ros-controllers based on a position interface can be
    used with this driver, but may behave wrong if the speed slider
    isn't set to 100% or if speed scaling slows down the robot. Also,
    the pausing function can only be used if the default scaled
    trajectory controller is used.**
- ROS-Service-based replacement of most every-day TP-interactions offer
  using UR robots without interacting with the teach pendant at all, if
  desired. The robot can be started, stopped and even recovery from
  safety events can be done using ROS service- and action calls. See the
  driver's dashboard services and the robot_state_helper node for
  details.

## Additional information

Most documentation is handled inside the Githhub
[README](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/README.md)
files.

## Contributing
