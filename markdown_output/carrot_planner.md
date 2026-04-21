## Overview

The \`carrot_planner::CarrotPlanner\` is a simple global planner that
adheres to the \`nav_core::BaseGlobalPlanner\` interface found in the
[nav_core](nav_core) package and can be used as a global planner
[ plugin](pluginlib ) for the [move_base](move_base) node. The planner
takes a goal point from an external user, checks if the user-specified
goal is in an obstacle, and if it is, it walks back along the vector
between the user-specified goal and the robot until a goal point that is
not in an obstacle is found. It then passes this goal point on as a plan
to a local planner or controller. In this way, the carrot planner allows
the robot to get as close to a user-specified goal point as possible.

![](attachment:planner_overview.png)

## CarrotPlanner

The \`carrot_planner::CarrotPlanner\` object exposes its functionality
as a [ C++ ROS Wrapper](navigation/ROS_Wrappers ). It operates within a
ROS namespace (assumed to be *name* from here on) specified on
initialization. It adheres to the \`nav_core::BaseGlobalPlanner\`
interface found in the [nav_core](nav_core) package.

Example creation of a \`carrot_planner::CarrotPlanner\` object:

```cplusplus
#include <tf/transform_listener.h>
#include <costmap_2d/costmap_2d_ros.h>
#include <carrot_planner/carrot_planner.h>

...
tf::TransformListener tf(ros::Duration(10));
costmap_2d::Costmap2DROS costmap("my_costmap", tf);

carrot_planner::CarrotPlanner cp;
cp.initialize("my_carrot_planner", &costmap);
```

### API Stability

-   The ROS API is stable.
-   The C++ API is stable.

### ROS Parameters

```clearsilver
param {
  no_header=True
  0.name = ~<name>/step_size
  0.default = Resolution of the associated costmap
  0.type = double 
  0.desc = The size steps to take backward in meters along the vector between the robot and the user-specified goal point when attempting to find a valid goal for the local planner.
  1.name = ~<name>/min_dist_from_robot
  1.default = 0.10
  1.type = double
  1.desc = The minimum distance from the robot in meters at which a goal point will be sent to the local planner.
}
```

### C++ API

The C++ \`carrot_planner::CarrotPlanner\` class adheres to the
\`nav_core::BaseGlobalPlanner\` interface found in the
[nav_core](nav_core) package. For detailed documentation, please see
[ CarrotPlanner Documentation](http://www.ros.org/doc/api/carrot_planner/html/classcarrot__planner_1_1CarrotPlanner.html ).
