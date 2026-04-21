Please check the for common problems, or open an
[issue](https://github.com/paulbovbel/frontier_exploration/issues) if
still unsolved.

## Overview

The best way to try `frontier_exploration` is using the demo provided
in [husky_navigation](husky_navigation), see the
[demo tutorial](husky_navigation/Tutorials/Husky Frontier Exploration Demo).

### Functionality

The `frontier_exploration` package provides a [costmap_2d](costmap_2d)
layer plugin `BoundedExploreLayer`, and [actionlib](actionlib)
client/server nodes `explore_client` and `explore_server`.

The provided nodes can be used to demo the functionality of the costmap
layer by executing a frontier exploration task bounded by a user-defined
polygon area. Layer `BoundedExploreLayer` can certainly be used for
more complex exploration tasks, functionality is exposed through two
[Services](Services): `UpdatePolygonBoundary` and `GetNextFrontier`.

[Youtube](https://www.youtube.com/watch?v=3W1ufJ7rpCA&rel=0)

To run this demo on your host, see
[frontier_exploration#For_running_a_demo](frontier_exploration#For_running_a_demo)
section.

Also, this video is an example of `frontier_exploration` integrated
with [Turtlebot](turtlebot)
([turtlebot_samples package is used](https://github.com/130s/turtlebot_samples)).

[Youtube](https://www.youtube.com/watch?v=WMcQRpBpN1s&rel=0)

### Requirements

Frontier exploration using this package requires a real or simulated
robot configuration that provides the following functionality:

1\. Laser scanner or similar sensor that can clear space and mark
obstacles. 2. Properly configured [navigation](navigation) stack that
can accept action goals to [move_base](move_base). 3. (Optional) Global
`/map` provided by [map_server](map_server), [gmapping](gmapping), or
the global costmap from [move_base](move_base)

## Usage

### For running a demo

Using a pre-existing robot and config, you can run a demo and see how
this package works.

1\. Install dependency.



```
sudo apt-get install ros-$ROS_DISTRO-frontier-exploration ros-$ROS_DISTRO-navigation-stage
```



2\. Run the necessary nodes one-by-one from separate terminal:



```
roslaunch navigation_stage move_base_gmapping_5cm.launch

roslaunch navigation_stage move_base.xml

roslaunch frontier_exploration global_map.launch
```



RViz pops up, then a demo robot appears around the center in a map.

3\. Open a `Marker plugin` on RViz (RViz plugins can be chosen in a
popup window that you can open by "Add" button).

4\. Pull down "`Displays \--> Marker \--> Marker Topic`" menu then
select "`exploration_polygon_marker`" topic.

5\. On the map on RViz, think of a region that you like the robot to
explore.

6\. Click "`Publish Point`" at the top of RViz.

7\. Click **a single corner** of `n` corners of the region (n=4 if
your region is square/rectangular, to be pedantic)．

8\. Repeat step 6 and 7 above for n times. After that you'll see a
polygon with n corners.

9\. Do the step 6 once again, then this time click anywhere within the
polygon.

At this point the demo robot should start moving
[as the video above](https://youtu.be/3W1ufJ7rpCA).

### For developers

If you just want to start taking advantage of the functionality of this
package,
[this tutorial in husky_navigation package](husky_navigation/Tutorials/Husky Frontier Exploration Demo)
helps.

If you like to understand a little more in depth, generally, when
launched `explore_server` will spin until it receives an exploration
goal. To submit a goal:

1\. Use `explore_client` and RViz - create a marker display in Rviz
for the `exploration_polygon_marker` topic, and use the "Click
Point" tool from the toolbar to mark the exploration boundary. Watch
the ROS console for feedback regarding your selected boundary.

2\. Submit a goal to the server with your own node via an
[actionlib](actionlib) SimpleActionClient.

The exploration goal contains an initial point to start exploration, and
a polygonal boundary to limit the exploration scope. To run an unbounded
exploration task, simply leave the boundary blank.

Once the server receives a goal, it will create the initial exploration
map, start processing sensor/costmap data, and issuing `move_base`
action goals. By default, the exploration task will explore all areas
within boundary (whether previously visited or not). Sample launch files
for several use cases are provided below.

#### Exploration without /map data

When running the action server/client without a global `/map`
information source, enable the `resize_to_boundary` parameter to
dynamically resize the map based on the action goal's polygon boundary.
Error messages thrown up by `costmap_2d` regarding the sensor being
outside of map bounds will occur when the robot is traveling outside the
exploration boundary. These can be safely ignored, and could be
suppressed using `rosconsole` configuration files.

If not using `resize_to_boundary` (e.g. running unbounded
exploration), make sure the costmap is configured with a large enough
height/width.

Sample launch file:
[no_global_map.launch](https://github.com/paulbovbel/frontier_exploration/blob/hydro-devel/launch/no_global_map.launch)

#### Exploration with /map data

When running the action server/client with a global `/map` information
source (either from `map_server` or `gmapping`), the exploration
costmap will match size/resolution to the external map source map loaded
by the static layer, so it is important to disable the
`resize_to_boundary` parameter and that the `global_frame` of the
exploration costmap matches that of the external /map.

When exploring with `gmapping`, you must also disable
`explore_clear_space` to prevent the node from re-exploring known
areas.

Sample launch file:
[global_map.launch](https://github.com/paulbovbel/frontier_exploration/blob/hydro-devel/launch/global_map.launch)

## Provided Components



```clearsilver
name = explore_client
desc = The `explore_client` node listens to points published by Rviz and builds an `ExploreTask` action goal to send to `explore_server`.
act_called {
  0.name= explore_server
  0.type= frontier_exploration/ExploreTask
  0.desc= Client for exploration goals to `explore_server`.
}
sub {
  0.name = /clicked_point
  0.type = geometry_msgs/PointStamped
  0.desc = Clicked points from [[rviz]] tool.
}
pub{
  0.name = exploration_polygon_marker
  0.type = visualization_msgs/Marker
  0.desc = Boundary visualization via clicked points.
}
```



### explore_server

The `explore_server` node executes exploration actions for any
connected clients. It uses a [costmap_2d](costmap_2d) object to keep
track of the exploration progress, and creates movement goals for
[move_base](move_base) as necessary.

#### Actions Provided



```clearsilver
act_called {
  no_header= True
  0.name= explore_server
  0.type= frontier_exploration/ExploreTask
  0.desc= Server for incoming exploration task requests
}
```

 

```clearsilver
act_called {
  0.name= move_base
  0.type= move_base_msgs/MoveBaseAction
  0.desc= Client for movement goals to `move_base`.
}
srv_called {
  0.name= ~explore_costmap/explore_boundary/update_boundary_polygon
  0.type= frontier_exploration/UpdateBoundaryPolygon
  0.desc= (Internal Service from Costmap) Set boundary for exploration task.
  1.name= ~explore_costmap/explore_boundary/get_next_frontier
  1.type= frontier_exploration/GetNextFrontier
  1.desc= (Internal Service from Costmap) Get the pose of the next frontier to explore.
}
param {
  0.name = ~explore_costmap
  0.type = plugins
  0.desc = Configuration for internal costmap layers, expected to include `BoundedExploreLayer`.
  1.name = ~frequency
  1.type = float
  1.desc = Frequency with which to reprocess the costmap for next frontier goal. If `0.0`, only ask for new frontier when last frontier was reached via `move_base`. Higher frequencies submit `move_base` goals more often and create 'smoother' exploration.
  1.default = 0.0
  2.name = ~goal_aliasing
  2.type = float
  2.default = 0.1
  2.desc = When `frequency` > `0.0`, `~goal_aliasing` is the required distance delta between the last goal and a new goal, before the new goal is submitted to `move_base`. It is safe to set to anywhere within `sensor_range/2` > `~goal_aliasing` > `0.0`, and this parameter will reduce the amount of redundant goals sent during 'smooth' exploration.
}
```





```clearsilver
name = BoundedExploreLayer
desc = The `frontier_exploration::BoundedExploreLayer` layer is a costmap_2d plugin that implements several functions required to execute a frontier exploration task.
srv {
  0.name= ~update_boundary_polygon
  0.type= frontier_exploration/UpdateBoundaryPolygon
  0.desc= Set boundary for exploration task.
  1.name= ~get_next_frontier
  1.type= frontier_exploration/GetNextFrontier
  1.desc= Get the pose of the next frontier to explore.
}
param {
  0.name = ~resize_to_boundary
  0.type = bool
  0.desc = When receiving a polygonal boundary via `~update_boundary_polygon`, resize the layer's parent costmap to the boundary extrema.
  0.default = false
  1.name = ~frontier_travel_point
  1.type = string
  1.desc = When outputting `pose` of next frontier via `~get_next_frontier`, define the geometric property of frontier to output as `pose.position`. Available: `closest` point to robot, `middle` point of frontier, `centroid` (cartesian average) of all frontier points.
  1.default = closest
  2.name = ~explore_clear_space
  2.type = bool
  2.desc = Configure whether the exploration task should explore all clear space (true), or just unknown space (false).
  2.default = true
}
pub {
  0.name = ~frontiers
  0.type = sensor_msgs/PointCloud2
  0.desc = Pointcloud `pcl::Pointcloud<pcl::PointXYZI>` marking all frontiers detected when service `~get_next_frontier` is called, with the selected frontier marked using a higher intensity point.
}
```


