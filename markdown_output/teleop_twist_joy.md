## Overview

The purpose of this package is to provide a generic facility for
tele-operating Twist-based ROS robots with a standard joystick. Examples
of such platforms include [TurtleBot](Robots/TurtleBot),
[Husky](Robots/Husky), and [Kingfisher](Robots/Kingfisher).

This node provides no rate limiting or autorepeat functionality. It is
expected that you take advantage of the features built into
[joy](https://index.ros.org/p/joy) for this.

## ROS API

The package comes with a node which may be used out of the box.



```clearsilver
name=teleop_node
desc=Republish Joy messages as scaled <<MsgLink(geometry_msgs/Twist)>> messages.
pub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Command velocity messages arising from Joystick commands.
}
sub {
  0.name = joy
  0.type = sensor_msgs/Joy
  0.desc = Joystick messages to be translated to velocity commands.
}
param {
  0.name = ~enable_button
  0.type = int
  0.desc = Joystick button to enable regular-speed movement.
  0.default = 0
  1.name = ~enable_turbo_button
  1.type = int
  1.desc = Joystick button to enable high-speed movement (disabled when -1).
  1.default = -1
  2.name = ~axis_linear
  2.type = int
  2.desc = Joystick axis to use for linear movement control.
  2.default = 1
  3.name = ~scale_linear
  3.type = double
  3.desc = Scale to apply to joystick linear axis for regular-speed movement, in m/s.
  3.default = 0.5
  4.name = ~scale_linear_turbo
  4.type = double
  4.desc = Scale to apply to joystick linear axis for high-speed movement, in m/s.
  4.default = 1.0
  5.name = ~axis_angular
  5.type = int
  5.desc = Joystick axis to use for angular movement control.
  5.default = 0
  6.name = ~scale_angular
  6.type = double
  6.desc = Scale to apply to joystick angular axis for regular-speed movement, in rad/s.
  6.default = 1.0
  7.name = ~scale_angular_turbo
  7.type = double
  7.desc = Scale to apply to joystick angular axis for high-speed movement, in rad/s.
  7.default = ~scale_angular
}
```



## C++ API

The teleop translation functionality is embeddable, if you'd like to
compile it into a larger "base" node for your robot. See the
[TeleopTwistJoy](http://docs.ros.org/latest-available/api/teleop_twist_joy/html/classteleop__twist__joy_1_1TeleopTwistJoy.html)
class for details or
[teleop_node.cpp](http://docs.ros.org/latest-available/api/teleop_twist_joy/html/teleop__node_8cpp_source.html)
for an example.
