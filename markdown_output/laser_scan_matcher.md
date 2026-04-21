![](attachment:laser_scan_matcher.png)

## Details

The [laser_scan_matcher](laser_scan_matcher) package is an incremental
laser scan registration tool. The package allows to scan match between
consecutive \<\<MsgLink(sensor_msgs/LaserScan)\>\> messages, and publish
the estimated position of the laser as a
\<\<MsgLink(geometry_msgs/Pose2D)\>\> or a [tf](tf) transform.

The package can be used without any odometry estimation provided by
other sensors. Thus, it can serve as a stand-alone odometry estimator.
Alternatively, you can provide several types of odometry input to
improve the registration speed and accuracy.

## Input

### Supported message types

The [laser_scan_matcher](laser_scan_matcher) can operate using
\<\<MsgLink(sensor_msgs/LaserScan)\>\> messages or
\<\<MsgLink(sensor_msgs/PointCloud2)\>\> messages. When using
\<\<MsgLink(sensor_msgs/PointCloud2)\>\>, make sure they have no \`nan\`
values.

### Scan prediction

While the [laser_scan_matcher](laser_scan_matcher) can operate by just
using scan data, we can speed up the scan registration process by
providing a guess for the current position of the sensor every time a
new scan message arrives. When no guess is available, a reasonable (and
widely-used) assumption is that the sensor didn\'t move (zero-velocity
model). Below is a list of inputs that
[laser_scan_matcher](laser_scan_matcher) accepts:

1\. **IMU** :An estimation for the change of the orientation angle
(\`delta-theta\`) of the robot in the form of a
\<\<MsgLink(sensor_msgs/IMU)\>\> message. We are assuming that the
\`yaw\` component of the IMU message corresponds to the orientation of
the robot. Thus, we don\'t really need a full 6DoF IMU sensor - a cheap
1-axis gyro will work as well, as long as its output is packed as an IMU
message. The required topic is \`imu/data\`.

2\. **Wheel odometry**: An estimation for the change of x-, y-, and
orientation angle of the robot from an odometric sensor such as wheel
encoders. The required topic is \`odom\`.

3\. **Constant velocity model**: Assumes the robot moved based on an
estimate of the robot\'s velocity. The velocity estimate can be obtained
from an external sensor, or by derivating and filtering the output of
the scan matcher itself. The required topic is \`vel\`. For an example
of how to use a simple filter to achieve this, check out
[ Alpha-beta tracking for scan matching predictions](AlphaBetaTracking ).

4\. **Zero-velocity model**: Don\'t use any prediction, ie, assume that
the robot stayed in the same place.

We can use combinations of the above such as IMU together with wheel
odometry or IMU together with alpha beta tracking. When several
prediction modes are enabled, the priority is IMU \> Odometry \>
Constant Velocity \> Zero Velocity.

**What should I use in practice?**

IMU and (to some extent) wheel odometry inputs significantly improve
convergence speed for rotational motion. The addition of an IMU input is
thus highly recommended.

Alpha-beta tracking can lead to a significant speed up when the
performance of the scan matcher is stable, but might result in weird
behavior for highly dynamic environments or environments with poor
features. We recommend enabling it and determining empirically if it is
useful for your environment.

### Keyframes vs frame-to-frame scan matching

In the classical frame-to-frame laser odometry, each laser scan is
compared to the previous scan. The transformation between the two is
aggregated over time to calculate the position of the robot in the fixed
frame.

Some noise in the scans is inevitable. Thus, even for a robot standing
still, the incremental transformations might be non-zero. This could
result in a slow drift of the pose of the robot.

To alleviate this, we implement keyframe-based matching. The change in
pose is calculated between the current laser scan and a \"keyframe\"
scan. The keyframe scan is updated after the robot moves a certain
distance. Thus, if the robot is standing still, the keyframe scan will
not change, and the pose will remain more drift free.

Setting the tolerance for updating the keyframe can be achieved via the
\`kf_dist_linear\` and \`kf_dist_angular\` parameters. Their default
values give a more robust performance, both while standing still and
moving.

To change the scan_matching mode back to the classical frame-to-frame,
the user can simply set either of the two thresholds to zero.

## Example

You can run the [laser_scan_matcher](laser_scan_matcher) on a
pre-recorded bag file that comes with the package. First, make sure you
have the [scan_tools](scan_tools) stack downloaded and installed by
following the [instruction instructions](scan_tools#Installing).

```shell
roslaunch laser_scan_matcher demo.launch
```

You should see a result similar to the video below. The video shows
tracking the position of a Hokuyo laser as it is being carried freely
around a room. The pose is determined entirely by the scan matcher - no
additional odometry is provided.

[Youtube](https://www.youtube.com/watch?v=sIMM73Was74)

## ROS API

Two drivers are available: \`laser_scan_matcher_nodelet\` and
\`laser_scan_matcher_node\`. Their parameters and topics are identical.

### Topics

```clearsilver
no_header=True
sub {
   0{
    name = scan
    type = sensor_msgs/LaserScan
    desc = Scans from a laser range-finder
    }
   1{
    name = cloud
    type = sensor_msgs/PointCloud2
    desc = Scans in point cloud form
    }
   2{
    name = imu/data
    type = sensor_msgs/Imu
    desc = Imu messages, used for theta prediction. Only used if `use_imu` is set to `true`.
    }
   3{
    name = odom
    type = nav_msgs/Odometry
    desc = Odometry messages, used for x-, y-, and theta prediction. Only used if `use_odom` is set to `true`.
    }
  }
pub {
   0{
    name = pose2D
    type = geometry_msgs/Pose2D
    desc = The pose of the base frame, in some fixed (world) frame.
   }
  }
```

### Transforms

```clearsilver
no_header=True
 req_tf{
  0{
    from = base_link
    to = laser
    desc = the pose of the laser in the base frame. 
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

### Parameters

#### Coordinate frames

```clearsilver
no_header=True
param{
no_header=True
    0.name = ~fixed_frame
    0.type = string
    0.default = `"world"`
    0.desc = the fixed frame

    1.name = ~base_frame
    1.type = string
    1.default = `"base_link"`
    1.desc = the base frame of the robot
}
```

#### Motion prediction

```clearsilver
no_header=True
param{
no_header=True
    2.name = ~use_imu
    2.type = bool
    2.default = `true`
    2.desc = Whether to use an imu for the theta prediction of the scan registration. Requires input on `/imu/data` topic.

    3.name = ~use_odom
    3.type = bool
    3.default = `true`
    3.desc = Whether to use wheel odometry for the x-, y-, and theta prediction of the scan registration. Requires input on `odom` topic.

    4.name = ~use_vel
    4.type = bool
    4.default = `false`
    4.desc = Whether to use constant velocity model for the x-, y-, and theta prediction of the scan registration. Requires input on `vel` topic.
}
```

#### Pointcloud input

Parameters when using \<\<MsgLink(sensor_msgs/PointCloud2)\>\> instead
of \<\<MsgLink(sensor_msgs/LaserScan)\>\> messages.

```clearsilver
no_header=True
param{
no_header=True
    5.name = ~use_cloud_input
    5.type = bool
    5.default = `false`
    5.desc = Whether to subscribe to a `/cloud` topic with <<MsgLink(sensor_msgs/PointCloud2)>> messages instead of a `/scan` topic with <<MsgLink(sensor_msgs/LaserScan)>> messages.

    6.name = ~cloud_range_min
    6.type = double
    6.default = 0.1
    6.desc = The minimum range of the sensor, if using <<MsgLink(sensor_msgs/PointCloud2)>> messages. Not needed if using <<MsgLink(sensor_msgs/LaserScan)>> messages.

    7.name = ~cloud_range_max
    7.type = double
    7.default = 50.0
    7.desc = The maximum range of the sensor, if using <<MsgLink(sensor_msgs/PointCloud2)>> messages. Not needed if using <<MsgLink(sensor_msgs/LaserScan)>> messages.
}
```

#### Keyframes

Parameters for setting up keyframe-scan based registration. Using the
default values, the keyframe is updated when the sensor moves 10 cm or
10 degrees. Setting either of these to zero will reduce to
frame-to-frame scan matching. Keeping them at default levels should
reduce drift while robot is stationary.

```clearsilver
no_header=True
param{
no_header=True
    8.name = ~kf_dist_linear
    8.type = double
    8.default = 0.10
    8.desc = What distance the fixed frame needs to move before updating the keyframe scan (in meters)

    9.name = ~kf_dist_angular
    9.type = double
    9.default = 0.175
    9.desc = What angle the fixed frame needs to move before updating the keyframe scan (in radians).
}
```

#### Output

```clearsilver
no_header=True
param{
no_header=True
    10.name = ~publish_tf
    10.type = bool
    10.default = `true`
    10.desc = whether to publish scan matcher's estimation for the position of the base frame in the world frame as a transform. 

    11.name = ~publish_pose
    11.type = bool
    11.default = `true`
    11.desc = whether to publish scan matcher's estimation for the position of the base frame in the world frame as a <<MsgLink(geometry_msgs/Pose2D)>>

    12.name = ~publish_pose_stamped
    12.type = bool
    12.default = `false`
    12.desc = whether to publish scan matcher's estimation for the position of the base frame in the world frame as a <<MsgLink(geometry_msgs/PoseStamped)>>
}
```

#### Scan matching

```clearsilver
no_header=True
param{
no_header=True

    13.name = ~max_iterations
    13.type = int
    13.default = 10
    13.desc = Maximum ICP cycle iterations

    14.name = ~max_correspondence_dist
    14.type = double
    14.default = 0.3
    14.desc = Maximum distance for a correspondence to be valid

    15.name = ~max_angular_correction_deg
    15.type = double
    15.default = 45.0
    15.desc = Maximum angular displacement between scans, in degrees

    16.name = ~max_linear_correction
    16.type = double
    16.default = 0.50
    16.desc = Maximum translation between scans (m)

    17.name = ~epsilon_xy
    17.type = double
    17.default = 0.000001
    17.desc = A threshold for stopping (m)

    18.name = ~epsilon_theta
    18.type = double
    18.default = 0.000001
    18.desc = A threshold for stopping (rad)

    19.name = ~outliers_maxPerc
    19.type = double
    19.default = 0.90
    19.desc = Percentage of correspondences to consider: if 0.90, always discard the top 10% of correspondences with more error

}
```

#### Scan matching (advanced)

```clearsilver
no_header=True
param{
no_header=True

    20.name = ~sigma
    20.type = double
    20.default = 0.010
    20.desc = Noise in the scan (m) (Not sure if changing this has any effect in the current implementation)

    21.name = ~use_corr_tricks
    21.type = int
    21.default = 1
    21.desc = If 1, use smart tricks for finding correspondences (see paper).

    22.name = ~restart
    22.type = int
    22.default = 0
    22.desc = Restart: If 1, restart if error is over threshold

    23.name = ~restart_threshold_mean_error
    23.type = double
    23.default = 0.01
    23.desc = Restart: Threshold for restarting

    24.name = ~restart_dt
    24.type = double
    24.default = 1.0
    24.desc = Restart: displacement for restarting. (m)

    25.name = ~restart_dtheta
    25.type = double
    25.default = 0.1
    25.desc = Restart: displacement for restarting. (rad)

    26.name = ~clustering_threshold
    26.type = double
    26.default = 0.25
    26.desc = Max distance for staying in the same clustering

    27.name = ~orientation_neighbourhood
    27.type = int
    27.default = 10
    27.desc = Number of neighbour rays used to estimate the orientation

    28.name = ~use_point_to_line_distance
    28.type = int
    28.default = 1
    28.desc = If 0, it's vanilla ICP

    29.name = ~do_alpha_test
    29.type = int
    29.default = 0
    29.desc = If 1, discard correspondences based on the angles

    30.name = ~do_alpha_test_thresholdDeg
    30.type = double
    30.default = 20.0
    30.desc = Discard correspondences based on the angles - threshold angle, in degrees

    31.name = ~outliers_adaptive_order
    31.type = double
    31.default = 0.7
    31.desc = Parameters describing a simple adaptive algorithm for discarding. 1) Order the errors. 2) Choose the percentile according to `outliers_adaptive_order` (if it is 0.7, get the 70% percentile). 3) Define an adaptive threshold multiplying `outliers_adaptive_mult` with the value of the error at the chosen percentile. 4) Discard correspondences over the threshold. This is useful to be conservative; yet remove the biggest errors.

    32.name = ~outliers_adaptive_mul
    32.type = double
    32.default = 2.0
    32.desc = Parameters describing a simple adaptive algorithm for discarding. 1) Order the errors. 2) Choose the percentile according to `outliers_adaptive_order` (if it is 0.7, get the 70% percentile). 3) Define an adaptive threshold multiplying `outliers_adaptive_mult` with the value of the error at the chosen percentile. 4) Discard correspondences over the threshold. This is useful to be conservative; yet remove the biggest errors.

    33.name = ~do_visibility_test
    33.type = int
    33.default = 0
    33.desc = If you already have a guess of the solution, you can compute the polar angle of the points of one scan in the new position. If the polar angle is not a monotone function of the readings index, it means that the surface is not visible in the next position. If it is not visible, then we don't use it for matching.

    34.name = ~outliers_remove_doubles
    34.type = int
    34.default = 1
    34.desc = If 1, no two points in laser_sens can have the same correspondence

    35.name = ~do_compute_covariance
    35.type = int
    35.default = 0
    35.desc = If 1, computes the covariance of ICP using the method http://purl.org/censi/2006/icpcov (Changing this has no effect in the current implementation)

    36.name = ~debug_verify_trick
    36.type = int
    36.default = 0
    36.desc = If 1, checks that find_correspondences_tricks gives the right answer

    37.name = ~use_ml_weights
    37.type = int
    37.default = 0
    37.desc = If 1, the field 'true_alpha' (or 'alpha') in the first scan is used to compute the incidence beta, and the factor (1/cos^2(beta)) used to weight the correspondence. (Changing this has no effect in the current implementation)

    38.name = ~use_sigma_weights
    38.type = int
    38.default = 0
    38.desc = If 1, the field 'readings_sigma' in the second scan is used to weight the correspondence by 1/sigma^2 (Not sure if changing this has any effect in the current implementation)
  }
```

## References

\[1\] A. Censi, \"An ICP variant using a point-to-line metric\"
Proceedings of the IEEE International Conference on Robotics and
Automation (ICRA), 2008

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports and
feature requests.

Please submit your tickets through
[github](https://github.com/ccny-ros-pkg/scan_tools/issues/) (requires
github account) or by emailing the maintainers.
