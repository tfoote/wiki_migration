## Overview

This package contains 2 nodes that communicate with the input devices
and publishes \<\<MsgLink(geometry_msgs/Twist)\>\> to an arbitrary
number of output topics, which allows control over a multiple number of
robots.

## ROS API

```clearsilver
node.0 {
name = joystick_teleoperator
desc = Reads input data from an external physical joystick device, processes it, and publishes <<MsgLink(geometry_msgs/Twist)>> with the corresponding output data.

pub{
   0{
    name = joy_cmd_vel
    type = geometry_msgs/Twist
    desc = The linear and angular velocity
   }
}
param{
    0.name = dev
    0.type = string
    0.default = `"/dev/input/js0"`
    0.desc = Usb device input port
}
```

```clearsilver
node.0 {
name = velocity_dispatcher
desc = Subscribes to a number of velocity input topics, and routes one selected input topic data, to the selected output topic. allows dynamic switching between of input/output channels via topics.

sub{
0.name= *input_topics parameter*
0.type= geometry_msgs/Twist
0.desc= An array of input velocity topics, usually defined in the launch file.
1.name= set_input
1.type= std_msgs/Int32
1.desc= Changes the currently active input (ranges from 1 to number of topics).
2.name= set_output
2.type= std_msgs/Int32
2.desc= Changes the currently active output (ranges from 1 to number of topics, 0 to disable output).

}
pub{
   0{
    name = *input_topics parameter*
    type = geometry_msgs/Twist
    desc = An array of output velocity topics, usually defined in the launch file.
   }
   1{
    name = current_input
    type = std_msgs/Int32
    desc = Publishes the current active input topic at 1Hz.
   }
   2{
    name = current_output
    type = std_msgs/Int32
    desc = Publishes the current active output topic at 1Hz.
   }
}
param{
    0.name = input_topics
    0.type = dictionary
    0.desc = Description of input topics.

    1.name = output_topics
    1.type = list of strings
    1.desc = List of output topic names.
}
```
