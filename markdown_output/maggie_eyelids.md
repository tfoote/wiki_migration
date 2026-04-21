## Overview

This package provides basic functionality for controlling two
servomotors working as eyelids of a robot.

### Devices Supported

This device supports all the drivers implemented in the
[maggie_serial_comm_drivers](maggie_serial_comm_drivers) package.

## ROS Nodes



```clearsilver
node.0 {
 name = eyelids_node
 desc = ROS node for controlling the servomotors of the eyelids.

 srv {
  0.name = move_abs_pos
  0.type = motor_controller_msgs/MoveAbsPos
  0.desc = Service to move the eyelid to an absolute position.

  1.name = move_str_pos
  1.type = eyelids_msgs/MoveStrPos
  1.desc = Service to move the eyelid to a predefined position. Options are: open, close, normal.
 }

 param {
  0.name = ~port
  0.type = string
  0.desc = Communication port name.

  1.name = ~side
  1.type = string
  1.desc = Eye option, left or right.
 }
}
```



## Launch File Examples

In a terminal window, start an eyelids node process running:



```
$ roslaunch maggie_eyelids eyelids.launch robot:=maggie
```



## Examples

An example of movement by string could be:

1\. Launch the node. 2. Move by string:



```
$ rosservice call /maggie/move_str_pos eyelids_msgs/MoveStrPos "open"
```


