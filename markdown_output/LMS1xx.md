## Supported Hardware

This package should work with Sick LMS 1xx laser range finders.

Note that this package has been released by Clearpath Robotics as
[lms1xx](lms1xx). You can install it on Ubuntu using apt:



```
sudo apt-get install ros-$ROS_DISTRO-lms1xx
```



## Nodes



```clearsilver
node.0 {
name=LMS100
desc=`LMS100` is a ROS node for libLMS1xx.
pub{
0.name= scan
0.type= sensor_msgs/LaserScan
0.desc= Scan data from the laser.
}
param {
0.name= ~host
0.default=`192.168.1.2`
0.type= string
0.desc= The device hostname or IP address.
2.name= ~frame_id
2.default=`laser`
2.type= string
2.desc= The laser data frame. This frame should be at the optical center of the laser, with the x-axis along the zero degree ray, and the y-axis along the pi/2 degree ray.
}
}
```


