## Overview

This package provides a ROS driver for Infinisoleil sensors. The driver
accesses the sensors using infinisoleil-lib.

The driver publishes range and IR images and point cloud. The driver
converts from received packets containing range and IR data into
sensor_msgs/Image respectively. In addition, the driver creates
sensor_msgs/PointCloud2 by using obtained range data and sensor
information.

## Installation

### Setup infiniosleil-lib

This package requires infinisoleil-lib. Please download the library from
[SourceForge](http://sourceforge.net/projects/infinisoleil-lib) and
install it.

### Install infinisoleil

Please clone the source repository into your catkin SOURCE SPACE and run
catkin_make at root of your catkin WORK SPACE.

## ROS API



```clearsilver
node.0 {
  name=FX8DrvierNodelet
  desc=The driver nodelet receives scan data from the sensor and publishes the data.
  pub {
    group.0 {
      name=Scan data
      desc=The driver receives scan data from the sensor and publishes it as range image, IR image and point cloud.
      1.name=range_image
      1.type=sensor_msgs/Image
      1.desc=Range image. It contains uint16 depths in mm.
      2.name=ir_image
      2.type=sensor_msgs/Image
      2.desc=IR image. It contains uint16 intensity.
      3.name=point_cloud
      3.type=sensor_msgs/PointCloud2
      3.desc=Point cloud. It contains xyz float type data in meter. Sensor xyz axes are the follows. +x is up, +y is right and +z is forward.
    }
    group.1 {
      name=Diagnostics
      desc=The driver publishes frequency diagnostics of topics, received error code from the sensor and returned error information of infinisoleil-lib.
      1.name=/diagnostics
      1.type=diagnostic_msgs/DiagnosticArray
      1.desc=Diagnostic status information.
    }
  }

  param {
    group.0 {
      name=Initial Parameters
      desc=These parameters only affect the driver when it starts.
      1.name=~hostname
      1.default=192.168.0.80
      1.type=str
      1.desc=Sensor hostname.
      2.name=~port_number
      2.default=50000
      2.type=str
      2.desc=Sensor port number.
      3.name=~connect_timeout
      3.default=10000
      3.type=int
      3.desc=Connect timeout [ms]. It should be greater than or equal to 0.
      4.name=~send_timeout
      4.default=3000
      4.type=int
      4.desc=Send timeout [ms]. It should be greater than or equal to 0.
      5.name=~receive_timeout
      5.default=5000
      5.type=int
      5.desc=Receive timeout [ms]. It should be greater than or equal to 0.
      6.name=~range_frame_id
      6.default=range_image
      6.type=str
      6.desc=Frame id of range_image.
      7.name=~ir_frame_id
      7.default=ir_image
      7.type=str
      7.desc=Frame id of ir_image
      8.name=~point_cloud_frame_id
      8.default=point_cloud
      8.type=str
      8.desc=Frame id of point_cloud.
      9.name=~diagnostics_enable
      9.default=true
      9.type=bool
      9.desc= Switch to enable diagnostics. If true, the driver publishes diagnostics.
    }
    group.1 {
      name=Reconfigurable Parameters
      desc=The sensor has measure_mode. The driver configures measure_mode of the sensor when the driver receives a request for reconfiguration. Image resolution and frame_cycle are changed according to measure_mode.
      1.name=~measure_mode
      1.default=0
      1.type=int
      1.desc=Measure mode of a sensor.
    }
    group.2 {
      name=Read-only Parameters
      desc=These parameters are read-only.
      1.name=~measure_point_x
      1.type=int
      1.desc=The number of measure points in a row of scan data.
      2.name=~measure_point_y
      2.type=int
      2.desc=The number of measure points in a col of scan data.
      3.name=~swing_fs
      3.type=int
      3.desc=High speed side deflection angle [1/10 degree].
      4.name=~swing_ss
      4.type=int
      4.desc=Low speed side deflection angle [1/10 degree].
      5.name=~xy_surface_count
      5.type=int
      5.desc=Xy data surface count.
      6.name=~frame_cycle
      6.type=int
      6.desc=Frame cycle [ms].
      7.name=~max_measure_mode
      7.type=int
      7.desc=Max value of measure mode.
      8.name=~xy_serial_number
      8.type=str
      8.desc=Xy data serial number. It is 4 bytes data.
      9.name=~logic_version
      9.type=str
      9.desc=Sensor logic version. It is set as Major.Minor.Sequence.
      10.name=~firm_version
      10.type=str
      10.desc=Sensor firm version. It is set as Major.Minor.Sequence.
      11.name=~product_number
      11.type=str
      11.desc=Sensor product number. It is set by 8 bytes ASCII-code.
    }
  }
}
node.1 {
  name=fx8_node
  desc=The node has nodelet loader and load FX8DriverNodelet at initialization. It provides the same ROS API as FX8DriverNodelet above.
}
```



## Usage

Start a nodelet manager process with an FX8DriverNodelet. The driver
publishes range image, IR image and point cloud. If other nodelets are
loaded in the same nodelet manager process, those will have zero copy
access to published topics.



```
$ rosrun nodelet nodelet manager
$ rosrun nodelet nodelet load infinisoleil/FX8DriverNodelet manager
```



Start a driver nodelet with configuration of hostname.


```
$ rosrun nodelet nodelet manager
$ rosrun nodelet nodelet load infinisoleil/FX8DriverNodelet manager _hostname:=192.168.0.81
```



### Launch file

This package has two launch files. fx8_drvier.launch runs a nodelet
manager process and an FX8DriverNodelet. fx8_node.launch runs an
fx8_node. 

```
$ roslaunch infinisoleil fx8_driver.launch
```

 

```
$ roslaunch infinisoleil fx8_node.launch
```



Start an fx8_node by roslaunch with configuration of hostname.


```
$ roslaunch infinisoleil fx8_node.launch hostname:=192.168.0.81
```



Start a driver nodelet by roslaunch without diagnostics.


```
$ roslaunch infinisoleil fx8_driver.launch diagnostics_enable:=false
```



fx8_driver.launch runs a nodelet manager and a driver nodelet. The
nodelet manager can load another driver nodelet but drivers cannot
connect to the same sensor. So, this case requires two sensors.


```
<launch>
    <!-- launch fx8_driver.launch -->
    <include file="$(find infinisoleil)/launch/fx8_driver.launch"/>
  
    <!-- Add another driver nodelet -->
    <node pkg="nodelet" type="nodelet" name="add_driver"
      args="load infinisoleil/FX8DriverNodelet fx8_nodelet_manager"
      output="screen">
      <remap from="range_image" to="add_driver/range_image"/>
      <remap from="ir_image" to="add_driver/ir_image"/>
      <remap from="point_cloud" to="add_driver/point_cloud"/>
      <param name="hostname" type="str" value="192.168.0.81"/>
    </node>
  </launch>
```



### Tests

This package supports hertz test. Hertz test checks frame_cycle
corresponded to specific measure_mode. For instance, run a test with
default parameters.



```
$ rostest infinisoleil fx8_driver_hertz.test
```



Run a test with configuration of hostname. 

```
$ rostest infinisoleil fx8_driver_hertz.test set_hostname:=192.168.0.81
```



Run a test with configuration of measure mode. 

```
$ rosrun nodelet nodelet manager
$ rosrun nodelet nodelet load infinisoleil/FX8DriverNodelet manager
```

0
