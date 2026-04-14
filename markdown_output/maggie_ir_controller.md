## Overview

This package provides basic functionality for controlling a device
compatible with an IR controller embeded in a robot.

The \'\'TVLabo\'\' file contains all possible commands to use with a TV.
To generate new commands for another TV consult the Users Manual.

### Devices Supported

This device supports all the drivers implemented in the
[maggie_ir_drivers](maggie_ir_drivers) package.

## ROS Nodes

```clearsilver
node.0 {
 name = ir_controller_node
 desc = ROS node for controlling the the IR controller for a TV.

 pub {
  0.name = tv_action
  0.type = maggie_ir_controller_msgs/GetTvAction
  0.desc = Publish the action done based on driver answer. Options are: on, off, vol_up, vol_down, ch_up, ch_down, tv, radio.
 }

 srv_called {
  0.name = send_command
  0.type = maggie_ir_controller_msgs/SetTvAction
  0.desc = Service to send a specific command.
 }
}
```

## Launch File Examples

In a terminal window, start an ir_controller node process running:

```
$ roslaunch maggie_ir_controller ir_controller.launch robot:=maggie
```

## Examples

An example of sending a command for turning on the TV could be:

1\. Launch the node. 2. Send the command:

```
$ rosservice call /maggie/send_command maggie_ir_controller_msgs/SetTvAction "on"
```
