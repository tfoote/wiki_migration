## Nodes

```clearsilver
node.0 {
  name = nao_joint_states
  desc = Reads Nao's sensors and torso odometry through the Aldebaran API.
  param {
    0.name = ~sensor_rate
    0.desc = Rate for reading the sensors. The maximum acceptable value is 50 Hz.
    0.type = float
    0.default = 25.0
    1.name = ~base_frame_id
    1.desc = Name of the base TF frame
    1.type = string
    1.default = base_link
    2.name = ~odom_frame_id
    2.desc = Name of the odometry TF frame
    2.type = string
    2.default = odom
    3.name = ~use_joint_sensors
    3.desc = Use sensor values or commanded (open-loop) values for joint angles. Set to False in simulation!
    3.type = boolean
    3.default = True
  }
  pub {
    0.name = odom
    0.type = nav_msgs/Odometry
    0.desc = Odometry
    1.name = imu
    1.type = sensor_msgs/Imu
    1.desc = Readings from the inertial measurement unit
    2.name = joint_states
    2.type = sensor_msgs/JointState
    2.desc = Current joint angle values
    3.name = joint_stiffness
    3.type = sensor_msgs/JointState
    3.desc = Current joint stiffness values
  }
  prov_tf {
    0.from = base_link
    0.to   = odom
    0.desc = Odometry transform (TF frame names can be configured using the corresponding parameters).
  }
}
node.1 {
  name = naoqi_moveto_listener
  desc = Move to a given goal pose.
  sub {
    0.name = /move_base_simple/goal
    0.description = goal location to move to
    0.type = geometry_msgs/PoseStamped
  }
}
node.2 {
  name = nao_logger
  desc = Send Nao log messages to rosout
  pub {
    0.name = /rosout
    0.description = Topic for ROS log messages
    0.type = rosgraph_msgs/Log
  }
}
```
