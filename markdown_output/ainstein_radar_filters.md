## Overview

This package is intended to contain a variety of data conversion and
filtering utilities. Currently supported are the following:

-   Conversion from radar data to pointcloud data, for use with eg.
    open-source point cloud library PCL
-   Conversion from radar data to laserscan data, for use with eg.
    open-source SLAM package gmapping
-   Filtering of radar data based on range
-   Filtering of radar data based on relative speed in radar frame
-   Filtering of radar data to nearest target
-   Tracking of radar targets based on raw detections

## Conversion Nodes

```clearsilver
node.0 {
name = radar_target_array_to_point_cloud_node
desc = Subscribes to radar data, converts to custom radar pointcloud data and publishes as a standard pointcloud message.
sub {
  0.name = ~radar_in
  0.type = ainstein_radar_msgs/RadarTargetArray
  0.desc = Radar detections (targets) to be converted to pointcloud data.
}
pub {
  0.name = ~cloud_out
  0.type = sensor_msgs/PointCloud2
  0.desc = Published pointcloud data corresponding to input radar data.
}
}
node.1 {
name = radar_target_array_to_laser_scan_node
desc = Subscribes to radar data, converts to and publishes as a standard laserscan message.
sub {
  0.name = ~radar_in
  0.type = ainstein_radar_msgs/RadarTargetArray
  0.desc = Radar detections (targets) to be converted to pointcloud data.
}
pub {
  0.name = ~scan_out
  0.type = sensor_msgs/LaserScan
  0.desc = Published laserscan data corresponding to input radar data.
}
param {
  0.name = ~angle_min
  0.type = float
  0.desc = Minimum angle represented in the laserscan, in radians.
  0.default = -pi/2
  1.name = ~angle_max
  1.type = float
  1.desc = Maximum angle represented in the laserscan, in radians.
  1.default = +pi/2
  2.name = ~angle_increment
  2.type = float
  2.desc = Angle increment per laserscan beam, in radians.
  2.default = 0.0175 (1 degree)
  3.name = ~time_increment
  3.type = float
  3.desc = Time increment per laserscan sample, in seconds.
  3.default = 0.0
  4.name = ~scan_time
  4.type = float
  4.desc = Time increment per scan, in seconds.
  4.default = 0.1
  5.name = ~range_min
  5.type = float
  5.desc = Minimum range of the laserscan, in meters.
  5.default = 0.0
  6.name = ~range_max
  6.type = float
  6.desc = Maximum range of the laserscan, in meters.
  6.default = 100.0
}
}
```

## Filter Nodes

```clearsilver
node.0 {
name = radar_target_array_speed_filter_node and radar_target_array_speed_filter_nodelet
desc = Filters radar targets based on relative speed along the radar measurement direction, assuming radar world-frame velocity is published by another node (eg from GPS). Can filter either by min or max speed (to preserve only stationary or moving targets, respectively); if either min/max speed threshold is not set as a parameter, it is not used for filtering. Also contains untested functionality for using the radar in a rotated fashion for obtaining 3d data.
sub {
  0.name = ~radar_in
  0.type = ainstein_radar_msgs/RadarTargetArray
  0.desc = Radar detections (targets) to be converted to pointcloud data.
  1.name = radar_vel
  1.type = geometry_msgs/Twist
  1.desc = Speed of the radar assumed to be in world (map) frame. Only the linear portion is used. If this topic is not available, no speed filtering is performed and the output radar data is identical to the input.
}
pub {
  0.name = ~radar_out
  0.type = ainstein_radar_msgs/RadarTargetArray
  0.desc = Speed-filtered radar detections (targets).
}
param {
  0.name = ~min_speed_thresh
  0.type = float
  0.desc = Minimum speed of output radar targets, in meters per second.
  0.default = 1.0
  1.name = ~max_speed_thresh
  1.type = float
  1.desc = Maximum speed of output radar targets, in meters per second.
  1.default = 1.0
  2.name = ~compute_3d
  2.type = bool
  2.desc = Specifies whether to use the 2d radar to compute 3d data (UNTESTED).
  2.default = false
  3.name = ~is_rotated
  3.type = bool
  3.desc = If compute_3d is true, then this specifies whether to use speed information to compute elevation if rotated or azimuth if not rotated (UNTESTED).
  3.default = false
}
req_tf {
  0.from = <the frame attached to incoming data>
  0.to   = map
  0.desc = Transformation from the radar data frame to the map (world) frame.
}
}
node.1 {
name = radardata_range filter_node and radardata_range filter_nodelet
desc = Filters radar targets based on reported range, with dynamically-reconfigurable limits.
sub {
  0.name = ~radar_in
  0.type = ainstein_radar_msgs/RadarTargetArray
  0.desc = Radar detections (targets) to be filtered.
}
pub {
  0.name = ~radar_out
  0.type = ainstein_radar_msgs/RadarTargetArray
  0.desc = Range-filtered radar detections (targets).
}
param {
  0.name = ~min_range
  0.type = float
  0.desc = Minimum range of output radar targets, in meters (DYNAMICALLY-RECONFIGURABLE).
  0.default = 0.5
  1.name = ~max_range
  1.type = float
  1.desc = Maximum range of output radar targets, in meters (DYNAMICALLY-RECONFIGURABLE).
  1.default = 10.0
}
}
node.2 {
name = radardata_to_nearest_target_node
desc = Filters radar targets down to the nearest target, published both as a single stamped target and in an array with a single target entry (for compatibility with other nodes). Also performs range filtering and optionally low-pass filters the nearest target data to help smooth the fact that it may jump around considerably (a simple form of target tracking).
sub {
  0.name = ~radar_in
  0.type = ainstein_radar_msgs/RadarTargetArray
  0.desc = Radar detections (targets) to be filtered.
}
pub {
  0.name = ~nearest_target
  0.type = ainstein_radar_msgs/RadarTargetStamped
  0.desc = Nearest radar detection, timestamped.
  1.name = ~nearest_target_array
  1.type = ainstein_radar_msgs/RadarTargetArray
  1.desc = Nearest radar detection as the single entry in a target array.
}
param {
  0.name = ~min_dist_thresh
  0.type = float
  0.desc = Minimum range of filtered radar targets, in meters.
  0.default = 0.0
  1.name = ~max_dist_thresh
  1.type = float
  1.desc = Maximum range of filtered radar targets, in meters.
  1.default = 100.0
  0.name = ~data_lpf_alpha
  0.type = float
  0.desc = Low-pass filter constant (0-1).
  0.default = 0.1
  1.name = ~data_lpf_timeout
  1.type = float
  1.desc = Timeout after which the "tracked" (filtered) target is re-initialized, in seconds.
  1.default = 3.0
}
}
node.3 {
name = radardata_to_tracked_targets_node
desc = Filters raw radar targets into tracked targets by instantiating Kalman Filters for each tracked target, running a simple kinematic process model and updating each with raw targets based on a measurement error check (validation gating). If a raw target does not correspond to an existing tracked target, it is added with a new KF and published after a specified time alive. Conversely, if a tracked target is not updated for a specified period of time, it is dropped from the filter. Additional parameters for the underlying KF implementation exist but are not listed below, see [[https://github.com/AinsteinAI/ainstein_radar/blob/master/ainstein_radar_filters/cfg/TrackingFilter.cfg#L26|here]] and tutorials for details. These generally need not be changed. 
sub {
  0.name = ~radar_in
  0.type = ainstein_radar_msgs/RadarTargetArray
  0.desc = Radar detections (targets) to be used for outputting tracked targets.
}
pub {
  0.name = ~tracked
  0.type = ainstein_radar_msgs/RadarTargetArray
  0.desc = Tracked targets output after updating Kalman Filters.
  1.name = ~boxes
  1.type = jsk_recognition_msgs/BoundingBoxArray
  1.desc = Bounding boxes corresponding to each tracked target, formed from all raw detections associated with that tracked target after the current update.
}
param {
  0.name = ~filter_update_rate
  0.type = int
  0.desc = Rate at which the filter is run, in Hz.
  0.default = 20
  1.name = ~filter_min_time
  1.type = float
  1.desc = Minimum time a target must be tracked before being published, in seconds (DYNAMICALLY-RECONFIGURABLE).
  1.default = 0.5
  2.name = ~filter_timeout
  2.type = float
  2.desc = Maximum time a tracked target can not be updated before being dropped, in seconds (DYNAMICALLY-RECONFIGURABLE).
  2.default = 0.5
  3.name = ~filter_val_gate_thresh
  3.type = string map
  3.desc = Validation gate confidence threshold map - see [[https://github.com/AinsteinAI/ainstein_radar/blob/master/ainstein_radar_filters/cfg/TrackingFilter.cfg#L13|here]] for options (DYNAMICALLY-RECONFIGURABLE).
  3.default = 90.0% confidence
}
}
```
