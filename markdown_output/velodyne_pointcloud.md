## Overview

This package provides point cloud conversions for Velodyne 3D LIDARs.
For a list of all supported models refer to the
[Supported Devices](https://index.ros.org/p/velodyne_driver) section.

The
[API review](http://ros.org/wiki/velodyne/Reviews/2012-02-02_API_Review)
describes the evolution of these interfaces.: the default `min_range`
value is now 0.9 meters.: a new pair of parameters `view_direction`
and `view_width` may be used to reduce the output point cloud to a
subset of angular directions. By default, every angle is included in the
point cloud. Setting `view_width` to *pi/2* radians will limit the
output to 90 degrees around the forward direction of the device (from
-45 degrees to +45). Also setting `view_direction` to *pi* would
return output only from the device's rear facing, instead. Similarly,
setting `view_direction` to *-pi/2* would limit output to 90 degrees
around the right facing in the XY plane of the device frame of
reference.

## ROS Nodes and Nodelets

### CloudNodelet

This nodelet reads raw data from the `velodyne_packets` ROS topic,
converts to
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)
format, and republishes to `velodyne_points` ROS topic in the original
frame of reference (typically `/velodyne`). In addition to the XYZ
points, this cloud includes fields for "intensity" and "ring".

#### Subscribed Topics

- `velodyne_packets`
  ([velodyne_msgs/msg/VelodyneScan](https://docs.ros.org/en/rolling/p/velodyne_msgs/msg/VelodyneScan.html)):
  one or more raw Velodyne data packets from the device.

#### Published Topics

- `velodyne_points`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  accumulated Velodyne points transformed in the original frame of
  reference.

#### Parameters

- `~model` (`string`, default: `"64E"`): model of sensor being used.
  Currently supported are: "VLP16", "32C", "32E", "64E",
  "64E_S2", "64E_S2.1", "64E_S3"
- `~max_range` (`double`, default: `130.0`): maximum range (in meters)
  to publish; measurements further than this won't be published.
- `~min_range` (`double`, default: 0.9, formerly 2.0): minimum range (in
  meters) to publish; measurements closer than this won't be published.
- `~calibration` (`string`): YAML file containing device-specific
  calibration information.
- `~view_direction` (`double`, default: `0.0`):: center of view angle in
  radians in the device frame of reference.
- `~view_width` (`double`, default: `2 * pi`):: width of view angle in
  radians in the XY plane of the device frame of reference.

#### Examples

Continuously convert raw Velodyne packets into
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)
messages. *Running as a standalone nodelet prevents zero-copy message
sharing.* 

```
$ rosrun nodelet nodelet standalone velodyne_pointcloud/CloudNodelet
```



This launch file runs the cloud nodelet in the same process with the
device driver. *That enables zero-copy message sharing.* The full path
name of the calibration file *must* be provided. This example uses one
of the package test files for calibration. 

```
<launch>
  <!-- start nodelet manager and driver nodelets -->
  <include file="$(find velodyne_driver)/launch/nodelet_manager.launch" />

  <!-- start cloud nodelet -->
  <include file="$(find velodyne_pointcloud)/launch/cloud_nodelet.launch">
    <arg name="calibration"
         value="$(find velodyne_pointcloud)/params/64e_utexas.yaml"/>
  </include>

</launch>
```



### cloud_node

This node runs the same code as `CloudNodelet` in a node by itself.

#### Examples

Continuously convert raw Velodyne packets into
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)
messages. 

```
$ rosrun velodyne_pointcloud cloud_node _calibration:=calibration.yaml
```



### TransformNodelet

This nodelet reads raw data from the `velodyne_packets` ROS topic,
converts to
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)
format, and republishes to `velodyne_points` ROS topic in a specified
frame of reference (typically `/odom`). In addition to the XYZ points,
this cloud includes fields for "intensity" and "ring".

#### Subscribed Topics

- `velodyne_packets`
  ([velodyne_msgs/msg/VelodyneScan](https://docs.ros.org/en/rolling/p/velodyne_msgs/msg/VelodyneScan.html)):
  one or more Raw Velodyne data packets from the device

#### Published Topics

- `velodyne_points`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  accumulated Velodyne points transformed into the `frame_id` frame of
  reference.

#### Parameters

- `~frame_id` (`str`, default: `"odom"`): Target frame ID. Resolved
  using `tf_prefix`, if defined.
- `~model` (`string`, default: `"64E"`): model of sensor being used.
  Currently supported are: "VLP16", "32C", "32E", "64E",
  "64E_S2", "64E_S2.1", "64E_S3"
- `~max_range` (`double`, default: `130.0`): maximum range (in meters)
  to publish; measurements further than this won't be published.
- `~min_range` (`double`, default: 0.9, formerly 2.0): minimum range to
  publish; measurements closer than this won't be published.
- `~calibration` (`string`): YAML file containing device-specific
  calibration information.
- `~view_direction` (`double`, default: `0.0`):: center of view angle in
  radians in the device frame of reference.
- `~view_width` (`double`, default: `2 * pi`):: width of view angle in
  radians in the XY plane of the device frame of reference.

#### Examples

Transform raw Velodyne packets into
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)
messages into the `/odom` frame. *Running as a standalone nodelet
prevents zero-copy message sharing.* 

```
$ rosrun nodelet nodelet standalone velodyne_pointcloud/TransformNodelet
```



This launch file runs the transform nodelet in the same process with the
device driver. *That enables zero-copy message sharing.* The full path
name of the calibration file *must* be provided. This example uses one
of the package test files. 

```
<launch>
  <!-- start nodelet manager and driver nodelets -->
  <include file="$(find velodyne_driver)/launch/nodelet_manager.launch" />

  <!-- start transform nodelet -->
  <include file="$(find velodyne_pointcloud)/launch/transform_nodelet.launch">
    <arg name="calibration"
         value="$(find velodyne_pointcloud)/params/64e_utexas.yaml"/>
  </include>
</launch>
```



### transform_node

This node runs the same code as `TransformNodelet` in a node by
itself.

#### Examples

Transform raw Velodyne packets into
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)
messages into the `/odom` frame. 

```
$ rosrun velodyne_pointcloud transform_node _calibration:=calibration.yaml
```



Transform raw Velodyne packets into
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)
messages into the `/map` frame. 

```
$ rosrun velodyne_pointcloud transform_node _frame_id:=/map
```



## Launch File Examples

In two separate terminal windows, start a `velodyne_nodelet_manager`
process running the driver nodelet and the cloud nodelet, which will
have zero-copy access to the raw data messages the driver publishes.



```
$ roslaunch velodyne_driver nodelet_manager.launch
```





```
$ roslaunch velodyne_pointcloud cloud_nodelet.launch calibration:=~/mydata.yaml
```



Start a driver nodelet with input from `tcpdump.pcap`, in the current
directory. The `pwd` provides a full path name, as required for
`roslaunch`. In another terminal, start the transform nodelet, to
publish the data points transformed into the /odom frame of reference.



```
$ roslaunch velodyne_driver nodelet_manager.launch pcap:=$(pwd)/tcpdump.pcap
```





```
$ roslaunch velodyne_pointcloud transform_nodelet.launch calibration:=~/mydata.yaml
```



Start a `velodyne_nodelet_manager` process for a Velodyne HDL-32E.
This script runs both the driver and the point cloud conversion,
providing the standard HDL-32E calibration.



```
$ roslaunch velodyne_pointcloud 32e_points.launch
```



Start another `velodyne_nodelet_manager` for the Velodyne HDL-32E, but
provide a PCAP dump file as input.



```
$ roslaunch velodyne_pointcloud 32e_points.launch pcap:=$(pwd)/tcpdump.pcap
```



## Utility Commands

### gen_calibration.py

This script generates a YAML calibration file for use by this package
from the `db.xml` file that was provided by Velodyne with the device.

#### Examples

Read `db.xml` from the current directory, writing the required
calibration data to `db.yaml`.



```
$ rosrun velodyne_pointcloud gen_calibration.py db.xml
```



Save generated 32E calibration data in `my_calibration.yaml`.



```
$ rosrun velodyne_pointcloud gen_calibration.py 32db.xml my_calibration.yaml
```



## C++ API

C++ interfaces exported by this package:

- #include
  [<velodyne_pointcloud/point_types.h>](http://ros.org/doc/api/velodyne_pointcloud/html/point__types_8h.html)
  defines a custom `velodyne_pointcloud::PointXYZIR` point, similar to
  `pcl::PointXYZI` (XYZ with intensity) plus an added field containing
  the laser ring number.

<!-- -->

- #include
  [<velodyne_pointcloud/rawdata.h>](http://ros.org/doc/api/velodyne_pointcloud/html/rawdata_8h.html)
  provides interfaces for interpreting raw packets from the device.
