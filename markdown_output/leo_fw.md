## Overview

This package contains the newest binary releases of
[leocore_firmware](https://github.com/LeoRover/leocore_firmware) and
[core2_firmware](https://github.com/LeoRover/core2_firmware) and the
script which flashes it to the
[LeoCore](https://www.leorover.tech/documentation/leo-core) or
[CORE2](https://husarion.com/manuals/core2/) board connected to the
Raspberry Pi. The script uses a modified version of
[stm32loader](https://github.com/fictionlab/stm32loader) python package,
so it has to be installed on the system.

## Usage

### Flashing firmware

To flash the newest firmware, simply type: 

```
rosrun leo_fw update
```

 To
flash the firmware from file, use the `flash` script:


```
rosrun leo_fw flash firmware.bin
```

 The script will guide you through the flashing
process.

The firmware uses [rosserial](https://index.ros.org/p/rosserial)
protocol to communicate with ROS nodes. This requires a running
host-side rosserial implementation which should be already started by
[leo_bringup](https://index.ros.org/p/leo_bringup), but it can also be
started manually: 

```
rosrun rosserial_python serial_node.py _port:=/dev/serial0 _baud:=250000
```

 Once the `serial_node`
connects to the firmware, the firmware's ROS API should be available on
the system.



```wiki
The ROS API differs between the firmwares released for Noetic and Melodic distributions. Make sure you read the correct section.
```



## ROS API (Noetic)

### firmware

#### Subscribed Topics

- `cmd_vel`
  ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
  Target velocity of the Rover. Only linear.x (m/s) and angular.z (r/s)
  are used.
- `firmware/wheel_{FL,RL,FR,RR}/cmd_pwm_duty`
  ([std_msgs/msg/Float32](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float32.html)):
  Sets the PWM duty cycle (in %) of the individual wheel.
- `firmware/wheel_{FL,RL,FR,RR}/cmd_velocity`
  ([std_msgs/msg/Float32](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float32.html)):
  Sets the target velocity (in rad/s) of the individual wheel.

##### Available only in the firmware for the CORE2 board:

- `firmware/servoX/cmd_angle`
  ([std_msgs/msg/Int16](https://docs.ros.org/en/rolling/p/std_msgs/msg/Int16.html)):
  Angular position (in user-defined units) of servo X.
- `firmware/servoX/cmd_pwm`
  ([std_msgs/msg/UInt16MultiArray](https://docs.ros.org/en/rolling/p/std_msgs/msg/UInt16MultiArray.html)):
  Pulse duration and period (in nanoseconds) of servo X. The values are
  passed through data array. Publishing to pwm topic overrides angle
  value and vice versa.

#### Published Topics

- `firmware/wheel_odom`
  ([leo_msgs/msg/WheelOdom](https://docs.ros.org/en/rolling/p/leo_msgs/msg/WheelOdom.html)):
  Odometry calculated from encoder readings.
- `firmware/battery`
  ([std_msgs/msg/Float32](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float32.html)):
  Current battery voltage reading.
- `firmware/battery_averaged`
  ([std_msgs/msg/Float32](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float32.html)):
  Battery voltage estimated from averaging readings from last 30
  seconds.
- `firmware/wheel_states`
  ([leo_msgs/msg/WheelStates](https://docs.ros.org/en/rolling/p/leo_msgs/msg/WheelStates.html)):
  Current states of the wheels (position, velocity, torque, PWM duty
  cycle).
- `firmware/imu`
  ([leo_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/leo_msgs/msg/Imu.html)):
  Current IMU gyroscope readings in radians per second.

#### Services

- `firmware/reset_odometry`
  ([std_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/std_srvs/srv/Trigger.html)):
  Resets the pose published on the `firmware/wheel_odom` topic.
- `firmware/reset_board`
  ([std_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/std_srvs/srv/Trigger.html)):
  Performs software reset of the board.
- `firmware/get_board_type`
  ([std_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/std_srvs/srv/Trigger.html)):
  Returns the board type codename (either *leocore* or *core2*).
- `firmware/get_firmware_version`
  ([std_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/std_srvs/srv/Trigger.html)):
  Returns the current firmware version.

#### Parameters

- `firmware/diff_drive/wheel_radius` (`float`, default: `0.0625`): The
  radius of the wheel in meters.
- `firmware/diff_drive/wheel_separation` (`float`, default: `0.33`): The
  distance (in meters) between the centers of the left and right wheels.
- `firmware/diff_drive/angular_velocity_multiplier` (`float`, default:
  `1.91`): Upon receiving a `cmd_vel` command, the angular velocity is
  multiplied by this parameter and the calculated odometry has its
  angular velocity divided by this parameter. This is done to account
  for a difference between a two-wheel robot model and the real robot.
- `firmware/diff_drive/input_timeout` (`int`, default: `500`): The
  timeout (in milliseconds) for the `cmd_vel` commands. The
  differential drive controller will stop the motors if it does not
  receive a command within the specified time. Set it to `0` to
  disable the timeout.
- `firmware/wheels/encoder_resolution` (`float`, default: `878.4`): The
  resolution of the wheel encoders in counts per rotation.
- `firmware/wheels/pid/p` (`float`, default: `0.0`): P constant of the
  motor's PID regulators.
- `firmware/wheels/pid/i` (`float`, default: `0.005`): I constant of the
  motor's PID regulators.
- `firmware/wheels/pid/d` (`float`, default: `0.0`): D constant of the
  motor's PID regulators.
- `firmware/wheels/pwm_duty_limit` (`float`, default: `100.0`): Limit of
  the PWM duty cycle (in %) applied to the motors. The value should be
  between `0.0` and `100.0`.
- `firmware/battery_min_voltage` (`float`, default: `10.0`): If the
  battery voltage drops below this value, the firmware will signal it by
  flickering the battery LED.

##### Available only in the firmware for the CORE2 board:

- `firmware/servo_voltage` (`int`, default: `2`): The number describing
  the servo power line voltage to set. The mapping of the values and
  corresponding voltages is as follows: `0` - 5V, `1` - 6V, `2` -
  7.4V, `3` - 8.6V
- `firmware/servoX/period` (`int`, default: `20000`): The period (in
  nanoseconds) of the PWM wave for servo X.
- `firmware/servoX/angle_min` (`int`, default: `-90`): The minimal angle
  (in user-defined units) for servo X.
- `firmware/servoX/angle_max` (`int`, default: `90`): The maximal angle
  (in user-defined units) for servo X.
- `firmware/servoX/width_min` (`int`, default: `1000`): The width of the
  pulse (in nanoseconds) corresponding to the minimal angle for servo X.
- `firmware/servoX/width_max` (`int`, default: `2000`): The width of the
  pulse (in nanoseconds) corresponding to the maximal angle for servo X.

### firmware_message_converter

A node that subscribes for the messages published by the firmware and
converts them to message types commonly used in ROS.

#### Subscribed Topics

- `firmware/wheel_states`
  ([leo_msgs/msg/WheelStates](https://docs.ros.org/en/rolling/p/leo_msgs/msg/WheelStates.html)):
  .
- `firmware/wheel_odom`
  ([leo_msgs/msg/WheelOdom](https://docs.ros.org/en/rolling/p/leo_msgs/msg/WheelOdom.html)):
  .
- `firmware/imu`
  ([leo_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/leo_msgs/msg/Imu.html)):
  .

#### Published Topics

- `joint_states`
  ([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html)):
  Converted from *firmware/wheel_states*.
- `wheel_odom_with_covariance`
  ([nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html)):
  Converted from *firmware/wheel_odom*.
- `imu/data_raw`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Converted from *firmware/imu*.

#### Parameters

- `robot_frame_id` (`string`, default: `"base_link"`): The TF frame id
  representing the robot. Used in the *child_frame_id* field of the
  *wheel_odom_with_covariance* messages.
- `odom_frame_id` (`string`, default: `"odom"`): The odom TF frame id.
  Used in the *header.frame_id* field of the
  *wheel_odom_with_covariance* messages.
- `imu_frame_id` (`string`, default: `"imu_frame"`): The TF frame id
  representing the IMU sensor. Used in the *header.frame_id* field of
  the *imu/data_raw* messages.
- `tf_frame_prefix` (`string`, default: `""`): The prefix added to each
  published TF frame id.
- `wheel_joint_names` (`string list`, default:
  `[wheel_FL_joint, wheel_RL_joint, wheel_FR_joint, wheel_RR_joint]`):
  Names of the wheel joints. Used in the *name* field of *joint_states*
  messages.
- `wheel_odom_twist_covariance_diagonal` (`float list`, default:
  `[0.0001, 0.0, 0.0, 0.0, 0.0, 0.001]`): The diagonal of the
  *twist.covariance* matrix used in the *wheel_odom_with_covariance*
  messages.
- `imu_angular_velocity_covariance_diagonal` (`float list`, default:
  `[0.000001, 0.000001, 0.00001]`): The diagonal of the
  *angular_velocity_covariance* matrix used in the *imu/data_raw*
  messages.
- `imu_linear_acceleration_covariance_diagonal` (`float list`, default:
  `[0.001, 0.001, 0.001]`): The diagonal of the
  *linear_acceleration_covariance* matrix used in the *imu/data_raw*
  messages.

## ROS API (Melodic)

### firmware

#### Subscribed Topics

- `cmd_vel`
  ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
  Target velocity of the Rover. Only linear.x (m/s) and angular.z (r/s)
  are used.
- `servoX/angle`
  ([std_msgs/msg/Int16](https://docs.ros.org/en/rolling/p/std_msgs/msg/Int16.html)):
  Angular position (in user-defined units) of servo X.
- `servoX/pwm`
  ([std_msgs/msg/UInt16MultiArray](https://docs.ros.org/en/rolling/p/std_msgs/msg/UInt16MultiArray.html)):
  Pulse duration and period (in nanoseconds) of servo X. The values are
  passed through data array. Publishing to pwm topic overrides angle
  value and vice versa.

#### Published Topics

- `wheel_odom`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Current linear and angular velocities estimated from encoder readings.
- `wheel_pose`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  A 2D pose of the robot estimated from the wheel velocities.
- `battery`
  ([std_msgs/msg/Float32](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float32.html)):
  Current battery voltage reading.
- `joint_states`
  ([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html)):
  Current state of the wheel joints. The units of measurements are as
  follows: position in radians, velocity in radians per second, effort
  in the PWM duty cycle (percent).

##### Only if IMU is enabled:

- `imu/gyro`
  ([geometry_msgs/msg/Vector3Stamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3Stamped.html)):
  Current IMU gyroscope readings in radians per second.
- `imu/accel`
  ([geometry_msgs/msg/Vector3Stamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3Stamped.html)):
  Current IMU accelerometer readings in meters per second squared.
- `imu/mag`
  ([geometry_msgs/msg/Vector3Stamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3Stamped.html)):
  Current IMU magnetometer readings in Gauss. The axes represent the
  North-West-Up world frame.

##### Only if GPS is enabled:

- `gps_fix`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  A Navigation Satellite fix returned by the GPS sensor.

#### Services

- `core2/reset_odometry`
  ([std_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/std_srvs/srv/Trigger.html)):
  Resets the pose published on the `wheel_pose` topic.
- `core2/reset_board`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Performs software reset on the CORE2 board.
- `core2/reset_config`
  ([std_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/std_srvs/srv/Trigger.html)):
  Loads the default config and saves it to persistant storage.
- `core2/get_firmware_version`
  ([std_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/std_srvs/srv/Trigger.html)):
  Returns the current firmware version.
- `core2/set_imu`
  ([std_srvs/srv/SetBool](https://docs.ros.org/en/rolling/p/std_srvs/srv/SetBool.html)):
  Enables or disables the IMU sensor and saves the configuration to
  persistent storage. Requires a reset to apply.
- `core2/set_gps`
  ([std_srvs/srv/SetBool](https://docs.ros.org/en/rolling/p/std_srvs/srv/SetBool.html)):
  Enables or disables the GPS sensor and saves the configuration to
  persistent storage. Requires a reset to apply.
- `core2/set_debug`
  ([std_srvs/srv/SetBool](https://docs.ros.org/en/rolling/p/std_srvs/srv/SetBool.html)):
  Enables or disables debug messages. For the messages to be sent to
  rosout, you also need to set the logger level of rosserial node to
  Debug. When enabled, it can cause issues with the rosserial
  communication due to high throughput.

##### Only if IMU is enabled:

- `imu/calibrate_gyro_accel`
  ([std_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/std_srvs/srv/Trigger.html)):
  Calibrates gyroscope and accelerometer biases and stores them in
  persistent storage. The IMU should lay perfectly still, parallel to
  the ground.
- `imu/calibrate_mag`
  ([std_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/std_srvs/srv/Trigger.html)):
  Calibrates magnetometer scale and biases and stores them in persistent
  storage. Wave the IMU in a figure eight until done.

#### Parameters

- `core2/diff_drive/wheel_radius` (`float`, default: `0.0625`): The
  radius of the wheel in meters.
- `core2/diff_drive/wheel_separation` (`float`, default: `0.33`): The
  distance (in meters) between the centers of the left and right wheels.
- `core2/diff_drive/angular_velocity_multiplier` (`float`, default:
  `0.0625`): Upon receiving a `cmd_vel` command, the angular velocity
  is multiplied by this parameter and the calculated odometry has its
  angular velocity divided by this parameter. This is done to account
  for a difference between a two-wheel robot model and the real robot.
- `core2/diff_drive/input_timeout` (`int`, default: `500`): The timeout
  (in milliseconds) for the `cmd_vel` commands. The differential drive
  controller will stop the motors if it does not receive a command
  within the specified time. Set it to `0` to disable the timeout.
- `core2/motors/encoder_resolution` (`float`, default: `878.4`): The
  resolution of the wheel encoders in counts per rotation.
- `core2/motors/encoder_pullup` (`int`, default: `1`): Whether to use
  internal pull-up for the encoder logic pins. Value of `1` means
  `yes`, any other value means `no`.
- `core2/motors/max_speed` (`float`, default: `800.0`): The maximum
  reachable speed of the motors in encoder counts per second. Used for
  limiting the value passed to the wheel controllers.
- `core2/motors/pid/p` (`float`, default: `0.0`): P constant of the
  motor's PID regulators.
- `core2/motors/pid/i` (`float`, default: `0.005`): I constant of the
  motor's PID regulators.
- `core2/motors/pid/d` (`float`, default: `0.0`): D constant of the
  motor's PID regulators.
- `core2/motors/power_limit` (`float`, default: `1000.0`): Limit of the
  PWM duty applied to the motors. The value should be between `0.0`
  (0% duty) and `1000.0` (100% duty).
- `core2/motors/torque_limit` (`float`, default: `1000.0`): This value
  applies an additional power limit depending on the current speed of
  the motors. The formula is as follows: `power_limit = (current_speed
  / max_speed) \* 1000.0 + torque_limit`
- `core2/servo_voltage` (`int`, default: `2`): The number describing the
  servo power line voltage to set. The mapping of the values and
  corresponding voltages is as follows: `0` - 5V, `1` - 6V, `2` -
  7.4V, `3` - 8.6V
- `core2/servoX/period` (`int`, default: `20000`): The period (in
  nanoseconds) of the PWM wave for servo X.
- `core2/servoX/angle_min` (`int`, default: `-90`): The minimal angle
  (in user-defined units) for servo X.
- `core2/servoX/angle_max` (`int`, default: `90`): The maximal angle (in
  user-defined units) for servo X.
- `core2/servoX/width_min` (`int`, default: `1000`): The width of the
  pulse (in nanoseconds) corresponding to the minimal angle for servo X.
- `core2/servoX/width_max` (`int`, default: `2000`): The width of the
  pulse (in nanoseconds) corresponding to the maximal angle for servo X.
- `core2/robot_frame_id` (`string`, default: `"base_link"`): The value
  of the frame_id field sent in the header of `wheel_odom` messages.
- `core2/odom_frame_id` (`string`, default: `"odom"`): The value of the
  frame_id field sent in the header of `wheel_pose` messages.

##### Only if IMU is enabled:

- `core2/imu_frame_id` (`string`, default: `"imu"`): The value of the
  frame_id field sent in the header of IMU messages.

##### Only if GPS is enabled:

- `core2/gps_frame_id` (`string`, default: `'gps'`): The value of the
  frame_id field sent in the header of GPS messages.
