## Nodes



```clearsilver
 name = kinect_estimation
 desc = Node to do (partial) state estimation using data from a Kinect
 sub {
   0{
    name = ~input
    type = sensor_msgs/PointCloud2
    desc = Point cloud from sensor
    }
   1{
    name = ~indices
    type = pcl/PointIndices
    desc = Indices of point cloud that are inliers of the planar model
    }
   2{
    name = ~model
    type = pcl/ModelCoefficients
    desc = Coefficients of the planar model
    }
   4{
    name = estimator/output
    type = nav_msgs/Odometry
    desc = Backup estimation source (i.e. Vicon). Only subscribed if `~use_backup_estimator_alt` parameter is set.
    }
  }
 pub {
   0{
    name = ~output
    type = nav_msgs/Odometry
    desc = Output state estimate
   }
   1{
    name = ~obstacle
    type = starmac_kinect/Obstacle
    desc = Detected obstacle information
   }
   2{
    name = ~debug
    type = starmac_kinect/Debug
    desc = Testing/debugging information
   }
   3{
    name = ~marker
    type = visualization_msgs/Marker
    desc = Visualization markers
   }
   4{
    name = ~mask_indices
    type = pcl/PointIndices
    desc = Indices of full point cloud that the kinect node is requested to publish
   }
  }
 param{
    0{
   name = ~use_backup_estimator_alt
    type = bool
    default = true
    desc = Whether to use a backup source of altitude state estimate (i.e. Vicon)
}

    1{
    name = ~imu_to_kinect_offset
    type = double
    default = 0.08
    desc =  Vertical distance in meters from IMU to Kinect (positive means Kinect is above IMU)
}

    2{
    name = ~max_est_kinect_delta_alt
    type = double
    default = 0.05
    desc =  Tolerance in meters on distance between Kinect-derived altitude and backup source of altitude data
}
    3{
    name = ~obstacle_height_threshold
    type = double
    default = 0.10
    desc =  Points more than this distance in meters above the ground plane will be considered potential obstacles
}
    4{
    name = ~debug_throttle_rate
    type = double
    default = 0
    desc =  For debugging purposes. Rate in Hz to limit the main callback by. Zero means to disable throttling.
}
    5{
    name = ~z_vel_filt_a
    type = double
    default = 0.9
    desc =  Altitude velocity determination filter parameter.
}
    6{
    name = ~z_vel_filt_b
    type = double
    default = 0.1
    desc =  Altitude velocity determination filter parameter.
}
}
```


