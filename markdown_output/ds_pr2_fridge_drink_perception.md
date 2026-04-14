### Description

The package contains two launch scripts.

extract_clusters.launch which launches the a perception pipeline which
locates cylindrical clusters inside a refrigerator using parametric
model fitting for

-   The internal structure of the refrigerator
-   The object clusters inside the refrigerator.

extract_clusters_offset.launch launches a perception pipeline which
calculates known offsets from the point cloud aligned to the internal
structure of the refrigerator.

The script works with both kinect and narrow stereo data. The input
topic is specified in the launch files.

![A screen shot from rviz with the detected can visualized with a marker, The marker is displayed on top of the kinect point cloud\|height=400 width=400](attachment:/home/sab1pal/Desktop/drinks_pics/markershot3.png)

### Launch Parameters

extract_clusters.launch : All parameters set in the launch file are
standard pcl parameters.

extract_clusters_offset.launch : The rail_x_offset,rail\_\<int\>\_offset
parameters are offsets from the right plane and back plane of the
refrigerator. rail_z_offset is the distance from the ground.

### Action Client

The action client takes a goal, which encodes the rail number inside the
refrigerator. Each rail number corresponds to a specific drink.

The action is defined as follows : ```
#goal definition
uint8 rail_nr
---
#result definition
geometry_msgs/PoseStamped centroid
geometry_msgs/TwistStamped target
bool success
---
#feedback
```
