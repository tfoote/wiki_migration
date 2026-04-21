## Algorithms

mcl_pi is a package for cooperative robots localization (or for a single
robot). It is based on using a distributed fusion technique for particle
filter named "Particles Intersection" \[1\]. This package contains two
main classes: Monte Carlo Localization (MCL) implementation in python,
based on \[2\], and a Particles Intersection (PI) algorithm based on
\[1\].

This implementation works only with laser scans and occupancy-grid based
maps. The PI algorithm can be extended to any type of recursive Bayesian
estimators, in particular, particle filters.

## Example

[Youtube](https://www.youtube.com/watch?v=CvRHvVOhvw0)

## Nodes



```clearsilver
node.0 {
  name=mcl
  desc=`mcl` takes in an occupancy grid based map, laser scans, and odometry data, and outputs a numerical approximation of the posterior distribution. On startup, `mcl` initializes its particle filter according to the parameters provided.  Note that, because of the defaults, if no parameters are set, the initial filter state will be a moderately sized particle cloud centered about (0,0,0).
  sub{
    0.name= scan
    0.type= sensor_msgs/LaserScan
    0.desc= Laser scans.
    1.name= initialpose
    1.type= geometry_msgs/PoseWithCovarianceStamped
    1.desc= Mean and covariance with which to (re-)initialize the particle filter.
    2.name= map
    2.type= nav_msgs/OccupancyGrid
    2.desc= When the `use_map_topic` parameter is set, mcl subscribes to this topic to retrieve the map used for laser-based localization.
    3.name= odom
    3.type= nav_msgs/Odometry
    3.desc= Odometry data (with covariance)
  }

pub{
    0.name= MCL_estimated_pose
    0.type= geometry_msgs/PoseWithCovarianceStamped
    0.desc= Robot's estimated pose in the map, with covariance.
    1.name= particlecloud
    1.type= geometry_msgs/PoseArray
    1.desc= The set of pose estimates being maintained by the filter.
    2.name= particlecloud2fuse_out
    2.type= geometry_msgs/PoseArray
    2.desc= A particle based estimation of the othere robots state. used for fusion.
    3.name= laser_frame
    3.type= tf/tfMessage
    3.desc= Publishes the transform from `odom` (which can be remapped via the ~odom_frame_id parameter) to `map`.
  }
}

node.1 {
  name=mcl_pi
  desc=`mcl_pi` uses the `mcl` node to run a self-localization algorithm on a single robot. Besides that, it searches robots in a view area when a robot found it subscribes to his `particlecloud2fuse_out` topic and uses it to enhance its localization.
  sub{
    0.name= scan
    0.type= sensor_msgs/LaserScan
    0.desc= Laser scans.
    1.name= initialpose
    1.type= geometry_msgs/PoseWithCovarianceStamped
    1.desc= Mean and covariance with which to (re-)initialize the particle filter.
    2.name= map
    2.type= nav_msgs/OccupancyGrid
    2.desc= When the `use_map_topic` parameter is set, mcl subscribes to this topic to retrieve the map used for laser-based localization.
    3.name= particlecloud2fuse_in
    3.type= geometry_msgs/PoseArray
    3.desc= Particles that appriximate the posterior distribution of the robots state. recived from anothere robot that track this one.
    3.name= odom
    3.type= nav_msgs/Odometry
    3.desc= Odometry data (with covariance)
  }

pub{
    0.name= MCL_estimated_pose
    0.type= geometry_msgs/PoseWithCovarianceStamped
    0.desc= Robot's estimated pose in the map, with covariance.
    1.name= particlecloud
    1.type= geometry_msgs/PoseArray
    1.desc= The set of pose estimates being maintained by the filter.
    2.name= transformed_particles
    2.type= geometry_msgs/PoseArray
    2.desc= A particle based estimation of the othere robots state. used for fusion.
    3.name= laser_frame
    3.type= tf/tfMessage
    3.desc= Publishes the transform from `odom` (which can be remapped via the ~odom_frame_id parameter) to `map`.
    4.name= estimated_pose
    4.type= geometry_msgs/PointStamped
    4.desc= Robot's estimated pose in the map as point)
    5.name= other_robot_observation
    5.type= sensor_msgs/PointCloud
    5.desc= A filtered observations of othere robots (Using a EKF)
    6.name= scope
    6.type= geometry_msgs/PolygonStamped
    6.desc= A scope of the EKF estimation area
  }
}
```



## References

\[1\] Thrun S, Burgard W, Fox D. Probabilistic robotics. MIT press; 2005
Aug 19.

\[2\] Tslil, Or, and Avishy Carmi. "Information fusion using particles
intersection." 2018 IEEE International Conference on Acoustics, Speech
and Signal Processing (ICASSP). IEEE, 2018.

\[3\] Tslil, Or, Feiner Tal, and Avishy Carmi. "Distributed Information
Fusion in Tangle Networks", Under review
