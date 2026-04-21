## Overview

The laser_geometry package contains a single C++ class:
[LaserProjection](http://ros.org/doc/fuerte/api/laser_geometry/html/classlaser__geometry_1_1LaserProjection.html).
There is no ROS API.

This class has two relevant functions for transforming from
<<MsgLink(sensor_msgs/LaserScan)>> to
<<MsgLink(sensor_msgs/PointCloud)>> or
<<MsgLink(sensor_msgs/PointCloud2)>>.

-   `projectLaser()` is simple and fast. It does not change the frame
    of your data.
-   `transformLaserScanToPointCloud()` is slower but more precise. It
    makes uses of [tf](tf) and the
    <<MsgLink(sensor_msgs/LaserScan)>> time increment to transform
    each individual ray appropriately. This is the recommended means of
    transformation for tilting laser scanners or moving robots.

Both of these functions have a final optional argument that augments the
<<MsgLink(sensor_msgs/PointCloud)>> which is created to include
extra channels. These channels may include intensities, distances,
timestamps, the index or thew viewpoint from the original laser array.

There is a simple Python implementation here
(<https://github.com/ros-perception/laser_geometry/blob/indigo-devel/src/laser_geometry/laser_geometry.py>).

## C++ Usage

### Simple projection

The method `projectLaser()` does the simplest possible projection of
the laser. Each ray is simply projected out along the appropriate angle
according to:

```latex
\begin{eqnarray*}
\left(\begin{array}{c}x\\y\\z\end{array}\right) & = & \left(\begin{array}{c}r \cos \theta\\r \sin \theta \\ 0\end{array}\right)
\end{eqnarray*}
```

The appropriate sine and cosine values are cached, making this a very
efficient operation. However, the generated
<<MsgLink(sensor_msgs/PointCloud)>> is in the same frame as the
original <<MsgLink(sensor_msgs/LaserScan)>>. While this has the
advantage that it does not require an instance of a `tf::transformer`
or message notifier, it does not hold up in situations where the laser
is moving and skew needs to be accounted for.

Please consult the
[API Documentation](http://www.ros.org/doc/api/laser_geometry/html/classlaser__geometry_1_1LaserProjection.html#f9dae281a663ebfcf0aa6f295241b60b)
for full usage details.

**Example:** To convert a <<MsgLink(sensor_msgs/LaserScan)>> to a
<<MsgLink(sensor_msgs/PointCloud)>> ```cplusplus
laser_geometry::LaserProjection projector_;

void scanCallback (const sensor_msgs::LaserScan::ConstPtr& scan_in)
{
  sensor_msgs::PointCloud cloud;
  projector_.projectLaser(*scan_in, cloud);

  // Do something with cloud.
}
```

### High fidelity projection

The `transformLaserScanToPointCloud()` method does a more advanced
projection, but requires that you have set up a [tf](tf) transform
listener. (If you are unfamiliar with [tf](tf), it is recommended you go
through the [tf/Tutorials](tf/Tutorials) first.)

Since we are gathering data across the time of the scan, it is often
important that the chosen target_frame is actually a fixed frame.

Because the stamp of a <<MsgLink(sensor_msgs/LaserScan)>> is the
time of the **first** measurement, one cannot simply wait for a
transform to target_frame at this stamp. Instead one also has to wait
for a transform at the **last** measurement of the scan.

Please consult the
[API Documentation](http://www.ros.org/doc/api/laser_geometry/html/classlaser__geometry_1_1LaserProjection.html#b7ce0e0fa1bb6ab0f6d7d477d71284e9)
for full usage details.

**Example:** To convert a <<MsgLink(sensor_msgs/LaserScan)>> to a
<<MsgLink(sensor_msgs/PointCloud)>> in the base_link frame, using a
high fidelity transform: ```cplusplus
laser_geometry::LaserProjection projector_;
tf::TransformListener listener_;

void scanCallback (const sensor_msgs::LaserScan::ConstPtr& scan_in)
{
  if(!listener_.waitForTransform(
        scan_in->header.frame_id,
        "/base_link",
        scan_in->header.stamp + ros::Duration().fromSec(scan_in->ranges.size()*scan_in->time_increment),
        ros::Duration(1.0))){
     return;
  }

  sensor_msgs::PointCloud cloud;
  projector_.transformLaserScanToPointCloud("/base_link",*scan_in,
          cloud,listener_);

  // Do something with cloud.
}
```

## Python Usage

### Simple projection

The method `projectLaser()` projects a single laser scan from a linear
array into a 3D <<MsgLink(sensor_msgs/PointCloud2)>>. The generated
cloud will be in the same frame as the original laser scan.

```python

import sensor_msgs.point_cloud2 as pc2
import rospy
from sensor_msgs.msg import PointCloud2, LaserScan
import laser_geometry.laser_geometry as lg
import math

rospy.init_node("laserscan_to_pointcloud")

lp = lg.LaserProjection()

pc_pub = rospy.Publisher("converted_pc", PointCloud2, queue_size=1)

def scan_cb(msg):
    # convert the message of type LaserScan to a PointCloud2
    pc2_msg = lp.projectLaser(msg)

    # now we can do something with the PointCloud2 for example:
    # publish it
    pc_pub.publish(pc2_msg)
    
    # convert it to a generator of the individual points
    point_generator = pc2.read_points(pc2_msg)
    

    # we can access a generator in a loop
    sum = 0.0
    num = 0
    for point in point_generator:
        if not math.isnan(point[2])
            sum += point[2]
            num += 1
    # we can calculate the average z value for example
    print(str(sum/num))

    # or a list of the individual points which is less efficient
    point_list = pc2.read_points_list(pc2_msg)

    # we can access the point list with an index, each element is a namedtuple
    # we can access the elements by name, the generator does not yield namedtuples!
    # if we convert it to a list and back this possibility is lost
    print(point_list[len(point_list)/2].x)



rospy.Subscriber("/scan", LaserScan, scan_cb, queue_size=1)
rospy.spin()
```

### High fidelity projection

Currently there is no Python version of the high fidelity projection
