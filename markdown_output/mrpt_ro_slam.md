## ROS API

The sections below describe the API of this package for Range-Only (RO)
SLAM, based on a mixture of Rao-Blackwellized Particle Filters (RBPF)
and EKF for each particle\'s map of beacons. This packages publishes
particles that represent the robot and the radio beacons into ROS.

## Demos

### Range-only (RO) SLAM with a set of radio beacons

Run:

```
roslaunch mrpt_ro_slam demo_ro.launch
``` to start:

-   a dataset (rawlog format) including RO and odometry observations,
-   the mrpt rbpf-slam with unknown beacon locations, and
-   RViz for visualization

NOTE: Module and documentation under development!
