## Overview

The `lj_laser` package is a localizing jockey for the Large Maps
Framework ([LaMa](Large Maps Framework)) that computes place
dissimilarities based on a 360-degree
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html).

The role of this jockey is to get the dissimilarity of the
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
descriptors of all vertices with the current place profile (represented
by a
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)).
The action is done when the dissimilarities are computed. Implemented
actions:

-   `GET_VERTEX_DESCRIPTOR`: return the ids of the LaserScan
    descriptor and the computed Crossing descriptor
-   `GET_SIMILARITY`: return the dissimilarity based on
    [sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)

## Usage

### ROS API

#### Interaction with the map (created by this jockey)

  -- --------------------------- -- ----------------------------------------------------------------------------------------- -- ------------------------------ --
     \[Getter\]\[/\]\[Setter\]      message type                                                                                 interface default name         
     Getter/Setter                  !VectorLaserScan                                                                             jockey_name + "_laser"      
     Setter                         [lama_msgs/msg/Crossing](https://docs.ros.org/en/rolling/p/lama_msgs/msg/Crossing.html)      jockey_name + "_crossing"   
  -- --------------------------- -- ----------------------------------------------------------------------------------------- -- ------------------------------ --



```clearsilver
sub {
   0.name=~<name>/base_scan
   0.type= sensor_msgs/LaserScan
   0.desc= 360-degree laser-scan
}
srv {
  0.name= ~<name>/dissimilarity_server
  0.type= polygon_matcher/PolygonDissimilarity
  0.desc= used to compare all known places (as polygons) with the current place.
}
param {
  0.name= ~<name>/laser_interface_name
  0.default= jockey_name + "_laser"
  0.type= String
  0.desc= Name of the map interface for laser-scans.
  1.name= ~<name>/crossing_interface_name
  1.default= jockey_name + "_crossing"
  1.type= String
  1.desc= Name of the map interface for crossings.
  2.name= ~<name>/dissimilarity_server_name
  2.default= "dissimilarity_server"
  2.type= String
  2.desc= Name of the dissimilarity server.
}
```


