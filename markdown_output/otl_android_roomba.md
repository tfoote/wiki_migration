## Overview

[Youtube](https://www.youtube.com/watch?v=lWmGXgDEOPQ)

It is good idea to use this with [otl_roomba](otl_roomba) package.

## Node Info

```clearsilver
name = ROS Sensor Roomba Controller (Android App)
desc = Publishes cmd_vel by tilting the device.
pub {
0.name = /cmd_vel
0.type = geometry_msgs/Twist
0.desc = Velocity of robot (roomba). 
1.name = /roomba/clean
1.type = std_msgs/Bool
1.desc = start cleaning or stop.
2.name = /roomba/dock
2.type = std_msgs/Bool
2.desc = start docking to charge station of roomba
}
```
