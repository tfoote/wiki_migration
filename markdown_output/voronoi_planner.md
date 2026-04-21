## Overview

Someone may want to search path which keeps robot away from the
obstacles instead of searching shortest path, as well-known A\*-planners
do.

![](attachment:voronoi_planner.jpg)

\`voronoi_planner\` uses [dynamicvoronoi](dynamicvoronoi) package to
make generalized Voronoi diagrams (GVD) which is made up of regions
around obstacles on costmap.

Then it searches a path from robot position to given goal on GVD.

[Youtube](https://www.youtube.com/watch?v=tSVTZ0HODyA)

## VoronoiPlanner

The \`voronoi_planner::VoronoiPlanner\` object exposes its functionality
as a [ C++ ROS Wrapper](navigation/ROS_Wrappers ). It operates withing a
ROS namespace (assumed to be *name* from here on) specified on
initialization. It adheres to the \`nav_core::BaseGlobalPlanner\`
interface found in the [nav_core](nav_core) package.

### ROS Parameters

```clearsilver
param {
  no_header=True
  0.name = ~<name>/publish_voronoi_grid
  0.default = true
  0.type = bool 
  0.desc = Publish Voronoi grid as costmap.
  1.name = ~<name>/smooth_path
  1.default = true
  1.type = bool
  1.desc = Smooth path.
  2.name = ~<name>/weight_data
  2.default = 0.5
  2.type = double
  2.desc = Weight of data when smoothing path.
  3.name = ~<name>/weight_smooth
  3.default = 0.3
  3.type = double
  3.desc = Weight of smoothing when smoothing path.
}
```

## Usage example

Planner was tested using [husky_gazebo](husky_gazebo),
[husky_navigation](husky_navigation) and [husky_viz](husky_viz). To use
\`voronoi_planner\` you need to change \`base_global_planner\` of
[move_base](move_base) in such a way: ```
<arg name="base_global_planner" default="voronoi_planner/VoronoiPlanner"/>
``` Other
parameters changed were global_costmap/width and global_costmap/height
(in move_base.launch from [husky_navigation](husky_navigation)):
```
<param name="global_costmap/width" value="35.0" if="$(arg no_static_map)"/>
    <param name="global_costmap/height" value="35.0" if="$(arg no_static_map)"/>
```

Path generated is published in \<name\>/plan topic. Voronoi grid map is
published (if publish_voronoi_grid parameter is true) in
\<name\>/voronoi_grid. You should configure RViz to view it.

[husky_navigation/Tutorials/Husky Move Base Demo](husky_navigation/Tutorials/Husky Move Base Demo)
may be useful.
