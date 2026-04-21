## Overview

This experimental package was an early rapid-prototyping test bed for
the [geographic_info](geographic_info) API for Open Street Map.

It is no longer in active development, but some people have found it
useful, and it still has some level of support.

## Uniform Resource Locators

The location of XML map data in Open Street Map format is specified by
URL. The current implementation only supports these URL types:

-   `file:*/full/path/to/local/map.xml`*

```{=html}
<!-- -->
```
-   `package:*ros_package/data/map.osm`*

## ROS Interface

```clearsilver
node.0 {
 name = osm_server node
 desc = ROS node that parses XML in Open Street Map format and returns [[geographic_msgs]] data to the caller. 
 srv {
  0.name= get_geographic_map
  0.type= geographic_msgs/GetGeographicMap
  0.desc= OSM map data from the requested URL
}
}
```

```clearsilver
node.0 {
 name = viz_osm node
 desc = ROS node that requests Open Street Map [[geographic_msgs]] information from the [[#osm_server|osm_server]] node, publishing it as [[rviz]] visualization markers. 
 pub {
  0.name= visualization_marker_array
  0.type= visualization_msgs/MarkerArray
  0.desc= Markers for OSM map data from the requested URL.
}
 srv_called {
  0.name= get_geographic_map
  0.type= geographic_msgs/GetGeographicMap
  0.desc= OSM map data for the requested URL.
}
 param {
  0.name= map_url
  0.type= string
  0.desc= Uniform Resource Locator for XML map in OSM format.
}
}
```

### viz_osm Launch File

Runs the osm_cartography nodes, passing the URL of a local file
containing the map.

Because UTM map coordinates are generally too large for the float
representation used by `rviz`, it will probably be necessary to
publish a transform to some nearby Cartesian coordinate frame within
about 10 km, and use that for visualization. You can name that as you
like, these examples call it `map_local`.

#### Arguments

`url (string)` Uniform Resource Locator for XML map in OSM format.

#### Example

In one terminal window, create a transform from the `/map` frame to
`/local_map`: ```
rosrun tf static_transform_publisher 622150 3362350 0 0 0 0 1 map local_map 100
``` Then, launch the visualization
nodes: ```
roslaunch osm_cartography viz_osm.launch url:=package://osm_cartography/tests/prc.osm
``` Finally, run `rviz`, create a Marker
display and set the static frame to `local_map`. You'll probably need
to zoom out.

## Map Visualization

The goal is to translate OSM data for a region into [rviz](rviz)
markers. Currently, the [viz_osm](#viz_osm) node only publishes
"interesting" information, like roads and buildings. For a full
implementation, that will need to be selectable.

![](attachment:prc-osm-small.png)

![](attachment:prc-rviz-small.png)
