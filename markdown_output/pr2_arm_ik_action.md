![](attachment:ik.png)

```clearsilver
node.0 {
 name = pr2_arm_ik_action
 desc << EOM  
`pr2_arm_ik_action` action is uses the [[joint_trajectory_action]] to move the wrist roll link to a desired pose.
EOM
 goal{
  0.name= <~arm>_arm_ik/goal
  0.type= pr2_common_action_msgs/ArmMoveIKGoal
  0.desc= This is the desired pose of the wrist roll link.
  }
 result{
  0.name= <~arm>_arm_ik/result
  0.type= pr2_common_action_msgs/ArmMoveIKResult
  0.desc= This returns the location where the plug was found in the gripper.
  }
 act_called {
  0.name= <~arm>_arm_controller/<~joint_trajectory_action>
  0.type= joint_trajectory_action
  0.desc= This action moves the arm to a joint configuration.
 }
 param {
  0.name= ~arm
  0.default= r
  0.type= string
  0.desc= Which arm to control (l or r).
  1.name= ~joint_trajectory_action
  1.default= r_arm_controller/joint_trajectory_action
  1.type= string
  1.desc= The namespace of the joint trajectory action to send trajectories to.
  2.name= ~free_angle
  2.default= 2
  2.type= int
  2.desc= Since the PR2 arms are redundant (they have 7 DOF), there are an infinite number of joint space configurations that satisfy a given Cartesian end effector pose. The ik solver will compute a joint space solution solution for every value of the "free angle" joint, and the valid solution that is closest to the seed configuration in the goal is chosen.
  3.name= ~search_discretization
  3.default= 0.01 rad
  3.type= double
  3.desc= The search step size for the "free angle" joint. 
  4.name= ~ik_timeout
  4.default= 5.0 sec
  4.type= double
  4.desc= The timeout on the ik solver. The action will fail if no valid solution is found withing this duration.
 }
}
```

Example launch file :

```
<launch>
  <!-- ik action -->
  <node pkg="pr2_arm_ik_action" type="arm_ik" name="r_arm_ik" output="screen">
    <param name="joint_trajectory_action" value="joint_trajectory_generator" />
    <param name="arm" value="r" />
    <param name="free_angle" value="2" />
    <param name="search_discretization" value="0.01" />
    <param name="ik_timeout" value="5.0" />
  </node>

  <!-- Trajectory generator -->
  <node pkg="joint_trajectory_generator" type="joint_trajectory_generator" output="screen"
        name="joint_trajectory_generator" ns="r_arm_controller" >
    <param name="max_acc" value="2.0" />
    <param name="max_vel" value="2.5" />
  </node>
</launch>
```
