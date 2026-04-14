![RB1 BASE \|width=\"600px\"](attachment:rb1_base.jpg)

## Overview

The rb1_base_common stack contains the packages that can be used in
both, real and simulated robot. More information can be found inside
each package.

## List of packages

### rb1_base_control

This package contains the launch and configuration files to spawn the
joint controllers with the ROS controller_manager. It allows to launch
the RB1-Base joint controllers.

### rb1_base_description

This package contains the URDF, meshes and other elements needed in the
robot\'s descriptions contained here. This package includes the
description for RB1-Base with and without elevator.

### rb1_base_localization

This package contains the launch and configuration files needed to start
the localization process as well as the mapping process. By default,
[amcl](http://wiki.ros.org/amcl?distro=noetic ) is the localization
algorithm and for mapping the default node is
[slam_gmapping](http://wiki.ros.org/gmapping).

### rb1_base_navigation

This package contains the launch and configuration files needed to use
the [Navigation Stack](http://wiki.ros.org/navigation?distro=noetic ).
It uses move_base package to move the robot to a desired map-based
position.

### rb1_base_pad

This package contains the launch and configuration files needed to
control the robot with a joystick. It allows to have different
configuration files to the different types of joysticks, such as PS4,
PS3, Logitech and Xbox360.
