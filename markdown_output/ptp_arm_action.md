## ROS API

### Action Interface

The `ptp_arm_action` node takes a
<<MsgLink(geometry_msgs/PoseStamped)>> from the
`LinearMovementAction` and instructs to robot to move its gripper to
that new location. ```clearsilver
sub {
   0.name = left_ptp, right_ptp (depends on which arm is being used)
   0.type = ptp_arm_actions/LinearMovementActionGoal
   0.desc = Goal for point-to-point movement action.

   1.name = left_ptp, right_ptp (depends on which arm is being used)
   1.type = ptp_arm_actions/LinearMovementActionFeedback
   1.desc = Returns error as a [[http://ros.org/doc/api/geometry_msgs/html/msg/Vector3.html|Vector3]]

   2.name = left_ptp, right_ptp (depends on which arm is being used)
   2.type = ptp_arm_actions/LinearMovementActionGoal
   2.desc = returns error as a [[http://ros.org/doc/api/geometry_msgs/html/msg/Vector3.html|Vector3]]

}

{{{
#!clearsilver CS/NodeAPI
param{
  0.name=translation_tolerance
  0.type=float
  0.desc=Tolerance for translation around goal point.
  1.name=rotation_tolerance
  1.type=float
  1.desc=Tolerance for rotation around goal point.
  2.name=stall_time
  2.type=float
  2.desc=Amount of time allowed for the arm to not make any progress towards goal.
  3.name=timeout
  3.type=float
  3.desc=How long before we should be aborting this motion.
}
```

}}}
