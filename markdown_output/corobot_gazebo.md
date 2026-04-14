## Description

This package is intended to be executed with Gazebo when trying to
simulate the Corobot. This node will provide all the interface to use
the simulated Corobot like a real one.

See [corobot_urdf](corobot_urdf) for launching the simulation

## ROS API

```clearsilver
node.0 {
name=corobot_gazebo_control
desc=This node will provide all the interface to use the simulated Corobot like a real one.
pub{
0.name= corobot_left_rear_wheel_controller/command
0.type= std_msgs/Float64
0.desc= command the left rear wheel of the simulated robot
1.name= corobot_right_rear_wheel_controller/command
1.type= std_msgs/Float64
1.desc= command the right rear wheel of the simulated robot
2.name= corobot_left_front_wheel_controller/command
2.type= std_msgs/Float64
2.desc= command the left front wheel of the simulated robot
3.name= corobot_right_front_wheel_controller/command
3.type= std_msgs/Float64
3.desc= command the right front wheel of the simulated robot
4.name= odometry
4.type= nav_msgs/Odometry
4.desc= the odometry message
}
sub{
0.name= PhidgetMotor
0.type= corobot_msgs/MotorCommand
0.desc= Speed command for the simulated Corobot
1.name= /gazebo/model_states
1.type= corobot_gazebo/ModelStates
1.desc= The state of the robot returned by Gazebo
2.name= lwheel_vtarget
2.type= std_msgs/Float32
2.desc= Left wheel velocity. To be used by PID when controlling the velocity with twist
3.name= rwheel_vtarget
3.type= std_msgs/Float32
3.desc= Right wheel velocity. To be used by PID when controlling the velocity with twist
}

}
```
