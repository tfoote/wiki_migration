## Overview

This package provides a convenient gamepad-based control option for
quadrotor UAVs and similar vehicles. The stick setup in the launch files
is similar to the \"Mode 2\" setup commonly used on RC helicopters as
described
[ here](http://www.rc-airplane-world.com/rc-helicopter-transmitter-modes.html ).
The node publishes
[ geomety_msgs/Twist](http://www.ros.org/doc/api/geometry_msgs/html/msg/Twist.html )
messages on the \`/cmd_vel\` topic, so the stick input corresponds to
desired linear and angular velocities.

We currently provide two launch files:

-   logitech_gamepad.launch for Logitech gamepads
-   xbox_controller.launch for Xbox controller gamepads Have a look at
    one of these for instructions on how to make a launch file for your
    own controller.

Other than those two, one is available for controlling it with keyboard
and the source code for the same can be taken from the following git.

[ Hector Keyboard Teleop](https://github.com/lharikrishnan1993/hector_keyboard_teleop )

This is currently under development and has been verified only with
Indigo. I t will be tested for other versions soon.
