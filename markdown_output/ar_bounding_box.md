

```clearsilver
name = ar_kinect
desc = Estimates a bounding box around a marker pattern using the Kinect camera and ARToolkit and publishes the contents of this bounding box as point cloud. 
pub {
  0.name = resulting_pcl
  0.type = sensor_msgs/PointCloud2
  0.desc = The resulting point cloud, limited to the bounding box

  1.name = bb_pcl
  1.type = sensor_msgs/PointCloud2
  1.desc = A point cloud with 4 points, describing the bounding box
}
param {
  0.name = boxsize
  0.type = double
  0.default = 0.135
  0.desc = Edge length of the bounding box

  1.name = marker_dist_threshold
  1.type = double
  1.default = 0.002
  1.desc = The maximum allowed error in detecting the markers. If you get too  many "Distance too large" errors, increase this value. Please note that the model quality will decrease with larger values.
}
prov_tf {
  0.from = "/camera_rgb_optical_frame"
  0.to = "/PATTERN_BASE"
  0.desc = The transformation from the camera to the object coordinate system
}
```


