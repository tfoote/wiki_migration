This package contains the ROS control node and its structures to control
the *qb SoftHand Research* or the *qb SoftHand2 Research* device. It
exploits the features provided by the base device-independent control
library (cf.
[qb_device_control](https://index.ros.org/p/qb_device_control)) and the
specific hardware interface (cf.
[qb_hand_hardware_interface](https://index.ros.org/p/qb_hand_hardware_interface)).

## Launch files

The launch files start a ROS node for the *qb SoftHand Research* or the
*qb SoftHand2 Research* to control it through a GUI and through
predefined configurable waypoints (stored in the
`config/qbhand_waypoints.yaml`). In both cases the controllers setup
can be found in the `config/qbhand_controllers.yaml`; it is
recommended not to change the default settings though.

### gui_control

This launch file calls the template
[full_bringup](https://index.ros.org/p/qb_device_bringup) with the
default settings to bringup a full control node for the device based on
GUI inputs. It also starts the Communication Handler and therefore it is
recommended not to start other driver nodes while using this one (cf.
[qb_chain](https://index.ros.org/p/qb_chain) to control several devices
together).

### waypoint_control

This launch file calls the template
[full_bringup](https://index.ros.org/p/qb_device_bringup) with the
default settings to bringup a full control node for the device based on
waypoint inputs. It also starts the Communication Handler and therefore
it is recommended not to start other driver nodes while using this one
(cf. [qb_chain](https://index.ros.org/p/qb_chain) to control several
devices together).

## Nodes and API

### qb_hand_control

This control library specifically designed for the robotic hand extends
the [qb_device_control](https://index.ros.org/p/qb_device_control) and
exploits the
[qb_hand_hardware_interface](https://index.ros.org/p/qb_hand_hardware_interface),
therefore it provides all the ROS resources and requires all the
specifications of this two base packages.

## Tutorials

- [Control Modes](#control-modes):
  Details on the control modes available for the qb SoftHand Research
  and qb SoftHand2 Research
- [GUI Control](#gui-control):
  Control the qb SoftHand Research and the qb SoftHand2 Research through
  a simple GUI
- [Waypoint Control](#waypoint-control):
  Control the qb SoftHand Research and the qb SoftHand2 Research motion
  through an automatic waypoint trajectory loop
- [API Control](#api-control):
  Custom control application using the qbrobotics API

## Control Modes

For the sake of simplicity, we are going to cover all the control modes
for a *[qb SoftHand Research](Robots/qbhand)* or a
*[qb SoftHand2 Research](Robots/qbhand)*, but it is just a matter of
putting things together and set the launch file parameters properly to
control several devices together
([qb_chain_control](https://index.ros.org/p/qb_chain_control) is
dedicated for such a scope).

All the control modes are initialized in the same manner but with
distinct command line arguments. The default single-device control Node
which brings everything up and simply waits for commands on the above
mentioned Action topic is the following: 

```
roslaunch qb_hand_control control.launch standalone:=true activate_on_initialization:=true device_id:=<actual_device_id>
```



- `activate_on_initialization \[false\]`: Activates the motor at
  startup (the device will not move since the first command reference is
  received).
- `device_id \[1\]`: Each device has its own ID, you need to set the
  one of the actual device connect to your system.
- `standalone \[false\]`: Starts the Communication Handler together
  with the control Node. If you set this to `false` (or remove it
  since the default value is `false`), you need to launch the
  Communication Handler in a separate terminal.

It is worth noting that the activation of the motor can be postponed to
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
  

```wiki
Be aware that both the ''[[Robots/qbhand|qb SoftHand Research]]'' and ''[[Robots/qbhand|qb SoftHand2 Research]]'' are desensorized and therefore it is not possible to know exactly the position of each finger: the screen visualization is just the result of an estimation of the closure value and may differ form the real configuration of your hand (e.g. when grasping an object).
```



The followings are particular control modes which are enabled with few
parameters, but the concepts of this paragraph hold for all of them:

- [GUI Control](#gui-control):
  Control the qb SoftHand Research and the qb SoftHand2 Research through
  a simple GUI
- [Waypoint Control](#waypoint-control):
  Control the qb SoftHand Research and the qb SoftHand2 Research motion
  through an automatic waypoint trajectory loop
- [API Control](#api-control):
  Custom control application using the qbrobotics API

## GUI Control

This control mode is the one suggested to test that everything is
working as expected. You are able to open and close the
*[qb SoftHand Research](Robots/qbhand)* or to command both the synergies
of the *[qb SoftHand2 Research](Robots/qbhand)* interactively, but
nothing more than this.

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
proper controller from the second dropdown menu and enable it through
the circular button. 1. A single or a double slider (depending on the
device connected) will appear in the GUI to control the robotic hand.
These commands are normalized. Move the slider to perform a complete
grasp or to partially open/close the hand. You can also vary the speed
through the bottom *speed scaling* slider if you like a faster/slower
motion. No other timing constraints can be set in this mode.

![screen_gui](https://bitbucket.org/qbrobotics/qbhand-ros/raw/ddbccc369d6846549e9b03c9dce0c2dc6c1115e1/qb_hand_media/screen_gui.png)

## Waypoint Control

This control mode is a bit more structured and useful than the previous:
it allows to set a fixed trajectory of any number of position waypoints
(with timing constraints) and set the robot to cycle infinitely on it
(because of the loop it is recommended to set the first and last
waypoint in a similar configuration to avoid unwanted sudden changes).

To start this mode just add `use_waypoints:=true` to the general
`roslaunch` command (be sure that the opposite `use_controller_gui`
is not used). You won't see any control interface in this case but the
*[qb SoftHand](Robots/qbhand)* should start moving according to the
given trajectory, parsed from a yaml file located at ```
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

The waypoint configuration depends on the device and is as follows for
*[qb SoftHand Research](Robots/qbhand)*: 

```yaml
# Waypoints describe the desired motion trajectory:
#  - time [s]: can be either a single value or an interval for which joint_positions hold
#  - joint_positions:
#     - hand closure [0,1];
#  - joint_velocities: optional, use it only if you want a nonzero value
#     - hand closure [0,1]/s;
#  - joint_accelerations: optional, use it only if you want a nonzero value
#     - hand closure [0,1]/s^2;
#
# It is worth noting that, if specified, joint_positions, joint_velocities and joint_accelerations must be of size one.

waypoints:
 -
   time: [1.0]
   joint_positions:
     <device_name>: [0.0]
 -
   time: [2.25, 2.75]
   joint_positions:
     <device_name>: [0.8]
  -
    time: [4.0]
    joint_positions:
      <device_name>: [0.5]
 -
   ...
```



For *[qb SoftHand2 Research](Robots/qbhand)* instead it is necessary to
send two commands:



```yaml
# Waypoints describe the desired motion trajectory:
#  - time [s]: can be either a single value or an interval for which joint_positions hold
#  - joint_positions:
#     - hand closure [0,1];
#  - joint_velocities: optional, use it only if you want a nonzero value
#     - hand closure [0,1]/s;
#  - joint_accelerations: optional, use it only if you want a nonzero value
#     - hand closure [0,1]/s^2;
#
# It is worth noting that, if specified, joint_positions, joint_velocities and joint_accelerations must be of size two.

waypoints:
 -
   time: [1.0]
   joint_positions:
     <device_name>: [0.0, 1.0]
 -
   time: [2.25, 2.75]
   joint_positions:
     <device_name>: [1.0, 0.8]
  -
    time: [4.0]
    joint_positions:
      <device_name>: [-1.0, 0.5]
   ...
```

## API Control

If you need a complex (i.e. real) control application, e.g. the
*[qb SoftHand Research ](Robots/qbhand)* or the
*[qb SoftHand2 Research](Robots/qbhand)* is mounted on a robot which
uses computer vision aid to grasp objects, the previous two control
modes don't really help much. What we provide for real applications is
the full ROS libraries to manage and control the hand.

You have to dig into the [qb_hand](https://index.ros.org/p/qb_hand)
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
