## Summary

This package provides an interface between [ros_control](ros_control)
(specifically [diff_drive_controller](diff_drive_controller)) and
[ros_arduino_bridge](ros_arduino_bridge).

## Getting Started

1\. Have your robot with an Arduino running the firmware from
[ros_arduino_bridge](ros_arduino_bridge). 2. Run the node with \`rosrun
diffdrive_arduino diffdrive_robot\`, specifying any parameters you need
to. 3. Set up the controllers. You will need to run a
[diff_drive_controller](diff_drive_controller) and a
[joint_state_controller](joint_state_controller). You may also need to
set the \`robot_description\` if that information is not provided
directly to the \`diff_drive_controller\`. 4. Run the controllers. 5.
Send some input to \`cmd_vel\` (e.g. with
[teleop_twist_joy](teleop_twist_joy)).

## Nodes

### diffdrive_robot

```clearsilver
param{
  0.name=~left_wheel_name
  0.type=string
  0.desc=Left wheel joint name
  0.default=left_wheel
  1.name=~right_wheel_name
  1.type=string
  1.desc=Right wheel joint name
  1.default=right_wheel
  2.name=~baud_rate
  2.type=int
  2.desc=Baud rate of serial connection
  2.default=57600
  3.name=~device
  3.type=string
  3.desc=Address of serial device
  3.default=/dev/ttyUSB0
  4.name=~loop_rate
  4.type=float
  4.desc=Frequency (in Hz) of the processing loop on the Arduino
  4.default=30.0
  5.name=~enc_counts_per_rev
  5.type=int
  5.desc=Number of encoder counts per wheel revolution
  5.default=1920
  6.name=~timeout
  6.type=int
  6.desc=Timeout (ms) of serial device
  6.default=1000
}
```

## Future Works

-   Support for different firmwares
-   PID adjustment
-   Better handling of parameters
-   Better documentation/tutorial
-   Example yamls/launch
