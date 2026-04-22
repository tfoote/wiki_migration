See
[robot_mechanism_controllers/JointSplineTrajectoryController](robot_mechanism_controllers/JointSplineTrajectoryController)
for information on the controller that the head action communicates
with.

![](attachment:head_action_topics.png)

## Usage

An example of using the head action on the PR2 can be found in the
[Moving the Head tutorial](pr2_controllers/Tutorials/Moving the Head).

## ROS API

The ROS API consists of three parts: private parameters, an action
server that achieves pointing actions, and an interface to a trajectory
controller.

### Parameters



```clearsilver
param {
  0.name=~pan_link
  0.type=string
  0.default=head_pan_link
  0.desc=The name of the pan link of the head
  1.name=~tilt_link
  1.type=string
  1.default=head_tilt_link
  1.desc=The name of the tilt link of the head
  2.name=~success_angle_threshold
  2.type=double
  2.default=0.1
  2.desc=The maximum angular error from the desired pointing direction for which the action reports success.
}
```



### Action interface

The joint trajectory action provides an action server (see
[actionlib](actionlib)) that takes in goals of the type
[pr2_controllers_msgs/msg/PointHeadGoal](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/PointHeadGoal.html).
It reports success when the head is pointed at the target.



```clearsilver
sub {
  0.name=~point_head_action/goal
  0.type=pr2_controllers_msgs/PointHeadActionGoal
  0.desc=Describes where to point the head along with some constraints for the movement.
  1.name=~point_head_action/cancel
  1.type=actionlib_msgs/GoalID
  1.desc=A request to cancel a specific goal.
}
pub {
  0.name=~point_head_action/feedback
  0.type=pr2_controllers_msgs/PointHeadActionFeedback
  0.desc=Feedback describing the progress the mechanism is making on pointing the head.
  1.name=~point_head_action/status
  1.type=actionlib_msgs/GoalStatusArray
  1.desc=Provides status information on the goals that are sent to the action.
  2.name=~point_head_action/result
  2.type=pr2_controllers_msgs/PointHeadActionResult
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


