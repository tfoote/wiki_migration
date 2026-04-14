/!\\ If you are using this package in your research work, please cite
these papers:

-   [Multi-robot Map Exploration Based on Multiple Rapidly-Exploring Randomized Trees](https://link.springer.com/article/10.1007/s42979-023-02193-2).

```{=html}
<!-- -->
```
-   [Autonomous robotic exploration based on multiple rapidly-exploring randomized trees](http://ieeexplore.ieee.org/document/8202319).

## Introduction

\"rrt_exploration\" is a ROS package that implements a multi-robot map
exploration algorithm for mobile robots. It is based on the
Rapidly-Exploring Random Tree (RRT) algorithm. It uses occupancy grids
as a map representation.The package has 5 different ROS nodes:

-   Global RRT frontier point detector node.
-   Local RRT frontier point detector node.
-   OpenCV-based frontier detector node.
-   Filter node.
-   Assigner node.

This is a playlist showing the package running on real robots and on
Gazebo simulation:

\<\<Youtube(abGyA3K1lzU?list=PLoGH52eUIHsc1B_xPLL6ogzYxrWy675kr)\>\>

## Package Requirements

The package has been tested on both ROS Kinetic and ROS Indigo, it
should work on other distributions like Jade. The following requirements
are needed before installing the package:

1- You should have installed a ROS distribution (indigo or later.
Recommended is either indigo or kinetic).

2- Created a workspace.

3- Installed the \"gmapping\" ROS package, you can do that by typing the
following command in the terminal:

```
sudo apt-get install ros-$ROS_DISTRO-gmapping
``` 4- Install ROS navigation stack. You can do
that with the following command:

```
sudo apt-get install ros-$ROS_DISTRO-navigation
``` 5- You should have Python 2.7. (it was not
tested on Python 3).

6-You should have/install the following python modules:

-OpenCV (cv2)

```
sudo apt-get install python-opencv
``` -Numpy

```
sudo apt-get install python-numpy
``` -Sklearn

```
sudo apt-get install python-scikits-learn
```

## Hardware Requirements

A mobile robot that can be used with the
[navigation stack](http://wiki.ros.org/navigation) (publishes /odom and
/tf. Receives velocity commands ..). The robot must also be equipped
with a laser scanner or any sensor that publishes laser scan message
(\<\<MsgLink(sensor_msgs/LaserScan Message)\>\>).

## Installation

Download the package and place it inside the /src folder in your
workspace. And then compile using catkin_make.

## Setting Up Your Robots

This package provides an exploration strategy for single or multiple
robots. However, for it to work, you should have set your robots ready
using the navigation stack. And each robot should run the
\"slam_gmapping\" node from the
[gmapping](http://wiki.ros.org/gmapping/) package.

Additionally, the robots must be set and prepared as follows.

Note: If you want to quickly run and test the package, you can try out
the
[rrt_exploration_tutorials](http://wiki.ros.org/rrt_exploration/tutorials)
package which provides Gazebo simulation for single and multiple robots,
you can use it directly with this package.

### Single Robot Setup

If you are using this package for exploration using a single robot, then
you will first need the following:

#### Setting up the navigation stack on the robot

The move_base_node node, which brings up the navigation stack on the
robot, must be running. This package (rrt_exploration) generates target
exploration goals, each robot must be able to receive these points and
move towards them. This is why the navigation stack is needed.
Additionally, each robot must have a global and local cost maps. All of
these are proivded from the \'\'\'move_base_node\'\'\'.

#### A mapping node

The robot should have a local map generated from the
[gmapping](http://wiki.ros.org/gmapping/) package.

### Multiple Robots Setup

#### Robots Network

For the multi-robot configuration, the package doesn\'t require special
network configuration, it simply works by having a single ROS master
(can be one of the robots). So on the other robots, the
\'\'\'ROS_MASTER_URI\'\'\' parameter should be pointing at the master\'s
address. For more information on setting up ROS on multiple machines,
follow [this](http://wiki.ros.org/ROS/NetworkSetup/) link.

#### Robot\'s frame names in tf

All robot\'s frames should be prefixed by its name. Naming of robots
starts from \"/robot_1\", \"/robot_2\", \"/robot_3\", .. and so on. So
for robot_1, the frames in the \'\'\'tf\'\'\' tree should look like
this:

![](https://github.com/hasauino/storage/blob/master/pictures/framesTf.png?raw=true)

#### Robot\'s node and topic names

All the nodes and topics running on a robot must also be prefixed by its
name. For robot 1, node names should look like: /robot_1/move_base_node,
/robot_1/slam_gmapping.

And topic names should be like: /robot_1/odom, /robot_1/map,
/robot_1/base_scan, ..etc.

#### Setting up the navigation stack on the robots

The move_base_node node, which brings up the navigation stack on the
robot, must be running. This package (rrt_exploration) generates target
exploration goals, each robot must be able to receive these points and
move towards them. This is why the navigation stack is needed.
Additionally, each robot must have a global and local cost maps. All of
these are proivded from the \'\'\'move_base_node\'\'\'.

#### A mapping node

Each robot should have a local map generated from the
[gmapping](http://wiki.ros.org/gmapping/) package.

#### A map merging node

There should be a node that merges all the local maps into one global
map. You can use the
[\"multirobot_map_merge\"](http://wiki.ros.org/multirobot_map_merge/)
package developed by Jiri Horner. /!\\ The \"multirobot_map_merge\" has
been updated, some users have reported problems getting correct map
merging. However, the old version still works fine. You can get the
forked old version [here](https://github.com/hasauino/m-explore)

## Nodes

There are 3 types of nodes; nodes for detecting frontier points in an
occupancy grid map, a node for filtering the detected points, and a node
for assigning the points to the robots. The following figure shows the
structure:

![](https://github.com/hasauino/storage/blob/master/pictures/fullSchematic.png?raw=true)

```clearsilver
name = global_rrt_frontier_detector
desc = The global_rrt_frontier_detector node takes an occupancy grid and finds frontier points (which are exploration targets) in it. It publishes the detected points so the filter node can process. In multi-robot configuration, it is intended to have only a single instance of this node running. <<BR>> Running additional instances of the global frontier detector can enhance the speed of frontier points detection, if needed.
sub {
  0.name = map
  0.type = nav_msgs/OccupancyGrid
  0.desc = Topic name is defined by the '''~map_topic''' parameter. It is the topic name on which the node will receive the map.

  1.name = clicked_point
  1.type = geometry_msgs/PointStamped
  1.desc = The global_rrt_frontier_detector node requires that the region to be explored is defined. This topic is where the node recieves five points that define the region. The first four points are four defining a square region to be explored, and the last point is the tree starting point. After publishing those five points on this topic, the RRT will start detecting frontier points. The five points are intended to be published from Rviz using {{https://github.com/hasauino/storage/blob/master/pictures/publishPointRviz_button.png?raw=true}} button.
}
pub {
  0.name = detected_points
  0.type = geometry_msgs/PointStamped Message
  0.desc = The topic on which the node publishes detected frontier points.

  1.name = ~shapes
  1.type = visualization_msgs/Marker Message
  1.desc = On this topic, the node publishes line shapes to visualize the RRT using Rviz.
}
param {
  0.name = ~map_topic
  0.type = string
  0.desc = This parameter defines the topic name on which the node will receive the map.
  0.default = "/robot_1/map"

  1.name = ~eta
  1.type = float
  1.desc = This parameter controls the growth rate of the RRT that is used in the detection of frontier points, the unit is in meters. This parameter should be set according to the map size, a very large value will cause the tree to grow faster and hence detect frontier points faster, but a large growth rate also implies that the tree will be missing small corners in the map.
  1.default = 0.5
}
``` ```clearsilver
name = local_rrt_frontier_detector
desc = This node is similar to the global_rrt_frontier_detector. However, it works differently, as the tree here keeps resetting every time a frontier point is detected. This node is intended to be run along side the global_rrt_frontier_detector node, it is responsible for fast detection of frontier points that lie in the close vicinity of the robot.<<BR>> In multi-robot configuration, each robot runs an instance of the local_rrt_frontier_detector. So for a team of 3 robots, there will be 4 nodes for detecting frontier points; 3 local detectors and 1 global detector. Running additional instances of the local frontier detector can enhance the speed of frontier points detection, if needed. <<BR>> All detectors will be publishing detected frontier points on the same topic ("/detected_points").
sub {
  0.name = map
  0.type = nav_msgs/OccupancyGrid
  0.desc = Topic name is defined by the '''~map_topic''' parameter. It is the topic name on which the node will receive the map.

  1.name = clicked_point
  1.type = geometry_msgs/PointStamped
  1.desc = The lobal_rrt_frontier_detector also subscribes to this topic similar to the global_rrt_frontier_detector.
}
pub {
  0.name = detected_points
  0.type = geometry_msgs/PointStamped Message
  0.desc = The topic on which the node publishes detected frontier points.

  1.name = ~shapes
  1.type = visualization_msgs/Marker Message
  1.desc = On this topic, the node publishes line shapes to visualize the RRT using Rviz.
}
param {
  0.name = ~/robot_1/base_link
  0.type = string
  0.desc = The frame attached to the robot. Every time the tree resets, it will start from the current robot location obtained from this frame.
  0.default = "/robot_1/base_link"

  1.name = ~map_topic
  1.type = string
  1.desc = This parameter defines the topic name on which the node will receive the map.
  1.default = "/robot_1/map"

  2.name = ~eta
  2.type = float
  2.desc = This parameter controls the growth rate of the RRT that is used in the detection of frontier points, the unit is in meters. This parameter should be set according to the map size, a very large value will cause the tree to grow faster and hence detect frontier points faster, but a large growth rate also implies that the tree will be missing small corners in the map.
  1.default = 0.5
}
```
```clearsilver
name = frontier_opencv_detector
desc = This node is another frontier detector, but it is not based on RRT. This node uses OpenCV tools to detect frontier points. It is intended to be run alone, and in multi-robot configuration only one instance should be run (running additional instances of this node does not make any difference).<<BR>>Originally this node was implemented for comparison against the RRT-based frontier detectors. Running this node along side the RRT detectors (local and global) may enhance the speed of frotiner points detection.<<BR>>Note: You can run any type and any number of detectors, all the detectors will be publishing on the same topic which the filter node (will be explained in the following section) is subscribing to. on the other hand, the filter will pass the filtered forntier points to the assigner in order to command the robots to explore these points.
sub {
  0.name = map
  0.type = nav_msgs/OccupancyGrid
  0.desc = Topic name is defined by the '''~map_topic''' parameter. It is the topic name on which the node will receive the map.

}
pub {
  0.name = detected_points
  0.type = geometry_msgs/PointStamped Message
  0.desc = The topic on which the node publishes detected frontier points.

  1.name = shapes
  1.type = visualization_msgs/Marker Message
  1.desc = On this topic, the node publishes detected points to be visualized using Rviz.
}
param {
  0.name = ~map_topic
  0.type = string
  0.desc = This parameter defines the topic name on which the node will receive the map.
  0.default = "/robot_1/map"

}
``` ```clearsilver
name = filter
desc = The filter nodes receives the detected frontier points from all the detectors, filters the points, and passes them to the assigner node to command the robots. Filtration includes the delection of old and invalid points, and it also dicards redundant points.
sub {
  0.name = map
  0.type = nav_msgs/OccupancyGrid
  0.desc = Topic name is defined by the '''~map_topic''' parameter. It is the topic name on which the node will receive the map.

  1.name = robot_x/move_base_node/global_costmap/costmap
  1.type = nav_msgs/OccupancyGrid
  1.desc = where x (in robot_x) refers to robot's number.<<BR>>The filter node subscribes for all the costmap topics of all the robots, the costmap is required therefore. Normally, costmaps should be published by the navigation stack (after bringing up the navigation stack on the robots, each robot will have a costmap). For example, if n_robots=2, the node will subscribe to: robot_1/move_base_node/global_costmap/costmap and robot_2/move_base_node/global_costmap/costmap. The costmaps are used to delete invalid points.<<BR>>Note: Namespaces of all the nodes corresponding to a robot should start with robot_x. Again x is the robot number.

  2.name = The goals topic
  2.type = geometry_msgs/PointStamped Message
  2.desc = Topic name is defined by the ~goals_topic parameter. It's the topic on which the filter node receives detected frontier points.
}
pub {
  0.name = frontiers
  0.type = visualization_msgs/Marker Message
  0.desc = The topic on which the filter node publishes the received frontier points for visualiztion on Rviz.

  1.name = centroids
  1.type = visualization_msgs/Marker Message
  1.desc = The topic on which the filter node publishes only the filtered frontier points for visualiztion on Rviz.

  2.name = filtered_points
  2.type = PointArray
  2.desc = All the filtered points are sent as an array of points to the assigner node on this topic.


}
param {
  0.name = ~map_topic
  0.type = string
  0.desc = This parameter defines the topic name on which the node will recieve the map. The map is used to know which points are no longer frontier points (old points).
  0.default = "/robot_1/map"

  1.name = ~costmap_clearing_threshold
  1.type = float
  1.desc = Any frontier point that has an occupancy value greater than this threshold will be considered invalid. The occupancy value is obtained from the costmap.
  1.default = 70.0

  2.name = ~info_radius
  2.type = float
  2.desc = The information radius used in calculating the information gain of frontier points.
  2.default = 1.0

  3.name = ~goals_topic
  3.type = string
  3.desc = defines the topic on which the node receives detcted frontier points.points.
  3.default =  "/detected_points"

  4.name = ~n_robots
  4.type = float
  4.desc = Number of robots.
  4.default =  1.0

  5.name = ~namespace
  5.type = string
  5.desc = namespace used in prefixing robot tf frame names and topic names . Normally, it's an empty string for the single robot case. However, in the multi-robot case, robot names (their tf frames and topic names) should be prefixed with a namespace (as described earlier). For example, if you have three robots with the following namespaces: "/robot_1","/robot_2", and "/robot_3", then you have to set this parameter to "/robot_"  
  5.default =  ''

  6.name = ~namespace_init_count
  6.type = float
  6.desc = Starting index for robot names, this index follows the namespace described above. It is used only for the multi-robot case (for the single robot case, this parameter is not used and can be neglected). In the multi-robot case, robot names have a namespace (you can set using the previously mentioned parameter), and followed by an index. If your set up has robot names that do not start with 1, then you can use this parameter according to you set up. Example: suppose you have two robots with the namespaces "/robot_4" and "/robot_5", then you have to set this parameter to 4. 
  6.default =  1.0

  7.name = ~rate
  7.type = float
  7.desc = node loop rate (in Hz).
  7.default =  100.0

}
```
```clearsilver
name = Assigner
desc = This node recieve target exploration goals, which are the filtered frontier points published by the filter node, and commands the robots accordingly. The assigner node commands the robots through the move_base_node. This is why you have bring up the navigation stack on your robots.


sub {
  0.name = map
  0.type = nav_msgs/OccupancyGrid
  0.desc = Topic name is defined by the '''~map_topic''' parameter.

  1.name = Filtered frontier points topic
  1.type = nav_msgs/OccupancyGrid
  1.desc = Topic name is defined by the ~frontiers_topic parameter

  2.name = The goals topic
  2.type = PointArray
  2.desc = Topic name is defined by the ~goals_topic parameter. It's the topic on which the filter node receives detected frontier points.
}

param {
  0.name = ~map_topic
  0.type = string
  0.desc = This parameter defines the topic name on which the node will recieve the map. In the single robot case, this topic should be set to the map topic of the robot. In the multi-robot case, this topic must be set to global merged map.
  0.default = "/robot_1/map"

  1.name = ~info_radius
  1.type = float
  1.desc = The information radius used in calculating the information gain of frontier points.
  1.default = 1.0

  2.name = ~info_multiplier
  2.type = float
  2.desc = The unit is meter. This parameter is used to give importance to information gain of a frontier point over the cost (expected travel distance to a frontier point).
  2.default = 3.0

  3.name = ~hysteresis_radius
  3.type = float
  3.desc = The unit is meter. This parameter defines the hysteresis radius.
  3.default =  3.0

  4.name = ~hysteresis_gain
  4.type = float
  4.desc = The unit is meter. This parameter defines the hysteresis gain.
  4.default =  2.0

  5.name = ~frontiers_topic
  5.type = string
  5.desc = The topic on which the assigner node receives filtered frontier points.
  5.default =  "/filtered_points"

  6.name = ~n_robots
  6.type = float
  6.desc = Number of robots.
  6.default =  1.0

  7.name = ~namespace
  7.type = string
  7.desc = namespace used in prefixing robot tf frame names and topic names .
  7.default =  ''

  8.name = ~namespace_init_count
  8.type = float
  8.desc = Starting index for robot names.
  8.default =  1.0


  9.name = ~delay_after_assignement
  9.type = float
  9.desc = The unit is seconds. It defines the amount of delay after each robot assignment.
  9.default =  0.5

  10.name = ~rate
  10.type = float
  10.desc = node loop rate (in Hz).
  10.default =  100.0

  10.name = ~global_frame
  10.type = string
  10.desc = frame name used as the global frame. In the single robot, it is the same as the "map_topic" parameter. In the multi-robot case, it is the frame name that corresponds to the global frame.
  10.default =  "/map"


}
```

## Tutorials

Tutorials on how to use the package are listed
[here](http://wiki.ros.org/rrt_exploration/Tutorials).

## Feedback

To report a bug, or suggest an enhancement, please create a Github issue
[here](https://github.com/hasauino/rrt_exploration/issues/new).

If you have a question, please post it on
[ROS answers](http://answers.ros.org/questions/scope:all/sort:activity-desc/tags:rrt_exploration/page:1/),
make sure your question is tagged by \'\'\'rrt_exploration\'\'\' so I
get notified.

## Acknowledgements & Citation

This package was written during my master\'s thesis at the American
University of Sharjah. My thesis advisor is Dr.
[Shayok Mukhopadhyay](https://sites.google.com/site/shayok/Home).

This work has been published on IROS. If you are using this package,
please cite our [paper](http://ieeexplore.ieee.org/document/8202319).

```
sudo apt-get install ros-$ROS_DISTRO-navigation
```0 Thesis title:
\"[Multi-Robot Map Exploration Based on Multiple Rapidly-Exploring Randomized Trees](https://dspace.aus.edu:8443/xmlui/handle/11073/8857)\"
