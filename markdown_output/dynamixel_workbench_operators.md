*ROS Software Maintainer: [ROBOTIS](http://wiki.ros.org/ROBOTIS)*

## ROBOTIS e-Manual

- [ROBOTIS e-Manual for Dynamixel-Workbench](http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/)

## ROS API



```clearsilver
node.0 {
name= joint_operator

srv{
  0{
    name= joint_command
    type= dynamixel_workbench_msgs/JointCommand
    desc= Send commands(id and goal_position) to move the Dynamixel
  }
}
```





```clearsilver
node.0 {
name= wheel_operator

srv{
  0{
    name= wheel_command
    type= dynamixel_workbench_msgs/WheelCommand
    desc= Send commands(right_vel and left_vel) to move the Dynamixels
  }
}
```



## Tutorials

- [dynamixel workbench operator tutorials](https://index.ros.org/p/dynamixel_workbench_controllers) -
  This tutorial describes how to run controllers with tutorial packages.
