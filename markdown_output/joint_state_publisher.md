{ }}}}

## Overview

This package publishes <<MsgLink(sensor_msgs/JointState)>> messages
for a robot. The package reads the `robot_description` parameter from
the [parameter server](Parameter Server), finds all of the non-fixed
joints and publishes a !JointState message with all those joints
defined.

This package can be used in conjunction with the
[robot_state_publisher](robot_state_publisher) node to also publish
transforms for all joint states.

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



```clearsilver
name = joint_state_publisher
desc = Publishes !JointState message with values read from various sources, including GUI.
pub {
  0.name = joint_states
  0.type = sensor_msgs/JointState
  0.desc = Joint State for each non-fixed joint in the robot
}
param {
  0.name = robot_description
  0.type = String
  0.desc = Contents of the URDF file for the robot
  0.default = None
  1.name = dependent_joints
  1.type = Map of Maps
  1.desc = The keys in the map are the names of the constrained joints. The values are maps which define a parent joint name, and optionally, a factor which to multiply the parent's value by to get the constrained joints value. An example YAML file can be seen below.
  1.default = None
  2.name = rate
  2.type = Integer
  2.desc = Rate at which joint states are published
  2.default = 10 Hz
  3.name = source_list
  3.type = list of strings
  3.desc = A list of topics to listen on for <<MsgLink(sensor_msgs/JointState)>> messages.
  3.default = []
  4.name = use_mimic_tags
  4.type = Boolean
  4.desc = Boolean flag to use mimic tags from URDF
  4.default = True
  5.name = zeros
  5.type = Dict mapping Strings to Floats
  5.desc = Dictionary to specify some joints' 'zero position' (since hydro)
  5.default = {}
  6.name = use_smallest_joint_limits
  6.type = Boolean
  6.desc = (?) Somehow narrow the joint limits using URDF-tag `safety_controller`.
  6.default = True
  7.name = publish_default_positions
  7.type = Boolean
  7.desc = Publish the joints' default positions (see [[#Default_value|Default value]] above) if no other data input is available.
  7.default = True
  8.name = publish_default_velocities
  8.type = Boolean
  8.desc = Publish the joints' velocities as 0 if no other data input is available.
  8.default = False
  9.name = publish_default_efforts
  9.type = Boolean
  9.desc = Publish the joints' efforts as 0 if no other data input is available.
  9.default = False
}
```



### Example YAML file for dependent_joints and zeros parameters

The following YAML snippets show examples of how to set the
`dependent_joints` and the `zeros` parameters using YAML syntax.
These can be loaded to the parameter server using the
[<rosparam> tag](roslaunch/XML/rosparam) in a launch file.



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


