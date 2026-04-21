# Applications

## Outdoor obstacle avoidance and hole detection with a time-of-flight camera

### Overview

This application implements a method to integrate a time of flight
camera on an all terrain outdoor mobile robot to enhance its reactive
navigation capabilities. The developed algorithms include sensor data
processing for obstacle and hole detection, as well as a planer to take
into account the non-holonomic property of the platform.

### Dependences

The next scheme shows the relationship between the original nodes of the
[pcl](pcl) and [navigation](navigation) stacks (gray), and the nodes
used in this application (white).

![\|width=\"770px\"](attachment:scheme.jpg)

**IRI nodes**:

-   [average_point_cloud_node](average_point_cloud_node)
-   [iri_obstacle_detection_normals](iri_obstacle_detection_normals)
-   [iri_hole_detection](iri_hole_detection)
-   [iri_bspline_navfn](iri_bspline_navfn)

### Usage

This section indicates the steps to follow to run the application once
the related dependences have been acquired.

**B-spline addition to global planner:**

To use this software it is expected to launch your robot with the ROS
navigation stack, inwhich the navfn node will be modified by a B-spline
addition.

1\. Download [iri_bspline_navfn](iri_bspline_navfn), rename it to
navfn. 1. Double-check your ROS_PACKAGE_PATH to ensure that new navfn
package is found in the correct precedence order (ROS needs to find the
new navfn package to use it with the [navigation](navigation) stack,
thus we indicate firstly the path of the new navfn node in the
ROS_PACKAGE_PATH). 1. Compile the new navfn package (\`rosmake\`).

To verify this procedure once the new navfn is compiled, one can run
\'roscd navfn\' and ensure that the current path is the correct one.

**Vision system:**

-   \`roslaunch teo_apps obstacle_hole_detection.launch\`

### Example Videos

This video shows the use of the provided software.

[Youtube](https://www.youtube.com/watch?v=UTFg7d6535U)
