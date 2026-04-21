## Overview

Laser Scanner measurements (or a rangefinder sensor) require to be
pre-processed before to be analized by the twoLevelMTTD. The algorithm
will elaborate only non-environment measurements (people or object in
movement), so separate environment and non-environment measurements is
necessary. This package provide `background` node which is
responsabile of this operation: if an pre-builted environment map is
avaiable by [map_server](map_server), laser measurements will be
compared with the environment and only non-environment measurement will
be used. The output is a [sensor_msgs/PointCloud](sensor_msgs) referred
to a target_frame (`"/map"` as default).

## Nodes



```clearsilver
node.0{
 name = background
 descr = Background subtraction on Laser Scanner Measurements

pub {
  0.name= /MTTDI1/object_point_cloud
  0.type= sensor_msgs/PointCloud
  0.desc= Non-environment measurements in PointCloud 
}
sub {
  0.name= /base_scan
  0.type= sensor_msgs/LaserScan
  0.desc=  Data received from the 2D laser scanner.
}
srv {
  0.name= static_map
  0.type= nav_msgs/GetMap
  0.desc= Service required avaiable by [[map_server|map_server]] node.
}
param{
    0.name=~target_frame_id
    0.default = `"/map"`
    0.type= string
    0.desc= The name of the PointCloud output frame.
    1.name=~laser_frame_id
    1.default = `"/base_scan"`
    1.type= string
    1.desc= The name of the laser scanner frame.
}
```


