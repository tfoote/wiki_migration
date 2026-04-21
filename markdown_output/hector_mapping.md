## Overview

An example video can be seen here:

[Youtube](https://www.youtube.com/watch?v=Cfq3s4-H2S4)

Further video examples are available in this playlist:
<http://www.youtube.com/playlist?list=PL0E462904E5D35E29>

Details can also be found in this paper: 

```
@INPROCEEDINGS{KohlbrecherMeyerStrykKlingaufFlexibleSlamSystem2011,
  author = {S. Kohlbrecher and J. Meyer and O. von Stryk and U. Klingauf},
  title = {A Flexible and Scalable SLAM System with Full 3D Motion Estimation},
  year = {2011},
  month = {November},
  booktitle = {Proc. IEEE International Symposium on Safety, Security and Rescue Robotics (SSRR)},
  organization = {IEEE},
}
```


available
[ here](http://www.sim.tu-darmstadt.de/publ/download/2011_SSRR_KohlbrecherMeyerStrykKlingauf_Flexible_SLAM_System.pdf )
.

## Hardware Requirements

To use `hector_mapping`, you need a source of
<<MsgLink(sensor_msgs/LaserScan)>> data (for example a Hokuyo
UTM-30LX LIDAR or bagfiles). The node uses [tf](tf) for transformation
of scan data, so the LIDAR does not have to be fixed related to the
specified base frame. Odometry data is not needed.

## ROS API



```clearsilver
node.0 {
name=hector_mapping
desc=`hector_mapping` is a node for LIDAR based SLAM with no odometry and low computational resources. For simplicity, the  ROS API detailed below provides information about the commonly used options from a user perspective, but not all options that are available for debugging purposes.

sub{
0.name= scan
0.type= sensor_msgs/LaserScan
0.desc= The laser scan used by the SLAM system.
1.name= syscommand
1.type= std_msgs/String
1.desc= System command. If the string equals "reset" the map and robot pose are reset to their inital state.
}

pub{
   0{
    name = map_metadata
    type = nav_msgs/MapMetaData
    desc = Get the map data from this topic, which is latched, and updated periodically.
   }
   1{
    name = map
    type = nav_msgs/OccupancyGrid
    desc = Get the map data from this topic, which is latched, and updated periodically
   }
2{
name= slam_out_pose
type= geometry_msgs/PoseStamped
desc= The estimated robot pose without covariance
}
3{
name= poseupdate
type= geometry_msgs/PoseWithCovarianceStamped
desc= The estimated robot pose with an gaussian estimate of uncertainty
}

}

 srv {
   0{
    name = dynamic_map
    type = nav_msgs/GetMap
    desc = Call this service to get the map data.
    }
   1{
    name = reset_map
    type = std_srvs/Trigger
    desc = Call this service to reset the map, and hector will start a whole new map from scratch. Notice that this doesn't restart the robot's pose, and it will restart from the last recorded pose.
    }
   2{
    name = pause_mapping
    type = std_srvs/SetBool
    desc = Call this service to stop/start processing laser scans. 
    }
   3{
    name = restart_mapping_with_new_pose
    type = hector_mapping/ResetMapping
    desc = Call this service to reset the map, the robot's pose, and resume mapping (if paused)
    }
  }

param{

0{
name = ~base_frame
type = string
default = base_link
desc = The name of the base frame of the robot. This is the frame used for localization and for transformation of laser scan data.
}
1{
name = ~map_frame
type = string
default = map_link
desc = The name of the map frame.
}
2{
name = ~odom_frame
type = string
default = odom
desc = The name of the odom frame.
}
3{
  name = ~map_resolution
  type = double
  default = 0.025
  desc = The map resolution [m]. This is the length of a grid cell edge.
}
4{
    name = ~map_size
    type = int
    default = 1024
    desc = The size [number of cells per axis] of the map. The map is square and has (map_size * map_size) grid cells.
}
5{
    name = ~map_start_x
    type = double
    default = 0.5
    desc = Location of the origin [0.0, 1.0] of the /map frame on the x axis relative to the grid map. 0.5 is in the middle.
}
6{
  name = ~map_start_y
  type = double
  default = 0.5
  desc = Location of the origin [0.0, 1.0] of the /map frame on the y axis relative to the grid map. 0.5 is in the middle.
}
7{
  name = ~map_update_distance_thresh
  type = double
  default = 0.4
  desc = Threshold for performing map updates [m]. The platform has to travel this far in meters or experience an angular change as described by the map_update_angle_thresh parameter since the last update before a map update happens.  
}
8{
  name = ~map_update_angle_thresh
  type = double
  default = 0.9
  desc = Threshold for performing map updates [rad]. The platform has to experience an angular change as described by this parameter of travel as far as specified by the map_update_distance_thresh parameter since the last update before a map update happens.
}
9{
    name = ~map_pub_period
    type = double
    default = 2.0
    desc = The map publish period [s].
}
10{
    name = ~map_multi_res_levels
    type = int
    default = 3
    desc = The number of map multi-resolution grid levels.
}
11{
    name = ~update_factor_free
    type = double
    default = 0.4
    desc = The map update modifier for updates of free cells in the range [0.0, 1.0]. A value of 0.5 means no change.
}
12{
    name = ~update_factor_occupied
    type = double
    default = 0.9
    desc = The map update modifier for updates of occupied cells in the range [0.0, 1.0]. A value of 0.5 means no change.
}
13{
    name = ~laser_min_dist
    type = double
    default = 0.4
    desc = The minimum distance [m] for laser scan endpoints to be used by the system. Scan endpoints closer than this value are ignored.
}
14{
    name = ~laser_max_dist
    type = double
    default = 30.0
    desc = The maximum distance [m] for laser scan endpoints to be used by the system. Scan endpoints farther away than this value are ignored.
}
15{
    name = ~laser_z_min_value
    type = double
    default = -1.0
    desc = The minimum height [m] relative to the laser scanner frame for laser scan endpoints to be used by the system. Scan endpoints lower than this value are ignored.
}
16{
    name = ~laser_z_max_value
    type = double
    default = 1.0
    desc = The maximum height [m] relative to the laser scanner frame for laser scan endpoints to be used by the system. Scan endpoints higher than this value are ignored.
}
17{
    name = ~pub_map_odom_transform
    type = bool
    default = true
    desc = Determine if the map->odom transform should be published by the system.
}
18{
    name = ~output_timing
    type = bool
    default = false
    desc = Output timing information for processing of every laser scan via ROS_INFO.
}
19{
    name = ~scan_subscriber_queue_size
    type = int
    default = 5
    desc = The queue size of the scan subscriber. This should be set to high values (for example 50) if logfiles are played back to hector_mapping at faster than realtime speeds.
}
20{
    name = ~pub_map_scanmatch_transform
    type = bool
    default = true
    desc = Determines if the scanmatcher to map transform should be published to tf. The frame name is determined by the 'tf_map_scanmatch_transform_frame_name' parameter.
}
21{
    name = ~tf_map_scanmatch_transform_frame_name
    type = string
    default = scanmatcher_frame
    desc = The frame name when publishing the scanmatcher to map transform as described in the preceding parameter.
}
}

 req_tf{
  0{
    from = <the frame attached to incoming scans>
    to = base_frame
    desc = usually a fixed value, broadcast periodically by a [[robot_state_publisher]], or a `tf` [[tf#static_transform_publisher|static_transform_publisher]].
  }
 }

 prov_tf{
  0{
    from = map
    to = odom
    desc = the current estimate of the robot's pose within the map frame (only provided if parameter "pub_map_odom_transform" is true).
  }
 }
```


