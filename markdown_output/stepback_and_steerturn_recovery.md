## Overview

The \`stepback_and_steerturn_recovery::StepbackAndSteerturnRecovery\` is
designed for a robot with a car-like steering mechanism. It adheres to
the \`nav_core::RecoveryBehavior\` interface found in the
[nav_core](nav_core) package and can be used as a recovery behavior
[ plugin](pluginlib ) for the [move_base](move_base) node.

## Flow of Recovery

The recovery behavior attempts to clear out space with a flow as
follows:

1\. A robot stucks, which disable the robot turn in any direction. 2.
Step back for space to turn with steering. 3. Scan the navigation
stack\'s [ costmaps](costmap_2d ) at the point where the robot stepped
back. 4. Detect the direction to the nearest obstacle and attempts to
turn in the opposite direction.

![stepback_and_steerturn_recovery\|width=\"700\"](attachment:stepback_and_steerturn_recovery.png)

The plugin frequently check if there is a obstacle in the proceeding
direction during recovery for protection of a robot. Detecting an
obstacle at a close point to the robot make it brake and invoke local
planning at the brake point.

### ROS API

```clearsilver
pub {
  0.name= recover_run
  0.type= Type: std_msgs::Bool
  0.desc= Notification of recovery status. True when recovery is running, False otherwise. 
}
```

#### StepbackAndSteerturnRecovery Parameters

```clearsilver
param {
  no_header=True
  0.name = ~<name>/only_single_steering
  0.default = false
  0.type = bool 
  0.desc = True if you want to invoke just once turn.
  1.name = ~<name>/trial_times
  1.default = 3
  1.type = int
  1.desc = The number of trial to recover.
  2.name = ~<name>/obstacle_patience
  2.default = 0.3
  2.type = double
  2.desc = Tolerance distance [m] to obstacle．
  3.name = ~<name>/obstacle_check_frequency
  3.default = 5.0
  3.type = double
  3.desc = Frequency to check obstacle during recovery.
  4.name = ~<name>/sim_angle_resolution
  4.default = 0.1
  4.type = double
  4.desc = Resolution of angle [rad] to check costmap for obstacle detection. Decrease this parameter to reduce the number of access to costmap for computation efficiency.
  5.name = ~<name>/simulation_frequency
  5.default = 5
  5.type = int
  5.desc = Forward simulation frequency on obstacle detection. Decrease this parameter to reduce the number of access to costmap for computation efficiency.
  6.name = ~<name>/linear_vel_back
  6.default = -0.3
  6.type = double
  6.desc = Velocity of stepback [m/s].
  7.name = ~<name>/step_back_length
  7.default = 1.0
  7.type = double
  7.desc = Length of stepback [m].
  8.name = ~<name>/step_back_timeout
  8.default = 15.0
  8.type = double
  8.desc = Timeout [sec] of stepback.
  9.name = ~<name>/linear_vel_steer    
  9.default = 0.3
  9.type = double
  9.desc = Linear velocity [m/s] during turn recovery.
 10.name = ~<name>/angular_speed_steer
 10.default = 0.3
 10.type = double
 10.desc = Angular speed [rad/s] during turn recovery.
 11.name = ~<name>/steering_timeout    
 11.default = 15.0
 11.type = double
 11.desc = Timeout [sec] of turn recovery.
 12.name = ~<name>/linear_vel_forward  
 12.default = 0.3
 12.type = double
 12.desc = Linear velocity [m/s] of proceeding recovery after the first turning one.
 13.name = ~<name>/step_forward_length 
 13default = 1.0
 13.type = double
 13.desc = Length of proceeding recovery after the first turning one.
 13.name = ~<name>/step_forward_timeout
 13default = 15.0
 13.type = double
 13.desc = Timeout of proceeding recovery after the first turning one.
}
```

#### TrajectoryPlannerROS Parameters

### C++ API

The C++ \`rotate_recovery::RotateRecovery\` class adheres to the
\`nav_core::RecoveryBehavior\` interface found in the
[nav_core](nav_core) package. For detailed documentation, please see
[ RotateRecovery documentation](http://www.ros.org/doc/api/rotate_recovery/html/classrotate__recovery_1_1RotateRecovery.html ).
