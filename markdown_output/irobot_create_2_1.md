## The Brown ROS Create Driver

### Dependencies

The only external dependency of the driver is
[ python-serial](http://pyserial.sourceforge.net/).

### Making

Provided the external dependencies are satisfied:



```
rosmake irobot_create_2_1
```



should work properly.

### Running

In its own terminal you will need to run roscore:



```
roscore
```



You can then run the create driver via:



```
rosrun irobot_create_2_1 driver.py
```



The node will assume the robot is attached to `/dev/ttyUSB0` if it is
not:



```
rosparam set /brown/irobot_create_2_1/port PORT
```



or an equivalent should be executed prior to running the driver, where
PORT is the port to which the robot is actually attached.

Additionally, you can check ROS/Create functionality by running:



```
rosrun irobot_create_2_1 bumpGo.py
```



*while* also running the driver. This will run a primitive bump and go
program using the ROS driver.
[bumpGo.py](http://code.google.com/p/brown-ros-pkg/source/browse/trunk/unstable/irobot_create_2_1/bin/bumpGo.py?spec=svn353&r=353 )
is a good place for new ROS users to get started with writing Brown ROS
driver based programs.

### Messages and Services

The ROS driver provides the following services:

-   Brake: takes in a single boolean. When the boolean is true (e.g. 1),
    stops the robot.

```{=html}
<!-- -->
```
-   Circle: takes in three parameters: clear (a boolean), speed, and
    radius. speed sets the forward speed in mm/s from -500 to 500 mm/s
    (negative speeds move the robot backwards). radius is used to set
    the radius of the circle in mm that the robot will move along.

```{=html}
<!-- -->
```
-   Demo: takes in a number and puts the robot into the equivalent demo
    mode (see the Open Interface documentation from iRobot). Requesting
    demo mode 255 will stop whatever demo is currently running.

```{=html}
<!-- -->
```
-   Leds: takes in four parameters. advance (a boolean), which it then
    sets the advance Led to (true is on). play (again a boolean), which
    it then sets the play Led to. color a number between 0-255. The
    power Led can vary in color between pure green (0) and pure red
    (255). color is used to set this color. Finally intensity is the
    parameter used to set the brightness of the power led from off (0)
    to full on (255).

```{=html}
<!-- -->
```
-   Tank: takes in three parameters: clear (a boolean), left, and right.
    left and right are used to set the left and right wheel velocities
    respectively. They can vary between -500 and 500 and are interpreted
    as mm/s with negative velocities moving backward.

```{=html}
<!-- -->
```
-   Turn: takes in two parameters: clear (a boolean), and turn. turn is
    a velocity in mm/s. Positive velocities turn the robot in place
    clockwise. Negative velocities turn the robot in place
    counter-clockwise.

Unless otherwise stated, all of these services return a boolean
indicating whether the service call was successful or not.

The driver publishes a single message type, which exports all of the
robot's sensory information:



```
Header header
bool wheeldropCaster
bool wheeldropLeft
bool wheeldropRight
bool bumpLeft
bool bumpRight
bool wall
bool cliffLeft
bool cliffFronLeft
bool cliffFrontRight
bool cliffRight
bool virtualWall
uint8 infraredByte
bool advance
bool play
int16 distance
int16 angle
uint8 chargingState
uint16 voltage
int16 current
int8 batteryTemperature
uint16 batteryCharge
uint16 batteryCapacity
uint16 wallSignal
uint16 cliffLeftSignal
uint16 cliffFrontLeftSignal
uint16 cliffFrontRightSignal
uint16 cliffRightSignal
bool homeBase
bool internalCharger
uint8 songNumber
uint8 songPlaying
```



All of the fields within the message (with the exception of the header)
are equivalent to sensor packets available within the iRobot Create Open
Interface. For details about the meaning of the packets, see the iRobot
Open Interface documentation.

Some of the services accept a clear parameter. When asserted, along with
having the desired motion effect the service call will also reset the
current distance and angle tracking.
