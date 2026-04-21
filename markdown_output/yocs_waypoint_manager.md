# Overview

Provides a multiple of poses with name as list of waypoint and
visualization markers.

# ROS APIs



```clearsilver
node { 
 0{
  name = Waypoint Manager
  desc = Provides a mulltiple poses with names parsed from yaml format
  param{
   0{
    name = ~filename
    type = string
    desc = YAML filename to extract waypoints.
   }
  }
  pub{
   0{
    name = waypoints
    type = yocs_msgs/WaypointList
    desc = Publishes a list of waypoints
   }
   1{
    name = waypoints_viz
    type = visualization_msgs/MarkerArray
    desc = to visualize waypoints on GUI
   }
  }
  srv{
   0{
    name = request_waypoints
    type = yocs_msgs/WaypointListService
    desc = Returns a list of waypoints
   }
  }
 }
```


