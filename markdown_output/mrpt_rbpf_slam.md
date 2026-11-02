## Description

The sections below describe the API of the package. The interface is
similar to gmapping (<http://wiki.ros.org/gmapping>) but the package
supports different particle filter algorithms, range-only SLAM and can
work with several grid maps simultaneously.

This package supports the following Particle Filter SLAM algorithms
(more details at
<http://www.mrpt.org/tutorials/slam-algorithms/rbpf-slam_algorithms/>):

- Sequential Importance Resampling -- SIR with the "standard" proposal
  distribution (enum value: pfStandardProposal)
- Auxiliary Particle Filter -- APF with the "standard" proposal
  distribution (enum value: pfAuxiliaryPFStandard)
- Optimal proposal distribution (enum value: pfOptimalProposal)
- Approximate Optimal Sampling -- A rejection sampling-based
  approximation to the optimal proposal when a closed-form expression is
  not available (enum value: pfAuxiliaryPFOptimal)

These algorithms allow building **grid map or range-only map**.

## Further documentation

The ROS node `mrpt_rbpf_slam` is a wrapper for the C++ class
****[mrpt::slam::CMetricMapBuilderRBPF](http://reference.mrpt.org/devel/classmrpt_1_1slam_1_1_c_metric_map_builder_r_b_p_f.html),
part of MRPT. Check out the documentation of this class for further
details.

This node has been designed to provide an interface similar to that of
[slam_gmapping](https://index.ros.org/p/slam_gmapping) for the
convenience of users who already know this package.

The coordinate frames are implemented according to the convention
[ROS REP 105: "Coordinate Frames for Mobile Platforms"](http://ros.org/reps/rep-0105.html).

## Usage

In order to use mrpt_rbpf_slam package it is necessary to install the
latest [MRPT](http://www.mrpt.org/) build and the
[mrpt_navigation](http://wiki.ros.org/mrpt_navigation) (see also the
[tutorial](http://wiki.ros.org/mrpt_navigation/Tutorials/Installing)).
Additionally, it is possible to install
[mvsim](http://wiki.ros.org/mvsim) simulator which allows to make
simulations with RBPF SLAM.

## Example

The following video demonstrates the work of the gridmap RBPF-based SLAM
using Rviz and MRPT GUI:

[Youtube](https://www.youtube.com/watch?v=KLMrDmq3G5E&feature)

To run the example of the gridmap RBPF SLAM in online mode, use the
following command:



```
roslaunch mrpt_rbpf_slam rbpf_slam.launch
```



To run the example of the gridmap RBPF SLAM from \*.rawlog file, use the
following command:



```
roslaunch mrpt_rbpf_slam rbpf_slam_rawlog.launch
```



another example is available by running



```
roslaunch mrpt_rbpf_slam rbpf_slam_rawlog.launch example:=2
```



Another possibility is to use the RBPF SLAM package for the range-only
SLAM. The following video demonstrates work of the range only RBPF-based
SLAM using Rviz and MRPT GUI:

[Youtube](https://www.youtube.com/watch?v=ydKxWQh6_qU)

The example usage of the range only RBPF SLAM in online mode:



```
roslaunch mrpt_rbpf_slam ro_slam.launch
```



The example usage of the range only RBPF SLAM from .rawlog file:



```
roslaunch mrpt_rbpf_slam ro_slam_rawlog.launch
```



The following video shows use of the mrpt_rbpf_slam package with mvsim
simulator:

[Youtube](https://www.youtube.com/watch?v=vEjsDGCdkjw)

The example usage of the mrpt_rbpf_slam with mvsim simulator:



```
roslaunch mrpt_rbpf_slam mvsim_slam.launch
```



The package was developed and tested as part of the Google Summer of
Code 2016 project. The following video shows the final tests carried out
with the robot:

[Youtube](https://www.youtube.com/watch?v=HfkRK3lwEgg)

## Nodes



```clearsilver
 name = mrpt_rbpf_slam
 desc = The `mrpt_rbpf_slam` node takes in <<MsgLink(sensor_msgs/LaserScan)>> messages and builds a gridmap (<<MsgLink(nav_msgs/OccupancyGrid)>>) or range only map. The map can be retrieved via a ROS [[Topics|topic]].
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
   2{
    name = beacon
    type = mrpt_msgs/ObservationRangeBeacon
    desc = The beacons for range only map
    }
  }
 pub {
   0{
    name = particlecloud_beacons
    type = geometry_msgs/PoseArray
    desc = The particle cloud where each particle represents the possible location of the beacon
   }
   1{
     name = map
     type = nav_msgs/OccupancyGrid
     desc = Occupancy grid map topic
    }
   2{
    name = particlecloud
    type = geometry_msgs/PoseArray
    desc = Estimate of the robot's pose
   }
   3{
    name = beacon_viz
    type = visualization_msgs/MarkerArray
    desc = Visualization of the beacons with ID 
   }
  }
 param{
    0.name = ~global_frame_id
    0.type = string
    0.default =`"map"`
    0.desc = The frame attached to the map

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
    3.desc = The name of topics with 2d laser scans or beacons (the name of topic should contain word `"scan"` or `"beacon"`)

    4.name = ~ini_filename
    4.type = string
    4.default = None
    4.desc = The path to the ini file with MRPT settings for SLAM (see tutorial folder)

    5.name = ~rawlog_filename
    5.type = string
    5.default = None
    5.desc = The path to rawlog file (if the rawlog file does not exist, the SLAM starts in the online mode) 

    7.name = ~rawlog_play_delay
    7.type = float
    7.default = 0.1
    7.desc = Delay for replaying SLAM from the rawlog file
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



------------------------------------------------------------------------
