## Hardware Requirements

This package configures the [hokuyo_node](hokuyo_node) to use a hokuyo
scanner for Care-O-bot.

## ROS API

This package doesn't have a own ROS API, it just configures the
[hokuyo_node](hokuyo_node).

## Usage/Examples

For starting the hokuyo node use ```
roslaunch cob_bringup hokuyo.launch
``` For including
the torso in your overall launch file use ```
<include file="$(find cob_bringup)/components/hokuyo.launch" />
```
