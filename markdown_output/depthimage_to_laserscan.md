## Overview / Example Scene

### RGB

Here is the scene in which the following screenshots were captured.

![attachment:scene.jpg](doc/scene.jpg)

### DepthImage

Note the
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
overlayed in color on the
[sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html).
Red is close to camera, purple is far from camera.

![attachment:depthimage.png](doc/depthimage.png)

### LaserScan

[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
projected on top of the
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html).

![attachment:pointcloud.png](doc/pointcloud.png)

### Top Down LaserScan

Top down view of the
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html).

![attachment:overhead_scan.png](doc/overhead_scan.png)

## Node

### depthimage_to_laserscan

`depthimage_to_laserscan` takes a depth image (float encoded meters or
preferably uint16 encoded millimeters for OpenNI devices) and generates
a 2D laser scan based on the provided parameters.
depthimage_to_laserscan uses lazy subscribing and will not subscribe to
`image` or `camera_info` until there is a subscriber for `scan`.

#### Subscribed Topics

- `image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  The input image that must conform to
  [REP 118](http://ros.org/reps/rep-0118.html). This can be floating
  point or raw uint16 format. For OpenNI devices, uint16 is the native
  representation and will be more efficient for processing. This is
  typically `/camera/depth/image_raw`. If your image is distorted,
  this topic should be remapped to `image_rect`. OpenNI cameras
  typically have little distortion and rectification can be skipped for
  this application.
- `camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Camera info for the associated image. Does not usually need to be
  remampped as camera_info will be subscribed to from the same namespace
  as `image`.

#### Published Topics

- `scan`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  The output laser scan. Follows
  [REP 117](http://ros.org/reps/rep-0117.html), and will output range
  arrays that contain !NaNs and +-Infs.

#### Parameters

- `~scan_height` (`int`, default: `1 pixel`): The number of pixel rows
  to use to generate the laserscan. For each column, the scan will
  return the minimum value for those pixels centered vertically in the
  image.
- `~scan_time` (`double`, default: `1/30.0Hz (0.033s)`): Time between
  scans (seconds). Typically, 1.0/frame_rate. This value is not easily
  calculated from consecutive messages, and is thus left to the user to
  set correctly.
- `~range_min` (`double`, default: `0.45m`): The minimum ranges to
  return in meters. Ranges less than this will be output as -Inf.
- `~range_max` (`double`, default: `10.0m`): The maximum ranges to
  return in meters. Ranges greater than this will be output as +Inf.
- `~output_frame_id` (`str`, default: `camera_depth_frame`): The frame
  id of the laser scan. For point clouds coming from an "optical"
  frame with Z forward, this value should be set to the corresponding
  frame with X forward and Z up.

## Nodelet

Same usage as the Node.

Available as:

`depthimage_to_laserscan/DepthImageToLaserScanNodelet`

## Installation

<https://github.com/ros-perception/depthimage_to_laserscan>
