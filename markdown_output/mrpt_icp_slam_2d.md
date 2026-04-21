## Description

The sections below describe the API of this package which allows
ICP-based SLAM in 2D *(x,y,phi)*.

The SLAM algorithm is a simple **incremental map building** using ICP to
align 2D laser scans to the map, which can be either a **point map** or
an **occupancy grid map**. \[For now, only point maps\]

Using this technique allows building **small to mid-sized maps**, as
long as errors do not grow excessively before closing any long loop.
Building larger maps requires more advanced SLAM techniques. However,
this simple icp-slam algorithm is an efficient and well-tested method
which suffices for many practical situations.

## Further documentation

The ROS node `mrpt_icp_slam_2d` is a wrapper for the C++ class
[mrpt::slam::CMetricMapBuilderICP](http://reference.mrpt.org/svn/classmrpt_1_1slam_1_1_c_metric_map_builder_i_c_p.html),
part of MRPT. Thus, check out the documentation of that class for
further details.

This node has been designed to provide an interface similar to that of
[slam_gmapping](slam_gmapping) for the convenience of users which
already knew that package.

For the convention on coordinate frames see
[ROS REP 105: "Coordinate Frames for Mobile Platforms"](http://ros.org/reps/rep-0105.html).

## Hardware Requirements

Using `mrpt_icp_slam_2d` requires a horizontally-mounted, fixed, laser
range-finder. Odometry is optional.

The `mrpt_icp_slam_2d` node will attempt to transform each incoming
scan into the `odom` (odometry) [tf](tf) frame. See the
"[Required tf transforms](#tf)" for more on required transforms.

## Usage

In order to use mrpt_icp_slam_2d package it is necessary to install the
last [MRPT](http://www.mrpt.org/) build and
the[mrpt_navigation](http://wiki.ros.org/mrpt_navigation)(see also the
[tutorial](http://wiki.ros.org/mrpt_navigation/Tutorials/Installing)) .

## Example

The following video presents the example of icp SLAM both in Rviz and
MRPT GUI:

[Youtube](https://www.youtube.com/watch?v=cMbI0Ca55gw)

The example of usage icp SLAM in online regime:

```
roslaunch mrpt_icp_slam_2d icp_slam.launch
``` The example of usage icp SLAM from .rawlog
file:

```
roslaunch mrpt_icp_slam_2d icp_slam_rawlog.launch
```

## Nodes

```clearsilver
 name = mrpt_icp_slam_2d
 desc = The `mrpt_icp_slam_2d` node takes in <<MsgLink(sensor_msgs/LaserScan)>> messages and builds a point-cloud map (<<MsgLink(sensor_msgs/PointCloud)>>) or/and gridmap (<<MsgLink(nav_msgs/OccupancyGrid)>>) . The map can be retrieved via a ROS [[Topics|topic]].
 sub {
   0{
    name = tf
    type = tf/tfMessage
    desc = Transforms necessary to relate frames for laser, base, and odometry (see below)
    }
   1{
    name = scan
    type = sensor_msgs/LaserScan
    desc = Laser scans to create the map from
    }
  }
 pub {
   0{
    name = PointCloudMap
    type = sensor_msgs/PointCloud
    desc = Get the point-cloud map data from this topic, which is latched, and updated periodically
   }
   1{
     name = map
     type = nav_msgs/OccupancyGrid
     desc = Occupancy grid map topic
    }
   2{
    name = robot_pose
    type = geometry_msgs/PoseStamped
    desc = Estimate of the robot pose
   }

  }
 param{
    0.name = ~global_frame_id
    0.type = string
    0.default =`"map"`
    0.desc = the frame attached to the map

    1.name = ~base_frame_id
    1.type = string
    1.default = `"base_link"`
    1.desc = The frame attached to the mobile base

    2.name = ~odom_frame_id
    2.type = string
    2.default = `"odom"`
    2.desc = The frame attached to the odometry system

    3.name = ~sensor_source
    3.type = string
    3.default = `"scan"`
    3.desc = The name of topics with 2d laser scans(the name of topic should contaion word `"scan"`)

    4.name = ~ini_filename
    4.type = string
    4.default = None
    4.desc = The path to the ini file with MRPT settings for icp SLAM (see tutorial folder)

    5.name = ~rawlog_filename
    5.type = string
    5.default = None
    5.desc = The path to rawlog file(if the rawlog file is not exists the SLAM starts in online regime) 

    7.name = ~rawlog_play_delay
    7.type = float
    7.default = 0.1
    7.desc = Delay for replay SLAM from rawlog file.
  }

 req_tf{
  0{
    from = <the frame attached to incoming scans>
    to = base_link
    desc = The relative pose of the laser sensor w.r.t. the robot. Usually a fixed value, broadcast periodically by a [[robot_state_publisher]], or a `tf` [[tf#static_transform_publisher|static_transform_publisher]].
  }
  1{
    from = base_link
    to = odom
    desc = The robot odometry, provided by the odometry system (e.g., the driver for the mobile base)
  }
 }
 prov_tf{
  0{
    from = map
    to = odom
    desc = The current estimate of the robot's pose within the map frame
  }
 }
```
