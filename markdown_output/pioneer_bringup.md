# Pionner_bringup

A ROS package providing roslaunch scripts for starting the Adept
MobileRobots Pioneer and Pioneer-compatible robots (Including Pioneer 2,
Pioneer 3, Pioneer LX, AmigoBot, PeopleBot, PatrolBot, PowerBot, Seekur
and Seekur Jr.)

\<\<GitHubIssues(amineHorseman/pioneer_bringup)\>\>

# Installation

## Dependencies

### RosAria

RosAria is used to communicate with Pioneer robots hardware:

```
cd ~/catkin_ws/src
git clone https://github.com/amor-ros-pkg/rosaria.git
source ~/catkin_ws/devel/setup.bash
rosdep install rosaria
```

Please refer to the
[official RosAria documentation](http://wiki.ros.org/ROSARIA/Tutorials/How%20to%20use%20ROSARIA)
for more information.

### LMS1XX or LMS200 \[optional\]

Allow to communicate with Sick LMS1xx/LMS200 Laser Range Finders. { }}}}
{ }}}} { }}}}

### Usb_cam  \[optional\]

Allows to communicate with usb cameras and webcams

Skip this section if you don\'t want to use usb cameras, or if you want
to invoke it yourself using another package { }}}} { }}}} { You may get
this error message \'\'ros-kinetic-usb-cam package doesn\'t exist\'\'.

In that case, simply install usb_cam package from source:

```
cd ~/catkin_ws/src
git clone https://github.com/bosch-ros-pkg/usb_cam.git
cd ..
catkin_make
``` }}}}

## Get the source and build the workspace

```
cd ~/catkin_ws/src
git clone https://github.com/amineHorseman/pioneer_bringup.git
cd ..
catkin_make
```

# Usage

There are actually 3 bringup modes:

## Minimal mode

Starts up the robot with a single master ROS environment and ROSARIA:

```
roslaunch pioneer_bringup minimal.launch
```

## Camera mode

Can do everything minimal mode does, but also launches the usb cam node

```
roslaunch pioneer_bringup camera.launch
```

## Laser mode

Can do everything minimal mode does, but also launches the Sick LMS1xx
laser node:

```
roslaunch pioneer_bringup laser_lms1xx.launch
```

If you want to bringup both the laser and camera together use the
following command:

```
roslaunch pionner_bringup laser_lms1xx.launch _camera:=1
```

# Known issues

## Use USB port in RosAria instead of Serial

All the bringup modes call first RosAria package which is responsible to
link ROS with the robot hardware.

Generally, the pioneer robots come with an onboard computer which
communicate with the hardware throught Serial port, that\'s why, in the
minimal.launch file we specify the port value as \"/dev/ttyS0\" (default
value).

Sometimes however, RosAria need to communicate throught USB port, and
then, you need to replace the followin line in the minimal.launch file:

```
<param name="port" value="/dev/ttyS0" />
```

with this one:

```
<param name="port" value="/dev/ttyUSB0" />
```

For more information about this modification, please refer to
[RosAria documentation\|](http://wiki.ros.org/ROSARIA/Tutorials/How%20to%20use%20ROSARIA):

## \'ros-kinetic-usb-cam package doesn\'t exist\'

At the moment of writing this tutorial, usb_cam cannot be located by
\'sudo apt-get install\'

Instead try to install it from source:

```
cd ~/catkin_ws/src
git clone https://github.com/bosch-ros-pkg/usb_cam.git
cd ..
catkin_make
```
