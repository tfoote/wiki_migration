## ROS API

The package [cob_ultrasonic](cob_ultrasonic) is responsible for the
visualisation of output from an ultrasonic sensor. It provides an output
in the form of feature interactive markers messages and a laser scan.
The feature marker messages provide information about each feature
detected by the ultrasonic sensor whereas the laser scan messages
provide 360 degrees visualisation. 

```clearsilver
 name = ultrasonic_node
 desc = The `ultrasonic_node` node publishes <<MsgLink(sensor_msgs/LaserScan)>> and <<MsgLink(visualization_msgs/InteractiveMarker)>> based on the output from an ultrasonic sensor. 

pub{
 0.name = /ultrasonic
 0.type = visualization_msgs/InteractiveMarker
 0.desc = The features will be published on this topic
 1.name = /scan
 1.type = sensor_msgs/LaserScan
 1.desc = The laserscan message generated will be published on this topic.
}

param{
 0.name = frame_id
 0.type = string
 0.default = /my_frame
 0.desc = It can be used to set custom frame ids for the markers.
 1.name = namespace
 1.type = string
 1.default = 
 1.desc = It can be used to setup a separate namespace for all the markers.
 2.name = line_color
 2.type = integer
 2.default = 0
 2.desc = For setting the colour of lines. Permissible values: 0=RED, 1=GREEN, 2=BLUE.
 3.name = point_color
 3.type = integer
 3.default = 1
 3.desc = For setting the colour of points. Permissible values: 0=RED, 1=GREEN, 2=BLUE.
 4.name = fast_color
 4.type = integer
 4.default = 2
 4.desc = For setting the colour of fasts. Permissible values: 0=RED, 1=GREEN, 2=BLUE.
 4.name = marker_radius
 4.type = double
 4.default = 10.0
 4.desc = This parameter can be used to set the radius for points and fasts.
 5.name = laserscan_range_min
 5.type = double
 5.default = 0.05
 5.desc = This parameter is used define the minimum range for the laser scan message.
 6.name = laserscan_range_max
 6.type = double
 6.default = 10.0
 6.desc = This parameter is used define the maximum range for the laser scan message.
}
```



## Usage/Examples



```
roslaunch cob_ultrasonic ultrasonic_node.launch
```


