## Overview

This package contains the code that runs in realtime to move the
mechanisms on the robot. These controllers are not specific to
mechanisms on the PR2 and may be useful on other robots.

- [Joint Trajectory Action Controller](robot_mechanism_controllers/JointTrajectoryActionController)
  for moving a set of joints along a joint space trajectory.
- [Joint Spline Trajectory Controller](robot_mechanism_controllers/JointSplineTrajectoryController)
  for moving a set of joints along a joint space trajectory
  *(deprecated, use the Joint Trajectory Action Controller instead)*.
- [Joint Effort Controller](robot_mechanism_controllers/JointEffortController)
  for commanding an effort (force or torque) to a single joint.
- [Joint Velocity Controller](robot_mechanism_controllers/JointVelocityController)
  for commanding velocities to a single joint.
- [Joint Position Controller](robot_mechanism_controllers/JointPositionController)
  for commanding positions to a single joint.
- [JT Cartesian Controller](robot_mechanism_controllers/JTCartesian Controller)
  for commanding poses (cartesian positions) to the end effector, with
  redundancy control.
- [Cartesian Wrench Controller](robot_mechanism_controllers/CartesianWrenchController)
  for commanding wrenches (cartesian forces and torques) to a chain of
  joints.
- [Cartesian Twist Controller](robot_mechanism_controllers/CartesianTwistController)
  for commanding twists (cartesian velocities) to a chain of joints.
- [Cartesian Pose Controller](robot_mechanism_controllers/CartesianPoseController)
  for commanding poses (cartesian positions) to a chain of joints.

## Stability

The controllers in this package should not be used directly. The
controllers should instead by used via their [action](actionlib)
interfaces, e.g., [joint_trajectory_action](joint_trajectory_action),
[pr2_gripper_action](pr2_gripper_action),
[pr2_head_action](pr2_head_action), and
[single_joint_position_action](single_joint_position_action).
