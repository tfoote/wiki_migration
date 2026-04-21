## Overview

This package controls the Rovio based on velocity commands published to
the /cmd_vel topic. Features such as control of the head position are
offered as a service.

## ROS API



```clearsilver
param {
  0.name=rovio_hostname
  0.type=string
  0.default=192.168.10.18
  0.desc=The hostname of the robot
  1.name=rovio_username
  1.type=string
  1.default=Required
  1.desc=The username to login to the robot
  2.name=rovio_password
  2.type=string
  2.default=Required
  2.desc=The password to login to the robot
}
sub {
  0.name=cmd_vel
  0.type=geometry_msgs/Twist
  0.desc=The twist to command
}
srv {
  0.name=head_position
  0.type=rovio_common/Head
  0.desc=Control of the head position
}
```


