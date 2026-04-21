repository: <git://github.com/neobotix/neo_driver>

## Neo Platformctrl Diff

This package implements the diff drive kinematics to control diff drive
platforms by \[neobotix\|neobotix\].

## Topics to publish/subscribe and configuration parameters



```clearsilver
sub {
  0.name = /joint_states
  0.type = sensor_msgs/JointStates
  0.desc = gets the jointstates from the drives
  1.name = /cmd_vel
  1.type = geometry_msgs/Twist
  1.desc = gets the velocity commands.
}
pub {
  0.name = /odom
  0.type = nav_msgs/Odometry
  0.desc = publishes the robots odometry
  1.name = /cmd_joint_traj
  1.type = trajectory_msgs/JointTrajectoryPoint
  1.desc = publishes the motor trajectory
}
param {
  0.name = kinematics
  0.desc = chooses the kinematic model to be used.
  1.name = wheelDiameter
  1.desc = the wheelDiameter in meter.
  2.name = robotWidth
  2.desc = the robots width in meter.
  3.name = sendTransform
  3.desc = should this node send transformations on /tf? [true, false]
}
```


