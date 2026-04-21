```html
<div style="position: relative; margin-top: -1.3%;">
 <ul>
   <li>Support level: <a href="http://rosindustrial.org/news/2016/10/7/better-supporting-a-growing-ros-industrial-software-platform">community</a></li>
</div>
```

```wiki
[[Included page Industrial/Software_Status/Experimental not found]]
```

## Overview

This stack is developed by Hans Robots and Canonical Robots. It
currently contains packages that provide nodes for communication with
Hans Robots Elfin Robots series of industrial robot controllers, URDF
models for various robot arms and the associated [MoveIt](moveit)
packages. The ROS Industrial driver has been developed as part of an
[ ROSIN ITP](https://rosin-project.eu/ftp/ros-and-fiona-based-environment-manipulation-for-agricultural-data-acquisition)
project.

## Compatibility

### ROS Distros

The current version has only been tested for kinetic distro.

### Robot descriptions and MoveIt packages

Robot description and MoveIt configurations from the `elfin_robot`
stack can be used.

## Installation

Please note that currently, only kinetic version is available.

The following instructions assume that a
[Catkin workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)
has been created at \$HOME/catkin_ws and that the source space is at
\$HOME/catkin_ws/src. Update paths appropriately if they are different
on the build machine.

In all other cases the packages will have to be build from sources in a
Catkin workspace:

```shell
cd /path/to/catkin_ws/src

# retrieve the sources 
git clone -b kinetic-devel https://github.com/canonical-robots/elfin_robot.git

cd /path/to/catkin_ws

# checking dependencies 
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro kinetic

# building
catkin_make

# source this workspace (careful when also sourcing others)
source /path/to/catkin_ws/devel/setup.bash
```

The packages can now be used as regular ROS packages.

Refer to the [catkin tutorials](catkin/Tutorials) for more information
on building catkin workspaces.

## Tutorials

See the [Tutorials](elfin_robot/Tutorials) page for an overview of the
available tutorials.

## Contact us/Technical support

For questions about this package , please contact the developers by
writting to <support (at) canonicalrobots.com> or by posting a message
in the [ROS Driver category](https://discourse.ros.org/c/drivers/) on
ROS Discourse.

## Report a Bug

<<GitHubIssues(canonical-robots/elfin_robot)>>

## Acknowledgement

![rosin_logo\|height=60](http://rosin-project.eu/wp-content/uploads/rosin_ack_logo_wide.png)

Supported by ROSIN - ROS-Industrial Quality-Assured Robot Software
Components. More information:
[rosin-project.eu](http://rosin-project.eu).

![eu_flag\|height=60](http://rosin-project.eu/wp-content/uploads/rosin_eu_flag.jpg)

This project has received funding from the European Union's Horizon 2020
research and innovation programme under grant agreement no. 732287.
