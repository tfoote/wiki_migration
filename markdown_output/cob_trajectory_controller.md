## ROS API



```clearsilver
 name = cob_trajectory_controller
 desc = The `cob_trajectory_controller` node takes in <<MsgLink(trajectory_msgs/JointTrajectory)>> messages and converts this to velocity commands to the hardware driver.

goal{
 0.name=joint_trajectory_action/goal
 0.type=pr2_controllers_msgs/JointTrajectoryActionGoal
 0.desc=The goal describes the trajectory for the robot to follow.
}

result{
 2.name=joint_trajectory_action/result
 2.type=pr2_controllers_msgs/JointTrajectoryActionResult
 2.desc=empty
}

feedback{
 0.name=joint_trajectory_action/feedback
 0.type=pr2_controllers_msgs/JointTrajectoryActionFeedback
 0.desc=empty
}

sub{
}

pub{
 0.name = /joint_states
 0.type = sensor_msgs/JointState
 0.desc = Publishes the joint states of all modules.
 1.name = command_vel
 1.type = brics_actuator/JointVelocities
 1.desc = Publishes the velocity commands for the hardware driver.
}

srv{
 0.name = set_joint_velocity
 0.type = cob_trajectory_controller/SetFloat
 0.desc = Sets the maximum velocity in joint space.
 1.name = set_joint_acceleration
 1.type = cob_trajectory_controller/SetFloat
 1.desc = Sets the maximum acceleration in joint space.
}
ptp_vel: 0.4 # rad/sec
ptp_acc: 0.1 # rad/sec^2
max_error: 0.2 # rad

param{
 0.name = ~ptp_vel
 0.type = double
 0.default = Required
 0.desc = Maximum velocity in joint space.
 1.name = ~ptp_acc
 1.type = double
 1.default = Required
 1.desc = Maximum acceleration in joint space.
 2.name = ~max_error
 2.type = double
 2.default = Required
 2.desc = Maximum allowed deviation from trajectory before controller is stopped.
}

req_tf{
}

prov_tf{
}
```
