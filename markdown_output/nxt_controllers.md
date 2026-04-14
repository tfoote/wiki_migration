## ROS API description

```clearsilver
node.0 {
name=nxt_base_controller
desc=`nxt_base_controller` provides a controller for a basic differential drive vehicle (i.e. a car). 
pub{
0.name= ~joint_command
0.type= nxt_msgs/JointCommand
0.desc= Effort commands to move the motors.
}
sub{
0.name= ~joint_states
0.type= sensor_msgs/JointState
0.desc= The current effort, position, and velocity of the servo motors.
1.name= ~cmd_vel
1.type= geometry/Twist
1.desc= The desired linear and angular x,y,z of the base.
}
param{
1.name= ~base_parameters/r_wheel_joint
1.default=None
1.type= string
1.desc= The name of the right wheel joint.
2.name= ~base_parameters/l_wheel_joint
2.default=None
2.type= string
2.desc= The name of the left wheel joint.
3.name= ~base_parameters/wheel_radius
3.default=0.022
3.type= double
3.desc= The radius of the Lego wheel, this assumes both wheels have the same radius.
4.name= ~base_parameters/wheel_basis
4.default=0.055
4.type= double
4.desc= The distance from the center of each wheel divided by 2. 
5.name= ~base_parameters/vel_to_eff
5.default=0.55
5.type= double
5.desc= The ratio of the output velocity to the commanded effort. 
}
}
node.1 {
name=nxt_base_odometry
desc=`nxt_base_odometry` provides odometry for a basic differential drive vehicle (i.e. a car). 
pub{
0.name= ~odom
0.type= nav_msgs/Odometry
0.desc= The change in position over time in the fixed frame.
}
sub{
0.name= ~joint_states
0.type= sensor_msgs/JointState
0.desc= The current effort, position, and velocity of the servo motors.
}
param{
1.name= ~base_parameters/r_wheel_joint
1.default=None
1.type= string
1.desc= The name of the right wheel joint.
2.name= ~base_parameters/l_wheel_joint
2.default=None
2.type= string
2.desc= The name of the left wheel joint.
3.name= ~base_parameters/wheel_radius
3.default=0.022
3.type= double
3.desc= The radius of the Lego wheel, this assumes both wheels have the same radius.
4.name= ~base_parameters/wheel_basis
4.default=0.055
4.type= double
4.desc= The distance from the center of each wheel divided by 2. 
}
}
```
