## Overview

This package allows the use of Erratic mobile base by Videre Design
within ROS.

## Nodes



```clearsilver
node.0 {
  name = erratic_player
  desc = A wrapper ROS node around an Erratic driver found in player project.

  sub {
    0.name = cmd_vel
    0.type = geometry_msgs/Twist
    0.desc = Velocity commands to drive the robot.
    1.name = cmd_vision_tilt
    1.type = std_msgs/Float64
    1.desc = Angle command to the vision tilt servo actuator. Only enabled when enable_vision_pan_tilt parameter is set to true.
    2.name = cmd_vision_pan
    2.type = std_msgs/Float64
    2.desc = Angle command to the vision pan servo actuator. Only enabled when enable_vision_pan_tilt parameter is set to true.
    3.name = cmd_ranger_tilt
    3.type = std_msgs/Float64
    3.desc = Angle command to the ranger tilt servo actuator. Only enabled when enable_ranger_tilt parameter is set to true.
  }

  pub {
    0.name = odom
    0.type = nav_msgs/Odometry
    0.desc = Odometry data.
    1.name = battery_state
    1.type = erratic_player/BatteryState
    1.desc = Battery data.
    2.name = ir
    2.type = erratic_player/RangeArray
    2.desc = IR sensors range information.
    3.name = sonar
    3.type = erratic_player/RangeArray
    3.desc = Sonar sensors range information.
  }

  param {
    0.name = port_name
    0.type = string
    0.desc = Name of the serial port that the robot is connected to.
    0.default = "/dev/ttyUSB0"
    1.name = odometry_frame_id
    1.type = string
    1.desc = The name of the frame which will be used to send stamped transforms through the TF mechanism. 
    1.default = "odom"
    2.name = max_trans_vel
    2.type = string
    2.desc = Maximum translational velocity.
    2.default = "0.5"
    3.name = max_rot_vel
    3.type = string
    3.desc = Maximum rotational velocity.
    3.default = "100"
    4.name = max_rot_vel
    4.type = string
    4.desc = Maximum rotational velocity.
    4.default = "100"
    5.name = trans_acc
    5.type = string
    5.desc = Maximum translational acceleration, nonnegative. The value of "0" means use robot's default value.
    5.default = "0"
    6.name = trans_decel
    6.type = string
    6.desc = Maximum translational deceleration, nonpositive. The value of "0" means use robot's default value.
    6.default = trans_acc
    7.name = rot_acc
    7.type = string
    7.desc = Maximum rotational acceleration, nonnegative. The value of "0" means use robot's default value.
    7.default = "0"
    8.name = rot_decel
    8.type = string
    8.desc = Maximum rotational deceleration, nonpositive. The value of "0" means use robot's default value.
    8.default = rot_acc
    9.name = enable_ir
    9.type = bool
    9.desc = Whether to enable IR sensors.
    9.default = false
    10.name = enable_sonar
    10.type = bool
    10.desc = Whether to enable Sonar sensors.
    10.default = false
    11.name = enable_vision_pan_tilt
    11.type = bool
    11.desc = Whether to enable vision pan/tilt servo motors.
    11.default = false
    12.name = enable_ranger_tilt
    12.type = bool
    12.desc = Whether to enable ranger tilt servo motor.
    12.default = false
}
```



## Tutorials

Links to relevant tutorials
