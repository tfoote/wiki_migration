## ROS API



```clearsilver
name = kurt_freespace
desc = 
sub {
  0.name = scan
  0.type = sensor_msgs/LaserScan
}
pub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
}
param {
  0.name = max_vel_x
  0.type = double
  0.default = 0.9
  0.desc = The maximum x velocity [m/s].
  1.name = max_rotational_vel
  1.type = double
  1.default = 1.0
  1.desc = The maximum yaw velocity [rad/s].
}
```


