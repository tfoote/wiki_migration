## Overview

[Youtube](https://www.youtube.com/watch?v=uiIi2rSKWAU)

humanoid_localization provides 6D Monte Carlo localization (x,y,z, roll,
pitch, yaw) specifically for humanoid robots. A distance sensor (e.g. 2D
laser or depth camera) is used for either endpoint- or raycasting-based
integration in an existing 3D !OctoMap world model from
[octomap_server](octomap_server). Additionally, IMU and odometry data is
fused in the particle filter. While designated for humanoid robots
(tested with on a Nao with Hokuyo URG-04LX laser), the code may also be
useful e.g. for UAVs.

Details are available in the corresponding publication
**[Humanoid Robot Localization in Complex Indoor Environments](http://hrl.informatik.uni-freiburg.de/papers/hornung10iros.pdf)**
by A. Hornung, K. M. Wurm, and M. Bennewitz (IROS 2010).


```
@INPROCEEDINGS{hornung10iros,
  author = {Armin Hornung and Kai M. Wurm and Maren Bennewitz},
  title = {Humanoid Robot Localization in Complex Indoor Environments},
  booktitle =  {Proc.~of the IEEE/RSJ International Conference on Intelligent 
  Robots and Systems (IROS)},
  year = 2010,
  address = {Taipei, Taiwan},
  month= {October}
}
```



humanoid_localization will request a 3D occupancy map from
[octomap_server](octomap_server), so it needs to be running with the map
loaded that you want to localize in. For the sensor model,
[octomap](octomap) is used for either raycasting or endpoint distance
lookup (the latter currently requires libdynamicEDT3D from !OctoMap 1.5
or later). Details about the required sensor data and tf transforms can
be found below. Once the localization is running, it can initialize the
particles from a given pose by the intial_pose parameter, or by using
the "2D Pose Estimate" tool in RViz (z, roll, and pitch will be
determined automatically). For visualization, set the fixed frame to
"/map" in RViz.

## ROS Node API



```clearsilver
name = localization_node
desc = The main 6D Monte Carlo localization node. Only the most important topics and parameters are documented, check out the source code / yaml files for more details. The code is partly parallelized with OpenMP and will use as many threads as you have processor cores available. You can explicitly set the number of threads with the environment variable OMP_NUM_THREADS.
sub {
  0.name = scan
  0.type = sensor_msgs/LaserScan
  0.desc = 2D laser scan to be integrated
  1.name = point_cloud
  1.type = sensor_msgs/PointCloud2
  1.desc = 3D point cloud to be integrated 
  2.name = imu
  2.type = sensor_msgs/Imu
  2.desc = IMU sensor message (only roll and pitch will be used, if parameter ~use_imu is enabled)
}

pub {
  0.name = pose
  0.type = geometry_msgs/PoseWithCovarianceStamped
  0.desc = Localized particle pose, published after each laser /point cloud callback
  1.name = pose_eval
  1.type = geometry_msgs/PoseWithCovarianceStamped
  1.desc = Localized particle pose, published only when a sensor integration happened in the laser /point cloud callback
  2.name = ~particlecloud
  2.type = geometry_msgs/PoseArray
  2.desc = The complete particle distribution
  3.name = ~best_particle
  3.type = geometry_msgs/PoseArray
  3.desc = The best particle (highest weight or averaged, depends on parameter ~best_particle_as_mean)
}

req_tf{
  0.from = odom
  0.to = torso
  0.desc = Required transform of the robot's base link ("torso" for humanoids, changeable with parameter base_frame_id) in the odometry frame (changeable with parameter odom_frame_id). 
  1.from = torso
  1.to = sensor data frame
  1.desc = Required transform from the robot's base link ("torso" for humanoids, changeable with parameter base_frame_id) to the sensor frame.
}

prov_tf{
  0.from = /map 
  0.to = odom 
  0.desc = Localization publishes the transform from map (global frame, changeable with parameter global_frame_id) to odom (odometry frame, changeable with parameter odom_frame_id)
}

param {
  1.name = ~odom_frame_id
  1.type = string
  1.desc = Odometry frame
  1.default = odom
  2.name = ~base_frame_id
  2.type = string
  2.desc = Base robot frame frame
  2.default = torso
  4.name = ~global_frame_id
  4.type = string
  4.desc = Static global map frame for the provided tf transform
  4.default = /map
  6.name = ~init_global
  6.type = bool
  6.desc = Whether to perform global localization
  6.default = false
  8.name = ~num_particles
  8.type = int
  8.desc = Number of particles to use
  8.default = 500
  9.name = ~neff_factor
  9.type = double
  9.desc = Factor to determine resampling based on the number of effective particles, between 0 (=never) and 1 (always).
  9.default = 1.0
  11.name = ~num_sensor_beams
  11.type = int
  11.desc = Number of beams to use of the sensor, the laser scan or point cloud will be subsampled to that number.
  11.default = 48
  12.name = ~use_raycasting
  12.type = bool
  12.desc = Whether to use the "raycasting" or "endpoint" sensor model. The first is more time-consuming (albeit parallelized), while the latter is only an approximation.
  12.default = true
  13.name = ~use_imu
  13.type = bool
  13.desc = Whether to use the IMU angles (only roll and pitch) in the particle filter. 
  13.default = false  

  20.name= ~update_min_trans
  20.default=0.2
  20.type= double
  20.desc= Translational movement required before performing a filter update (in m)
  21.name= ~update_min_rot
  21.default=&pi;/6.0
  21.type= double
  21.desc= Rotational movement required before performing a filter update (in rad)
  22.name= ~transform_tolerance
  22.default=0.1
  22.type= double
  22.desc= Time in sec. with which to post-date the transform that is published, to indicate that this transform is valid into the future.

  23.name= ~initial_pose/{x/y/z/roll/pitch/yaw}
  23.type= double
  23.desc= Initial pose mean as 3D pose, used to initialize filter with Gaussian distribution.
  24.name= ~initial_std/{x/y/z/roll/pitch/yaw}
  24.type= double
  24.desc= Initial pose standard deviation of the 3D pose, used to initialize filter with Gaussian distribution.

}
```


