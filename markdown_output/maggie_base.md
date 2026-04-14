## Overview

This package provides basic functionality for controlling two
differential wheels.

### Devices Supported

This device supports all the drivers implemented in the
[maggie_motor_drivers](maggie_motor_drivers) package.

## ROS Nodes

```clearsilver
node.0 {
 name = base_motor_node
 desc = ROS node for controlling the rfid.

 pub {
  0.name = odom
  0.type = nav_msgs/Odometry
  0.desc = Publish the odometry of the wheels.
 }

 sub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Subscribe to control the linear and angular velocity.
 }
}
```

## Launch File Examples

In a terminal window, start a base node process running:

```
$ roslaunch maggie_base base.launch robot:=maggie
```

## Examples

An example to read the content of a rfid card could be:

1\. Launch the node. 2. Show the value of the odometry topic:

```
$ rostopic echo /maggie/odom
```
