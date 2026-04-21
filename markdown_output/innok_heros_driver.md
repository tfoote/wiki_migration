ROS driver for the [Innok Heros](Robots/Innok-Heros) robot plattform.

{

Make sure that the `host` parameter in `heros_base.launch` is set to
the correct address of your Heros (default host is 192.168.1.213).

## Nodes



```clearsilver
node.1 {
 name = heros_driver
 desc = driver for the Innok Heros robot platform
 pub {
  0.name= odom
  0.type= nav_msgs/Odometry
  0.desc= odometry data of the robot
 }
sub {
  1.name= cmd_vel
  1.type= geometry_msgs/Twist
  1.desc= velocity commands for the platform
}
param {
  0.name = host
  0.type = string
  0.desc = host address of the robot
  0.default = "192.168.1.213"
 }
}
prov_tf{
  0{
    from = odom
    to = base_link
    desc = the current estimate of the robot's pose within the odom frame
  }
 }
```



}}}}
