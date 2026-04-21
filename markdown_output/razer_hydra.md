-   Maintainer: [Adam Leeper](Adam Leeper)
-   License: BSD
-   Bugtracker: <https://github.com/ros-drivers/razer_hydra/issues>
-   Source: <https://github.com/ros-drivers/razer_hydra>

## Overview

<https://github.com/aleeper/razer_hydra_ros>

This package provides an unofficial, open-source driver for the Sixense
Razer Hydra Controller. The driver opens a connection to the device
using /dev/hidraw\*, a feature of Linux kernel 3.0.0+. A ROS node opens
the device and publishes custom messages with the state of the buttons,
joysticks, and 3D poses.

Please report bugs and request features on the github issue tracker:
<https://github.com/aleeper/razer_hydra_ros/issues>

## Supported Distributions

This package has been tested on Ubuntu Precise 12.04. Based on the
hidraw interface in use, it should also work with Ubuntu Oneiric 11.10;
verification would be appreciated.

## Bringup

Install the udev rules for the Razer Hydra by running the configure
script in the razer_hydra directory: ```
roscd razer_hydra
./configure_udev_rules
```

Then launch the device node:

```
roslaunch razer_hydra hydra.launch publish_tf:=true/false
```

You can check if things are working either by looking at the TF tree in
Rviz, or by doing: ```
rostopic echo /hydra_calib
```

## Frames and Offsets

The default frame location for the Razer Hydra (at least, as reported
raw over USB) seems to be far back along the paddles, behind where the
cord attaches to each paddle. This leads to un-intuitive motion.

To correct for this, two frames are computed from the transform reported
by the hydra driver, a "pivot" frame and a "grab" frame. Parameters
can be specified to define a translation to each frame from the raw
frame along the local coordinate axes. Another parameter specifies which
of the two frames should be used in the hydra messages.

An appropriate offset will be dependent on each user (e.g. size of hands
and how the paddles are held) as well as the interaction paradigm that
the hydra paddles represent and the resulting location of a virtual
center-of-rotation (e.g. imagining the paddles are at the wrist of a
long end-effector, vs. imagining that the point under the joystick is a
"grab point" for manipulating objects, etc.).

(Note: The existence of two frames is useful for debugging while looking
at the tf tree. Otherwise, it would be sufficient to just have a single
offset frame.)

## Filtering

The raw position data for the hydra is rather jittery. To overcome this,
a low-pass
[biquad filter](http://www.earlevel.com/main/2003/03/02/the-bilinear-z-transform/)
is used on position, and a low-pass
[one-pole filter](http://www.earlevel.com/main/2012/12/15/a-one-pole-filter/)
is used on the orientation.

The corner/cutoff frequency for the filters is specified at launch, with
a default value of 2.5 Hz. ```
roslaunch razer_hydra hydra.launch corner_hz:=2.5
```

## ROS API

```clearsilver
name = hydra
desc = Driver node for Razer Hydra controller.
pub {
  0.name = hydra_calib
  0.type = razer_hydra/Hydra
  0.desc = Publishes the state of each paddle (pose, joystick, and buttons) using ROS frame conventions.
  1.name = hydra_raw
  1.type = razer_hydra/HydraRaw
  1.desc = Publishes the raw values of position, quaternion, joystick, and buttons.
  2.name = hydra_joy
  2.type = sensor_msgs/Joy
  2.desc = Emulates a PS3 controller joystick message (version 0.0.6 and up)
}
param {
  0.name = ~device
  0.type = string
  0.default = /dev/hydra
  0.desc = The device to open. The default udev rules alias the hydra to /dev/hydra, so this will work by default.

  1.name = ~publish_tf
  1.type = bool
  1.default = `false`
  1.desc = By default only messages are published. If `true`, transforms will be published to tf between `hydra_base`, `hydra_<left/right>_pivot` and `hydra_<left/right>_grab`.

  2.name = ~polling_ms
  2.type = int
  2.default = 10
  2.desc = The max number of milliseconds to wait while polling for new data from the hydra device. Note that this does NOT set the sample rate; the sample rate is currently not controllable, and will always be 250 Hz.
  
  3.name = ~corner_hz
  3.type = double
  3.default = 2.5
  3.desc = Corner/cutoff frequency for low-pass filtering.

  4.name = ~use_grab_frame
  4.type = bool
  4.default = `false`
  4.desc = If `true`, uses the `grab_frame` in messages. Otherwise, uses the `pivot_frame`.

  5.name = ~px,py,pz
  5.type = double
  5.default = 0
  5.desc = The x,y,z components of a translation offset between what is reported by the low-level hydra driver and what is set as the `hydra_<left/right>_pivot` frame.

  6.name = ~gx,gy,gz
  6.type = double
  6.default = 0
  6.desc = The x,y,z components of a translation offset between what is reported by the low-level hydra driver and what is set as the `hydra_<left/right>_grab` frame.
}
```
