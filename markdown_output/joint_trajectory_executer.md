A node that sits above the !JointSplineTrajectoryController and provides
an action interface for executing trajectories.

## Action API



```clearsilver
sub {
  0.name=action/goal
  0.type=joint_trajectory_executer/JointTrajectoryActionGoal
  0.desc=A trajectory for the controller to follow.
  1.name=action/cancel
  1.type=actionlib_msgs/GoalID
  1.desc=A request to stop following a particular trajectory.
}
pub {
  1.name= action/status
  1.type= actionlib_msgs/GoalStatusArray
  1.desc= Provides status information on the goals that are sent to the `action` action.
  2.name= action/result
  2.type= action_msgs/JointTrajectoryActionResult
  2.desc= Result is empty for the `action` action.
}
```



## ROS API to the controller



```clearsilver
pub {
  0.name=~controller_command
  0.type=trajectory_msgs/JointTrajectory
  0.desc=Sends goals to the controller.  Connect up to the "command" topic of the controller.
}
sub {
  0.name=~controller_state
  0.type=robot_mechanism_controllers/JointTrajectoryControllerState
  0.desc=Tracks the state of the controller.  Connect up to the "state" topic of the controller.
}
```



## Parameters



```clearsilver
param {
  0.name=joints
  0.type=Array of strings
  0.desc=The joints which the incoming trajectories control
  1.name=constraints/<joint>/goal
  1.type=double
  1.default=-1.0
  1.desc=The tolerance for reaching the goal for the joint named <joint>.  A negative number indicates no constraint.
  2.name=constraints/<joint>/trajectory
  2.type=double
  2.default=-1.0
  2.desc=The tolerance for each point along the trajectory for the joint named <joint>.  A negative number indicates no constraint.
}
```



## Example Roslaunch



```XML
<launch>

  <node pkg="joint_trajectory_executer" type="joint_trajectory_executer" name="r_arm_trajectory_executer">
    <rosparam>
      joints:
        - r_shoulder_pan_joint
        - r_shoulder_lift_joint
        - r_upper_arm_roll_joint
        - r_elbow_flex_joint
        - r_forearm_roll_joint
        - r_wrist_flex_joint
        - r_wrist_roll_joint
    </rosparam>
    <remap from="~controller_command" to="/r_arm_controller/command" />
    <remap from="~controller_state" to="/r_arm_controller/state" />
  </node>

</launch>
```


