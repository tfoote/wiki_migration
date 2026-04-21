## Overview

webots_ros is a package that provides the necessary interfaces to
simulate a robot in the [Webots](https://cyberbotics.com/) open-source
3D rigid body simulator for robots. It integrates with ROS using ROS
messages and services.

[Youtube](https://www.youtube.com/watch?v=O7U3sX_ubGc)

Some of the key features of Webots include:

-   Cross-platform \[windows, linux, mac\].
-   Stable physics engine.
-   Reproducibility.
-   Efficient rendering engine using
    [Physically Based Rendering](https://en.wikipedia.org/wiki/Physically_based_rendering)
    for realistic images.
-   Simple and intuitive user interface.
-   Wide range of simulated
    [sensors](https://www.cyberbotics.com/doc/guide/sensors) and
    [actuators](https://www.cyberbotics.com/doc/guide/actuators)
    available and ready to work.
-   Wide range of
    [robot models](https://www.cyberbotics.com/doc/guide/robots)
    available and ready to work.
-   Wide range of documented
    [samples](https://www.cyberbotics.com/doc/guide/sample-webots-applications).

[Youtube](https://www.youtube.com/watch?v=uphkNrJgqCY)

## Installation

### Webots Software

Webots is a prerequisite to use the webots_ros package. It can be
downloaded from the
[Github repository](https://github.com/cyberbotics/webots/releases). The
installation is straightforward, but if need the installation
instructions can be found
[here](https://www.cyberbotics.com/doc/guide/installing-webots).

### webots_ros Package

#### From Package Manager

```
sudo apt-get install ros-$ROS_DISTRO-webots-ros
```

#### From Sources

The following instructions assume that a
[Catkin workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)
is already available:

```shell
cd /path/to/catkin_ws/src

# retrieve the sources
git clone https://github.com/cyberbotics/webots_ros.git
# if you are not using the latest version of Webots, you need to checkout the tag corresponding to the Webots version: https://github.com/cyberbotics/webots_ros/releases
# if you are using the development version of Webots, you need to checkout the develop branch.

cd /path/to/catkin_ws

# checking dependencies
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro $ROS_DISTRO

# building
catkin_make

# source this workspace (careful when also sourcing others)
source /path/to/catkin_ws/devel/setup.bash
```

The packages can now be used as regular ROS packages.

Refer to the [catkin tutorials](catkin/Tutorials) for more information
on building catkin workspaces.

## Tutorials

See the [Tutorials](webots_ros/Tutorials) page for an overview of the
available tutorials.

## Contact us/Technical support

For questions about this package or Webots in general, get in touch with
the developers on [Discord](https://discord.gg/fyPuMM4).

## Report a Bug

<<GitHubIssues(cyberbotics/webots_ros)>>

## Acknowledgement

[Included page rosin/acknowledgement not found](Included page rosin/acknowledgement not found)

\
\

![OpenDR Logo\|height=60](attachment:opendr_logo.png)

Supported by OpenDR - Open Deep Learning Toolkit for Robotics.\
More information: [opendr.eu](https://opendr.eu/)\

  -- ------------------------------------------------- -- ----------------------------------------------------------------------------------- --
     ![EU Flag\|height=45](attachment:opendr_eu.png)      <99%> This project has received funding from the European Union's Horizon 2020\   
                                                          research and innovation programme under grant agreement No. 871449.                 

  -- ------------------------------------------------- -- ----------------------------------------------------------------------------------- --
