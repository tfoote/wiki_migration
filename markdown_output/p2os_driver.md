## Overview

p2os_driver provides a driver for robots using the Pioneer P2OS/ARCOS
interface in the form of a ROS node.

## Documentation

p2os_driver contains p2os, the main node controlling the pioneer base.

Parameters used:

-   port (string, default=\"/dev/ttyS0\")
-   use_sonar (bool, default=false): is used to decide whether to use
    sonar or not.
-   pulse (float32): is used to control the frequency of checking
    commands and disabling the motors. (set = 1.0 to mute the annoying
    beep)

Subscribed topics: 1. /cmd_vel (type:
[geometry_msgs/Twist](http://ros.org/doc/diamondback/api/geometry_msgs/html/msg/Twist.html))
2. /gripper_control (type:
[p2os_driver/GripperState](http://ros.org/doc/diamondback/api/p2os_driver/html/msg/GripperState.html))
3. /cmd_motor_state (type:
[p2os_driver/MotorState](http://ros.org/doc/diamondback/api/p2os_driver/html/msg/MotorState.html))
4. /ptz_control (type:
[p2os_driver/PTZState](http://ros.org/doc/diamondback/api/p2os_driver/html/msg/PTZState.html))

Published topics: 1. /sonar (type:
[p2os_driver/SonarArray](http://ros.org/doc/diamondback/api/p2os_driver/html/msg/SonarArray.html))
2. /pose (type:
[nav_msgs.Odometry](http://ros.org/doc/diamondback/api/nav_msgs/html/msg/Odometry.html))
3. /gripper_state (type:
[p2os_driver/GripperState](http://ros.org/doc/diamondback/api/p2os_driver/html/msg/GripperState.html))
4. /motor_state (type:
[p2os_driver/MotorState](http://ros.org/doc/diamondback/api/p2os_driver/html/msg/MotorState.html))
5. /aio (type:
[p2os_driver/AIO](http://ros.org/doc/diamondback/api/p2os_driver/html/msg/AIO.html))
6. /ptz_state (type:
[p2os_driver/PTZState](http://ros.org/doc/diamondback/api/p2os_driver/html/msg/PTZState.html))
7. /tf
([tf/tfMessage](http://ros.org/doc/diamondback/api/tf/html/msg/tfMessage.html))
8. /battery_state (type:
[p2os_driver/BatteryState](http://ros.org/doc/diamondback/api/p2os_driver/html/msg/BatteryState.html))
9. /dio (type:
[p2os_driver/DIO](http://ros.org/doc/diamondback/api/p2os_driver/html/msg/DIO.html))
