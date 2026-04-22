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

-   `laser_scan_assembler`: Assembles a stream of
    [sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
    messages into point clouds
-   `point_cloud_assembler`: Sometimes due to some pre-processing,
    laser scans have already been converted into cartesian coordinates
    as
    [sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html)
    messages. This node assembles a stream of these
    [sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html)
    messages into larger point clouds

## Roadmap / Stability

The ROS API of this package is considered stable. We don't foresee
making any large changes to `laser_assembler` anytime soon.

## Data Flow

The general data flow can be descibed as follows:

![](attachment:laser_scan_assembler.png)

The `laser_scan_assembler` subscribes to
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
messages on the `scan` topic. These scans are processed by the
Projector and Transformer, which project the scan into Cartesian space
and then transform it into the `fixed_frame`. This results in a
[sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html)
that can be added to the rolling buffer. Clouds in the rolling buffer
are then assembled on service calls.

Note that the Transformer automatically receives [tf](tf) data without
any user intervention.

![](attachment:point_cloud_assembler.png)

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

## Deprecated API

As of laser_pipeline 0.4.0. A large part of the laser_assembler's ROS
API was deprecated. The API reference for the deprecated API is
available on the [laser_assembler-0.3.0](laser_assembler-0.3.0) page.
