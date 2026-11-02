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

### teleop_node

Republish Joy messages as scaled
[geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)
messages.

#### Subscribed Topics

- `joy`
  ([sensor_msgs/msg/Joy](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Joy.html)):
  Joystick messages to be translated to velocity commands.

#### Published Topics

- `cmd_vel`
  ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
  Command velocity messages arising from Joystick commands.

#### Parameters

- `~enable_button` (`int`, default: `0`): Joystick button to enable
  regular-speed movement.
- `~enable_turbo_button` (`int`, default: `-1`): Joystick button to
  enable high-speed movement (disabled when -1).
- `~axis_linear` (`int`, default: `1`): Joystick axis to use for linear
  movement control.
- `~scale_linear` (`double`, default: `0.5`): Scale to apply to joystick
  linear axis for regular-speed movement, in m/s.
- `~scale_linear_turbo` (`double`, default: `1.0`): Scale to apply to
  joystick linear axis for high-speed movement, in m/s.
- `~axis_angular` (`int`, default: `0`): Joystick axis to use for
  angular movement control.
- `~scale_angular` (`double`, default: `1.0`): Scale to apply to
  joystick angular axis for regular-speed movement, in rad/s.
- `~scale_angular_turbo` (`double`, default: `~scale_angular`): Scale to
  apply to joystick angular axis for high-speed movement, in rad/s.

## C++ API

The teleop translation functionality is embeddable, if you'd like to
compile it into a larger "base" node for your robot. See the
[TeleopTwistJoy](http://docs.ros.org/latest-available/api/teleop_twist_joy/html/classteleop__twist__joy_1_1TeleopTwistJoy.html)
class for details or
[teleop_node.cpp](http://docs.ros.org/latest-available/api/teleop_twist_joy/html/teleop__node_8cpp_source.html)
for an example.
