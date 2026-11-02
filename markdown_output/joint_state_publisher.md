{ }}}}

## Overview

This package publishes
[sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html)
messages for a robot. The package reads the `robot_description`
parameter from the [parameter server](Parameter Server), finds all of
the non-fixed joints and publishes a !JointState message with all those
joints defined.

This package can be used in conjunction with the
[robot_state_publisher](https://index.ros.org/p/robot_state_publisher)
node to also publish transforms for all joint states.

## Usage / data input

There are four possible sources for the value of each !JointState:

1\. Values directly input through the GUI 1. !JointState messages that
the node subscribes to 1. The value of another joint 1. The default
value

Each is described in details:

### GUI



```wiki
The GUI functionality has been split out of the main `joint_state_publisher` package into its own package called `joint_state_publisher_gui`.  The old `use_gui` parameter to `joint_state_publisher` is removed.  For packages transitioning before this change, `joint_state_publisher_gui` should be added as an `<exec_depend>` to package.xml and launch files should be updated to launch `joint_state_publisher_gui` instead of using `joint_state_publisher` with `use_gui` parameter.
```



If GUI is present, the package displays the joint positions in a window
as sliders. Each slider is set to the joints' min and max limits,
except for continuous joints, which range from -Pi to +Pi. Joint
velocity limits are not taken into account when publishing joint state
messages.

![](https://raw.githubusercontent.com/ros/joint_state_publisher/kinetic-devel/joint_state_publisher_gui/screenshot.png)

### Subscribing JointState messages

Set the `source_list` parameter, see below.

### Dependent Joints

This node also lets you constrain certain joints to be equal to other
joints, or multiples of other joints. For example, if you had two
separate joints for two wheels, but wanted them to turn at the same
rate, you could constrain the rotation of one to be equal to the other.
Or, if you had two unequally sized pulleys, and wanted to have one
pulley drive the other, you could constrain the second pulley to turn 3
times as fast as the other.

This is can be specified through the `dependent_joints` parameter or
the `mimic` tag in the [URDF](URDF).

### Default value

The default value is zero. If zero is not a permissible value
*(max+min)/2* is used. To override the default value for some joints,
use the `zeros` parameter. An example YAML file is seen below.

## Node API

### joint_state_publisher

Publishes !JointState message with values read from various sources,
including GUI.

#### Published Topics

- `joint_states`
  ([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html)):
  Joint State for each non-fixed joint in the robot

#### Parameters

- `robot_description` (`String`, default: `None`): Contents of the URDF
  file for the robot
- `dependent_joints` (`Map of Maps`, default: `None`): The keys in the
  map are the names of the constrained joints. The values are maps which
  define a parent joint name, and optionally, a factor which to multiply
  the parent's value by to get the constrained joints value. An example
  YAML file can be seen below.
- `rate` (`Integer`, default: `10 Hz`): Rate at which joint states are
  published
- `source_list` (`list of strings`, default: `[]`): A list of topics to
  listen on for
  [sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html)
  messages.
- `use_mimic_tags` (`Boolean`, default: `True`): Boolean flag to use
  mimic tags from URDF
- `zeros` (`Dict mapping Strings to Floats`, default: `{}`): Dictionary
  to specify some joints' 'zero position' (since hydro)
- `use_smallest_joint_limits` (`Boolean`, default: `True`): (?) Somehow
  narrow the joint limits using URDF-tag `safety_controller`.
- `publish_default_positions` (`Boolean`, default: `True`): Publish the
  joints' default positions (see
  [Default value](#default-value)
  above) if no other data input is available.
- `publish_default_velocities` (`Boolean`, default: `False`): Publish
  the joints' velocities as 0 if no other data input is available.
- `publish_default_efforts` (`Boolean`, default: `False`): Publish the
  joints' efforts as 0 if no other data input is available.

### Example YAML file for dependent_joints and zeros parameters

The following YAML snippets show examples of how to set the
`dependent_joints` and the `zeros` parameters using YAML syntax.
These can be loaded to the parameter server using the
[<rosparam> tag](https://index.ros.org/p/roslaunch) in a launch file.



```
dependent_joints:
  joint_D: {parent: joint_A, factor: 3 }
  joint_E: {parent: joint_B }
  joint_F: {parent: joint_C, factor: -1 }
```

 

```
zeros:
  joint_A: 1.57
  joint_B: 0.785
```
