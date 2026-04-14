## Overview

This package contains Husky control configuration, for interfacing with
[ros_control](ros_control), [twist_mux](twist_mux),
[robot_localization](robot_localization), and
[teleop_twist_joy](teleop_twist_joy). All file paths are relative to the
base package.

### Velocity Input

Husky velocity input is multiplexed across several channels using
[twist_mux](twist_mux). This interface is brought up in
[launch/control.launch](https://github.com/husky/husky_control/blob/indigo-devel/launch/control.launch),
and configured in
[config/twist_mux.yaml](https://github.com/husky/husky_control/blob/indigo-devel/config/twist_mux.yaml).
Channels are preconfigured in descending priority for:

1\. teleoperation 2. interactive marker ([husky_viz](husky_viz)) 3.
autonomous movement ([husky_navigation](husky_navigation)) 4.
miscellaneous external input on the standard \`cmd_vel\` topic.
