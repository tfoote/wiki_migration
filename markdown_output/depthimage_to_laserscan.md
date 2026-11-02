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



```clearsilver
node.0 {
 name = depthimage_to_laserscan
 desc = `depthimage_to_laserscan` takes a depth image (float encoded meters or preferably uint16 encoded millimeters for OpenNI devices) and generates a 2D laser scan based on the provided parameters.  depthimage_to_laserscan uses lazy subscribing and will not subscribe to `image` or `camera_info` until there is a subscriber for `scan`.
 sub{
  0.name= image
  0.type= sensor_msgs/Image
  0.desc << EOM
The input image that must conform to [[http://ros.org/reps/rep-0118.html|REP 118]].  This can be floating point or raw uint16 format.  For OpenNI devices, uint16 is the native representation and will be more efficient for processing.  This is typically `/camera/depth/image_raw`.  If your image is distorted, this topic should be remapped to `image_rect`.  OpenNI cameras typically have little distortion and rectification can be skipped for this application.
EOM
  1.name= camera_info
  1.type= sensor_msgs/CameraInfo
  1.desc= Camera info for the associated image.  Does not usually need to be remampped as camera_info will be subscribed to from the same namespace as `image`.
  }
 pub {
  0.name= scan
  0.type= sensor_msgs/LaserScan
  0.desc= The output laser scan.  Follows [[http://ros.org/reps/rep-0117.html|REP 117]], and will output range arrays that contain !NaNs and +-Infs.
 }
 param {
  0.name= ~scan_height
  0.default= 1 pixel
  0.type= int
  0.desc= The number of pixel rows to use to generate the laserscan.  For each column, the scan will return the minimum value for those pixels centered vertically in the image.
  2.name= ~scan_time
  2.default= 1/30.0Hz (0.033s)
  2.type= double
  2.desc= Time between scans (seconds).  Typically, 1.0/frame_rate. This value is not easily calculated from consecutive messages, and is thus left to the user to set correctly.
  3.name= ~range_min
  3.default= 0.45m
  3.type= double
  3.desc= The minimum ranges to return in meters.  Ranges less than this will be output as -Inf.
  4.name= ~range_max
  4.default= 10.0m
  4.type= double
  4.desc= The maximum ranges to return in meters.  Ranges greater than this will be output as +Inf.
  5.name= ~output_frame_id
  5.default= camera_depth_frame
  5.type= str
  5.desc= The frame id of the laser scan. For point clouds coming from an "optical" frame with Z forward, this value should be set to the corresponding frame with X forward and Z up.
 }
}
}
```



## Nodelet

Same usage as the Node.

Available as:

`depthimage_to_laserscan/DepthImageToLaserScanNodelet`

## Installation

<https://github.com/ros-perception/depthimage_to_laserscan>
