## Nodes



```clearsilver
node.0 {
name = revel_driver
desc = The revel driver is responsible for communicating and interfacing between the motors and ROS. The driver can be run in several modes, including position, velocity and gravity control mode. Use cases for these modes are trajectory playback, cartesian velocity and kinesthetic teaching respectively.
sub {
0.name = /joint_states
0.type = sensor_msgs/JointState
0.desc = Standardized joint state information used to inform `tf`, `moveit`, etc.
}
pub {
0.name = /revel/motor_state
0.type = svenzva_msgs/MotorStateList
0.desc = Raw motor state information collected directly from motor packets.
1.name = /svenzva_joint_action/
1.type = svenzva_msgs/SvenzvaJointAction
1.desc = A forward kinematics joint action interface.
2.name = /revel/follow_joint_trajectory
2.type = control_msgs/FollowJointTrajectoryAction
2.desc = A trajectory playback action interface for MoveIt! and compliant controllers.
3.name = /revel/gripper_action/
3.type = svenzva_msgs/GripperAction
3.desc = A gripper action interface used to open and close the Revel gripper.
}
srv { 
0.name = /home_arm_service
0.type = svenzva_msgs/HomeArmService
0.desc = commands the arm to the __all-zero__ configuration
1.name = /revel/SetTorqueEnable
1.type = svenzva_msgs/SetTorqueEnable
1.desc = commands individual joints to enable or disable torque actuation without turning off the motor
2.name = /revel/gripper/insert_finger
2.type = svenzva_msgs/HomeArmService
2.desc = resets finger position in model. Useful when hot-swapping for fingers of a different size or shape

}
param {
0.name = ~data_frequency
0.type = int
0.desc = The frequency (Hz) that state information is gathered from the arm's motors. Stable maximum is 100 Hz.
0.default = 50
1.name = ~mode
1.type = str
1.desc = The initial, internal mode of the arm motors set in the `svenzva_bringup.launch` file. Possible values are `user_defined`, `velocity` and `gravity`. 
1.default = `user_defined` (position control)
}
}
```





```clearsilver
node.0 {
name = revel_dynamic_model
desc = The revel dynamic model uses the current position of the robot along with an internal model of the arms dynamics to estimate the amount of force required to hold the arm up at that position against gravity. This module is required for `gravity` mode.
sub {
0.name = /joint_states
0.type = sensor_msgs/JointState
0.desc = Standardized joint state information used to inform `tf`, `moveit`, etc.
}
pub {
0.name = /revel/model_efforts
0.type = sensor_msgs/JointState
0.desc = Estimated torque information for each motor given the current position of the arm.
}

}
```


