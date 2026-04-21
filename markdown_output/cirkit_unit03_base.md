See [Robots/CIR-KIT-Unit03](Robots/CIR-KIT-Unit03) for instructions and
tutorials.

## Overview

The `cirkit_unit03_base` package contains a node for communicating
with the CIR-KIT-Unit03 MCU, and launch files to bring up the
CIR-KIT-Unit03 control and diagnostic systems. The
`cirkit_unit03_node` hardware interface is configured through the
[cirkit_unit03_control](cirkit_unit03_control) package.



```clearsilver
node.0 {
 name = cirkit_unit03_node
 desc = Control and communication node for CIR-KIT-Unit03 MCU. Includes [[ros_control]] integration via [[steer_drive_controller]].
 pub {
  0.name= steer_drive_controller/odom
  0.type= nav_msgs/Odometry
  0.desc= Odometry information from CIR-KIT-Unit03 MCU.
 }
sub {
  1.name= steer_drive_controller/cmd_vel
  1.type= geometry_msgs/Twist
  1.desc= Twist velocity command for CIR-KIT-Unit03 MCU, muxed in [[cirkit_unit03_control]]. External clients should publish to bare `cmd_vel` topic.
}
```


