## ROS API

### ZMP estimation from force sensors

The most widely used balance criterion is the (virtual) Zero Momentum
Point. When this point exits the robot polygon support, the robot start
falling.

It is therefore interesting to monitor this point while the robot is
running to make sure that it stays near its planned position.

A method to estimate the ZMP position is to measure the force applied on
both feet and deduce the ZMP position from it. This tool realizes this
computation and makes the following assuption:

-   the frame orientation of the force sensor data is the standard one
    (X forward, Y to the left and Z up),
-   two force sensors localized in the feet/ankles and synchronized data
    from them are available as
    <<MsgLink(geometry_msgs/WrenchStamped)>> messages.
-   the robot is biped.

```clearsilver
name = zmp_estimator
desc = ZMP estimation node from feet force sensors

sub {
  0.name = ~left_foot_wrench
  0.type = geometry_msgs/WrenchStamped
  0.desc = Left foot wrench measure by a force sensor.

  1.name = ~right_foot_wrench
  1.type = geometry_msgs/WrenchStamped
  1.desc = Right foot wrench measure by a force sensor.

}

pub {
  0.name = zmp_estimated
  0.type = geometry_msgs/Vector3Stamped
  0.desc = ZMP position estimation.
}

param {
  0.name = left_foot_wrench
  0.type = string
  0.desc = Left foot wrench topic name
  0.default = left_foot

  1.name = right_foot_wrench
  1.type = string
  1.desc = Right foot wrench topic name
  1.default = right_foot

  2.name = contact_threshold
  2.type = Float64
  2.desc = Minimum force to consider that the foot touched the ground. By default 10 Newton. We recommend 2% of the robot total mass.
  2.default = 10

  3.name = approximate_sync
  3.type = Float64
  3.desc = Maximum allowed offset between the left and right foot wrench messages.
  3.default = 0.001

  4.name = queue_size
  4.type = Float64
  4.desc = Subscriber queue size
  4.default = 10

  5.name = reference_frame
  5.type = string
  5.desc = Id of the frame in which the foot positions are given.
  5.default = /world

  6.name = left_foot_x
  6.type = Float64
  6.desc = Left foot X position in reference frame.
  6.default = 0.

  7.name = left_foot_y
  7.type = Float64
  7.desc = Left foot Y position in reference frame.
  7.default = 0.

  8.name = left_foot_z
  8.type = Float64
  8.desc = Left foot Z position in reference frame.
  8.default = 0.105

  9.name = right_foot_x
  9.type = Float64
  9.desc = Right foot X position in reference frame.
  9.default = 0.

  10.name = right_foot_y
  10.type = Float64
  10.desc = Right foot Y position in reference frame.
  10.default = 0.

  11.name = right_foot_z
  11.type = Float64
  11.desc = Right foot Z position in reference frame.
  11.default = 0.105
}
```

For instance, you may run this script by typing:
```shell
rosrun walk_tools zmp_monitor _left_foot_wrench:=/force_0 _right_foot_wrench:=/force_1
```

### Effort monitor

During movement execution, effort monitoring on each actuator prevents
robot dammage.

This script regularly checks that the current torques reported by the
`joint_states` topic are lower than the limit indicated in the robot
URDF model. If the effort is higher that 85% of the limit, a warning is
issued. Warning and errors are reported using the ROS diagnostics stack.

```clearsilver
name = effort_monitor
desc = Monitor efforts on joints.

sub {
  0.name = joint_states
  0.type = sensor_msgs/JointStates
  0.desc = Current state of each joint. In particular, this structure contains the current efforts applied to the robot joints.
}

pub {
  0.name = diagnosics
  0.type = diagnostic_msgs/DiagnosticArray
  0.desc = Diagnostic topic.
}
```

```clearsilver
name = force_monitor
desc = Monitor force applied to robot feet. The script makes the assumption that the reaction force is along the Z axis.

sub {
  0.name = left_foot
  0.type = geometry_msgs/WrenchStamped
  0.desc = Force sensor output on left foot.

  1.name = right_foot
  1.type = geometry_msgs/WrenchStamped
  1.desc = Force sensor output on right foot.
}

pub {
  0.name = diagnosics
  0.type = diagnostic_msgs/DiagnosticArray
  0.desc = Diagnostic topic.
}

param {
  0.name = force_warning_threshold
  0.type = Float64
  0.desc = Maxmimum allowed force before warning the user.

  1.name = force_error_threshold
  1.type = Float64
  1.desc = Maxmimum allowed force before reporting an error.
}
```
