## Package Summary

The [cob_3d_mapping_filters](cob_3d_mapping_filters) package contains
nodes for noise filtering of point clouds. Input data is supposed to
come from 3-D cameras like Microsoft Kinect.

## Overview

There are several filter algorithms implemented in this package.



```clearsilver
name = amplitude_filter
desc = Thresholding filter on the amplitude channel.

goal{
}
result{
}

feedback{
}
sub{
 0.name = /point_cloud2
 0.type = sensor_msgs/PointCloud2 
 0.desc = Input topic.
 }
 
 pub{
  0.name = /point_cloud2_filtered
  0.type = sensor_msgs/PointCloud2  
  0.desc = Filtered point cloud.
 }

param{
 0.name = ~amplitude_min_threshold
 0.type = double
 0.default = 500
 0.desc = Minimum amplitude threshold. All values below are filtered out.
 1.name = ~amplitude_max_threshold
 1.type = double
 1.default = 60000
 1.desc = Maximum amplitude threshold. All values above are filtered out.
}
```





```clearsilver
name = intensity_filter
desc = Thresholding filter on the intensity channel.

goal{
}
result{
}

feedback{
}
sub{
 0.name = /point_cloud2
 0.type = sensor_msgs/PointCloud2 
 0.desc = Input topic.
 }
 
 pub{
  0.name = /point_cloud2_filtered
  0.type = sensor_msgs/PointCloud2  
  0.desc = Filtered point cloud.
 }

param{
 0.name = ~intensity_min_threshold
 0.type = double
 0.default = 2000
 0.desc = Minimum intensity threshold. All values below are filtered out.
 1.name = ~intensity_max_threshold
 1.type = double
 1.default = 60000
 1.desc = Maximum intensity threshold. All values above are filtered out.
}
```





```clearsilver
name = cob_3d_mapping_filters/JumpEdgeFilter
desc = Filter for removing jump edges that occur in TOF point clouds or during fast camera movement. Implements the method described in Stefan Fuchs and Stefan May:  [[http://www.robotic.dlr.de/fileadmin/robotic/fuchs/TOFCamerasFuchsMay2007.pdf|Calibration and Registration for Precise Surface Reconstruction]], In Proceedings of the DAGM Dyn3D Workshop, September, 2007, Heidelberg, Germany

goal{
}
result{
}

feedback{
}
sub{
 0.name = ~point_cloud_in
 0.type = sensor_msgs/PointCloud2 
 0.desc = Input topic.
 }
 
 pub{
  0.name = ~point_cloud_out
  0.type = sensor_msgs/PointCloud2  
  0.desc = Filtered point cloud.
 }

param{
 0.name = ~upper_angle_deg
 0.type = double
 0.default = 170
 0.desc = Max angle between neighbouring points to be detected as jump edge (degree).
}
```





```clearsilver
name = smoothing_filter
desc = 

goal{
}
result{
}

feedback{
}
sub{
 0.name = /point_cloud2
 0.type = sensor_msgs/PointCloud2 
 0.desc = Input topic.
 }
 
 pub{
  0.name = /point_cloud2_filtered
  0.type = sensor_msgs/PointCloud2  
  0.desc = Filtered point cloud.
 }

param{
 0.name = ~edge_threshold
 0.type = double
 0.default = 0.05
 0.desc = 
 1.name = ~smoothing_factor
 1.type = double
 1.default = 0.25
 1.desc = 
 2.name = ~integral_factor
 2.type = double
 2.default = 0.25
 2.desc = 
}
```





```clearsilver
name = speckle_filter
desc = Outlier removal filter based on region growing (speckles).

goal{
}
result{
}

feedback{
}
sub{
 0.name = /point_cloud2
 0.type = sensor_msgs/PointCloud2 
 0.desc = Input topic.
 }
 
 pub{
  0.name = /point_cloud2_filtered
  0.type = sensor_msgs/PointCloud2  
  0.desc = Filtered point cloud.
 }

param{
 0.name = ~speckle_size
 0.type = double
 0.default = 50
 0.desc = Minimum allowed size of a speckle (number of points).
 1.name = ~speckle_range
 1.type = double
 1.default = 0.1
 1.desc = Minimum allowed distance between two speckles.
}
```


