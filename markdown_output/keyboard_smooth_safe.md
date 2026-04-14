The keyboard_smooth_safe packages provides a keyboard teleop for the
waiterbot which uses a modified joint driver to cause smoother movements
and the proximity sensor to avoid collisions with the environment.

## Get Started

To start the keyboard_smooth_safe teleop you first have to bring up the
skin using

```
roslaunch skin_common bringup_skin.launch
``` Then you might want to make sure you have the
right amount of patches set

```
rosrun skin_config skin_config
``` After these steps you are ready to run the
teleop

```
roslaunch keyboard_smooth_safe keyboard_smooth_safe.launch
``` Use the arrow keys to move the robot aroun.

## Parameters

The keyboard_smooth_safe node takes 3 parameters:

-   scale_angular: The speed of turning the robot
-   scale_linear: The speed of linear movement
-   dbl_max_x_orientation: The maximum x orientation a patch is allowed
    to have before it is considered to be in the front (if the patch\'s
    x orientation is positive) or in the back (if the patch\'s
    orientation is negative). Patches in the \"front\" or in the
    \"back\" that are activated stop linear movements in this direction.
