

```wiki

= THE canonical_scan_matcher PACKAGE IS DISCONTINUED =
the package has been renamed to  [[laser_scan_matcher]] and has been updated with additional features.

The information below be preserved for a while while people switch.
```



![](attachment:canonical_scan_matcher.png)

## Details

The [canonical_scan_matcher](canonical_scan_matcher) package is a
wrapper around Andrea Censi's Canonical Scan Matcher \[1\]
implementation. The package allows to scan match between consecutive
<<MsgLink(sensor_msgs/LaserScan)>> messages, and publish the
estimated position of the laser as a
<<MsgLink(geometry_msgs/Pose2D)>> or a [tf](tf) transform.

The package is intended to be used without any odometry estimation
provided by other sensors. Thus, it can serve as a stand-alone odometry
estimator.

An estimation for theta can optionally be provided to improve accuracy,
in the form of a <<MsgLink(sensor_msgs/Imu)>>. This message would
typically be published by an IMU or other angular rate sensor.

Alternatively, an estimation for x, y, and theta can optionally be
provided to improve accuracy, in the form of a [tf](tf) transform. This
transform would typically be published by an odometry system. This has
not yet been tested.

## Example

You can run the [canonical_scan_matcher](canonical_scan_matcher) on a
pre-recorded bag file that comes with the package. First, make sure you
have the [scan_tools](scan_tools) stack downloaded and installed by
following the instructions [here](scan_tools#Installing).

Next, make sure you have the necessary tools installed:



```shell
rosmake rviz rosbag tf
```



Finally, run the demo:



```shell
roslaunch canonical_scan_matcher demo.launch
```



You should see a result similar to the video below. The video shows CSM
tracking the position of a Hokuyo laser as it is being carried freely
around a room. The pose is determined entirely by the scan matcher - no
additional odometry is provided.

[Youtube](https://www.youtube.com/watch?v=sIMM73Was74)

## Nodes



```clearsilver
 name = csm_node
 desc = The `csm_node` takes in <<MsgLink(sensor_msgs/LaserScan)>> messages, performs scan registration, and outputs an estimate for the displacement of the robot.
sub {
   0{
    name = scan
    type = sensor_msgs/LaserScan
    desc = Scans from a laser range-finder
    }
   1{
    name = imu
    type = sensor_msgs/Imu
    desc = Imu messages, used for theta estimation. Only used if `odometry_type` is set to `imu`.
    }
  }
pub {
   0{
    name = pose2D
    type = geometry_msgs/Pose2D
    desc = The pose of the base frame, in some fixed (world) frame.
   }
  }

param{

    1.name = ~world_frame
    1.type = string
    1.default = `"world"`
    1.desc = the fixed frame

    2.name = ~base_frame
    2.type = string
    2.default = `"base_link"`
    2.desc = the base frame of the robot

    3.name = ~publish_tf
    3.type = bool
    3.default = `true`
    3.desc = whether to publish scan matcher's estimation for the position of the base frame in the world frame as a transform. Disable this if some other node is already publishing an odometric estimation.

    4.name = ~publish_pose
    4.type = bool
    4.default = `true`
    4.desc = whether to publish scan matcher's estimation for the position of the base frame in the world frame as a <<MsgLink(geometry_msgs/Pose2D)>>

    5.name = ~odometry_type
    5.type = string
    5.default = "`none`"
    5.desc = If "`none`", the scan matcher will not use any estimate for the displacement between scans. If "`imu`", the matcher will use as an estimate the yaw value of <<MsgLink(sensor_msgs/Imu)>> messages published on a topic called "`imu`". If "`tf`", the matcher will use as an estimate the x, y, and yaw value of a tf transform between the `world` and `base` frames.

    6.name = ~max_angular_correction_deg
    6.type = double
    6.default = 45.0
    6.desc = Maximum angular displacement between scans, in degrees

    7.name = ~max_linear_correction
    7.type = double
    7.default = 0.50
    7.desc = Maximum translation between scans (m)

    8.name = ~max_iterations
    8.type = int
    8.default = 10
    8.desc = Maximum ICP cycle iterations

    9.name = ~epsilon_xy
    9.type = double
    9.default = 0.001
    9.desc = A threshold for stopping (m)

    10.name = ~epsilon_theta
    10.type = double
    10.default = 0.00872
    10.desc = A threshold for stopping (rad)

    11.name = ~max_correspondence_dist
    11.type = double
    11.default = 0.5
    11.desc = Maximum distance for a correspondence to be valid

    12.name = ~sigma
    12.type = double
    12.default = 0.010
    12.desc = Noise in the scan (m) (Not sure if changing this has any effect in the current implementation)

    13.name = ~use_corr_tricks
    13.type = int
    13.default = 1
    13.desc = If 1, use smart tricks for finding correspondences (see paper).

    14.name = ~restart
    14.type = int
    14.default = 0
    14.desc = Restart: If 1, restart if error is over threshold

    15.name = ~restart_threshold_mean_error
    15.type = double
    15.default = 0.01
    15.desc = Restart: Threshold for restarting

    16.name = ~restart_dt
    16.type = double
    16.default = 1.0
    16.desc = Restart: displacement for restarting. (m)

    17.name = ~restart_dtheta
    17.type = double
    17.default = 0.1
    17.desc = Restart: displacement for restarting. (rad)

    18.name = ~clustering_threshold
    18.type = double
    18.default = 0.25
    18.desc = Max distance for staying in the same clustering

    19.name = ~orientation_neighbourhood
    19.type = int
    19.default = 10
    19.desc = Number of neighbour rays used to estimate the orientation

    20.name = ~use_point_to_line_distance
    20.type = int
    20.default = 1
    20.desc = If 0, it's vanilla ICP

    21.name = ~do_alpha_test
    21.type = int
    21.default = 0
    21.desc = If 1, discard correspondences based on the angles

    22.name = ~do_alpha_test_thresholdDeg
    22.type = double
    22.default = 20.0
    22.desc = Discard correspondences based on the angles - threshold angle, in degrees

    23.name = ~outliers_maxPerc
    23.type = double
    23.default = 0.90
    23.desc = Percentage of correspondences to consider: if 0.90, always discard the top 10% of correspondences with more error

    24.name = ~outliers_adaptive_order
    24.type = double
    25.default = 0.7
    25.desc = Parameters describing a simple adaptive algorithm for discarding. 1) Order the errors. 2) Choose the percentile according to `outliers_adaptive_order` (if it is 0.7, get the 70% percentile). 3) Define an adaptive threshold multiplying `outliers_adaptive_mult` with the value of the error at the chosen percentile. 4) Discard correspondences over the threshold. This is useful to be conservative; yet remove the biggest errors.

    26.name = ~outliers_adaptive_mul
    26.type = double
    26.default = 2.0
    26.desc = Parameters describing a simple adaptive algorithm for discarding. 1) Order the errors. 2) Choose the percentile according to `outliers_adaptive_order` (if it is 0.7, get the 70% percentile). 3) Define an adaptive threshold multiplying `outliers_adaptive_mult` with the value of the error at the chosen percentile. 4) Discard correspondences over the threshold. This is useful to be conservative; yet remove the biggest errors.

    27.name = ~do_visibility_test
    27.type = int
    27.default = 0
    27.desc = If you already have a guess of the solution, you can compute the polar angle of the points of one scan in the new position. If the polar angle is not a monotone function of the readings index, it means that the surface is not visible in the next position. If it is not visible, then we don't use it for matching.

    28.name = ~outliers_remove_doubles
    28.type = int
    28.default = 1
    28.desc = If 1, no two points in laser_sens can have the same correspondence

    29.name = ~do_compute_covariance
    29.type = int
    29.default = 0
    29.desc = If 1, computes the covariance of ICP using the method http://purl.org/censi/2006/icpcov (Changing this has no effect in the current implementation)

    30.name = ~debug_verify_trick
    30.type = int
    30.default = 0
    30.desc = If 1, checks that find_correspondences_tricks gives the right answer

    31.name = ~use_ml_weights
    31.type = int
    31.default = 0
    31.desc = If 1, the field 'true_alpha' (or 'alpha') in the first scan is used to compute the incidence beta, and the factor (1/cos^2(beta)) used to weight the correspondence. (Changing this has no effect in the current implementation)

    32.name = ~use_sigma_weights
    32.type = int
    32.default = 0
    32.desc = If 1, the field 'readings_sigma' in the second scan is used to weight the correspondence by 1/sigma^2 (Not sure if changing this has any effect in the current implementation)
  }

 req_tf{
  0{
    from = world
    to = base_link
    desc = the pose of the robot base in the world frame. Only needed when `use_odometry` is enabled.
  }
  0{
    from = base_link
    to = laser
    desc = the pose of the laser in the base frame. Only needed when `use_odometry` is enabled.
  }
 }

 prov_tf{
  0{
    from = world
    to = base_link
    desc = the pose of the robot base in the world frame. Only provided when `publish_tf` is enabled.
  }
 }
```



## References

\[1\] A. Censi, "An ICP variant using a point-to-line metric"
Proceedings of the IEEE International Conference on Robotics and
Automation (ICRA), 2008

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.

Please use our [Trac](http://robotics.ccny.cuny.edu/trac/) to
[report bugs](http://robotics.ccny.cuny.edu/trac/newticket?component=scan_tools/canonical_scan_matcher&type=defect)
or
[request features](http://robotics.ccny.cuny.edu/trac/newticket?component=scan_tools/canonical_scan_matcher&type=enhancement).
