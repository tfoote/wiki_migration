## Nodes



```clearsilver
node {
 0{
 name = elektron_base_node
 desc = `elektron_base_node` controls Elektron mobile robot (set wheel speeds), retrieves and calculates odometry.
 param{
  0{
  name = ~device
  type = string
  default = `/dev/protonek`
  desc = Linux USB device from which to read the data.
  }
  1{
  name = ~publish_odom_tf
  type = bool
  default = `False`
  desc = Whether to publish or not odometry transform
  }
  2{
  name = ~lin_scale
  type = double
  default = 1.0
  desc = Linear scaling factor for correct odometry
  }
  3{
  name = ~rot_scale
  type = double
  default = 1.0
  desc = Angular scaling factor for correct odometry
  }
 }
 pub{
  0{
  name = ~odom
  type = nav_msgs/Odometry
  desc = The odometry of the robot based on the wheel movement
  }
 } 
 sub{
  0{
  name = ~cmd_vel
  type = geometry_msgs/Twist
  desc = Desired robot speed
  }
 }
 prov_tf{
  0{
    from = odom
    to = base_link
    desc = the pose of the robot base in the odom frame. Only provided when `publish_odom_tf` is enabled.
  }
```


