\`local_map\` provides a simple local cost map for several jockeys for
the Large Maps Framework ([LaMa](Large Maps Framework)). The map is
centered on the frame of the laser range finder on which it is based but
its orientation is fixed.

## Overview

The image shows the map in player on the left and the local map obtained
from the !LaserScan (red dots) on the right. The robot\'s orientation is
approximately 45° but the map\'s orientation is fixed.

![\|height=\"291\",width=\"751\"](attachment:local_map2.png)

## Usage

### ROS API

```clearsilver
sub {
   0.name=~<name>/footprint
   0.type= sensor_msgs/LaserScan
   0.desc= LaserScan with possibly less than 360° angular range.
}
pub {
  0.name= ~<name>/local_map
  0.type= nav_msgs/OccupancyGrid
  0.desc= The values in the costmap (similar to [[costmap_2d]]).
}
param {
  0.name= ~<name>/map_width
  0.default= 200
  0.type= float
  0.desc= Map pixel width (x-direction).
  1.name= ~<name>/map_height
  1.default= 200
  1.type= float
  1.desc= Map pixel height (y-direction).
  2.name= ~<name>/map_resolution
  2.default= 0.02
  2.type= double
  2.desc= Map resolution (m/pixel).
}
```
