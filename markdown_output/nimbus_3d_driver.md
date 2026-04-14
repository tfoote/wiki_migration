Official ROS driver for the
[Nimbus 3D](https://shop.pieye.org/en/Cameras/Nimbus-3D-camera.html)
time-of-flight camera.

```wiki
This package is still in development and the API might change in the future. Please report any bugs or feature requests on [[https://github.com/pieye/nimbus-ros/issues|GitHub]].
```

## Overview

![Nimbus 3D (Nimbus 3D is a ToF camera in the Raspberry Pi form factor.)\|width=\"350\"](attachment:raspberry_nimbus.png)

### Time-of-flight measuring principle

-   The time-of-flight technology is successfully established on the
    market since a lot of years. Nimbus 3D makes this technology
    available to the Raspberry Pi now. The time-of-flight technology
    measures the distance between objects and camera through the light
    propagation time with the help of modulated light pulses.

### Applications

-   The compact form factor opens a wide range of applications. Starting
    from people counting over gesture recognition to volume
    measurements, the only boundary is your imagination.

### Technical data

-   Resolution: 352 x 288
-   Measurement range: 0,1 m -- 5 m
-   Field of view: 66° x 54° (H x V)
-   Framerate: up to 30fps
-   Imager: Infineon REAL3 IRS1125A
-   Output: 3D-point cloud, amplitude, radial and confidence

The \'\'nimbus_3d_driver\'\' is the official ROS driver for the
\'\'Nimbus 3D\'\' which provides ROS parameters (configuration) and ROS
topics (sensor data: Images and Point Cloud).

Fruthermore here is the official
[documentation](https://nimbus-docs.readthedocs.io/en/latest/index.html)
for the Nimbus 3D.

## Configuration

### Parameters

The following parameters can be changed during runtime or in the given
config file.

-   /nimbus_ros_node/amplitude \[0 - 3000\]
-   /nimbus_ros_node/downsampling \[true \| false\]
-   /nimbus_ros_node/downsampling_voxel_size \[0.0 - 1.0\]
-   /nimbus_ros_node/hdr_factor \[0.0 - 1.0\]
-   /nimbus_ros_node/exposure_mode \[-1 (manual), 0 (default), 1 (Auto),
    2 (HDR)\]
-   /nimbus_ros_node/intensity_image \[true \| false\]
-   /nimbus_ros_node/max_exposure \[0 - 32766\]
-   /nimbus_ros_node/pointcloud \[true \| false\]
-   /nimbus_ros_node/range_image \[true \| false\]

## Provided Topics

### Point Cloud, Images

The following topics are provided.

-   /nimbus/camera/info (sensor_msgs::CameraInfo)
-   /nimbus/info/exposure (std_msgs::Float32)
-   /nimbus/info/temperature (std_msgs::Float32)
-   /nimbus/intensity_image (sensor_msgs::Image, MONO8)
-   /nimbus/pointcloud (sensor_msgs::PointCloud2, XYZI)
-   /nimbus/range_image (sensor_msgs::Image, RGB8)

## Relevant Coordinate Frames

The following coordinate frames are relevant for interpreting the data
provided by the Nimbus 3D:

-   \`camera\`: The imager center of the Nimbus 3D camera. All camera
    data such as images and point clouds are given in this frame.
-   \`world\`: Transformation from the camera to the world coordinates.
    By default, a simple static transform is published in the launch
    file. This should be changed according to the given application.

## Installation and Launch

Detailed Information to install the driver can be found in the
[GitHub README](https://github.com/pieye/nimbus-ros).

## Report a Bug

\<\<GitHubIssues(pieye/nimbus-ros)\>\>
