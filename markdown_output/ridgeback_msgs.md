## Notes

These messages are the low-level interface between
[Ridgeback](Robots/Ridgeback)'s ARM MCU and integrated PC. Most users
of Ridgeback should be able to use standard ROS interfaces (eg.
[geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html),
[diagnostics](https://index.ros.org/p/diagnostics)) to command and
monitor the robot. A possible exception is to programmatically monitor
system state such as voltage, current, battery, faults, etc.
