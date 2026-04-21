ROS node for the "multivehicle simulator" framework. ******Under
development!\*\*******

## Installing

-   From the repositories: ```
sudo apt-get install ros-$ROS_DISTRO-mvsim
```

```{=html}
<!-- -->
```
-   From sources: Clone into your catkin workspace and build as usual.

## Nodes

### mvsim_node

The `mvsim_node` node wraps Multi-Vehicle Simulator library
(libmvsim). It loads a `world` file and exposes vehicles, sensors and
wheel forces via ROS.

Usage: See parameters below. You can start running the provided demo
files, for example:

```
roslaunch mvsim mvsim_demo_2robots.launch
```

#### World files

(Write me!)

#### Subscribed topics

If there is only one vehicle defined in the world file, all of these
topics appear at the top namespace. However, if more than one vehicle
exist, topics are placed into their own namespaces like `veh<i>/` ,
e.g., `veh0/cmd_vel` etc.

`cmd_vel` <<MsgLink(geometry_msgs/Twist)>> velocity commands to
drive the position model of the robot

#### Published topics

If there is only one vehicle defined in the world file, all of these
topics appear at the top namespace. However, if more than one vehicle
exist, topics are placed into their own namespaces like `veh<i>/` ,
e.g., `veh0/odom` etc.

`odom` (<<MsgLink(nav_msgs/Odometry)>>) odometry data from the
vehicle. `base_pose_ground_truth` (<<MsgLink(nav_msgs/Odometry)>>)
ground truth pose `<LASER_SENSOR_NAME>`
(<<MsgLink(sensor_msgs/LaserScan)>>) scans from simulated 2D laser
scanners (name matches that provided in the world file)

The `odom` topic gives simulated odometry, while
`base_pose_ground_truth` always provides a perfect, globally
referenced pose.

#### Parameters

`base_watchdog_timeout` (default: 0.2) time (in seconds) after
receiving the last command on `cmd_vel` before stopping a position
model

#### tf transforms provided

`base_link` &rarr; `base_<LASER_SENSOR_NAME>` transform from
robot base to attached laser(s) `base_footprint` &rarr; `base_link`
identity transform `odom` &rarr; `base_footprint` transform from
odometric origin to base
