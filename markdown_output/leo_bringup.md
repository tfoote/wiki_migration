## Overview

This package contains resources for bringing up basic Leo Rover
functionalities.

The most important file is the **leo_bringup.launch** which is run by
[LeoOS](LeoOS) at the startup process and includes core software
components used by Leo, such as: host-side [rosserial](rosserial) and
[rosbridge](rosbridge_suite) nodes,
[robot_state_publisher](robot_state_publisher), camera driver and some
more.

## Usage

This package is intended to be used by a system service, but it can also
be used standalone: 

```
roslaunch leo_bringup leo_bringup.launch
```



## Nodes



```clearsilver
name= leo_system
desc= A simple node which exposes system shutdown and reboot functions on ROS topics
sub {
  0.name= system/shutdown
  0.type= std_msgs/Empty
  0.desc= Performs system shutdown.
  1.name= system/reboot
  1.type= std_msgs/Empty
  1.desc= Performs system reboot.
}
pub {
  0.name= robot_namespace
  0.type= std_msgs/String
  0.desc= The namespace of the robot.
}
```


