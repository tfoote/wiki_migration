## Overview

This experimental package is in an early rapid-prototyping phase. The
initial goal is to demonstrate the feasibility of the
[geographic_info](https://index.ros.org/p/geographic_info) API for
working with Open Street Map information.

These interfaces are still changing rapidly, nothing is stable yet.

## ROS Nodes

### plan_route

ROS node that reads route network messages, and provides a route
planning service.

#### Subscribed Topics

- `route_network`
  ([geographic_msgs/msg/RouteNetwork](https://docs.ros.org/en/rolling/p/geographic_msgs/msg/RouteNetwork.html)):
  Graph of drivable routes.

#### Services

- `get_route_plan`
  ([geographic_msgs/srv/GetRoutePlan](https://docs.ros.org/en/rolling/p/geographic_msgs/srv/GetRoutePlan.html)):
  Determine path to from start to goal way point.

### route_network

ROS node that gets a geographic map from a server (like the
[osm_server](https://index.ros.org/p/osm_cartography) node), and
publishes a route network graph based on it.

#### Published Topics

- `route_network`
  ([geographic_msgs/msg/RouteNetwork](https://docs.ros.org/en/rolling/p/geographic_msgs/msg/RouteNetwork.html)):
  Graph of drivable routes.

#### Services Called

- `get_geographic_map`
  ([geographic_msgs/srv/GetGeographicMap](https://docs.ros.org/en/rolling/p/geographic_msgs/srv/GetGeographicMap.html)):
  Get map of current region.

#### Parameters

- `map_url` (`string`): Uniform Resource Locator for the map (see
  [osm_cartography](https://index.ros.org/p/osm_cartography) for
  details).

### viz_routes

ROS node that reads route network messages, and publishes
[rviz](https://index.ros.org/p/rviz) visualization markers.

#### Subscribed Topics

- `route_network`
  ([geographic_msgs/msg/RouteNetwork](https://docs.ros.org/en/rolling/p/geographic_msgs/msg/RouteNetwork.html)):
  Graph of drivable routes.

#### Published Topics

- `visualization_marker_array`
  ([visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html)):
  Markers for visualizing the route network.
