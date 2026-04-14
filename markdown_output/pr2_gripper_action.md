![](attachment:gripper_action_topics.png)

Users interested in grasping more delicate objects may want to checkout
the alternative [pr2_gripper_sensor_action](pr2_gripper_sensor_action)
package.

## Usage

You can see an example of using the pr2 gripper action on the PR2 in the
[Moving the Gripper tutorial](pr2/Tutorials/Moving the gripper).

## ROS API

The ROS API consists of three parts: private parameters, an action
server that achieves gripper goals, and an interface to the gripper
controller.

The [Moving the Gripper tutorial](pr2/Tutorials/Moving the gripper)
provides more context on how the
[action and controller are launched](pr2/Tutorials/Moving the gripper#The_gripper_action_and_trajectory_controller)
and how
[action goals are interpreted](pr2/Tutorials/Moving the gripper#The_action_goal).

### Parameters

```clearsilver
param {
  0.name=~goal_threshold
  0.type=double
  0.desc=The distance from the desired position at which the result is considered successful.
  0.default=0.01
  1.name=~stall_timeout
  1.type=double
  1.default=0.1
  1.desc=The amount of time (in seconds) the joint must be stationary to be considered a stall.
  2.name=~stall_velocity_threshold
  2.type=double
  2.default=1e-6
  2.desc=Parameter used when stall velocity oscillates (e.g. simulation jitter).
}
```

### Action interface

```clearsilver
sub {
  0.name=~gripper_action/goal
  0.type=pr2_controllers_msgs/Pr2GripperCommandActionGoal
  0.desc=The position/force for the gripper to achieve.
  1.name=~gripper_action/cancel
  1.type=actionlib_msgs/GoalID
  1.desc=A request to stop trying to move the gripper.
}
pub {
  1.name= ~gripper_action/status
  1.type= actionlib_msgs/GoalStatusArray
  1.desc= Provides status information on the goals that are sent to the `action` action.
  2.name= ~gripper_action/result
  2.type= pr2_controllers_msgs/Pr2GripperActionResult
  2.desc= Describes why the gripper stopped (stalled or reached the final position).
}
```

### Controller interface

```clearsilver
sub {
  0.name=~state
  0.type=pr2_controllers_msgs/JointControllerState
  0.desc=Listens to the state of the controller.
}
pub {
  0.name=~command
  0.type=pr2_controllers_msgs/Pr2GripperCommand
  0.desc=Sends grip commands to the controller.
}
```
