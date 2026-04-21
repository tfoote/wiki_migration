## Overview

This tutorial package provides one teleop node:

-   `turtle_teleop_joy` node which can be interfaced with any node
    publishing joy messages to drive turtle1 in turtlesim.

## Running the Tutorial Code

To run the default examples, start by getting the required dependencies
and making the package.



```
$ rosdep install turtle_teleop
$ rosmake turtle_teleop
```



Then there are five different launch files for setting up your device
with the teleop node and driving turtle1 in the turtlesim. See the
[tutorials](turtle_teleop/Tutorials) for more device specific details.

-   turtle_joy.launch - setup for a standard linux joystick
-   turtle_keyboard.launch - setup for a standard keyboard
-   turtle_ps3joy.launch - setup for a PS3 bluetooth joystick
-   turtle_spacenav.launch - setup for a spacenavigator
-   turtle_wii.launch -setup for a wiimote
