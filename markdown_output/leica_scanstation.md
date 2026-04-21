## Overview

The Leica Scanstation C5 is a scalable large range laser scanner. This
package is a ROS wrapper for controlling the scanstation directly from a
computer. To achieve this, a collection of rosservices are provided and
information received is published as rostopics.

. ![](attachment:scanstationC5.jpg)

## Getting started

### Scan with Leica Scanstation C5

The Leica Scanstation C5 is a scalable and flexible laser scanner, which
means that user can set some parameters to better fit the scanning area.
Using this ROS wrapper, the user can specify the following parameters:

-   \'\'\'Pan center\'\'\' and \'\'\'tilt center\'\'\'. Middle point of
    the scan process.
-   \'\'\'Width\'\'\' and \'\'\'height\'\'\' are the size of the scan
    window.
-   \'\'\'Vertical resolution\'\'\' and \'\'\'horizontal
    resolution\'\'\'. Can be understood as the \'\'number of rays\'\' to
    cover the scan window. A higher resolution means a more detailed
    cloud but a slower process.

. ![\|width=\"450px\"](attachment:scanparams.png)

### About Software development

Due to Leica\'s libraries dependencies, the source code relative to SDK
have been developed under \'\'\'Windows 10\'\'\'. For that reason,
\'\'leica_scanstation_ros\'\' will only compile on Windows OS. However,
once the program is released, it can be executed in either \'\'\'Windows
or Linux\'\'\' (with tools such us Wine).

For \'\'\'development purposes\'\'\', please refer to
[leica_scanstation_ros](https://github.com/fada-catec/leica_scanstation/tree/master/leica_scanstation_ros)
documentation.

### Package List

-   Source: git <https://github.com/fada-catec/leica_scanstation>
    (branch: master)
-   \'\'\'leica_scanstation_ros\'\'\'. Based on Leica SDK, this package
    contains functions to communicate with the device using a computer.
    Note that this package is meant to be compiled and executed in
    Windows. It includes a ROS node with the following options:
-   operating the device through ROS services.
-   to read and understand the information sent by the scanstation which
    is published in a ROS topic.
-   to view the video captured by the device which is published as
    images in another ROS Topic.

```{=html}
<!-- -->
```
-   \'\'\'leica_scanstation_msgs\'\'\'. This package defines the
    messages and services that allow for interpretation of the scanner
    information. It is OS independent.

```{=html}
<!-- -->
```
-   \'\'\'leica_scanstation_utils\'\'\'. This package contains common
    functions that assist in the program\'s execution independently of
    the OS used. Its main purpose is to define the paths for generating
    and collecting the point clouds.

## Usage

### In ROS Windows

1\.
[Setup](https://github.com/fada-catec/leica_scanstation/tree/master/leica_scanstation_ros#set-up)
your workspace.

2\. Execute program ```
roslaunch leica_scanstation_ros start.launch
```

3\. Use [ROS services](#anchor_services) to control, move and start
scanning on the Scanstation. E.g: Try to move your pan and tilt
```
rosservice call /leica/move 3.141 0.785
```

### In Ubuntu (using wine)

1\. Create a workspace and clone this repo ```
mkdir -p ~/catkin_ws/src && cd ~/catkin_ws/src
 git clone https://github.com/fada-catec/leica_scanstation
```

2\. Compile (be careful: package leica_scanstation_ros is meant to be
compiled on Windows) ```
cd ~/catkin_ws
 catkin_make -DCATKIN_BLACKLIST_PACKAGES="leica_scanstation_ros"
```

3\. To be able to execute the program with wine, you need to export it
first. Read
[how to export program](https://github.com/fada-catec/leica_scanstation/blob/master/leica_scanstation_ros/README.md#export-program)
to get more information. ```
roscore
 cd ~/catkin_ws/src/leica_scanstation/leica_scanstation_ros/export
 wineconsole leica_scanstation_ros_node.exe
```

4\. Use [ROS services](#anchor_services) to control, move and start
scanning on the Scanstation. E.g: Try to move your pan and tilt
```
rosservice call /leica/move 3.141 0.785
```

## ROS API

### Topics

```clearsilver
pub {
  no_header = True
  0{
   name = eventer_info
   type = leica_scanstation_msgs/EventerInfo
   desc = Show information received from scanstation such as: process finished, progress state, error...
   }
  1{
   name = image
   type = sensor_msgs/Image
   desc = Video image from scanstation
   }
}
```

### Services

```clearsilver
srv{
  no_header = True
  0{
   name = ~connect
   type = std_srvs/Trigger
   desc = Open connection with scanner
   }
  1{
   name = ~disconnect
   type = std_srvs/Trigger
   desc = Close connection with scanner
   }
  2{
   name = ~move
   type = leica_scanstation_msgs/MotorPose
   desc = Move scanstation to specified position: pan and tilt angles in radians
   }
  3{
   name = ~tilt
   type = std_srvs/SetBool
   desc = Enable tilt
   }
  4{
   name = ~scan_info
   type = leica_scanstation_msgs/PointCloudFile
   desc = Read scan info from specified file, such us scan size, resolution...
   }
  5{
   name = ~scan
   type = leica_scanstation_msgs/Scan
   desc = Start scan request. Parameters: ''file_name'' to save it with; ''vertical_res'' and ''horizontal_res'' are the resolution of the pointcloud; ''pan_center'' and ''tilt_center'' are the middle point of the scan process and it's size is defined by ''width'' and ''height''.
   }
  6{
   name = ~cancel
   type = std_srvs/Trigger
   desc = Stop and cancel scan process
   }
  7{
   name = ~pause
   type = std_srvs/Trigger
   desc = Pause scan process
   }
  8{
   name = ~resume
   type = std_srvs/Trigger
   desc = Continue scan process if paused
   }
  9{
   name = ~convert
   type = leica_scanstation_msgs/PointCloudFile
   desc = Leica Scanstation saves scan results in binary format. Convert it to readable format '''.ptx'''
   }
  10{
   name = ~video
   type = leica_scanstation_msgs/MotorPose
   desc = Publish video images from scanstation
   }
```

### Parameters

```clearsilver
param {
  no_header = True
  0{
   name = /pointcloud_folder
   type = string
   desc = Set by leica_scanstation_utils and operating system dependent
   default = "leica_scanstation_utils/pointclouds"
   }
```

## Acknowledgement

[Included page rosin/acknowledgement not found](Included page rosin/acknowledgement not found)
