<https://github.com/csiro-robotics/dynamixel_interface>

![\|align=\"centre\"](https://i.imgur.com/HCrmRDS.gif)

# Overview

This package wraps the Robotis
[dynamixel_sdk](https://wiki.ros.org/dynamixel_sdk) in an easy to use,
fast and scalable driver that makes configuring and controlling many
dynamixels very straightforward. Simply create a single custom yaml file
specifying the ports, ids and some simple configuration info then load
it into the driver at launch time.

Features:

-   Fast C++ implementation capable of controlling 10\'s of dynamixels
    at very high (\>\>100Hz) rates.
-   Easily configure all dynamixels in a single yaml file
-   Synchronous across multiple serial ports (using threaded IO)
-   All dynamixel states/commands are exchanged via a single
    sensor_msgs/JointState message
-   Supports position, velocity and current\* control modes.
-   In position control mode, can supply profile velocities as well

```{=html}
<!-- -->
```
-   current control not available on all models.

Currently the following series of motors are supported:

-   AX
-   RX
-   DX
-   EX
-   MX
-   XM
-   PRO
-   PRO+
-   P

# Installation

## Requirements

-   Ubuntu 18.04 LTS and ROS Melodic; or
-   Ubuntu 20.04 LTS and ROS Noetic

## Dependencies

-   [dynamixel_sdk](https://wiki.ros.org/dynamixel_sdk)

## Building from source

```highlight
mkdir -p catkin_ws/src
cd catkin_ws/src
git clone https://github.com/csiro-robotics/dynamixel_interface.git
cd ..
rosdep install --from-paths src --ignore-src -r -y
catkin build
```

# Usage

For detailed instructions, consult the tutorials on github:

-   [Tutorial 1: Using The Controller](https://github.com/csiro-robotics/dynamixel_interface/blob/noetic-devel/tutorials/tutorial_1_using_the_controller.md)
-   [Tutorial 2: Multi Port Communications](https://github.com/csiro-robotics/dynamixel_interface/blob/noetic-devel/tutorials/tutorial_2_multi_port_communication.md)

## Operation

To use the dynamixel_interface_controller to operate servos:

1\. Create a controller_config.yaml with the necessary parameters for
each servo (see the tutorials as well as the example in the config/
folder for an example and explanation of the various configuration
options) 2. Launch the dynamixel_interface_controller_node, loading in
the custom config file (see the example in the launch/ folder)

During operation:

-   The controller communicates using the sensor_msgs::JointState
    message.
-   Current joint states are published to /joint_states
-   Commands should be sent to /desired_joint_states
-   For each control mode
-   Position Control: only position and velocity are considered in the
    command message, velocity controls the moving speed to the goal
    position of the dynamixel. If no velocity is specified the default
    is used
-   Velocity Control: only the velocity value is considered
-   Torque Control: only the effort value is considered
-   Note that all non-empty arrays must have the same length as the
    array of joint_names, otherwise the command is invalid

A note on units:

-   Positions are in radians
-   Velocities are in radians/second
-   Effort is in mA of current

# Improving Driver Performance

Got too many dynamixels? Driver running too slow? Well, this driver is
designed with goal of achieving the maximum possible loop rate for a
given configuration of dynamixels. To that end, there are three key
optimisations that we recommend:

## Baud rate

The baud rate used to communicate on the bus directly affects the
maximum achieveable loop rate on the bus. A higher loop rate will result
in faster update rates but can reduce the noise the bus can tolerate,
for most applications the recommended baud rate is the maximum of 3Mbps.

## Return delay time

The return delay time is a parameter on the dynamixels that sets the
amount of delay in microseconds before they respond to a packet, by
default this value is quite large (250, which equates to 500
microseconds). Lowering this value will reduce the total round-trip time
for any comms on the bus. It is recommended to set this value very low
(tested at 5, or 10 microseconds).

Both the above values will need to be configured PRIOR TO OPERATION
using the dynamixel wizard available from robotis.

## FTDI Driver Latency For Serial Communications

Since 16.04, the default latency_timer value for the ftdi usb driver was
changed from 1ms to 16ms. This value represents how long the kernel
driver waits before passing data up to the user application. It
significantly affects the speed the driver will be able to communicate
with the dynamixels, resulting in very low achievable loop rates. To
correct this, a script is included that can change a serial port into
\'low latency\' mode (a latency_timer value of 1), which requires the
installation of the setserial command:

# Related Links

-   Syropod Highlevel Controller:
    <https://github.com/csiro-robotics/syropod_highlevel_controller>
-   Legged Robotics Research At CSIRO:
    <https://research.csiro.au/robotics/our-work/research-areas/legged-robots/>
