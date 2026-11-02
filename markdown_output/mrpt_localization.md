## Overview

This package uses dynamic or static (MRPT or ROS) maps for
self-localization. If an MRPT format is used the node publishes the map
for debugging and interface reasons in ROS standard format.

MRPT particle filtering allows for localization with:

- A number of different
  [algorithms](http://www.mrpt.org/tutorials/programming/statistics-and-bayes-filtering/particle_filter_algorithms/).
- **Different map kinds:** Occupancy grid maps (as images or in MRPT
  binary format), point clouds, beacon map (for range-only sensors). At
  present, these combinations are exposed to ROS:
- Map: **occupancy grid**, Sensor: anyone capable of generating a point
  cloud (see
  [mrpt_local_obstacles](http://wiki.ros.org/mrpt_local_obstacles)).
  Several occupancy grids, each at a different height, to be used for
  laser scans at the corresponding robot height.
- Map: **beacons** at predefined 3D positions, Sensor: **range-only**.
  For *Range-Only (RO) Localization*.
- Multiple simultaneous sensors: The combinations above can be used
  together and their **probabilistic information automatically fused**
  together.

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     <tablewidth="818px" tableheight="419px"> ![attachment:pioneer.jpg](doc/pioneer.jpg) *This Figure shows the mprt pf-localization working together with ROS. RViz can be used to visualize the data and to set an initial pose.*    
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

[Youtube](https://www.youtube.com/watch?v=b5glQhT2Zac)

## Related papers

- **Optimal particle filtering algorithm**
- J.L. Blanco, J. Gonzalez-Jimenez, J.A. Fernandez-Madrigal, *"Optimal
  Filtering for Non-Parametric Observation Models: Applications to
  Localization and SLAM"*, The International Journal of Robotics
  Research (IJRR), vol. 29, no. 14, 2010.
  ([PDF](http://ingmec.ual.es/~jlblanco/papers/blanco2010ofn_IJRR.pdf))

<!-- -->

- **Range-Only localization**
- J. Gonzalez-Jimenez, J.L. Blanco, C. Galindo, A. Ortiz-de-Galisteo,
  J.A. Fernandez-Madrigal, F.A. Moreno, J. Martinez, *"Mobile Robot
  Localization based on Ultra-Wide-Band Ranging: A Particle Filter
  Approach"*, Robotics and Autonomous Systems, vol. 57, no. 5, pp.
  496\--507, 2009.
  ([PDF](http://ingmec.ual.es/~jlblanco/papers/gonzalez2008mrl.pdf))

## Demos

### LIDAR localization with a gridmap

Run: 

```
roslaunch mrpt_localization demo.launch
```

 to start:

- a rosbag including tf and laser scan data,
- the mrpt localization with a mrpt map
- RViz for visualization

### Range-only (RO) localization with a set of fixed, known radio beacons

Run: 

```
roslaunch mrpt_localization demo_ro.launch
```

 to start:

- a dataset (rawlog format) including RO and odometry observations,
- the mrpt localization with known beacon locations, and
- RViz for visualization

## Tutorial

We added also gazebo tutorial, but you have to get sure to have
gazebo_ros, teleop_twist_keyboard and some other pkg installed. The
tutorial shows a pioneer 3DX robot unter the namespace r1.

- **roslaunch mrpt_tutorials r1_gazebo_gh25.launch**\
  it should start gazebo with a simple environment. If you have problems
  there check your gazeo installation and try some native gazebo_ros
  launches like *roslaunch gazebo_ros empty_world.launch*
- **roslaunch mrpt_tutorials r1_localization.launch**\
  it will start the mrpt pf-localization. You can use additional
  arguments to define a the mrpt ini_file, map_file or laser scan topic.
  Have a look at the *r1_localization.launch* file
- **roslaunch mrpt_tutorials r1_rviz.launch**\
  it will start RViz. Using the 2D pose Estimation tool, you can reset
  the robot pose. (Since the robot lies within the namespace r1 you have
  to check the Panel->Tool Propertiers to publish the robot pose under
  */r1/initialpose*)
- **roslaunch mrpt_tutorials r1_teleop.launch**\
  Now you can control the robot with the keyboard. The teleop publishes
  Twist msgs on r1/cmd_vel (
  [teleop_twist_keyboard](http://wiki.ros.org/teleop_twist_keyboard)
  must be installed!!)

## Nodes

### mrpt_localization

The `mrpt_localization` node wraps MRPT particle-filter localization
algorithms through a ROS interface. See demo launch-file and tutorials
above.

Example usage:



```
roslaunch mrpt_localization demo.launch
```



#### Published Topics

- `map`
  ([nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)):
  Only if param `map_file` is NOT empty, the loaded map will be
  published here (Latched)
- `map_metadata` (`nav_msgs::MapMetaData`): Only if param `map_file`
  is NOT empty, the loaded map will be published here (Latched)
- `particlecloud`
  ([geometry_msgs/msg/PoseArray](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseArray.html)):
  The hypotheses of the particle filter. Its mean is published via a tf
  transformation.

#### Services

- `static_map`
  ([nav_msgs/srv/GetMap](https://docs.ros.org/en/rolling/p/nav_msgs/srv/GetMap.html)):
  You can retrieve the loaded map here

#### Parameters

- `~ini_file` (`string`, default: `"pf-localization.ini"`): Path to
  a configuration file containing all the particle-filter parameters
  required by MRPT pf-localization. It defines the kind and number of
  metric maps and many important parameters of probabilistic observation
  models. See commented example files in
  <https://github.com/jlblancoc/mrpt/tree/master/share/mrpt/config_files/pf-localization>
- `~map_file` (`string`, default: `(none)`): Path to an MRPT map file in
  either `.simplemap` or `.gridmap` formats. If none is provided,
  the node \*will do a blocking call\* to the service
  GetMap("static_map") to retrieve an occupancy grid map from a static
  map server like [map_server](https://index.ros.org/p/map_server) or
  [mrpt_map](https://index.ros.org/p/mrpt_map).
- `~tf_prefix` (`string`, default: `""`): Prefix for TF frame names
  (e.g. "r1", "robot2", or none if only using one robot)
- `~global_frame_id` (`string`, default: `"map"`): TF frame name for the
  global reference map (typically, a static map)
- `~odom_frame_id` (`string`, default: `"odom"`): TF frame name for
  odometry
- `~base_frame_id` (`string`, default: `"base_link"`): TF frame name for
  the robot
- `~sensor_sources` (`string`, default: `"scan,scan1,scan2"`): List of
  topics to subscribe to for sensory data (split with ",")

#### Provided tf Transforms

- <value of global_frame_id> (typ: `map`) → <value of
  odom_frame_id> (typ: `odom`): transform from global map to odometry
  origin
