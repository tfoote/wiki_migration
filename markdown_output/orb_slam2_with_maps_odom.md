## Overview

This project is based on ORB_SLAM2 generate and release pointcloud data,
octree data and 2D grid occupy map. And map saving and overloading are
added.

## Node API



```clearsilver
name = Topic
sub {
  0.name = /camera/color/image_raw
  0.type = sensor_msgs/Image
  0.desc = Camera RGB image.
  1.name = /camera/depth/image_rect_raw
  1.type =sensor_msgs/Image
  1.desc = Camera depth image.
  2.name = /orbslam2/pointcloud
  2.type = sensor_msgs/PointCloud2
  2.desc = Point cloud image
}
pub {
  0.name = /orbslam2/octomap
  0.type = octomap_msgs/Octomap
  0.desc = Octree map.
  1.name = /orbslam2/occupancymap
  1.type = octomap_msgs/Octomap
  1.desc = Two-digit occupancy grid map.
  2.name = /orbslam2/odometry
  2.type = nav_msgs/Odometry
  2.desc = Odom frame data.
}
```


