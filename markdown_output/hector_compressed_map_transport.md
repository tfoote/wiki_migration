## Overview

This package compresses map data using image transport. Currently, only
a conversion from map to image is available. The opposite direction is
not implemented yet. The code in this package is a proof of concept and
subject to change.

## ROS API



```clearsilver
node.0 {
name = map_to_image_node
desc = Converts map to image data and publishes the images using image_transport. The conversion is only done when the image data is requested, so the computational cost of this node running is low when no images are requested. Both a full map image as well as a tile based map image that shows only the local area around the robot are made available. For the latter to work, the robot pose must be available on the 'pose' topic as described below.

sub{
0.name= map
0.type= nav_msgs/OccupancyGrid
0.desc= The map to transmit
1.name= pose
1.type= geometry_msgs/PoseStamped
1.desc= The robot pose given in the map frame
}

pub{
   0{
    name = map_image/full
    type = sensor_msgs/Image
    desc = The complete map converted to an image.
   }
   1{
    name = map_image/tile
    type = sensor_msgs/Image
    desc = A tile of the map showing the area around the robot published as an image.
   }
}
```


