## ROS API



```clearsilver
node.0 {
name=corobot_state_tf
desc=`corobot_state_tf` is a package that calculate the odometry of a Corobot using the encoders data.
sub{
0.name= position_data
0.type= corobot_msgs/PosMsg
0.desc= Encoders data
}
pub{
0.name= odometry
0.type= nav_msgs/Odometry
0.desc= Odometry information
}
param{
0.name= Explorer
0.default = false
0.desc= Defines if the robot is a Corobot Explorer or a Corobot classic
0.type= bool
0.name= Corobot4WD
0.default = false
0.desc= True if the robot is a Corobot CL4. If not, we assume it is a CL2. 
0.type= bool
1.name= publish_odom_tf
1.default = true
1.desc= Choose to publish or not the tf transform message from odom to base_footprint
1.type= bool
}
prov_tf{
0.from= odom
0.to= base_footprint
0.desc= the estimate of the robot's pose
1.from= base_footprint
1.to= base_link
1.desc= Nul transform. necessary for some applications
2.from= base_link
2.to= laser
2.desc= Fixed transform from the center of the robot to the laser range finder
}
}
}
```


