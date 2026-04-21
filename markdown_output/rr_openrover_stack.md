## Description

The rr_openrover_stack is a collection of software to operate the the
Rover Pro and Rover Zero. It provides driver support for serial
communication between compute hardware and the Rover Pro and Rover Zero
platforms, as well as support for remote control using PS4 controllers.

Below is the the Node structure of the packages when launched
![\|width="800px"](attachment:rover_robotics_ros_stack3.png)

## Installation

We recommend running through our "Ubuntu 18.04 Computer Setup guide"
on our docs page <https://roverrobotics.com/pages/docs>

This will install necessary systemd scripts (used for starting ROS on
boot), udev rules (nice if you ever unplug your USB devices) and
joystick drivers.

If you want to install this package in isolation you can do so with the
following command 

```
sudo apt-get install ros-melodic-rr-openrover-stack
```



## Release Notes

This package is currently in pre-release meaning the code has been
tested and is functional, but backwards compatibility is not guaranteed
until v1.0.0, so make note of which version you are using and read the
changelog carefully before updating.
