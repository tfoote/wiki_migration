## Overview

webots_ros is a package that provides the necessary interfaces to
simulate a robot in the [Webots](https://cyberbotics.com/) open-source
3D rigid body simulator for robots. It integrates with ROS using ROS
messages and services.

[Youtube](https://www.youtube.com/watch?v=O7U3sX_ubGc)

Some of the key features of Webots include:

- Cross-platform \[windows, linux, mac\].
- Stable physics engine.
- Reproducibility.
- Efficient rendering engine using
  [Physically Based Rendering](https://en.wikipedia.org/wiki/Physically_based_rendering)
  for realistic images.
- Simple and intuitive user interface.
- Wide range of simulated
  [sensors](https://www.cyberbotics.com/doc/guide/sensors) and
  [actuators](https://www.cyberbotics.com/doc/guide/actuators) available
  and ready to work.
- Wide range of
  [robot models](https://www.cyberbotics.com/doc/guide/robots) available
  and ready to work.
- Wide range of documented
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

Refer to the [catkin tutorials](https://index.ros.org/p/catkin) for more
information on building catkin workspaces.

## Tutorials

See the [Tutorials](#tutorials-1) page for an
overview of the available tutorials.

## Contact us/Technical support

For questions about this package or Webots in general, get in touch with
the developers on [Discord](https://discord.gg/fyPuMM4).

## Report a Bug

## Acknowledgement

![ROSIN Logo\|height=60](https://raw.githubusercontent.com/rosin-project/press_kit/master/img/rosin_ack_logo_wide.png)

Supported by ROSIN - ROS-Industrial Quality-Assured Robot Software
Components.\
More information: [rosin-project.eu](http://rosin-project.eu/)\

  -- --------------------------------------------------------------------------------------------------------------- -- ----------------------------------------------------------------------------------- --
     ![EU Flag\|height=45](https://raw.githubusercontent.com/rosin-project/press_kit/master/img/rosin_eu_flag.jpg)      <99%> This project has received funding from the European Union's Horizon 2020\   
                                                                                                                        research and innovation programme under grant agreement No. 732287.                 

  -- --------------------------------------------------------------------------------------------------------------- -- ----------------------------------------------------------------------------------- --

\
\

![OpenDR Logo](doc/opendr_logo.png)

Supported by OpenDR - Open Deep Learning Toolkit for Robotics.\
More information: [opendr.eu](https://opendr.eu/)\

  -- ------------------------------- -- ----------------------------------------------------------------------------------- --
     ![EU Flag](doc/opendr_eu.png)      <99%> This project has received funding from the European Union's Horizon 2020\   
                                        research and innovation programme under grant agreement No. 871449.                 

  -- ------------------------------- -- ----------------------------------------------------------------------------------- --

## Tutorials

The following tutorials are provided to demonstrate the installation and
operation of a Universal Robot using the ROS Industrial interfaces:

- [Sample Simulations](#sample-simulations):
  This tutorial presents the sample simulations included in this
  package.

## Sample Simulations

- **Description:** This tutorial presents the sample simulations
  included in this package.
- **Keywords:** Webots, simulation, pioneer, e-puck, slam, line
  following, video recording
- **Tutorial Level:** BEGINNER

For each simulation, the simplest solution is to use the associated
launch file, but of course, if you prefer you can start Webots, open the
corresponding world and then launch the node yourself.

### Simulation Pionneer 3 AT

This simulation shows a Pionneer 3 AT robot equipped with a Sick lidar
sensor. The robot is performing slam using the *gmapping* package, the
resulting map can be seen using rviz.

![thumb](doc/pioneer3at.png)

You can launch this simulation with the following launch file:


```
roslaunch webots_ros pioneer3at.launch
```



You can then enable SLAM with: 

```
rosrun gmapping slam_gmapping scan:=/pioneer3at/Sick_LMS_291/laser_scan _xmax:=30 _xmin:=-30 _ymax:=30 _ymin:=-30 _delta:=0.2
```



And move the robot using a keyboard: 

```
rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/pioneer3at/pioneer_diff_drive_controller/cmd_vel
```



### Simulation TIAGo

The simulation features the MoveIt integration. It is enough to open
rviz, include the MotionPlanning visualization, and you should be able
to perform motion planning with the TIAGo arm.

![thumb\|width=100%](https://raw.githubusercontent.com/cyberbotics/webots/released/docs/blog/images/webots_ros_tiago.gif)

In addition, the simulation also includes a gmapping support:


```
rosrun gmapping slam_gmapping scan:=/Hokuyo_URG_04LX_UG01/laser_scan _xmax:=5 _xmin:=-5 _ymax:=5 _ymin:=-5 _delta:=0.1
```



And you can control the robot using Twist commands:


```
rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/diff_drive_controller/cmd_vel
```



### Simulation E-Puck Line

This simulation shows an e-puck robot performing line-following.

![thumb](doc/e-puck_line.png)

You can launch this simulation with the following launch file:


```
roslaunch webots_ros e_puck_line.launch
```



### Simulation Keyboard Tele-operated

This simulation shows how to use the keyboard to control a robot.

![thumb](doc/keyboard_teleop.png)

You can launch this simulation with the following launch file:


```
roslaunch webots_ros keyboard_teleop.launch
```



### Simulation Panoramic View Recorder

This simulation shows how to record a movie and move the viewpoint from
a node.

You can launch this simulation with the following launch file:


```
roslaunch webots_ros panoramic_view_recorder.launch
```



### Simulation Catch the Bird

This simulation shows how to use a range-finder device.

You can launch this simulation with the following launch file:


```
roslaunch webots_ros catch_the_bird.launch
```



### Simulation Robot Information Parser

This simulation is the most basic one, the node only parses the robot
and show the list of devices. It is a good base to start building your
own node.

You can launch this simulation with the following launch file:


```
roslaunch webots_ros robot_information_parser.launch
```



### Simulation Complete Test

This simulation doesn't show any particular application but contains an
almost exhaustive list of the services and topics available from the
Webots-ROS interface.

You can launch this simulation with the following launch file:


```
roslaunch webots_ros complete_test.launch
```
