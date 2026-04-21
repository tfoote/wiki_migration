## ROS API

This package provides the `move_arm` node which is a major component
of the arm navigation stack. The node uses ROS services to connect to an
environment server for most of its internal needs: e.g. checking
trajectories and states for collisions, performing inverse kinematics,
talking to controllers, etc.. It communicates with users using an action
interface.

### API Stability

-   The ROS API is REVIEWED but UNSTABLE

### ROS Parameters



```clearsilver
param {
  1.name= ~move_arm_frequency
  1.default= 50.0
  1.type= double
  1.desc= The rate in Hz at which to run the internal state loop for move_arm. This is also the rate at which move_arm will monitor the execution of the planned trajectory.
  2.name= ~group
  2.default= ""
  2.type= string
  2.desc= The name of the group on which move_arm is acting. A group is a collection of joints (and corresponding links). Groups are specified using a yaml file. See [[planning_environment/YAML configuration|planning environment YAML configuration]] for more details on how to specify groups.
  3.name= ~ik_allowed_time
  3.default= 2.0
  3.type= double
  3.desc= The time in seconds that is allowed for IK computation. Move arm will pass this parameter in a service request to the IK node.
  4.name= ~trajectory_filter_allowed_time
  4.default= 2.0
  4.type= double
  4.desc= The time in seconds that is allowed for trajectory filtering. Move arm will pass this parameter in a service request to the trajectory filter server.
  5.name= ~controller_action_name
  5.default= /r_arm_controller/joint_trajectory_action/
  5.type= string
  5.desc= Move arm interfaces to controllers through a simple action client. This parameter specifies the name of the action server corresponding to the controller. 
}
```



### Action API

The `move_arm` node provides an implementation of a
`SimpleActionServer` (see [ actionlib documentation](actionlib )),
that takes in goals containing `move_arm/MoveArmGoal` messages. You
can communicate with the `move_arm` node over ROS directly, but the
recommended way to send goals to `move_arm` if you care about tracking
their status is by using the `SimpleActionClient`. Please see
[ actionlib documentation](actionlib ) for more information.

#### Action Subscribed Topics



```clearsilver
sub {
  no_header= True
  0.name= move_arm/goal
  0.type= move_arm_msgs/MoveArmGoal
  0.desc=A goal for `move_arm` to pursue in the world. 
  1.name= move_arm/cancel
  1.type= actionlib_msgs/GoalID
  1.desc= A request to cancel a specific goal.
}
```



#### Action Published Topics



```clearsilver
pub {
  no_header= True
  0.name= move_arm/feedback
  0.type= move_arm_msgs/MoveArmFeedback
  0.desc= Feedback contains two fields: (a) the current state that the internal move arm state machine is in, (b) time to completion 
  1.name= move_arm/status
  1.type= actionlib_msgs/GoalStatusArray
  1.desc= Provides status information on the goals that are sent to the `move_arm` action. 
  2.name= move_arm/result
  2.type= move_arm_msgs/MoveArmActionResult
  2.desc= It contains an error code that indicates why move arm failed. The error code is of type motion_planning_msgs/ArmNavigationErrorCodes.
}
```



### move_arm required services

Move arm uses service calls to get information about the robot and the
world, compute IK, call planners and do control. It performs minimal
computation within the node itself. The service calls are presented
below categorized according to the type of service they provide.



```clearsilver
 srv{
  group.0{
    name = Utility services
    desc = These are the services that move_arm uses to perform utility functions like figuring out all the joints in a group.
    0.name = get_joints_in_group
    0.type = planning_environment_msgs/GetJointsInGroup
    0.desc = This service allows move_arm to find out which joints belong in a particular group (collection of joints). E.g., the group ''right_arm'' contains the joints:  ''r_shoulder_pan_joint r_shoulder_lift_joint r_upper_arm_roll_joint r_elbow_flex_joint r_forearm_roll_joint r_wrist_flex_joint r_wrist_roll_joint''
    1.name = get_robot_state
    1.type = planning_environment_msgs/GetRobotState
    1.desc = This services allows move_arm to get the complete state of the robot as a [[motion_planning_msgs/RobotState]] message. This message contains information about the joint positions of all the (real) joints on the robot. 
          }
  group.1{
    name = Monitoring/Checking services
    desc = These are the services that move_arm uses to monitor the environment, check the plan that it receives, check whether a goal state has been reached and monitor the safety of a executed trajectory
    0.name = get_environment_safety
    0.type = planning_environment_msgs/GetEnvironmentSafety
    0.desc = This service allows move_arm to determine if the environment is safe for a plan to be generated. This service could be used, for example, to warn the move_arm node that state message have not been received from the robot in a while or that sensor messages are outdated and so information about the environment is invalid. 
    1.name = get_execution_safety
    1.type = planning_environment_msgs/GetJointTrajectoryValidity
    1.desc = This services allows move_arm to determine if the execution of the trajectory is safe. The server node checks for collisions along the part of the trajectory that is yet to be traversed. Internally, it computes the closest state on the trajectory to the current state of the robot and uses this state to compute the part of the trajectory that it still needs to check. 
    3.name = get_trajectory_validity
    3.type = planning_environment_msgs/GetJointTrajectoryValidity
    3.desc = Check if the specified plan is valid, i.e. whether it satisfies the goal and path constraints AND is not in collision at any point along the path.
          }
  group.2{
    name = IK service
    desc = This service allows move_arm to perform inverse kinematics on a particular link on the robot using a particular set of joints
    0.name = arm_ik
    0.type = kinematics_msgs/GetConstraintAwarePositionIK
    0.desc = The service contains the name of the link to perform IK for and the set of joints that should be used in the IK computation.
          }
  group.3{
    name = Planning service
    desc = This is the service that move_arm uses to call a planner to compute motion plans
    0.name = 
    0.type = motion_planning_msgs/GetMotionPlan
    0.desc = The service name is set as part of the !MoveArmGoal message. In addition, when the actual service call is made, the service name is prepended with the ``planner_id`` field provided in the !MoveArmGoal message. 
         }
  group.4{
    name = Filtering service
    desc = This is the service that move_arm uses to filter paths before sending them out to the controller
    0.name = filter_trajectory
    0.type = motion_planning_msgs/FilterJointTrajectoryWithConstraints
    0.desc = Move arm uses this service to filter trajectories. 
         }
  }
```



### move_arm topics



```clearsilver
sub{
  no_header = True
  group.0{
    name = Visualization topics
    desc = These are the topics on which move_arm publishes the planned path and the desired joint goal
    0.name = display_joint_goal
    0.type = motion_planning_msgs/DisplayTrajectory
    0.desc = The desired joint goal that move_arm is trying to move the arm to.
    1.name = display_path
    1.type = motion_planning_msgs/DisplayTrajectory
    1.desc = The planned path that move_arm will move the arm along.
    2.name = allowed_contact_regions_array
    2.type = visualization_msgs/MarkerArray
    2.desc = This is a visual representation of the allowed contacts regions. The allowed contacts regions are regions in space where certain links of the robot may be allowed to touch objects. They are specified by a user within the !MoveArmGoal message.

    }
}
```



## Additional Configuration Details

Additional configuration details are provided on the
[Configuration page](move_arm/Configuration).
