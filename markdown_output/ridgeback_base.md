## Overview

This package contains the primary binary which runs on
[Ridgeback](Robots/Ridgeback), providing the
[rosserial_server](rosserial_server)-based communication the MCU, as
well as diagnostic support, and other basic services such as lighting
and cooling. In addition, it provides the CAN based communication to the
[Puma motor controllers](puma_motor_driver).

## Compass Calibration

Ridgeback includes a built-in magnetometer, which is used by
[imu_filter_madgwick](imu_filter_madgwick) to estimate orientation. To
calibrate the magnetometer using scripts provided by this package, see
[the compass calibration tutorial from Jackal](http://docs.ros.org/api/jackal_tutorials/html/calibration.html).
