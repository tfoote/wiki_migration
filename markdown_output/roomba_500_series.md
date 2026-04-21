## The Roomba Robot

The roomba_500_series package was developed on top of the iRobot Open
Interface Specification. The 500 series Roombas communicate over the
same protocol that the popular iRobot Creates do, however the same
protocol (although similar) is not shared with the older 400 series
Roombas. This package was fully tested on the models 530, 555 and 560.

![](attachment:Roomba560_Roomba530_TopView.jpg)

The Roomba is a very interesting and robust platform for mobile robot
research. Although its performance is not comparable to that of a robot
designed with research in mind, the extremely low price is a compelling
argument.

### Sensors

The Roomba comes equipped with the following sensors:

-   2 bumpers up front;
-   6 IR bumpers up front;
-   4 cliff IR sensors;
-   Left, right and omni directional IR data receivers;
-   Various buttons.

### Actuators

The Roomba has the following actuators:

-   Left and right wheel motors;
-   Main and side brush motors and vacuum motor;
-   Rudimentary music playback.
-   Various lights.

### Accessories

Most Roomba models ship with the following accessories:

-   Docking station;
-   Virtual wall/beacon.

## ROS API

### Action API

The
[go_dock](http://www.ros.org/doc/api/roomba_500_series/html/classGoDock.html)
library present on the `roomba560_node` and `godock_server` nodes
provides an implementation of the !GoDockAction (see
[ actionlib documentation](actionlib )), that automatically docks the
Roomba. The !GoDockAction is still experimental, it still needs a lot of
work until it can be considered stable.

#### Action Subscribed Topics



```clearsilver
sub {
no_header= True
0.name= godock/goal
0.type= roomba_500_series/GoDockActionGoal
0.desc= Goal is empty for the `go_dock` action.
1.name= battery
1.type= roomba_500_series/Battery
1.desc= Battery status to know if the robot is docked.
2.name= ir_character
2.type= roomba_500_series/IRCharacter
2.desc= Data from the Roomba IR receivers, left right and omni directional, to guide the Roomba to the dock.
}
```



#### Action Published Topics



```clearsilver
pub {
no_header= True
0.name= godock/result
0.type= roomba_500_series/GoDockActionResult
0.desc= Result is empty for the `go_dock` action.
1.name= cmd_vel
1.type= geometry_msgs/Twist
1.desc= Velocity commands to the robot.
}
```





```clearsilver
node.0 {
name=roomba500_light_node
desc=`roomba500_light_node` is a driver for any Roomba from the 500 series. It solely subscribes to velocity commands and publishes the robot's odometry.
sub{
0.name= cmd_vel
0.type= geometry_msgs/Twist
0.desc= Velocity commands to the robot.
}
pub{
0.name= odom
0.type= nav_msgs/Odometry
0.desc= Odometry readings from the robot.
}
param {
0.name= roomba/port
0.default= /dev/ttyUSB0
0.type= string
0.desc= The serial port where the Roomba can be found.
}
}
node.1 {
name=roomba560_node
desc=`roomba560_node` is a driver for the Roomba 555 and 560. It exposes all the functionalities that these models have to offer. This node includes the !GoDockAction.
sub{
0.name= cmd_vel
0.type= geometry_msgs/Twist
0.desc= Velocity commands to the robot.
1.name= leds
1.type= roomba_500_series/Leds
1.desc= Various Leds on the Roomba.
2.name= digit_leds
2.type= roomba_500_series/DigitLeds
2.desc= The digit Leds on the Roomba (clock).
3.name= song
3.type= roomba_500_series/Song
3.desc= Store a song on the Roomba.
4.name= play_song
4.type= roomba_500_series/PlaySong
4.desc= Play a song on the Roomba.
}
pub{
0.name= odom
0.type= nav_msgs/Odometry
0.desc= Odometry readings from the robot.
1.name= battery
1.type= roomba_500_series/Battery
1.desc= Battery status.
2.name= bumper
2.type= roomba_500_series/Bumper
2.desc= Left and right bumper readings
3.name= buttons
3.type= roomba_500_series/Buttons
3.desc= Status of the various buttons on the Roomba.
4.name= cliff
4.type= roomba_500_series/RoombaIR
4.desc= Cliff sensor readings
5.name= ir_bumper
5.type= roomba_500_series/RoombaIR
5.desc= Readings from the array of six IR sensors on the front of the Roomba.
6.name= ir_character
6.type= roomba_500_series/IRCharacter
6.desc= Data from the Roomba IR receivers, left right and omni directional.
7.name= wheel_drop
7.type= roomba_500_series/WheelDrop
7.desc= Wheel drop sensor readings.
}
param {
0.name= roomba/port
0.default= /dev/ttyUSB0
0.type= string
0.desc= The serial port where the Roomba can be found.
}
}
node.2 {
name=godock_server
desc=`godock_server` is a wrapper node for the !GoDockAction created for testing and debugging.
}
node.3 {
name=godock_client
desc=`godock_client` is a client implementation for the !GoDockAction created for testing and debugging.
}
```



## Custom Nodes

The iRobot Open Interface protocol for the 500 series Roomba is also
available as a library on the [roomba_500_series](roomba_500_series)
package. This can be used to make custom nodes with any desired
combination of Roomba features. To start your own node check the
[Code API](http://www.ros.org/doc/api/roomba_500_series/html/) page.

## Tutorials

Coming soon\...

## iRobot Open Interface Specification

The iRobot Open Interface Specification document used for developing
this package can be found
[here](http://www.irobot.lv/uploaded_files/File/iRobot_Roomba_500_Open_Interface_Spec.pdf).
