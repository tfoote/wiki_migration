## Overview

The packages provides support for CANopen devices within ROS.

It can be divided into different parts:

-   CAN layer abstraction
-   CANopen master with device/object management
-   Profile-specific support, currently only for 402 profile (drives and
    motion control)
-   ROS interfaces, motion control through ros_control

![ros canopen package structure\|width=\"100%\"](attachment:ros_canopen_structure.png)
