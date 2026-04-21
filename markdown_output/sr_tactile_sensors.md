## Overview

This package contains an interface to the tactile sensors used in our
Dexterous Hand. The tactile sensors are - for the time being - simple
pressure sensors, one on each finger tip, but they will evolve to more
complex tactile sensors.

To ensure the same versatile use as the [sr_hand](sr_hand) package, the
sr_tactile_sensors come in three flavours: dummy sensors, simulated
sensors and real sensors.

-   The **dummy** sensors are useful to check the main steps of your
    algorithm, they\'re very lightweight and don\'t do much except
    return a pressure value for each sensors. The output value of those
    **dummy** sensors is just computed from the joint positions of the
    finger joints.
-   The **simulated** sensors are bumper sensors added to the Gazebo
    model of the Dexterous Hand. If you want more info on how to use the
    tactile sensors Gazebo interface, go to this
    [tutorial](sr_tactile_sensors/Tutorials/Simulation).
-   The **real** sensor interface is accessing the information published
    by the tactile sensors integrated in our hardware. For more
    information, have a look at this
    [tutorial](sr_tactile_sensors/Tutorials/Real).

There\'s a good example on how to use the data coming from the tactile
sensors in the
[Fancy Touch Demo example](http://bazaar.launchpad.net/~shadowrobot/sr-ros-interface/trunk/view/head:/shadow_robot/sr_hand/examples/fancy_touch_demo.py)

## ROS API

### Published Topics

When you start the interface, two topics per sensors will be published
(10 topics in all). Each sensor publishes a pressure value. Each of the
topic is publishing a [std_msgs](std_msgs)/float64 value.

Here is a list of the published topics:

-   **/sr_tactile/touch/ff**
-   **/sr_tactile/touch/mf**
-   **/sr_tactile/touch/rf**
-   **/sr_tactile/touch/lf**
-   **/sr_tactile/touch/th**

### Parameters

A parameter file containing the sensor names to use is loaded into the
parameter server. By default it\'s in
sr_tactile_sensors/param/sensor_names.yaml. This file contains:

-   **display_names**: the names which will be used in the published
    topics (e.g. \"ff\")
-   **sensor_touch_names**: the names under which the touch sensors are
    available in the robot (e.g. FF_Touch).

## Compiling

By default, when you run **rosmake sr_tactile_sensors**, the tactiles
are compiled as a set of dummy sensors.

To compile the interface to the real tactile sensors, run: **REAL_HAND=1
rosmake sr_tactile_sensors**.

If you want to compile the Gazebo tactile sensors: **GAZEBO=1 rosmake
sr_tactile_sensors**.
