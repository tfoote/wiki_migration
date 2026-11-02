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
[slam_gmapping](https://index.ros.org/p/slam_gmapping) for the
convenience of users which already knew that package.

For the convention on coordinate frames see
[ROS REP 105: "Coordinate Frames for Mobile Platforms"](http://ros.org/reps/rep-0105.html).

## Hardware Requirements

Using `mrpt_icp_slam_2d` requires a horizontally-mounted, fixed, laser
range-finder. Odometry is optional.

The `mrpt_icp_slam_2d` node will attempt to transform each incoming
scan into the `odom` (odometry) [tf](https://index.ros.org/p/tf)
frame. See the
"Required tf transforms" for more
on required transforms.

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
```

 The example of usage icp SLAM from .rawlog
file:



```
roslaunch mrpt_icp_slam_2d icp_slam_rawlog.launch
```



## Nodes

### mrpt_icp_slam_2d

The `mrpt_icp_slam_2d` node takes in
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
messages and builds a point-cloud map
([sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html))
or/and gridmap
([nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html))
. The map can be retrieved via a ROS [topic](Topics).

#### Subscribed Topics

- `tf`
  ([tf/msg/tfMessage](https://docs.ros.org/en/rolling/p/tf/msg/tfMessage.html)):
  Transforms necessary to relate frames for laser, base, and odometry
  (see below)
- `scan`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Laser scans to create the map from

#### Published Topics

- `PointCloudMap`
  ([sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html)):
  Get the point-cloud map data from this topic, which is latched, and
  updated periodically
- `map`
  ([nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)):
  Occupancy grid map topic
- `robot_pose`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Estimate of the robot pose

#### Parameters

- `~global_frame_id` (`string`, default: `"map"`): the frame
  attached to the map
- `~base_frame_id` (`string`, default: `"base_link"`): The frame
  attached to the mobile base
- `~odom_frame_id` (`string`, default: `"odom"`): The frame attached
  to the odometry system
- `~sensor_source` (`string`, default: `"scan"`): The name of topics
  with 2d laser scans(the name of topic should contaion word
  `"scan"`)
- `~ini_filename` (`string`, default: `None`): The path to the ini file
  with MRPT settings for icp SLAM (see tutorial folder)
- `~rawlog_filename` (`string`, default: `None`): The path to rawlog
  file(if the rawlog file is not exists the SLAM starts in online
  regime)
- `~rawlog_play_delay` (`float`, default: `0.1`): Delay for replay SLAM
  from rawlog file.

#### Required tf Transforms

- `<the frame attached to incoming scans>` → `base_link`: The relative
  pose of the laser sensor w.r.t. the robot. Usually a fixed value,
  broadcast periodically by a
  [robot_state_publisher](https://index.ros.org/p/robot_state_publisher),
  or a `tf` [static_transform_publisher](https://index.ros.org/p/tf).
- `base_link` → `odom`: The robot odometry, provided by the odometry
  system (e.g., the driver for the mobile base)

#### Provided tf Transforms

- `map` → `odom`: The current estimate of the robot's pose within the
  map frame
