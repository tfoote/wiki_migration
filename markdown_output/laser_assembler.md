## Overview

Laser Rangefinder sensors (such as Hokuyo's
[ UTM-30LX](http://www.hokuyo-aut.jp/02sensor/07scanner/utm_30lx.html))
generally output a stream of scans, where each scan is a set of range
readings of detected objects (in polar coordinates) in the plane of the
sensor.

Many robotic systems, like PR2's tilting laser platform, articulate a
laser rangefinder in order to get a 3D view of the world. The
`laser_assembler` package provides nodes that listen to streams of
scans and then assemble them into a larger 3D Cartesian coordinate (XYZ)
point cloud.

Users interface with the laser_assembler package via two ROS nodes:

- `laser_scan_assembler`: Assembles a stream of
  [sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
  messages into point clouds
- `point_cloud_assembler`: Sometimes due to some pre-processing, laser
  scans have already been converted into cartesian coordinates as
  [sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html)
  messages. This node assembles a stream of these
  [sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html)
  messages into larger point clouds

## Roadmap / Stability

The ROS API of this package is considered stable. We don't foresee
making any large changes to `laser_assembler` anytime soon.

## Data Flow

The general data flow can be descibed as follows:

![attachment:laser_scan_assembler.png](doc/laser_scan_assembler.png)

The `laser_scan_assembler` subscribes to
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
messages on the `scan` topic. These scans are processed by the
Projector and Transformer, which project the scan into Cartesian space
and then transform it into the `fixed_frame`. This results in a
[sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html)
that can be added to the rolling buffer. Clouds in the rolling buffer
are then assembled on service calls.

Note that the Transformer automatically receives
[tf](https://index.ros.org/p/tf) data without any user intervention.

![attachment:point_cloud_assembler.png](doc/point_cloud_assembler.png)

The `point_cloud_assembler` looks very similar to the
`laser_scan_assembler`, except that the projection step is skipped,
since the input clouds are already in Cartesian coordinates.

## ROS API/Nodes

The main interaction with the assemblers is via ROS services. The
`laser_scan_assembler` and `point_cloud_assembler` both provide the
`assemble_scans` service, which is documented below.

NOTE: For laser_pipeline releases < 0.5.0, this service is called
`build_cloud`.



```clearsilver
node.0{
  name= laser_scan_assembler
  desc= Assembles a stream of <<MsgLink(sensor_msgs/LaserScan)>> messages into point clouds.
  sub {
    0.name= scan
    0.type=sensor_msgs/LaserScan  
    0.desc= Topic on which to receive a stream of sensor_msgs/LaserScan messages.
  }
  param {
    0.name= ~fixed_frame
    0.type= string
    0.desc= '''[Required]''' Stationary frame into which received scans (or clouds) are transformed.
    1.name= ~tf_cache_time_secs
    1.type= double
    1.desc= The cache time (seconds) to store past transforms.
    1.default = 10.0
    2.name= ~max_scans
    2.type= int
    2.default = 400
    2.desc= The number of scans to store in the assembler's rolling buffer.
    3.name= ~ignore_laser_skew
    3.default=`true`
    3.type= bool
    3.desc= If true, pretend that all hits in a single scan correspond to the same tf transforms. If false, individually transform each hit to the fixed_frame (this is a fairly cpu intensive operation). 
  }
 srv {
    0.name = assemble_scans
    0.type = laser_assembler/AssembleScans
    0.desc = When an assembler receives an `assemble_scans` request, it searches its rolling buffer for clouds that occur in the requested interval (`begin` to `end`). These clouds are then assembled into a larger cloud, in the frame specified by the `~fixed_frame` parameter, and sent to to the caller in the service response. This is a ''non-blocking'' operation and will return an empty cloud if no scans are received in the requested interval.  The resulting cloud will have channels named `intensities`, `index`, `distances`, and `stamps` as defined by the [[http://www.ros.org/doc/api/laser_geometry/html/classlaser__geometry_1_1LaserProjection.html | laser_geometry::LaserProjection]] library.
    1.name = assemble_scans2
    1.type = laser_assembler/AssembleScans2
    1.desc = Same as assemble_scans, except returns a <<MsgLink(sensor_msgs/PointCloud2)>>
  }
}
node.1{
  name= point_cloud_assembler 
  desc= Assembles a stream of these <<MsgLink(sensor_msgs/PointCloud)>> messages into larger point clouds.
  sub {
    0.name=cloud 
    0.type= sensor_msgs/PointCloud
    0.desc= Topic on which to receive a stream of sensor_msgs/PointCloud messages.
  }
  param {
    0.name= ~fixed_frame
    0.type= string
    0.desc= '''[Required]''' Stationary frame into which received scans (or clouds) are transformed.
    1.name= ~tf_cache_time_secs
    1.type= double
    1.desc= The cache time (seconds) to store past transforms.
    1.default = 10.0
    2.name= ~max_clouds
    2.type= int
    2.default = 400
    2.desc= The number of point clouds to store in the assembler's rolling buffer.
  }
 srv {
    0.name = assemble_scans
    0.type = laser_assembler/AssembleScans
    0.desc = When an assembler receives an `assemble_scans` request, it searches its rolling buffer for clouds that occur in the requested interval (`begin` to `end`). These clouds are then assembled into a larger cloud, in the frame specified by the `~fixed_frame` parameter, and sent to to the caller in the service response. This is a ''non-blocking'' operation and will return an empty cloud if no scans are received in the requested interval.
  }  
}
```



### Example Launch

**laser_scan_assembler:**

Launch an assembler operating on `tilt_scan`
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
messages in the base_link frame, with a buffer of 400
scans.[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)



```
<launch>
  <node type="laser_scan_assembler" pkg="laser_assembler"
        name="my_assembler">
    <remap from="scan" to="tilt_scan"/>
    <param name="max_scans" type="int" value="400" />
    <param name="fixed_frame" type="string" value="base_link" />
  </node>
</launch>
```



**point_cloud_assembler:**

Launch an assembler operating on `my_cloud_in`
[sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html)
messages in the `base_link` frame, with a buffer of 400 scans.



```
<launch>
  <node type="point_cloud_assembler" pkg="laser_assembler"
        name="my_assembler">
    <remap from="cloud" to="my_cloud_in"/>
    <param name="max_clouds" type="int" value="400" />
    <param name="fixed_frame" type="string" value="base_link" />
  </node>
</launch>
```



### Example: Calling from C++

Request a cloud with scans occurring between the start of time and now.


```cplusplus
#include <ros/ros.h>
#include <laser_assembler/AssembleScans.h>
using namespace laser_assembler;
int main(int argc, char **argv)
{
  ros::init(argc, argv, "test_client");
  ros::NodeHandle n;
  ros::service::waitForService("assemble_scans");
  ros::ServiceClient client = n.serviceClient<AssembleScans>("assemble_scans");
  AssembleScans srv;
  srv.request.begin = ros::Time(0,0);
  srv.request.end   = ros::Time::now();
  if (client.call(srv))
    printf("Got cloud with %u points\n", srv.response.cloud.points.size());
  else
    printf("Service call failed\n");
  return 0;
}
```



### Example: Calling from Python

Request a cloud with scans occurring between the start of time and now.


```python
#!/usr/bin/env python
import roslib; roslib.load_manifest('laser_assembler')
import rospy; from laser_assembler.srv import *

rospy.init_node("test_client")
rospy.wait_for_service("assemble_scans")
try:
    assemble_scans = rospy.ServiceProxy('assemble_scans', AssembleScans)
    resp = assemble_scans(rospy.Time(0,0), rospy.get_rostime())
    print "Got cloud with %u points" % len(resp.cloud.points)
except rospy.ServiceException, e:
    print "Service call failed: %s"%e
```



NOTE: in both service calls the number of points in the returned point
cloud is capped by the size of the assembler's rolling buffer.

## Tutorials

- [How to assemble laser scan lines into a composite point cloud](#how-to-assemble-laser-scan-lines-into-a-composite-point-cloud):
  In this tutorial you will learn how to assemble individual laser scan
  lines into a composite point cloud. One particular use case is to
  assemble individual scan lines from a laser on a tilting stage into a
  single point cloud to form a full 3D laser sweep.

## Deprecated API

As of laser_pipeline 0.4.0. A large part of the laser_assembler's ROS
API was deprecated. The API reference for the deprecated API is
available on the [laser_assembler-0.3.0](laser_assembler-0.3.0) page.

## How to assemble laser scan lines into a composite point cloud

In the
[laser pipeline tutorials](https://index.ros.org/p/laser_pipeline), you
learned how to work with a single scan line. In many cases, however, it
would be more useful to have multiple scan lines together as a larger
point cloud. For example, if the laser is on a tilting unit, it's
useful to group together all of the scans that came from one
top-to-bottom tilting cycle. Or it might be useful to accumulate a set
of scans over a fixed time period. To aggregate scans we look to the
laser_assembler package containing the
`laser_scan_assembler` and the `point_cloud_assembler`.

### Example Laser Data

So that you can try all of the nodes described in this tutorial, we've
provided a source of laser data. ROS can [record](rosrecord) sensor data
(actually any ROS system data) into a *bag* file. You can download a bag
file containing laser data
[here](http://vault.willowgarage.com/wgdata1/vol1/wiki_docs/laser_pipeline/laser.bag).

The bag contains two topics:

- `/tf \[tf/tfMessage\]`
- `/tilt_scan \[sensor_msgs/LaserScan\]`

You can verify this using `rosbag`: 

```
rosbag info laser.bag
```



The `tilt_scan` topic was recorded from a planar laser mounted on a
tilting stage. The `/tf` topic contains the robot transforms.

To play back the bag, first run a roscore:



```
$ roscore
```



We're going to be using bagfile data, so we want to make sure that all
of our nodes' times are based off of simulation time:


```
$ rosparam set /use_sim_time true
```



Then play back the bag: 

```
$ rosbag play --clock laser.bag
```



We need the `\--clock` argument in order to publish simulation time.

Familiarize yourself with the data by viewing it in
[rviz](https://index.ros.org/p/rviz).

### The Laser Scan Assembler

The `laser_scan_assembler` accumulates laser scans by listening to the
appropriate topic and accumulating messages in a ring buffer of a
specific size. When the `assemble_scans` service is called, the
contents of the current buffer that fall between two times are converted
into a single cloud and returned.

Here is an example launch file for the `laser_scan_assembler`
operating on the scan topic `tilt_scan`:



```
<launch>
  <node type="laser_scan_assembler" pkg="laser_assembler" name="my_assembler">
    <remap from="scan" to="tilt_scan"/>
    <param name="max_scans" type="int" value="400" />
    <param name="fixed_frame" type="string" value="base_link" />
  </node>
</launch>
```

 This instantiation of the
`laser_scan_assembler` keeps a rolling buffer of 400 scans, and
transforms incoming scans into the base_link frame. The full set of
parameters is available in the `laser_assembler`'s
ROS Interface section.

The `fixed_frame` parameter name is not accidental. Each single scan
is converted into this frame when it arrives, and no additional
transforms are done to the data when the cloud is published. Therefore,
you will very likely want to choose a frame that isn't moving for your
`fixed_frame`. If your robot is stationary, the `base_link` frame
might be a good choice. If your robot is moving, choose a frame that is
stationary in the world like a `map` frame.

Try running the `laser_scan_assembler` on the `\\tilt_scan` topic in
`laser.bag`. It doesn't look like much is happening, right? But
behind the scenes, the buffer is filling up\...

### The Point Cloud Assembler

If your scan lines are already in point cloud message form, you can use
the `point_cloud_assembler` instead. The `point_cloud_assembler`
works very much like the laser_scan_assembler, here's a launch file for
it:



```
<launch>
  <node type="point_cloud_assembler" pkg="laser_assembler" name="my_assembler">
    <remap from="cloud" to="my_cloud_in"/>
    <param name="max_clouds" type="int" value="400" />
    <param name="fixed_frame" type="string" value="base_link" />
  </node>
</launch>
```

 Try out the `point_cloud_assembler` by first
converting the `tilt_scan` topic into a point cloud and then
assembling it. (Forgot how to convert a laser scan into a point cloud?
Go back to the
[introduction to working with laser scanner data](https://index.ros.org/p/laser_pipeline).)
Once again, nothing visible is happening, but the buffer is filling
up\...

### Using the Assemblers: A Laser Snapshotter

The assemblers will work away dutifully as laser scans (or point clouds)
come in, but they won't publish anything until you call the
`assemble_scans` service. The `assemble_scans` service has two
request fields:

- `time begin`
- `time end`

All buffer entries between these two times will be grouped into one
point cloud and returned in the response field:

- `sensor_msgs::PointCloud cloud`

How often you call `assemble_scans` depends on your robot and
application, here are some suggestions:

- every x seconds,
- whenever you're ready to process the resulting cloud, or
- when receiving a signal from your system, such as when a laser tilting
  stage passes through one sweep.

As an example, the `laser_assembler` package has an example node in
the `examples` folder called `periodic_snapshotter` which calls the
`assemble_scans` service every 5 seconds and publishes the resulting
clouds.

Try running the `periodic_snapshotter` with the
`laser_scan_assembler` and viewing the resulting point cloud
(published on the topic `assembled_cloud`) in
[rviz](https://index.ros.org/p/rviz). Instead of a updating
line-by-line, the point cloud will change every 5 seconds and display
all of the accumulated data at once.

### Conclusion

Now you should be able to assemble single scans (or clouds) into full
point clouds. By combining this with the tools in
[laser_geometry](https://index.ros.org/p/laser_geometry) and
[laser_filters](https://index.ros.org/p/laser_filters) that you learned
about in previous [tutorials](https://index.ros.org/p/laser_pipeline),
you can convert your raw sensor data into more useful formats.

## Tutorials

- [How to assemble laser scan lines into a composite point cloud](#how-to-assemble-laser-scan-lines-into-a-composite-point-cloud):
  In this tutorial you will learn how to assemble individual laser scan
  lines into a composite point cloud. One particular use case is to
  assemble individual scan lines from a laser on a tilting stage into a
  single point cloud to form a full 3D laser sweep.

## Troubleshooting

### Reporting Errors

If you encounter a problem that isn't addressed on this page, please
[file a ticket](https://code.ros.org/trac/ros-pkg/newticket?component=laser_pipeline&keywords=laser_assembler&owner=vpradeep)

The current list of open issues is available on
[trac](https://code.ros.org/trac/ros-pkg/query?status=assigned&status=new&status=reopened&group=milestone&order=priority&col=id&col=summary&col=status&col=type&col=priority&col=milestone&col=component&keywords=~laser_assembler)

### Common Problems When Using Package

(There are currently no recorded commonly occurring errors)
