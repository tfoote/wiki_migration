## Supported Hardware

The scout_node was only tested on a Nomad Scout 2 robot, however
according to NClient it should work with the following models:

-   Nomad N200;
-   Nomad N150;
-   Nomad Scout;
-   Nomad Scout 2.

## ROS API



```clearsilver
node.0 {
name=scout_node
desc=`scout_node` is a ROS driver for the Nomad Scout 2 robot.
sub{
0.name= cmd_vel
0.type= geometry_msgs/Twist
0.desc= Velocity commands to the robot.
}
pub{
0.name= odom
0.type= nav_msgs/Odometry
0.desc= Odometry data from the robot.
1.name= range
1.type= lse_sensor_msgs/Range
1.desc= Range data from the sonars.
}
param {
0.name= ~port
0.default= /dev/ttyUSB0
0.type= string
0.desc= The port where the robot can be found.
1.name= ~model
1.default= Scout2
1.type= string
1.desc= The model of the robot being used. Accepted models are N200, N150, Scout and Scout2.
}
}
```


