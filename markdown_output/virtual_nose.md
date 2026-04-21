## ROS API



```clearsilver
node.0 {
name=virtual_nose_node
desc=`virtual_nose_node` is a wrapper for the [[plumesim]] service [[http://www.ros.org/doc/api/plumesim/html/srv/ReadPlumeSim.html|plumesim/ReadPlumeSim]]. It subscribes to the robot's odometry and polls the service for the chemical readings for posterior publish thus mimicking a nose node.
sub{
0.name= odom
0.type= nav_msgs/Odometry
0.desc= The robot's odometry.
}
pub{
0.name= nose
0.type= lse_sensor_msgs/Nostril
0.desc= Chemical data from [[plumesim]].
}
srv_called{
0.name= read_plumesim
0.type= plumesim/ReadPlumeSim
0.desc= `virtual_nose_node` calls this service to get the chemical data from the robot's current position.
}
param {
2.name= ~frame_id
2.default= /base_nose
2.type= string
2.desc= The frame in which nose readings will be returned.
}
}
```



## Tutorials

virtual_nose was designed to work with [plumesim](plumesim). You can
find a tutorial on how to use virtual_nose on the
[ PlumeSim Tutorials page ](plumesim/Tutorials ).
