## Overview

In the aerospace industry,
[FODs](https://www.fodcontrol.com/what-is-fod/) are a recurrent problem
that implies a high risk. This package has been developed to help
identifying FODs in aeronautical structures.

Using point cloud analysis techniques, this software aims to compare the
current state of the structure with previous state to identify possible
foreign objects. It opens up the posibility of applying a pre-scan in
which it is guaranteed to be free of FODs or a CAD of the structure that
is ideal and free of fods.

## Getting started

Source: git <https://github.com/fada-catec/leica_point_cloud_processing>
(branch: master)

This package have been designed to be used in combination with the
[leica_scanstation](https://github.com/fada-catec/leica_scanstation)
package, which allows to control the scanstation to scan an aeronautical
part. When the scan is finished, you get the point cloud that proceeds
to be analyzed. In order to reproduce this behaviour if the device is
not available, we created a
[simulator](https://github.com/fada-catec/leica_gazebo_simulator).

However, it is possible to feed this program with pointclouds from other
sources and it will run the same way.

NOTE: you will need *leica_scanstation_msgs* and
*leica_scanstation_utils* packages from *leica_scanstation* to use this
one.

## Workflow

The aim is to compare two pointclouds: the one obtained after scanning
with the Leica Scanstation, with an ideal one free of FODs. This second
cloud can be from a previous scan or the CAD of the structure. The first
stage is to get both clouds registerd as exposed in
[PCL Registration API](https://pointclouds.org/documentation/tutorials/registration_api.html).
When FOD detection process ends, results clouds are available in ROS
topics.

This proccedure is developed as a Finite State Machine. The worklow is
the following.

![\|width="720px"](attachment:fsm.png)

## Usage

### Publish clouds

**load_and_publish_clouds** node will load both source and target clouds
into ROS environment. ```
rosrun leica_point_cloud_processing load_and_publish_clouds
```

Considerations:

-   Make sure pointcloud files are on the correct folder, specified in
    ROS param server as `/pointcloud_folder` (default: package
    leica_scanstation_utils/pointclouds).

```{=html}
<!-- -->
```
-   Supported formats: `.obj` and `.ply` for CAD files and `.pcd`
    for scanned files.

```{=html}
<!-- -->
```
-   Publisher starts when service `/publish_clouds` is called:
    automatically done by `leica_scanstation_ros_node` when scan is
    finished or manually by user: ```
rosservice call /publish_clouds "source_cloud_file: 'scan_fods.pcd'
        target_cloud_file: 'cad.ply'"
```

### Start process

**node** is the main node that perform alignment and FOD detection. It
opens subscribers to clouds topics and start process. As the target
cloud indicated in example above comes from a CAD file, set param
`using_CAD` to true. ```
roslaunch leica_point_cloud_processing leica_point_cloud_processing.launch using_CAD:=true
```

## ROS API

### Topics

```clearsilver
pub {
  no_header = True
  0{
   name = target/cloud
   type = sensor_msgs/PointCloud2
   desc = Point cloud created from loading Part's CAD or scan free of FODs.
   }
  1{
   name = source/cloud
   type = sensor_msgs/PointCloud2
   desc = Point cloud obtained from loading the result of a scanning process.
   }
  2{
   name = target/cloud_filtered
   type = sensor_msgs/PointCloud2
   desc = Target Point cloud after downsampling.
   }
  3{
   name = source/cloud_aligned
   type = sensor_msgs/PointCloud2
   desc = Point cloud resulting of the aligned cloud.
   }
  4{
   name = source/num_of_fods
   type = std_msgs/Int16
   desc = Number of FODs detected in cloud
   }
  5{
   name = source/fods_detected
   type = sensor_msgs/PointCloud2
   desc = FODs presented as point cloud. 
   }
```

### Services

```clearsilver
srv{
  no_header = True
  0{
   name = publish_clouds
   type = leica_scanstation_msgs/PointCloudFile
   desc = Tell which pointcloud file to publish into ROS environment.
   }
```

### Parameters

```clearsilver
param {
  no_header = True
  0{
   name = /using_CAD
   type = bool
   desc = Set to true if target cloud is a CAD. 
   default = false
   }
  1{
   name = /align_method
   type = int
   desc = Harris=0, Boundary=1, Multiscale=2, Normals=3, None=4. 
   default = 1
   }
```

## Acknowledgement

[Included page rosin/acknowledgement not found](Included page rosin/acknowledgement not found)
