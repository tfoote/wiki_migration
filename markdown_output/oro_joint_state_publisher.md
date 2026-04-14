## OROCOS API

### Input ports

```clearsilver
sub {
  no_header= True
  0.name= msrJntPos
  0.type= vector<double>
  0.desc=Measured position of joints. 
}
```

### Output ports

```clearsilver
pub {
  no_header= True
  0.name= joints_state
  0.type= sensor_msgs/JointState
  0.desc=Joint state information for ROS. 
}
```

### Properties

```clearsilver
param {
  no_header= True
  0.name= number_of_joints
  0.type= int
  0.desc=Number of joints that will be handled by joint_state_publisher.

  1.name= jointX_name
  1.type= string
  1.desc=ROS name of X joint.
}
```
