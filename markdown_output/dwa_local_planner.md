## Overview

The `dwa_local_planner` package provides a controller that drives a
mobile base in the plane. This controller serves to connect the path
planner to the robot. Using a map, the planner creates a kinematic
trajectory for the robot to get from a start to a goal location. Along
the way, the planner creates, at least locally around the robot, a value
function, represented as a grid map. This value function encodes the
costs of traversing through the grid cells. The controller's job is to
use this value function to determine dx,dy,dtheta velocities to send to
the robot.

![](attachment:local_plan.png)

The basic idea of the Dynamic Window Approach (DWA) algorithm is as
follows:

1\. Discretely sample in the robot's control space (dx,dy,dtheta) 1.
For each sampled velocity, perform forward simulation from the robot's
current state to predict what would happen if the sampled velocity were
applied for some (short) period of time. 1. Evaluate (score) each
trajectory resulting from the forward simulation, using a metric that
incorporates characteristics such as: proximity to obstacles, proximity
to the goal, proximity to the global path, and speed. Discard illegal
trajectories (those that collide with obstacles). 1. Pick the
highest-scoring trajectory and send the associated velocity to the
mobile base. 1. Rinse and repeat.

Useful references:

-   [D. Fox, W. Burgard, and S. Thrun. "The dynamic window approach to collision avoidance".](http://www.cs.washington.edu/ai/Mobile_Robotics/postscripts/colli-ieee.ps.gz)
    The Dynamic Window Approach to local control.
-   [Alonzo Kelly. "An Intelligent Predictive Controller for Autonomous Vehicles"](http://www.ri.cmu.edu/pub_files/pub1/kelly_alonzo_1994_7/kelly_alonzo_1994_7.pdf).
    A previous system that takes a similar approach to control.
-   [Brian P. Gerkey and Kurt Konolige. "Planning and Control in Unstructured Terrain "](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.330.2120&rep=rep1&type=pdf).
    Discussion of the Trajectory Rollout algorithm in use on the LAGR
    robot.

## DWAPlannerROS

The `dwa_local_planner::DWAPlannerROS` object is a
[wrapper](navigation/ROS_Wrappers) for a
`dwa_local_planner::DWAPlanner` object that exposes its functionality
as a [C++ ROS Wrapper](navigation/ROS_Wrappers). It operates within a
ROS namespace (assumed to be *name* from here on) specified on
initialization. It adheres to the `nav_core::BaseLocalPlanner`
interface found in the [nav_core](nav_core) package.

Example creation of a `dwa_local_planner::DWAPlannerROS` object:



```cplusplus
#include <tf/transform_listener.h>
#include <costmap_2d/costmap_2d_ros.h>
#include <dwa_local_planner/dwa_planner_ros.h>

...

tf::TransformListener tf(ros::Duration(10));
costmap_2d::Costmap2DROS costmap("my_costmap", tf);

dwa_local_planner::DWAPlannerROS dp;
dp.initialize("my_dwa_planner", &tf, &costmap);
```



### API Stability

-   The C++ API is stable
-   The ROS API is stable



```clearsilver
pub {
  0.name = ~<name>/global_plan
  0.type = nav_msgs/Path
  0.desc = The portion of the global plan that the local planner is currently attempting to follow. Used primarily for visualization purposes.
  1.name = ~<name>/local_plan
  1.type = nav_msgs/Path
  1.desc = The local plan or trajectory that scored the highest on the last cycle. Used primarily for visualization purposes.
}
```

 

```clearsilver
sub {
  0.name = odom
  0.type = nav_msgs/Odometry
  0.desc = Odometry information that gives the local planner the current speed of the robot. The velocity information in this message is assumed to be in the same coordinate frame as the `robot_base_frame` of the costmap contained within the `TrajectoryPlannerROS object`. See the [[costmap_2d]] package for information about the `robot_base_frame` parameter.
}
```



### Parameters

There are a large number of ROS [Parameters](Parameters) that can be set
to customize the behavior of the `dwa_local_planner::DWAPlannerROS`
wrapper. These parameters are grouped into several categories: robot
configuration, goal tolerance, forward simulation, trajectory scoring,
oscillation prevention, and global plan. Most of these parameters can
also be changed using [dynamic_reconfigure](dynamic_reconfigure) to
facilitate tuning the local planner in a running system.

#### Robot Configuration Parameters



```clearsilver
param{
  no_header=True
  0.name = ~<name>/acc_lim_x
  0.default = 2.5
  0.type = double
  0.desc = The x acceleration limit of the robot in meters/sec^2
  1.name = ~<name>/acc_lim_y
  1.default = 2.5
  1.type = double
  1.desc = The y acceleration limit of the robot in meters/sec^2
  2.name = ~<name>/acc_lim_th
  2.default = 3.2
  2.type = double
  2.desc = The rotational acceleration limit of the robot in radians/sec^2
  3.name = ~<name>/max_vel_trans
  3.default = 0.55
  3.type = double
  3.desc = The absolute value of the maximum translational velocity for the robot in m/s
  4.name = ~<name>/min_vel_trans
  4.default = 0.1
  4.type = double
  4.desc = The absolute value of the minimum translational velocity for the robot in m/s
  5.name = ~<name>/max_vel_x
  5.default = 0.55
  5.type = double
  5.desc = The maximum x velocity for the robot in m/s.
  6.name = ~<name>/min_vel_x
  6.default = 0.0
  6.type = double
  6.desc = The minimum x velocity for the robot in m/s, negative for backwards motion.
  7.name = ~<name>/max_vel_y
  7.default = 0.1
  7.type = double
  7.desc = The maximum y velocity for the robot in m/s
  8.name = ~<name>/min_vel_y
  8.default = -0.1
  8.type = double
  8.desc = The minimum y velocity for the robot in m/s
  9.name = ~<name>/max_rot_vel
  9.default = 1.0
  9.type = double
  9.desc = The absolute value of the maximum rotational velocity for the robot in rad/s
  10.name = ~<name>/min_rot_vel
  10.default = 0.4
  10.type = double
  10.desc = The absolute value of the minimum rotational velocity for the robot in rad/s
}
```



#### Goal Tolerance Parameters



```clearsilver
param{
  no_header=True
  1.name = ~<name>/yaw_goal_tolerance
  1.default = 0.05
  1.type = double
  1.desc = The tolerance in radians for the controller in yaw/rotation when achieving its goal
  2.name = ~<name>/xy_goal_tolerance
  2.default = 0.10
  2.type = double
  2.desc = The tolerance in meters for the controller in the x & y distance when achieving a goal
  3.name = ~<name>/latch_xy_goal_tolerance
  3.default = false
  3.type = bool
  3.desc = If goal tolerance is latched, if the robot ever reaches the goal xy location it will simply rotate in place, even if it ends up outside the goal tolerance while it is doing so.
}
  4.name = ~<name>/rot_stopped_vel
  4.default = 1e-2
  4.type = double
  4.desc = The rotational speed in rad/s at which the robot is considered stopped
  5.name = ~<name>/trans_stopped_vel
  5.default = 1e-2
  5.type = double
  5.desc = The translational speed in m/s at which the robot is considered stopped
```



#### Forward Simulation Parameters



```clearsilver
param{
  no_header=True
  1.name = ~<name>/sim_time
  1.default = 1.7
  1.type = double
  1.desc = The amount of time to forward-simulate trajectories in seconds
  2.name = ~<name>/sim_granularity
  2.default = 0.025
  2.type = double
  2.desc = The step size, in meters, to take between points on a given trajectory
  3.name = ~<name>/vx_samples
  3.default = 3
  3.type = integer
  3.desc = The number of samples to use when exploring the x velocity space
  4.name = ~<name>/vy_samples
  4.default = 10
  4.type = integer
  4.desc = The number of samples to use when exploring the y velocity space
  5.name = ~<name>/vth_samples
  5.default =  20
  5.type = integer
  5.desc = The number of samples to use when exploring the theta velocity space
  6.name = ~<name>/controller_frequency
  6.default =  20.0
  6.type = double
  6.desc = The frequency at which this controller will be called in Hz. Uses searchParam to read the parameter from parent namespaces if not set in the namespace of the controller. For use with [[move_base]], this means that you only need to set its "controller_frequency" parameter and can safely leave this one unset.
}
```



#### Trajectory Scoring Parameters

The cost function used to score each trajectory is in the following
form:



```
cost =
  path_distance_bias * (distance to path from the endpoint of the trajectory in meters)
  + goal_distance_bias * (distance to local goal from the endpoint of the trajectory in meters)
  + occdist_scale * (maximum obstacle cost along the trajectory in obstacle cost (0-254))
```

 

```clearsilver
param{
  no_header=True
  1.name = ~<name>/path_distance_bias
  1.default =  32.0
  1.type = double
  1.desc = The weighting for how much the controller should stay close to the path it was given
  2.name = ~<name>/goal_distance_bias
  2.default = 24.0
  2.type = double
  2.desc = The weighting for how much the controller should attempt to reach its local goal, also controls speed
  3.name = ~<name>/occdist_scale
  3.default = 0.01
  3.type = double
  3.desc = The weighting for how much the controller should attempt to avoid obstacles
  4.name = ~<name>/forward_point_distance
  4.default = 0.325
  4.type = double
  4.desc = The distance from the center point of the robot to place an additional scoring point, in meters
  5.name = ~<name>/stop_time_buffer
  5.default = 0.2
  5.type = double
  5.desc = The amount of time that the robot must stop before a collision in order for a trajectory to be considered valid in seconds
  6.name = ~<name>/scaling_speed
  6.default = 0.25
  6.type = double
  6.desc = The absolute value of the velocity at which to start scaling the robot's footprint, in m/s
  7.name = ~<name>/max_scaling_factor
  7.default = 0.2
  7.type = double
  7.desc = The maximum factor to scale the robot's footprint by
  8.name = ~<name>/publish_cost_grid
  8.default = false
  8.type = bool
  8.desc = Whether or not to publish the cost grid that the planner will use when planning. When true, a sensor_msgs/PointCloud2 will be available on the ~<name>/cost_cloud topic. Each point cloud represents the cost grid and has a field for each individual scoring function component as well as the overall cost for each cell, taking the scoring parameters into account.
}
```



#### Oscillation Prevention Parameters



```clearsilver
param{
  no_header=True
  1.name = ~<name>/oscillation_reset_dist
  1.default = 0.05
  1.type = double
  1.desc = How far the robot must travel in meters before oscillation flags are reset
}
```



#### Global Plan Parameters



```clearsilver
param{
  no_header=True
  0.name = ~<name>/prune_plan
  0.default = `true`
  0.type = bool
  0.desc = Defines whether or not to eat up the plan as the robot moves along the path. If set to true, points will fall off the end of the plan once the robot moves 1 meter past them.
}
```



### C++ API

For C++ level API documentation on the
`base_local_planner::TrajectoryPlannerROS` class, please see the
following page:
[DWAPlannerROS C++ API](http://www.ros.org/doc/api/dwa_local_planner/html/classdwa__local__planner_1_1DWAPlannerROS.html)

## DWAPlanner

The `dwa_local_planner::DWAPlanner` provides implementations of the
DWA and Trajectory Rollout algorithms described earlier. In order to use
the `dwa_local_planner::DWAPlanner` with ROS, please use the
[DWAPlannerROS wrapper](#DWAPlannerROS). It is not recommended to use
the `dwa_local_planner::DWAPlanner` on its own.

### API Stability

-   The C++ API is stable. However, it is recommended that you use the
    [DWAPlannerROS wrapper](#DWAPlannerROS) instead of using the
    `dwa_local_planner::TrajectoryPlanner` on its own.

### C++ API

For C++ level API documentation on the `dwa_local_planner::DWAPlanner
class`, please see the following page:
[DWAPlanner C++ API](http://www.ros.org/doc/api/dwa_local_planner/html/classdwa__local__planner_1_1DWAPlanner.html)
