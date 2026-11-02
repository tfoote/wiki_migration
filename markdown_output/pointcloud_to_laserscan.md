If you're trying to create a virtual laserscan from your RGBD device,
and your sensor is forward-facing, you'll find
[depthimage_to_laserscan](https://index.ros.org/p/depthimage_to_laserscan)
will be much more straightforward and efficient since it operates on
image data instead of bulky pointclouds. However, if your sensor is
angled, or you have some other esoteric use case, you may find this node
to be very helpful!

Please check the for common problems, or open an
[issue](https://github.com/ros-perception/pointcloud_to_laserscan/issues)
if still unsolved.

## Node



```clearsilver
node.0 {
 name = pointcloud_to_laserscan_node
 desc = `pointcloud_to_laserscan_node` takes a point cloud and generates a 2D laser scan based on the provided parameters.
 sub{
  0.name= cloud_in
  0.type= sensor_msgs/PointCloud2
  0.desc= The input point cloud.
  }
 pub {
  0.name= scan
  0.type= sensor_msgs/LaserScan
  0.desc= The output laser scan.
 }
 param {
  0.name= ~min_height
  0.default= 0.0
  0.type= double
  0.desc= The minimum height to sample in the point cloud in meters.
  1.name= ~max_height
  1.default= 1.0
  1.type= double
  1.desc= The maximum height to sample in the point cloud in meters.
  2.name= ~angle_min
  2.default= -&pi;/2
  2.type= double
  2.desc= The minimum scan angle in radians.
  3.name= ~angle_max
  3.default= &pi;/2
  3.type= double
  3.desc= The maximum scan angle in radians.
  4.name= ~angle_increment
  4.default= &pi;/360
  4.type= double
  4.desc= Resolution of laser scan in radians per ray.
  5.name= ~scan_time
  5.default= 1.0/30.0
  5.type= double
  5.desc= The scan rate in seconds.
  6.name= ~range_min
  6.default= 0.45
  6.type= double
  6.desc= The minimum ranges to return in meters.
  7.name= ~range_max
  7.default= 4.0
  7.type= double
  7.desc= The maximum ranges to return in meters.
  8.name= ~target_frame
  8.default= none
  8.type= str
  8.desc= If provided, transform the pointcloud into this frame before converting to a laser scan. Otherwise, laser scan will be generated in the same frame as the input point cloud.
  9.name= ~concurrency_level
  9.default= 1
  9.type= int
  9.desc= Number of threads to use for processing pointclouds. If 0, automatically detect number of cores and use the equivalent number of threads. Input queue size for pointclouds is tied to this parameter. In nodelet form, number of threads is capped by the nodelet manager configuration.
  10.name= ~use_inf
  10.default= true
  10.type= boolean
  10.desc= If disabled, report infinite range (no obstacle) as `range_max + 1`. Otherwise report infinite range as `+inf`. Associated with the `inf_is_valid` parameter for [[costmap_2d]] obstacle layers.
 }
}
```



## Nodelet

Same API as node, available as
`pointcloud_to_laserscan/pointcloud_to_laserscan_nodelet`.
