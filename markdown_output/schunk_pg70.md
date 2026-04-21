## Overview

This package is part of
[schunk_grippers](http://wiki.ros.org/schunk_grippers) stack. It allows
user to control Schunk PG70 gripper over RS232 link using standard ROS
services and provides Xacro model for easier integration with various
robots.

## Installation

This package depends on
[ROS serial](http://wiki.ros.org/http://wiki.ros.org/serial) library by
William Woodall, git clone and catkin_make if not already in your
workspace. Then you can proceed to clone and build of
schunk_pg70[source](https://github.com/SmartRoboticSystems/schunk_grippers.git).

### Permissions

The right to access a serial port is determined by the permissions of
the device file (e.g. /dev/ttyS0). Serial ports are usualy owned by root
and group dialout, so to access the serial device as non-root user it is
convenient to add yourself to **dialout** group:

```
$ usermod -a -G dialout USER_NAME
``` Reboot to apply group changes.

## ROS API

```clearsilver
name = pg70_rs232_control
desc = Node for interfacing PG70 by serial library. Provides ROS services for gripper control and publishes actual gripper position to joint_states
pub {
  0.name = joint_states
  0.type = sensor_msgs/JointState
  0.desc = publishes actual gripper position
}
param {
  0.name = gripper_id
  0.type = std_msgs/UInt8
  0.desc = Gripper ID according to controller setup
  1.name = portname
  1.type = std_msgs/String
  1.desc = serial port communicating with gripper
  2.name = baudrate
  2.type = std_msgs/Int16
  2.desc = baudrate of serial port
}
srv {
  0.name = schunk_pg70/reference
  0.type = std_msgs/Empty
  0.desc = Referencing the gripper
  1.name = schunk_pg70/get_error
  1.type = std_msgs/Empty
  1.desc = Getting actual gripper error
  2.name = schunk_pg70/acknowledge_error
  2.type = std_msgs/Empty
  2.desc = Acknowledging occured error/errors
  3.name = schunk_pg70/get_position
  3.type = std_msgs/Empty
  3.desc = Getting actual gripper position
  4.name = schunk_pg70/set_position
  4.type = std_msgs/Float32
  4.desc = Setting actual gripper position
  5.name = schunk_pg70/stop
  5.type = std_msgs/Empty
  5.desc = Stopping gripper movement
}
req_tf {
  0.from = robot_end_link
  0.to   = schunk_pg70_base_link
  0.desc = Connecting gripper to robot
}

prov_tf{
  0.from = schunk_pg70_base_link
  0.to   = schunk_pg70_finger_1_link
  0.desc = Finger 1 link
  1.from = schunk_pg70_base_link
  1.to   = schunk_pg70_finger_2_link
  1.desc = Finger 2 link
}
```

## Usage

*Note: Before interfacing Schunk PG70 gripper from Linux, we highly
recomend to use original Windows application Schunk MTS Tool to verify
that gripper is fully functional and there are no wiring or other
hardware issues. Depending on default configuration it might be also
necessary to perform **memory reset** to allow serial communication with
the gripper for a first time.*

### Launch

To launch the driver node, use the following command:

```
$ roslaunch schunk_pg70 pg70_rs232_control.launch
``` if everything is okay, after typing

```
$ rostopic echo /joint_states
``` you should see actual gripper position being
published on \"joint_states\" topic approximately 10 times per second:

```
header:
  seq: 21
  stamp:
    secs: 1443075477
    nsecs: 409227511
  frame_id: ''
name: ['pg70_finger1_joint', 'pg70_finger2_joint']
position: [0.010000248908996583, 0.010000248908996583]
velocity: []
effort: []
---
header:
  seq: 22
  stamp:
    secs: 1443075477
    nsecs: 511969796
  frame_id: ''
name: ['pg70_finger1_joint', 'pg70_finger2_joint']
position: [0.010000248908996583, 0.010000248908996583]
velocity: []
effort: []
```

### Test the driver

To get the list of available services type:

```
$ rosservice list
``` If everything is okay, you should notice 6
services being advertised by \"pg70_rs232_control\" node:

```
schunk_pg70/reference
schunk_pg70/get_error
schunk_pg70/acknowledge_error
schunk_pg70/get_position
schunk_pg70/set_position
schunk_pg70/stop
``` These services are ROS user interface to Schunk
PG70 gripper. Except \"set_position\" all of them use
[std_msgs::Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
requests, so you don\'t need to specify any values, just \"rosservice
call\" as in the example below.

#### get_error service

To test the driver start by calling the *get_error* service
([std_msgs::Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
request):

```
$ rosservice call /schunk_pg70/get_error
``` If no error occured - the service should
respond:

```
error_code: 0
```

#### get_position

To get actual gripper position, call *get_position* service
([std_msgs::Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
request):

```
$ rosservice call /schunk_pg70/get_position
``` Service respond with actual position value is
in
[std_msgs::Float32](http://docs.ros.org/api/std_msgs/html/msg/Float32.html)
format:

```clearsilver
name = pg70_rs232_control
desc = Node for interfacing PG70 by serial library. Provides ROS services for gripper control and publishes actual gripper position to joint_states
pub {
  0.name = joint_states
  0.type = sensor_msgs/JointState
  0.desc = publishes actual gripper position
}
param {
  0.name = gripper_id
  0.type = std_msgs/UInt8
  0.desc = Gripper ID according to controller setup
  1.name = portname
  1.type = std_msgs/String
  1.desc = serial port communicating with gripper
  2.name = baudrate
  2.type = std_msgs/Int16
  2.desc = baudrate of serial port
}
srv {
  0.name = schunk_pg70/reference
  0.type = std_msgs/Empty
  0.desc = Referencing the gripper
  1.name = schunk_pg70/get_error
  1.type = std_msgs/Empty
  1.desc = Getting actual gripper error
  2.name = schunk_pg70/acknowledge_error
  2.type = std_msgs/Empty
  2.desc = Acknowledging occured error/errors
  3.name = schunk_pg70/get_position
  3.type = std_msgs/Empty
  3.desc = Getting actual gripper position
  4.name = schunk_pg70/set_position
  4.type = std_msgs/Float32
  4.desc = Setting actual gripper position
  5.name = schunk_pg70/stop
  5.type = std_msgs/Empty
  5.desc = Stopping gripper movement
}
req_tf {
  0.from = robot_end_link
  0.to   = schunk_pg70_base_link
  0.desc = Connecting gripper to robot
}

prov_tf{
  0.from = schunk_pg70_base_link
  0.to   = schunk_pg70_finger_1_link
  0.desc = Finger 1 link
  1.from = schunk_pg70_base_link
  1.to   = schunk_pg70_finger_2_link
  1.desc = Finger 2 link
}
```0

#### set_position

To move the gripper to target position, call *set_position* service
([std_msgs::float32](http://docs.ros.org/api/std_msgs/html/msg/Float32.html)
request):

```clearsilver
name = pg70_rs232_control
desc = Node for interfacing PG70 by serial library. Provides ROS services for gripper control and publishes actual gripper position to joint_states
pub {
  0.name = joint_states
  0.type = sensor_msgs/JointState
  0.desc = publishes actual gripper position
}
param {
  0.name = gripper_id
  0.type = std_msgs/UInt8
  0.desc = Gripper ID according to controller setup
  1.name = portname
  1.type = std_msgs/String
  1.desc = serial port communicating with gripper
  2.name = baudrate
  2.type = std_msgs/Int16
  2.desc = baudrate of serial port
}
srv {
  0.name = schunk_pg70/reference
  0.type = std_msgs/Empty
  0.desc = Referencing the gripper
  1.name = schunk_pg70/get_error
  1.type = std_msgs/Empty
  1.desc = Getting actual gripper error
  2.name = schunk_pg70/acknowledge_error
  2.type = std_msgs/Empty
  2.desc = Acknowledging occured error/errors
  3.name = schunk_pg70/get_position
  3.type = std_msgs/Empty
  3.desc = Getting actual gripper position
  4.name = schunk_pg70/set_position
  4.type = std_msgs/Float32
  4.desc = Setting actual gripper position
  5.name = schunk_pg70/stop
  5.type = std_msgs/Empty
  5.desc = Stopping gripper movement
}
req_tf {
  0.from = robot_end_link
  0.to   = schunk_pg70_base_link
  0.desc = Connecting gripper to robot
}

prov_tf{
  0.from = schunk_pg70_base_link
  0.to   = schunk_pg70_finger_1_link
  0.desc = Finger 1 link
  1.from = schunk_pg70_base_link
  1.to   = schunk_pg70_finger_2_link
  1.desc = Finger 2 link
}
```1 where \"**position**\" is within a range of
\<0 - 69\> mm, velocity \<0-83\>mm/s and acceleration \<0-320\>mm/s2.
The gripper should respond with goal_position being accepted or not and
move to goal position:

```clearsilver
name = pg70_rs232_control
desc = Node for interfacing PG70 by serial library. Provides ROS services for gripper control and publishes actual gripper position to joint_states
pub {
  0.name = joint_states
  0.type = sensor_msgs/JointState
  0.desc = publishes actual gripper position
}
param {
  0.name = gripper_id
  0.type = std_msgs/UInt8
  0.desc = Gripper ID according to controller setup
  1.name = portname
  1.type = std_msgs/String
  1.desc = serial port communicating with gripper
  2.name = baudrate
  2.type = std_msgs/Int16
  2.desc = baudrate of serial port
}
srv {
  0.name = schunk_pg70/reference
  0.type = std_msgs/Empty
  0.desc = Referencing the gripper
  1.name = schunk_pg70/get_error
  1.type = std_msgs/Empty
  1.desc = Getting actual gripper error
  2.name = schunk_pg70/acknowledge_error
  2.type = std_msgs/Empty
  2.desc = Acknowledging occured error/errors
  3.name = schunk_pg70/get_position
  3.type = std_msgs/Empty
  3.desc = Getting actual gripper position
  4.name = schunk_pg70/set_position
  4.type = std_msgs/Float32
  4.desc = Setting actual gripper position
  5.name = schunk_pg70/stop
  5.type = std_msgs/Empty
  5.desc = Stopping gripper movement
}
req_tf {
  0.from = robot_end_link
  0.to   = schunk_pg70_base_link
  0.desc = Connecting gripper to robot
}

prov_tf{
  0.from = schunk_pg70_base_link
  0.to   = schunk_pg70_finger_1_link
  0.desc = Finger 1 link
  1.from = schunk_pg70_base_link
  1.to   = schunk_pg70_finger_2_link
  1.desc = Finger 2 link
}
```2

#### reference

To reference gripper, call *reference* service (empty request).
Referencing may also help in cases when you are not able to move the
gripper although everything else looks okay:

```clearsilver
name = pg70_rs232_control
desc = Node for interfacing PG70 by serial library. Provides ROS services for gripper control and publishes actual gripper position to joint_states
pub {
  0.name = joint_states
  0.type = sensor_msgs/JointState
  0.desc = publishes actual gripper position
}
param {
  0.name = gripper_id
  0.type = std_msgs/UInt8
  0.desc = Gripper ID according to controller setup
  1.name = portname
  1.type = std_msgs/String
  1.desc = serial port communicating with gripper
  2.name = baudrate
  2.type = std_msgs/Int16
  2.desc = baudrate of serial port
}
srv {
  0.name = schunk_pg70/reference
  0.type = std_msgs/Empty
  0.desc = Referencing the gripper
  1.name = schunk_pg70/get_error
  1.type = std_msgs/Empty
  1.desc = Getting actual gripper error
  2.name = schunk_pg70/acknowledge_error
  2.type = std_msgs/Empty
  2.desc = Acknowledging occured error/errors
  3.name = schunk_pg70/get_position
  3.type = std_msgs/Empty
  3.desc = Getting actual gripper position
  4.name = schunk_pg70/set_position
  4.type = std_msgs/Float32
  4.desc = Setting actual gripper position
  5.name = schunk_pg70/stop
  5.type = std_msgs/Empty
  5.desc = Stopping gripper movement
}
req_tf {
  0.from = robot_end_link
  0.to   = schunk_pg70_base_link
  0.desc = Connecting gripper to robot
}

prov_tf{
  0.from = schunk_pg70_base_link
  0.to   = schunk_pg70_finger_1_link
  0.desc = Finger 1 link
  1.from = schunk_pg70_base_link
  1.to   = schunk_pg70_finger_2_link
  1.desc = Finger 2 link
}
```3

## Xacro model

To visualize Schunk PG70 gripper in Rviz use
\"pg70_visualize_standalone.launch\" file.

```clearsilver
name = pg70_rs232_control
desc = Node for interfacing PG70 by serial library. Provides ROS services for gripper control and publishes actual gripper position to joint_states
pub {
  0.name = joint_states
  0.type = sensor_msgs/JointState
  0.desc = publishes actual gripper position
}
param {
  0.name = gripper_id
  0.type = std_msgs/UInt8
  0.desc = Gripper ID according to controller setup
  1.name = portname
  1.type = std_msgs/String
  1.desc = serial port communicating with gripper
  2.name = baudrate
  2.type = std_msgs/Int16
  2.desc = baudrate of serial port
}
srv {
  0.name = schunk_pg70/reference
  0.type = std_msgs/Empty
  0.desc = Referencing the gripper
  1.name = schunk_pg70/get_error
  1.type = std_msgs/Empty
  1.desc = Getting actual gripper error
  2.name = schunk_pg70/acknowledge_error
  2.type = std_msgs/Empty
  2.desc = Acknowledging occured error/errors
  3.name = schunk_pg70/get_position
  3.type = std_msgs/Empty
  3.desc = Getting actual gripper position
  4.name = schunk_pg70/set_position
  4.type = std_msgs/Float32
  4.desc = Setting actual gripper position
  5.name = schunk_pg70/stop
  5.type = std_msgs/Empty
  5.desc = Stopping gripper movement
}
req_tf {
  0.from = robot_end_link
  0.to   = schunk_pg70_base_link
  0.desc = Connecting gripper to robot
}

prov_tf{
  0.from = schunk_pg70_base_link
  0.to   = schunk_pg70_finger_1_link
  0.desc = Finger 1 link
  1.from = schunk_pg70_base_link
  1.to   = schunk_pg70_finger_2_link
  1.desc = Finger 2 link
}
```4 Since fingers are mechanically interlocked,
there is only one joint to control the movement both of them. Use
joint_state_publisher GUI to test the movement:

![\|height=\"464\",width=\"698\"](attachment:pg70_standalone.jpg)
