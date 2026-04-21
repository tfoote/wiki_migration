## ROS API



```clearsilver
node.0 {
name=pose_estimation
desc=`pose_estimation` is a node for estimating the 6DOF of a robot based on the EKF of various sensor sources.

sub{
0.name= fix
0.type= sensor_msgs/NavSatFix
0.desc= GPS data.
1.name= raw_imu
1.type= Sensor_msgs/Imu
1.desc= Raw IMU data.
2.name= syscommand
2.type= std_msgs/String
2.desc= System command. If the string equals "reset" the map and robot pose are reset to their initial state.
3.name= magnetic
3.type= geometry_msgs/Vector3Stamped
3.desc= Magnetic orientation.
4.name= pressure_height
4.type= geometry_msgs/PointStamped
4.desc= Altitude from barometric pressure.
5.name= fix_velocity
5.type= geometry_msgs/Vector3Stamped
5.desc= Velocities from GPS data (North = x, East = y).
6.name= twistupdate
6.type= geometry_msgs/TwistWithCovarianceStamped
6.desc= Twist update.
7.name= poseupdate
7.type= geometry_msgs/PoseWithCovarianceStamped
7.desc= Estimated robot pose with a gaussian estimate of uncertainty.
}

pub{
   0{
    name = pose
    type = geometry_msgs/PoseStamped
    desc = Estimated pose of the robot based on the sensor fusing.
   }
   1{
    name = velocity
    type = geometry_msgs/Vector3Stamped
    desc = X, Y and Z velocities of the robot. 
   }
   2{
    name= state
    type= nav_msgs/Odometry
    desc= Odometry computed based on robot's sensors.
   }
   3{
    name= fix/pose
    type= geometry_msgs/PoseStamped
    desc= The estimated robot pose based on the GPS data.
   }
   4{
    name= imu
    type= sensor_msgs/Imu
    desc= Filtered IMU data.
   }
   5{
    name= angular_velocity_bias
    type= geometry_msgs/Vector3Stamped
    desc= TBD
   }
   6{
    name= tf
    type= tf2_msgs/TFMessage
    desc= TBD
   }
   7{
    name= linear_acceleration_bias
    type= geometry_msgs/Vector3Stamped
    desc= TBD
   }
   8{
    name= global
    type= sensor_msgs/NavSatFix
    desc= Global GPS coordinates.
   }
   9{
    name= euler
    type= geometry_msgs/Vector3Stamped
    desc= Euler angles.
   }
}
```


