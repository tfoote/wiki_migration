## Overview

This package contains the driver for the etherCAT Hand. It uses the
[pr2_etherCAT](pr2_etherCAT) which is running the main loop at 1kHz for
sending and receiving packets to/from the etherCAT. We also load the
[pr2_controller_manager](pr2_controller_manager) which will be used to
load the controllers on demand.

The driver sends different demands to the etherCAT hand and receives and
formats correctly the incoming packets. The incoming data is stored in a
vector of actuators (defined in the [sr_robot_lib](sr_robot_lib)
package). Those actuators are then passed to the controllers for the
1kHz control loop. The controllers are publishing the relevant data
(position / effort / velocity) at 100Hz on the \'\'\'/joint_states\'\'\'
topic, and the hardware diagnostics on the \'\'\'/diagnostics\'\'\'
topic at 1Hz.

The protocol used to interpret or build the etherCAT packets can be
found in [sr_external_dependencies](sr_external_dependencies).

Please refer to the [Tutorials](shadow_robot_etherCAT/Tutorials) to
learn how to use the driver.

## Checking the status of the robot

You can look at the current status of the robot using the
[robot_monitor](robot_monitor): ```
$ rosrun robot_monitor robot_monitor
```
