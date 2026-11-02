## Overview

This package defines an [pluginlib](https://index.ros.org/p/pluginlib)
interface and provides some plugins for converting occupied cells of
[costmap_2d](https://index.ros.org/p/costmap_2d) to geometric
primitives. This primitives (points, lines, polygons) represent
obstacles in the map. It is intendend for nodes that incorporate
obstacles (e.g. in navigation) and do not rely on cost cells, but
consider obstacles defined by shapes in the plane (e.g. polygons). The
costmap is still favorable in conjunction with
[navigation](https://index.ros.org/p/navigation) since it fuses multiple
range sensors with a global static map and some filtering might be
applied. A naive approach to further incorporate the costmap is to take
each occupied cell as point-obstacle. However, by integrating the
costmap_converter interface the costmap is converted continuously during
runtime and if desired the conversion is invoked in a separate thread.

The tutorial section is going to be added in the future. Before then,
refer to the example implementation in
[teb_local_planner](https://index.ros.org/p/teb_local_planner) package
or to the implementation of the
[standalone node](#standalone-node).

Contributions of new plugins, or extensions/improvements of current
plugins are welcome!

## Plugins

### CostmapToPolygonsDBSMCCH

This plugin converts occupied cells to a set of convex polygons. The
conversion is performed in two stages: 1. Clusters are determined using
the DBSCAN Algorithm (<https://en.wikipedia.org/wiki/DBSCAN>).
Reference: Ester, Martin et al. *A density-based algorithm for
discovering clusters in large spatial databases with noise*. Proceedings
of the Second International Conference on Knowledge Discovery and Data
Mining. AAAI Press. 1996. pp. 226--231.

2\. In the subsequent stage, clusters are converted into convex polgons.
Refer to the Code-API documentation for details.

All single points that do not define a cluster (noise) are also treated
as polygons (represented as a single vertex each)

Examples are depicted in the following figures. Only yellow cells are
occupied cost cells (without inflation)! Additionally, just the local
map has been converted and not the complete static map.

![Conversion to convex polygons](doc/costmap_converter_convex_hull.png)
![Conversion to convex polygons](doc/CostmapToPolygonsDBSMCCH_2.png)

#### Parameters

- `~<name>/cluster_max_distance` (`double`, default: `0.4`): Parameter
  for DB_Scan, maximum distance to neighbors \[m\]
- `~<name>/cluster_min_pts` (`int`, default: `2`): Parameter for
  DB_Scan: minimum number of points that define a cluster
- `~<name>/cluster_max_pts` (`int`, default: `30`): Parameter for
  DB_Scan: maximum number of points that define a cluster (limit cluster
  size to avoid large L- and U-shapes)
- `~<name>/convex_hull_min_pt_separation` (`double`, default: `0.1`):
  Clear keypoints/vertices of the convex polygon that are close to each
  other \[distance in meters\] (0: keep all)

### CostmapToPolygonsDBSConcaveHull

This plugin converts occupied cells to a set of non-convex (concave)
polygons. The conversion is performed in three stages: 1. Generate
clusters using DBSCAN. 2. Convert clusters to convex polygons. 3.
Convert convex polygons to concave polygons Reference: J.-S. Park et al.
*A New Concave Hull Algorithm and Concaveness Measure for n-dimensional
Datasets*. Journal of Information Science & Engineering 28 (2012) 3.

Examples are depicted in the following figures. Only yellow cells are
occupied cost cells (without inflation)! Additionally, just the local
map has been converted and not the complete static map.

![Conversion to concave polygons](doc/costmap_converter_concave_hull.png)

#### Parameters

- `~<name>/cluster_max_distance` (`double`, default: `0.4`): Parameter
  for DB_Scan, maximum distance to neighbors \[m\]
- `~<name>/cluster_min_pts` (`int`, default: `2`): Parameter for
  DB_Scan: minimum number of points that define a cluster
- `~<name>/cluster_max_pts` (`int`, default: `30`): Parameter for
  DB_Scan: maximum number of points that define a cluster (limit cluster
  size to avoid large L- and U-shapes)
- `~<name>/convex_hull_min_pt_separation` (`double`, default: `0.1`):
  Clear keypoints/vertices of the convex polygon that are close to each
  other \[distance in meters\] (0: keep all)
- `~<name>/concave_hull_depth` (`double`, default: `2.0`): Smaller
  depth: sharper surface, large depth: convex hull

### CostmapToLinesDBSMCCH

This plugin converts occupied cells to a set of lines (and points). This
plugin converts occupied cells to a set of non-convex (concave)
polygons. The conversion is performed in three stages: 1. Generate
clusters using DBSCAN. 2. Convert clusters to convex polygons. 3.
Convert polygon edges to lines if there exist at least a predefined
number of support points.

Examples are depicted in the following figures. Only yellow cells are
occupied cost cells (without inflation)! Additionally, just the local
map has been converted and not the complete static map. Converted points
and polygons are colored in red while lines are colored in green.

![Conversion to lines](doc/costmap_converter_convex_hull_lines.png)
![Conversion to lines](doc/CostmapToLinesDBSMCCH_1.png)

#### Parameters

- `~<name>/cluster_max_distance` (`double`, default: `0.4`): Parameter
  for DB_Scan, maximum distance to neighbors \[m\]
- `~<name>/cluster_min_pts` (`int`, default: `2`): Parameter for
  DB_Scan: minimum number of points that define a cluster
- `~<name>/cluster_max_pts` (`int`, default: `30`): Parameter for
  DB_Scan: maximum number of points that define a cluster (limit cluster
  size to avoid large L- and U-shapes)
- `~<name>/convex_hull_min_pt_separation` (`double`, default: `0.1`):
  Clear keypoints/vertices of the convex polygon that are close to each
  other \[distance in meters\] (0: keep all)
- `~<name>/support_pts_max_dist` (`double`, default: `0.3`): Minimum
  distance from a point to the line to be counted as support point
- `~<name>/support_pts_max_dist_inbetween` (`double`, default: `1.0`): A
  line is only defined, if the distance between two consecutive support
  points is less than this treshold. Set to 0 in order to deactivate
  this check.
- `~<name>/min_support_pts` (`int`, default: `2`): Minimum number of
  support points required to represent a line.

### CostmapToLinesDBSRANSAC

This plugin converts occupied cells to a set of lines (and points). The
conversion is performed in two stages: 1. Generate clusters using
DBSCAN. 2. RANSAC algorithm is used to find straight line segment models
(<https://en.wikipedia.org/wiki/RANSAC>) RANSAC is invoked repeatedly to
find multiple lines per cluster until the number of inliers is below a
specific threshold. Outliers are also treated as polygons (represented
as a single vertex each). Resulting lines of RANSAC are currently not
refined by linear regression.

Examples are depicted in the following figures. Only yellow cells are
occupied cost cells (without inflation)! Additionally, just the local
map has been converted and not the complete static map. Converted points
and polygons are colored in red while lines are colored in green.

![Conversion to lines](doc/CostmapToLinesDBSRANSAC_2.png)
![Conversion to lines](doc/CostmapToLinesDBSRANSAC_4.png)

#### Parameters

- `~<name>/cluster_max_distance` (`double`, default: `0.4`): Parameter
  for DB_Scan, maximum distance to neighbors \[m\]
- `~<name>/cluster_min_pts` (`int`, default: `2`): Parameter for
  DB_Scan: minimum number of points that define a cluster
- `~<name>/cluster_max_pts` (`int`, default: `30`): Parameter for
  DB_Scan: maximum number of points that define a cluster (limit cluster
  size to avoid large L- and U-shapes)
- `~<name>/ransac_inlier_distance` (`double`, default: `0.2`): Maximum
  distance to the line segment for inliers \[in meters\].
- `~<name>/ransac_min_inliers` (`int`, default: `10`): Minimum numer of
  inliers required to form a line.
- `~<name>/ransac_no_iterations` (`int`, default: `2000`): Number of
  ransac iterations per cluster.
- `~<name>/ransac_remainig_outliers` (`int`, default: `3`): Abort ransac
  iterations if the number of outliers is equal or below the value
  specified here.
- `~<name>/ransac_convert_outlier_pts` (`bool`, default: `true`):
  Convert remaining outliers to single points.
- `~<name>/ransac_filter_remaining_outlier_pts` (`bool`, default:
  `false`): Filter the interior of remaining outliers and keep only
  keypoints of their convex hull.
- `~<name>/convex_hull_min_pt_separation` (`double`, default: `0.1`):
  Clear keypoints/vertices of the convex polygon that are close to each
  other \[distance in meters\] (0: keep all)

## Standalone Node

The costmap_converter interface is intended to be directly included in
the source code. However, sometimes it could be useful to convert an
incoming
[nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)
Message (e.g. as published by
[navigation](https://index.ros.org/p/navigation)).

For that purpose the internal `standalone_converter` node
(*costmap_converter_node.cpp*) might be employed. Currently, parameters
are hardcoded. These are going to be substituted with changeble
parameters in an upcoming release. Before then please inspect the source
code for further details.
