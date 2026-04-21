1.  keywords joystick, wiimote, wii

![A Wiimote\|align="right"](attachment:wiimoteOverview.jpg)

## API Stability

This package should be considered as **stable,** except for support of
the Classic controller, which requires additional testing.

## System Dependencies

The package depends on the third-party cwiid wiimote bluetooth
interface. With permission of the author, Donnie Smith, cwiid is
distributed as the ROS package `cwiid`. **NOTE:** The cwiid library
currently only recognizes Wiimotes which report the name as "Nintendo
RVL-CNT-01"; the latest Wiimotes will not be discovered. See
<http://wiibrew.org/wiki/Wiimote#SDP_information>.

Python needs to be installed on your system. This package has been
tested under Python 2.5.2 and 2.6.5.

## Installing the wiimote Package

Check out the wiimote package, and `rosmake` to ready the package for
operation. Plug the Bluetooth dongle into your machine's USB port.

If you have the Motion+ Wiimote attachment, plug it into the bottom of
your Wiimote device.

Make sure your Wiimote's batteries are charged.

## Nodes



```clearsilver
node {
0{
name = wiimote_node.py
desc = `wiimote_node.py` publishes Wiimote sensor data and allows ROS clients to control LED and Rumble.
sub {
0{
name= set_feedback
type= sensor_msgs/JoyFeedbackArray
desc= Topic where ROS clients control the Wiimote's leds and rumble (vibrator) facility.
}
}
pub {
0{
name= joy
type= joy/Joy
desc= Topic on which Wiimote accelerometer, gyro, and button data are published. Axes are: linear AccelerationX/Y/Z, followed by angular velocityX/Y/Z (a.k.a. Roll, Pitch, Yaw, a.k.a. Phi, Theta, Psi). The values are corrected to be near zero at rest. For raw values, use the [[#wiimoteMsgSec|State message]]. The Wiimote buttons are reported in the same order as in the State message ([[#buttonAssignments|see below]]).  
}
1{
name= imu/data
type= sensor_msgs/Imu
desc= Topic on which Wiimote gyro and accelerometer data are sent out.
}
2{
name= wiimote/state
type= wiimote/State
desc= Topic for comprehensive information about Wiimote state.
}
3{
name= wiimote/nunchuk
type= joy/Joy
desc= Topic on which data from an attached Nunchuk are sent out, including the joystick, accelerometer and button data. Axes are: Joystick X/Y, Acceleration X/Y/Z. The buttons are Z then C. Note the spelling of the topic name does not include a 'c'. 
}
4{
name= wiimote/classic
type= joy/Joy
desc= Topic on which data for a Wiimote classic attachment are sent out (Untested by Willow Garage). 
}
5{
name= imu/is_calibrated
type= std_msgs/Bool
desc= Latched topic for learning the most recent Wiimote calibration result.
}
}
srv{
0{
name= imu/calibrate
type= std_srvs/Empty
desc= Service to request that the Wiimote be re-calibrated.
}

}
```



## The State Message

The `State` message communicates all data that is available from your
Wiimote device. Samples are taken and broadcast at 100Hz. Here are
comments on some of the fields:

The message header's time `stamp` is set to reflect the time when the
respective message's sample was taken from the Wiimote device.

The `angular_velocity_zeroed` shows the Motion+ gyroscope reading.
These values are valid only if the Motion+ attachment is plugged into
the Wiimote. Else they are held at constant zero, and matrix entry
\[0,0\] in message field angular_velocity_covariance is set to -1.

The gyro reading is corrected by the zero-motion bias of the gyro. This
bias was determined during the initial pairing/calibration process. The
`angular_velocity_raw` is the uncorrected, raw gyro reading.

It is safe to remove the Motion+ from the Wiimote device while the
wiimote node is running. However, plugging the appendage back in will
not resume readings. You will need to stop and restart the Wiimote node.

The accelerometer readings are shown analogously to the gyro readings.
However, the accelerometer bias is not obtained through observation
during calibration, but is read from the Wiimote. The devices come with
this information factory installed. The `buttons` array shows which
buttons are currently depressed on the Wiimtoe device. The position
mapping is as follows: 

```
Position   Button Name
0         1
1         2
2         A
3         B (toggle button on back of device)
4         Plus
5         Minus
6         Rocker Left
7         Rocker Right
8         Rocker Up
9         Rocker Down
10        HOME
```

 LED and Rumble
(vibrator) states are simple Booleans.

The `ir_tracking` are four sets of x/y/\[z\], and size measures, for
the four infrared light sources that the Wiimote device can track. When
no lights are detected, the respective values are set to -1. The z axis
is always -1, as it is not measured.

The `ir_sizes` array are four intensity measures of the lights that
the camera observes. The meaning of these measures are unclear to the
author.

The `raw_battery` entry is the battery charge reading. The unit of
this number is unclear. Field `percent_battery` returns the remaining
charge as a percentage of full charge.

The `zeroing_time` is the time of the most recent device calibration.

The `errors` field is currently not used.
