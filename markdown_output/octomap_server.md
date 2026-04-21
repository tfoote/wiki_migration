## Overview

General information about !OctoMap is available at
<http://octomap.github.com> and in the publication
["OctoMap: An Efficient Probabilistic 3D Mapping Framework Based on Octrees"](http://www.informatik.uni-freiburg.de/~hornunga/pub/hornung13auro.pdf)
by A. Hornung, K. M. Wurm, M. Bennewitz, C. Stachniss, and W. Burgard
(Autonomous Robots Journal, 2013).

BibTeX: ```
@ARTICLE{hornung13auro,
  author = {Armin Hornung and Kai M. Wurm and Maren Bennewitz and Cyrill
  Stachniss and Wolfram Burgard},
  title = {{OctoMap}: An Efficient Probabilistic {3D} Mapping Framework Based
  on Octrees},
  journal = {Autonomous Robots},
  year = 2013,
  url = {http://octomap.github.com},
  doi = {10.1007/s10514-012-9321-0},
  note = {Software available at \url{http://octomap.github.com}}
}
``` Please cite our paper if you use
!OctoMap in your research.

## ROS Node API

### dynamic_reconfigure API

**octomap_server** and **octomap_server_multilayer** offer a
dynamic_reconfigure interface to change the displayed map resolution on
the fly (since version 0.3.8). Note that this will not change the
resolution of the underlying OctoMap, but only of the published marker /
collision topics (e.g. for visualization).

```clearsilver
node.0 {
 name = octomap_server
 desc = octomap_server builds and distributes volumetric 3D occupancy maps as !OctoMap binary stream and in various ROS-compatible formats e.g. for obstacle avoidance or visualization. The map can be a static !OctoMap .bt file (as command line argument) or can be incrementally built from incoming range data (as !PointCloud2). octomap_server starts with an empty map if no command line argument is given. In general, octomap_server creates and publishes only on topics that are subscribed. Since some can be time-consuming to build for large maps, only subscribe to topics you absolutely need (e.g. in RViz) and set the "latch" parameter for false when building maps.
 sub{
  0.name = cloud_in
  0.type = sensor_msgs/PointCloud2
  0.desc = Incoming 3D point cloud for scan integration. You need to remap this topic to your sensor data and provide a tf transform between the sensor data and the static map frame. The frame_id of the point cloud has to be the sensor frame. Raytracing (clearing of free space) is always done from the origin of this frame at the time of the point cloud.
 }
 pub{
  0.name = octomap_binary
  0.type = octomap_msgs/Octomap
  0.desc = The complete maximum-likelihood occupancy map as compact !OctoMap binary stream, encoding free and occupied space. The binary message only distinguishes between free and occupied space but is smaller. See [[octomap_msgs]] for deserializing the message.

  1.name = octomap_full
  1.type = octomap_msgs/Octomap
  1.desc = The complete maximum-likelihood occupancy map as compact !OctoMap binary stream, encoding free and occupied space. The full message contains the complete probabilities and all additional data stored in the tree. See [[octomap_msgs]] for deserializing the message.

  2.name = occupied_cells_vis_array
  2.type = visualization_msgs/MarkerArray
  2.desc = All occupied voxels as "box" markers for visualization in RViz. Be sure to subscribe to the topic '''occupied_cells_vis''' in RViz!
  3.name = octomap_point_cloud_centers
  3.type = sensor_msgs/PointCloud2
  3.desc = The centers of all occupied voxels as point cloud, useful for visualization. Note that this will have gaps as the points have no volumetric size and !OctoMap voxels can have different resolutions! Use the !MarkerArray topic instead.

  4.name = map (up to fuerte) / projected_map (since fuerte)
  4.type = nav_msgs/OccupancyGrid
  4.desc = Downprojected 2D occupancy map from the 3D map. Be sure to remap this topic if you have another 2D map server running. '''New / changed in octomap_mapping 0.4.4''': The topic is now `projected_map` by default to avoid collisions with static 2D maps
 }
srv{
  0.name = octomap_binary
  0.type = octomap_msgs/GetOctomap
  0.desc = The complete maximum-likelihood occupancy map as compact !OctoMap binary stream, encoding free and occupied space.

  1.name = ~clear_bbx
  1.type = octomap_msgs/BoundingBoxQuery
  1.desc = Clears a region in the 3D occupancy map, setting all voxels in the region to "free"
  2.name = ~reset
  2.type = std_srvs/Empty
  2.desc = Resets the complete map
 }

req_tf{
  0.from = sensor data frame
  0.to = /map (static world frame, changeable with parameter frame_id)
  0.desc = Required transform of sensor data into the global map frame if you do scan integration. This information needs to be available from an external SLAM or localization node.
}

param {
  1.name = ~frame_id
  1.type = string
  1.desc = Static global frame in which the map will be published. A transform from sensor data to this frame needs to be available when dynamically building maps.
  1.default = /map

  2.name = ~resolution
  2.type = float
  2.desc = Resolution in meter for the map when starting with an empty map. Otherwise the loaded file's resolution is used.
  2.default = 0.05

  3.name = ~base_frame_id
  3.type = string
  3.desc = The robot's base frame in which ground plane detection is performed (if enabled)
  3.default = base_footprint

  4.name = ~height_map
  4.type = bool
  4.desc = Whether visualization should encode height with different colors
  4.default = true

  5.name = ~color/[r/g/b/a]
  5.type = float
  5.desc = Color for visualizing occupied cells when ~heigh_map=False, in range [0:1]

  6.name= ~sensor_model/max_range
  6.type = float
  6.desc = Maximum range in meter for inserting point cloud data when dynamically building a map. Limiting the range to something useful (e.g. 5m) prevents spurious erroneous points far away from the robot.
  6.default = -1 (unlimited)

  7.name = ~sensor_model/[hit|miss]
  7.type = float
  7.desc = Probabilities for hits and misses in the sensor model when dynamically building a map
  7.default = 0.7 / 0.4

  8.name = ~sensor_model/[min|max]
  8.type = float
  8.desc = Minimum and maximum probability for clamping when dynamically building a map
  8.default = 0.12 / 0.97

  9.name = ~latch
  9.type = bool
  9.desc = Whether topics are published latched or only once per change. For maximum performance when building a map (with frequent updates), set to false. When set to true, on every map change all topics and visualizations will be created.
  9.default = True for a static map, false if no initial map is given 

  10.name = ~filter_ground
  10.type = bool
  10.desc = Whether the ground plane should be detected and ignored from scan data when dynamically building a map, using pcl::SACMODEL_PERPENDICULAR_PLANE. This clears everything up to the ground, but will not insert the ground as obstacle in the map. If this is enabled, it can be further configured with the ~ground_filter/... parameters.
  10.default = false

  11.name = ~ground_filter/distance
  11.type = float
  11.desc = Distance threshold for points (in z direction) to be segmented to the ground plane
  11.default = 0.04

  12.name = ~ground_filter/angle
  12.type = float
  12.desc = Angular threshold of the detected plane from the horizontal plane to be detected as ground
  12.default = 0.15

  13.name = ~ground_filter/plane_distance
  13.type = float
  13.desc = Distance threshold from z=0 for a plane to be detected as ground (4th coefficient of the plane equation from PCL)
  13.default = 0.07

  15.name = ~pointcloud_[min|max]_z
  15.type = float
  15.desc = Minimum and maximum height of points to consider for insertion in the callback. Any point outside of this intervall will be discarded before running any insertion or ground plane filtering. You can do a rough filtering based on height with this, but if you enable the ground_filter this interval needs to include the ground plane.
  15.default = -/+ infinity

  16.name = ~occupancy_[min|max]_z
  16.type = float
  16.desc = Minimum and maximum height of occupied cells to be consider in the final map. This ignores all occupied voxels outside of the interval when sending out visualizations and collision maps, but will not affect the actual octomap representation.
  16.default = -/+ infinity
}
}

node.1 {
 name = octomap_server_multilayer
 desc = An extension of octomap_server to publish multilayer projected 2D maps, used by the [[3d_navigation]] stack. Subscriptions and publications are mostly identical to the octomap_server node.
}

node.2 {
 name = octomap_saver
 desc = A small command line tool to request octomap files from an octomap_server, similar to [[map_server#map_saver]]. Just run "octomap_saver mapfile.bt" to request a compressed binary octomap via service call and save it to mapfile.bt. Run "octomap_saver -f mapfile.ot" to request a full probability octomap instead (Requires version 0.5 or later).
}
```

## Report a Bug

Use the octomap
[issue tracker](https://github.com/OctoMap/octomap_mapping/issues) to
report bugs or request features. For questions (and FAQ), check
[answers.ros.org](http://answers.ros.org/questions/scope:all/sort:activity-desc/tags:octomap/page:1/).
