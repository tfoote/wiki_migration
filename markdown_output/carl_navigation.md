## About

The \`carl_navigation\` package contains nodes, configuration files, and
launch files for allowing carl to autonomously move its base. This also
includes support of layered costmaps, which allow obstacles to be
represented in a costmap that otherwise would not be detected by CARL.

\<\<MsgSrvDoc(carl_navigation)\>\>

## Nodes

```clearsilver
node.0 {
  name = furniture_layer
  desc = Layered costmap plugin for a global costmap that will display obstacle footprints for defined furniture pieces.  Localization footprints (i.e. the parts of the furniture that will be seen by a laser scan) are also calculated and sent to the localization map.
  sub {
    0.name = /furniture_layer/update_obstacles
    0.type = rail_ceiling/Obstacles
    0.desc = Incoming furniture obstacle information.
  }
  pub {
    0.name = /furniture_layer/obstacle_grid
    0.type = carl_navigation/BlockedCells
    0.desc = Furniture obstacle information denoted as blocked grid cells for purposes of localization.
  }
  pub {
    1.name = /furniture_layer/local_obstacle_grid
    1.type = carl_navigation/BlockedCells
    1.desc = Furniture obstacle information denoted as blocked grid cells for addition to a local costmap.
  }
  srv_called {
    0.name = furniture_tracker/get_all_poses
    0.type = rail_ceiling/GetAllObstacles
    0.desc = Get all of the currently known pose information for furniture obstacles.
  }
}
node.1 {
  name = furniture_layer_local
  desc = Layered costmap plugin for a local costmap that will display obstacle footprints for defined furniture pieces.  Localization footprints are not calculated with this node.
 sub {
    0.name = furnituer_layer/local_obstacle_grid
    0.type = carl_navigation::BlockedCells
    0.desc = Incoming furnituer obstacle information for the local map.
  }
}
node.2 {
  name = map_republisher
  desc = Combines a base static map with localization footprints from furniture obstacles calculated by the furniture_layer costmap plugin.
 sub {
    0.name = map_server/map
    0.type = nav_msgs/OccupancyGrid
    0.desc = The static map, used as the map base.
  }
  sub {
    1.name = furniture_layer/obstacle_grid
    1.type = carl_navigation/BlockedCells
    1.desc = Incoming obstacle localization footprints to add to the map.
  }
 pub {
    0.name = map
    0.type = nav_msgs/OccupancyGrid
    0.desc = The combined map.
  }
  pub {
    0.name = map_metadata
    0.type = nav_msgs/MapMetaData
    0.desc = Metadata for the combined map.
  }
  srv {
    0.name = static_map
    0.type = nav_msgs/GetMap
    0.desc = Service call to get the combined map.
  }
}
node.3 {
  name = rail_lab_location_server
  desc = Layered costmap plugin for a global costmap that will display obstacle footprints for defined furniture pieces.  Localization footprints (i.e. the parts of the furniture that will be seen by a laser scan) are also calculated and sent to the localization map.
  goal {
    0.name = move_carl
    0.type = carl_navigation/MoveCarlGoal
    0.desc = Automatic navigation to a pred-defined semantic location.
  }
  result {
    0.name = move_carl
    0.type = carl_navigation/MoveCarlResult
    0.desc = Result of automatic navigation to a pred-defined semantic location.
  }
  param {
    0.name = locations_config
    0.type = string
    0.desc = File path for location definitions.
    0.default = (path to carl_navigation)/config/rail_lab_locations.yaml
  }
}
```

## Installation

To install the carl_navigation package, you can install from source with
the following commands:

```
cd /(your catkin workspace)/src
git clone https://github.com/WPI-RAIL/carl_navigation.git
cd ..
catkin_make
```

## Startup

The carl_navigation package contains multiple launch files. One can
launch the navigation stack using:

```
roslaunch carl_navigation navigation.launch
``` One can see a visual representation of
navigation using rviz with:

```
roslaunch carl_navigation view_nav.launch
``` Finally, one can generate a map of the
environment using gmapping:

```
roslaunch carl_navigation gmapping.launch
``` The carl_navigation package also supports the
inclusion of defined obstacles that may not be visible to a laser scan.
These obstacles appear on a furniture layer costmap plugin defined in
this package. Packages such as [rail_ceiling](rail_ceiling) can provide
furniture definitions and tracking. One can launch the the navigation
stack configured to use these layered costmaps with:

```
roslaunch carl_navigation navigation_layered.launch
```

## Support

Please send bug reports to the
[github issue tracker](https://github.com/WPI-RAIL/carl_navigation/issues)
