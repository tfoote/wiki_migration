## Overview

This package is part of the [ROS-Industrial](Industrial) program.

## Status

The package is usable as-is, but is not feature complete. However, no
significant development is planned, as development focus has shifted to
[abb_robot_driver](https://github.com/ros-industrial/abb_robot_driver)
(with [abb_libegm](https://github.com/ros-industrial/abb_libegm) and
[abb_librws](https://github.com/ros-industrial/abb_librws)).

Community contributed usability enhancements and new features will
however be accepted and merged.

## YuMi

While it is possible to use this driver with !YuMi, for now this is not
recommended.

Users who have the EGM option available, consider using
[abb_robot_driver](https://github.com/ros-industrial/abb_robot_driver),
as it will offer the best possible motion quality.

The driver does not include any robot models (ie: `_description`
packages) however. Various sources for those exist, one of which could
be [kth-ros-pkg/yumi](https://github.com/kth-ros-pkg/yumi).

## Features

This package currently supports the following:

- IRC5 controllers with !RobotWare 5.13 and up
- Single mechanical units (ie: a basic 6 axis robot)
- Up to 4 integrated external *linear* axes (in a single mechanical
  unit)
- Joint state reporting for all axes (in a single mechanical unit)
- Trajectory downloading for all axes (in a single mechanical unit)

The driver is largely manipulator agnostic, meaning that it will work
with just about any ABB robot an IRC5 controller is compatible with.

### Multi-group robots

There is no special support for robot controllers configured with
multiple mechanical units, but this can be worked-around by setting up
multiple instances of the RAPID programs and assigning them to specific
units. Paired with multiple instances of the ROS nodes (appropriately
namespaced) this supports asynchronous motion execution and state
reporting in multi-group robot setups.

## Requirements

The ABB ROS Server code is written in RAPID, using a socket interface
and multiple parallel tasks. The code was originally tested on an IRC5
controller, with an IRB-2400 robot, but other combinations should also
work. The following controller options are required:

- `623-1`: *Multitasking*
- `672-1`: *Socket Messaging* (in recent !RobotWare versions, this
  option is included with `616-1`: *PC Interface*)

!RobotWare OS version 5.13 or later is required due to the use of
certain socket options. Earlier versions may work, but will require
modifications to the RAPID code.

## Tutorials

Use the links on the [Tutorials](https://index.ros.org/p/abb) page for
access to the tutorials. These explain how to install and set up the
RAPID programs on the controller, as well as how to use them in
conjunction with the ROS nodes in this package.

## Nodes

### robot_state

Connects to the !StateServer RAPID task on the controller and publishes
joint states.

#### Action Feedback

- `feedback_states`
  ([control_msgs/msg/FollowJointTrajectory](https://docs.ros.org/en/rolling/p/control_msgs/msg/FollowJointTrajectory.html)):
  Provide feedback of current vs. desired joint position (and
  velocity/acceleration).

#### Published Topics

- `joint_states`
  ([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html)):
  Joint state for all joints of the connected robot.
- `robot_status`
  ([industrial_msgs/msg/RobotStatus](https://docs.ros.org/en/rolling/p/industrial_msgs/msg/RobotStatus.html)):
  Aggregate controller/robot status (ie: drives enabled, motion
  possible, etc)

#### Parameters

- `robot_ip_address` (`str`, default: `none`): IP address of the
  controller to connect to. If this is not set the node will exit.
- `~port` (`integer`, default: `11002`): TCP port the !StateServer RAPID
  task is listening on.
- `robot_description` (`str`, default: `none`): The urdf xml robot
  description.
- `controller_joint_names` (`[str, str, str, ..]`): (optional) A list
  containing all joints the driver should assume control over. If this
  parameter is not found, the driver will try to extract this from the
  `robot_description` parameter, but this will result in all joints in
  the urdf to be included. If the driver should only publish joint
  states for a subset of the joints in the urdf, the
  `controller_joint_names` parameter must be set.

### motion_download_interface

Connects to the !MotionServer RAPID task on the controller and uploads
trajectories.

#### Subscribed Topics

- `joint_states`
  ([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html)):
  Joint state for all joints of the connected robot.
- `joint_path_command`
  ([trajectory_msgs/msg/JointTrajectory](https://docs.ros.org/en/rolling/p/trajectory_msgs/msg/JointTrajectory.html)):
  Execute a pre-calculated joint trajectory on the robot.

#### Services

- `joint_path_command`
  ([industrial_msgs/srv/CmdJointTrajectory](https://docs.ros.org/en/rolling/p/industrial_msgs/srv/CmdJointTrajectory.html)):
  Execute a new motion trajectory on the robot.
- `stop_motion`
  ([industrial_msgs/srv/StopMotion](https://docs.ros.org/en/rolling/p/industrial_msgs/srv/StopMotion.html)):
  Stop execution of the current motion at the earliest time possible.

#### Parameters

- `robot_ip_address` (`str`, default: `none`): IP address of the
  controller to connect to. If this is not set the node will exit.
- `~port` (`integer`, default: `11000`): TCP port the !MotionServer
  RAPID program is listening on.
- `robot_description` (`str`, default: `none`): The urdf xml robot
  description.
- `controller_joint_names` (`[str, str, str, ..]`, default: `none`):
  (optional) A list containing all joints the driver should assume
  control over. If this parameter is not found, the driver will try to
  extract this from the `robot_description` parameter, but this will
  result in all joints in the urdf to be included. If the driver should
  only control a subset of the joints in the urdf, the
  `controller_joint_names` parameter must be set.

## Contact us/Technical support

For questions about this package or ROS-Industrial in general, please
contact the developers by posting a message in the
[ROS-Industrial category](https://discourse.ros.org/c/ros-industrial) on
ROS Discourse.

## Tutorials

The following tutorials are provided to demonstrate installation and
operation of an [ABB](https://index.ros.org/p/abb) robot using the
ROS-Industrial abb_driver:

- [Installing the ABB ROS Server](#installing-the-abb-ros-server):
  This tutorial walks through the steps of installing the ROS server
  code on the ABB robot controller and configuring the required
  controller settings.
- [Running the ROS Server](#running-the-ros-server):
  This tutorial describes how to run the ABB ROS Server, so the robot
  will execute motion commands sent from the ROS client node.

The following tutorials show how to use the ABB Robot Studio with the
driver:

1\.
[Using Simulated Robot in Robot Studio](#using-simulated-robot-in-robot-studio)\
This tutorial describes how to setup the ABB !RobotStudio simulator for
use with the ROS-Industrial driver.

## Installing the ABB ROS Server

- **Note:** This tutorial assumes basic familiarity with the ABB robot
  controller. Consult the manufacturer's documentation for further
  details on any of the steps listed in this tutorial.
- **Description:** This tutorial walks through the steps of installing
  the ROS server code on the ABB robot controller and configuring the
  required controller settings.
- **Keywords:** ABB, Industrial, IRC5
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:** Next, you'll learn how to run and manage the ABB
  ROS Server
  [Running the server](#running-the-ros-server)

This tutorial has two parts: installing server code and configuring the
controller with the appropriate tasks.

### Prerequisites

The ABB ROS Server code is written in RAPID, using a socket interface
and multiple parallel tasks. The code was originally tested on an IRC-5
controller, with an IRB-2400 robot, but other combinations should also
work. The following controller options are required:

- `623-1`: *Multitasking*
- `672-1`: *Socket Messaging* (in recent !RobotWare versions, this
  option is included with `616-1`: *PC Interface*)

!RobotWare OS version 5.13 or later is required due to the use of
certain socket options. Earlier versions may work, but will require
modifications to the RAPID code.

### Installing Server Code

All files in the
[abb_driver/rapid](https://github.com/ros-industrial/abb_driver) (Indigo
and later) directory should be copied to the robot controller. This
tutorial assumes the files are copied to a "`ROS`" subdirectory
under the system's `HOME` directory (e.g.
`/<system>/HOME/ROS/\*`).

See the manufacturer's documentation for file-transfer methods.
!RobotStudio Online and USB drives are often convenient methods to
transfer files to the controller.

### Configuring Controller Settings

The ROS Server code requires 3 tasks. Some modules are loaded to
specific tasks, and others are shared between tasks, as described below:

#### File Overview

- Shared by all tasks
- `ROS_common.sys` \-- Global variables and data types shared by all
  files
- `ROS_socket.sys` \-- Socket handling and
  [simple_message](https://index.ros.org/p/simple_message)
  implementation
- `ROS_messages.sys` \-- Implementation of specific message types
- Specific task modules
- `ROS_stateServer.mod` \-- Broadcast joint position and state data
- `ROS_motionServer.mod` \-- Receive robot motion commands
- `ROS_motion.mod` \-- Issues motion commands to the robot

#### Create Tasks

1\. Browse to *Controller tab* → *Configuration Editor* → *Controller* →
*Task*, then right-click *New Task*

(In !RobotStudio 5, this is found under *ABB* → *Control Panel* →
*Configuration* → *Topics* → *Controller* → *Task*)

1\. Create 3 tasks as follows:

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------- -- ------------ -- ------------- -- ------- -- ------------- --
     <tablestyle="text-align:left;border-style:solid;border-width:1px"rowbgcolor="#FFFFE0" rowstyle="vertical-align:bottom;font-weight:bold;">Name      Type            Trust Level      Entry      Motion Task   
     ROS_!StateServer                                                                                                                                          SEMISTATIC      !NoSafety        main       NO            
     ROS_!MotionServer                                                                                                                                         SEMISTATIC      !SysStop         main       NO            
     T_ROB1                                                                                                                                                     NORMAL                           main       YES           
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------- -- ------------ -- ------------- -- ------- -- ------------- --

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     <tablebgcolor="#E6E6FF" tablestyle="border-style:solid;border-width:1px;">It is easiest to wait until all configuration tasks are completed before rebooting the controller.   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

**NOTES:** 1. *-The `T_ROB1` motion task probably already exists on
your controller.-// 1.* -If `T_ROB1` has existing motion-control
modules, you may need to rename the `main()` routine in
`ROS_Motion.mod` to `ROS_main()`. In this case, set the Entry point
for `T_ROB1` task to `ROS_main()`.-// 1. *-For multi-robot
controllers, specify the desired robot (e.g. `rob1`) for each
task-// 1.* -`SEMISTATIC` tasks will auto-start when controller is
booted. They are visible, but cannot be easily seen for troubleshooting.
For debug or development purposes, it may be desired to set both
`ROS_\*Server` tasks to `Type=NORMAL`.-//

#### Create Signals

1\. Browse to *Controller tab* → *Configuration Editor* → *I/O System* →
*Signal*, then right-click *New Signal*

(In !RobotStudio 5, this is found under *ABB* → *Control Panel* →
*Configuration* → *Topics* → *I/O* → *Signal*)

1\. Create 7 signals as follows:

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------- --
     <tablestyle="text-align:left;border-style:solid;border-width:1px"rowbgcolor="#FFFFE0" rowstyle="vertical-align:bottom;font-weight:bold;">Name      Type of Signal   
     signalExecutionError                                                                                                                                       Digital Output   
     signalMotionPossible                                                                                                                                       Digital Output   
     signalMotorOn                                                                                                                                              Digital Output   
     signalRobotActive                                                                                                                                          Digital Output   
     signalRobotEStop                                                                                                                                           Digital Output   
     signalRobotNotMoving                                                                                                                                       Digital Output   
     signalRosMotionTaskExecuting                                                                                                                               Digital Output   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------- --

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     <tablebgcolor="#E6E6FF" tablestyle="border-style:solid;border-width:1px;">It is easiest to wait until all configuration tasks are completed before rebooting the controller.   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

#### Tie Signals to the System Outputs

1\. Browse to *Controller tab* → *Configuration Editor* → *I/O System* →
*System Output*, then right-click *New System Output*

(In !RobotStudio 5, this is found under the *ABB* → *Control Panel* →
*Configuration* → *Topics* → *I/O* → *System Output*)

1\. Add one entry for signal as follows:

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------- -- ------- -- -------- -- ------- -- ------- --
     <tablestyle="text-align:left;border-style:solid;border-width:1px"rowbgcolor="#FFFFE0" rowstyle="vertical-align:bottom;font-weight:bold;">Signal Name      Status                          Arg 1      Arg 2       Arg 3      Arg 4   
     signalExecutionError                                                                                                                                              Execution Error                 N/A        T_ROB1      N/A        N/A     
     signalMotionPossible                                                                                                                                              Runchain OK                     N/A        N/A         N/A        N/A     
     signalMotorOn                                                                                                                                                     Motors On State                 N/A        N/A         N/A        N/A     
     signalRobotActive                                                                                                                                                 Mechanical Unit Active          ROB_1      N/A         N/A        N/A     
     signalRobotEStop                                                                                                                                                  Emergency Stop                  N/A        N/A         N/A        N/A     
     signalRobotNotMoving                                                                                                                                              Mechanical Unit Not Moving      ROB_1      N/A         N/A        N/A     
     signalRosMotionTaskExecuting                                                                                                                                      Task Executing                  N/A        T_ROB1      N/A        N/A     
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------- -- ------- -- -------- -- ------- -- ------- --

#### Load Modules to Tasks

1\. Browse to *Controller tab* → *Configuration Editor* → *Controller* →
*Automatic Loading of Modules*, then right-click *New Automatic Loading
of Modules*

(In !RobotStudio 5, this is found under *ABB* → *Control Panel* →
*Configuration* → *Topics* → *Controller* → *Automatic Loading of
Modules*)

1\. Add one entry for each server file as follows:

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------------------- -- ----------- -- ----------- -- -------- --
     <tablestyle="text-align:left;border-style:solid;border-width:1px"rowbgcolor="#FFFFE0" rowstyle="vertical-align:bottom;font-weight:bold;">File      Task                    Installed      All Tasks      Hidden   
     HOME:/ROS/ROS_common.sys                                                                                                                                                           NO             YES            NO       
     HOME:/ROS/ROS_socket.sys                                                                                                                                                           NO             YES            NO       
     HOME:/ROS/ROS_messages.sys                                                                                                                                                         NO             YES            NO       
     HOME:/ROS/ROS_stateServer.mod                                                                                                                              ROS_!StateServer       NO             NO             NO       
     HOME:/ROS/ROS_motionServer.mod                                                                                                                             ROS_!MotionServer      NO             NO             NO       
     HOME:/ROS/ROS_motion.mod                                                                                                                                   T_ROB1                  NO             NO             NO       
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------------------- -- ----------- -- ----------- -- -------- --

1\. After the last change, select __YES__ to restart the controller
and apply the changes.

#### Updating Software

To update robot-server files with new code versions, use the following
procedure to ensure that the changes are actually applied:

1\. Copy the new/updated files onto the robot controller, as before. 1.
Restart the controller using a **P-Start**

- *ABB* → *Restart* → *Advanced* → *P-Start* → *OK*
- *NOTE: This will erase any existing modules that have been loaded to
  memory. This may cause compilation issues on restart. If this is a
  concern, try another method: Warm Start, manually reloading modules
  (may require setting SEMISTATIC tasks to NORMAL tasks), etc.* 1. After
  the controller reboots, the new changes should be active.

## Running the ROS Server

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Installing the ABB ROS Server](https://index.ros.org/p/abb).
- **Description:** This tutorial describes how to run the ABB ROS
  Server, so the robot will execute motion commands sent from the ROS
  client node.
- **Keywords:** ABB, Industrial, IRC5
- **Tutorial Level:** BEGINNER

### Overview

As described in
[Installing the ROS Server](https://index.ros.org/p/abb), the ABB ROS
Server consists of 3 tasks. In the previous tutorial, 2 of those tasks
were configured as SEMISTATIC (background) tasks, and the 3rd task is a
NORMAL task. The following sections describe how to run the ABB ROS
Server tasks, to allow motion control by external (PC-based) ROS nodes.

### Socket-Server Tasks

The two socket-server tasks (ROS_!MotionServer and ROS_!StateServer)
are configured as SEMISTATIC (background) tasks, and will run
automatically when the controller is booted. It is not possible to start
or stop these tasks from the robot pendant. To restart the tasks, reboot
the robot controller.

### Robot Motion Task

The T_ROB1 task is responsible for issuing motion commands to the robot.
It is run as a NORMAL (foreground) task, and requires explicit user
action to run the task. *When the controller is booted, it is not able
to execute motion commands until the user first runs the T_ROB1 task.*

The T_ROB1 task should already be configured with the required RAPID
modules when the controller boots. It must also be configured to run in
`Continuous Mode`. Consult the controller's documentation for
instructions on how to set the Run Mode using the Quickset Menu.

The following sections describe how to run this task, depending on
whether the controller is in MANUAL or AUTO mode:

#### Running in MANUAL mode

1\. Display the ABB __Production Window__ (or Program Editor)
screen 1. Check to see that a Program Pointer is displayed . press the
"PP to Main" softkey if required 1. Hold the pendant __Enable__
Switch . the drives should power on, and the screen should show "Motors
On" 1. Press the __PLAY__ button to run the program 1. Issue the
desired motion command from the ROS/PC application

Here are a few notes about running in MANUAL mode:

- *the enable switch must be held during all robot motions*
- the robot runs at **reduced speed**
- releasing the enable switch (or pressing STOP) will stop the robot
- to resume motion, re-engage the enable switch and press the PLAY
  button
- ROS may try to cancel the move, since it takes longer than expected.
  Disable this behavior as described
  [here](http://moveit.ros.org/wiki/Executing_Trajectories_with_MoveIt!#The_Trajectory_Execution_Manager)

#### Running in AUTO mode

1\. Press the __Drives On__ button on the controller . the light
should stay on, and the pendant should show "Motors On" 1. Press the
__PLAY__ button to run the program

Here are a few notes about running in AUTO mode:

- the robot runs at **full speed**. Be careful.
- make sure the robot workspace is clear of personnel and obstructions
- motion could start at any time, when commanded from the remote ROS
  application
- press STOP on the pendant to stop the robot, and PLAY to resume motion

## Using Simulated Robot in Robot Studio

- **Description:** This tutorial describes how to setup the ABB
  !RobotStudio simulator for use with the ROS-Industrial driver.
- **Keywords:** ABB, Industrial, IRC5, !RobotStudio
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [Installing the ABB ROS Server](https://index.ros.org/p/abb)

### ABB RobotStudio

It's possible to simulate the communication between ROS and an ABB arm,
by replacing the real arm by a simulated arm. In this case, there are
two PC's: one PC running windows and a simulated ABB arm (called the
WINDOWSPC from now on) and one PC running Ubuntu and ROS (called ROSPC
from now on).

### RobotStudio Setup

The following steps will guide you for setting up the environment on the
WINDOWSPC: 1. Install ABB !RobotStudio from the
[ABB website](http://new.abb.com/products/robotics/robotstudio/downloads).
Note that there is a 30-days trial version of the software, but that you
will need a license in the long run (!RobotStudio is a very powerful
tool with many options. You can look online for
[tutorials](http://new.abb.com/products/robotics/robotstudio/how-to-use-it)
or have a look at the !RobotStudio
[forum](http://forums.robotstudio.com/)). 1. The following steps will
set up a robot arm able to communicate with ROS in !RobotStudio: a. Open
!RobotStudio by clicking on the icon that was placed on the desktop
during installation. a. In the opening dialog, create an empty station.
a. Select *ABB library* and pick the robot type you want to model. a.
The robot is spawned. You can zoom (scroll wheel), move (`CTRL+drag
mouse`) and rotate (`CTRL+SHIFT+drag mouse`). a. Select *Virtual
Controller* and choose *From Layout\...* a. Give the system a name,
leave the rest of the options untouched and press *Next >*. a. There
should be only one mechanism, so just press *Next >*. a. Click
*Options\...* and select *616-1 PC interface* and *623-1 Multitasking*.
a. Click *Finish*.

### Install RAPID Files

Before continuing in !RobotStudio, you need to put the RAPID files of
the ROS driver on the controller of the created arm.

1\. Go to `<documents_directory>\\RobotStudio\\Systems` and select
the folder corresponding to the name of your station. 1. Open the
`HOME` directory. 1. Create a new directory called `ROS`. 1. Copy
all the files from
[abb_driver/rapid](https://github.com/ros-industrial/abb_driver) (Indigo
and later) directory and place them in the newly created `ROS`
directory.

### GetSysInfo() patch

As the `GetSysInfo(..)` function does not return a valid IP address
when used in !RobotStudio (it returns "VC" instead of the IP of your
Windows machine), we need to change something in the `ROS_socket.sys`
source file.

Make sure your Windows PC has a static IP configured. In the example
below, we'll assume that this IP is `192.168.1.1`. If your
workstation does not have a static IP address, you'll have to repeat
the below changes each time your IP address changes.

Now open `ROS_socket.sys` and change the following line:



```
IF (SocketGetStatus(server_socket) = SOCKET_CREATED) SocketBind server_socket, GetSysInfo(\LanIp), port;
```



into:



```
IF (SocketGetStatus(server_socket) = SOCKET_CREATED) SocketBind server_socket, "192.168.1.1", port;
```



note: **use the IP of your workstation running !RobotStudio, the IP
shown here is only an example**.

### Install ROS-I Driver

You are now ready to install the ROS-Industrial driver in !RobotStudio:

1\. Select the tab *controller* and then *!FlexPendant*. This is a
simulated version of the !FlexPendant on the real robot on which you
need to install the driver. 1. First go into `MANUAL` mode by
selecting the button left from the joystick and turning the key in the
upright position. 1. You can now follow the installation instructions
from the ABB
[install server](#installing-the-abb-ros-server)
tutorial.
