## Overview

This experimental package is in an early rapid-prototyping phase. The
initial goal is to demonstrate the feasibility of the
[geographic_info](https://index.ros.org/p/geographic_info) API for
working with Open Street Map information.

These interfaces are still changing rapidly, nothing is stable yet.

## ROS Nodes



```clearsilver
node.0 {
 name = plan_route
 desc = ROS node that reads route network messages, and provides a route planning service. 
 sub {
  0.name= route_network
  0.type= geographic_msgs/RouteNetwork
  0.desc= Graph of drivable routes.
}
 srv {
  0.name= get_route_plan
  0.type= geographic_msgs/GetRoutePlan
  0.desc= Determine path to from start to goal way point.
}
}
```





```clearsilver
node.0 {
 name = route_network
 desc = ROS node that gets a geographic map from a server (like the [[osm_cartography#osm_server|osm_server]] node), and publishes a route network graph based on it. 
 pub {
  0.name= route_network
  0.type= geographic_msgs/RouteNetwork
  0.desc= Graph of drivable routes.
}
 srv_called {
  0.name= get_geographic_map
  0.type= geographic_msgs/GetGeographicMap
  0.desc= Get map of current region.
}
 param {
  0.name= map_url
  0.type= string
  0.desc= Uniform Resource Locator for the map (see [[osm_cartography#Uniform_Resource_Locators|osm_cartography]] for details).
}
}
```





```clearsilver
node.0 {
 name = viz_routes
 desc = ROS node that reads route network messages, and publishes [[rviz]] visualization markers.
 sub {
  0.name= route_network
  0.type= geographic_msgs/RouteNetwork
  0.desc= Graph of drivable routes.
}
 pub {
  0.name= visualization_marker_array
  0.type= visualization_msgs/MarkerArray
  0.desc= Markers for visualizing the route network.
}
}
```
