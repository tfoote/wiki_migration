## Overview

Data Processing Layer (DPL) is a second layer in experimental robotic
stack. The main task of this package is to fuse multiple sources of data
from [HAL](p3dx_hal_vrep). The output from nodes in DPL are standard
higher level messages like
\<\<MsgLink(nav_msgs/Odometry)\>\>,\<\<MsgLink(sensor_msgs/PointCloud)\>\>\...

## Architecture

For more information about whole experimental robot stack and ideas
behind DPL please see our [repo](https://github.com/hrnr/robo-rescue)
readme.

## Dependencies

### Packages

#### robot_localization

In DPL we use [robot_localization](robot_localization) package for
fusion of IMU data and calculate wheel odometry. In current state we use
our own fork of this package with some bug fixes. Please download and
compile it from our
[repository](https://github.com/Lukx19/robot_localization).

## Nodes

```clearsilver
name = motor_controler
desc = This motor driver is suitable for differential driven robot. Received data are in form of <<MsgLink(geometry_msgs/Twist)>> and transformed into angular speeds for left and right wheels.
sub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = reads messages from
  }
pub {
  0.name = hal/leftMotor/setVel
  0.type = std_msgs/Float64
  0.desc = angular speed of left wheel in m/s
  1.name = hal/rightMotor/setVel
  1.type = std_msgs/Float64
  1.desc = angular speed of right wheel in m/s
  }
``` ```clearsilver
name = odometry_provider
desc = This node calculates forward velocity and angular speed around Z axis of the robot with differential drive.
sub {
  0.name = hal/leftMotor/getState
  0.type = sensor_msgs/JointState
  0.desc = uses joint position
  1.name = hal/rightMotor/getState
  1.type = sensor_msgs/JointState
  1.desc = uses joint position
}
pub {
  0.name = odom
  0.type = nav_msgs/Odometry
  0.desc = .
  }
param {
  0.name = ~frameIDodom
  0.type = string
  0.desc = frame_id which is used in <<MsgLink(nav_msgs/Odometry)>>
  0.default = odom

  1.name = ~odomPublTopic
  1.type = string
  1.desc = topic where is <<MsgLink(nav_msgs/Odometry)>> message published
  1.default = odom
}
```
```clearsilver
name = imu_provider
desc = This node merges accelerometer and gyroscope data into complete <<MsgLink(sensor_msgs/Imu)>> message.
``` ```clearsilver
name = odom_tf_broadcaster
desc = Creates tf transformation between odom frame and robot's base link.
param {
  0.name = ~frameIDodom
  0.type = string
  0.desc = frame_id which is used in <<MsgLink(nav_msgs/Odometry)>>
  0.default = odom

  1.name = ~odomPublTopic
  1.type = string
  1.desc = topic where is <<MsgLink(nav_msgs/Odometry)>> message published
  1.default = odom
}
prov_tf {
  0.from = odom
  0.to   = base_footprint
  0.desc = .
}
```
