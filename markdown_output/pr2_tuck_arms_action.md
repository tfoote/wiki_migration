![](attachment:tuckarm.jpg)



```clearsilver
node.0 {
 name = pr2_tuck_arm_action
 desc << EOM  
`pr2_tuck_arm_action` action uses the [[joint_trajectory_action]] to tuck and untuck the PR2's arms. Tucked arms allow the PR2 to navigate without obstructing its own view.

EOM
 goal{
  0.name= tuck_arms/goal
  0.type= pr2_common_action_msgs/TuckArmsGoal
  0.desc= This message specifies with arm(s) to (un)tuck. 
  }
 result{
  0.name= tuck_arms/result
  0.type= pr2_common_action_msgs/TuckArmsResult
  0.desc= Empty result message. The action status provides information on success/failure.
  }
 act_called {
  0.name= r_arm_controller/<~joint_trajectory_action> and l_arm_controller/<~joint_trajectory_action>
  0.type= joint_trajectory_action
  0.desc= This action moves the arm to a joint configuration.
 }
 param {
  0.name= ~r_joint_trajectory_action
  0.default= r_arm_controller/joint_trajectory_action
  0.type= string
  0.desc= The namespace of the right arm joint trajectory action to send trajectories to.
  1.name= ~l_joint_trajectory_action
  1.default= l_arm_controller/joint_trajectory_action
  1.type= string
  1.desc= The namespace of the left arm joint trajectory action to send trajectories to.
  2.name= ~move_duration
  2.default= 2.5 seconds
  2.type= float
  2.desc= The duration of each trajectory segment that is executed by tuck arms. If you use a trajectory generator, you can set this value to zero to achieve the maximum possible speed.
 }
}
```



### Examples

For a running ROS system with a PR2 robot the following terminal command
can be written to tuck the arms
` rosrun pr2_tuck_arms_action tuck_arms.py -lt `

See [tucking arms video](http://vimeo.com/57923959)
