\'\'ROS Software Maintainer: [Clobot](http://wiki.ros.org/clobot)\'\'

## Overview

![Clober Robot\|width=400](attachment:myahrs_ros2_driver/myahrs.png)

\'\'\'Myahrs ROS2 Driver\'\'\' package is a ROS2 driver for the myAHRS+
which is a low cost high performance AHRS(Attitude Heading Reference
System). Using this package, users can create the format of IMU
sensor_msgs in ROS2 system.

## ROS Wiki related to related to Myahrs ROS2 Driver

-   [clober](clober)

## References related to Myahrs ROS2 Driver

-   [Website for Clobot](http://www.clobot.co.kr/)
-   [myahrs_ros2_driver](https://github.com/CLOBOT-Co-Ltd/myahrs_ros2_driver)
-   [myahrs_plus](https://github.com/withrobot/myAHRS_plus)
-   [visualization_tutorials(clobot-git)](https://github.com/clobot-git/visualization_tutorials)
-   [myahrs_driver](http://wiki.ros.org/myahrs_driver)

## Video

## ROS API

```clearsilver
node.0 {
name= myahrs_ros2_driver
desc= 'myahrs_ros2_driver' is a ROS2 driver for the myAHRS+ which is a low cost high performance AHRS(Attitude Heading Reference System).
}
pub {
  0.name = imu/data_raw
  0.type = sensor_msgs/Imu
  0.desc = raw data of linear_acceleration and angular_velocity from myahrs+.
  1.name = imu/data
  1.type = sensor_msgs/Imu
  1.desc = orientation data from myahrs+, including raw data of linear_acceleration and angular_velocity.
  2.name = imu/mag
  2.type = sensor_msgs/MagneticField
  2.desc = magnetic_field data from myahrs+.
  3.name = imu/temperature
  3.type = std_msgs/Float64
  3.desc = temperature data from myahrs+.
}
param {
  0.name = ~angular_velocity_stddev
  0.type = double
  0.desc = square root of the angular_velocity_covariance diagonal elements in rad/s.
  0.default = 0.002428
  1.name = ~linear_acceleration_stddev
  1.type = double
  1.desc = square root of the linear_acceleration_covariance diagonal elements in m/s^2.
  1.default = 0.026831
  2.name = ~magnetic_field_stddev
  2.type = double
  2.desc = square root of the magnetic_field_covariance diagonal elements in Tesla.
  2.default = 0.00000327468
  3.name = ~orientation_field_stddev
  3.type = double
  3.desc = square root of the orientation_covariance diagonal elements in rad.
  3.default = 0.002143
}
```
