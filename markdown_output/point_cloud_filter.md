![](attachment:point_cloud_filter.png)

## Details

<<MsgLink(sensor_msgs/PointCloud)>> messages provide space for
additional channels, allowing values such as confidence or intensity to
be attached to each point in the cloud. The
[point_cloud_filter](point_cloud_filter) reads in a
<<MsgLink(sensor_msgs/PointCloud)>> message, and discards any points
whose channel value falls outside a specified threshold interval.

## Example

You can run the [point_cloud_filter](point_cloud_filter) on a
pre-recorded bag file that comes with the package.

First, make sure you have the [scan_tools](scan_tools) stack downloaded
and installed by following the instructions
[here](scan_tools#Installing).

Next, make sure you have the necessary tools installed:



```shell
rosmake rviz rosbag
```



Finally, launch the demo:



```shell
roslaunch point_cloud_filter demo.launch
```



You should see a result similar to the video below. The bag file
contains a single reading from a Swissranger 4000 camera. The point
cloud is filtered based on confidence values, with the minimum set to
248. The input (raw) cloud is displayed in blue, and the output
(filtered) in red.

[Youtube](https://www.youtube.com/watch?v=vmW-euUIcNg)

## Nodes



```clearsilver
 name = point_cloud_filter
 desc = The `point_cloud_filter` node takes in <<MsgLink(sensor_msgs/PointCloud)>> and applies a threshold filter, based on a specified channel.
 sub {
   0{
    name = swissranger_camera/pointcloud_raw
    type = sensor_msgs/PointCloud
    desc = The raw point cloud. By default, the output of a [[swissranger_camera]] is used.
    }
  }
 pub {
   0{
    name = pointcloud_filtered
    type = sensor_msgs/PointCloud
    desc = The filtered pointcloud. Values outside of min_value and max_value are removed. 
   }
  }
  
 param{
    0.name = ~channel
    0.type = int
    0.default = `1`
    0.desc = the channel in the <<MsgLink(sensor_msgs/PointCloud)>> message. `1` corresponds to "confidence" for the [[swissranger_camera]].

    1.name = ~min_value
    1.type = double
    1.default = `180`
    1.desc = the minimum threshold value. Points with a corresponding channel value less than this are discarded.
 
    2.name = ~max_value
    2.type = double
    2.default = `255`
    2.desc = the maximum threshold value. Points with a corresponding channel value more than this are discarded.

    3.name = ~copy_channels
    3.type = bool
    3.default = `true`
    3.desc = whether to copy the channel information to the filtered point cloud. Disabling this improves performance.
 }
```



## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.

Please use our [Trac](http://robotics.ccny.cuny.edu/trac/) to
[report bugs](http://robotics.ccny.cuny.edu/trac/newticket?component=ccny_vision/ar_pose&type=defect)
or
[request features](http://robotics.ccny.cuny.edu/trac/newticket?component=ccny_vision/ar_pose&type=enhancement).
