![\|width="333",height="200"](attachment:Logo-white-medium.jpg)

## Description

The asr_flock_of_birds package is the driver for
[Ascension Technology Corp](http://www.ascension-tech.com/products/product-history/)
magnet tracking system "Flock of Birds" (FoB). It provides the remote
server which publishes two 6d posemarker and the necessary TF from the
magnet tracking system. It also contains launch-files and calibration
tools for the use of it.

## Functionality

Flock of Birds is a 6D tracking system which can very precisely track
position and orientation of three sensors in a magnetic field in front
of the receiver. Each tracker is connected to an data-glove and so only
two trackers are used currently (for left and right hand). If started,
the node publishes periodically the pose of the trackers as TF-publisher
as well as **asr_msgs::!AsrObject**-Messages on the
**/fob_object**-Topic.

![\|width="333",height="200"](attachment:index.png)
![\|width="333",height="200"](attachment:index.jpeg)

Left image: Flock of Birds magnet-tracker receiver with its controller
PC.

Right image: Flock of Birds dataglove with for handmotion captureing
(green) and the Flock of Bilds sensor (red).

## Usage

This package can be used as a standalone-driver for the Flock of Birds
tracker system, but it is recommended to use it as a part of the
[asr_kinematic_chain_dome](asr_kinematic_chain_dome).

### Needed packages

This package depends on **asr_msgs**-Package for the publication of the
fob_objects.

### Needed hardware

[Ascension Technology Corp](http://www.ascension-tech.com/products/product-history/)
magnet tracking system "Flock of Birds" is needed.

### Start system

There are mainly two ways to start the Flock of Birds server: To start
it directly form the PC which the hardware is connected with, use
**roslaunch asr_flock_of_birds flock_of_birds.launch** To start from
another PC, the package provides a remote script. But Firstly, a ssh
connection have to be set up. Secondly, use **rosrun asr_flock_of_birds
flock_of_birds_remote.sh**

## ROS Nodes

The launched Node publishes **asr_msgs::!AsrObject**-Messages on the
**/fob_object**-Topic. There are no configuration or controlling
elements.
