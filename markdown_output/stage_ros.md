## Nodes

### stageros

The `stageros` node wraps the Stage 2-D multi-robot simulator, via
libstage. Stage simulates a world as defined in a `.world` file. This
file tells stage everything about the world, from obstacles (usually
represented via a bitmap to be used as a kind of background), to robots
and other objects.

This node only exposes a subset of Stage's functionality via ROS.
Specifically, it finds the Stage models of type laser, camera and
position, and maps these models to the ROS topics given below. If at
least one laser/camera and position model are not found, stageros exits.

Usage



```
rosrun stage_ros stageros [-g runs headless] <world> [standard ROS args]
```

 Parameters:

- world : The Stage .world file to load.
- -g : If set, this option will run stage as "headless," no GUI will
  be displayed.

#### World syntax

The .world file syntax is documented in the
[Stage manual](http://rtv.github.io/Stage/modules.html). stageros only
exposes models created by a subset of the .world file syntax,
specifically **laser**, **position** and **camera** models. For
examples, see the `world` directory in the `stage` and `stage_ros`
packages.

#### Subscribed topics

If there is only one position model defined in the world file, all of
these topics appear at the top namespace. However, if more than 1
position models exist, these topics are pushed down into their own
namespaces, by prefixing the topics with `robot_<i>/` , e.g.,
`robot_0/cmd_vel` etc.

`cmd_vel`
[geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)
velocity commands to drive the position model of the robot

#### Published topics

If there is only one position model defined in the world file, all of
these topics appear at the top namespace. However, if more than 1
position models exist, these topics are pushed down into their own
namespaces, by prefixing the topics with `robot_<i>/` , e.g.,
`robot_0/cmd_vel` etc.

`odom`
([nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html))
odometry data from the position model. `base_scan`
([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html))
scans from the laser model `base_pose_ground_truth`
([nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html))
ground truth pose `image`
([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html))
visual camera image `depth`
([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html))
depth camera image `camera_info`
([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html))
camera calibration info

##### odom vs. base_pose_ground_truth

The `odom` topic gives simulated odometry, which is affected by
settings in the .world file, which can change its origin and noise model
(the transforms mentioned below use the same data); see the
[Stage documentation](http://rtv.github.io/Stage/group__model__position.html)
for details on changing this behavior. The `base_pose_ground_truth`
topic always provides a perfect, globally referenced pose for the robot
in the simulation, independent of .world file settings. The
`base_pose_ground_truth` data is intended for testing purposes; it
should not be used in robot control loops (because it's unrealistic).

#### Parameters

`base_watchdog_timeout` (default: 0.2) time (in seconds) after
receiving the last command on `cmd_vel` before stopping a position
model `is_depth_canonical` (default: true) whether depth image should
use canonical (32FC1) or OpenNI (16UC1) representation

#### tf transforms provided

`base_link` \&rarr; `base_laser` transform from robot base to
attached laser `base_footprint` \&rarr; `base_link` identity
transform `odom` \&rarr; `base_footprint` transform from odometric
origin to base `base_link` \&rarr; `camera` transform from robot
base to attached camera

## Using Stage controllers

Stage supports the use of "controllers," which are chunks of code that
control simulated robots from inside the simulator, instead of being on
the other end of a ROS connection. There are some situations in which it
can be advantageous to use Stage controllers. For a discussion of when
and how to use Stage controllers, see
[this tutorial](https://index.ros.org/p/stage).
