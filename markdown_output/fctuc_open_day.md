## Demo Description

This package was created for the FCTUC open day demo. The demo consisted
on 2 Roombas equipped with Hokuyo lasers wandering inside and around a
small arena while taking chemical measurements of the environment.

## ROS API



```clearsilver
node.0 {
name= demo
desc= The node that runs the actual demo.
pub{
0.name= cmd_vel
0.type= geometry_msgs/Twist
0.desc= Velocity commands to the Roomba.
}
sub{
1.name= nose
1.type= lse_sensor_msgs/Nostril
1.desc= Chemical data from the LSE MOX nose.
2.name= battery
2.type= roomba_500_series/Battery
2.desc= Roomba battery data to check battery level and if the Roomba is docked.
3.name= poses
3.type= fctuc_open_day/Poses
3.desc= Array of goal poses.
}
}
node.1 {
name= pose_reader
desc= Reads a file containing poses for the robot and publishes them for the demo node to run.
pub{
0.name= poses
0.type= fctuc_open_day/Poses
0.desc= Array of goal poses.
}
}
```


