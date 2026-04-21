## Documentation

To start the WheeledRobin driver node use the launch files in
wheeled_robin_bringup.

## Nodes



```clearsilver
name = wheeled_robin_node
desc = ROS bindings for the !WheeledRobin driver (wheeled_robin_driver). This is based on create_node driver by OSRF.
sub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Desired velocity for !WheeledRobin (x, theta)
}
pub {
  0.name = odom
  0.type = nav_msgs/Odometry
  0.desc = Odometry of !WheeledRobin.
  1.name = joint_states
  1.type = sensor_msgs/JointState
  1.desc = Joint State for the left and right wheel.
  2.name = ~sensor_state
  2.type = wheeled_robin_node/WheeledRobinSensorState
  2.desc = State of the !WheeledRobin sensors.
  3.name = diagnostics
  3.type = diagnostic_msgs/DiagnosticArray
  3.desc = Diagnostic information for !WheeledRobin.
}
srv {
  0.name = ~set_operation_mode
  0.type = wheeled_robin_node/SetWheeledRobinMode
  0.desc = Sets the operation mode of !WheeledRobin.
  1.name = ~set_digital_outputs
  1.type = wheeled_robin_node/SetDigitalOutputs
  1.desc = Sets the digital outputs of !WheeledRobin.
}
param {
  0.name = ~update_rate
  0.type = double
  0.desc = Polling rate for the !WheeledRobin. Choices: 5 - 1000 Hz
  0.default = 100.0
  1.name = ~drive_mode
  1.type = string
  1.desc = The possible drive modes. While 'drive' takes a geometry_msgs/Twist message and sends it directly to the robot, 'direct_drive' takes a geometry_msgs/Twist message, calculates wheels speeds and sends them to the robot. Choices: 'drive' or 'direct_drive'
  1.default = 'drive'
  2.name = ~cmd_vel_timeout
  2.type = double
  2.desc = How long to wait before timing out on a velocity command. Choices: 0.0 - 1.0
  2.default = 0.6
  3.name = ~odom_angular_scale_correction
  3.type = double
  3.desc = A correction applied to the computation of the rotation in the odometry. Choices: 0.0 - 3.0
  3.default = 1.0
  4.name = ~odom_linear_scale_correction
  4.type = double
  4.desc = A correction applied to the computation of the translation in odometry. Choices: 0.0 - 3.0
  4.default = 1.0
  5.name = ~min_abs_yaw_vel
  5.type = double
  5.desc = Minimum angular velocity of the !WheeledRobin. Choices: 0.0 - 3.0
  5.default = None
  6.name = ~max_abs_yaw_vel
  6.type = double
  6.desc = Maximum angular velocity of the !WheeledRobin. Choices: 0.0 - 3.0
  6.default = None
  7.name = ~port
  7.type = string
  7.desc = Serial port where !WheeledRobin is connected to.
  7.default = /dev/ttyUSB0
  8.name = ~publish_tf
  8.type = bool
  8.desc = Publish Transformations.
  8.default = False
  9.name = ~odom_frame
  9.type = string
  9.desc = Name of the odom frame (used while publishing TF).
  9.default = odom
  10.name = ~base_footprint_frame
  10.type = string
  10.desc = Name of the base_footprint frame (used while publishing TF).
  10.default = base_footprint
  11.name = ~base_link_frame
  11.type = string
  11.desc = Name of the base_link frame (used while publishing TF).
  11.default = base_link
  12.name = ~operation_mode
  12.type = integer
  12.desc = Operation mode of !WheeledRobin used while driving. Choices: 2 or 3
  12.default = 3
}
prov_tf {
  0.from = odom
  0.to   = base_footprint
  0.desc = odom frame is set with '~odom_frame' parameter, base_footprint frame is set with '~base_footprint_frame' parameter. Depends on the odometry of !WheeledRobin
  1.from = base_footprint
  1.to   = base_link
  1.desc = base_footprint frame is set with '~base_footprint_fra,e' parameter, base_link frame is set with '~base_link_frame' parameter. Depends on the pitch angle of !WheeledRobin
}
```


