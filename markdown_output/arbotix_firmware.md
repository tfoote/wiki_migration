## Overview

This package contains the source code for firmware that handles
communication with the ArbotiX-ROS bindings. It can be compiled and
uploaded to the ArbotiX using the Arduino IDE.

## Compiling and Uploading Firmware

To compile and upload the firmware you will need to:

-   Install the Arduino IDE, following the directions on the
    [Arduino website](http://arduino.cc/en/Guide/HomePage).
-   Install the ArbotiX extensions, following directions found on the
    [ArbotiX wiki](http://code.google.com/p/arbotix/wiki/GettingSetup).
-   Install the
    [RoboController libraries](http://code.google.com/p/robocontroller/).

You can then copy the files found in the *src* folder of this package
into your sketchbook. You should then be able to open the *ros* sketch,
compile and upload.

## Build Configurations

There are several build macros that select the configuration of your
firmware:

-   **USE_PML** - builds support for the Planar Meta-Laser (PML).
-   **USE_BASE** - builds support for control of a differential drive
    base.
-   **USE_BIG_MOTORS** - uses the BigMotors library, which allows
    upgrading the 1A motor drivers found on the ArbotiX to a 30A motor
    driver available from Pololu. (Details soon).
-   **USE_HW_SERVOS** - uses the *HServo* library rather than the newer
    *Servo* library for hobby servo support. This limits the ArbotiX to
    only 2 hobby servos, however it provides immunity against servo
    jitter under heavy processor load (and is therefore recommended).

## Road Map

Future releases of this package will include pre-compiled binaries that
can be uploaded using just avrdude.
