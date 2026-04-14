## Overview

This package is part of
[schunk_grippers](http://wiki.ros.org/schunk_grippers) stack. It allows
user to control Schunk EZN64 gripper over USB using standard ROS
services and provides Xacro model for easier integration with various
robots.

## Installation

Git clone
[source](https://github.com/SmartRoboticSystems/schunk_grippers.git) to
your \"\'\'catkin_ws/src\" \'\'folder and \'\'catkin_make\'\' as usual.

This package depends on [libusb1.0-0](http://www.libusb.org/) library
which should be part of ROS installation. To check availibility type:

```
$ sudo apt-get install libusb-1.0-0
```

### Permissions

By default, the file permissions for the EZN64 gripper device does not
permit writing. This often leads to an error \"Not able to open a
device\" or similar. To permanently change the permissions, it is
recomended to create a udev rule. Login as root, create a file
\"20-usb-ezn64.rules\", copy the text below and move the file to
\"/etc/udev/rules.d/\" folder.

```
SUBSYSTEM=="usb"
ATTR{idVendor}=="7358"
ATTR{idProduct}=="371"
ACTION=="add"
MODE:="0666"
``` Reboot to apply udev changes.

## ROS API

```clearsilver
name = ezn64_usb_control
desc = Node for interfacing EZN64 by libusb1.0-0. Provides ROS services for gripper control and publishes actual gripper position to joint_states
pub {
  0.name = joint_states
  0.type = sensor_msgs/JointState
  0.desc = publishes actual gripper position
}
param {
  0.name = vendor_id
  0.type = std_msgs/UInt16
  0.desc = Vendor ID according to USB conventions
  1.name = product_id
  1.type = std_msgs/UInt16
  1.desc = Product ID according to USB conventions
  2.name = gripper_id
  2.type = std_msgs/UInt8
  2.desc = Gripper ID according to controller setup
}
srv {
  0.name = schunk_ezn64/reference
  0.type = std_msgs/Empty
  0.desc = Referencing the gripper
  1.name = schunk_ezn64/get_error
  1.type = std_msgs/Empty
  1.desc = Getting actual gripper error
  2.name = schunk_ezn64/acknowledge_error
  2.type = std_msgs/Empty
  2.desc = Acknowledging occured error/errors
  3.name = schunk_ezn64/get_position
  3.type = std_msgs/Empty
  3.desc = Getting actual gripper position
  4.name = schunk_ezn64/set_position
  4.type = std_msgs/Float32
  4.desc = Setting actual gripper position
  5.name = schunk_ezn64/stop
  5.type = std_msgs/Empty
  5.desc = Stopping gripper movement
}
req_tf {
  0.from = robot_end_link
  0.to   = schunk_ezn64_base_link
  0.desc = Connecting gripper to robot
}

prov_tf{
  0.from = schunk_ezn64_base_link
  0.to   = schunk_ezn64_finger_1_link
  0.desc = Finger 1 link
  1.from = schunk_ezn64_base_link
  1.to   = schunk_ezn64_finger_2_link
  1.desc = Finger 2 link
  2.from = schunk_ezn64_base_link
  2.to   = schunk_ezn64_finger_3_link
  2.desc = Finger 3 link
}
```

## Usage

\'\'Note: Before interfacing Schunk EZN64 gripper from Linux, we highly
recomend to use original Windows application Schunk MTS Tool to verify
that gripper is fully functional and there are no wiring or other
hardware issues. \'\'

### Launch

To launch the driver node, use the following command:

```
$ roslaunch schunk_ezn64 ezn64_usb_control.launch
``` if everything is okay, after typing

```
$ rostopic echo /joint_states
``` you should see actual gripper position being
published on \"joint_states\" topic 10 times per second:

```
header:
  seq: 34
  stamp:
    secs: 1443076490
    nsecs: 513091024
  frame_id: ''
name: ['ezn64_finger_1_joint', 'ezn64_finger_2_joint', 'ezn64_finger_3_joint']
position: [0.011971454620361328, 0.011971454620361328, 0.011971454620361328]
velocity: []
effort: []
---
header:
  seq: 35
  stamp:
    secs: 1443076490
    nsecs: 612699408
  frame_id: ''
name: ['ezn64_finger_1_joint', 'ezn64_finger_2_joint', 'ezn64_finger_3_joint']
position: [0.01197367763519287, 0.01197367763519287, 0.01197367763519287]
velocity: []
effort: []
``` \'\'Note: In case of initialization problems,
try to unplug and plug the USB cable again. \'\'

### Test the driver

To get the list of available services type:

```
$ rosservice list
``` If everything is okay, you should notice 6
services being advertised by \"ezn64_usb_control\" node:

```
schunk_ezn64/reference
schunk_ezn64/get_error
schunk_ezn64/acknowledge_error
schunk_ezn64/get_position
schunk_ezn64/set_position
schunk_ezn64/stop
``` These services are ROS user interface to Schunk
EZN64 gripper. Except \"set_position\" all of them use
[std_msgs::Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
requests, so you don\'t need to specify any values, just \"rosservice
call\" as in the example below.

#### get_error service

To test the driver start by calling the \'\'get_error\'\' service
([std_msgs::Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
request):

```
$ rosservice call /schunk_ezn64/get_error
``` If no error occured - the driver should
respond:

```
error_code: 0
```

#### get_position

To get actual gripper position, call \'\'get_position\'\' service
([std_msgs::Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
request):

```
SUBSYSTEM=="usb"
ATTR{idVendor}=="7358"
ATTR{idProduct}=="371"
ACTION=="add"
MODE:="0666"
```0 Gripper should respond with actual position
value in
[std_msgs::Float32](http://docs.ros.org/api/std_msgs/html/msg/Float32.html)
format:

```
SUBSYSTEM=="usb"
ATTR{idVendor}=="7358"
ATTR{idProduct}=="371"
ACTION=="add"
MODE:="0666"
```1

#### set_position

To move the gripper to target position, call \'\'set_position\'\'
service
([std_msgs::float32](http://docs.ros.org/api/std_msgs/html/msg/Float32.html)
request):

```
SUBSYSTEM=="usb"
ATTR{idVendor}=="7358"
ATTR{idProduct}=="371"
ACTION=="add"
MODE:="0666"
```2 where \"\'\'\'value\'\'\'\" is within a range
of \<0 - 12\> mm. The current driver supports\'\'\' only position
control\'\'\', which means that \"goal_velocity\" and
\"goal_acceleration\" are permanently set to default values.

If goal_position within a range, the gripper should respond with
goal_position being accepted and move to desired position:

```
SUBSYSTEM=="usb"
ATTR{idVendor}=="7358"
ATTR{idProduct}=="371"
ACTION=="add"
MODE:="0666"
```3

#### reference

To reference gripper, call \'\'reference\'\' service
([std_msgs::Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
request). Referencing may also help in cases you are not able to move
the gripper although everything else looks okay:

```
SUBSYSTEM=="usb"
ATTR{idVendor}=="7358"
ATTR{idProduct}=="371"
ACTION=="add"
MODE:="0666"
```4

## Xacro model

To visualize Schunk EZN64 gripper in Rviz use
\"ezn64_visualize_standalone.launch\" file.

```
SUBSYSTEM=="usb"
ATTR{idVendor}=="7358"
ATTR{idProduct}=="371"
ACTION=="add"
MODE:="0666"
```5 Since all three fingers are mechanically
interlocked, there is only one joint to control the movement of all of
them. Use joint_state_publisher GUI to test the movement:

![\|height=\"464\",width=\"698\"](attachment:ezn64_standalone.jpg)
