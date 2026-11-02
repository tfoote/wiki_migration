## ROS API

### cob_trajectory_controller

The `cob_trajectory_controller` node takes in
[trajectory_msgs/msg/JointTrajectory](https://docs.ros.org/en/rolling/p/trajectory_msgs/msg/JointTrajectory.html)
messages and converts this to velocity commands to the hardware driver.

#### Action Goal

- `joint_trajectory_action/goal`
  ([pr2_controllers_msgs/msg/JointTrajectoryActionGoal](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/JointTrajectoryActionGoal.html)):
  The goal describes the trajectory for the robot to follow.

#### Action Result

- `joint_trajectory_action/result`
  ([pr2_controllers_msgs/msg/JointTrajectoryActionResult](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/JointTrajectoryActionResult.html)):
  empty

#### Action Feedback

- `joint_trajectory_action/feedback`
  ([pr2_controllers_msgs/msg/JointTrajectoryActionFeedback](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/JointTrajectoryActionFeedback.html)):
  empty

#### Published Topics

- `/joint_states`
  ([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html)):
  Publishes the joint states of all modules.
- `command_vel`
  ([brics_actuator/msg/JointVelocities](https://docs.ros.org/en/rolling/p/brics_actuator/msg/JointVelocities.html)):
  Publishes the velocity commands for the hardware driver.

#### Services

- `set_joint_velocity`
  ([cob_trajectory_controller/srv/SetFloat](https://docs.ros.org/en/rolling/p/cob_trajectory_controller/srv/SetFloat.html)):
  Sets the maximum velocity in joint space.
- `set_joint_acceleration`
  ([cob_trajectory_controller/srv/SetFloat](https://docs.ros.org/en/rolling/p/cob_trajectory_controller/srv/SetFloat.html)):
  Sets the maximum acceleration in joint space.

#### Parameters

- `~ptp_vel` (`double`, default: `Required`): Maximum velocity in joint
  space.
- `~ptp_acc` (`double`, default: `Required`): Maximum acceleration in
  joint space.
- `~max_error` (`double`, default: `Required`): Maximum allowed
  deviation from trajectory before controller is stopped.
