## Overview

This package currently requires two sensors to be connected; a
[CH Robotics IMU](http://www.chrobotics.com/) on port \"/dev/imu\" and a
Microsoft Kinect.

## Launchfiles

**\*indoor_sensors.launch:** Launches the IMU node and the Kinect
nodelet. Requires a [nodelet manager](nodelet) to be operational (not
launched here). **\*indoor_ekf.launch:** To be launched along with
*indoor_sensors.launch*. Launches a nodelet manager, a number of point
cloud processing nodes
([pointcloud_to_laserscan](pointcloud_to_laserscan), for example), and
an instance of [robot_pose_ekf](robot_pose_ekf) which has been
configured to produce the data that the examples in the
[husky_navigation](husky_navigation) stack require. *Note:* The nodelet
manager is launched here instead of in the *indoor_sensors* launchfile
to allow for simulated Kinects to be used.
