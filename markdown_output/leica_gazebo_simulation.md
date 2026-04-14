## Overview

The Leica Scanstation C5 is a scalable large range laser scanner. This
package is a simulator of the Leica Scanstation C5, which allows the
user to acquire a point cloud of the scene targeted by the device in the
simulator. The simulator allows for the configuration of the scanning
window so that the resulting cloud is as similar as possible to the one
that would be produced with the actual Leica Scanstation C5. The use of
the simulator begins with the loading of the virtual environment and the
device. Then the laser profile to point cloud converter is loaded
followed by the device plug-in.

. ![](attachment:simulator.gif)

## Getting started

### Leica Scanstation C5 Simulator

The Leica Scanstation C5 is a configurable laser scanner, which means
that the user can adjust the settings to define a scanning window. Using
this simulator, the following parameters can be specified:

-   \'\'\'Pan center\'\'\' and \'\'\'tilt center\'\'\'. Middle point of
    the scan window.
-   \'\'\'Width\'\'\' and \'\'\'height\'\'\' are the dimensions of the
    scanning window at a distance of one metre from the Leica
    Scanstation.
-   \'\'\'Vertical resolution\'\'\' and \'\'\'horizontal
    resolution\'\'\' can be understood as the \'\'number of rays\'\' to
    cover the scan window. A higher resolution means a more detailed
    cloud but a slower process.

. ![\|width=\"450px\"](attachment:scanparams.png)

### About Software Development

Currently, the simulator is still in its development stage, so the
configuration of the scanning window must be conducted via the
configuration file (\'\'sensor.urdf.xacro\'\').

## Usage

1\. Create a workspace and clone this repo ```
mkdir -p ~/catkin_ws/src
 cd ~/catkin_ws/src
 git clone https://github.com/fada-catec/leica_gazebo_simulation.git
```

2\. Install and compile dependencies: ```
sudo apt-get install libeigen3-dev
 mkdir -p ~/catkin_ws/src && cd ~/catkin_ws/src
 git clone https://github.com/fada-catec/leica_scanstation.git

 cd ~/catkin_ws
 catkin_make -DCATKIN_BLACKLIST_PACKAGES="leica_scanstation_ros"
```

3\. Compile all: ```
cd ~/catkin_ws
 catkin_make
 source devel/setup.bash
```

4\. Launch the environment and the device: ```
roslaunch leica_gazebo_simulation c5_system_spawn.launch world:=assembly_line
```

Place the Leica at your convenience.

. ![\|width=\"450px\"](attachment:C5_simulator.jpg)

The plugin created for LeicaScanstation C5 on Gazebo will publish
LaserScan msg. Use laserscan_to_pointcloud to convert it to PointCloud2.
Run the plugin to start movement and complete a scan on Gazebo.

```
roslaunch leica_gazebo_simulation c5_init.launch namespace:=c5
```

Tell simulator to start scan with desired window parameters. Point cloud
is published simultaneously. Once scan is finished, it will store the
complete point cloud with given file_name on folder specified in ROS
param server as \'\'/pointcloud_folder\'\' (default: package
leica_scanstation_utils/pointclouds).

```
rosservice call /c5/scan "{file_name: 'scan_sim', vertical_res: 512, horizontal_res: 1024, pan_center: 0.0, tilt_center: 0.0, width: 2, height: 2}"
```

## ROS API

### Services

```clearsilver
srv{
  no_header = True
  0{
   name = c5/scan
   type = leica_scanstation_msgs/Scan
   desc = Start scan request. Parameters: ''file_name'' to save it with; ''vertical_res'' and ''horizontal_res'' are the resolution of the pointcloud; ''pan_center'' and ''tilt_center'' are the middle point of the scan process and it's size is defined by ''width'' and ''height'', in meters.
   }
}
```

### Topics

```clearsilver
pub {
  no_header = True
  0{
   name = c5/simulator/scan
   type = sensor_msgs/LaserScan
   desc = Single scan from planar laser
   }
  1{
   name = c5/simulator/cloud
   type = sensor_msgs/PointCloud2
   desc = Point cloud constructed from laser scan data
   }
  2{
   name = c5/simulator/resolution
   type = std_msgs/Float64
   desc = Number of horizontal rays
   }
  3{
   name = c5/simulator/window
   type = sensor_msgs/RegionOfInterest
   desc = Define scan window. x_offset is the pan center, y_offset is the tilt center, width and height are set in milimeters.
   }
}
```

## Acknowledgement

\<\<Include(rosin/acknowledgement)\>\>
