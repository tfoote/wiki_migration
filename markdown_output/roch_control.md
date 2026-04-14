  -- ------------------------- -- -- -- ----------------------------- --
     [English](roch_control)            [简体中文](cn/roch_control)   
  -- ------------------------- -- -- -- ----------------------------- --

## Overview

roch_control package includes mainly interface with
[ros_control](ros_control), [twist_mux](twist_mux),
[robot_localization](robot_localization),
[imu_sensor_controller](imu_sensor_controller) and
[teleop_twist_joy](teleop_twist_joy).

For above files used by launch file of control.launch via
[roch_bringup](roch_bringup).

Finally also refrence [husky_control](husky_control).

### Input topics

Roch velocity configuration file input with \'\'twist_mux.yaml\'\' and
global configuration file with \'\'control.yaml\'\' which configure
interface with [ros_control](ros_control) and also
\'\'imu_sensor_controll.yaml\'\' configure interface with
[imu_sensor_controller](imu_sensor_controller) in
[ros_control](ros_control).

\'\'twist_mux.yaml\'\' file is wrappers for speed command topics, such
as teleop_keyboard, navigation velocity, joy control and etc.

## Report a Bug

Use github to
[report bugs](https://github.com/SawYer-Robotics/roch_robot/issues) or
[request features](https://github.com/SawYer-Robotics/roch_robot/issues).
