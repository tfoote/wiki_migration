1.  keywords joystick, ps3

## Overview

This package provides a driver for the PS3 (SIXAXIS or DUALSHOCK3)
bluetooth joystick. This joystick is currently used with the PR2 robot.

This driver exists because Linux's native support for the PS3 joystick
is unreliable, and does not give access to the joystick's
accelerometers and gyroscope. This driver solves both problems. However
in its current form, **this driver will not coexist with any other
bluetooth device**. In future releases, we plan to allow first non-HID
and later any bluetooth device to coexist with this driver. If you have
a need for such functionality, let it be known.

It has been observed that coexistence is possible, at least in the two
following cases:

-   Non-HID devices using a userland driver, such as one written using
    pybluez.
-   Keyboards or mice running in HID proxy mode, which appear to the
    kernel as USB devices.

## Hardware Support

This driver may only work with Bluetooth 2.0 adapters.

In our experience, the driver works with most 2.x Bluetooth adapters.
Please report other incompatible Bluetooth adapters to the issue tracker
(you can find the link in the beginning of the page).

Adapters that are known not to work:

-   Linksys USBBT100 version 2 (Bluetooth 1.1).
-   USB device 0a12:0x0001

## Supported Distributions

`ps3joy.py` is known to work with Ubuntu 12.10, Ubuntu 12.04, Ubuntu
Jaunty 9.04, and Ubuntu Hardy 8.04. To make it work with Ubuntu Karmic
9.10, you will have to follow these
[instructions](ps3joy/KarmicInstructions).

Sixpair runs on all platforms that have been tested.

## API Stability

We do not anticipate any incompatible changes to the API of this
package. With maturing support for the PS3 joystick in BlueZ and the
Linux kernel, we hope that most people will no longer need this package
unless they want to use the gyroscope and accelerometer axes.

## Getting Started

The
[How to Pair the PS3 Joystick with a Bluetooth Dongle](ps3joy/Tutorials/PairingJoystickAndBluetoothDongle)
is a good starting point for how to use this package.

### Install

Install from source (see repo link above) or from repository:
```
sudo apt-get install ros-%ROSDISTRO%-joystick-drivers
sudo apt-get install ros-indigo-joystick-drivers       (ROS Indigo for example)
```

## ROS API

```clearsilver
name = ps3joy.py
desc = Joystick driver for the PS3 Joystick. Plain Python without any ROS-references, needed to be easily started with `sudo`, which is the easiest way to grant it permissions to access bluetooth hardware.
``` ```clearsilver
name = ps3joy_node.py
desc = Joystick driver for the PS3 Joystick, which is also a ROS node to publish diagnostics and receive controller feedback messages.
sub {
  0.name = joy/set_feedback
  0.type = sensor_msgs/JoyFeedbackArray
  0.desc = Set the rumble and leds of the joystick. The PS3 has 4 leds (ids:0-3) and two rumblers (ids:0-1). The high frequency rumbler is id 1 and the low frequency rumbler is id 0. 
}
pub {
  0.name = /diagnostics
  0.type = diagnostic_msgs/DiagnosticArray
  0.desc = Publishes the battery status, charging status, connection.
}
```

## Command-Line Options

This is the same for `ps3joy.py` and `ps3joy_node.py`.
```
$ ./ps3joy.py --help
usage: ps3joy.py [--inactivity-timeout=<n>] [--no-disable-bluetoothd] [--redirect-output]=<f>
<n>: inactivity timeout in seconds (saves battery life).
<f>: file name to redirect output to.
Unless --no-disable-bluetoothd is specified, bluetoothd will be stopped.
```

`\--inactivity-timeout` Turn off the joystick after a certain period
of inactivity. This is useful to save batteries and reduce contention on
the 2.4 GHz network.

`\--no-disable-bluetoothd` Tells `ps3joy.py` not to take down
bluetoothd. For this option to work, bluetoothd must be configured not
handle input devices, otherwise you will get an "Error binding to
socket" error message. (New in 1.1.1 and 1.0.3)

`\--redirect-output` Allows the standard output and error to be
redirected to a file. This is useful when `ps3joy.py` is run in the
background. (New in 1.1.1 and 1.0.3)

`\--continuous-output` Output continuous motion sensor streams, and as
a side effect of continuous output, no longer leaves long periods of no
messages on the /joy topic.

## Specifics for ps3joy_node

### Launching with permissions

Starting the ROS node variant of ps3joy is somewhat tricky. It needs
higher permissions to access bluetooth hardware, which can be achieved
via sudo, but running ROS code as sudo is neither recommended nor
trivial. Here is what you can do: ```
.../ps3joy$ sudo bash -c "source /home/myself/.bashrc; ./scripts/ps3joy_node.py --inactivity-timeout=300"
```

Or you could write a sudo script for sourcing ROS and starting
ps3joy_node; I use
[ps3joy_node_starter.sh](https://gist.github.com/felix-kolbe/8419903) to
automatically start the `ps3joy_node` after booting and a ROS-check.

### Sending feedback to the controller

To set the led or rumble from the command line: ```
rostopic pub  /joy/set_feedback sensor_msgs/JoyFeedbackArray '[ [0, 3, 1], [1, 1, 0.8] ]'
```
There is
[real world code sending feedback](https://github.com/felix-kolbe/uashh-rvl-ros-pkg/blob/master/teleop_ps3/src/teleop_ps3.cpp#L334).

## PS3 Joystick Buttons and Axes

![](attachment:ps3_buttons.jpg) ![](attachment:ps3_buttons_front.jpg)
![](attachment:ps3_axes.jpg)

Buttons 4-15 are reported as axes as well as buttons. The axis
corresponding to a button can be used to determine how hard the user is
pressing on the button, ranging from 0 when there is no press, to -1 for
a hard press. For these buttons, the axis number is the same as the
button number.

**ps3joy.py** also exposes the joystick's three-axis accelerometer and
the single-axis gyroscope:

  -- ---------- -- ---------------------------------------- --
     **Axis**      **Description**                          
     16            Right-Left (positive is left)            
     17            Forward-Backward (positive is forward)   
     18            Up-Down (positive is up)                 
     19            Yaw axis (positive is clockwise)         
  -- ---------- -- ---------------------------------------- --

### Button number macros for C++

With these #defines you can access the PS3 buttons within the
[sensor_msgs/Joy message published by the joy_node](joy#Published_Topics)
without worrying about magic numbers:

```
// note on plain values:
// buttons are either 0 or 1
// button axes go from 0 to -1
// stick axes go from 0 to +/-1

#define PS3_BUTTON_SELECT            0
#define PS3_BUTTON_STICK_LEFT        1
#define PS3_BUTTON_STICK_RIGHT       2
#define PS3_BUTTON_START             3
#define PS3_BUTTON_CROSS_UP          4
#define PS3_BUTTON_CROSS_RIGHT       5
#define PS3_BUTTON_CROSS_DOWN        6
#define PS3_BUTTON_CROSS_LEFT        7
#define PS3_BUTTON_REAR_LEFT_2       8
#define PS3_BUTTON_REAR_RIGHT_2      9
#define PS3_BUTTON_REAR_LEFT_1       10
#define PS3_BUTTON_REAR_RIGHT_1      11
#define PS3_BUTTON_ACTION_TRIANGLE   12
#define PS3_BUTTON_ACTION_CIRCLE     13
#define PS3_BUTTON_ACTION_CROSS      14
#define PS3_BUTTON_ACTION_SQUARE     15
#define PS3_BUTTON_PAIRING           16

#define PS3_AXIS_STICK_LEFT_LEFTWARDS    0
#define PS3_AXIS_STICK_LEFT_UPWARDS      1
#define PS3_AXIS_STICK_RIGHT_LEFTWARDS   2
#define PS3_AXIS_STICK_RIGHT_UPWARDS     3
#define PS3_AXIS_BUTTON_CROSS_UP         4
#define PS3_AXIS_BUTTON_CROSS_RIGHT      5
#define PS3_AXIS_BUTTON_CROSS_DOWN       6
#define PS3_AXIS_BUTTON_CROSS_LEFT       7
#define PS3_AXIS_BUTTON_REAR_LEFT_2      8
#define PS3_AXIS_BUTTON_REAR_RIGHT_2     9
#define PS3_AXIS_BUTTON_REAR_LEFT_1      10
#define PS3_AXIS_BUTTON_REAR_RIGHT_1     11
#define PS3_AXIS_BUTTON_ACTION_TRIANGLE  12
#define PS3_AXIS_BUTTON_ACTION_CIRCLE    13
#define PS3_AXIS_BUTTON_ACTION_CROSS     14
#define PS3_AXIS_BUTTON_ACTION_SQUARE    15
#define PS3_AXIS_ACCELEROMETER_LEFT      16
#define PS3_AXIS_ACCELEROMETER_FORWARD   17
#define PS3_AXIS_ACCELEROMETER_UP        18
#define PS3_AXIS_GYRO_YAW                19
```
