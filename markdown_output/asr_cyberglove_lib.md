![\|width=\"333\",height=\"200\"](attachment:Logo-white-medium.jpg)

## Description

The asr_cyberglove_lib package is used to start a server that provides
the current joint state values received from the Cybergloves via ROS
topics.

## Usage

### Needed packages

This package depends on the following packages:

-   [asr_msgs](asr_msgs)

### Needed hardware

The following hardware components are needed:

-   Cybergloves

![\|width=\"430\",height=\"241\"](attachment:cybergloves.jpg)

### Start system

After ensuring that the Cybergloves are turned on, the
asr_cyberglove_lib server can be started directly from the PC to which
the hardware is connected:

```
roslaunch asr_cyberglove_lib glove_lib.launch
``` Instead of using the preconfigured
.launch-file, the server can also be started via *rosrun*, e.g. with:

```
rosrun asr_cyberglove_lib gloveServer_node -r --calibration-file-right $(find asr_cyberglove_lib)/cfg/GloveCalibrationRight.cal --tty-right /dev/ttyD2 -d 0
``` Alternatively, the server can also be started
from remote if the hardware is connected to another Lab-PC. The
following command will also use a preconfigured .launch-file:

```
rosrun asr_cyberglove_lib glove_lib_remote.sh
```

### Start system from remote using different ROS distributions

If the hardware is connected to a ROS Indigo Lab-PC and it is needed to
start the asr_cyberglove_lib server from a remote ROS Kinetic Lab-PC,
some workarounds / dirty hacks are needed. For the following, it is
assumed that both ROS systems use the same file system and that the
corresponding catkin workspaces are */indigo_ws* and */kinetic_ws*.

Open the terminal and source Kinetic (if not already sourced via
/*.bashrc*):

-   *source /opt/ros/kinetic/setup.bash*
-   *source /kinetic_ws/devel/setup.bash*

Additional ssh environment setups are needed
(<https://github.com/sigproc/qbo_sigproc/wiki/Detailed-environment-setup>):

-   *ssh-agent bash*
-   *ssh-add /.ssh/id_rsa*

A ssh connection can now be established, but the /*.bashrc* needs to be
modified to be able to start the server on ROS Indigo:

-   Add: *source /opt/ros/indigo/setup.bash*
-   Add: *source /indigo_ws/devel/setup.bash*
-   Comment out: *source /opt/ros/kinetic/setup.bash*
-   Comment out: *source /kinetic_ws/devel/setup.bash*

The asr_cyberglove_lib server can now be started from remote:

-   *rosrun asr_cyberglove_lib glove_lib_remote.sh*

To listen to the publishing ROS-Topic in a new terminal, ROS Kinetic has
to be sourced again (or modify the /*.bashrc* again before opening the
new terminal):

-   *source /opt/ros/kinetic/setup.bash*
-   *source /kinetic_ws/devel/setup.bash*
-   *rostopic echo /rightGloveData_radian*

Alternatively, the glove movements can also be visualized with the
[asr_cyberglove_visualization](asr_cyberglove_visualization) package
(Kinetic needs to be sourced again):

-   *source /opt/ros/kinetic/setup.bash*
-   *source /kinetic_ws/devel/setup.bash*
-   *roslaunch asr_cyberglove_visualization demo_glove.launch*

## ROS Nodes

### Published Topics

The sensor data of the Cybergloves are published as
**asr_msgs::!AsrGlove **messages to the following topics:

-   ***/rightGloveData***
-   ***/leftGloveData***
-   ***/rightGloveData_radian***
-   ***/leftGloveData_radian***

### Parameters

As mentioned in subsection 2.3, the asr_cyberglove_lib server can be
started directly via *rosrun* without using the preconfigured
.launch-file. For this case, it is needed to specify the *rosrun*
arguments. The following arguments can be passed:

-   *glove-right/r*: Indicates that the right glove should be used.
-   *glove-left/l*: Indicates that the left glove should be used.
-   *calibration-file-right*: If the right glove should be used, specify
    the path to its calibration file. Default: *\"\$(find
    asr_cyberglove_lib)/cfg/GloveCalibrationRight.cal\"*
-   *calibration-file-left*: If the left glove should be used, specify
    the path to its calibration file. Default: *\"\$(find
    asr_cyberglove_lib)/cfg/GloveCalibrationLeft.cal\"*
-   *tty-right*: If the right glove should be used, specify its device
    path. Default: *\"/dev/ttyD2\"*
-   *tty-left*: If the left glove should be used, specify its device
    path. Default: *\"/dev/ttyD3\"*
-   *debug-level/d*: Defines the debug level. The higher, the more debug
    infomation. Default: *\"0\"*
