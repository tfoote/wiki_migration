## Documentation

To start the WheeledRobin in a faked odometry mode the \'\_fake\' launch
files in wheeled_robin_bringup.

## Nodes

```clearsilver
name = wheeled_robin_node
desc = This node simulates a robot by summing up cmd_vel commands and publishing a faked perfect odometry of the robot. No physical calculations are done.
sub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Desired velocity for !WheeledRobin (x, theta)
}
pub {
  0.name = odom
  0.type = nav_msgs/Odometry
  0.desc = Odometry of !WheeledRobin.
  1.name = joint_states
  1.type = sensor_msgs/JointState
  1.desc = Joint State for the left and right wheel.
}
prov_tf {
  0.from = odom
  0.to   = base_footprint
  0.desc = Depends on the odometry of !WheeledRobin
  1.from = base_footprint
  1.to   = base_link
  1.desc = Depends on the pitch angle of !WheeledRobin which is estimated proportional to the linear velocity.
}
```
