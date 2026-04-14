## Introduction

This package provides a hardware interface for ROS control. Its aim is
to allow generic software controllers to control a set of Dynamixel
actuators. ROS control is a framework to design software control loops
in ROS (Robot Operating System) where the controller code is decoupled
from the actual hardware. Dynamixel is a popular servo range for robots
with all-in-one module (reductor, PID controller, profil speed /
acceleration, encoder\...).

## Features

-   simple, ROS-style control interface for your dynamixel-based robot
-   not specific to a given number or set of actuators
-   position and velocity control
-   works with both version of Dynamixel protocol (1 and 2)
-   uses radians uniformly over all Dynamixel models (no need to worry
    about ticks-to-angle conversion)
-   you can set an offset for each actuator\'s position
-   set names for your dynamixels in a configuration file
-   joint limits

## Limitations

We are currently working on the following features:

-   add support for the more exotic control modes (including current and
    multi-turn)
-   it would be great to offer a service to reset one actuator after an
    overload error

## Installation and usage

[dynamixel_control_hw](https://github.com/resibots/dynamixel_control_hw)
depends on the [libdynamixel](https://github.com/resibots/libdynamixel)
library. Please install it, it\'s light and quick.

Then, you\'ll need to store the installation path of libdynamixel in the
\'\'\'LIBDYNAMIXEL\'\'\' environment variable.

Install the ros package ros_control. In apt-get, it is called
\`ros-YourDistro-ros-control\` (where \*YourDistro\* must be changed by
the ROS distribution\'s name, like indigo or jade).

Clone the \`dynamixel_control_hw\` repository in your catkin
workspace\'s source directory and run a \`catkin_make\`.

## Parameters

For sample configuration files, see the ones in \`config/\`. Here are
the accepted parameters.

```
{
#!clearsilver CS/NodeAPI
 param{
  0.name = ~serial_interface
  0.type = string
  0.default = auto
  0.desc = path to the USB to serial interface for example "/dev/ttyUSB0"
  1.name = ~baudrate
  1.type = int
  1.default = 0
  1.desc = baud-rate for the serial communication with actuators (in bauds)
  2.name = ~loop_frequency
  2.type = float
  2.default = 0.0
  2.desc = frequency at which the control loop will run (in Hz)
  3.name = ~cycle_time_error_threshold
  3.type = float
  3.default = 0.0
  3.desc = how much delay is tolerated on the control loop (in s)
  4.name = ~read_timeout
  4.type = float
  4.default = 0.0
  4.desc = timeout on the reception of replies from the servos (in s)
  5.name = ~servos
  5.type = Servo
  5.default = auto
  5.desc = object which keys are the name of the joints and which values contain
  6.name = ~id
  6.type = int
  6.default = 0
  6.desc = actuator's ID to its name (the one used in the controller list and in URDF)
  7.name = ~offset
  7.type = float
  7.default = 0.0
  7.desc = correction to be applied to the angle of the joint (in rad)
  8.name = ~command_interface
  8.type = string
  8.default = position
  8.desc = the command mode (velocity or position)
  9.name = ~max_speed
  9.type = float
  9.default = 0.0
  9.desc = maximal allowed velocity (rad/s)
  10.name = ~default_command_interface
  10.type = string
  10.default = position
  10.desc = if no 'command_interface' is defined for a joint, this value is used instead
}
```}

## Testing the hardware interface

If you want to use the sample launch files or to use one of the default
controllers, please install with apt-get:

\- \`ros-YourDistro-ros-controllers\` and -
\`ros-YourDistro-joint-state-publisher\`.

Have a look at the \`launch/sample.launch\` file. It will by default
launch two feed-forward only controllers (one position and one velocity)
and a virtual controller that publishes the states of the two actuators.

-   Before starting\* it, check \`config/sample.yaml\` for the \`id\`
    parameters, the \`serial_interface\` and \`baudrate\` settings. Once
    you are sure that it\'s correct, you can \`roslaunch
    dynamixel_control_hw sample.launch\`. By looking at the available
    topics, you should find two, for the commands the joints, and one
    for the joint state.

## Troubleshooting read time

If the reading time seems too long, check the value of the USB latency
timer. On ubuntu this value is retrieved with this command \`cat
/sys/bus/usb-serial/devices/ttyUSB0/latency_timer\`. It is the time, in
milliseconds, for which the device driver buffers data before making it
available.

You can change this timer with the command \`echo 4 \| sudo tee
/sys/bus/usb-serial/devices/ttyUSB0/latency_timer\` which sets it to 4
ms for the device \`/dev/ttyUSB0\`.

## Alternative software

If you know of an other software offering similar functionalities to
this one, feel free to open an issue so that we can add it here.

## Support and contact

This software is developed as part of the ResiBots project. We do our
best to keep it free of bug and to implement relevant features. Should
you face an issue or have a suggestion, please open an issue.

## Projects using this software

\- [ResiBots](https://www.resibots.eu/)

## License

Unless stated otherwise, the license for this repository is CeCILL-C
(see LICENSE and LICENSE.fr).

[ResiBots](https://www.resibots.eu/): <http://www.resibots.eu>
[libdynamixel](http://github.com/resibots/libdynamixel):
<http://github.com/resibots/libdynamixel> [ROS](http://www.ros.org/):
<http://www.ros.org/> [ROS control](http://wiki.ros.org/ros_control):
<http://wiki.ros.org/ros_control>
