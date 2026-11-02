![attachment:polar_scan_matching.png](doc/polar_scan_matching.png)

## Details

The polar_scan_matcher package is a
wrapper around Polar Scan Matcher \[1\], courtesy of:

Albert Diosi and Lindsay Kleeman\
Intelligent Robotics Research Centre (IRRC)\
Monash University\
<http://www.irrc.monash.edu.au/adiosi/downloads.html>\

The package allows to scan match between consecutive
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
messages, and publish the estimated position of the laser as a
[geometry_msgs/msg/Pose2D](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Pose2D.html)
or a [tf](https://index.ros.org/p/tf) transform.

The package is intended to be used without any odometry estimation
provided by other sensors. Thus, it can serve as a stand-alone odometry
estimator.

An estimation for theta can optionally be provided to improve accuracy,
in the form of a
[sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html).
This message would typically be published by an IMU or other angular
rate sensor.

Alternatively, an estimation for x, y, and theta can optionally be
provided to improve accuracy, in the form of a
[tf](https://index.ros.org/p/tf) transform. This transform would
typically be published by an odometry system. This has not yet been
tested.

## Example

You can run the polar_scan_matcher on
a pre-recorded bag file that comes with the package. First, make sure
you have the [scan_tools](https://index.ros.org/p/scan_tools) stack
downloaded and installed by following the instructions
[here](https://index.ros.org/p/scan_tools).

Next, make sure you have the necessary tools installed:



```shell
rosmake rviz rosbag tf
```



Finally, run the demo:



```shell
roslaunch polar_scan_matcher demo.launch
```



You should see a result similar to the video below. The video shows PSM
tracking the position of a Hokuyo laser as it is being carried freely
around a room. The pose is determined entirely by the scan matcher - no
additional odometry is provided.

[Youtube](https://www.youtube.com/watch?v=moJP1zGgAoI)

## Nodes

### psm_node

The `psm_node` takes in
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
messages, performs scan registration, and outputs an estimate for the
displacement of the robot.

#### Subscribed Topics

- `scan`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Scans from a laser range-finder
- `imu`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Imu messages, used for theta estimation. Only used if
  `odometry_type` is set to `imu`.

#### Published Topics

- `pose2D`
  ([geometry_msgs/msg/Pose2D](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Pose2D.html)):
  The pose of the base frame, in some fixed (world) frame.

#### Parameters

- `~world_frame` (`string`, default: `"world"`): the fixed frame
- `~base_frame` (`string`, default: `"base_link"`): the base frame
  of the robot
- `~publish_tf` (`bool`, default: `true`): whether to publish scan
  matcher's estimation for the position of the base frame in the world
  frame as a transform. Disable this if some other node is already
  publishing an odometric estimation.
- `~publish_pose` (`bool`, default: `true`): whether to publish scan
  matcher's estimation for the position of the base frame in the world
  frame as a
  [geometry_msgs/msg/Pose2D](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Pose2D.html)
- `~odometry_type` (`string`, default: "`none`"): If "`none`",
  the scan matcher will not use any estimate for the displacement
  between scans. If "`imu`", the matcher will use as an estimate the
  yaw value of
  [sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)
  messages published on a topic called "`imu`". If "`tf`", the
  matcher will use as an estimate the x, y, and yaw value of a tf
  transform between the `world` and `base` frames.
- `~min_valid_points` (`int`, default: `200`): the minimum valid
  points required to perform a scan match
- `~search_window` (`int`, default: `40`): the window in which to
  search for a match for the rotation. The units are number of laser
  scan beams.
- `~max_error` (`double`, default: `0.20`): the maximum distance, in
  meters, for correlating two points.
- `~max_iterations` (`int`, default: `20`): the maximum number of
  algorithm iterations
- `~stop_condition` (`double`, default: `0.01`): the stop condition,
  in meters, for the variance of the error

#### Required tf Transforms

- `base_link` → `laser`: the pose of the laser in the base frame. Only
  needed when `use_odometry` is enabled.

#### Provided tf Transforms

- `world` → `base_link`: the pose of the robot base in the world frame.
  Only provided when `publish_tf` is enabled.

## References

\[1\] A. Diosi and L. Kleeman, "Laser Scan Matching in Polar
Coordinates with Application to SLAM " Proceedings of 2005 IEEE/RSJ
International Conference on Intelligent Robots and Systems, August,
2005, Edmonton, Canada

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.

Please use our [Trac](http://robotics.ccny.cuny.edu/trac/) to
[report bugs](http://robotics.ccny.cuny.edu/trac/newticket?component=scan_tools/polar_scan_matcher&type=defect)
or
[request features](http://robotics.ccny.cuny.edu/trac/newticket?component=scan_tools/polar_scan_matcher&type=enhancement).
