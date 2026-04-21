## Overview

This package contains the RFlex driver and drivers for specific robots
derived from it. The drivers are designed to be standalone drivers, not
integrated into the ROS framework (with the exception of a few data
structures that are convenient to use). The ROS integration is contained
in separate classes which define the nodes.

The RFlex driver provides a means of controlling and getting data from
six different subsystems.

-   **Motor** - Controls position, brake and reads odometry
-   **Sonar** - Controls the different sets of sonar sensors
-   **IR** - Infared sensors
-   **Digitial IO** - Varies per robot\...possibly bump sensors
-   **Joystick** - For use with external joysticks that plug directly
    into the robot
-   **System** - Monitors things like battery status

The RFlex driver takes care of all of the input/output to the device and
packet parsing. It saves the input to the protected variables. This
allows the driver to be extended into a new class which interprets the
raw data values.

## Drivers

Below is a list of the current robot drivers. Currently the only
implemented drivers that extends the RFlex driver are the B21 driver and
the beginnings of a ATRVJr driver.

-   [ B21](rflex/B21 )
-   [ ATRV Jr.](rflex/ATRVJr )
