## Overview

![mr_tools data in rqt1\|width=780](attachment:teleop1.png)

This package contains an rqt plugin which allows comfortable ways of
controlling multiple robots, such as external joystick devices,
keyboards and mouses. The plugin also provides visual feedback of the
current velocity.

## ROS API

```clearsilver
node.0 {
name = mr_rqt(rqt plugin)
desc =
pub{
   0{
    name = keyboard_cmd_vel
    type = geometry_msgs/Twist
    desc = The linear and angular velocity
   }
   1{
    name = mouse_cmd_vel
    type = geometry_msgs/Twist
    desc = The linear and angular velocity
   }
}
param{
    0.name = /output_topics
    0.type = list of strings
    0.desc = List of output topic names.
}
```
