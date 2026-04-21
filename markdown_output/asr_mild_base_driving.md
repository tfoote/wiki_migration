![\|height="200",width="333"](attachment:Logo-white-medium.jpg)

## Description

This package sends driving commands to the motors and receives "Ticks"
from an incremental encoder to control the movement of a differential
drive robot.

Also, the real velocity is adjusted to the required velocity, this means
if the robot should drive straight forward, it doesn't drive a curve.

This package runs on a self-made robot (MILD). But you can take code
from this package for your own motor control.

## Functionality

The package includes two components:

**CanListener**

Get "Ticks" from the incremental encoder. Calculate the odometry from
the ticks and publish them on the ROS-Topic /odom
([Odometry.msg](http://docs.ros.org/api/nav_msgs/html/msg/Odometry.html)).

How the driven distance (d) and the rotated angle (angular_d) are
calculated:

![\|height="279",width="412"](attachment:odometrie.JPG)

**BaseController**

Get ROS cmd_vel messages. Calculate velocities for the left and right
wheel based on the cmd_vel messages and transmit them to the
can-controller.

The components compare the real driven way (With calculations out of the
ticks from the incremental encoder) and the required driven way. If the
ways differ, an offset is being computed that compensates the
difference. So you can compensate errors if the two motors have
different speed properties.

You can also speed up the velocity of the motors if the desired velocity
isn't fast enough. But this can result in an inaccurate navigation.

This picture shows you how a differential drive robot drives, with
different wheel velocities (al and ar). If al > ar the robot drives a
curve to the right. If al = ar the robot drives straight.

![\|height="200",width="259"](attachment:differnenzial.jpg)

## Usage

### Needed Packages

[asr_mild_base_launch_files](asr_mild_base_launch_files) if you want to
start the node with the mild.launch files.

### Needed Software

libsdl1.2-dev

### Needed hardware

We used:

\- Dukenmotors Typ GR63x55 (<http://www.dunkermotoren.de>)

\- Maxon motorcontroller
([Motorcontroller_4QDC_ADS_50-10_168049.pdf](http://wiki.ros.org/asr_mild_base_driving?action=AttachFile&do=view&target=Motorcontroller_4QDC_ADS_50-10_168049.pdf))

\- They are all connected with a self made circuit board over a CAN-Bus.

![\|height="326",width="333"](attachment:Driving_components.jpg)

### Start system

Execute the following command on the computer with CAN and laserscann
connection (start driving and laserscanner):



```
roslaunch asr_mild_base_launch_files mild.launch
```

 OR

To only start the driving:



```
rosrun asr_mild_base_driving mild_base_driving
```

 If it starts succesfully, you will see this on
the console:



```
Can: Socket set successfully.
CanListener: Started successfully.
BaseController: Started successfully.
```



## ROS Nodes

### Subscribed Topics

cmd_vel (
[geometry_msgs/Twist](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html))

-   A stream of velocity commands from the move_base.

### Published Topics

odom (
[nav_msgs/Odometry](http://docs.ros.org/api/nav_msgs/html/msg/Odometry.html))

-   Odometry information that gives the navigation the current speed and
    the actual position of the robot.

### Parameters

Look at [asr_mild_base_launch_files](asr_mild_base_launch_files) on how
to adapt the parameters.

velocity (double)

-   Speeds up the motors with this factor.
