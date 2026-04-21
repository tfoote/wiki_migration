## Nodes

### stdr_server_node

The `stdr_server_node` node implements the synchronization and
coordination functionalities of `stdr_simulator`. It is used to serve
the static map, which represents the simulated environment and keeps
track of active robots.

#### Action API (Internal Usage)

The `stdr_server_node` node provides several action server
implementations used for robot handling and coordination.

##### Action Topics

`spawn_robot`
([stdr_msgs/SpawnRobotAction](http://docs.ros.org/api/stdr_msgs/html/action/SpawnRobot.html))
Action to spawn a new robot. Called either from [STDR GUI](stdr_gui) or
from [robot_handler](stdr_robot#robot_handler) node. `delete_robot`
([stdr_msgs/DeleteRobotAction](http://docs.ros.org/api/stdr_msgs/html/action/DeleteRobot.html))
Action to handle robot deletion. Called either from [STDR GUI](stdr_gui)
or from [robot_handler](stdr_robot#robot_handler) node.
`register_robot`
([stdr_msgs/RegisterRobotAction](http://docs.ros.org/api/stdr_msgs/html/action/RegisterRobot.html))
Action to register a newly spawned robot. Called from `stdr_robot`
nodelet itself, serves synchronization purposes.

```clearsilver
pub {
  0.name = map
  0.type = nav_msgs/OccupancyGrid
  0.desc = The world to be used at simulation, loaded as a map. Delegated to robots and GUIs, using a latched publisher.

  1.name = map_metadata
  1.type = nav_msgs/MapMetaData
  1.desc = Publishes the map metadata.

  2.name = active_robots
  2.type = stdr_msgs/RobotIndexedVectorMsg
  2.desc = Publishes active robots when a deletion or an addition takes place, using a latched topic.
}

srv {
  0.name = load_static_map
  0.type = stdr_msgs/LoadMap
  0.desc = Allows an external user to load a map, providing the map filename.

  1.name = load_static_map_external
  1.type = stdr_msgs/LoadExternalMap
  1.desc = Allows an external user to load a map, providing an <<MsgLink(nav_msgs/OccupancyGrid)>>. Used by [[stdr_server#map_loader_node|map_loader_node]], see below.
}

srv_called {
  0.name = robot_manager/load_nodelet
  0.type = nodelet/NodeletLoad
  0.desc = Called to load a new robot.

  1.name = robot_manager/unload_nodelet
  1.type = nodelet/NodeletUnload
  1.desc = Called to unload/delete a robot.
}

prov_tf {
  0.from = world
  0.to = map
  0.desc = represents the map origin described in map description file. See [[map_server#YAML_format|map_server]] package for details. 

  1.from = world
  1.to = map_static
  1.desc = frame fixed to bottom left corner of the static map, regardless of the map origin. Useful for geometric calculations.
}
```

#### Command-Line Usage

`stdr_server_node` can run without any command-line arguments and
simply waits until someone calls either `load_static_map` or
`load_static_map_external` service. There is an option to run
`stdr_server_node` passing an image file to load as the static map or
you can include it to a launch file using the `args` option.
```
$ rosrun stdr_server stdr_server_node <map_file.yaml>
```

### map_loader_node

The `map_loader_node` node uses [map_server](map_server)'s
`image_loader` library to load an map image from a file, fill a
<<MsgLink(nav_msgs/OccupancyGrid)>> message, call
`load_static_map_external` service and load it to the simulator. The
loading functionality is also provided in `map_loader` library and can
be used by other packages.

#### Command-Line Usage

```
$ rosrun stdr_server load_map <map_file.yaml>
```

## Tutorials

For tutorials see [stdr_simulator/Tutorials](stdr_simulator/Tutorials).
