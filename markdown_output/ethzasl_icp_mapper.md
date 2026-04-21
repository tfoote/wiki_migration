## Overview

One of the main problems with point-cloud registration solutions is that
their efficiency often depends on the application. This package provides
a convenient way to tune, test and deploy several registration solutions
using the same node. It provides a real-time tracker and mapper in 2D
and 3D, based on the
[libpointmachter](https://github.com/ethz-asl/libpointmatcher) and
[libnabo](https://github.com/ethz-asl/libnabo) libraries. This allows a
complete configuration of the registration chain through
[YAML](http://www.yaml.org/) files, see the
[chain configuration page](ethzasl_icp_configuration) for a list of
modules and their parameters. You can think of this package as the front
end of a SLAM system, including everything but loop-closure detection
and relaxation.

For installation instructions, see the
[ethzasl_icp_mapping](ethzasl_icp_mapping) stack page. A preliminary
version of this package was deployed in the
[ROS kinect contest](openni/Contests/ROS 3D/Automatic Calibration of Extrinsic Parameters).

## Citing

Two papers talk about our open-source ICP library. The first one
introduces the library and proposes a sound evaluation methodology using
it. It was published in Autonomous Robots and can be found
[ here ](http://link.springer.com/article/10.1007%2Fs10514-013-9327-2 )
([full text](http://publications.asl.ethz.ch/files/pomerleau13comparing.pdf)):


```
@ARTICLE{pomerleau13comparing,
   Author = {F. Pomerleau and F. Colas and R. Siegwart and S. Magnenat},
   Title = {Comparing ICP variants on real-world data sets},
   Journal = {Autonomous Robots},
   Volume = {34},
   Number = {3},
   Month = {April},
   Year = {2013},
   Pages = {133--148}
}
```



In addition, a paper using a preliminary version of this package to
evaluate a Kinect tracker was presented at IROS 2011 and can be found
[ here ](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6094861 )
([fulltext](http://publications.asl.ethz.ch/files/pomerleau11tracking.pdf)):


```
@INPROCEEDINGS{pomerleau11tracking,
    author = {François Pomerleau and Stéphane Magnenat and Francis Colas and Ming Liu and Roland Siegwart},
    title = {Tracking a Depth Camera: Parameter Exploration for Fast ICP},
    booktitle = {Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
    publisher = {IEEE Press},
    pages = {3824--3829},
    year = {2011}
}
```



## Quick Start

Since the proposed ICP chain is highly modular, it has many parameters.
You can play with it directly if you have an
[openni-compatible](openni_camera) sensor: 

```
roscd ethzasl_icp_mapper 
roslaunch launch/openni/tracker_viewer.launch
```

 You
can then have a look into the `launch/openni/` files to see how the
openni tracker is configured. This file roughly corresponds to the
following chain:

![Sample ICP chain for openni](attachment:modular_cloud_matcher_icp_chain_kinect.png)

Starting from this chain, you can
[develop your own chain](ethzasl_icp_configuration).

## Nodes



```clearsilver

name = mapper
desc = This node performs continuous registration of point clouds and publishes the resulting pose using [[tf]] and through <<MsgLink(nav_msgs/Odometry)>> messages. The type of topic messages must be <<MsgLink(sensor_msgs/LaserScan)>> (2D) or <<MsgLink(sensor_msgs/PointCloud2)>> (2D or 3D). This effectively implements a real-time tracker in 2D or 3D.

sub {
  0.name = /scan
  0.type = sensor_msgs/LaserScan
  0.desc = If parameter `~subscribe_scan` is true, the topic on which laser scans (2D) are received.
  1.name = /cloud_in
  1.type = sensor_msgs/PointCloud2
  1.desc = If parameter `~subscribe_cloud` is true, the topic on which point clouds (2D or 3D) are received.
}

pub {
  0.name = /point_map
  0.type = sensor_msgs/PointCloud2
  0.desc = Resulting map (2D or 3D depending on incoming data)
  1.name = /icp_odom
  1.type = nav_msgs/Odometry
  1.desc = sensor to map frame odometry message
  2.name = /icp_error_odom
  2.type = nav_msgs/Odometry
  2.desc = odom to map frame odometry message
}

srv {
  0.name = dynamic_point_map
  0.type = map_msgs/GetPointMap
  0.desc = Return the built map
  1.name = ~save_map
  1.type = map_msgs/SaveMap
  1.desc = Save the built map to the disk
  2.name = ~load_map
  2.type = ethzasl_icp_mapper/LoadMap
  2.desc = Load a map from the disk, reset odom-to-map transform to identity
  3.name = ~reset
  3.type = std_srvs/Empty
  3.desc = Clear the map and reset odom-to-map transform to identity
  4.name = ~correct_pose
  4.type = ethzasl_icp_mapper/CorrectPose
  4.desc = Set the odom-to-map transform
  5.name = ~set_mode
  5.type = ethzasl_icp_mapper/SetMode
  5.desc = Set the localizing/mapping mode
  6.name = ~get_mode
  6.type = ethzasl_icp_mapper/GetMode
  6.desc = Get the current localizing/mapping mode
}

req_tf {
  0.from = sensor frame
  0.to = /odom
  0.desc = sensor to odom frame transform, input from odometry
}

prov_tf {
  0.from = /odom
  0.to = /map
  0.desc = odom to map frame transform, result of ICP
}
```



### Parameters

`icpConfig` (`string`, no default)

. Name of the YAML file configuring the modular ICP chain, see
[Configuration](#Chain_configuration) section.

`useROSLogger` (`bool`, default: `false`)

. If true, use ROS console for logging, otherwise use logger defined in
config file.

`cloudTopic` (`string`, default: `"/camera/rgb/points"`)

. The node listens to the topic whose name is defined by this parameter
and expects a `sensor_msgs/PointCloud2`.

`deltaPoseTopic` (`string`, default: `"/openni_delta_pose"`)

. Topic on which to send delta pose.

`fixedFrame` (`string`, default: `"/world"`)

. Frame name used as fixed frame in the [tf](tf) published by the node.

`sensorFrame` (`string`, default: `"/openni_rgb_optical_frame"`)

. Frame name used as moving frame in the [tf](tf) published by the node.

`startupDropCount` (`unsigned`, default: `0`)

. Number of clouds to drop on startup, useful if sensor is producing
garbage in a startup phase.

## Node: matcher_service

This node provides a service to match two point clouds.

### Services offered

`match_clouds` (ethzasl_icp_mapper/MatchClouds.srv - custom messages
in the package)

. This service takes two `sensor_msgs/PointCloud2` messages as inputs
(the first is the reference and the second the reading) and provides a
`geometry_msgs/Transform` message as output. The resulting
transformation can be used to move the reading point cloud.

### Parameters

As with the `mapper` node, the chain is configured through a
[YAML file](ethzasl_icp_configuration).

`config` (`string`, no default)

. Name of the YAML file configuring the modular ICP chain, see
[ICP chain configuration](ethzasl_icp_configuration) file.

`useROSLogger` (`bool`, default: `false`)

. If true, use ROS console for logging, otherwise use logger defined in
config file.

## Node: occupancy_grid_builder

This node builds a 2D nav_msgs/OccupancyMap from sensor_msgs/LaserScan.
It is yet to be fully documented.

## Limitations

This library solely performs point-cloud registration, it does not
incorporate data fusion based on IMU or odometry. This can be done
through other nodes such as [robot_pose_ekf](robot_pose_ekf).

## Known bugs

The version released in ROS does not work in 2D, please use the latest
git master version for this use case.

## Report a Bug

Please report bugs and request features using the
[github page](https://github.com/ethz-asl/ethzasl_icp_mapping/issues).
