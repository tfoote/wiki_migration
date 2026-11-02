## Overview

This package provides the driver for the SICK safeVisionary2 cameras.

## Installation

Please see the install instructions in the official
[Github repository](https://github.com/SICKAG/sick_safevisionary_ros1).

## ROS API

### sick_safevisionary

Control node for the 3D camera. The node publishes to the following
topics.

#### Published Topics

- `camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  General camera information
- `camera_io`
  ([sick_safevisionary_msgs/msg/CameraIO](https://docs.ros.org/en/rolling/p/sick_safevisionary_msgs/msg/CameraIO.html)):
  Input output configurations and states
- `depth`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Depth measurements
- `device_status`
  ([sick_safevisionary_msgs/msg/DeviceStatus](https://docs.ros.org/en/rolling/p/sick_safevisionary_msgs/msg/DeviceStatus.html)):
  General camera status
- `fields`
  ([sick_safevisionary_msgs/msg/FieldInformationArray](https://docs.ros.org/en/rolling/p/sick_safevisionary_msgs/msg/FieldInformationArray.html)):
  Fields information
- `imu_data`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  IMU measurements
- `intensity`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Intensity measurements
- `points`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  The camera's point cloud measurements
- `region_of_interest`
  ([sick_safevisionary_msgs/msg/ROIArray](https://docs.ros.org/en/rolling/p/sick_safevisionary_msgs/msg/ROIArray.html)):
  The regions of interest
- `state`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  The camera's pixel state map

#### Parameters

- `~frame_id` (`string`, default: `camera`): The frame_id of the
  published messages' header
- `~udp_port` (`int`, default: `6060`): The udp port on which to receive
  data from the camera. Users need to configure this once for each
  device. See the install instructions.

## Additional Information

You'll find additional information in the official
[Github repository](https://github.com/SICKAG/sick_safevisionary_ros1).
