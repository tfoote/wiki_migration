```clearsilver
name = corridor_extraction
desc = This node generates flight commands based on the sensor data provided by the Kinect sensor to navigate a UAV down a corridor.
sub {
  0.name = /camera/depth/image_raw
  0.type = sensor_msgs/Image
  0.desc = The depth image provided by the Kinect sensor.
  1.name = /camera/depth/points2
  1.type = sensor_msgs/PointCloud2
  1.desc = The 3D point cloud provided by the Kinect sensor.
}
pub {
  0.name = /kinectPose
  0.type = kinect_utils/kinectPose
  0.desc = The estimated position and orientation of the Kinect sensor within the corridor.
  1.name = /flightCommand
  1.type = kinect_utils/flightCommand
  1.desc = The calculated motion vector (`[dx, dy, dz, dyaw]`). The raw vector (`[dx_raw, dy_raw, dz_raw, dyaw_raw]`) does not consider any obstacles.
  2.name = /wall_marker
  2.type = visualization_msgs/Marker
  2.desc = The marker of the estimated walls for visualization with `rviz`.
  3.name = /flightCommand_marker
  3.type = visualization_msgs/Marker
  3.desc = The marker of the motion vector for visualization with `rviz`.
  4.name = /unmatchedPoints
  4.type = sensor_msgs/PointCloud2
  4.desc = Points which are not contained in one of the wall planes and thus may be part of possible obstacles.
}
```
