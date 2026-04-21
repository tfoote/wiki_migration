## Overview

This package provides the functionality of an I/O data acquisition
board.

### Devices Supported

This device supports all the drivers implemented in the
[maggie_labjack_drivers](maggie_labjack_drivers) package.

## ROS Nodes



```clearsilver
node.0 {
 name = labjack_node
 desc = ROS node for controlling the labjack controller.

 srv {
  0.name = get_touch_sensors
  0.type = touch_skill_msgs/LabjackTouchInfo
  0.desc = Service to get the information the touch sensors receive.

  1.name = get_voltage
  1.type = batteries_skill_msgs/LabjackBatteryInfo
  1.desc = Service to get the current voltage of the batteries.

  2.name = is_plugged
  2.type = batteries_skill_msgs/LabjackPlugInfo
  2.desc = Service to get if the robot are connected or not.

  3.name = get_state
  3.type = basic_states_skill_msgs/GetLabjackState
  3.desc = Service to get the current state of the robot. Options are: emergency, sleep, stop, active.

  4.name = set_state
  4.type = basic_states_skill_msgs/SetLabjackState
  4.desc = Service to set the state of the robot. Options are: emergency, sleep, stop, active.
 }
}
```



## Launch File Examples

In a terminal window, start an eyelids node process running:



```
$ roslaunch maggie_labjack labjack.launch robot:=maggie
```



## Examples
