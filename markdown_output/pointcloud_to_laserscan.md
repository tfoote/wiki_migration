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

### pointcloud_to_laserscan_node

`pointcloud_to_laserscan_node` takes a point cloud and generates a 2D
laser scan based on the provided parameters.

#### Subscribed Topics

- `cloud_in`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  The input point cloud.

#### Published Topics

- `scan`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  The output laser scan.

#### Parameters

- `~min_height` (`double`, default: `0.0`): The minimum height to sample
  in the point cloud in meters.
- `~max_height` (`double`, default: `1.0`): The maximum height to sample
  in the point cloud in meters.
- `~angle_min` (`double`, default: `-&pi;/2`): The minimum scan angle in
  radians.
- `~angle_max` (`double`, default: `&pi;/2`): The maximum scan angle in
  radians.
- `~angle_increment` (`double`, default: `&pi;/360`): Resolution of
  laser scan in radians per ray.
- `~scan_time` (`double`, default: `1.0/30.0`): The scan rate in
  seconds.
- `~range_min` (`double`, default: `0.45`): The minimum ranges to return
  in meters.
- `~range_max` (`double`, default: `4.0`): The maximum ranges to return
  in meters.
- `~target_frame` (`str`, default: `none`): If provided, transform the
  pointcloud into this frame before converting to a laser scan.
  Otherwise, laser scan will be generated in the same frame as the input
  point cloud.
- `~concurrency_level` (`int`, default: `1`): Number of threads to use
  for processing pointclouds. If 0, automatically detect number of cores
  and use the equivalent number of threads. Input queue size for
  pointclouds is tied to this parameter. In nodelet form, number of
  threads is capped by the nodelet manager configuration.
- `~use_inf` (`boolean`, default: `true`): If disabled, report infinite
  range (no obstacle) as `range_max + 1`. Otherwise report infinite
  range as `+inf`. Associated with the `inf_is_valid` parameter for
  [costmap_2d](https://index.ros.org/p/costmap_2d) obstacle layers.

## Nodelet

Same API as node, available as
`pointcloud_to_laserscan/pointcloud_to_laserscan_nodelet`.
