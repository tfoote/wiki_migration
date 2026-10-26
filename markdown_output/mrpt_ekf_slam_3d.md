## Description

The sections below describe the API of this package for 3D EKF-based
SLAM. This method takes input measurements to landmarks in the form of
range-bearing observations.

## Further documentation

The ROS node mrpt_ekf_slam_3d is a wrapper for the C++ class
[mrpt::slam::CRangeBearingKFSLAM](http://reference.mrpt.org/devel/classmrpt_1_1slam_1_1_c_range_bearing_k_f_s_l_a_m.html)
****, part of MRPT. Thus, check out the documentation of that class for
further details.

For the convention on coordinate frames see
[ROS REP 105: "Coordinate Frames for Mobile Platforms"](http://ros.org/reps/rep-0105.html).

## Usage

In order to use mrpt_ekf_slam_3d package it is necessary to install the
last [MRPT](http://www.mrpt.org/) build and
the[mrpt_navigation](http://wiki.ros.org/mrpt_navigation)(see also the
[tutorial](http://wiki.ros.org/mrpt_navigation/Tutorials/Installing)) .

## Example

The following video represents the EKF 3D SLAM in Rviz and MRPT GUI:

[Youtube](https://www.youtube.com/watch?v=8myjTFCanP8)

The example of usage EKF 3D SLAM in online regime:



```
roslaunch mrpt_ekf_slam_3d ekf_slam_3d.launch
```

 The example of usage EKF 3D SLAM from .rawlog
file:



```
roslaunch mrpt_ekf_slam_3d ekf_slam_3d_rawlog.launch
```



## Nodes



```clearsilver
 name = mrpt_ekf_slam_3d
 desc = The `mrpt_ekf_slam_3d` node takes in mrpt_msgs/ObservationRangeBearing messages and builds a map with landmarks and robot pose. The map can be retrieved via a ROS [[Topics|topic]].
 sub {
   0{
    name = tf
    type = tf/tfMessage
    desc = Transforms necessary to relate frames for laser, base, and odometry (see below)
    }
   1{
    name = landmark
    type = mrpt_msgs/ObservationRangeBearing
    desc = Landmarks to create the map 
    }
  }
 pub {
   0{
    name = state_viz
    type = visualization_msgs/MarkerArray
    desc = Visualization of the current state of the EKF 
   }
   1{
     name = data_association_viz
     type = visualization_msgs/MarkerArray
     desc = Visualization of the currently observed landmarks by robot 
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
    3.desc = The name of topics with 2d laser scans or beacons (the name of topic should contaion word `"scan"` or `"beacon"`)

    4.name = ~ini_filename
    4.type = string
    4.default = None
    4.desc = The path to the ini file with MRPT settings for SLAM (see tutorial folder)

    5.name = ~rawlog_filename
    5.type = string
    5.default = None
    5.desc = The path to rawlog file(if the rawlog file is not exists the SLAM starts in online regime) 

    7.name = ~rawlog_play_delay
    7.type = float
    7.default = 0.1
    7.desc = Delay for replay SLAM from rawlog file.

    8.name = ~ellipse_scale
    8.type = float
    8.default = 1
    8.desc = The parameter for rescaling covariance ellipses visualization.
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


