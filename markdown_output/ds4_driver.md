1.  keywords joystick, ps4, ds4, dualshock4

## Overview

This package provides a driver for the DualShock 4 (PS4) Bluetooth
controller. Some of the features of this package are:

-   Access to information such as IMU, battery, and touchpad
-   Access to feedback such as rumble, LED color, and LED flashing
-   Connection via Bluetooth for wireless control

## Installation and Usage

Pair and connect to your DualShock 4 by long-pressing the PS button and
Share button for up to 10 seconds until the LED starts flashing. Use
your system's Bluetooth settings to connect to the device.

This driver depends on `ds4drv`. Some features of this driver depend
on pull requests have not yet been merged upstream. Until they are
merged, use [the fork](https://github.com/naoki-mizuno/ds4drv) (devel
branch).

```console
$ git clone https://github.com/naoki-mizuno/ds4drv --branch devel
$ cd ds4drv
$ python2 setup.py install --prefix ~/.local
$ sudo cp udev/50-ds4drv.rules /etc/udev/rules.d/
$ sudo udevadm control --reload-rules
$ sudo udevadm trigger
$ cd ~/catkin_ws/src
$ git clone https://github.com/naoki-mizuno/ds4_driver.git
```

Compile and source this package just like any other ROS package. To run,

```console
$ roslaunch ds4_driver ds4_driver.launch
# Or
$ rosrun ds4_driver ds4_driver_node.py
```

### Disable touchpad input device

Note: You can skip this section if you use the forked version of
`ds4drv` (i.e. `naoki-mizuno/ds4drv`) because the following line is
included in the udev rules by default.

By default the touchpad of the DualShock 4 is recognized as an input
device. Because of this, the mouse moves to the location on screen that
corresponds to the location touched, making it very hard to track the
mouse cursor (and worse, it automatically clicks at that location). If
you want to prevent the touchpad from being recognized as an input
device, add the following to the udev rules and run the `udevadm`
commands (you will still be able to use the touchpad from this driver):

```
SUBSYSTEM=="input", ATTRS{name}=="*Wireless Controller Touchpad", RUN+="/bin/rm %E{DEVNAME}", ENV{ID_INPUT_JOYSTICK}=""
```

## Demonstration

Get a glimpse of some of the features of `ds4_driver` including
touchpad, rumble, and LED control:

```console
$ roslaunch ds4_driver demo.launch
```

Moving the left/right stick controls the rumble. Sliding left and right
on the touchpad while pressing circle, triangle, cross buttons controls
the brightness of the red, green, blue LED, respectively (you can tell
from the color of the button). Pressing the PS button triggers the
flashing of the LED.

## Nodes

```clearsilver
node.0 {
  name = ds4_driver_node.py
  desc = Driver for DualShock 4, which publishes the device's status and applies feedback to the device.

pub {
group.0 {
  0.name = status
  0.type = ds4_driver/Status
  0.desc = Publishes the current state of the device.
}
group.1 {
  name = When using ROS standard messages.
  desc = Topics published only when `~use_standard_msgs` is `true`
  0.name = raw_report
  0.type = ds4_driver/Report
  0.desc = Raw information sent from the device.
  0.name = battery
  0.type = sensor_msgs/BatteryState
  0.desc = Battery information such as percentage left.
  1.name = joy
  1.type = sensor_msgs/Joy
  1.desc = Joypad data.
  2.name = imu
  2.type = sensor_msgs/Imu
  2.desc = IMU data, where X points to the right, Y points up, and Z points towards the person holding the device.
}
}
sub {
group.0 {
  0.name = set_feedback
  0.type = ds4_driver/Feedback
  0.desc = Feedback for the device such as LED color, LED flashing, and rumble.
}
group.1 {
  name = When using ROS standard messages.
  desc = Topics subscribed to only when `~use_standard_msgs` is `true`
  0.name = set_feedback
  0.type = sensor_msgs/JoyFeedbackArray
  0.desc = Feedback for the device (only LED color and rumble).
}
}
param {
  0.name = ~device_addr
  0.type = string
  0.desc << EOS
Hardware address of the device to be connected to. If unspecified, the first device found will be used.
EOS
  1.name = ~backend
  1.type = string
  1.default = hidraw
  1.desc << EOS
Backend to be used to connect to the device via Bluetooth. `bluetooth` is only for legacy support and should not be used unless necessary. Refer to the docs of `ds4drv` for details.
EOS
  2.name = ~use_standard_msgs
  2.type = bool
  2.default = false
  2.desc << EOS
If `true`, uses ROS standard messages such as <<MsgLink(sensor_msgs/Joy)>>.
EOS
  3.name = ~deadzone
  3.type = float
  3.default = 0.1
  3.desc << EOS
Amount by which the joystick has to move before it is considered to be off-center.
EOS
  4.name = ~frame_id
  4.type = string
  4.default = ds4
  4.desc = Frame ID to be used for the messages.
  5.name = ~imu_frame_id
  5.type = string
  5.default = ds4_imu
  5.desc = Frame ID to be used for the IMU messages.
}
}

node.1 {
  name = ds4_twist_node.py
  desc = Subscribes to the device status messages and converts them to velocity commands.

pub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Velocity commands. Type is <<MsgLink(geometry_msgs/TwistStamped)>> if `~stamped` parameter is `true`.
}
sub {
  0.name = status
  0.type = ds4_driver/Status
  0.desc = Joypad state published from the driver.
}
param {
  0.name = ~stamped
  0.type = bool
  0.default = false
  0.desc << EOS
Whether to publish <<MsgLink(geometry_msgs/Twist)>> or <<MsgLink(geometry_msgs/TwistStamped)>> for the output velocity command. For robots such as [[http://wiki.ros.org/Robots/TurtleBot|TurtleBot]], [[http://wiki.ros.org/Robots/Husky|Husky]], and [[http://wiki.ros.org/Robots/PR2|PR2]], `/cmd_vel` is not stamped (i.e. <<MsgLink(geometry_msgs/Twist)>> is used) but stamped velocity commands may be required for some applications.
EOS
  1.name = ~inputs
  1.type = dict
  1.desc << EOS
What buttons and axes to use for the value of each velocity vector. Expressions can be used to combine values of multiple keys (see [[https://github.com/naoki-mizuno/ds4_driver/blob/master/config/twist_6dof.yaml|config/twist_6dof.yaml]] for examples).
EOS
  2.name = ~scales
  2.type = dict
  2.default = 1.0 for all fields
  2.desc << EOS
Scaling factor for each velocity vector.
EOS
}
}
```
