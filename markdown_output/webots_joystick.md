## Overview of the Webots Joystick package

The [webots_joystick](webots_joystick) package is part of the
[webots](webots) stack.

It is a simple example of interfacing Webots and ROS using a C++ Webots
controller and roscpp.

It contains a sample ROS node that is actually a Webots robot
controller. This controller launches the ROS joy node and subscribes to
its 'joy' topic to read the input from a joystick. This input is used
to drive a simulated robot in Webots.

It is a good starting point to implement a C++ interface between Webots
and ROS for controlling simulated robots in Webots from ROS.

## Installation

### Prerequisites

You will obviously need to install Webots in order to be able to use
this package. Webots is a commercial software and if you don't already
have a copy of it, you can get a free 30 day trial version from
[Cyberbotics](http://www.cyberbotics.com). Such a version is actually
equivalent to the full version of Webots PRO, but is limited to 30 days.
It will nevertheless allow you to run the Webots Joystick ROS code.

Webots was declared as a rosdep dependency in the webots packages and is
referred to in the rosdep.yaml file of the Webots stack. However, in
order for ROS to be able to install it automatically, you will need to
setup the correct Webots deb repository in your apt system. The setup
details (repository URL and authentication key file) are provided
[here](http://www.cyberbotics.com/linux).

To run this specific example, you will also need a standard joystick or
gamepad connected to your Linux box.

### Setup

The Webots Joystick package should be installed in a new Webots project.
In order to proceed, you can use the Webots wizard to create a new
Webots project. A Webots project is simply a directory containing a
number of sub-directories including 'controllers' and 'worlds'. Then
you will have to:

-   copy the 'joystick.wbt' file from the 'webots_joystick'
    directory into the 'worlds' directory of your Webots project,

```{=html}
<!-- -->
```
-   create a new directory named 'joystick' in the 'controllers'
    directory of your project and

```{=html}
<!-- -->
```
-   copy all the other files of the 'webots_joystick' directory into
    this new 'joystick' directory.

In order to be able to compile and use this webots_joystick node, you
should add the full path of your Webots project (i.e.,
/home/joe/webots/my_ros_project/) to the ROS_PACKAGE_PATH in
'/opt/ros/cturtle/setup.sh'.

Finally, you may need to adjust the device name in the joy.launch file
(e.g., "/dev/input/js1").

### Compilation

In order to compile this controller, simply go to the joystick This will
in turn call rosmake with all the necessary things to get the joystick
controller compiled and linked against ROS and Webots libraries.
Alternatively, you can also press the "build" button in the Webots
IDE.

## Usage

Simply open the worlds/joystick.wbt file and run the simulation. This
will in turn start the joystick controller that will launch the joy ROS
node (using 'roslaunch') and subscribe to its "joy" topic. When you
move the joystick, the joy node receives an event from the joystick and
emits a corresponding message. This message is received by the joystick
controller that interprets it to drive the simulated robot (i.e., 'up'
-> move forward, 'left' -> turn left, etc.).

It is possible to monitor the output of the joy node while the
simulation is running by issuing the following ROS command:

\$ rostopic echo joy

## Going further with the Webots / ROS interface

This example can be extended in the following directions:

1\) The Webots controller may publish topics with sensory information
coming from the simulated robot, so that other ROS nodes may be able to
read simulated sensor data.

2\) The Webots controller may subscribe to other topics in order to
allow other ROS nodes to drive directly the motors of the simulated
robot, Servos, LEDs or other actuators.

## License

All the software included in the webots_joystick package is distributed
under the open source BSD license.

## Thanks

Credits go to Andreas Breitenmoser (from ETHZ, Switzerland) who
developed the original version of the Joystick/ROS/Webots interface and
to Olivier Michel (from Cyberbotics) who further adapted it.
