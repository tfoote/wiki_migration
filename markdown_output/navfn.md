## Overview

This package provides an implementation of a fast, interpolated
navigation function used to create plans for a mobile base through the
\`navfn::NavFn\` class. It also provides a
[ ROS Wrapper](navigation/ROS_Wrappers ) for this class via the
\`navfn::NavfnROS\` object that adheres to the
\`nav_core::BaseGlobalPlanner\` interface specified in the
[nav_core](nav_core) package. The \`navfn::NavfnROS\` object is also
used as a global planner plugin for the [move_base](move_base) node.

## NavfnROS

The \`navfn::NavfnROS\` object is a [ wrapper](navigation/ROS_Wrappers )
for a \`navfn::NavFn\` object that exposes its functionality as a
[ C++ ROS Wrapper](navigation/ROS_Wrappers ). It operates within a ROS
namespace (assumed to be *name* from here on) specified on
initialization. It adheres to the \`nav_core::BaseGlobalPlanner\`
interface found in the [nav_core](nav_core) package.

Example creation of a \`navfn::NavfnROS\` object:

```cplusplus
#include <tf/transform_listener.h>
#include <costmap_2d/costmap_2d_ros.h>
#include <navfn/navfn_ros.h>

...

tf::TransformListener tf(ros::Duration(10));
costmap_2d::Costmap2DROS costmap("my_costmap", tf);

navfn::NavfnROS navfn;
navfn.initialize("my_navfn_planner", &costmap);
```

### API Stability

-   The ROS API is stable
-   The C++ API is stable

### ROS API

```clearsilver
pub {
  0.name  = ~<name>/plan
  0.type = nav_msgs/Path
  0.desc = The last plan computed by `navfn`, published everytime the planner computes a new path, and used primarily for visualization purposes.
}
param {
  0.name = ~<name>/allow_unknown
  0.default = `true`
  0.type = bool
  0.desc = Specifies whether or not to allow navfn to create plans that traverse unknown space.  NOTE: if you are using a layered costmap_2d costmap with [[costmap_2d/hydro/obstacles|a voxel or obstacle layer]], you must also set the track_unknown_space param for that layer to be true, or it will convert all your unknown space to free space (which navfn will then happily go right through).
  1.name = ~<name>/planner_window_x
  1.default = 0.0
  1.type = double
  1.desc = Specifies the x size of an optional window to restrict the planner to. This can be useful for restricting !NavFn to work in a small window of a large costmap.
  2.name = ~<name>/planner_window_y
  2.default = 0.0
  2.type = double
  2.desc = Specifies the y size of an optional window to restrict the planner to. This can be useful for restricting !NavFn to work in a small window of a large costmap.
  3.name = ~<name>/default_tolerance
  3.default = 0.0
  3.type = double
  3.desc = A tolerance on the goal point for the planner. NavFn will attempt to create a plan that is as close to the specified goal as possible but no further than `default_tolerance` away. '''New in navigation 1.3.0'''
  4.name = ~<name>/visualize_potential
  4.default = `false`
  4.type = bool
  4.desc = Specifies whether or not to visualize the potential area computed by navfn via a !PointCloud2. '''New in navigation 1.3.1'''
}
```

### C++ API

\`navfn::NavfnROS\` adheres to the \`nav_core::BaseGlobalPlanner\`
interface found in the [nav_core](nav_core) package. For detailed
documentation, please see
[ NavfnROS C++ Documentation](http://www.ros.org/doc/api/navfn/html/classnavfn_1_1NavfnROS.html ).

## NavFN

The \`navfn::NavFn\` object provides an implementation of the navigation
function described above. Feel free to use it, but beware that we make
no guarantees about the stability of its public API.

### API Stability

-   The C++ API is **not** stable. It is subject to change at any time.

### C++ API

Documentation on the C++ API for the \`navfn::NavFn\` class can be found
here:
[ NavFn Documentation](http://www.ros.org/doc/api/navfn/html/classnavfn_1_1NavFn.html ).
Again, the C++ API is **not** guaranteed to be stable.

## Reference

-   [Rationale of Dijkstra being used in navfn instead of A\*](http://answers.ros.org/question/28366/why-navfn-is-using-dijkstra)
