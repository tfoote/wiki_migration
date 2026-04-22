## Overview

The joint trajectory action is a node that provides an action interface
for tracking trajectory execution. It passes trajectory goals to the
controller, and reports success when they have finished executing. The
joint trajectory action can also enforce constraints on the trajectory,
and abort trajectory execution when the constraints are violated.

See:
[robot_mechanism_controllers/JointSplineTrajectoryController](robot_mechanism_controllers/JointSplineTrajectoryController)

![](attachment:joint_trajectory_action_topics.png)

## ROS API

The ROS API consists of three parts: private parameters, an action
server that achieves trajectory goals, and an interface to a trajectory
controller.

### Parameters



```clearsilver
param {
  0.name=joints
  0.type=Array of strings
  0.desc=List of joints that this action will be commanding.  Must match the joints the controller is commanding.
  0.default=Required
  1.name=constraints/goal_time
  1.type=double
  1.default=0.0
  1.desc=The amount of time (in seconds) that the controller is permitted to be late to the goal.  If goal_time has passed and the controller still has not reached the final position, then the goal is aborted.
  2.name=constraints/<joint>/goal
  2.type=double
  2.default=-1.0
  2.desc=The maximum final error for <joint> for the trajectory goal to be considered successful.  Negative numbers indicate that there is no constraint.  Given in units of joint position (generally radians for revolute joints or meters for prismatic joints).  If this constraint is violated, the goal is aborted.
  3.name=constraints/<joint>/trajectory
  3.type=double
  3.default=-1.0
  3.desc=The maximum error for <joint> at any point during execution for the trajectory goal to be considered successful.  Negative numbers indicate that there is no constraint.  Given in units of joint position (generally radians for revolute joints or meters for prismatic joints).  If this constraint is violated, the goal is aborted.
  4.name=constraints/stopped_velocity_tolerance
  4.type=double
  4.default=0.01
  4.desc=The maximum velocity at the end of the trajectory for the joint to be considered stopped.  Given in units of joint position (generally radians for revolute joints or meters for prismatic joints).  If this constraint is satisfied, the goal is successful.
}
```



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
[actionlib](actionlib)) that takes in goals of the type
[pr2_controllers_msgs/msg/JointTrajectoryGoal](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/JointTrajectoryGoal.html).



```clearsilver
sub {
  0.name=joint_trajectory_action/goal
  0.type=pr2_controllers_msgs/JointTrajectoryActionGoal
  0.desc=The goal describes the trajectory for the robot to follow.
  1.name=joint_trajectory_action/cancel
  1.type=actionlib_msgs/GoalID
  1.desc=A request to cancel a specific goal.
}
pub {
  0.name=joint_trajectory_action/feedback
  0.type=pr2_controllers_msgs/JointTrajectoryActionFeedback
  0.desc=Feedback describing the progress the mechanism is making on following the trajectory.
  1.name=joint_trajectory_action/status
  1.type=actionlib_msgs/GoalStatusArray
  1.desc=Provides status information on the goals that are sent to the action.
  2.name=joint_trajectory_action/result
  2.type=pr2_controllers_msgs/JointTrajectoryActionResult
  2.desc=empty
}
```



### Controller interface



```clearsilver
sub {
  0.name=state
  0.type=pr2_controllers_msgs/JointTrajectoryControllerState
  0.desc=Listens to the state of the controller.
}
pub {
  0.name=command
  0.type=trajectory_msgs/JointTrajectory
  0.desc=Sends joint trajectories to the controller.
}
```



## Usage

You can find an example of using the joint trajectory action in
[this tutorial](pr2_controllers/Tutorials/Moving the arm using the Joint Trajectory Action)
for moving the arm on the PR2.
