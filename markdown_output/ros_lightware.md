This package provides a simple driver for the Lightware SF 10 altimeter.

-   Maintainer: Steven Waslander
-   Author: Timo Steihagen
-   License: BSD
-   Source: <https://github.com/WAVELaboratory/ros_lightware>
-   Dependency: Cereal port, a catkinized package is avaliable at
    <https://github.com/WAVELaboratory/cereal_port>

This package publishes a single custom message called sensor_data, which
includes altitude (range in m) and voltage . The update rate and serial
port parameters are hard coded in the single source file to the default
values for the sensor. The communication protocol is defined in
<https://www.parallax.com/sites/default/files/downloads/28051-28053-Lightware-SF10-Manual-Rev-6.pdf>.
