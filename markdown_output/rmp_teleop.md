## Overview

The rmp_teleop package provides teleoperation functionalities for a
Segway Robotics Mobility Platform.

This package currently supports the xbox wireless joytsick.

## Quick Start



```
$ roslaunch rmp_teleop joystick.launch
```



## Node



```clearsilver
node.1 {
  name = joy_node
  desc = Modified version of joy (http://wiki.ros.org/joy). The node won't publish any messages if no event is received within a certain period.
}
node.2 {
 name = rmp_teleop_node
 desc = ros interface to control a Segway RMP 440LE.
 sub {
  1.name= /rmp440le/joy
  1.type= sensor_msgs/Joy
  1.desc= joystick messages
}
 pub {
  1.name= /rmp440le/base/vel_cmd
  1.type= geometry_msgs/TwistStamped
  1.desc= velocity command
  2.name= /rmp440le/deadman
  2.type= rmp_msgs/BoolStamped
  2.desc= deadman
  3.name= /rmp440le/audio_cmd
  3.type= rmp_msgs/AudioCommand
  3.desc= audio command
}
param {
  1.name= joy_topic 
  1.type= string
  1.desc= joystick topic
  1.default= rmp440le/joy
  2.name= velocity_command_topic 
  2.type= string
  2.desc= velocity command topic
  2.default= /rmp440le/base/vel_cmd
  3.name= deadman_topic
  3.type= string
  3.desc= deadman topic
  3.default= /rmp440le/deadman
  4.name= audio_command_topic
  4.type= string
  4.desc= audio command topic
  4.default= /rmp440le/audio_cmd
  5.name= update_frequency
  5.type= double
  5.desc= process update rate
  5.default= 50.0
  6.name= translational_velocity_scale
  6.type= double
  6.desc= translational veolicty scale
  6.default= 2.2352
  7.name= rotational_velocity_scale
  7.type= double
  7.desc= rotational velocity scale
  7.default= 3.0
  8.name= translational_velocity_boost_scale
  8.type= double
  8.desc= translational veolicty boost scale
  8.default= 8.0
  9.name= rotational_velocity_boost_scale
  9.type= double
  9.desc= rotational velocity boost scale
  9.default= 4.4
 }
}
```



## Controller Usage

<https://github.com/sri-robotics/segwayrmp/blob/master/rmp_teleop/xbox_controller_usage.pdf>
