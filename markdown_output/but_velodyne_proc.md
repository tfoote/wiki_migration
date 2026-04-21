## Overview

This package contains tools for Velodyne 3D laser scanner (tested with
Velodyne HDL-32E). There are three main nodes:

-   **Laserscan Node** - simulates conventional 2D scanner by using data
    from 3D LiDAR.
-   **Groundmap Node** - estimates "safe ground" (i.e. not too rough,
    without high steps and other obstacles) around the robot.
-   **Cloud Assembler Node** - combines several consecutive point clouds
    into a more dense cloud.

Each node has it's nodelet counterpart with same ROS API.

## Installation

From source:

1\. Clone the github repository. 1. Copy the cloned repository into the
'src' folder of your ROS workspace. 1. Recompile your ROS workspace:
\$ catkin_make.

## Laserscan Node

Uses 3D data to simulate conventional 2D scanner. This way, Velodyne
might be used with [move_base](move_base).

![Simulated 2D scanner (green points).\|width=600px](attachment:laserscan.png)

Usage example:



```shell
roslaunch but_velodyne_proc laserscan_node.launch
```



### Topics



```clearsilver
no_header=True
pub {
no_header=True
   0 {
      name= scan_out
      type= sensor_msgs/LaserScan
      desc= simulated 2D scanner output
     }
}
sub {
no_header=True
  0{
     name= points_in
     type= sensor_msgs/PointCloud2
     desc= input 3D cloud
   }
}
```



### Parameters



```clearsilver
no_header=True
param {
no_header=True
  0 {
    name=~frame_id 
    default=`""`
    type= string
    desc= output frame_id (will be same as in input data if not specified)
    }

  1 {
    name=~min_z 
    default=`""`
    type= double
    desc= points under this height will be discarded
    }

  2 {
    name=~max_z 
    default=`""`
    type= double 
    desc= points above this height will be discarded
    }

  3 {
    name=~angular_res
    default=`""`
    type= double
    desc= angular resolution (radians)
    }

  4 {
    name=~min_range
    default=`""`
    type= double
    desc= points closer to the sensor than this will be discarded
    }

}
```



## Groundmap Node

Estimates frame-to-frame *bumpiness* of robot's surrounding and
publishes it as an occupancy grid. This might be used by autonomous
rovers supposed to navigate on a rough terrain.

![Resulting groundmap published as occupancy grid.\|width=600px](attachment:but_velodyne_proc_groundmap.png)

### Topics



```clearsilver
no_header=True
pub {
no_header=True
   0 {
      name= map2d_out
      type= nav_msgs/OccupancyGrid
      desc= 2D map of ''bumpiness''
     }
}
sub {
no_header=True
  0{
     name= points_in
     type= sensor_msgs/PointCloud2
     desc= input 3D cloud
   }
}
```



### Parameters



```clearsilver
no_header=True
param {
no_header=True
  0 {
    name=~map2d_res 
    default=`"0.001"`
    type= double
    desc= resolution of output 2D map
    }

  1 {
    name=~map2d_width 
    default=`"0"`
    type= double
    desc= width of output 2D map
    }

  2 {
    name=~map2d_height 
    default=`"0"`
    type= double 
    desc= height of output 2D map
    }

  3 {
    name=~max_range
    default=`"0"`
    type= double
    desc= points further than ''max_range'' will be skipped
    }

  4 {
    name=~angular_res
    default=`"0.01"`
    type= double
    desc= angular resolution for internal processing
    }

  5 {
    name=~radial_res
    default=`"0.01"`
    type= double
    desc= radial resolution for internal processing
    }

  6 {
    name=~max_road_irregularity
    default=`"0"`
    type= double
    desc= tbd
    }

  7 {
    name=~max_height_diff
    default=`"0"`
    type= double
    desc= tbd
    }

  8 {
    name=~noise_filter
    default=`"true"`
    type= double
    desc= simple filtering of isolated ''occupied'' cells
    }

  9 {
    name=~ground_prob
    default=`""`
    type= double
    desc= tbd
    }

  10 {
    name=~obstacle_prob
    default=`""`
    type= double
    desc= tbd
    }
}
```



## Cloud Assembler Node

When a robot is moving, this node combines few historic clouds and the
current one to produce denser cloud.

![Original cloud.\|width=600px](attachment:cloud_assembler_0.png)

![Output cloud.\|width=600px](attachment:cloud_assembler_1.png)

### Topics



```clearsilver
no_header=True
pub {
no_header=True
   0 {
      name= output
      type= sensor_msgs/PointCloud2
      desc= dense cloud
     }
}
sub {
no_header=True
  0{
     name= /velodyne_points
     type= sensor_msgs/PointCloud2
     desc= input 3D cloud
   }
}
```


