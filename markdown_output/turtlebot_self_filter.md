## Nodes

```clearsilver
name = laser_footprint_filter
desc = Filters out a circular region of a specific size centered about a TF frame.
sub {
  0.name = /scan
  0.type = sensor_msgs/LaserScan
  0.desc = Laser scan from an input sensor.
}
pub {
  0.name = /scan_filtered
  0.type = sensor_msgs/LaserScan
  0.desc = Laser scan with scans within the footprint of the robot set to the max range + 1.0 (out of range).
}
param {
  0.name = ~base_frame
  0.type = string
  0.desc = The frame to center the footprint around.
  0.default = /base_link

  1.name = ~footprint_inscribed_radius
  1.type = double
  1.desc = Radius of the circle inscribing the footprint of the robot in meters.
  1.default = 0.16495
}
req_tf {
  0.from = frame_id of the /scan topic
  0.to   = ~base_frame
  0.desc = It's necessary to be able to transform the laser scan into the base_frame prior to self-filtering.
}
```
