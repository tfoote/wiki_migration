

```clearsilver
name = height_tracker
desc = 
pub {
  0.name = people_tracker_measurements
  0.type = people_msgs/PositionMeasurement
  1.name = /head_controller/point_head
  1.type = geometry_msgs/PointStamped
  2.name = visualization_marker
  2.type = visualization_msgs/Marker
  3.name = flattened_image
  3.type = sensor_msgs/Image
}
sub { 
  0.name = stereo_namespace/cloud
  0.type = sensor_msgs/PointCloud
  1.name = people_tracker_filter
  1.type = people_msgs/PositionMeasurement
}
param {
  0.name = hack_height
  0.type = 
  0.default = 170.0
  1.name = stereo_namespace
  1.type = string 
  1.default = wide_stereo
  2.name = fixed_frame
  2.type = 
  2.default = string("/base_footprint"
  3.name = do_display
  3.type = 
  3.default = false
  4.name = minimum_x
  4.type = 
  4.default = 0.0
  5.name = maximum_x
  5.type = 
  5.default = 10.0
  6.name = minimum_y
  6.type = 
  6.default = -3.0
  7.name = maximum_y
  7.type = 
  7.default = 3.0
  8.name = minimum_z
  8.type = 
  8.default = 0.0
  9.name = maximum_z
  9.type = 
  9.default = 2.5
  10.name = flattened_width
  10.type = 
  10.default = 640
  11.name = flattened_height
  11.type = 
  11.default = 480
}
```


