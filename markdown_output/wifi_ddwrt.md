## Overview

This package provides tools for logging statistics from a router using
[ ddwrt](http://www.dd-wrt.com ) !OpenSource firmware and publishing
them over ROS.

## Nodes

### ddwrt

The ddwrt [ ROS Node](Nodes ) publishes information about the Access
Point that the router is currently connected to as well as survey
information about all the Access Points that the router can see.



```clearsilver
  pub {
    0.name = ddwrt/sitesurvey
    0.type = wifi_ddwrt/SiteSurvey
    0.desc = A survey of all the Access Points that the router sees with their associated signal strength and noise values.
    1.name = ddwrt/accesspoint
    1.type = wifi_ddwrt/AccessPoint
    1.desc = Information about the Access Point that the router is currently connected to including signal strength and noise values. 
  }
  param {
    0.name = ~router
    0.default = "10.68.0.5"
    0.type = string
    0.desc = The ip address of the router we wish to publish information about.
    1.name = ~username
    1.default = root
    1.type = string
    1.desc = Username to connect to router
    2.name = ~password
    2.type = string
    2.desc = Password to connect to router.
    2.default =
  }
```



### monitor

The monitor node publishes a visualization marker to [rviz](rviz) that
displays between 1-5 bars over the robot's head according to the signal
strength of the Access Point the robot is currently connected to.



```clearsilver
  sub {
    0.name = ddwrt/sitesurvey
    0.type = wifi_ddwrt/SiteSurvey
    0.desc = A survey of all the Access Points that the router sees with their associated signal strength and noise values.
    1.name = ddwrt/accesspoint
    1.type = wifi_ddwrt/AccessPoint
    1.desc = Information about the Access Point that the router is currently connected to including signal strength and noise values. 
  }
  pub {
    0.name = visualization_marker
    0.type = visualization_msgs/Marker
    0.desc = A marker to display bars above the robot's head in rviz
  }
```



### analysis

The analysis node logs information about signal strength from the Access
Points that the robot connects to and displays visualizations of this
information on a map which it saves as a png image.



```clearsilver
  sub {
    0.name = ddwrt/sitesurvey
    0.type = wifi_ddwrt/SiteSurvey
    0.desc = A survey of all the Access Points that the router sees with their associated signal strength and noise values.
    1.name = ddwrt/accesspoint
    1.type = wifi_ddwrt/AccessPoint
    1.desc = Information about the Access Point that the router is currently connected to including signal strength and noise values. 
  }
  pub {
    0.name = visualization_marker
    0.type = visualization_msgs/Marker
    0.desc = Markers corresponding to the signal strength of a given Access Point at each position a reading was taken.
  }
```



### output

The analysis node will save a file called "static_map.png" on exit
that displays signal strength information for a run.
