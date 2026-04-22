![](attachment:polar_scan_matching.png)

## Details

The [polar_scan_matcher](polar_scan_matcher) package is a wrapper around
Polar Scan Matcher \[1\], courtesy of:

Albert Diosi and Lindsay Kleeman\
Intelligent Robotics Research Centre (IRRC)\
Monash University\
<http://www.irrc.monash.edu.au/adiosi/downloads.html>\

The package allows to scan match between consecutive
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
messages, and publish the estimated position of the laser as a
[geometry_msgs/msg/Pose2D](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Pose2D.html)
or a [tf](tf) transform.

The package is intended to be used without any odometry estimation
provided by other sensors. Thus, it can serve as a stand-alone odometry
estimator.

An estimation for theta can optionally be provided to improve accuracy,
in the form of a
[sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html).
This message would typically be published by an IMU or other angular
rate sensor.

Alternatively, an estimation for x, y, and theta can optionally be
provided to improve accuracy, in the form of a [tf](tf) transform. This
transform would typically be published by an odometry system. This has
not yet been tested.

## Example

You can run the [polar_scan_matcher](polar_scan_matcher) on a
pre-recorded bag file that comes with the package. First, make sure you
have the [scan_tools](scan_tools) stack downloaded and installed by
following the instructions [here](scan_tools#Installing).

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



```clearsilver
 name = psm_node
 desc = The `psm_node` takes in <<MsgLink(sensor_msgs/LaserScan)>> messages, performs scan registration, and outputs an estimate for the displacement of the robot.
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

    6.name = ~min_valid_points
    6.type = int
    6.default = `200`
    6.desc = the minimum valid points required to perform a scan match

    7.name = ~search_window
    7.type = int
    7.default = `40`
    7.desc = the window in which to search for a match for the rotation. The units are number of laser scan beams.

    8.name = ~max_error
    8.type = double
    8.default = `0.20`
    8.desc = the maximum distance, in meters, for correlating two points.

    9.name = ~max_iterations
    9.type = int
    9.default = `20`
    9.desc = the maximum number of algorithm iterations

    10.name = ~stop_condition
    10.type = double
    10.default = `0.01`
    10.desc = the stop condition, in meters, for the variance of the error
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
