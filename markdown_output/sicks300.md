## The AIS Bonn SickS300 Driver

### General Information

This package contains a driver which reads out the scan data of a
Sick(R) S300 Professional via the lasers serial interface.

### Getting started

Make sure that all dependencies are satisfied:



```
rosmake sicks300 sicks300
```



Run the node:



```
rosrun sicks300 sick300_driver
```



### Messages



```clearsilver
pub {
0.name = /laserscan
0.type = sensor_msgs/LaserScan
0.desc = Scan data
}
param {
0.name = ~frame
0.type = String
0.desc = Laser frame
0.default = "base_laser_link"
1.name = ~send_transform
1.type = int
1.desc = Send Transform from base_link to base_laser_link.
1.default = 1
2.name = ~tf_x
2.type = double
2.desc = Transformation along x-axis
2.default = 0.115
3.name = ~tf_y
3.type = double
3.desc = Transformation along y-axis
3.default = 0.0
4.name = ~tf_z
4.type = double
4.desc = Transformation along z-axis
4.default = 0.21
5.name = ~reduced_fov
5.type = int
5.desc = Reduces the field of view to 180 degrees.
5.default = 0
6.name = ~devicename
6.type = String
6.desc = Port connected to laser.
6.default = "/dev/sick300"
7.name = ~baudrate
7.type = int
7.desc = Sets the baud rate
7.default = 500000
}
```


