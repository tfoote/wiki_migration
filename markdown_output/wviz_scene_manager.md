## Overview

When observing or controlling a robot remotely over high latency
connections, it is important to compress and limit the amount of data
being sent without sacrificing the amount of information being provided
to the client. Marker topics are published by many nodes in ROS and can
be large and frequently published. wviz_scene_manager provides two
services, add_marker and remove_marker, that allow clients to specify
which markers are of interest. Once added the wviz_scene_manager will
subscribe to the marker and aggregate incoming messages into a scene
composed of markers. Whenever the scene changes it is published as a
whole.

## Running the wviz_scene_manager node

```
$ rosrun wviz_scene_manager wviz_scene_manager
```

## Nodes

```clearsilver
pub {
  0.name= scene
  0.type= wviz_scene_manager/VisualizationScene
  0.desc= Contains an array of markers of type visualization_msgs/Marker that make up the scene
}
srv{
  0.name= ~<name>/add_marker
  0.type= wviz_scene_manager/AddMarker
  0.desc= Allows a client to add a marker topic to the scene
  1.name= ~<name>/remove_marker
  1.type= wviz_scene_manager/RemoveMarker
  1.desc= Allows a client to remove a marker topic from the scene
}
```
