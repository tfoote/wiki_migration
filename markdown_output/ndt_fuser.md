This package contains code for NDT Fuser - a maximum-likelihood mapping
approach with frame-to-model registration.

## Documentation

This package implements NDT fusion - a maximum-likelihood mapping
approach. There are two main templated classes NDTFuser and NDTFuserHMT.
The first class fuses masurements into one single fixed size map. The
second class extends this approach by using a grid of submaps that are
dynamically stored and loaded from disk. For more details on the NDT
Fuser, check out the code API, as well as the tutorials.

## Nodes

This package provides one node - ndt_fuser. ```clearsilver
name = ndt_fuser
desc = fuses 2D or 3D range information into an NDT map
sub {
  0.name = ~/points
  0.type = sensor_msgs/PointCloud2
  0.desc = 3D point clouds to fuse into the model
  1.name = ~/laser_scan
  1.type = sensor_msgs/LaserScan
  1.desc = laser scans if used in a 2D setting and enabled
  2.name = ~/odometry
  2.type = nav_msgs/Odometry
  2.desc = vehicle odometry, if available and enabled 
}
pub {
  0.name = /tf
  0.type = tf/tfMessage
  0.desc = publishes a transform from frame /test to /world with the corrected vehicle position
  1.name = /ndt_map
  1.type = ndt_map/NDTMapMsg
  1.desc = publishes a NDT Map
}
srv {
  0.name = ~/save_map
  0.type = std_srvs/Empty
  0.desc = request the fuser to save the current map
}
```

For detailed description and list of parameters, see the tutorial.

## Tutorials

A tutorial describing how to set-up an NDT fuser node and use it with
your robot is available -
[Using NDT Fuser to create an NDT map](perception_oru/Tutorials/Using NDT Fuser to create an NDT map).
