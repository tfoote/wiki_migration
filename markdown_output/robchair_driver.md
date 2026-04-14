## ROS API

```clearsilver
node.0 {
name=robchair_node
desc=`robchair_node` is the hardware driver for the robchair robot. It subscribes to velocity commands and publishes the robot's odometry.
sub{
0.name= cmd_vel
0.type= geometry_msgs/Twist
0.desc= Velocity commands to the robot.
}
pub{
0.name= odom
0.type= nav_msgs/Odometry
0.desc= Odometry readings from the robot.
}
param {
0.name= kp
0.default= 0
0.type= double
0.desc= Kp gain for the motor drives. If set to 0 default values are used.
}
param {
1.name= ki
1.default= 0
1.type= double
1.desc= Ki gain for the motor drives. If set to 0 default values are used.
}
}
```

## Tutorials

All the robchair tutorials can be found on the
[robchair_robot](robchair_robot) wiki page.
