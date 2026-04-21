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

To flash the newest firmware, simply type: ```
rosrun leo_fw update
``` To
flash the firmware from file, use the `flash` script:
```
rosrun leo_fw flash firmware.bin
``` The script will guide you through the flashing
process.

The firmware uses [rosserial](rosserial) protocol to communicate with
ROS nodes. This requires a running host-side rosserial implementation
which should be already started by [leo_bringup](leo_bringup), but it
can also be started manually: ```
rosrun rosserial_python serial_node.py _port:=/dev/serial0 _baud:=250000
``` Once the
`serial_node` connects to the firmware, the firmware's ROS API should
be available on the system.

```wiki
The ROS API differs between the firmwares released for Noetic and Melodic distributions. Make sure you read the correct section.
```

## ROS API (Noetic)

```clearsilver
name= firmware
sub {
  group.0 {
    0.name= cmd_vel
    0.type= geometry_msgs/Twist
    0.desc= Target velocity of the Rover. Only linear.x (m/s) and angular.z (r/s) are used.
    1.name= firmware/wheel_{FL,RL,FR,RR}/cmd_pwm_duty
    1.type= std_msgs/Float32
    1.desc= Sets the PWM duty cycle (in %) of the individual wheel.
    2.name= firmware/wheel_{FL,RL,FR,RR}/cmd_velocity
    2.type= std_msgs/Float32
    2.desc= Sets the target velocity (in rad/s) of the individual wheel.
  }
  group.1 {
    name= Available only in the firmware for the CORE2 board:
    0.name= firmware/servoX/cmd_angle
    0.type= std_msgs/Int16
    0.desc= Angular position (in user-defined units) of servo X.
    1.name= firmware/servoX/cmd_pwm
    1.type= std_msgs/UInt16MultiArray
    1.desc= Pulse duration and period (in nanoseconds) of servo X. The values are passed through data array. Publishing to pwm topic overrides angle value and vice versa.
  }
}
pub {
  0.name= firmware/wheel_odom
  0.type= leo_msgs/WheelOdom
  0.desc= Odometry calculated from encoder readings.
  1.name= firmware/battery
  1.type= std_msgs/Float32
  1.desc= Current battery voltage reading.
  2.name= firmware/battery_averaged
  2.type= std_msgs/Float32
  2.desc= Battery voltage estimated from averaging readings from last 30 seconds.
  3.name= firmware/wheel_states
  3.type= leo_msgs/WheelStates
  3.desc= Current states of the wheels (position, velocity, torque, PWM duty cycle).
  4.name= firmware/imu
  4.type= leo_msgs/Imu
  4.desc= Current IMU gyroscope readings in radians per second.
}
srv{
  0.name= firmware/reset_odometry
  0.type= std_srvs/Trigger
  0.desc= Resets the pose published on the `firmware/wheel_odom` topic.
  1.name= firmware/reset_board
  1.type= std_srvs/Trigger
  1.desc= Performs software reset of the board.
  2.name= firmware/get_board_type
  2.type= std_srvs/Trigger
  2.desc= Returns the board type codename (either ''leocore'' or ''core2'').
  3.name= firmware/get_firmware_version
  3.type= std_srvs/Trigger
  3.desc= Returns the current firmware version.
}
param {
  group.0 {
    0.name= firmware/diff_drive/wheel_radius
    0.type= float
    0.default= 0.0625
    0.desc= The radius of the wheel in meters.
    1.name= firmware/diff_drive/wheel_separation
    1.type= float
    1.default= 0.33
    1.desc= The distance (in meters) between the centers of the left and right wheels.
    2.name= firmware/diff_drive/angular_velocity_multiplier
    2.type= float
    2.default= 1.91
    2.desc= Upon receiving a `cmd_vel` command, the angular velocity is multiplied by this parameter and the calculated odometry has its angular velocity divided by this parameter. This is done to account for a difference between a two-wheel robot model and the real robot.
    3.name= firmware/diff_drive/input_timeout
    3.type= int
    3.default= 500
    3.desc= The timeout (in milliseconds) for the `cmd_vel` commands. The differential drive controller will stop the motors if it does not receive a command within the specified time. Set it to `0` to disable the timeout.
    4.name= firmware/wheels/encoder_resolution
    4.type= float
    4.default= 878.4
    4.desc= The resolution of the wheel encoders in counts per rotation.
    7.name= firmware/wheels/pid/p
    7.type= float
    7.default= 0.0
    7.desc= P constant of the motor's PID regulators.
    8.name= firmware/wheels/pid/i
    8.type= float
    8.default= 0.005
    8.desc= I constant of the motor's PID regulators.
    9.name= firmware/wheels/pid/d
    9.type= float
    9.default= 0.0
    9.desc= D constant of the motor's PID regulators.
    10.name= firmware/wheels/pwm_duty_limit
    10.type= float
    10.default= 100.0
    10.desc= Limit of the PWM duty cycle (in %) applied to the motors. The value should be between `0.0` and `100.0`.
    11.name= firmware/battery_min_voltage
    11.type= float
    11.default= 10.0
    11.desc= If the battery voltage drops below this value, the firmware will signal it by flickering the battery LED.
  }
  group.1 {
    name= Available only in the firmware for the CORE2 board:
    12.name= firmware/servo_voltage
    12.type= int
    12.default= 2
    12.desc= The number describing the servo power line voltage to set. The mapping of the values and corresponding voltages is as follows: `0` - 5V, `1` - 6V, `2` - 7.4V, `3` - 8.6V
    13.name= firmware/servoX/period
    13.type= int
    13.default= 20000
    13.desc= The period (in nanoseconds) of the PWM wave for servo X.
    14.name= firmware/servoX/angle_min
    14.type= int
    14.default= -90
    14.desc= The minimal angle (in user-defined units) for servo X.
    15.name= firmware/servoX/angle_max
    15.type= int
    15.default= 90
    15.desc= The maximal angle (in user-defined units) for servo X.
    16.name= firmware/servoX/width_min
    16.type= int
    16.default= 1000
    16.desc= The width of the pulse (in nanoseconds) corresponding to the minimal angle for servo X.
    17.name= firmware/servoX/width_max
    17.type= int
    17.default= 2000
    17.desc= The width of the pulse (in nanoseconds) corresponding to the maximal angle for servo X.
  }
}
```

```clearsilver
name= firmware_message_converter
desc= A node that subscribes for the messages published by the firmware and converts them to message types commonly used in ROS.
sub {
  0.name= firmware/wheel_states
  0.type= leo_msgs/WheelStates
  0.desc= .
  1.name= firmware/wheel_odom
  1.type= leo_msgs/WheelOdom
  1.desc= .
  2.name= firmware/imu
  2.type= leo_msgs/Imu
  2.desc= .
}
pub {
  0.name= joint_states
  0.type= sensor_msgs/JointState
  0.desc= Converted from ''firmware/wheel_states''.
  1.name= wheel_odom_with_covariance
  1.type= nav_msgs/Odometry
  1.desc= Converted from ''firmware/wheel_odom''.
  2.name= imu/data_raw
  2.type= sensor_msgs/Imu
  2.desc= Converted from ''firmware/imu''.
}
param {
  0.name= robot_frame_id
  0.type= string
  0.default= "base_link"
  0.desc= The TF frame id representing the robot. Used in the ''child_frame_id'' field of the ''wheel_odom_with_covariance'' messages.
  1.name= odom_frame_id
  1.type= string
  1.default= "odom"
  1.desc= The odom TF frame id. Used in the ''header.frame_id'' field of the ''wheel_odom_with_covariance'' messages.
  2.name= imu_frame_id
  2.type= string
  2.default= "imu_frame"
  2.desc= The TF frame id representing the IMU sensor. Used in the ''header.frame_id'' field of the ''imu/data_raw'' messages.
  3.name= tf_frame_prefix
  3.type= string
  3.default= ""
  3.desc= The prefix added to each published TF frame id.
  4.name= wheel_joint_names
  4.type= string list
  4.default= [wheel_FL_joint, wheel_RL_joint, wheel_FR_joint, wheel_RR_joint]
  4.desc= Names of the wheel joints. Used in the ''name'' field of ''joint_states'' messages.
  5.name= wheel_odom_twist_covariance_diagonal
  5.type= float list
  5.default= [0.0001, 0.0, 0.0, 0.0, 0.0, 0.001]
  5.desc= The diagonal of the ''twist.covariance'' matrix used in the ''wheel_odom_with_covariance'' messages.
  6.name= imu_angular_velocity_covariance_diagonal
  6.type= float list
  6.default= [0.000001, 0.000001, 0.00001]
  6.desc= The diagonal of the ''angular_velocity_covariance'' matrix used in the ''imu/data_raw'' messages.
  7.name= imu_linear_acceleration_covariance_diagonal
  7.type= float list
  7.default= [0.001, 0.001, 0.001]
  7.desc= The diagonal of the ''linear_acceleration_covariance'' matrix used in the ''imu/data_raw'' messages.
}
```

## ROS API (Melodic)

```clearsilver
name= firmware
sub {
  0.name= cmd_vel
  0.type= geometry_msgs/Twist
  0.desc= Target velocity of the Rover. Only linear.x (m/s) and angular.z (r/s) are used.
  1.name= servoX/angle
  1.type= std_msgs/Int16
  1.desc= Angular position (in user-defined units) of servo X.
  2.name= servoX/pwm
  2.type= std_msgs/UInt16MultiArray
  2.desc= Pulse duration and period (in nanoseconds) of servo X. The values are passed through data array. Publishing to pwm topic overrides angle value and vice versa.
}
pub {
  group.0 {
    0.name= wheel_odom
    0.type= geometry_msgs/TwistStamped
    0.desc= Current linear and angular velocities estimated from encoder readings.
    1.name= wheel_pose
    1.type= geometry_msgs/PoseStamped
    1.desc= A 2D pose of the robot estimated from the wheel velocities.
    2.name= battery
    2.type= std_msgs/Float32
    2.desc= Current battery voltage reading.
    3.name= joint_states
    3.type= sensor_msgs/JointState
    3.desc= Current state of the wheel joints. The units of measurements are as follows: position in radians, velocity in radians per second, effort in the PWM duty cycle (percent).
  }
  group.1 {
    name= Only if IMU is enabled:
    0.name= imu/gyro
    0.type= geometry_msgs/Vector3Stamped
    0.desc= Current IMU gyroscope readings in radians per second.
    1.name= imu/accel
    1.type= geometry_msgs/Vector3Stamped
    1.desc= Current IMU accelerometer readings in meters per second squared.
    2.name= imu/mag
    2.type= geometry_msgs/Vector3Stamped
    2.desc= Current IMU magnetometer readings in Gauss. The axes represent the North-West-Up world frame.
  }
  group.2 {
    name= Only if GPS is enabled:
    0.name= gps_fix
    0.type= sensor_msgs/NavSatFix
    0.desc= A Navigation Satellite fix returned by the GPS sensor.
  }
}
srv{
  group.0 {
    0.name= core2/reset_odometry
    0.type= std_srvs/Trigger
    0.desc= Resets the pose published on the `wheel_pose` topic.
    1.name= core2/reset_board
    1.type= std_srvs/Empty
    1.desc= Performs software reset on the CORE2 board.
    2.name= core2/reset_config
    2.type= std_srvs/Trigger
    2.desc= Loads the default config and saves it to persistant storage.
    3.name= core2/get_firmware_version
    3.type= std_srvs/Trigger
    3.desc= Returns the current firmware version.
    4.name= core2/set_imu
    4.type= std_srvs/SetBool
    4.desc= Enables or disables the IMU sensor and saves the configuration to persistent storage. Requires a reset to apply.
    5.name= core2/set_gps
    5.type= std_srvs/SetBool
    5.desc= Enables or disables the GPS sensor and saves the configuration to persistent storage. Requires a reset to apply.
    6.name= core2/set_debug
    6.type= std_srvs/SetBool
    6.desc= Enables or disables debug messages. For the messages to be sent to rosout, you also need to set the logger level of rosserial node to Debug. When enabled, it can cause issues with the rosserial communication due to high throughput.
  }
  group.1 {
    name= Only if IMU is enabled:
    0.name= imu/calibrate_gyro_accel
    0.type= std_srvs/Trigger
    0.desc= Calibrates gyroscope and accelerometer biases and stores them in persistent storage. The IMU should lay perfectly still, parallel to the ground.
    1.name= imu/calibrate_mag
    1.type= std_srvs/Trigger
    1.desc= Calibrates magnetometer scale and biases and stores them in persistent storage. Wave the IMU in a figure eight until done.
  }
}
param {
  group.0 {
    0.name= core2/diff_drive/wheel_radius
    0.type= float
    0.default= 0.0625
    0.desc= The radius of the wheel in meters.
    1.name= core2/diff_drive/wheel_separation
    1.type= float
    1.default= 0.33
    1.desc= The distance (in meters) between the centers of the left and right wheels.
    2.name= core2/diff_drive/angular_velocity_multiplier
    2.type= float
    2.default= 0.0625
    2.desc= Upon receiving a `cmd_vel` command, the angular velocity is multiplied by this parameter and the calculated odometry has its angular velocity divided by this parameter. This is done to account for a difference between a two-wheel robot model and the real robot.
    3.name= core2/diff_drive/input_timeout
    3.type= int
    3.default= 500
    3.desc= The timeout (in milliseconds) for the `cmd_vel` commands. The differential drive controller will stop the motors if it does not receive a command within the specified time. Set it to `0` to disable the timeout.
    4.name= core2/motors/encoder_resolution
    4.type= float
    4.default= 878.4
    4.desc= The resolution of the wheel encoders in counts per rotation.
    5.name= core2/motors/encoder_pullup
    5.type= int
    5.default= 1
    5.desc= Whether to use internal pull-up for the encoder logic pins. Value of `1` means `yes`, any other value means `no`.
    6.name= core2/motors/max_speed
    6.type= float
    6.default= 800.0
    6.desc= The maximum reachable speed of the motors in encoder counts per second. Used for limiting the value passed to the wheel controllers.
    7.name= core2/motors/pid/p
    7.type= float
    7.default= 0.0
    7.desc= P constant of the motor's PID regulators.
    8.name= core2/motors/pid/i
    8.type= float
    8.default= 0.005
    8.desc= I constant of the motor's PID regulators.
    9.name= core2/motors/pid/d
    9.type= float
    9.default= 0.0
    9.desc= D constant of the motor's PID regulators.
    10.name= core2/motors/power_limit
    10.type= float
    10.default= 1000.0
    10.desc= Limit of the PWM duty applied to the motors. The value should be between `0.0` (0% duty) and `1000.0` (100% duty).
    11.name= core2/motors/torque_limit
    11.type= float
    11.default= 1000.0
    11.desc= This value applies an additional power limit depending on the current speed of the motors. The formula is as follows: `power_limit = (current_speed / max_speed) * 1000.0 + torque_limit`
    12.name= core2/servo_voltage
    12.type= int
    12.default= 2
    12.desc= The number describing the servo power line voltage to set. The mapping of the values and corresponding voltages is as follows: `0` - 5V, `1` - 6V, `2` - 7.4V, `3` - 8.6V
    13.name= core2/servoX/period
    13.type= int
    13.default= 20000
    13.desc= The period (in nanoseconds) of the PWM wave for servo X.
    14.name= core2/servoX/angle_min
    14.type= int
    14.default= -90
    14.desc= The minimal angle (in user-defined units) for servo X.
    15.name= core2/servoX/angle_max
    15.type= int
    15.default= 90
    15.desc= The maximal angle (in user-defined units) for servo X.
    16.name= core2/servoX/width_min
    16.type= int
    16.default= 1000
    16.desc= The width of the pulse (in nanoseconds) corresponding to the minimal angle for servo X.
    17.name= core2/servoX/width_max
    17.type= int
    17.default= 2000
    17.desc= The width of the pulse (in nanoseconds) corresponding to the maximal angle for servo X.
    18.name= core2/robot_frame_id
    18.type= string
    18.default= "base_link"
    18.desc= The value of the frame_id field sent in the header of `wheel_odom` messages.
    19.name= core2/odom_frame_id
    19.type= string
    19.default= "odom"
    19.desc= The value of the frame_id field sent in the header of `wheel_pose` messages.
  }
  group.1 {
    name= Only if IMU is enabled:
    0.name= core2/imu_frame_id
    0.type= string
    0.default= "imu"
    0.desc= The value of the frame_id field sent in the header of IMU messages.
  }
  group.2 {
    name= Only if GPS is enabled:
    0.name= core2/gps_frame_id
    0.type= string
    0.default= 'gps'
    0.desc= The value of the frame_id field sent in the header of GPS messages.
  }
}
```
