![\|width=\"333\",height=\"200\"](attachment:Logo-white-medium.jpg)

## Description

This package includes an updated version of the standard
[navfn](http://wiki.ros.org/navfn) global planner in the standard
ROS_Navigation. The updated function is, that the global planner can now
find a nearest goal if the desired destination is in an obstacle. First
have a look at this documentation: [navfn](http://wiki.ros.org/navfn).

## Functionality

Instead of aborting the path calculation if the goal is in an obstacle,
now the planner doesn\'t abort. It calculates the shortest (weighted)
path to the goal using the Dijkstra algorithm. The points on the costmap
which are obstacles are rated as high as possible.

After calculating the path it is checked whether the goal is in an
obstacle. If that is the case, the path is traversed backwards from the
goal until a point is found which is not part of an obstacle. Otherwise
the path is returned as it is.

![\|width=\"501\",height=\"348\"](attachment:asr_navfn.png)

At this picture you see a examle path calculation. The goal (red dot) is
out of the reachable area of the global map. So the algorithm go
backwart to the naearest reachable point.

## Usage

Clone this package to your catkin_workspace and compile it.

To use the asr_navfn set the \"base_global_planner\" parameter in the
move_base package (look at
[move_base parameters](http://wiki.ros.org/move_base)) to
\"asr_navfn/NavfnROS\". You can set it as parameter (\"param\") by start
the move_base node in an launch file:

```
<param name="base_global_planner" value="asr_navfn/NavfnROS"/>
``` An example can be found in
[asr_mild_navigation](asr_mild_navigation) in file
\"launch/navigation.launch\".

## ROS Nodes

### Published Topics

\<name\>/plan (
[nav_msgs/Path](http://docs.ros.org/api/nav_msgs/html/msg/Path.html))

The last plan computed by asr_navfn, published everytime the planner
computes a new path, and used primarily for visualization purposes.

### Parameters

The same parameters like in [navfn](http://wiki.ros.org/navfn).
