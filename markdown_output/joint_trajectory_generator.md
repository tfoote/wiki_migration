![](attachment:trapezoid.png) Image source: Herman Bruyninckx, Motion
Interpolation

```clearsilver
node.0 {
 name = joint_trajectory_generator
 desc << EOM  
`joint_trajectory_generator` action takes in a trajectory specified by a number of joint positions, and it generates a new smooth trajectory through these joint positions. The smooth trajectory is created by limiting the joint velocity and acceleration to specified maximal values. The generated trajectory can have a longer duration than the input trajectory if the input trajectory could only be executed with joint velocities and accelerations that exceed the specified maximal values. The generated trajectory will however never have a shorter duration than the input trajectory.
<<BR>> <<BR>>
The action sends its output to the [[joint_trajectory_action]], to execute the smooth trajectory it generated.
EOM
 goal{
  0.name= joint_trajectory_generator/goal
  0.type= pr2_controllers_msgs/JointTrajectoryGoal
  0.desc= The goal contains the 'rough' trajectory that is only specified by a sequence of desired joint positions.
  }
 result{
  0.name= joint_trajectory_generator/result
  0.type= pr2_controllers_msgs/JointTrajectoryResult
  0.desc= The result indicates if the trajectory was executed successfully.
  }
 act_called {
  0.name= joint_trajectory_action
  0.type= joint_trajectory_action
  0.desc= This action moves the arm to a joint configuration.
 }
 param{
  0.name= ~max_acc
  0.type= float64
  0.desc= The maximum allowed acceleration of a joint. The generated trajectory will never make a joint accelerate faster than this value.
  1.name = ~/max_vel
  1.type = float64
  1.desc = The maximum allowed velocity of a joint. The generated trajectory will never make a joint move faster than this value.
  2.name = robot_description
  2.type = string
  2.desc = The [[urdf]] robot description. This is used to know if a joint is continuous or rotational.
}
```
