## Overview

The multipoint_navigation_receiver realizes the simultaneous delivery of
multiple target points of the mobile robot. It maintains two arrays with
one-to-one correspondence between positions and attitudes, and obtains
feedback of the navigation results through SimpleActionClient, and
arrives in the order of the requested target points. Achieve a state
similar to patrol.

The working principle of obstacle_server node is as follows:

1\. Start a separate thread to subscribe to news on the topic
"/move_base/global_costmap/costmap 2. Obtain global_costmap data from
the subscribed data 3. Start a service "obstacle_information" for
feedback of obstacle information 4. The possibility of obtaining
obstacles from data according to the coordinates of the map passed in
when requesting the service (that is, the cost of a point in the
global_costmap)

The working principle of the multipoint_navigation_receiver node is as
follows:

1\. Confirm that the obstacle_information service has been turned on 2.
Start a service "goals_server" to receive data from multiple targets
3. Store the received array and get feedback from SimpleActionClient, If
you reach the current target point or if you haven't reached the target
point after a period of time and have the possibility to meet obstacles
on target point, then navigate to the next target point until you reach
the final target point

## Node API

```clearsilver
name = obstacle_server
desc = Provides possibility to meet obstacles on target point at map.
sub {
  0.name = move_base/global_costmap/costmap
  0.type = nav_msgs/OccupancyGrid
  0.desc = Provides obstacle information for the entire map.
}
srv {
  0.name = /obstacle_information
  0.type = multipoint_navigation_receiver/obstacle_srv
  0.desc = Allows an extemal user to ask for the possibility to meet obstacles on target point.
}
``` ```clearsilver
name = multipoint_navigation_receiver
desc = Receive multiple target points.
srv {
  0.name = /goals_server
  0.type = multipoint_navigation_receiver/set_goal_srv
  0.desc = Allows an extemal user to send multiple target points.
}
```
