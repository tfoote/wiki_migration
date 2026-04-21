## Overview

Trike is a robot built from an iRobot Create, a Kinect, a netbook, and a
camera tripod.

![](attachment:trike_sm.jpg)

## Building Trike

### Rewire Kinect

We rewired our Kinect, similarly to as in
[kinect/Tutorials/Adding a Kinect to an iRobot Create](kinect/Tutorials/Adding a Kinect to an iRobot Create).
However, we pulled power from the cargo bay headers, and also put the
12V regulator on the Create-side of the power connectors, so that we
could still use the original wall wart when testing for long periods of
time

On the 25-pin connector, pin 25 is ground and pins 10, 11, and 12 are
switched power (approximately 15 volts). Using a male 25-pin d-sub
connector, we wired up a power/ground connection:

![](attachment:bay_power.jpg)

We then installed the 12V regulator, as found in
[kinect/Tutorials/Adding a Kinect to an iRobot Create](kinect/Tutorials/Adding a Kinect to an iRobot Create)
on a small protoboard, and attached a power connector to the output:

![](attachment:power.jpg)

We also put a matching connector on the original power supply, so that
we can switch between wall power and robot battery.

### Prep Tripod

To mount the Kinect to a tripod, we printed an adapter on a Makerbot 3D
printer. This design can be found on
[Thingiverse](http://www.thingiverse.com/thing:5004):

![](attachment:adapter.jpg)

### Assemble

We then fabricated a small stand to mount the tripod on. This was cut
from 3/4" MDF and screwed down to the Create using the cargo bay
mounts. We installed three wood screws to which the legs of the tripod
were tie-strapped:

![](attachment:trike-plate.jpg)

By having the top edge of the wood screws capture the foot of the
tripod, this is a very rigid mount:

![](attachment:trike-screw.jpg)

Lastly, we gave the robot some character, with some awesome orange hair:

![](attachment:hair.jpg)

## Software

Trike has his own software package, with launch files just for him.
Currently, this includes:

-   **trike_tf.launch** - configures tf frames for the Kinect and mobile
    base.
-   **trike_perception.launch** - starts the Kinect with VGA color image
    and QQVGA point cloud. Includes *trike_tf.launch* internally.
-   **trike_bringup.launch** - starts everything, includes
    *trike_perception.launch* and also connects to the iRobot Create
    mobile base on /dev/ttyUSB0. Will eventually include a URDF model
    for visualizations.
