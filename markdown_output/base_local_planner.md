

```wiki
Please be aware that the description below is not valid to all ROS distributions! Presumably its up to date for the current distribution, but in older distributions parameters might have different names, different defaults or might even not exist. 
[[https://github.com/ros-planning/navigation/issues/90|case example]]
```



## Overview

The `base_local_planner` package provides a controller that drives a
mobile base in the plane. This controller serves to connect the path
planner to the robot. Using a map, the planner creates a kinematic
trajectory for the robot to get from a start to a goal location. Along
the way, the planner creates, at least locally around the robot, a value
function, represented as a grid map. This value function encodes the
costs of traversing through the grid cells. The controller's job is to
use this value function to determine dx,dy,dtheta velocities to send to
the robot.

![](attachment:local_plan.png)

The basic idea of both the Trajectory Rollout and Dynamic Window
Approach (DWA) algorithms is as follows:

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

DWA differs from Trajectory Rollout in how the robot's control space is
sampled. Trajectory Rollout samples from the set of achievable
velocities over the entire forward simulation period given the
acceleration limits of the robot, while DWA samples from the set of
achievable velocities for just one simulation step given the
acceleration limits of the robot. This means that DWA is a more
efficient algorithm because it samples a smaller space, but may be
outperformed by Trajectory Rollout for robots with low acceleration
limits because DWA does not forward simulate constant accelerations. In
practice however, we find DWA and Trajectory Rollout to perform
comparably in all our tests and recommend use of DWA for its efficiency
gains.

Useful references:

-   [Brian P. Gerkey and Kurt Konolige. "Planning and Control in Unstructured Terrain "](https://pdfs.semanticscholar.org/dabd/bb636f02d3cff3d546bd1bdae96a058ba4bc.pdf?_ga=2.75374935.412017123.1520536154-80785446.1520536154).
    Discussion of the Trajectory Rollout algorithm in use on the LAGR
    robot.
-   [D. Fox, W. Burgard, and S. Thrun. "The dynamic window approach to collision avoidance".](http://www.cs.washington.edu/ai/Mobile_Robotics/postscripts/colli-ieee.ps.gz)
    The Dynamic Window Approach to local control.
-   [Alonzo Kelly. "An Intelligent Predictive Controller for Autonomous Vehicles"](http://www.ri.cmu.edu/pub_files/pub1/kelly_alonzo_1994_7/kelly_alonzo_1994_7.pdf).
    An previous system that takes a similar approach to control.

### Map Grid

In order to score trajectories efficiently, the Map Grid is used. For
each control cycle, a grid is created around the robot (the size of the
local costmap), and the global path is mapped onto this area. This means
certain of the grid cells will be marked with distance 0 to a path
point, and distance 0 to the goal. A propagation algorithm then
efficiently marks all other cells with their manhattan distance to the
closest of the points marked with zero.

This map grid is then used in the scoring of trajectories.

The goal of the global path may often lie outside the small area covered
by the map_grid, when scoring trajectories for proximity to goal, what
is considered is the "local goal", meaning the first path point which
is inside the area having a consecutive point outside the area. The size
of the area is determined by move_base.

## Oscillation Suppression

Oscillation occur when in either of the x, y, or theta dimensions,
positive and negative values are chosen consecutively. To prevent
oscillations, when the robot moves in any direction, for the next cycles
the opposite direction is marked invalid, until the robot has moved
beyond a certain distance from the position where the flag was set.

## Generic Local Planning

**New in navigation 1.10.0**

The groovy release of ROS includes a new implementation of the
[dwa_local_planner](dwa_local_planner) package. The implementation
attempts to be more modular, to allow easier creation of custom local
planners while reusing a lot of code. The code base of
base_local_planner has been extended with several new headers and
classes.

The principle of local planning is the search for a suitable local plan
in every control cycle. For that purpose, a number of candidate
trajectories is generated. For a generated trajectory, it is checked
whether it collides with an obstacle. If not, a rating is given to
compare several trajectories picking the best.

Obviously, depending on the robot shape (and actuator shape) and the
domain, this principle can be instantiated in very different ways. There
are many special ways to generate trajectories, and ways to search the
space of potential trajectories for a most suitable one.

The interfaces and classes below capture the generic local planning
principles allowing many instantiations. It should be possible to create
custom local planners using the `dwa_local_planner` as template and
just adding own cost functions or trajectory generators.

### TrajectorySampleGenerator

This interface describes a Generator which may generate a finite or
infinte number of trajectories, returning a new one on each invocation
of `nextTrajectory()`.

The `SimpleTrajectoryGenerator` class can generate trajectories
described in the overview, using either the trajectory rollout or the
DWA principle.

### TrajectoryCostFunction

This interface contains most importantly `scoreTrajectory(Trajectory
&traj)`, which takes a trajectory and returns a score. A negative score
means the trajectory is invalid. For positive value, the semantics are
that a trajectory with a lower score is preferrable to one with a higher
score with respect to this cost function.

Each cost function also has a scale by which its impact can be altered
in comparison to the other cost functions.

The `base_local_planner` package ships with some cost functions used
on the PR2, described below.

### SimpleScoredSamplingPlanner

This is a simple implementation of a trajectory search, taking a
`TrajectorySampleGenerator` and a list of `TrajectoryCostFunction`.
It will invoke `nextTrajectory()` until the generator stops generating
trajectories. For each, trajectory, it will loop over the list of cost
functions, adding up their positive values or aborting the scoring if
one cost function returns a negative value.

Using the scale of the cost functions the result is then the Trajectory
with the best weighted sum of positive cost function results.

### Helper classes

#### LocalPlannerUtil

This helper interface provides functionality that should be common to
all localplanners in the move_base context. It manages the current
global plan, the current motion limits, and the current costmap (local
map of sensed obstacles).

#### OdometryHelperRos

This class provides odometry information for ROS based robots.

#### LatchedStopRotateController

Ideally a local planner will make a robot stop exactly where it should.
In practice however, due to sensor noise and actuator uncertainty, it
may happen that the robot approaches the target spot but moves on. This
can lead to undesired robot behavior of oscilatting on a spot.

The LatchedStopRotateController is a Controller that can be used as soon
as the robot is close enough to the goal. The Controller will then just
perform a full stop and a rotation on the spot towards the goal
orientation, regardless of whether the robot position after the full
stop leads the robot outside the goal position tolerance.

### Cost Functions

#### ObstacleCostFunction

This cost function rates a trajectory based on the perceived obstacles.
It either returns negative costs if the trajectory passes through an
obstacle, or zero else.

#### MapGridCostFunction

This cost function class rates a trajectory based on how closely the
trajectory follows a global path or approaches a goal point. This
attempts to optimize calculation speed by using the same precomputed map
of distances to a path or goal point for all trajectories.

In the dwa_local_planner, this cost function is instantiated multiple
times, for different purposes. To keep the trajectory close to the path,
to make the robot advance towards a local goal, and also to make the
robot front ("nose") point towards a local goal. This cost function is
a heuristics that can give bad results or even fail with unsuitable
parameters.

#### OscillationCostFunction

This cost function class helps reducing certain oscillations, be
returning negative costs for switches of motion directions if the last
previous switch happened below a certain distance. While this
effectively prevents these oscillations, but might also prevent good
solutions if used with unsuitable parameters.

#### PreferForwardCostFunction

This cost function class was designed with robots like the PR2 in mind
having good sensor coverage only in front of the robot (tilting laser).
The costs function prefers motions in the front direction, penalizing
backwards and strafing motions. On other robots or in other domains this
may be very undesirable behavior.

## TrajectoryPlannerROS

The `base_local_planner::TrajectoryPlannerROS` object is a
[ wrapper](navigation/ROS_Wrappers ) for a
`base_local_planner::TrajectoryPlanner` object that exposes its
functionality as a [ C++ ROS Wrapper](navigation/ROS_Wrappers ). It
operates within a ROS namespace (assumed to be *name* from here on)
specified on initialization. It adheres to the
`nav_core::BaseLocalPlanner` interface found in the
[nav_core](nav_core) package.

Example creation of a `base_local_planner::TrajectoryPlannerROS`
object: 

```cplusplus
#include <tf/transform_listener.h>
#include <costmap_2d/costmap_2d_ros.h>
#include <base_local_planner/trajectory_planner_ros.h>

...

tf::TransformListener tf(ros::Duration(10));
costmap_2d::Costmap2DROS costmap("my_costmap", tf);

base_local_planner::TrajectoryPlannerROS tp;
tp.initialize("my_trajectory_planner", &tf, &costmap);
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
  2.name = ~<name>/cost_cloud
  2.type = sensor_msgs/PointCloud2
  2.desc = The cost grid used for planning. Used for visualization purposes. See the `publish_cost_grid_pc` parameter for enabling/disabling this visualization. '''New in navigation 1.4.0'''
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
to customize the behavior of the
`base_local_planner::TrajectoryPlannerROS` wrapper. These parameters
are grouped into several categories: robot configuration, goal
tolerance, forward simulation, trajectory scoring, oscillation
prevention, and global plan.

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
  2.name = ~<name>/acc_lim_theta
  2.default = 3.2
  2.type = double
  2.desc = The rotational acceleration limit of the robot in radians/sec^2
  3.name = ~<name>/max_vel_x
  3.default = 0.5
  3.type = double
  3.desc = The maximum forward velocity allowed for the base in meters/sec
  4.name = ~<name>/min_vel_x
  4.default =  0.1
  4.type = double
  4.desc = The minimum forward velocity allowed for the base in meters/sec. It is useful to specify this to guarantee that velocity commands sent to a mobile base are high enough to allow the base to overcome friction.
  5.name = ~<name>/max_vel_theta
  5.default = 1.0
  5.type = double
  5.desc = The maximum rotational velocity allowed for the base in radians/sec
  6.name = ~<name>/min_vel_theta
  6.default = -1.0
  6.type = double
  6.desc = The minimum rotational velocity allowed for the base in radians/sec
  7.name = ~<name>/min_in_place_vel_theta
  7.default = 0.4
  7.type = double
  7.desc = The minimum rotational velocity allowed for the base while performing in-place rotations in radians/sec
  8.name = ~<name>/backup_vel
  8.default = -0.1
  8.type = double
  8.desc = '''DEPRECATED (use escape_vel)''':Speed used for backing up during escapes in meters/sec. Note that it must be negative in order for the robot to actually reverse. A positive speed will cause the robot to move forward while attempting to escape.
  9.name = ~<name>/escape_vel
  9.default = -0.1
  9.type = double
  9.desc = Speed used for driving during escapes in meters/sec. Note that it must be negative in order for the robot to actually reverse. A positive speed will cause the robot to move forward while attempting to escape. '''New in navigation 1.3.1'''
 10.name = ~<name>/holonomic_robot
 10.default = true
 10.type = bool
 10.desc = Determines whether velocity commands are generated for a holonomic or non-holonomic robot. For holonomic robots, strafing velocity commands may be issued to the base. For non-holonomic robots, no strafing velocity commands will be issued.
}
```



The following parameters are only used if `holonomic_robot` is set to
true:



```clearsilver
param{
  no_header=True
  0.name = ~<name>/y_vels
  0.default = [-0.3, -0.1, 0.1, 0.3]
  0.type = list
  0.desc = The strafing velocities that a holonomic robot will consider in meters/sec
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
  3.desc = If goal tolerance is latched, if the robot ever reaches the goal xy location it will simply rotate in place, even if it ends up outside the goal tolerance while it is doing so. - '''New in navigation 1.3.1'''
}
```



#### Forward Simulation Parameters



```clearsilver
param{
  no_header=True
  1.name = ~<name>/sim_time
  1.default = 1.0
  1.type = double
  1.desc = The amount of time to forward-simulate trajectories in seconds
  2.name = ~<name>/sim_granularity
  2.default = 0.025
  2.type = double
  2.desc = The step size, in meters, to take between points on a given trajectory
  3.name = ~<name>/angular_sim_granularity
  3.default = ~<name>/sim_granularity
  3.type = double
  3.desc = The step size, in radians, to take between angular samples on a given trajectory. - '''New in navigation 1.3.1'''
  4.name = ~<name>/vx_samples
  4.default = 3
  4.type = integer
  4.desc = The number of samples to use when exploring the x velocity space
  5.name = ~<name>/vtheta_samples
  5.default =  20
  5.type = integer
  5.desc = The number of samples to use when exploring the theta velocity space
  6.name = ~<name>/controller_frequency
  6.default =  20.0
  6.type = double
  6.desc = The frequency at which this controller will be called in Hz. Uses searchParam to read the parameter from parent namespaces if not set in the namespace of the controller. For use with [[move_base]], this means that you only need to set its "controller_frequency" parameter and can safely leave this one unset. - '''New in navigation 1.3.1'''
}
```



#### Trajectory Scoring Parameters

The cost function used to score each trajectory is in the following
form:



```
cost = 
  pdist_scale * (distance to path from the endpoint of the trajectory in map cells or meters depending on the meter_scoring parameter) 
  + gdist_scale * (distance to local goal from the endpoint of the trajectory in map cells or meters depending on the meter_scoring parameter) 
  + occdist_scale * (maximum obstacle cost along the trajectory in obstacle cost (0-254))
```





```clearsilver
param{
  no_header=True
  0.name = ~<name>/meter_scoring
  0.default =  `false`
  0.type = bool
  0.desc = Whether the `gdist_scale` and `pdist_scale` parameters should assume that `goal_distance` and `path_distance` are expressed in units of meters or cells. Cells are assumed by default. '''New in navigation 1.3.1'''
  1.name = ~<name>/pdist_scale
  1.default =  0.6
  1.type = double
  1.desc = The weighting for how much the controller should stay close to the path it was given, maximal possible value is 5.0
  2.name = ~<name>/gdist_scale
  2.default = 0.8
  2.type = double
  2.desc = The weighting for how much the controller should attempt to reach its local goal, also controls speed, maximal possible value is 5.0


  3.name = ~<name>/occdist_scale
  3.default = 0.01
  3.type = double
  3.desc = The weighting for how much the controller should attempt to avoid obstacles
  4.name = ~<name>/heading_lookahead
  4.default =  0.325
  4.type = double
  4.desc = How far to look ahead in meters when scoring different in-place-rotation trajectories
  5.name = ~<name>/heading_scoring
  5.default = `false`
  5.type = bool
  5.desc = Whether to score based on the robot's heading to the path or its distance from the path
  6.name = ~<name>/heading_scoring_timestep
  6.default = 0.8
  6.type = double
  6.desc = How far to look ahead in time in seconds along the simulated trajectory when using heading scoring
  7.name = ~<name>/dwa
  7.default = `true`
  7.type = bool
  7.desc = Whether to use the Dynamic Window Approach (DWA)_ or whether to use Trajectory Rollout (NOTE: In our experience DWA worked as well as Trajectory Rollout and is computationally less expensive. It is possible that robots with extremely poor acceleration limits could gain from running Trajectory Rollout, but we recommend trying DWA first.)
  8.name = ~<name>/publish_cost_grid_pc
  8.default = `false`
  8.type = bool
  8.desc = Whether or not to publish the cost grid that the planner will use when planning. When true, a `sensor_msgs/PointCloud2` will be available on the `~<name>/cost_cloud` topic. Each point cloud represents the cost grid and has a field for each individual scoring function component as well as the overall cost for each cell, taking the scoring parameters into account. '''New in navigation 1.4.0'''
  9.name = ~<name>/global_frame_id
  9.default = `odom`
  9.type = string
  9.desc = The frame to set for the `cost_cloud`. Should be set to the same frame as the local costmap's global frame. '''New in navigation 1.4.0'''
}
```



#### Oscillation Prevention Parameters



```cplusplus
#include <tf/transform_listener.h>
#include <costmap_2d/costmap_2d_ros.h>
#include <base_local_planner/trajectory_planner_ros.h>

...

tf::TransformListener tf(ros::Duration(10));
costmap_2d::Costmap2DROS costmap("my_costmap", tf);

base_local_planner::TrajectoryPlannerROS tp;
tp.initialize("my_trajectory_planner", &tf, &costmap);
```

0

#### Global Plan Parameters



```cplusplus
#include <tf/transform_listener.h>
#include <costmap_2d/costmap_2d_ros.h>
#include <base_local_planner/trajectory_planner_ros.h>

...

tf::TransformListener tf(ros::Duration(10));
costmap_2d::Costmap2DROS costmap("my_costmap", tf);

base_local_planner::TrajectoryPlannerROS tp;
tp.initialize("my_trajectory_planner", &tf, &costmap);
```

1

## TrajectoryPlanner

The `base_local_planner::TrajectoryPlanner` provides implementations
of the DWA and Trajectory Rollout algorithms described earlier. In order
to use the `base_local_planner::TrajectoryPlanner` with ROS, please
use the [TrajectoryPlannerROS wrapper](#TrajectoryPlannerROS). It is not
recommended to use the `base_local_planner::TrajectoryPlanner` on its
own.

### API Stability

The C++ API is stable. However, it is recommended that you use the
[TrajectoryPlannerROS wrapper](#TrajectoryPlannerROS) instead of using
the `base_local_planner::TrajectoryPlanner` on its own.
