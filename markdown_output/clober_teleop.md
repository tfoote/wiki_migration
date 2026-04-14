\'\'ROS Software Maintainer: [Clobot](http://wiki.ros.org/clobot)\'\'

## Overview

![Clober Robot\|width=400](attachment:clober/clober_right.png)

\'\'\'clober teleop\'\'\' packages are currently under development.
We\'ll be launching our hardware and related packages on the coming
months!

## Clober e-Manual

-   [Clober e-manual on gitbook](https://app.gitbook.com/@clobot-git/s/clober-manual/)

## ROS API

```clearsilver
node.1 {
name= teleop_twist_keyboard
desc= This package is used [[http://wiki.ros.org/teleop_twist_keyboard|teleop_twist_keyboard]]
}
pub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Twist has a linear component, for the (x,y,z) velocities, and an angular component for the angular rate about the (x,y,z) axes.
}
```

## References related to Clober

-   [Website for Clobot](http://www.clobot.co.kr/)
