## Overview

This package provides basic device handling for 2D Laser Scanner RPLIDAR
A1/A2 and A3.

RPLIDAR is a low cost LIDAR sensor suitable for indoor robotic SLAM
application. It provides 360 degree scan field, 5.5hz/10hz rotating
frequency with guaranteed 8 meter ranger distance, current more than 16m
for A2 and 25m for A3 . By means of the high speed image processing
engine designed by RoboPeak, the whole cost are reduced greatly, RPLIDAR
is the ideal sensor in cost sensitive areas like robots consumer and
hardware hobbyist.

[RPLIDAR A3](http://www.slamtec.com/en/Lidar/A3) performs high speed
distance measurement with more than 16K samples per
second,[RPLIDAR A2](http://www.slamtec.com/en/Lidar) performs high speed
distance measurement with more than 4K/8K samples per
second,[RPLIDAR A1](http://www.slamtec.com/en/Lidar/A1) supports 2K/4K
samples per second. For a scan requires 360 samples per rotation, the
10hz scanning frequency can be achieved. Users can customized the
scanning frequency from 2hz to 10hz freely by control the speed of the
scanning motor. RPLIDAR will self-adapt the current scanning speed.

The driver publishes device-dependent
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
data.

SLAM based on RPLIDAR and ROS Hector Mapping:

[Youtube](https://www.youtube.com/watch?v=pCF7P7u8pDk)

## ROS Nodes



```clearsilver
node.0 {
  name = rplidarNode
  desc = rplidarNode is a driver for RPLIDAR. It reads RPLIDAR raw scan result using RPLIDAR's SDK and   convert to ROS LaserScan message.
  pub {
    0.name = scan
    0.type = sensor_msgs/LaserScan
    0.desc = it publishes scan topic from the laser.
  }
  srv {
     0.name = stop_motor
     0.type = std_srvs/Empty
     0.desc = Call the serive to stop the motor of rplidar.
     1.name = start_motor
     1.type = std_srvs/Empty
     1.desc = Call the service to start the motor of rplidar.
  }
  param {
    0.name= serial_port
    0.type= string
    0.desc= serial port name used in your system.
    0.default= /dev/ttyUSB0
    1.name= serial_baudrate
    1.type= int
    1.desc= serial port baud rate.
    1.default= 115200
    2.name= frame_id
    2.type= string
    2.desc= frame ID for the device.
    2.default= laser_frame
    3.name= inverted
    3.type= bool
    3.desc= indicated whether the LIDAR is mounted inverted.
    3.default= false
    4.name= angle_compensate
    4.type= bool
    4.desc= indicated whether the driver needs do angle compensation.
    4.default= false
    5.name= scan_mode
    5.type= string
    5.desc= the scan mode of lidar.
    5.default= std::string()
  }
}
```



## Device Settings

[RPLIDAR tutorial](https://github.com/robopeak/rplidar_ros/wiki)

Use following udev rules to set permission for a rplidar device.



```
KERNEL=="ttyUSB*", MODE="0666"
```

 For fixed rplidar port, you can using the
script file to remap the USB port name:



```
./scripts/create_udev_rules.sh
```

 Once you have change the USB port remap, you
can change the launch file about the serial_port value.



```
<param name="serial_port" type="string" value="/dev/rplidar"/>
```



## Launch File Examples

Check the authority of rplidar's serial-port :



```
ls -l /dev |grep ttyUSB
```

 Add the authority of write: (such as
/dev/ttyUSB0)



```
sudo chmod 666 /dev/ttyUSB0
```

 Start a rplidar node and view the scan result
in rviz.



```
$ roslaunch rplidar_ros view_rplidar.launch    #for rplidar A1/A2
or
 $ roslaunch rplidar_ros view_rplidar_a3.launch #for rplidar A3
```

 Start a rplidar node and run rplidar client
process to print the raw scan result



```
$ roslaunch rplidar_ros rplidar.launch  #for rplidar A1/A2
or
 $ roslaunch rplidar_ros_a3 rplidar.launch  #for rplidar A3

 $ rosrun rplidar_ros rplidarNodeClient
```



## About Slamtec/RoboPeak

RoboPeak is a research & development team in robotics platforms and
applications, founded in 2009. Our team members are Software Engineers,
Electronics Engineers and New Media Artists that all come from China. We
establish our company [Slamtec](http://www.slamtec.com/en) in 2013.

Slamtec focus on providing economically affordable and high-performance
solution for robots in auto localization and navigation as well as
offering related core sensors. And our major products are low-cost LIDAR
sensor(RPLIDAR), SLAM (Simultaneous Localization and Mapping) solution
based on LIDAR technology and Zeus General Purpose Robot Platform which
can be widely used in business places.

Our vision is to enrich people's daily-life with the ever-changing
development and innovation in robotic technologies.

Website: [Slamtec](http://www.slamtec.com/en)

## Distributor Links

[Slamtec resellers](http://www.slamtec.com/en/Home/Buy)

## Related Links

[Slamtec HomePage](http://www.slamtec.com/en)

[RPLIDAR SDK](http://www.slamtec.com/en/Lidar)

[rplidar_ros tutorial](https://github.com/robopeak/rplidar_ros/wiki)

[Review by mechatronicsguy](https://sites.google.com/site/mechatronicsguy/rplidar-review)
