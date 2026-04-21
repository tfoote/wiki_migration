## Overview

This package enables conversion of messages of type
<<MsgLink(toposens_msgs/TsScan)>> into messages of type
<<MsgLink(sensor_msgs/PointCloud2)>>.

### Surface Normals

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     <#FFFFCC>Since **version 2.0** the package makes use of the standard PointCloud type **PointXYZINormal** instead of the custom type **TsPoint**. As a result the PointCloud also contains information about the surface normals.   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

Due to the specular reflection behavior of ultrasound, the surface
normal of the detected object can be represented by a vector pointing
from the detected point towards the sensor's position while the point
was recorded. This normal vector is added to the PointCloud
representation. For a more detailed explanation of the physics behind
Toposens sensors see
[Physics of 3D Ultrasonic Sensors](https://www.researchgate.net/publication/334784649_Physics_of_3D_Ultrasonic_Sensors).

## ROS Nodes



```clearsilver
name = ts_cloud_node
desc = translates messages of type <<MsgLink(toposens_msgs/TsScan)>> into messages of type <<MsgLink(sensor_msgs/PointCloud2)>>. Also logs the PointCloud into a pcd file.
sub {
  0.name = ts_scans
  0.type = toposens_msgs/TsScan
  0.desc = the scans that are published by the [[toposens_driver]] (name of the topic is a parameter)
}
pub {
  0.name = ts_cloud
  0.type = sensor_msgs/PointCloud2
  0.desc = the PointCloud of type: PointXYZINormal that is created by accumulating the Toposens sensor data
  1.name = ts_cloud_normals
  1.type = visualization_msgs::Marker
  1.desc = markers that visualize the the normal vectors of the points in the PointCloud
}
param {
  0.name = ~scans_topic
  0.type = std_msgs/String
  0.desc = topic name to listen for TsScan data
  1.name = ~target_frame
  1.type = std_msgs/String
  1.desc = frame ID in which the data is published
  2.name = ~pcd_save_interval
  2.type = int
  2.desc = interval after which PointCloud is stored to pcd file (set to zero for non logging the PointCloud)
  3.name = ~pcd_path
  3.type = std_msgs/String
  3.desc = path where pcd file should be stored
  4.name = ~lifetime_normals_vis
  4.type = float
  4.desc = lifetime for markers that visualize normal vectors (set to zero for not publishing the markers)
}
```


