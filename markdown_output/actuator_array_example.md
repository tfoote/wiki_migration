## Overview

A simple example project that demonstrates how to create a custom driver
using the [actuator_array_driver](actuator_array_driver) base class.
This example uses a simulated servo motor to demonstrate the driver
operation while avoiding hardware dependencies.

For details on how to create your own Actuator Array Driver, see the
[tutorials](actuator_array_driver/Tutorials) page.

## ROS Nodes

### example1_driver

This is a very simple example demonstrating the use of the Actuator
Array Driver base class. This example makes use of convinience classes
provided in the base class to read a simple list of actuators from the
parameter server and set up the standard Actuator Array Driver
communication interface. This example does not make use of the robot
description. Instead, the `init_actuator_` function manually fills in
some of the useful properties for each actuator. A Dummy Actuator class
is used to simulate the operation of a real R/C Servo motor. This
removes the need to have specific hardware to test the basic Actuator
Array Driver system.

#### Subscribed Topics

`command`
([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html))
A message containing the desired position of one or more joints
controlled by this driver.

#### Published Topics

`joint_states`
([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html))
The current state of each joint controlled by this driver.

#### Services

`stop`
([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html))
Instruct the driver to stop all actuators immediately.

`home`
([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html))
Instruct each actuator to return to its home position.

#### Parameters

`robot_description_parameter` (string, default: robot_description) The
`example1_driver` node does not use any [urdf](urdf) information, so
this parameter should be set to an empty string.

`joints` (string) An array of joint names to be controlled by this
driver.

#### Configuration Files

`cfg/Example1Joints.yaml` An example [yaml](YAML Overview)
configuration file specifying a set of joints to control.

#### Launch Files

`launch/example1.launch` A simple launch file that starts the
`example1_driver` node and the
[actuator_array_gui](actuator_array_gui) for control.

### example2_driver

This example extends `example1_driver` to use the robot description
file. Because the base class was designed to use the robot description
information, there are very few code changes. The only different is the
custom 'init_actuator_' function now makes use of information
obtained from the robot description instead of using hard-coded
defaults. The only extra work really involved is in the creation of the
robot description file itself.

#### Subscribed Topics

`command`
([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html))
A message containing the desired position of one or more joints
controlled by this driver.

#### Published Topics

`joint_states`
([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html))
The current state of each joint controlled by this driver.

#### Services

`stop`
([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html))
Instruct the driver to stop all actuators immediately.

`home`
([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html))
Instruct each actuator to return to its home position.

#### Parameters

`robot_description_parameter` (string, default: robot_description)
This is the name of a parameter on the parameter server that holds the
robot description [urdf](urdf), not the robot description itself.

`joints` (string) An array of joint names to be controlled by this
driver.

#### Configuration Files

`cfg/Example2Joints.yaml` An example [yaml](YAML Overview)
configuration file specifying a set of joints to control.

`robots/robot2.urdf.xacro` A [urdf](urdf) file describing a simple,
four-link robotic manipulator.

#### Launch Files

`launch/example2.launch` A simple launch file that starts the
`example2_driver` node, a
[robot_state_publisher](robot_state_publisher) to enable the [tf](tf)
system, and the [actuator_array_gui](actuator_array_gui) for control.

### example3_driver

In this example, a timer is used to trigger read events instead of the
built-in `spin()` function. The YAML configuration file associated
with Example3 provides additional properties, such as a channel number
and home position for each servo. The custom 'init_actuator_'
function demonstrates how to read these additional fields from the
XMLRPS structure. Also, as a demonstration, the various helper functions
are called directly, instead of using the all-in-one 'init()'
function. Again, a Dummy Actuator class is used to simulate the
operation of a real R/C Servo motor. This removes the need to have
specific hardware to test the basic Actuator Array Driver system.

#### Subscribed Topics

`command`
([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html))
A message containing the desired position of one or more joints
controlled by this driver.

#### Published Topics

`joint_states`
([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html))
The current state of each joint controlled by this driver.

#### Services

`stop`
([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html))
Instruct the driver to stop all actuators immediately.

`home`
([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html))
Instruct each actuator to return to its home position.

#### Parameters

`robot_description_parameter` (string, default: robot_description)
This is the name of a parameter on the parameter server that holds the
robot description [urdf](urdf), not the robot description itself.

`joints` (string) An array of joint names to be controlled by this
driver.

#### Configuration Files

`cfg/Example3Joints.yaml` An example [yaml](YAML Overview)
configuration file specifying a set of joints to control. Each joint in
this file contains additional information, such as a `channel id` and
`home` position.

`robots/robot3.urdf.xacro` A [urdf](urdf) file describing a simple,
four-link robotic manipulator.

#### Launch Files

`launch/example3.launch` A simple launch file that starts the
`example3_driver` node, a
[robot_state_publisher](robot_state_publisher) to enable the [tf](tf)
system, and the [actuator_array_gui](actuator_array_gui) for control.
