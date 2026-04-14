## Overview

This package provides a simple GUI for viewing and controlling the state
of a node compliant with the
[actuator_array_driver](actuator_array_driver). The joint names to be
controlled are read from the parameter server. The same
[yaml](YAML Overview) formats used by the Actuator Array Driver are also
acceptable here, so the same configuration file may be used for both
nodes. If available, this node also parses the robot description
[urdf](urdf) for joint limits and other information.

The GUI provides the user with two sets of information for each joint:
(1) the command and (2) the current state of each joint. The user may
adjust the command position slider and change the values of the velocity
and effort fields. Clicking on the \`Send\` button causes the GUI to
publish a single \<\<MsgLink(sensor_msgs/JointState)\>\> message on the
\`command\` topic. Toggling the \`Auto Send\` button causes the GUI to
continuously send command messages at a rate of 10Hz. The \`Home\` and
\`Stop\` buttons produce the corresponding service calls.

![](attachment:actuator_array_gui.png)

## ROS Nodes

### actuator_array_gui

#### Subscribed Topics

\`joint_states\` (\<\<MsgLink(sensor_msgs/JointState)\>\>) The current
state of each joint

#### Published Topics

\`command\` (\<\<MsgLink(sensor_msgs/JointState)\>\>) A message
containing the desired position/velocity/effort of all joints

#### Called Services

\`stop\` (\<\<SrvLink(std_srvs/Empty)\>\>) Instruct the driver to stop
all actuators immediately.

\`home\` (\<\<SrvLink(std_srvs/Empty)\>\>) Instruct each actuator to
return to its home position.

#### Parameters

\`robot_description_parameter\` (string, default: robot_description)
This is the name of a parameter on the parameter server that holds the
robot description [urdf](urdf), not the robot description itself. If no
robot description is available, this parameter should be set to an empty
string and the GUI will use default values for the actuatoir parameters.

\`joints\` (string) This is an array of joint names to be controlled by
this GUI. This is expected to be in [yaml](YAML Overview) format,
probably loaded from a file using [rosparam](rosparam). This array can
be in two different formats. Either it is an array of strings, in which
case each string is assumed to be a joint name. Or it can be an array of
structures containing user-defined information. If the structure
approach is used, one element of each structure must be \`name\`, the
name of the joint. All other information contained within the structure
will be ignored by this GUI.

Example Format #1 ```
joints:

  - joint1
  - joint2
  - joint3
  - joint4
```

Example Format #2 ```
joints:

  - name: joint1
    channel: 0      
    home: 0.0

  - name: joint2
    channel: 3      
    home: -1.57

  - name: joint3
    channel: 1      
    home: 1.57

  - name: joint4
    channel: 2      
    home: 0.785
```
