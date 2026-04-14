## Overview

This package provides a means to control a [WowWee Rovio](rovio) mobile
webcam remotely using a Joystick. This package subscribes to the /joy
topic for joystick commands and converts them into a Twist geometry
message which is published on the /cmd_vel topic.

## ROS API

```clearsilver
pub {
  0.name=cmd_vel
  0.type=geometry_msgs/Twist
  0.desc=Velocity Command
}
sub {
  0.name=joy
  0.type=joy/Joy
  0.desc=Joystick Input
}
srv_called {
  0.name=head_position
  0.type=rovio_common/Head
  0.desc=Control of the head position 
}
```

## Control Layout

The default controls are configured as shown below.

![](attachment:roviojoy.jpg)
