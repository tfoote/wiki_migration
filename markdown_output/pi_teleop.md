## Overview

The pi_teleop ROS package provides an HTML5/rosbridge GUI for
teleoperating and monitoring a robot running ROS. The only requirement
on the client is an HTML5-compatible browser so that the same interface
can be run on a desktop, tablet or smart phone.

## Release Status

Please note that this is a very early beta version of the package.

## Installation

### Install the rosbridge package

**NOTE**: This package uses version 1.0 of rosbridge, not version 2.0.
To get version 1.0, move into your personal ROS directory and run:

```
$ svn co http://brown-ros-pkg.googlecode.com/svn/trunk/distribution/brown_remotelab/rosbridge
$ cd rosbridge
$ rosmake --rosdep-install
```

### Install the mjpeg_server package

Move into your personal ROS directory and run:

```
$ svn co http://svn.code.sf.net/p/bosch-ros-pkg/code/trunk/stacks/mjpeg_server
$ cd mjpeg_server
$ rosmake --rosdep-install
```

### Install the pi_teleop package

Move into your personal ROS directory, then run the commands:

```
$ svn co http://pi-robot-ros-pkg.googlecode.com/svn/trunk/experimental/pi_teleop
$ cd pi_teleop
$ rosmake --rosdep-install
```

### (Optional but recommended): Install the ROS By Example stack

If you want to be able to test the pi_teleop package using a simple
simulator, then install the
[ROS By Example](http://code.google.com/p/ros-by-example/) stack as
follows. Move into your personal ROS directory and run:

```
$ svn co http://ros-by-example.googlecode.com/svn/trunk/rbx_vol_1
$ rosmake rbx_vol_1
$ rospack profile
```

### Setting up a Web Server

Before using the pi_teleop package, you will need to make the pi_teleop
directory accessible to a web server running on your robot. If you are
already running the Apache webserver and you know how to add access to
the pi_teleop directory, you can go that route.

A simpler method is to use the small
[dhttpd](http://dhttpd.sourceforge.net/cgi-bin/index.pl) web server.
First, install the dhttpd package as follows:

```
$ sudo apt-get install dhttpd
```

The dhttpd daemon will attempt to start on port 80 immediately after
being installed and may or may not be successful depending on whether or
not you are already using port 80. In any event, kill this initial
process like this:

```
$ sudo pkill dhttpd
```

Now run the dhttpd process on an unpriviledge port like 8181 and set the
pi_teleop directory as the document root. The command to do this is:

```
$ dhttpd -p 8181 -r `rospack find pi_teleop`
```

To test that you have the webserver running correctly, bring up an HTML5
web browser like Google Chrome and point to:

```
http://localhost:8181/
```

You should see the pi_teleop GUI.

### Testing with a Fake Robot

If you installed the ROS By Example stack in STEP 4 above, you can test
many of the pi_teleop controls using a fake robot and RViz.

First launch the fake robot, a test map, a move_base node, and fake
localization:

```
$ roslaunch pi_teleop fake_pi_teleop.launch
```

Now fire up RViz:

```
$ rosrun rviz rviz -d `rospack find rbx1_nav`/nav_electric.vcg
```

Then, on the same machine, point your browser to:

```
$ svn co http://svn.code.sf.net/p/bosch-ros-pkg/code/trunk/stacks/mjpeg_server
$ cd mjpeg_server
$ rosmake --rosdep-install
```0

If you already had this page up, click on the Reload button.

You should now be able to move the robot in RViz with the Base Control
trackpad on the right of the pi_teleop interface and you can pan and
tilt the head of the fake robot using the Servo Control trackpad on the
left.

Click on the Navigation tab and you can send the robot to different
locations on the test map.

### Testing on a Tablet or a different Computer

Once this is working, try it on a tablet on or another machine on your
local network using an HTML5 browser (e.g. Chrome) and point to:

```
$ svn co http://svn.code.sf.net/p/bosch-ros-pkg/code/trunk/stacks/mjpeg_server
$ cd mjpeg_server
$ rosmake --rosdep-install
```1

where x.y.z.w is the IP address of the webserver machine. Or use the
Zeroconf hostname:

```
$ svn co http://svn.code.sf.net/p/bosch-ros-pkg/code/trunk/stacks/mjpeg_server
$ cd mjpeg_server
$ rosmake --rosdep-install
```2

Try the controls and observe the fake robot's motion in RViz.
