![\|width="333",height="200"](attachment:Logo-white-medium.jpg)

## Description

This package controls a motorized robot head (a sensor setup equipped
with a PTU) in order to ensure that the hand of a human user remains
inside its field of view. The human hand is tracked with the help of an
Ascension - Flock of Birds system. The purpose of this package is to
enable continuous localization of objects during their manipulation
through the tracked hand.

## Functionality

To track the current position of the sensor, this tool subscribes to the
Flock ob Birds objects (Topic: /fob_objects) and the current PTU (Topic:
/put_state) joint Angles. The current PTU state is only needed for
direct PTU controlling and not for autonomous tracking. We assume that
the PTU is the center of a sphere because the PTU has only two joints.
Whit this assumption no complex inverse kinematic have to be solved and
only azimuth and altitude have to be calculated like a simple "look
at" function. Azimuth is set as panning (yaw-angle) and altitude for
tilting (pitch-angle) and simply published to the PTU. The following
picture illustrates this as an open loop solution of the problem:

![\|width="373",height="224"](attachment:index.png)
![\|width="338",height="202"](attachment:index2.png)

First of all, the position of magnet tracker (p) is transformed into the
PTU's coordinate frame. Azimuth (a_xy) and altitude (a_yz) are
calculated with the arccos of dot-Product divided by euclidiean
distance. The following equations shows this:
![\|width="307",height="144"](attachment:index3.png)

![\|width="333",height="131"](attachment:index4.png)

Finally, the concrete panning and tiltig angles are transformed to
degree and directly set as the target pan and tilt on the PTU.

![\|width="325",height="97"](attachment:index5.png)

## Usage

To successfully run this tool the whole kinematic chain of the PbD -Dome
has to be started (PTU and Flock of Birds) first and the correct topic-
and framenames have to set in "**tracker_settings.yaml**". With keys
"R" or "L" the PTU can look at the right or left tracker (autonomous
tracking). In addition the PTU can be moved with the arrwokeys (direct
PTU controlling).

### Needed packages

-   asr_flir_ptu_driver: PTU data and controlling
-   asr_flock_of_birds: FoB data
-   asr_msgs: FoB -Messages

### Needed software

-   Boost: Threading

### Needed hardware

-   [Ascension Technology Corp](http://www.ascension-tech.com/products/product-history/)
    magnet tracking system "Flock of Birds" is needed (Or any 3D/6D
    tracking system).
-   Pan Tilt Unit

### Start system

To start tracking first set up all sensors and then use

```
roslaunch asr_flock_of_birds_tracking tracker.launch
```

## ROS Nodes

### Subscribed Topics

-   **/fob_objects**: current pose of FoB -Tracker
-   **/ptu_state**: current joint angles

### Published Topics

-   **/ptu_cmd**: new PTU command

## Source

Pictures and Equations from "Reactive Object Search for Scene
Recognition in Programming by Demonstration" - Valerij Wittenbeck
