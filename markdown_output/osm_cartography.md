## Overview

This experimental package was an early rapid-prototyping test bed for
the [geographic_info](https://index.ros.org/p/geographic_info) API for
Open Street Map.

It is no longer in active development, but some people have found it
useful, and it still has some level of support.

## Uniform Resource Locators

The location of XML map data in Open Street Map format is specified by
URL. The current implementation only supports these URL types:

- `file:*/full/path/to/local/map.xml`*

<!-- -->

- `package:*ros_package/data/map.osm`*

## ROS Interface

### osm_server node

ROS node that parses XML in Open Street Map format and returns
[geographic_msgs](https://index.ros.org/p/geographic_msgs) data to the
caller.

#### Services

- `get_geographic_map`
  ([geographic_msgs/srv/GetGeographicMap](https://docs.ros.org/en/rolling/p/geographic_msgs/srv/GetGeographicMap.html)):
  OSM map data from the requested URL

### viz_osm node

ROS node that requests Open Street Map
[geographic_msgs](https://index.ros.org/p/geographic_msgs) information
from the osm_server node,
publishing it as [rviz](https://index.ros.org/p/rviz) visualization
markers.

#### Published Topics

- `visualization_marker_array`
  ([visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html)):
  Markers for OSM map data from the requested URL.

#### Services Called

- `get_geographic_map`
  ([geographic_msgs/srv/GetGeographicMap](https://docs.ros.org/en/rolling/p/geographic_msgs/srv/GetGeographicMap.html)):
  OSM map data for the requested URL.

#### Parameters

- `map_url` (`string`): Uniform Resource Locator for XML map in OSM
  format.

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
`/local_map`: 

```
rosrun tf static_transform_publisher 622150 3362350 0 0 0 0 1 map local_map 100
```

 Then, launch the visualization
nodes: 

```
roslaunch osm_cartography viz_osm.launch url:=package://osm_cartography/tests/prc.osm
```

 Finally, run `rviz`, create a Marker
display and set the static frame to `local_map`. You'll probably need
to zoom out.

## Map Visualization

The goal is to translate OSM data for a region into
[rviz](https://index.ros.org/p/rviz) markers. Currently, the
viz_osm node only publishes
"interesting" information, like roads and buildings. For a full
implementation, that will need to be selectable.

![attachment:prc-osm-small.png](doc/prc-osm-small.png)

![attachment:prc-rviz-small.png](doc/prc-rviz-small.png)
