## Overview

This package contains the firmware source files for the
ros_arduino_bridge controller. It requires version 1.0 or higher of the
Arduino IDE.

The firmware can be found in the ROSArduinoBridge directory under
src/libraries. At the moment, the following hardware configurations are
supported:

-   [Pololu VNH5019 dual motor shield](http://www.pololu.com/catalog/product/2502)
-   [Pololu MC33926 dual motor shield](http://www.pololu.com/catalog/product/2502=3)
-   [Robogaia Mega Encoder shield](http://www.robogaia.com/two-axis-encoder-counter-mega-shield-version-2.html)

If you don\'t have the hardware required for base control, you can still
use the library and the rest of the ROS Arduino packages for reading
sensors and controlling PWM servos by undefining the USE_BASE macro in
the source. See the README on the GitHub repository for a more detailed
[installation and configuration guide](https://github.com/hbrobotics/ros_arduino_bridge/blob/master/README.md).

## Report a Bug

<https://github.com/hbrobotics/ros_arduino_bridge/issues>
