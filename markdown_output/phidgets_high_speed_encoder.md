## Overview

This package provides a ROS node for Phidget's high speed 4-Input
(1047) quadrature encoder decoder.

## Launch examples

Assuming you already have roscore running on another terminal:



```shell
rosrun phidgets_high_speed_encoder phidgets_high_speed_encoder _joint0_name:=wheel_FR _joint1_name:=wheel_FL _joint2_name:=wheel_RR _joint3_name:=wheel_RL _serial_number:=1234567 _PUBLISH_RATE:=20
```



Published topics:

-   `joint_states`: `JointState` msg with position and instantaneous
    speed of each axis.
-   `joint_states_ch{0,1,2,3}_decim_speed`: `EncoderDecimatedSpeed`
    msg with decimated (smoothed) speed for each channel.

Parameters:

-   `serial_number`: Board serial number to open.
-   `joint{0,1,2,3}_name`: Name of each axis; to be published inside
    the `name` field of each `JointState` msg.
-   `joint{0,1,2,3}_tick2rad`: Conversion factor from encoder
    "ticks" (counts) to radians.
-   `frame_id`: The frame that all messages are published in.
-   `PUBLISH_RATE`: Rate (in Hz) to publish status updates.
    (Default=20)
-   `SPEED_FILTER_SAMPLES_LEN`: (Default=10) Number of samples for the
    sliding window average filter of speeds.
-   `SPEED_FILTER_IDLE_ITER_LOOPS_BEFORE_RESET`: (Default=1) Number of
    "ITERATE" loops without any new encoder tick before resetting the
    filtered average velocities.
