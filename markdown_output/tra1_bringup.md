# Quick start

To try this package without real robot, type following command in a
terminal:

```
$ roslaunch tra1_bringup tra1_bringup.launch simulation:=true
``` The argument \"simulation:=true\" set the
controller into loop-back mode, to emulate real hardware.

And type this command in another terminal:

```
$ roslaunch tra1_bringup tra1_moveit.launch
``` Now you can see MoveIt! rviz interface to
control the robot.

![ScreenShot\|width=\"75%\"](attachment:Screenshot from 2017-09-15 10-56-31.png)

If you have real tra1 robot (so lucky!), remove the \"simulation\"
argument from roslaunch.

Enjoy!

# Package contents

This package contains launch and config files. The files are organized
in following directories.

-   launch/ contains the launch files to start the system.
-   config/ contains the configuration files for MoveIt!
