## Overview

This package provides the driver for the SICK safeVisionary2 cameras.

## Installation

Please see the install instructions in the official
[Github repository](https://github.com/SICKAG/sick_safevisionary_ros1).

## ROS API

```clearsilver
name = sick_safevisionary
desc = Control node for the 3D camera. The node publishes to the following topics.
pub {
  0.name = camera_info
  0.type = sensor_msgs/CameraInfo
  0.desc = General camera information
  1.name = camera_io
  1.type = sick_safevisionary_msgs/CameraIO
  1.desc = Input output configurations and states
  2.name = depth
  2.type = sensor_msgs/Image
  2.desc = Depth measurements
  3.name = device_status
  3.type = sick_safevisionary_msgs/DeviceStatus
  3.desc = General camera status
  4.name = fields
  4.type = sick_safevisionary_msgs/FieldInformationArray
  4.desc = Fields information
  5.name = imu_data
  5.type = sensor_msgs/Imu
  5.desc = IMU measurements
  6.name = intensity
  6.type = sensor_msgs/Image
  6.desc = Intensity measurements
  7.name = points
  7.type = sensor_msgs/PointCloud2
  7.desc = The camera's point cloud measurements
  8.name = region_of_interest
  8.type = sick_safevisionary_msgs/ROIArray
  8.desc = The regions of interest
  9.name = state
  9.type = sensor_msgs/Image
  9.desc = The camera's pixel state map
}

param {
  0.name = ~frame_id
  0.type = string
  0.desc = The frame_id of the published messages' header
  0.default = camera
  1.name = ~udp_port
  1.type = int
  1.desc = The udp port on which to receive data from the camera. Users need to configure this once for each device. See the install instructions.
  1.default = 6060
}
```

## Additional Information

You'll find additional information in the official
[Github repository](https://github.com/SICKAG/sick_safevisionary_ros1).
