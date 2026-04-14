## Description

This package uses a joystick for teleoperating robots by neobotix.

## Topics/Configuration

```clearsilver
sub {
  0.name = /joy
  0.type = sensor_msgs/Joy
}
pub {
  0.name = /cmd_vel
  0.type = geometry_msgs/Twist
}
param {
  0.name = axis_linear_x
  0.type = int
  0.desc = the joysticks x axis
  1.name = scale_linear_x
  1.type = float
  1.desc = max linear velocity 
  2.name = axis_linear_y
  2.type = int
  2.desc = the joysticks y axis
  3.name = scale_linear_y
  3.type = float
  3.desc = max linear velocity
  4.name = axis_angular_z
  4.type = int
  4.desc = the joysticks w axis
  5.name = scale_angular_z
  5.type = float
  5.desc = max angular velocity
}
```

## Usage/Example

```
roslaunch neo_teleop teleop.launch
```
