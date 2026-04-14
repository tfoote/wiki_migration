## Nodes

### safe_trajectory_node

This node takes as input commands for a robot base and outputs the
nearest safe commands. The core functionality has some similarities to
[base_local_planner](base_local_planner).

```clearsilver
pub {
  0.name= ~<name>/safe_vel
  0.type= geometry_msgs/Twist
  0.desc= Safe base commands
  1.name= ~<name>/user_plan
  1.type= nav_msgs/Path
  1.desc= The trajectory corresponding to the incoming base commands
  2.name= ~<name>/local_plan
  2.type= nav_msgs/Path
  2.desc= The trajectory corresponding to the outgoing (safe) base commands
}
```

```clearsilver
sub {
  0.name= /base_velocity
  0.type= geometry_msgs/Twist
  0.desc= Desired base commands
  1.name= /odom
  1.type= nav_msgs/Odometry
  1.desc= Base odometry
}
srv{
    0.name= ~<name>/clear_costmaps 
    0.type= std_srvs/Empty
    0.desc= Clear marked cells in the current costmap layers. (available on 0.0.3 and later)
}
```

#### Parameters

Many of the parameters are identical to those of the
[base_local_planner](base_local_planner) package.

```clearsilver
param {
  no_header=True

  0.name= ~<name>/acc_lim_x
  0.default= 2.5
  0.type= double
  0.desc= Maximum forward acceleration (in m/s/s)

  1.name= ~<name>/acc_lim_y
  1.default= 2.5
  1.type= double
  1.desc= Maximum lateral acceleration (in m/s/s)

  2.name= ~<name>/acc_lim_th
  2.default= 3.2
  2.type= double
  2.desc= Maximum rotational acceleration (in radians/s/s)

  3.name= ~<name>/sim_time
  3.default= 1.0
  3.type= double
  3.desc= Length, in seconds, of trajectories to simulate forward

  4.name= ~<name>/sim_granularity
  4.default= 0.025
  4.type= double
  4.desc= Resolution at which to sample trajectories

  5.name= ~<name>/vx_samples
  5.default= 3
  5.type= integer
  5.desc= Number of x velocities to consider

  6.name= ~<name>/vy_samples
  6.default= 5
  6.type= integer
  6.desc= Number of y velocities to consider

  7.name= ~<name>/vtheta_samples
  7.default= 10
  7.type= integer
  7.desc= Number of rotational velocities to consider

  8.name= ~<name>/user_bias
  8.default= 0.6
  8.type= double
  8.desc= Weight given to incoming base commands, used in trajectory scoring

  9.name= ~<name>/occdist_scale
  9.default= 0.01
  9.type= double
  9.desc= Weight given to distance to nearest occupied grid cell, used in trajectory scoring

  10.name= ~<name>/max_vel_x
  10.default= 0.5
  10.type= double
  10.desc= Maximum forward velocity in m/s

  11.name= ~<name>/min_vel_x
  11.default= 0.1
  11.type= double
  11.desc= Minimum forward velocity in m/s

  12.name= ~<name>/max_vel_y
  12.default= 0.2
  12.type= double
  12.desc= Maximum lateral velocity in m/s

  13.name= ~<name>/min_vel_y
  13.default= -0.2
  13.type= double
  13.desc= Minimum lateral velocity in m/s
  
  14.name= ~<name>/min_vel_y
  14.default= -0.2
  14.type= double
  14.desc= Minimum lateral velocity in m/s7.name= ~<name>/max_rotational_vel

  15.name= ~<name>/max_rotational_velocity
  15.default= 1.0
  15.type= double
  15.desc= Maximum rotational velocity rad/s

  16.name= ~<name>/world_model
  16.default= costmap
  16.type= string
  16.desc= World model type

  17.name= ~<name>/holonomic_robot
  17.default= true
  17.type= bool
  17.desc= True to indicate robot can move laterally

  18.name= ~<name>/dwa
  18.default= true
  18.type= bool
  18.desc= True to indicate dynamic window

  19.name= ~<name>/safe_backwards
  19.default= false
  19.type= bool
  19.desc= True to use safe trajectory for moving backward (available on 0.0.3 and later)

}
```
