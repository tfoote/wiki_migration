## Overview

This component is doing interpolation between two sequential points
specified by
[trajectory_msgs/msg/JointTrajectoryPoint](https://docs.ros.org/en/rolling/p/trajectory_msgs/msg/JointTrajectoryPoint.html)
message. It output
[oro_servo_msgs/msg/Setpoints](https://docs.ros.org/en/rolling/p/oro_servo_msgs/msg/Setpoints.html)
message containing position, velocity and acceleration for current
interpolation point.

Interpolation type depend on which data was supplied by
[trajectory_msgs/msg/JointTrajectoryPoint](https://docs.ros.org/en/rolling/p/trajectory_msgs/msg/JointTrajectoryPoint.html)
message:

position and time - linear interpolation.

position, velocity and time - cubic spline interpolation.

position, velocity, acceleration and time - quintic spline
interpolation.

## OROCOS API

### Input ports



```clearsilver
param {
  no_header= True
  0.name= cmdJntPos
  0.type= vector<double>
  0.desc= Desired position of joint.
}
sub {
  no_header= True
  0.name= trajectory_point
  0.type= trajectory_msgs/JointTrajectoryPoint
  0.desc=Next point for interpolation.
}
```



### Output ports



```clearsilver
param {
  no_header= True
  0.name= dsrJntPos
  0.type= vector<double>
  0.desc=New setpoint for servo.
  1.name= buffer_ready
  1.type= bool
  1.desc=Indicate that component is ready to receive next interpolation point.
}
```



### Properties



```clearsilver
param {
  no_header= True
  0.name= number_of_joints
  0.type= int
  0.desc=Number of joints used in interpolation.
}
```


