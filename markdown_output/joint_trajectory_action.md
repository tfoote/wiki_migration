## Overview

The joint trajectory action is a node that provides an action interface
for tracking trajectory execution. It passes trajectory goals to the
controller, and reports success when they have finished executing. The
joint trajectory action can also enforce constraints on the trajectory,
and abort trajectory execution when the constraints are violated.

See:
[JointSplineTrajectoryController](https://index.ros.org/p/robot_mechanism_controllers)

![attachment:joint_trajectory_action_topics.png](doc/joint_trajectory_action_topics.png)

## ROS API

The ROS API consists of three parts: private parameters, an action
server that achieves trajectory goals, and an interface to a trajectory
controller.

### Parameters

#### Parameters

- `joints` (`Array of strings`, default: `Required`): List of joints
  that this action will be commanding. Must match the joints the
  controller is commanding.
- `constraints/goal_time` (`double`, default: `0.0`): The amount of time
  (in seconds) that the controller is permitted to be late to the goal.
  If goal_time has passed and the controller still has not reached the
  final position, then the goal is aborted.
- `constraints/<joint>/goal` (`double`, default: `-1.0`): The maximum
  final error for <joint> for the trajectory goal to be considered
  successful. Negative numbers indicate that there is no constraint.
  Given in units of joint position (generally radians for revolute
  joints or meters for prismatic joints). If this constraint is
  violated, the goal is aborted.
- `constraints/<joint>/trajectory` (`double`, default: `-1.0`): The
  maximum error for <joint> at any point during execution for the
  trajectory goal to be considered successful. Negative numbers indicate
  that there is no constraint. Given in units of joint position
  (generally radians for revolute joints or meters for prismatic
  joints). If this constraint is violated, the goal is aborted.
- `constraints/stopped_velocity_tolerance` (`double`, default: `0.01`):
  The maximum velocity at the end of the trajectory for the joint to be
  considered stopped. Given in units of joint position (generally
  radians for revolute joints or meters for prismatic joints). If this
  constraint is satisfied, the goal is successful.

Example configuration (from
pr2_controller_configuration/pr2_arm_controllers.yaml):



```
joint_trajectory_action_node:
  joints:
    - r_shoulder_pan_joint
    - r_shoulder_lift_joint
    - r_upper_arm_roll_joint
    - r_elbow_flex_joint
    - r_forearm_roll_joint
    - r_wrist_flex_joint
    - r_wrist_roll_joint
  constraints:
    goal_time: 0.3
    r_shoulder_pan_joint:
      goal: 0.04
    r_shoulder_lift_joint:
      goal: 0.04
    r_upper_arm_roll_joint:
      goal: 0.04
    r_elbow_flex_joint:
      goal: 0.04
    r_forearm_roll_joint:
      goal: 0.04
    r_wrist_flex_joint:
      goal: 0.04
    r_wrist_roll_joint:
      goal: 0.04
```



### Action interface

The joint trajectory action provides an action server (see
[actionlib](https://index.ros.org/p/actionlib)) that takes in goals of
the type
[pr2_controllers_msgs/msg/JointTrajectoryGoal](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/JointTrajectoryGoal.html).

#### Subscribed Topics

- `joint_trajectory_action/goal`
  ([pr2_controllers_msgs/msg/JointTrajectoryActionGoal](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/JointTrajectoryActionGoal.html)):
  The goal describes the trajectory for the robot to follow.
- `joint_trajectory_action/cancel`
  ([actionlib_msgs/msg/GoalID](https://docs.ros.org/en/rolling/p/actionlib_msgs/msg/GoalID.html)):
  A request to cancel a specific goal.

#### Published Topics

- `joint_trajectory_action/feedback`
  ([pr2_controllers_msgs/msg/JointTrajectoryActionFeedback](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/JointTrajectoryActionFeedback.html)):
  Feedback describing the progress the mechanism is making on following
  the trajectory.
- `joint_trajectory_action/status`
  ([actionlib_msgs/msg/GoalStatusArray](https://docs.ros.org/en/rolling/p/actionlib_msgs/msg/GoalStatusArray.html)):
  Provides status information on the goals that are sent to the action.
- `joint_trajectory_action/result`
  ([pr2_controllers_msgs/msg/JointTrajectoryActionResult](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/JointTrajectoryActionResult.html)):
  empty

### Controller interface

#### Subscribed Topics

- `state`
  ([pr2_controllers_msgs/msg/JointTrajectoryControllerState](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/JointTrajectoryControllerState.html)):
  Listens to the state of the controller.

#### Published Topics

- `command`
  ([trajectory_msgs/msg/JointTrajectory](https://docs.ros.org/en/rolling/p/trajectory_msgs/msg/JointTrajectory.html)):
  Sends joint trajectories to the controller.

## Usage

You can find an example of using the joint trajectory action in
[this tutorial](https://index.ros.org/p/pr2_controllers) for moving the
arm on the PR2.

## Tutorials

In addition to the tutorials below, you can find an example of using the
joint trajectory action in [this tutorial](https://index.ros.org/p/pr2)
for moving the arm on the PR2.
