See also
[robot_mechanism_controllers/JointSplineTrajectoryController](robot_mechanism_controllers/JointSplineTrajectoryController),
which is used by this action.

![](attachment:sjposition_action_topics.png)

## Usage

You can find an example of using the single joint position action on the
PR2 in the
[Moving the Torso tutorial](pr2_controllers/Tutorials/Moving the torso).

## ROS API

The ROS API consists of three parts: private parameters, an action
server that achieves position goals, and an interface to a trajectory
controller.

### Parameters

```clearsilver
param {
  0.name=~joint
  0.type=string
  0.default=Required
  0.desc=The joint to command
  1.name=~goal_threshold
  1.type=double
  1.default=0.1
  1.desc=The maximum distance from the goal at which to report success.
}
```

### Action interface

The joint trajectory action provides an action server (see
[actionlib](actionlib)) that takes in goals of the type
<<MsgLink(pr2_controllers_msgs/SingleJointPositionGoal)>>.

```clearsilver
sub {
  0.name=~position_joint_action/goal
  0.type=pr2_controllers_msgs/SingleJointPositionActionGoal
  0.desc=The goal describes the position for the robot to achieve
  1.name=~position_joint_action/cancel
  1.type=actionlib_msgs/GoalID
  1.desc=A request to cancel a specific goal.
}
pub {
  0.name=~position_joint_action/feedback
  0.type=pr2_controllers_msgs/SingleJointPositionActionFeedback
  0.desc=Feedback describing the progress the mechanism is making on reaching the goal position
  1.name=~position_joint_action/status
  1.type=actionlib_msgs/GoalStatusArray
  1.desc=Provides status information on the goals that are sent to the action.
  2.name=~position_joint_action/result
  2.type=pr2_controllers_msgs/SingleJointPositionActionResult
  2.desc=empty
}
```

### Controller interface

```clearsilver
sub {
  0.name=~state
  0.type=pr2_controllers_msgs/JointTrajectoryControllerState
  0.desc=Listens to the state of the controller.
}
pub {
  0.name=~command
  0.type=trajectory_msgs/JointTrajectory
  0.desc=Sends joint trajectories to the controller.
}
```
