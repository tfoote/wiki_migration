See
[JointSplineTrajectoryController](https://index.ros.org/p/robot_mechanism_controllers)
for information on the controller that the head action communicates
with.

![attachment:head_action_topics.png](doc/head_action_topics.png)

## Usage

An example of using the head action on the PR2 can be found in the
[Moving the Head tutorial](https://index.ros.org/p/pr2_controllers).

## ROS API

The ROS API consists of three parts: private parameters, an action
server that achieves pointing actions, and an interface to a trajectory
controller.

### Parameters

#### Parameters

- `~pan_link` (`string`, default: `head_pan_link`): The name of the pan
  link of the head
- `~tilt_link` (`string`, default: `head_tilt_link`): The name of the
  tilt link of the head
- `~success_angle_threshold` (`double`, default: `0.1`): The maximum
  angular error from the desired pointing direction for which the action
  reports success.

### Action interface

The joint trajectory action provides an action server (see
[actionlib](https://index.ros.org/p/actionlib)) that takes in goals of
the type
[pr2_controllers_msgs/msg/PointHeadGoal](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/PointHeadGoal.html).
It reports success when the head is pointed at the target.

#### Subscribed Topics

- `~point_head_action/goal`
  ([pr2_controllers_msgs/msg/PointHeadActionGoal](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/PointHeadActionGoal.html)):
  Describes where to point the head along with some constraints for the
  movement.
- `~point_head_action/cancel`
  ([actionlib_msgs/msg/GoalID](https://docs.ros.org/en/rolling/p/actionlib_msgs/msg/GoalID.html)):
  A request to cancel a specific goal.

#### Published Topics

- `~point_head_action/feedback`
  ([pr2_controllers_msgs/msg/PointHeadActionFeedback](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/PointHeadActionFeedback.html)):
  Feedback describing the progress the mechanism is making on pointing
  the head.
- `~point_head_action/status`
  ([actionlib_msgs/msg/GoalStatusArray](https://docs.ros.org/en/rolling/p/actionlib_msgs/msg/GoalStatusArray.html)):
  Provides status information on the goals that are sent to the action.
- `~point_head_action/result`
  ([pr2_controllers_msgs/msg/PointHeadActionResult](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/PointHeadActionResult.html)):
  empty

### Controller interface

#### Subscribed Topics

- `~state`
  ([pr2_controllers_msgs/msg/JointTrajectoryControllerState](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/JointTrajectoryControllerState.html)):
  Listens to the state of the controller.

#### Published Topics

- `~command`
  ([trajectory_msgs/msg/JointTrajectory](https://docs.ros.org/en/rolling/p/trajectory_msgs/msg/JointTrajectory.html)):
  Sends joint trajectories to the controller.
