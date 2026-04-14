## Overview

A base class that implements the common Actuator Array interface. This
base class handles the communication with ROS and parses the robot
description URDF for relevant information about the controlled joints. A
custom driver that adheres to the Actuator Array protocol can be created
by implementing just a few functions.

## ROS Nodes

### actuator_array_driver

The \`actuator_array_driver\` is actually a base class and not a node
itself. However, the base class implements the following ROS API, so all
derived nodes will also implement this API. Further, all nodes in the
[actuator_array](actuator_array) stack assume this API.

#### Subscribed Topics

\`command\` (\<\<MsgLink(sensor_msgs/JointState)\>\>) A message
containing the desired position of one or more joints controlled by this
driver. Any joints contained in the command message that are not part of
this driver will be ignored.

#### Published Topics

\`joint_states\` (\<\<MsgLink(sensor_msgs/JointState)\>\>) The current
state of each joint controlled by this driver. The
\<\<MsgLink(sensor_msgs/JointState)\>\> message specifies position,
velocity, and effort/torque information. If the specific hardware
controlled by this driver does not provide velocity or effort
information, then these arrays will be left empty.

#### Services

\`stop\` (\<\<SrvLink(std_srvs/Empty)\>\>) Instruct the driver to stop
all actuators immediately.

\`home\` (\<\<SrvLink(std_srvs/Empty)\>\>) Instruct each actuator to
return to its home position.

#### Parameters

\`robot_description_parameter\` (string, default: robot_description)
This is the name of a parameter on the parameter server that holds the
robot description [urdf](urdf), not the robot description itself. If use
of the robot description is not desired, this parameter can be set to an
empty string and the driver will ignore it.

\`joints\` (string) This is an array of joint names to be controlled by
this driver. This is expected to be in [yaml](YAML Overview) format,
probably loaded from a file using [rosparam](rosparam). This array can
be in two different formats. Either it is an array of strings, in which
case each string is assumed to be a joint name. Or it can be an array of
structures containing user-defined information. If the structure
approach is used, one element of each structure must be \`name\`, the
name of the joint.

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

## C++ Interface

For a complete listing of all functions, see the
[C++ API](http://ros.org/doc/api/actuator_array_driver/html/index.html)
reference. The \`actuator_array_driver\` driver is a base class for
generating that custom drivers that interact with chains of r/c-type
servos with minimal effort. By uses this base class, much of the ROS
interface code is handled automatically and interoperability with the
other nodes in the [actuator_array](actuator_array) stack is guaranteed.

The base class is templated on a \`JOINT\` structure. If no additional
data is needed, the provided \`JointProperties\` can be used as the
template argument. If additional information needs to be stored on a
per-joint basis, then the \`JointProperties\` class can be used as a
base for a custom \`JOINT\` structure.

### Joint Properties

The standard \`JointProperties\` class contains the following entries.
Additional entries can be created by deriving a custom
\`JointProperties\` class using this as a base. This custom JOINT
structure would then be provided as a template argument to the
\`actuator_array_driver\`.

-   has_position_limits (\`bool\`)
-   min_position (\`double\`)
-   max_position (\`double\`)
-   has_velocity_limits (\`bool\`)
-   max_velocity (\`double\`)
-   has_acceleration_limits (\`bool\`)
-   max_acceleration (\`double\`)
-   has_effort_limits (\`bool\`)
-   max_effort (\`double\`)
-   friction (\`double\`)
-   damping (\`double\`)

### Required Functions

Because the specifics of the hardware to be controlled will vary between
applications, the base class provides hooks for the end-user to
implement the actual code nessisary to control the actuators. A default,
empty implementation of each of these functions exist in case certain
functionality is not requird.

`bool init_actuator_(const std::string& joint_name, JOINT& joint_properties,`
`        XmlRpc::XmlRpcValue& joint_data)` A helper method that performs
custom initialization on a per-actuator basis. If the \'joints\'
parameter contains an XMLRPC array of structs, then this function is
also provided with the full XMLRPC structure. This is a convenience
function that allows a single YAML configuration file to both initialize
the list of actuators to control, and define custom properties about
each actuator. Such entries as \`channel id\`, \`offset\` , and \`home\`
are common attributes that are unique to each actuator.

`bool read_(ros::Time ts = ros::Time::now())` Virtual function that is
responsible for reading the current device state and updating the
internal \`joint_state_msg\_\`. The base class will publish these values
if the read was successful.

`bool command_()` Virtual function that handles sending a command to the
device. This gets called once after every message received on the
\`command\` topic. The internal \`command_msg\_\` will already be
updated with the new command information.

`bool stop_()` Virtual function that sends a stop command to the device.
This gets called in response to a \'stop\' service call

`bool home_()` Virtual function that sends the device to the home
position. This gets called in response to a \'home\' service call

### Provided Convenience Functions

`void parse_urdf(const ros::NodeHandle& node)` A helper method that
parses the URDF contained in the \`robot_description_parameter\` on the
Parameter Server and stores it in the \`urdf_model\_\` property of the
base class.

`void update_joint_from_urdf(const std::string& joint_name, JOINT& joint_properties)`
A helper method that extracts information from the URDF model about a
specific joint name and stores it in the provided JOINT class. If the
provided joint name does not exist in the URDF, a warning will be issued
and the JOINT class will not be updated.

`void parse_actuator_list(const ros::NodeHandle& node)` A helper method
that reads in a list of actuator names from the parameter server and
initializes the joints\_ map. This list can be a simple list loaded via
rosparam, or a complex struct defining additional properties about each
actuator. If the struct approach is used, generally loaded via a YAML
file, one entry must be called \'name\'. Additionally, an initialization
function named \'init_actuator\_\' can be implemented. This function is
called once per actuator in the list, and is provided with the full
XMLRPC struct for that actuator. This call occurs after the joint is
updated using the URDF information, so any information inside the URDF
can be accessed by the initialization function. The provided node object
should be in the namespace of the \'joints\' list on the parameter
server (i.e. a private node)

`void advertise_and_subscribe(ros::NodeHandle& node)` A helper method
that sets up the communication elements with ROS. This involves
subscribing to the \'command\' topic, advertising the \'joint_states\'
topic, and creating the \'stop\' and \'home\' services. All topics will
be advertised in the namespace of the provided \'node\' object.

`void init()` A convenience method that calls \'parse_actuator_list\',
\'parse_urdf\' and \'advertise_and_subscribe\' in order. This is broken
out of the constructor to allow derived classes to choose how to
initialize the system (e.g. Gazebo plugin). Most derived classes will
probably want to call init() in the constructor.
