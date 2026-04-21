

```clearsilver
param {
  0.name=pan_link
  0.type=string
  0.desc=Name of the pan link
  0.default=Required
  1.name=tilt_link
  1.type=string
  1.desc=Name of the tilt link
  1.default=Required
}
sub {
  0.name=point_head
  0.type=geometry_msgs/PointStamped
  0.desc=The location to point the head at.
  1.name=command
  1.type=sensor_msgs/JointState
  1.desc=A desired set of joint positions
}
```


