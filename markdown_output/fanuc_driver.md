

```html
<div style="position: relative; margin-top: -1%;">
 <ul>
   <li><a href="http://rosindustrial.org/news/2016/10/7/better-supporting-a-growing-ros-industrial-software-platform"><img src="http://img.shields.io/badge/support%20level-community-lightgray.svg"/></a></li>
 </ul>
</div>
```

## Troubleshooting

This page lists some of the possible errors and issues encountered when
using the fanuc_driver package. The
*Remedy* subsections provide possible solutions.

If you encounter an error not listed on this page or the provided remedy
does not seem to work, please contact the developers posting a message
in the
[ROS-Industrial category](https://discourse.ros.org/c/ros-industrial) on
ROS Discourse.



```wiki
Make sure to check the [[fanuc/indigo/known_issues|Known Issues]] page before posting a message on ROS Discourse.
```



### Controller

#### KAREL programs are invisible on the Program Select window

After copying the KAREL programs onto your controller, you do not see
them on the *Program Select* window, nor can you change the displayed
program `TYPE` to `KAREL Progs`.

**Cause**: Listing and accessing KAREL programs is not enabled on the
controller.

**Remedy**: Enable the listing of KAREL programs by setting the
`\$KAREL_ENB` system variable to `1`. Open the *SYSTEM Variables*
screen (`Menu`→`NEXT`→`SYSTEM`→`Variables`), and scroll down to
`\$KAREL_ENB`. Press `ENTER`, and change the value to `1`. The
modification is immediate, you do not need to restart the controller.

#### MEMO-159: Convert failed in PROG

While trying to copy a new or updated version of any of the
ROS-Industrial KAREL programs, the TP shows the following error:



```
Duplicate creation TYPE mismatch
MEMO-159 Convert failed in PROG
VARS-014 Create type - KL_TYPE failed
```

 Where `PROG` is any KAREL program, and
`KL_TYPE` is a KAREL type used in `PROG`.

**Cause**: The type or structure of a variable used in `PROG` has
changed in the updated version, and the KAREL runtime system cannot
convert the variable to the new type. This error can occur even after
removing `PROG.PC` file from the controller, as the related `.vr`
file (or *variable record*, the file that stores information on
variables) is not automatically deleted upon deleting the p-code file.

**Remedy**: Remove the `PROG.VR` file from the controller. This can be
done from the *Program Select* window, as well as by using the
`Menu`→`FILE` menu (switch to the `MD:` device). If the copy
attempt left a `PROG.PC` file, remove it as well. The copy operation
should now succeed.

In some cases, other (ROS-Industrial) KAREL programs or libraries have
references to the old type as well and these will have to be removed
too. Always first delete the `.PC` file, then the `.VR`.

**Note**: Removing the `.VR` file will result in loss of the values of
the variables stored in the `.VR`. Backup important data before
deleting the files. The `PROG.VA` file should provide you with an
ASCII rendering of the `.VR` file.

#### TPIF-013: Other program is running

Upon trying to (re)start the `ros` TP program, the TP shows the
following error:



```
TPIF-013 Other program is running
```



**Cause**: This is caused by another TPE or KAREL program that is still
running on the controller. You cannot start programs while others are
still running.

**Remedy**: Make sure no other user programs are running or paused on
the controller before trying to start the ROS programs. `Fctn`→`ABORT
ALL` can be used to abort any running programs.

**Note**: You may need to use `ABORT ALL` twice for programs that have
network sockets that are in the `ACCEPT` state. For the `ros_relay`
and `ros_state` programs, this is when the TP shows the following on
the User Menu:



```
12345 I RSTA Waiting for ROS state prox
12345 I RREL Waiting for ROS traj relay
```



and the ROS PC is not connected to the controller. Select
`Fctn`→`ABORT ALL` twice, then try again.

### KAREL driver

#### HOST-144: Comm Tag error

The TP shows the following on the User Menu:



```
12345 E PROG cfg err, TAG idx: N
```

 Where `PROG` is any of `RSTA` or `RREL`,
and `N` is a Server Tag index number.

**Cause**: the configured Server Tag does either not exist, is not
correctly configured, or is not in the correct state.

**Remedy**: make sure you have configured the Tag correctly, and that
the configuration of the respective ROS-Industrial program uses the
correct tag number. Refer to the
[Server Tags](https://index.ros.org/p/fanuc) section of the installation
tutorial for information on Tag setup.

#### FILE-032: Illegal parameter

The TP shows the following on the User Menu:



```
12345 E PROG cfg error: -1
12346 E PROG check cfg
```

 Where `PROG` is any of `RSTA` or `RREL`.

**Cause:** the configuration of the respective program is either
uninitialised, or has not been completed.

**Remedy:** make sure the configuration of all ROS-Industrial programs
has been completed, and that the `checked` entry is set to `TRUE`.
Refer to the [KAREL Programs](https://index.ros.org/p/fanuc) section of
the installation tutorial for information on the setup of the KAREL and
TPE programs.

#### INTP-320: (LIBSSOCK, N) Undefined built-in

Nothing is shown on the User Menu, and all ROS-Industrial programs
(`ros_state`, `ros_relay`) have been aborted.

**Cause**: this is most likely caused by attempting to start the
programs on a controller that does not have all required options
installed. For `libssock`, this is most likely option R648 (*User
Socket Messaging*) (resulting in the missing `MSG_\*` built-ins).

**Remedy**: make sure the controller has all required options installed
(and activated). Refer to the
[Prerequisites](https://index.ros.org/p/fanuc) section of the
installation tutorial for information on which options are required.

If the controller has the required options installed, please report the
issue to the mailinglist and / or the
[ros-industrial/fanuc](https://github.com/ros-industrial/fanuc/issues)
repository. Do not forget to include any relevant information (ROS
release, version of fanuc_driver,
controller type and software and used manipulator).

#### jnt_pkt_srlise err: ERRNO

The TP shows the following on the User Menu:



```
12345 E PROG jnt_pkt_srlise err: ERRNO
12345 I PROG Waiting for ROS ..
```

 Where `PROG` is any of `RSTA` or `RREL`,
and `ERRNO` is a negative error number (possible values: `-67213`).

**Cause**: The ROS client disconnected the TCP socket connection at the
moment the KAREL program tried to write to or read from it.

**Remedy**: This is not an error. The state proxy and trajectory relay
will handle the disconnect and wait for a new connection.

#### exec_move err: -1

The TP shows the following on the User Menu:



```
12345 E RREL exec_move err: -1
12345 I RREL Waiting for ROS ..
```

 The ROS console shows:



```
[ERROR] [1234567890.123456789]: Socket sendBytes failed, rc: -1. Error: 'Broken pipe' (errno: 32)
[ERROR] [1234567890.123456789]: Failed to connect to server, rc: -1. Error: 'Transport endpoint is already connected' (errno: 106)

(the same error repeated)

[ERROR] [1234567890.123456789]: Failed to connect to server, rc: -1. Error: 'Transport endpoint is already connected' (errno: 106)
[ERROR] [1234567890.123456789]: Timeout connecting to robot controller.  Send new motion command to retry.
```

 Sending a new motion command does not always
work.

**Cause**: The ROS client asked the trajectory relay to move to a point
in the current trajectory that the robot is unable to reach (violation
of joint limits). The relay aborts execution of the trajectory and
disconnects the ROS client in that case.

**Remedy**: Verify that the joint limits configured on the Fanuc
controller correspond to those in the used urdf (in the support
package). The MoveIt motion planners depend on these limits to generate
valid trajectories. Update the limits in the xacro macro if there are
any differences. Be sure to regenerate the urdf and any MoveIt packages
that depend on the it.

**Note**: In some cases it may be necessary to restart the `ros` TPE
program on the controller.

#### check_socket err: ERRNO

The TP shows the following on the User Menu:



```
12345 E PROG check_socket err: ERRNO
12345 I PROG Waiting for ROS ..
12345 I PROG Connected
12345 E PROG check_socket err: ERRNO
12345 I PROG Waiting for ROS ..
12345 I PROG Connected
...
```

 Where `PROG` is any of `RSTA` or `RREL`,
and `ERRNO` is a negative error number (possible values: `-67211`,
`-67212` or others in the `67000` range).

Repeats of `check_socket err`, `Waiting for ROS ..` and
`Connected` may also occur.

**Cause**: The most likely cause is a bad network connection, causing
data to be corrupted or TCP/IP sessions to be prematurely terminated.
This error is also seen when trying to connect to the controller over a
wireless network.

**Remedy**: Make sure the cable and network card used are undamaged,
functioning properly and that their configuration is correct for the
network they are connected to. Also make sure that no wireless networks
are between the ROS client and the server programs on the controller. In
computers or laptops with multiple network cards (ie: wired and
wireless), make sure the wireless connection is not being preferred over
the wired one if both are enabled.

**Note**: Using wireless network(s) (segments) is expressly not
supported by the programs in `fanuc_driver`.

#### FILE-051: NESTED kread issued

While running either `ROS_TRAJ` or `ROS_STATE` in a Roboguide
workcell of a `V5.xx` or early `V6.xx` system software version
(FVRC), the User Menu will show various errors and one or both programs
will terminate with a `FILE-051: NESTED kread issues` error in the top
line of the TP screen.

**Cause**: There appears to be a problem with the emulated network
socket infrastructure in Roboguide with system software versions
`V5.xx` and early `V6.xx` that prevents use of any the `MSG_\*`
Karel built-ins. As the `fanuc_driver` Karel programs make extensive
us of those built-ins, the mentioned error is triggered and the programs
cannot continue.

**Remedy**: None. This is a problem with the system software for
versions `V5.xx` and early `V6.xx` in Fanuc Roboguide. If possible,
try to simulate a more recent version of the system software.

### ROS

#### RViz only shows 'collision quality' models

After starting RViz (either by using the `test_\...launch` files in
the support packages, or when running any of the MoveIt
`planning_execution` launch files), the visualisation only shows
collision detail models, even when *Visual Enabled* is selected.

**Cause:** the support packages only include the collision quality
models, as we do not currently have permission from Fanuc to distribute
the detailed CAD models.

**Remedy:** none. A possible work-around would involve re-exporting the
support package meshes from !SolidWorks or any other suitable program. A
complicating factor is that correct display of the model depends on
proper origins of the meshes, which are not necessarily identical to
those of the original models. Additionally, users would need access to
the original models.

#### Interactive marker in RViz cannot be dragged around

After starting `demo.launch` or `moveit_planning_execution.launch`
from any of the Fanuc MoveIt configurations, the 6D interactive marker
cannot be dragged from the starting position, and the terminal window
shows the following error: 

```
[ERROR] [1234567890.123456789]: Exception caught while handling end-effector update: ikfast exception: /path/to/ikfast/plugin/solver.cpp:LINE_NR: polyroots8: Assertion 'rawcoeffs[0] != 0' failed
```



**Cause:** the manipulator is most likely a singular configuration, for
which the IK plugin cannot find any valid solutions. `demo.launch`
(and `moveit_planning_execution.launch` without the `sim:=false`
argument) does not use real joint state data, but a simple joint space
interpolator, for which the initial state puts all joints at their
'zero position'. For some models this is a singular configuration.

**Remedy:** if possible, use a different initial state, command the
manipulator to move away (in joint space) from the singular
configuration, or (if in simulation) use the *random valid* option for
the *Goal State* and click *Plan and Execute* button. As soon as the
manipulator is out of the singular configuration, dragging the
interactive marker should start working again.

#### Kinematic solver fails to find any solutions for customised robot

After editing the urdf or xacro of a robot variant in any of the robot
support packages in [fanuc](https://index.ros.org/p/fanuc) or
[fanuc_experimental](fanuc_experimental) and updating the MoveIt
configuration package to match, the provided kinematic solvers (in a
`fanuc_X_moveit_plugins` package) cannot find any solutions to IK
problems, or solutions returned do not appear to be correct.

Dragging the 6D interactive marker around in RViz also does not seem to
work any more.

**Cause:** The (IKFast based) kinematic solvers provided in the
`fanuc_X_moveit_plugins` packages include code that was generated
off-line and then compiled into the shared libraries that host the
kinematic plugins. This code was generated to match a specific kinematic
structure and cannot easily be re-used with other kinematic chains.

**Remedy:** To keep using an IKFast based plugin, it will have to be
regenerated to make it match the changed kinematics of the robot. As
this essentially generates a new IKFast solver, it is recommended to
create a new plugin package to host it, instead of overwriting the
solver in the `fanuc_X_moveit_plugins` package. Refer to the MoveIt
[Generate IKFast Plugin Tutorial](http://docs.ros.org/kinetic/api/moveit_tutorials/html/doc/ikfast_tutorial.html)
for more information.

As an alternative, a plugin that dynamically constructs an IK solver
based on the robots kinematics (and can thus cope with changes to it)
could be used. Options (with MoveIt or stand-alone) would be
[trac_ik](https://index.ros.org/p/trac_ik), the LMA plugin from
[moveit_kinematics](https://index.ros.org/p/moveit_kinematics) or
[bio_ik](https://github.com/TAMS-Group/bio_ik).

#### Robot stops at seemingly random points during trajectory execution

The TP shows the following on the User Menu:



```
12345 I RREL Trajectory stop
```

 The ROS console shows:



```
[ERROR] [1234567890.123456789]: Controller is taking too long to execute trajectory (the expected upper bound for the trajectory execution was X.Y seconds). Stopping trajectory.
[ INFO] [1234567890.123456789]: MoveitSimpleControllerManager: Cancelling execution for
[ INFO] [1234567890.123456789]: Execution completed: TIMED_OUT
```

 Where `X.Y` is some duration in seconds.

**Cause:** the !MoveIt *Trajectory Execution Manager* detects a
trajectory execution overrun, and aborts execution of the trajectory.
This is often due to the physical robot not being able to attain the
speeds specified in the trajectory. The Fanuc KAREL trajectory relay
overrides specified motion speed, resulting in the quoted error message.

**Remedy:** increase the !MoveIt duration scaling parameter, or disable
duration monitoring completely. See the *The Trajectory Execution
Manager* section on the
[Executing Trajectories with MoveIt!](https://index.ros.org/p/fanuc)
page on the !MoveIt wiki or
[How do I disable execution_duration_monitoring ?](http://answers.ros.org/question/196586/how-do-i-disable-execution_duration_monitoring/)
on ROS Answers for more information.

#### Failed to load byte array

The TP shows the following on the User Menu:



```
12345 I RSTA Connected
12345 I RREL Connected
```

 The ROS console shows:



```
[ERROR] [1234567890.123456789]: Set buffer size: 1060, larger than MAX:, 1024
[ERROR] [1234567890.123456789]: Failed to load byte array
```

 **Cause:** one possible cause is a difference
in endianness between the robot and the PC running ROS. The Fanuc stack
includes preconfigured launch files taking the endianness of the
specific robot controller into account. If the actual controller uses a
different endianness, the communication will not work properly.

**Remedy:** try to provide the launchfile with a different value for the
`use_bswap` argument. For most controllers, this is set to `true`.
If appending `use_bswap:=false` solves the problem, please report the
issue to the mailinglist and / or the
[ros-industrial/fanuc](https://github.com/ros-industrial/fanuc/issues)
repository. Do not forget to include any relevant information (ROS
release, version of fanuc_driver,
controller type and software and used manipulator).

#### Unable to reconnect to the robot

The TP shows the following on the User Menu:



```
12345 I RSTA Waiting for ROS state prox
12345 I RREL Waiting for ROS traj relay
12345 I RSTA Connected
```

 or



```
12345 I RREL Connected
```

 The ROS console shows:



```
[ERROR] [1234567890.123456789]: Failed to connect to server, rc: -1. Error: 'Connection timed out' (errno: 110)
[..]
[ERROR] [1234567890.123456789]: Timeout connecting to robot controller.  Send new motion command to retry.
```

 **Cause:** this error can be caused by an
incomplete and / or unexpected shutdown of the ROS-Industrial nodes on
the PC, leaving the ROS-Industrial programs on the controller in an
inconsistent state. In such a case, the socket on the controller is
still waiting for a timeout to occur and blocks any new connection
attempt in the meantime.

**Remedy:** either wait for the timeout on the controller to occur, or
forcibly stop the ROS-Industrial programs on the controller using
`Fctn`→`ABORT (ALL)`. Now restart the programs on the controller,
then restart the ROS nodes on the PC.

#### J3 on TP and joint_3 in ROS do not match

When comparing the joint angle shown on the TP for `J3` and the
`joint_3` entry in the `JointState` message as published by the
`robot_state` ROS node, the values do not seem to match, even though
the robot is shown in the correct pose in RViz and all planning and
execution seems to work correctly.

**Cause:** all Fanuc robots have a `J2/J3` coupling configured that
compensates the `J3` angle to keep `J3` in the same position
relative to `J2` when jogging `J2`. The ROS driver compensates for
this, as ROS needs the *decoupled* joint angle for `J3`. All
`JointState` messages will have their `joint_3` entry set to the
result of `J3 - J2`, leading to the discrepancy between what the TP
shows and ROS `/joint_state` publications.

**Remedy:** none. This is an integral feature and design characteristic
of Fanuc robots. It is also only a visualisation issue: the
`fanuc_driver` nodes will automatically compensate for the coupling
and remove and add it back when needed. **Always** use decoupled values
for `joint_3` when interacting with the nodes in `fanuc_driver`.

**Note:** on some controllers, the TP can be configured to show the
value for `J3` that corresponds to what the ROS driver uses. This is
shown on the `POSITION` screen in `Joint` display mode, below the
values for the joints. Look for the `J2/J3 Interaction` item.
