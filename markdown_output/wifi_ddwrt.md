## Overview

This package provides tools for logging statistics from a router using
[ddwrt](http://www.dd-wrt.com) !OpenSource firmware and publishing them
over ROS.

## Nodes

### ddwrt

The ddwrt [ROS Node](Nodes) publishes information about the Access Point
that the router is currently connected to as well as survey information
about all the Access Points that the router can see.

#### Published Topics

- `ddwrt/sitesurvey`
  ([wifi_ddwrt/msg/SiteSurvey](https://docs.ros.org/en/rolling/p/wifi_ddwrt/msg/SiteSurvey.html)):
  A survey of all the Access Points that the router sees with their
  associated signal strength and noise values.
- `ddwrt/accesspoint`
  ([wifi_ddwrt/msg/AccessPoint](https://docs.ros.org/en/rolling/p/wifi_ddwrt/msg/AccessPoint.html)):
  Information about the Access Point that the router is currently
  connected to including signal strength and noise values.

#### Parameters

- `~router` (`string`, default: `"10.68.0.5"`): The ip address of the
  router we wish to publish information about.
- `~username` (`string`, default: `root`): Username to connect to router
- `~password` (`string`): Password to connect to router.

### monitor

The monitor node publishes a visualization marker to
[rviz](https://index.ros.org/p/rviz) that displays between 1-5 bars over
the robot's head according to the signal strength of the Access Point
the robot is currently connected to.

#### Subscribed Topics

- `ddwrt/sitesurvey`
  ([wifi_ddwrt/msg/SiteSurvey](https://docs.ros.org/en/rolling/p/wifi_ddwrt/msg/SiteSurvey.html)):
  A survey of all the Access Points that the router sees with their
  associated signal strength and noise values.
- `ddwrt/accesspoint`
  ([wifi_ddwrt/msg/AccessPoint](https://docs.ros.org/en/rolling/p/wifi_ddwrt/msg/AccessPoint.html)):
  Information about the Access Point that the router is currently
  connected to including signal strength and noise values.

#### Published Topics

- `visualization_marker`
  ([visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)):
  A marker to display bars above the robot's head in rviz

### analysis

The analysis node logs information about signal strength from the Access
Points that the robot connects to and displays visualizations of this
information on a map which it saves as a png image.

#### Subscribed Topics

- `ddwrt/sitesurvey`
  ([wifi_ddwrt/msg/SiteSurvey](https://docs.ros.org/en/rolling/p/wifi_ddwrt/msg/SiteSurvey.html)):
  A survey of all the Access Points that the router sees with their
  associated signal strength and noise values.
- `ddwrt/accesspoint`
  ([wifi_ddwrt/msg/AccessPoint](https://docs.ros.org/en/rolling/p/wifi_ddwrt/msg/AccessPoint.html)):
  Information about the Access Point that the router is currently
  connected to including signal strength and noise values.

#### Published Topics

- `visualization_marker`
  ([visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)):
  Markers corresponding to the signal strength of a given Access Point
  at each position a reading was taken.

### output

The analysis node will save a file called "static_map.png" on exit
that displays signal strength information for a run.
