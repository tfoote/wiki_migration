## Overview

This package provides interfaces and tools for bridging a running ROS
system to the Point Cloud Library. These include ROS nodelets, nodes,
and C++ interfaces.

## ROS nodelets

\`pcl_ros\` includes several
[PCL filters](http://www.ros.org/wiki/pcl_ros/Filters) packaged as ROS
nodelets. These links provide details for using those interfaces:

-   [Extract_Indices](http://www.ros.org/wiki/pcl_ros/Tutorials/filters#Extract_Indices)
-   [PassThrough](http://www.ros.org/wiki/pcl_ros/Tutorials/filters#PassThrough)
-   [ProjectInliers](http://www.ros.org/wiki/pcl_ros/Tutorials/filters#ProjectInliers)
-   [RadiusOutlierRemoval](http://www.ros.org/wiki/pcl_ros/Tutorials/filters#RadiusOutlierRemoval)
-   [StatisticalOutlierRemoval](http://www.ros.org/wiki/pcl_ros/Tutorials/filters#StatisticalOutlierRemoval)
-   [VoxelGrid](http://www.ros.org/wiki/pcl_ros/Tutorials/filters#VoxelGrid)

## ROS C++ interface

\`pcl_ros\` extends the ROS [C++ client library](roscpp) to support
message passing with [PCL](pcl) native data types. Simply add the
following include to your ROS node source code: ```
#include <pcl_ros/point_cloud.h>
```

This header allows you to publish and subscribe
[pcl::PointCloud\<T\>](http://www.ros.org/doc/api/pcl/html/classpcl_1_1PointCloud.html)
objects as ROS messages. These appear to ROS as
\<\<MsgLink(sensor_msgs/PointCloud2)\>\> messages, offering seamless
interoperability with non-PCL-using ROS nodes. For example, you may
publish a \`pcl::PointCloud\<T\>\` in one of your nodes and visualize it
in [rviz](rviz) using a
[Point Cloud2 display](rviz/DisplayTypes/PointCloud). It works by
hooking into the
[roscpp serialization](roscpp/Overview/MessagesSerializationAndAdaptingTypes)
infrastructure.

The old format \<\<MsgLink(sensor_msgs/PointCloud)\>\> is not supported
in PCL.

### Publishing point clouds

You may publish PCL point clouds using the standard \`ros::Publisher\`:

```cplusplus
#include <ros/ros.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl_conversions/pcl_conversions.h>

typedef pcl::PointCloud<pcl::PointXYZ> PointCloud;

int main(int argc, char** argv)
{
  ros::init (argc, argv, "pub_pcl");
  ros::NodeHandle nh;
  ros::Publisher pub = nh.advertise<PointCloud> ("points2", 1);

  PointCloud::Ptr msg (new PointCloud);
  msg->header.frame_id = "some_tf_frame";
  msg->height = msg->width = 1;
  msg->points.push_back (pcl::PointXYZ(1.0, 2.0, 3.0));

  ros::Rate loop_rate(4);
  while (nh.ok())
  {
    pcl_conversions::toPCL(ros::Time::now(), msg->header.stamp);
    pub.publish (*msg);
    ros::spinOnce ();
    loop_rate.sleep ();
  }
}
```

### Subscribing to point clouds

You may likewise subscribe to PCL point clouds using the standard
\`ros::Subscriber\`:

```cplusplus
#include <ros/ros.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/point_types.h>
#include <boost/foreach.hpp>

typedef pcl::PointCloud<pcl::PointXYZ> PointCloud;

void callback(const PointCloud::ConstPtr& msg)
{
  printf ("Cloud: width = %d, height = %d\n", msg->width, msg->height);
  BOOST_FOREACH (const pcl::PointXYZ& pt, msg->points)
    printf ("\t(%f, %f, %f)\n", pt.x, pt.y, pt.z);
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "sub_pcl");
  ros::NodeHandle nh;
  ros::Subscriber sub = nh.subscribe<PointCloud>("points2", 1, callback);
  ros::spin();
}
```

## ROS nodes

Several tools run as ROS nodes. They convert ROS messages or bags to and
from Point Cloud Data (PCD) file format. ```clearsilver
node.0 {
name=bag_to_pcd
desc=Reads a bag file, saving all ROS point cloud messages on a specified topic as PCD files.
}
```

#### Usage

```
$ rosrun pcl_ros bag_to_pcd <input_file.bag> <topic> <output_directory>
```

Where:

-   \<input_file.bag\> is the bag file name to read.
-   \<topic\> is the topic in the bag file containing messages to save.
-   \<output_directory\> is the directory on disk in which to create PCD
    files from the point cloud messages.

#### Example

Read messages from the \`/laser_tilt_cloud\` topic in \`data.bag\`,
saving a PCD file for each message into the \`./pointclouds\`
subdirectory.

```
$ rosrun pcl_ros bag_to_pcd data.bag /laser_tilt_cloud ./pointclouds
``` ```clearsilver
node.0 {
name=convert_pcd_to_image
desc=Loads a PCD file, publishing it as a ROS image message five times a second.
pub {
0.name=output
0.type=sensor_msgs/Image
0.desc=A stream of images generated from the PCD file.
}
}
```

#### Usage

```
$ rosrun pcl_ros convert_pcd_to_image <cloud.pcd>
```

Read the point cloud in \<cloud.pcd\> and publish it in ROS image
messages at 5Hz. ```clearsilver
node.0 {
name=convert_pointcloud_to_image
desc=Subscribes to a ROS point cloud topic and republishes image messages.
sub {
0.name=input
0.type=sensor_msgs/PointCloud2
0.desc=A stream of point clouds to convert to images.
}
pub {
0.name=output
0.type=sensor_msgs/Image
0.desc=Corresponding stream of images.
}
}
```

#### Examples

Subscribe to the \`/my_cloud\` topic and republish each message on the
\`/my_image\` topic.

```
$ rosrun pcl_ros convert_pointcloud_to_image input:=/my_cloud output:=/my_image
```

To view the images created by the previous command, use
[image_view](image_view). ```cplusplus
#include <ros/ros.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl_conversions/pcl_conversions.h>

typedef pcl::PointCloud<pcl::PointXYZ> PointCloud;

int main(int argc, char** argv)
{
  ros::init (argc, argv, "pub_pcl");
  ros::NodeHandle nh;
  ros::Publisher pub = nh.advertise<PointCloud> ("points2", 1);

  PointCloud::Ptr msg (new PointCloud);
  msg->header.frame_id = "some_tf_frame";
  msg->height = msg->width = 1;
  msg->points.push_back (pcl::PointXYZ(1.0, 2.0, 3.0));

  ros::Rate loop_rate(4);
  while (nh.ok())
  {
    pcl_conversions::toPCL(ros::Time::now(), msg->header.stamp);
    pub.publish (*msg);
    ros::spinOnce ();
    loop_rate.sleep ();
  }
}
```0
```cplusplus
#include <ros/ros.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl_conversions/pcl_conversions.h>

typedef pcl::PointCloud<pcl::PointXYZ> PointCloud;

int main(int argc, char** argv)
{
  ros::init (argc, argv, "pub_pcl");
  ros::NodeHandle nh;
  ros::Publisher pub = nh.advertise<PointCloud> ("points2", 1);

  PointCloud::Ptr msg (new PointCloud);
  msg->header.frame_id = "some_tf_frame";
  msg->height = msg->width = 1;
  msg->points.push_back (pcl::PointXYZ(1.0, 2.0, 3.0));

  ros::Rate loop_rate(4);
  while (nh.ok())
  {
    pcl_conversions::toPCL(ros::Time::now(), msg->header.stamp);
    pub.publish (*msg);
    ros::spinOnce ();
    loop_rate.sleep ();
  }
}
```1

#### Usage

```cplusplus
#include <ros/ros.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl_conversions/pcl_conversions.h>

typedef pcl::PointCloud<pcl::PointXYZ> PointCloud;

int main(int argc, char** argv)
{
  ros::init (argc, argv, "pub_pcl");
  ros::NodeHandle nh;
  ros::Publisher pub = nh.advertise<PointCloud> ("points2", 1);

  PointCloud::Ptr msg (new PointCloud);
  msg->header.frame_id = "some_tf_frame";
  msg->height = msg->width = 1;
  msg->points.push_back (pcl::PointXYZ(1.0, 2.0, 3.0));

  ros::Rate loop_rate(4);
  while (nh.ok())
  {
    pcl_conversions::toPCL(ros::Time::now(), msg->header.stamp);
    pub.publish (*msg);
    ros::spinOnce ();
    loop_rate.sleep ();
  }
}
```2

Where:

-   \<file.pcd\> is the (required) file name to read.
-   \<interval\> is the (optional) number of seconds to sleep between
    messages. If \<interval\> is zero or not specified the message is
    published once.

#### Examples

Publish the contents of \`point_cloud_file.pcd\` once in the
\`/base_link\` frame of reference.

```cplusplus
#include <ros/ros.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl_conversions/pcl_conversions.h>

typedef pcl::PointCloud<pcl::PointXYZ> PointCloud;

int main(int argc, char** argv)
{
  ros::init (argc, argv, "pub_pcl");
  ros::NodeHandle nh;
  ros::Publisher pub = nh.advertise<PointCloud> ("points2", 1);

  PointCloud::Ptr msg (new PointCloud);
  msg->header.frame_id = "some_tf_frame";
  msg->height = msg->width = 1;
  msg->points.push_back (pcl::PointXYZ(1.0, 2.0, 3.0));

  ros::Rate loop_rate(4);
  while (nh.ok())
  {
    pcl_conversions::toPCL(ros::Time::now(), msg->header.stamp);
    pub.publish (*msg);
    ros::spinOnce ();
    loop_rate.sleep ();
  }
}
```3

Publish the contents of \`cloud_file.pcd\` approximately ten times a
second in the \`/odom\` frame of reference.

```cplusplus
#include <ros/ros.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl_conversions/pcl_conversions.h>

typedef pcl::PointCloud<pcl::PointXYZ> PointCloud;

int main(int argc, char** argv)
{
  ros::init (argc, argv, "pub_pcl");
  ros::NodeHandle nh;
  ros::Publisher pub = nh.advertise<PointCloud> ("points2", 1);

  PointCloud::Ptr msg (new PointCloud);
  msg->header.frame_id = "some_tf_frame";
  msg->height = msg->width = 1;
  msg->points.push_back (pcl::PointXYZ(1.0, 2.0, 3.0));

  ros::Rate loop_rate(4);
  while (nh.ok())
  {
    pcl_conversions::toPCL(ros::Time::now(), msg->header.stamp);
    pub.publish (*msg);
    ros::spinOnce ();
    loop_rate.sleep ();
  }
}
```4 ```cplusplus
#include <ros/ros.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl_conversions/pcl_conversions.h>

typedef pcl::PointCloud<pcl::PointXYZ> PointCloud;

int main(int argc, char** argv)
{
  ros::init (argc, argv, "pub_pcl");
  ros::NodeHandle nh;
  ros::Publisher pub = nh.advertise<PointCloud> ("points2", 1);

  PointCloud::Ptr msg (new PointCloud);
  msg->header.frame_id = "some_tf_frame";
  msg->height = msg->width = 1;
  msg->points.push_back (pcl::PointXYZ(1.0, 2.0, 3.0));

  ros::Rate loop_rate(4);
  while (nh.ok())
  {
    pcl_conversions::toPCL(ros::Time::now(), msg->header.stamp);
    pub.publish (*msg);
    ros::spinOnce ();
    loop_rate.sleep ();
  }
}
```5

#### Examples

Subscribe to the \`/velodyne/pointcloud2\` topic and save each message
in the current directory. File names look like
\`1285627014.833100319.pcd\`, the exact names depending on the message
time stamps.

```cplusplus
#include <ros/ros.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl_conversions/pcl_conversions.h>

typedef pcl::PointCloud<pcl::PointXYZ> PointCloud;

int main(int argc, char** argv)
{
  ros::init (argc, argv, "pub_pcl");
  ros::NodeHandle nh;
  ros::Publisher pub = nh.advertise<PointCloud> ("points2", 1);

  PointCloud::Ptr msg (new PointCloud);
  msg->header.frame_id = "some_tf_frame";
  msg->height = msg->width = 1;
  msg->points.push_back (pcl::PointXYZ(1.0, 2.0, 3.0));

  ros::Rate loop_rate(4);
  while (nh.ok())
  {
    pcl_conversions::toPCL(ros::Time::now(), msg->header.stamp);
    pub.publish (*msg);
    ros::spinOnce ();
    loop_rate.sleep ();
  }
}
```6

Set the \`prefix\` parameter in the current namespace, save messages to
files with names like \`/tmp/pcd/vel_1285627015.132700443.pcd\`.

```cplusplus
#include <ros/ros.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl_conversions/pcl_conversions.h>

typedef pcl::PointCloud<pcl::PointXYZ> PointCloud;

int main(int argc, char** argv)
{
  ros::init (argc, argv, "pub_pcl");
  ros::NodeHandle nh;
  ros::Publisher pub = nh.advertise<PointCloud> ("points2", 1);

  PointCloud::Ptr msg (new PointCloud);
  msg->header.frame_id = "some_tf_frame";
  msg->height = msg->width = 1;
  msg->points.push_back (pcl::PointXYZ(1.0, 2.0, 3.0));

  ros::Rate loop_rate(4);
  while (nh.ok())
  {
    pcl_conversions::toPCL(ros::Time::now(), msg->header.stamp);
    pub.publish (*msg);
    ros::spinOnce ();
    loop_rate.sleep ();
  }
}
```7

## More examples

We have more examples on <http://wiki.ros.org/pcl_ros/Tutorials> page
