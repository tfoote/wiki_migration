## Overview

This package contains an implementation of an action that will attempt
to follow desired trajectories in a collision free manner, i.e. the
action will execute desired trajectories but abort them if there is a
possibility of a collision. The action has a simple action client
interface, similar to the interface for the !JointTrajectoryAction. If
the first point in the desired trajectory is far away from the current
state of the robot, the action will create a trajectory segment between
the current state of the robot and the first point in the trajectory.
This trajectory segment will obey velocity and acceleration limits
specified in the filter yaml configuration. The action will then attempt
to follow the rest of the desired trajectory as best as it can without
filtering it, i.e. the onus is on the user to provide a trajectory that
the action will be able to follow.

## ROS API

### API Stability

-   The ROS API is UNREVIEWED and UNSTABLE

#### Action API

The collision_free_arm_trajectory_controller node provides an
implementation of a `SimpleActionServer` (see
[ actionlib documentation](actionlib )), that takes in goals containing
`pr2_controllers_msgs/JointTrajectoryAction` messages. The recommended
way to send goals to this node if you care about tracking their status
is by using the `SimpleActionClient`. Please see
[ actionlib documentation](actionlib ) for more information. Also, see
the [tutorials](collision_free_arm_trajectory_controller/Tutorials) for
this package for a better idea on how to use the interface.

##### Action Subscribed Topics

```clearsilver
sub {
  no_header= True
  0.name= [collision_free_arm_trajectory_action_]+group_name/goal
  0.type= pr2_controllers_msgs/JointTrajectoryGoal
  0.desc= The desired trajectory for the controller to follow. 
  1.name= [collision_free_arm_trajectory_action_]+group_name/cancel
  1.type= actionlib_msgs/GoalID
  1.desc= A request to cancel a specific trajectory.
}
```

##### Action Published Topics

```clearsilver
pub {
  no_header= True
  0.name= [collision_free_arm_trajectory_action_]+group_name/feedback
  0.type= pr2_controllers_msgs/JointTrajectoryFeedback
  0.desc= Feedback is empty
  1.name= [collision_free_arm_trajectory_action_]+group_name/status
  1.type= actionlib_msgs/GoalStatusArray
  1.desc= Provides status information on the goals that are sent to the action. 
  2.name= [collision_free_arm_trajectory_action_]+group_name/status
  2.type= pr2_controllers_msgs/JointTrajectoryActionResult
  2.desc= Result contains information about the status of the controller when its done. 
}
```

```clearsilver
param {
  2.name= ~group_name
  2.default= ""
  2.type= string
  2.desc= The name of the group on which the node is acting. A group is a collection of joints (and corresponding links). Groups are specified using a yaml file. See [[planning_environment/YAML configuration|planning environment YAML configuration]] for more details on how to specify groups.
  5.name= ~traj_action_name
  5.default= /r_arm_controller/joint_trajectory_action/
  5.type= string
  5.desc= This node interfaces to controllers through a simple action client. This parameter specifies the name of the action server corresponding to the controller. 

}
```

```clearsilver
srv {
    1.name = get_execution_safety
    1.type = planning_environment_msgs/GetJointTrajectoryValidity
    1.desc = This services allows the node to determine if the execution of the trajectory is safe. The server node checks for collisions along the part of the trajectory that is yet to be traversed. Internally, it computes the closest state on the trajectory to the current state of the robot and uses this state to compute the part of the trajectory that it still needs to check.
    2.name = get_robot_state
    2.type = planning_environment_msgs/GetRobotState
    2.desc = This services allows the node to get the complete state of the robot as a [[motion_planning_msgs/RobotState]] message. This message contains information about the joint positions of all the (real) joints on the robot. 
    0.name = filter_trajectory
    0.type = motion_planning_msgs/FilterJointTrajectory
    0.desc = The action uses this service to filter trajectories if required. If the first point in the desired trajectory is far away from the current state of the robot, the action will use this service to create a trajectory segment between the current state of the robot and the first point in the trajectory. This trajectory segment will obey velocity and acceleration limits specified in the filter yaml configuration. The action will then attempt to follow the rest of the desired trajectory as best as it can without filtering it, i.e. the onus is on the user to provide a trajectory that the action will be able to follow.

}
```

## Additional Configuration Details

Additional configuration details are provided on the
[collision_free_arm_trajectory_controller/Configuration](collision_free_arm_trajectory_controller/Configuration)
page.
