This package contains the ROS control node and its structures to control
the *qbrobotics® qbmove* device. It exploits the features provided by
the base device-independent control library (cf.
[qb_device_control](https://index.ros.org/p/qb_device_control)) and the
specific hardware interface (cf.
[qb_move_hardware_interface](https://index.ros.org/p/qb_move_hardware_interface)).

## Launch files

The two launch files start a ROS node for the *qbmove* respectively to
control it through a GUI and through predefined configurable waypoints
(stored in the `config/qbmove_waypoints.yaml`). In both cases the
controllers setup can be found in the
`config/qbmove_controllers.yaml`; it is recommended not to change the
default settings though.

### gui_control

This launch file calls the template
[full_bringup](https://index.ros.org/p/qb_device_bringup) with the
default settings to bringup a full control node for the *qbmove* based
on GUI inputs. It also starts the Communication Handler and therefore it
is recommended not to start other driver nodes while using this one (cf.
[qb_chain](https://index.ros.org/p/qb_chain) to control several devices
together).

### waypoint_control

This launch file calls the template
[full_bringup](https://index.ros.org/p/qb_device_bringup) with the
default settings to bringup a full control node for the *qbmove* based
on waypoint inputs. It also starts the Communication Handler and
therefore it is recommended not to start other driver nodes while using
this one (cf. [qb_chain](https://index.ros.org/p/qb_chain) to control
several devices together).

## Nodes and API

### qb_move_control

This control library specifically designed for the *qbmove* extends the
[qb_device_control](https://index.ros.org/p/qb_device_control) and
exploits the
[qb_move_hardware_interface](https://index.ros.org/p/qb_move_hardware_interface),
therefore it provides all the ROS resources and requires all the
specifications of this two base packages.

## Tutorials

- [Control Modes](#control-modes):
  Details on the control modes available for the qbmove
- [GUI Control](#gui-control):
  Control the qbmove through a simple GUI
- [Waypoint Control](#waypoint-control):
  Control the qbmove motion through an automatic waypoint trajectory
  loop
- [API Control](#api-control):
  Custom control application using the qbrobotics API

## Control Modes

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [Control](https://index.ros.org/p/qb_device_control).
- **Description:** Details on the control modes available for the qbmove
- **Keywords:** qbrobotics qbmove control
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [GUI Control](#gui-control)

For the sake of simplicity, we are going to cover all the control modes
for a single *[qbmove](Robots/qbmove)*, but it is just a matter of
putting things together and set the launch file parameters properly to
control several devices together
([qb_chain_control](https://index.ros.org/p/qb_chain_control) is
dedicated for such a scope).

All the control modes are initialized in the same manner but with
distinct command line arguments. The default single-device control Node
which brings everything up and simply waits for commands on the above
mentioned Action topic is the following: 

```
roslaunch qb_move_control control.launch standalone:=true activate_on_initialization:=true device_id:=<actual_device_id>
```



- `activate_on_initialization \[false\]`: Activates the motors at
  startup (the device will not move since the first command reference is
  received).
- `device_id \[1\]`: Each device has its own ID, you need to set the
  one of the actual device connect to your system.
- `standalone \[false\]`: Starts the Communication Handler together
  with the control Node. If you set this to `false` (or remove it
  since the default value is `false`), you need to launch the
  Communication Handler in a separate terminal.

It is worth noting that the activation of the motors can be postponed to
improved safety if you are not aware of the state of the system at
startup. To do so just set `activate_on_initialization:=false` (or
remove it since the default value is `false`) and make a call to the
Communication Handler `activate_motors` Service, when your system is
ready, e.g. as follows: 

```
rosservice call /communication_handler/activate_motors {"id: <actual_device_id>, max_repeats: 0"}
```



- `control_duration \[0.01\]`: The duration of the control loop
  expressed in seconds.
- `get_currents \[true\]`: Choose whether or not to retrieve current
  measurements from the device.
- `get_positions \[true\]`: Choose whether or not to retrieve position
  measurements from the device.
- `get_distinct_packages \[false\]`: Choose whether or not to retrieve
  current and position measurements from the device in two distinct
  packages.
- `max_repeats \[3\]`: The maximum number of consecutive repetitions
  to mark retrieved data as corrupted.
- `set_commands \[true\]`: Choose whether or not to send command
  positions to the device.
- `set_commands_async \[false\]`: Choose whether or not to send
  commands without waiting for ack.
- `use_rviz \[true\]`: Choose whether or not to use rviz. If enabled
  you should see a virtual hand on screen performing a similar behavior.

The followings are particular control modes which are enabled with few
parameters, but the concepts of this paragraph hold for all of them:

- [GUI Control](#gui-control):
  Control the qbmove through a simple GUI
- [Waypoint Control](#waypoint-control):
  Control the qbmove motion through an automatic waypoint trajectory
  loop
- [API Control](#api-control):
  Custom control application using the qbrobotics API

## GUI Control

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Control Modes](#control-modes).
- **Description:** Control the qbmove through a simple GUI
- **Keywords:** qbrobotics qbmove control
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Waypoint Control](#waypoint-control)

This control mode is the one suggested to test that everything is
working as expected. You are able to move the *[qbmove](Robots/qbmove)*
shaft position and its stiffness interactively, but nothing more than
this.

*Note that you will probably need this only the very first times and for
debugging.*

To start this mode just add `use_controller_gui:=true` to the general
`roslaunch` command (be sure that the opposite `use_waypoints` is
not used).

After a while a GUI should appear to screen with two empty dropdown
menus, a red enable button below them, and a *speed scaling* slider at
the bottom. 1. Select the *Controller Manager* namespace from the left
menu, e.g. `/<robot_namespace>/control/controller_manager` (where
`<robot_namespace>` is an additional argument of the launch file
needed with several devices). This enables the right menu which provides
all the controllers available for the connected device. 1. Select the
*[qbmove](Robots/qbmove)* controller from the second dropdown menu and
enable it through the circular button. 1. Two slider will appear in the
GUI: the first controls the shaft position (which ranges respectively
within the shaft position limits expressed in radians), while the second
sets the stiffness preset, which ranges from `0` (lowest stiffness) to
`1` (highest stiffness). You can also vary the speed through the
bottom _speed scaling_ slider if you like a faster/slower motion. No
other timing constraints can be set in this mode.

![screen_gui](https://bitbucket.org/qbrobotics/qbmove-ros/raw/dab88e4fd48facdf82237c217b53ad8032b295aa/qb_move_media/screen_gui.png)

## Waypoint Control

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Control Modes](#control-modes),
  [GUI Control](#gui-control).
- **Description:** Control the qbmove motion through an automatic
  waypoint trajectory loop
- **Keywords:** qbrobotics qbmove control
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [API Control](#api-control)

This control mode is a bit more structured and useful than the previous:
it allows to set a fixed trajectory of any number of position waypoints
(with timing constraints) and set the robot to cycle infinitely on it
(because of the loop it is recommended to set the first and last
waypoint in a similar configuration to avoid unwanted sudden changes).

To start this mode just add `use_waypoints:=true` to the general
`roslaunch` command (be sure that the opposite `use_controller_gui`
is not used). You won't see any control interface in this case but the
*[qbmove](Robots/qbmove)* should start moving according to the given
trajectory, parsed from a yaml file located at ```
<robot_package>_control/config/<robot_name>_waypoints.yaml ```
where `robot_name` and `robot_package` are two additional launch
file arguments.

### Customization

You can modify the waypoint trajectory to replicate the behavior you
want: either change the
`<robot_package>_control/config/<robot_name>_waypoints.yaml` or
add another custom application-specific file in the `config`
directory. In the second case you need to set the argument
`robot_name` properly when launching the command from the terminal.

The waypoint configuration is as follows: 

```yaml
# Waypoints describe the desired motion trajectory:
#  - time [s]: can be either a single value or an interval for which joint_positions hold
#  - joint_positions:
#     - shaft position [radians] and stiffness preset [0,1];
#  - joint_velocities: optional, use it only if you want a nonzero values
#     - shaft position [radians/s] and stiffness preset [0,1]/s;
#  - joint_accelerations: optional, use it only if you want a nonzero values
#     - shaft position [radians/s^2] and stiffness preset [0,1]/s^2;
#
# It is worth noting that, if specified, joint_positions, joint_velocities and joint_accelerations must be of size two.

waypoints:
  -
    time: [1.0]
    joint_positions:
      <device_name>: [0.0, 0.0]
  -
    time: [2.75, 3.25]
    joint_positions:
      <device_name>: [1.57, 0.0]
  -
    time: [4.0]
    joint_positions:
      <device_name>: [-0.5, 0.0]
    joint_velocities:
      <device_name>: [-0.5, 0.0]
 -
   ...
```

## API Control

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Control Modes](#control-modes),
  [Waypoint Control](#waypoint-control).
- **Description:** Custom control application using the qbrobotics API
- **Keywords:** qbrobotics qbmove control
- **Tutorial Level:** ADVANCED

If you need a complex (i.e. real) control application, e.g. the
*[qbmove](Robots/qbmove)* is mounted on a robot which uses computer
vision aid to grasp objects, the previous two control modes don't
really help much. What we provide for real applications is the full ROS
libraries to manage and control the device.

You have to dig into the [qb_move](https://index.ros.org/p/qb_move)
package documentation and find what better suite for your needs, e.g.
extend the `qbDeviceControl` class provided, or even redesign some of
its parts by following an approach similar to ours.



```wiki
Our recommendation is to use as much as possible our resources, classes and macros to help you while developing your application. Don't reinvent the wheel!
```



At last, if you come up with a something useful for the whole community,
it will be amazing if you propose your improvement with a Pull Request
in the package of interest on
[our Bitbucket](https://bitbucket.org/account/user/qbrobotics/projects/ROS).
