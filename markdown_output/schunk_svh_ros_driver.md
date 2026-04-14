## Overview

This package provides the driver for controlling the
[Schunk Five Finger Hand](https://schunk.com/de/en/gripping-systems/special-gripper/svh/c/PGR_3161)
with [ROS-control](http://wiki.ros.org/ros_control).

## Installation

Please see the install instructions in the official
[Github repository](https://github.com/SCHUNK-GmbH-Co-KG/schunk_svh_ros_driver).
The driver communicates via a RS485-based protocol, for which the
\'\'Brainbox\'\' USB to Serial converters have proven to work well. They
are usually distributed together with the hand.

## ROS API

```clearsilver
name = svh_ros_control_node
desc = This is the only node that's needed to control the Schunk Five Finger Hand. It uses ROS-control for managing controllers. Most topic and service communication is thus handled through the controller manager, such as publishing `joint_states` and receiving action goals for the `joint_trajectory_controller`. The node adds the following topics and services.
sub {
  0.name = connect
  0.type = std_msgs/Empty
  0.desc = Tries to connect to the hardware when triggered. The hardware will use the `serial_device` that can be reconfigured via dynamic reconfigure
  2.name = enable_channel
  2.type = std_msgs/Int8
  2.desc = Enables a given channel (finger). See channel mapping.
}

srv {
  0.name = home_reset_offset_all
  0.type = schunk_svh_msgs/HomeAll
  0.desc = Reset all of the SVH's joints.
  1.name = home_reset_offset_by_id
  1.type = schunk_svh_msgs/HomeWithChannels
  1.desc = Reset a subset of the SVH's joints.
  2.name = set_all_force_limits
  2.type = schunk_svh_msgs/SetAllChannelForceLimits
  2.desc = Set the force limits for all joints. Each limit is represented by a single float.
  3.name = set_force_limit_by_id
  3.type = schunk_svh_msgs/SetChannelForceLimit
  3.desc = Set the force limits for an individual joint
}


param {
  0.name = ~autostart
  0.type = bool
  0.desc = If set to true the controller will immediately try to connect to the hardware and start a reset of all the channels (fingers)
  0.default = true
  1.name = ~connect_retry_count
  1.type = int
  1.desc = Number of times that we try to connect during startup when not successful.
  1.default = 3
  2.name = ~serial_device
  2.type = string
  2.desc = Device handle to use for the serial communication, e.g /dev/ttyUSB0
  2.default = /dev/ttyUSB0
  3.name = ~disable_flags
  3.type = vector of bool
  3.desc = Indicates if a channel (finger) should be disabled. If disabled a finger will not be activated by the hardware but behaves as if everything was fine. This can be used in case a finger has a hardware failure.
  3.default = 9 x false
  4.name = ~reset_timeout
  4.type = int
  4.desc = Time in seconds after which a reset of a channel (finger) is aborted if the reset current threshold can not be reached. If a channel (finger) needs to reach 300mA for detection of a hard stop but is stuck at 200mA the reset is aborted after reset_timeout seconds.
  4.default = 5
  5.name = ~finger_reset_speed
  5.type = double
  5.desc = Speed of fingers during reset, given as percentage of their usual speed.
  5.default = 0.2
  6.name = /robot_description
  6.type = urdf model
  6.default = schunk_svh_description/urdf/svh-standalone.urdf.xacro
  6.desc = Urdf model of the hand, including the joints and links describing the svh
  7.name = ~maximal_force
  7.type = float
  7.default = 0.9
  7.desc = set the max force / current as a percentage of the maximally possible current
  8.name = ~name_prefix
  8.type = string
  8.default = right_hand
  8.desc = Set either `left_hand` or `right_hand` according to your hardware setup.
}
```

## Additional Information

You\'ll find additional information under the following links about

-   the
    [SVH\'s channel (finger) mappings](http://wiki.ros.org/schunk_svh_driver#Channel_Mapping)
-   a
    [trouble shooting section](http://wiki.ros.org/schunk_svh_driver#Troubleshooting)
-   and
    [the URDF, kinematic ranges, and datasheets](http://wiki.ros.org/schunk_svh_driver#Additional_information).
