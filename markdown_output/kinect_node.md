# Deprecated

Please see [kinect_camera](kinect_camera) in [kinect](kinect) stack for
the new version.

# Old documentation

![](http://ros.org/images/wiki/kinect_node/kinect_node.png)

## Details

The [kinect_node](kinect_node) package provides a driver for using the
Kinect RGB-D sensor with ROS. Currently this package depends on the
[libfreenect_install](libfreenect_install) package which is a wrapper
around the [libfreenect](http://git.marcansoft.com/?p=libfreenect.git)
driver. The library is patched using Stéphane Magnenat's memory trash
patch.

This package currently outputs a
<<MsgLink(sensor_msgs/PointCloud)>>, a RGB
<<MsgLink(sensor_msgs/Image)>> and it's associated
<<MsgLink(sensor_msgs/CameraInfo)>>. The PointCloud, Image, and
CameraInfo are published with the same timestamp (the node will hold
data until all 3 have become available).

For calibration information based on this package, please see
[/Calibration](/Calibration).

## Future Work

-   Switch to PCL - PointCloud2 with RGB values - requires accurate
    cross-calibration of the cameras
-   Output Depthmap as an image topic
-   Improve 3D calibration
-   Publish the accelerometer data
-   Listen for pose information to control the camera motor

## Running

```
roscore  >& /dev/null &
rosrun kinect_node kinect_node  >& /dev/null &
rosrun rviz rviz
```

Set Fixed Frame to /kinect_depth or whatever name was provided with the
kinect_depth_frame argument.

## Example

You can download the pre-recorded bag file of the video shown below from
[here](https://code.ros.org/svn/data/trunk/ccny/). This can be viewed in
[rviz](rviz).

kinect_node.bag is 1.1GB of data and may not be useful.

kinect_node_subset.bag is a 143M subset of the above bag file.

```
roscore >& /dev/null &
rosrun rviz rviz >& /dev/null &
rosbag play -q -l kinect_node_subset.bag
```

In rviz select 'File > Open Config' from the main menu then open the
'kinect_node/launch/demo.vcg' config file.

[Youtube](https://www.youtube.com/watch?v=jQgnuupBUI4)

## Nodes

```clearsilver
 name = kinect_node
 desc = The `kinect_node` uses the libfreenect driver to access the Kinect RGB-D Sensor.

pub {
   0{
    name = cloud
    type = sensor_msgs/PointCloud
    desc = 3D Pointcloud data
   }
   1{
    name = image_raw
    type = sensor_msgs/Image
    desc = RGB Image Data
   }
   2{
    name = camera_info
    type = sensor_msgs/CameraInfo
    desc = CameraInfo Topic for Calibration
   }
  }

param{

    1.name = ~kinect_rgb_frame
    1.type = string
    1.default = `"/kinect_rgb"`
    1.desc = the name of the RGB camera frame

    1.name = ~kinect_depth_frame
    1.type = string
    1.default = `"/kinect_depth"`
    1.desc = the name of the Depth camera frame

    2.name = ~max_range
    2.type = float
    2.default = `5.0`
    2.desc = The maximum range of the sensor in meters, beyond this the error is too large.

    3.name = ~width
    3.type = int
    3.default = `640`
    3.desc = The width of the image returned by the Kinect

    4.name = ~height
    4.type = int
    4.default = `480`
    4.desc = The height of the image returned by the Kinect

    5.name = ~camera_name
    5.type = string
    5.default = `"camera"`
    5.desc = The name of the camera used by CameraInfo

    6.name = ~camera_info_url
    6.type = string
    6.default = `"file://ROS_PACKAGE_NAME/info/calibration.yaml"`
    6.desc = The location of the camera calibration file. Can also  be set to 'auto'
  }

 req_tf{
 }
 prov_tf{
 }
```

## References

\[1\] H. Martin,
["Open source Kinect driver"](http://git.marcansoft.com/?p=libfreenect.git),
The Internets, 2010

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.

Please use our [Trac](http://robotics.ccny.cuny.edu/trac/) to
[report bugs](http://robotics.ccny.cuny.edu/trac/newticket?component=scan_tools/canonical_scan_matcher&type=defect)
or
[request features](http://robotics.ccny.cuny.edu/trac/newticket?component=scan_tools/canonical_scan_matcher&type=enhancement).
