## Overview

This package currently holds the plugin for the Kobuki ROS Gazebo
interface.

### Kobuki ROS Gazebo plugin

This plugin handles the exchange of data between the Kobuki simulation
in Gazebo and the ROS world. Important functionalities of the real
Kobuki have been implemented:

-   Publishing
-   bumper events
-   cliff detection events
-   odometry data
-   IMU data
-   tf data for the base position
-   Retrieving
-   velocity commands
-   motor state commands

### Configuration

The plugin is configured throught the parameters given in the URDF
description. See the [kobuki_description](kobuki_description) for
details.

### Usage

Have a look at the [kobuki_gazebo](kobuki_gazebo) package to find out
how to use this plugin.
