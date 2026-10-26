The um7 package provides a ROS driver node for the CH Robotics UM7
Orientation sensor (IMU). It communicates with the UM7 over its serial
bus, converts the data to ROS standards, and publishes the data on
standard ROS topics.

The sensor hardware includes 3 axis angular rate, acceleration and
magnetometer data. It has a built-in Extended Kalman Filter (EKF) which
generates orientation data for all three axes in both Quaternion and
Euler form. It also provides a sensor temperature reading.

The UM7 is available directly from chrobotics.com or from other sellers,
e.g. pololu.com. It is available in two forms: the UM7-LT which is an
unenclosed circuit board and the UM7 which provides an enclosure. This
driver supports both.

CH Robotics also provides "CHRobotics Serial Interface" software which
allows complete configuration of the sensor, testing capability and
Calibration for the magnetometer. This software runs on Windows.

# Installation:

## Hardware Installation:

The sensor should be mounted on the vehicle in the default configuration
if possible (see below). If you don't, you will have to perform
transforms of the data in your applications to restore the proper
orientation of the readings.

The sensor should be mounted parallel to the Earth with the component
side pointed up. To optimize performance, you can shim the sensor
mounting so that the X and Y acceleration signals are zero when the
vehicle is level. To minimize cross-coupling between the X and Y axis,
the sensor should be pointed in the direction of normal forward movement
of the vehicle as accurately as practical. (see pictures below)

To optimize magnetometer data, the sensor should be located as far as
practical from iron parts on the vehicle, from electrical motors and
from high current power wires. Suitable places on the vehicle can be
found by using a hand-held compass. With power on the vehicle, verify
that the compass heading in the proposed location is close to the
heading of the compass when held far from the vehicle and any sources of
magnetic distortion. Retest with any electric motors running.

A magnetometer calibration procedure is provided by the CHRobotics
Serial Interface software. Unfortunately, no directions for this
procedure are in the UM7 documentation. Procedures for the predecessor
device, the UM6, can be found at:
www.chrobotics.com/docs/AN-1003-GettingStartedUM6.pdf and will work with
minor adaptations.

![\|align="center",width="611"](attachment:orientB.jpg)

testing

## Software Installation:

. um7 is released for indigo, but should work under hydro and may work
in later versions.



```
sudo apt-get install ros-$ROS_DISTRO-um7
```

 Run the driver:

. **note**: replace "ttyUSB0" below with the port number of your UM7
device. See /dev



```
rosrun um7 um7_driver _port:=/dev/ttyUSB0
```

 **Note:** the "port" assignment actually
defaults to "/dev/ttyUSB0", so if your sensor is on that port, the
parameter setting shown above is unnecessary.

**Note:** if you get a "Couldn't find executable named um7_driver
below /opt/ros/\$ROS_DISTRO/share/um7" message, try restarting linux. I
don't know why; but it has happened to me a couple times. It should
only happen on the first attempt to run.

## Nodes

### um7_driver

#### imu/data (sensor_msgs/Imu)

. Filtered orientation, accelerations and angular rotations: .
orientation is specified as a quaternion. It is only available if
quat_mode is selected (default). 3 axis angular rotations are specified
in radians/second. 3 axis accelerations are specified in
meters/second/second.

. Note: each of these has a covariance matrix in the topic format. The
UM7 does not supply covariance data so these matrices are set to all
zeros, meaning "data unknown". A parameter (below) is available to set
covariance of the quaternion data to alternate fixed values if you need
to do so.

#### imu/mag (geometry_mags/Vector3Stamped)

. Filtered magnetometer data from sensor. . provided as 3D orientation
in X,Y,Z.

#### imu/rpy (geometry_msgs/Vector3Stamped)

. Roll, Pitch and Yaw angles for sensed orientation: . angles are
specified in radians.

#### imu/temperature (std_msgs/Float32)

. temperature of sensor device in degrees centigrade.

**Note:** To clarify data polarities, I will describe them in terms of
aircraft motion. NU/ND is aircraft nose up (as in climbing or nose down
as in descent. RWD/LWD is right wing down as in an aircraft turning to
the right in flight; left wing down to turn to the left. NR/NL is nose
right as if the aircraft is turning right on the ground, and nose left
for turn to the left.

angular rotation about the X axis (roll) is positive for RWD. rotation
about the Y axis (pitch) is positive for ND. Rotation about the Z axis
(yaw) is positive for NL.

Angular positions are the same polarities as angular rate. ND is
positive, RWD is positive and NL is positive:

Acceleration in the X axis is positive for acceleration in the forward
direction. Acceleration in the Y axis is positive for acceleration to
the left Acceleration in the Z axis is positive for acceleration in the
upward direction.

### Parameters:

. Note: The full set of sensor parameters comes as a factory
configuration. They can all be modified with the CHRobotics Serial
Interface software. However the um7_driver has a default configuration
which sets the transmission rate of all the parameters to 20 hz and the
baud rate of the sensor to 115200. . . Note: Be aware that while all
these are "private" parameters, they are stored on the parameter
server. Any parameters you set to a non-default condition will be used
again the next time you restart um7_driver unless you specifically set
them back to the default. . . . **port(string, default: /dev/ttyUSB0)**
. Serial device to connect to. .

- **baud (int, default: 115200)** . baud rate that sensor is set to.
  Currently, default configuration above sets the sensor to 115200. .
  - frame_id(string, default: imu_link) **. frame_id placed in the
    header of the data, mag, and rpy messages .** mag_updates(bool,
    default: true) **. include magnetometer data in the pose estimate.
    This causes the yaw parameter to track to magnetic heading but with
    a long filter time constant. Otherwise, the yaw value will tend to
    drift slowly but continuously.** quat_mode(bool, default: true) **.
    This sets the EKF in quaternion mode where it generates the
    quaternion data necessary for the orientation data in the imu/data
    message. If not true, the orientation data will read 0,0,0,1 (all 0
    degree attitudes)** zero_gyros(bool, default: true) **. If true, the
    um7_driver will send a zero_gyros command to the sensor at driver
    startup. This command causes the sensor to average gyro readings
    over about 1 second to determine the null value of the gyros. The
    vehicle must be stationary during this command.** covariance(string,
    default: "0 0 0 0 0 0 0 0 0") **. The UM7 sensor does not provide
    covariance data so the default imu/data values are set to all zero
    indicating unknown data. However, some ROS applications may require
    covariance data for the orientation data. This parameter allows you
    to specify a string of fixed floating point values (separated by
    spaces) suitable for your needs.**

### Commands:

. The um7_driver provides three commands which can be sent to the
sensor. These commands are sent with the Reset service. The command
message is: . Reset.srv . bool zero_gyros . bool reset_ekf . bool
set_mag_ref . **zero_gyros** . if true, causes the sensor to recalculate
the angular gyro nulls. The robot must be stationary when this command
is issued and remain so for at least a second. **reset_ekf** . if true,
causes the Extended Kalman Filter to restart. **set_mag_ref** . if true,
causes the EKF (if the mag_updates parameter is set) to change its
magnetic heading reference from zero degrees to whatever the current
value of magnetic heading happens to be. This change will ramp in over a
5 or 10 second (roughly) time constant.
