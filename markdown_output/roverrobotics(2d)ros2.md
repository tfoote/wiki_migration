# Overview

This stack contain everything needed for using Rover Robotics products
with ROS 2

<https://github.com/RoverRobotics/roverrobotics_ros2>

## Installation

It is recommended to install this package from binaries using the
following command ```
sudo apt install ros-foxy-roverrobotics-ros2
```

## Packages

-   rover_bringup
-   rover_description
-   rover_driver
-   rover_msgs
-   rover_navigation

### rover_bringup

Contains launch and config files for bringing up the stack of code.
Users should create a systemd script that calls a launch file from this
package in order to bring up this stack when the host computer boots.

### rover_description

Contains models of the Rover Robotics products

### rover_driver

<http://wiki.ros.org/rover-driver>

\-\-\-- /!\\ \'\'\'Edit conflict - other version:\'\'\' \-\-\--
<http://wiki.ros.org/rover-driver>

\-\-\-- /!\\ \'\'\'Edit conflict - your version:\'\'\' \-\-\--

\-\-\-- /!\\ \'\'\'End of edit conflict\'\'\' \-\-\-- Contains drivers
that abstracts away the physical communication (mostly UART) that is
used to communicate with Rover products and presents the user with the
familiar ROS 2 topics such as /cmd_vel

### rover_msgs

Contains custom ROS 2 message definitions

### rover_navigation

Contains code for running Navigation2 with Rover products.
