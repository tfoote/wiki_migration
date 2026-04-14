\<\<GitHubIssues(jstnhuang/surface_perception)\>\>

## Overview

![demo\|width=100%](attachment:demoImage.png)

\`surface_perception\` is a simple tabletop/shelf perception pipeline.

[surface_perception::Segmentation](http://docs.ros.org/indigo/api/surface_perception/html/classsurface__perception_1_1Segmentation.html)
is the main API. It takes in a point cloud, where the positive \"z\"
direction points up. It also assumes that the point cloud has been
cropped down to a tabletop/shelf scene.

Example: ```cplusplus
surface_perception::Segmentation seg;
seg.set_input_cloud(pcl_cloud);

// (Optional) Set the particular indices to be used in the input point cloud,
// for the segmentation operation. If the indices is not set, the entire
// input cloud will be used.
seg.set_indices(point_indices);

// (Optional, default 10) Set the maximum difference between the normal
// vector of surfaces and the z-axis.
seg.set_horizontal_tolerance_degrees(10);

// (Optional, default 0.005) Set the maximum distance between the surface
// inliers and the plane that represents the surface.
seg.set_margin_above_surface(0.01);

// (Optional, default 0.01) Set the required distance between each cluster
// corresponding to each object, during the object extraction.
seg.set_cluster_distance(0.01);

// (Optional, default 10) Set the minimum size of object clusters.
seg.set_min_cluster_size(10);

// (Optional, default 10000) Set the maximum size of object clusters.
seg.set_max_cluster_size(10000);

// (Optional, default 5000) Set the minimum number of inliers contained by a
// surface.
seg.set_min_surface_size(5000);

std::vector<SurfaceObjects> surface_objects;
bool success = seg.Segment(&surface_objects);
```

## Demo

To run the demo: ```
rosrun surface_perception demo target_point_cloud_frame cloud_in:=input_point_cloud_topic
``` If
\`target_point_cloud_frame\` is not provided, the point cloud will be
processed in \`base_link\`.

[surface_perception::SurfaceViz](http://docs.ros.org/indigo/api/surface_perception/html/classsurface__perception_1_1SurfaceViz.html)
visualizes the result: ```cplusplus
SurfaceViz viz(marker_pub);
viz.set_surface_objects(surface_objects);
viz.Show();

// Removes the visualization.
viz.Hide();
```

```clearsilver
  name = surface_perception_demo
  desc = This node runs the demo of surface_perception

  param {
    0.name = crop_min_x
    0.type = float
    0.default = 0.0
    0.desc = The minimum x coordinate of the cropped input cloud.
    1.name = crop_min_y
    1.type = float
    1.default = -0.5
    1.desc = The minimum y coordinate of the cropped input cloud.
    2.name = crop_min_z
    2.type = float
    2.default = 0.05
    2.desc = The minimum z coordinate of the cropped input cloud.
    3.name = crop_max_x
    3.type = float
    3.default = 1.3
    3.desc = The maximum x coordinate of the cropped input cloud.
    4.name = crop_max_y
    4.type = float
    4.default = 0.5
    4.desc = The maximum y coordinate of the cropped input cloud.
    5.name = crop_max_z
    5.type = float
    5.default = 2.0
    5.desc = The maximum z coordinate of the cropped input cloud.
    6.name = horizontal_tolerance_degrees
    6.type = float
    6.default = 10.0
    6.desc = The maximum degree difference between normal vector of a surface and the z-axis.
    7.name = margin_above_surface
    7.type = float
    7.default = 0.015
    7.desc = The the maximum distance between the surface and its inliers.
    8.name = cluster_distance
    8.type = float
    8.default = 0.01
    8.desc = The maximum cluster distance for object extraction.
    9.name = min_cluster_size
    9.type = integer
    9.default = 100
    9.desc = The minimum number of points for an extracted object.
    10.name = max_cluster_size
    10.type = integer
    10.default = 5000
    10.desc = The maximum number of points for an extracted object.
    11.name = min_surface_size
    11.type = integer
    11.default = 5000
    11.desc = The minimum number of points a surface must have.
    12.name = min_surface_exploration_iteration
    12.type = integer
    12.default = 1000
    12.desc = The minimum number of iteration that the surface exploration algorithm must go through.
  }
```
