## Requirements

-   PR2 robot launched with \`pr2_cockpit\` in \`ROS_PACKAGE_PATH\`
    (sudo robot start -e)
-   Two Phantom Omni running on different computers.

## Running

Prior to running the teleop package, pull out the Omni pens from its
calibration wells.

On the first computer (I use a laptop for this) connected to a Phantom
Omni: ```
rosrun phantom_omni omni2.sh
``` Now place omni2\'s tip back into its
calibration well. This will control the PR2\'s left arm.

On the second computer, also connected to an Omni:
```
roslaunch pr2_omni_teleop stereo_omni_pr2.launch
``` Now, place the right omni\'s tip back into its
calibration well. Open rosconsole on pr2_dashboard.

## User Interface

Adjust the stereo separation with your left and right arrow keys. Then
with both the pens in their calibration well, pull the pens out slowly.
The Omni\'s should now be applying a force guiding you to a point in its
workspace. This point is the location of the PR2\'s end effector in the
Omni\'s workspace. After you have moved to the bottom of this potential
well, activate position control of the PR2 by pressing the grey and
darker grey button on the Omni\'s pen simultaneously (on either Omni but
NOT on both Omni\'s at once). While running, pressing the dark grey
button will close the gripper and pressing the light grey button will
open it. The PR2\'s head also does not need to be repositioned as it
will always track the center point of the two grippers.

To turn off position control, press both the grey and dark grey button
simultaneously (again, on either Omni but NOT both). Push the pens back
into their calibration well.

## Beta Version Warning

The controllers applying the potential well have been updated and seem
very stable. Force feedback has been implemented and can be launched
using the ff_omni_pr2.launch file. This allows you specify the arm you
want to control (left or right) and whether or not to activate force
feedback. The force feedback is currently a position position
architecture. Moving the omni stylus quickly with force feedback
activated will cause you to feel the inertia inherent in moving the
gripper of the PR2 quickly. If you release the stylus while moving
quickly, the omni stylus may go unstable.

## track_gripper.py

This node will track the midpoint of the line joining the PR2\'s gripper
tips, allowing the user to not have to worry about controlling the
PR2\'s pantilt unit during teleoperation. It is also independent of the
\`pr2_omni_teleop package\`. To use it run: ```
rosrun pr2_omni_teleop track_gripper.py
```
