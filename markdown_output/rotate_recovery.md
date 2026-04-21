## Overview

The \`rotate_recovery::RotateRecovery\` is a simple recovery behavior
that attempts to clear out space in the navigation stack\'s
[ costmaps](costmap_2d ) by rotating the robot 360 degrees if local
obstacles allow. It adheres to the \`nav_core::RecoveryBehavior\`
interface found in the [nav_core](nav_core) package and can be used as a
recovery behavior [ plugin](pluginlib ) for the [move_base](move_base)
node.

## RotateRecovery

The \`rotate_recovery::RotateRecovery\` object exposes its functionality
as a [ C++ ROS Wrapper](navigation/ROS_Wrappers ). It operates within a
ROS namespace (assumed to be **name** from here on) specified on
initialization. It adheres to the \`nav_core::RecoveryBehavior\`
interface found in the [nav_core](nav_core) package.

Example creation of a \`rotate_recovery::RotateRecovery\` object:

```cplusplus
#include <tf/transform_listener.h>
#include <costmap_2d/costmap_2d_ros.h>
#include <rotate_recovery/rotate_recovery.h>

...
tf::TransformListener tf(ros::Duration(10));
costmap_2d::Costmap2DROS global_costmap("global_costmap", tf);
costmap_2d::Costmap2DROS local_costmap("local_costmap", tf);

rotate_recovery::RotateRecovery rr;
rr.initialize("my_rotate_recovery", &tf, &global_costmap, &local_costmap);

rr.runBehavior();
```

### API Stability

-   The C++ API is stable.
-   The ROS API is stable.

### ROS Parameters

The \`rotate_recovery::RotateRecovery\` object assumes that the local
planner used by the [move_base](move_base) node is the
\`base_local_planner::TrajectoryPlannerROS\` documented in the
[base_local_planner](base_local_planner) package and reads some of its
parameters accordingly. It will work on its own, but this requires the
user to specify additional parameters.

#### RotateRecovery Parameters

```clearsilver
param {
  no_header=True
  0.name = ~<name>/sim_granularity
  0.default = 0.017
  0.type = double
  0.desc = The distance in radians between checks for obstacles when checking if an in-place rotation is safe. Defaults to  1 degree.
  1.name = ~<name>/frequency
  1.default = 20.0
  1.type = double
  1.desc = The frequency in HZ at which to send velocity commands to the mobile base.
}
```

#### TrajectoryPlannerROS Parameters

These parameters are already set when using the
\`base_local_planner::TrajectoryPlannerROS\` local planner, they only
need to be set explicitly for the \`rotate_recovery::RotateRecovery\`
recovery behavior if a different local planne is used with the
[ navigation stack](navigation ).

```clearsilver
param{
  no_header=True
  1.name = ~TrajectoryPlannerROS/yaw_goal_tolerance
  1.default = 0.05
  1.type = double
  1.desc = The tolerance in radians for the controller in yaw/rotation when achieving its goal
  2.name = ~TrajectoryPlannerROS/acc_lim_th
  2.default = 3.2
  2.type = double
  2.desc = The rotational acceleration limit of the robot in radians/sec^2
  3.name = ~TrajectoryPlannerROS/max_rotational_vel
  3.default = 1.0
  3.type = double
  3.desc = The maximum rotational velocity allowed for the base in radians/sec
  4.name = ~TrajectoryPlannerROS/min_in_place_rotational_vel
  4.default = 0.4
  4.type = double
  4.desc = The minimum rotational velocity allowed for the base while performing in-place rotations in radians/sec
}
```

### C++ API

The C++ \`rotate_recovery::RotateRecovery\` class adheres to the
\`nav_core::RecoveryBehavior\` interface found in the
[nav_core](nav_core) package. For detailed documentation, please see
[ RotateRecovery documentation](http://www.ros.org/doc/api/rotate_recovery/html/classrotate__recovery_1_1RotateRecovery.html ).
