DOCUMENTATION IN PROGRESS

# Overview

This package allows you to control any robot that accepts
geometry_msgs::Twist messages (usually, in a cmd_vel topic). It can use
either (or both) keyboard and joystick as input. Besides controlling the
robot, the input sources generate events
(\<\<MsgLink(universal_teleop/Event)\>\>) which are user-defined
text-based commands.

While this node allows you to tele-operate a robot, it is intended to be
used together with other nodes that autonomously control the robot. The
universal_teleop node is designed so that, by default, it will not
control the robot unless specified. This is done by mapping a keyboard
key or joystick button to a special \"override\" event. When this
key/button is pressed, the universal_teleop node will then start sending
geometry_msgs::Twist messages to the robot. At the same time, this
\"override\" event should be received by node that controls the robot
autonomously so that it can stop controlling the robot.

Keyboard/joystick mappings and linear/angular velocity scales can be
configured by means of standard ROS parameters. Configuration can be
simplified by writing all values directly in YAML in a separate file.
Please check the supplied .launch and .yml files.

## Nodes

```clearsilver
name = universal_teleop
desc = Subscribes to input sources and generates event and control messages
sub {
  0.name = joy
  0.type = sensor_msgs/Joy
  0.desc = button and axis messages used for generating events
  1.name = keyboard/key_up
  1.type = keyboard/Key
  1.desc = key-presses used for generating events
  2.name = keyboard/key_down
  2.type = keyboard/Key
  2.desc = ditto
} 
pub {
  0.name = robot/cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = velocity commands sent to robot when "override" is enabled
  1.name = events
  1.type = universal_teleop/Event
  1.desc = events generated when a key/button is pressed/de-pressed
  2.name = controls
  2.type = universal_teleop/Control
  2.desc = control commands (joystick axis-motions)
}
```
