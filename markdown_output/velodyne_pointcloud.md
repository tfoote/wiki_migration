## Overview

This package provides point cloud conversions for Velodyne 3D LIDARs.
For a list of all supported models refer to the
[ Supported Devices](velodyne_driver#Supported_Devices ) section.

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



```clearsilver
node.0 {
 name = CloudNodelet
 desc = This nodelet reads raw data from the `velodyne_packets` ROS topic, converts to <<MsgLink(sensor_msgs/PointCloud2)>> format, and republishes to `velodyne_points` ROS topic in the original frame of reference (typically `/velodyne`). In addition to the XYZ points, this cloud includes fields for "intensity" and "ring".
 sub {
  0.name= velodyne_packets
  0.type= velodyne_msgs/VelodyneScan
  0.desc= one or more raw Velodyne data packets from the device.
 }
 pub {
  0.name= velodyne_points
  0.type= sensor_msgs/PointCloud2
  0.desc= accumulated Velodyne points transformed in the original frame of reference.
 }
param {
  2.name= ~model
  2.type= string
  2.default= "64E"
  2.desc= model of sensor being used. Currently supported are: "VLP16", "32C", "32E", "64E", "64E_S2", "64E_S2.1", "64E_S3"
  3.name= ~max_range
  3.type= double
  3.default= 130.0
  3.desc= maximum range (in meters) to publish; measurements further than this won't be published.
  4.name= ~min_range
  4.type= double
  4.default= <<Version(Indigo)>> 0.9, formerly 2.0
  4.desc= minimum range (in meters) to publish; measurements closer than this won't be published.
  10.name= ~calibration
  10.type= string
  10.desc= YAML file containing device-specific calibration information.
  20.name= ~view_direction
  20.type= double
  20.default= 0.0
  20.desc= <<Version(Indigo)>>: center of view angle in radians in the device frame of reference.
  21.name= ~view_width
  21.type= double
  21.default= 2 * pi
  21.desc= <<Version(Indigo)>>: width of view angle in radians in the XY plane of the device frame of reference.
 }
}
```



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





```clearsilver
node.0 {
 name = cloud_node
 desc = This node runs the same code as `CloudNodelet` in a node by itself.
}
```



#### Examples

Continuously convert raw Velodyne packets into
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)
messages. 

```
$ rosrun velodyne_pointcloud cloud_node _calibration:=calibration.yaml
```





```clearsilver
node.0 {
 name = TransformNodelet
 desc = This nodelet reads raw data from the `velodyne_packets` ROS topic, converts to <<MsgLink(sensor_msgs/PointCloud2)>> format, and republishes to `velodyne_points` ROS topic in a specified frame of reference (typically `/odom`). In addition to the XYZ points, this cloud includes fields for "intensity" and "ring".
 sub {
  0.name= velodyne_packets
  0.type= velodyne_msgs/VelodyneScan
  0.desc= one or more Raw Velodyne data packets from the device
 }
 pub {
  0.name= velodyne_points
  0.type= sensor_msgs/PointCloud2
  0.desc= accumulated Velodyne points transformed into the `frame_id` frame of reference.
 }
param {
  0.name= ~frame_id
  0.type= str
  0.default= "odom"
  0.desc= Target frame ID. Resolved using `tf_prefix`, if defined.
  2.name= ~model
  2.type= string
  2.default= "64E"
  2.desc= model of sensor being used. Currently supported are: "VLP16", "32C", "32E", "64E", "64E_S2", "64E_S2.1", "64E_S3"
  3.name= ~max_range
  3.type= double
  3.default= 130.0
  3.desc= maximum range (in meters) to publish; measurements further than this won't be published.
  4.name= ~min_range
  4.type= double
  4.default= <<Version(Indigo)>> 0.9, formerly 2.0
  4.desc= minimum range to publish; measurements closer than this won't be published.
  10.name= ~calibration
  10.type= string
  10.desc= YAML file containing device-specific calibration information.
  20.name= ~view_direction
  20.type= double
  20.default= 0.0
  20.desc= <<Version(Indigo)>>: center of view angle in radians in the device frame of reference.
  21.name= ~view_width
  21.type= double
  21.default= 2 * pi
  21.desc= <<Version(Indigo)>>: width of view angle in radians in the XY plane of the device frame of reference.
 }
}
```



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





```clearsilver
node.0 {
 name = transform_node
 desc = This node runs the same code as `TransformNodelet` in a node by itself. 
}
```



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
$ rosrun nodelet nodelet standalone velodyne_pointcloud/CloudNodelet
```

0

## Launch File Examples

In two separate terminal windows, start a `velodyne_nodelet_manager`
process running the driver nodelet and the cloud nodelet, which will
have zero-copy access to the raw data messages the driver publishes.



```
$ rosrun nodelet nodelet standalone velodyne_pointcloud/CloudNodelet
```

1



```
$ rosrun nodelet nodelet standalone velodyne_pointcloud/CloudNodelet
```

2

Start a driver nodelet with input from `tcpdump.pcap`, in the current
directory. The `pwd` provides a full path name, as required for
`roslaunch`. In another terminal, start the transform nodelet, to
publish the data points transformed into the /odom frame of reference.



```
$ rosrun nodelet nodelet standalone velodyne_pointcloud/CloudNodelet
```

3



```
$ rosrun nodelet nodelet standalone velodyne_pointcloud/CloudNodelet
```

4

Start a `velodyne_nodelet_manager` process for a Velodyne HDL-32E.
This script runs both the driver and the point cloud conversion,
providing the standard HDL-32E calibration.



```
$ rosrun nodelet nodelet standalone velodyne_pointcloud/CloudNodelet
```

5

Start another `velodyne_nodelet_manager` for the Velodyne HDL-32E, but
provide a PCAP dump file as input.



```
$ rosrun nodelet nodelet standalone velodyne_pointcloud/CloudNodelet
```

6

## Utility Commands

### gen_calibration.py

This script generates a YAML calibration file for use by this package
from the `db.xml` file that was provided by Velodyne with the device.

#### Examples

Read `db.xml` from the current directory, writing the required
calibration data to `db.yaml`.



```
$ rosrun nodelet nodelet standalone velodyne_pointcloud/CloudNodelet
```

7

Save generated 32E calibration data in `my_calibration.yaml`.



```
$ rosrun nodelet nodelet standalone velodyne_pointcloud/CloudNodelet
```

8

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
