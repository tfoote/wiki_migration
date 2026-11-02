  -- ---------------------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ![Experimental](doc/1Column.png)      **EXPERIMENTAL**: This status indicates that this software is experimental code at best. There are known issues and missing functionality. The APIs are completely unstable and likely to change. Use in production systems is not recommended. All code starts at this level. For more information see the ROS-Industrial software status [page](Industrial/Software_Status).   
  -- ---------------------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

![PointCloud published by hokuyo3d node](doc/hokuyo3d_pointcloud.png)

## Supported Hardware

This driver should work with VSSP 1.0/1.1-compliant HOKUYO 3D-LIDARs.

## ROS API

<a id="NodeApi"></a>

### hokuyo3d

`hokuyo3d` is a driver for VSSP 1.0/1.1 (Volumetric Scanning Sensor
Protocol) compliant Hokuyo 3D LIDARs.

#### Published Topics

- `~/hokuyo_cloud`
  ([sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html)):
  Output of measured point cloud in PointCloud message type which
  contains all multi echos with intensity. Published on demand.
- `~/hokuyo_cloud2`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  Output of measured point cloud in PointCloud2 message type which
  contains all multi echos with intensity. Published on demand.
- `~/imu`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Output of embedded 6D gyro and accelerometer data.
- `~/mag`
  ([sensor_msgs/msg/MagneticField](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/MagneticField.html)):
  Output of embedded 3D magnetic field vector.

#### Parameters

- `~ip` (`string`, default: `"192.168.0.10"`): IP address of the sensor.
- `~port` (`int`, default: `10940`): TCP Port of the sensor.
- `~interlace` (`int`, default: `4`): Interlace setting of laser
  scanning. One means no interlace.
- `~frame_id` (`string`, default: `"hokuyo3d"`): The TF frame ID in
  which point clouds will be returned.
- `~range_min` (`float`, default: `0.0`): Points within range_min are
  dropped. This parameter is useful to remove ghost points nearby for
  early development version of this 3D sensors.
- `~output_cycle` (`string`, default: `"field"`): Specifies timing of
  point cloud output. "frame": outputs for each interlace cycle
  (several fields), "field": one horizontal scan (tens of lines),
  "line": one vertical scan
