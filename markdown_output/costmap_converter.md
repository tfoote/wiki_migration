## Overview

This package defines an [pluginlib](pluginlib) interface and provides
some plugins for converting occupied cells of [costmap_2d](costmap_2d)
to geometric primitives. This primitives (points, lines, polygons)
represent obstacles in the map. It is intendend for nodes that
incorporate obstacles (e.g. in navigation) and do not rely on cost
cells, but consider obstacles defined by shapes in the plane (e.g.
polygons). The costmap is still favorable in conjunction with
[navigation](navigation) since it fuses multiple range sensors with a
global static map and some filtering might be applied. A naive approach
to further incorporate the costmap is to take each occupied cell as
point-obstacle. However, by integrating the costmap_converter interface
the costmap is converted continuously during runtime and if desired the
conversion is invoked in a separate thread.

The tutorial section is going to be added in the future. Before then,
refer to the example implementation in
[teb_local_planner](teb_local_planner) package or to the implementation
of the [standalone node](costmap_converter#Standalone_Node).

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

![Conversion to convex polygons\|width="350"](attachment:costmap_converter_convex_hull.png)
![Conversion to convex polygons\|width="325"](attachment:CostmapToPolygonsDBSMCCH_2.png)

#### Parameters



```clearsilver
param{
  no_header=True
  0.name = ~<name>/cluster_max_distance
  0.default = 0.4
  0.type = double
  0.desc = Parameter for DB_Scan, maximum distance to neighbors [m]
  1.name = ~<name>/cluster_min_pts
  1.default = 2
  1.type = int
  1.desc = Parameter for DB_Scan: minimum number of points that define a cluster
  2.name = ~<name>/cluster_max_pts
  2.default = 30
  2.type = int
  2.desc = Parameter for DB_Scan: maximum number of points that define a cluster (limit cluster size to avoid large L- and U-shapes)
  3.name = ~<name>/convex_hull_min_pt_separation
  3.default = 0.1
  3.type = double
  3.desc = Clear keypoints/vertices of the convex polygon that are close to each other [distance in meters] (0: keep all)
}
```



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

![Conversion to concave polygons\|width="350"](attachment:costmap_converter_concave_hull.png)

#### Parameters



```clearsilver
param{
  no_header=True
  0.name = ~<name>/cluster_max_distance
  0.default = 0.4
  0.type = double
  0.desc = Parameter for DB_Scan, maximum distance to neighbors [m]
  1.name = ~<name>/cluster_min_pts
  1.default = 2
  1.type = int
  1.desc = Parameter for DB_Scan: minimum number of points that define a cluster
  2.name = ~<name>/cluster_max_pts
  2.default = 30
  2.type = int
  2.desc = Parameter for DB_Scan: maximum number of points that define a cluster (limit cluster size to avoid large L- and U-shapes)
  3.name = ~<name>/convex_hull_min_pt_separation
  3.default = 0.1
  3.type = double
  3.desc = Clear keypoints/vertices of the convex polygon that are close to each other [distance in meters] (0: keep all)
  4.name = ~<name>/concave_hull_depth
  4.default = 2.0
  4.type = double
  4.desc = Smaller depth: sharper surface, large depth: convex hull
}
```



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

![Conversion to lines\|width="350"](attachment:costmap_converter_convex_hull_lines.png)
![Conversion to lines\|width="350"](attachment:CostmapToLinesDBSMCCH_1.png)

#### Parameters



```clearsilver
param{
  no_header=True
  0.name = ~<name>/cluster_max_distance
  0.default = 0.4
  0.type = double
  0.desc = Parameter for DB_Scan, maximum distance to neighbors [m]
  1.name = ~<name>/cluster_min_pts
  1.default = 2
  1.type = int
  1.desc = Parameter for DB_Scan: minimum number of points that define a cluster
  2.name = ~<name>/cluster_max_pts
  2.default = 30
  2.type = int
  2.desc = Parameter for DB_Scan: maximum number of points that define a cluster (limit cluster size to avoid large L- and U-shapes)
  3.name = ~<name>/convex_hull_min_pt_separation
  3.default = 0.1
  3.type = double
  3.desc = Clear keypoints/vertices of the convex polygon that are close to each other [distance in meters] (0: keep all)
  4.name = ~<name>/support_pts_max_dist
  4.default = 0.3
  4.type = double
  4.desc = Minimum distance from a point to the line to be counted as support point
  5.name = ~<name>/support_pts_max_dist_inbetween
  5.default = 1.0
  5.type = double
  5.desc = A line is only defined, if the distance between two consecutive support points is less than this treshold. Set to 0 in order to deactivate this check.
  6.name = ~<name>/min_support_pts
  6.default = 2
  6.type = int
  6.desc = Minimum number of support points required to represent a line.
}
```



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

![Conversion to lines\|width="350"](attachment:CostmapToLinesDBSRANSAC_2.png)
![Conversion to lines\|width="350"](attachment:CostmapToLinesDBSRANSAC_4.png)

#### Parameters



```clearsilver
param{
  no_header=True
  0.name = ~<name>/cluster_max_distance
  0.default = 0.4
  0.type = double
  0.desc = Parameter for DB_Scan, maximum distance to neighbors [m]
  1.name = ~<name>/cluster_min_pts
  1.default = 2
  1.type = int
  1.desc = Parameter for DB_Scan: minimum number of points that define a cluster
  2.name = ~<name>/cluster_max_pts
  2.default = 30
  2.type = int
  2.desc = Parameter for DB_Scan: maximum number of points that define a cluster (limit cluster size to avoid large L- and U-shapes)
  3.name = ~<name>/ransac_inlier_distance
  3.default = 0.2
  3.type = double
  3.desc = Maximum distance to the line segment for inliers [in meters].
  4.name = ~<name>/ransac_min_inliers
  4.default = 10
  4.type = int
  4.desc = Minimum numer of inliers required to form a line.
  5.name = ~<name>/ransac_no_iterations
  5.default = 2000
  5.type = int
  5.desc = Number of ransac iterations per cluster.
  6.name = ~<name>/ransac_remainig_outliers
  6.default = 3
  6.type = int
  6.desc = Abort ransac iterations if the number of outliers is equal or below the value specified here.
  7.name = ~<name>/ransac_convert_outlier_pts
  7.default = true
  7.type = bool
  7.desc = Convert remaining outliers to single points.
  8.name = ~<name>/ransac_filter_remaining_outlier_pts
  8.default = false
  8.type = bool
  8.desc = Filter the interior of remaining outliers and keep only keypoints of their convex hull.
  9.name = ~<name>/convex_hull_min_pt_separation
  9.default = 0.1
  9.type = double
  9.desc = Clear keypoints/vertices of the convex polygon that are close to each other [distance in meters] (0: keep all)

}
```



## Standalone Node

The costmap_converter interface is intended to be directly included in
the source code. However, sometimes it could be useful to convert an
incoming
[nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)
Message (e.g. as published by [navigation](navigation)).

For that purpose the internal `standalone_converter` node
(*costmap_converter_node.cpp*) might be employed. Currently, parameters
are hardcoded. These are going to be substituted with changeble
parameters in an upcoming release. Before then please inspect the source
code for further details.
