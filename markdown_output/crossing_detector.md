## Overview

The `crossing_detector` package implements a method to recognize a
crossing, i.e. a place from where the robot can take clearly distinctive
paths. It is part of the Large Maps Framework
([LaMa](Large Maps Framework)).

The computation is based on a costmap such as those provided by the
[local_map](local_map) package, a <<MsgLink(sensor_msgs/LaserScan)>>
message, or a <<MsgLink(lama_msgs/PlaceProfile)>> message. It is
meant to be used in the form of a class instance but two nodes are
provided that compute a <<MsgLink(lama_msgs/Crossing)>> from a
<<MsgLink(lama_msgs/PlaceProfile)>> or a
<<MsgLink(sensor_msgs/LaserScan)>>, respectively, as a service.

The crossing center and radius are computed, as well as the frontiers,
i.e. a free space through which the robot can go.

![crossing center and radius](attachment:crossing_center_and_radius.png)

![frontiers](attachment:frontiers.png)

## Usage

Packages [lj_costmap](lj_costmap) and [lj_laser](lj_laser) use the
functionalities provided by the `crossing_detector` package and can be
used as example.

<<MsgSrvDoc(crossing_detector)>>
