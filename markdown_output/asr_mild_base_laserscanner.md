![\|width="333",height="200"](attachment:Logo-white-medium.jpg)

## Description

ROS-Node that starts the SICK PLS 101-312 laserscanner and publishes its
laserscan data.

## Functionality

The main class is sick.cpp. It contains the SICK configuration and
starts the code which communicates with the SICK. Also, it publishes the
scan data to ROS. All other code is based on the
[sicktoolbox](http://wiki.ros.org/sicktoolbox) . The toolbox also
contains code for other SICK laserscanners.

The "SickPLS.cc" class contains all methods you need. It also contains
many methods to get information from the SICK, e.g. resolution.

## Usage

For a successful laserscan you only need to connect the SICK PLS 101-312
laserscanner to your PC. You can use USB or a Serial interface. For a
baudrate of 500k you need USB or a RS422 Serial port and cable. To
establish a connection, you must adapt the name of the connected port
(look at parameter "serial"). Then you only need to start a launchfile
with the laserscanner node e.g.
[asr_mild_base_launch_files](asr_mild_base_launch_files).

Two example scans in RVIZ. The used SICK PLS 101-312 has a little noise
in its scans which you can see in the right image.

![\|width="333",height="254"](attachment:Laserscann_1.jpg)
![\|width="333",height="250"](attachment:Laserscann_2.jpg)

### Needed Packages

[asr_mild_base_launch_files](asr_mild_base_launch_files) if you want to
start the node with the mild.launch file.

### Needed hardware

SICK PLS 101 312 connected with serial or USB. Serial 422b is needed for
a 500k baudrate.

![\|width="333",height="352"](attachment:3646.jpg)

### Start system

Execute the following command on the computer with CAN and laserscan
connection (start driving and laserscanner):

```
roslaunch asr_mild_base_launch_files mild.launch
``` OR

Start only the laserscanner:

```
rosrun mild_base_laserscanner mild_base_laserscanner
``` Wait until the following is shown (this can
take 1-2 minutes):

```
Init. complete: Sick PLS is online and ready!
tScan Angle: 180
tScan Resolution: 0.5
tMeasuring Units: cm
``` It can take several tries to connect to the
laserscanner!

## ROS Nodes

### Published Topics

_/scan_ (
[sensor_msgs/LaserScan.msg](http://docs.ros.org/api/sensor_msgs/html/msg/LaserScan.html)*)*

Includes an array of all scanned points of one iteration with its
distance information.

### Parameters

Look at [asr_mild_base_launch_files](asr_mild_base_launch_files) on how
to adapt the parameters.

topic (string)

-   the topic name where the scans are published on. Usually "/scan".

serial (String)

-   Path to the port, e.g. "/dev/rs422b" for a serial RS422b device
    connection.

init_attempts (int)

-   How often the package should try to connect to the laserscanner
    until it stops trying.

baudrate (int)

-   Set the baudrate of the scanner. Allowed parameters are: 9600,
    19200, 38400, 500000. A baudrate of 38400 means 4 complete measures
    in 1 second.
