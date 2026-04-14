## Overview

This package currently holds the plugin for the Create ROS Gazebo
interface.

### Create ROS Gazebo plugin

This plugin handles the exchange of data between the Create simulation
in Gazebo and the ROS world. Important functionalities of the real
Create have been implemented:

-   Publishing
-   odometry data
-   Retrieving
-   velocity commands

### Configuration

The plugin is configured throught the parameters given in the URDF
description. See the [create_description](create_description) for
details.

### Usage

Have a look at the [turtlebot_gazebo](turtlebot_gazebo) package to find
out how to use this plugin.
