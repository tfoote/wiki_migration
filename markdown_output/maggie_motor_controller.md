## Overview

This package provides basic functionality for controlling the motors of
a robot.

### Devices Supported

This device supports all the drivers implemented in the
[maggie_motor_drivers](maggie_motor_drivers) package.

## ROS Nodes

## Launch File Examples

-   For the arms: In a terminal window, start a motor_controller node
    process running:



```
$ roslaunch maggie_motor_controller arms_controller.launch robot:=maggie
```



-   For the neck: In a terminal window, start a motor_controller node
    process running:



```
$ roslaunch maggie_motor_controller neck_controller.launch robot:=maggie
```



## Examples
