## Overview

The `clear_costmap_recovery::ClearCostmapRecovery` is a simple
recovery behavior that clears out space in the navigation stack's
[ costmaps](costmap_2d ) by reverting to the static map outside of a
given radius away from the robot. It adheres to the
`nav_core::RecoveryBehavior` interface found in the
[nav_core](nav_core) package and can be used as a recovery behavior
[ plugin](pluginlib ) for the [move_base](move_base) node.

## ClearCostmapRecovery

The `clear_costmap_recovery::ClearCostmapRecovery` object exposes its
functionality as a [ C++ ROS Wrapper](navigation/ROS_Wrappers ). It
operates within a ROS namespace (assumed to be **name** from here on)
specified on initialization. It adheres to the
`nav_core::RecoveryBehavior` interface found in the
[nav_core](nav_core) package.

Example creation of a `clear_costmap_recovery::ClearCostmapRecovery`
object:



```cplusplus
#include <tf/transform_listener.h>
#include <costmap_2d/costmap_2d_ros.h>
#include <clear_costmap_recovery/clear_costmap_recovery.h>

...
tf::TransformListener tf(ros::Duration(10));
costmap_2d::Costmap2DROS global_costmap("global_costmap", tf);
costmap_2d::Costmap2DROS local_costmap("local_costmap", tf);

clear_costmap_recovery::ClearCostmapRecovery ccr;
ccr.initialize("my_clear_costmap_recovery", &tf, &global_costmap, &local_costmap);

ccr.runBehavior();
```



### API Stability

-   The C++ API is stable.
-   The ROS API is stable.

### ROS Parameters



```clearsilver
param {
  no_header=True
  0.name = ~<name>/reset_distance
  0.default = 3.0
  0.type = double 
  0.desc = The length of the side of a square centered on the robot pose, outside which obstacles will be removed from the costmaps when they are reverted to the static map.
  1.name=~<name>/invert_area_to_clear
  1.default = false
  1.type = bool
  1.desc = Clears costmap/s outside of a square centered on the robot pose, if false and inside, if true. The length of the side of the square is set by '~<name>/reset_distance' parameter.

  2.name = ~<name>/layer_names
  2.default = ["obstacles"]
  2.type = list
  2.desc = Clears only the 'layers' that are mentioned in the 'layer_names' parameter. The layers are defined according to the plugins for local_costmap and global_costmap.
}
```



### C++ API

The C++ `clear_costmap_recovery::ClearCostmapRecovery` class adheres
to the `nav_core::RecoveryBehavior` interface found in the
[nav_core](nav_core) package. For detailed documentation, please see
[ ClearCostmapRecovery Documentation](http://www.ros.org/doc/api/clear_costmap_recovery/html/classclear__costmap__recovery_1_1ClearCostmapRecovery.html ).
