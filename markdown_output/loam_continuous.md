![](attachment:maps.jpg)

```wiki
The code has been removed from the public domain. The technology is available as commercial produces from [[http://www.kaarta.com|Kaarta]].
```

## Overview

Laser Odometry and Mapping (Loam) is a realtime method for state
estimation and mapping using a 3D lidar. The program contains two major
threads running in parallel. An \"odometry\" thread computes motion of
the lidar between two sweeps, at a higher frame rate. It also removes
distortion in the point cloud caused by motion of the lidar. A
\"mapping\" thread takes the undistorted point cloud and incrementally
builds a map, while simultaneously computes pose of the lidar on the map
at a lower frame rate. The lidar state estimation is combination of the
outputs from the two threads.

If an IMU is available, the orientation (integrated from angular rate)
and acceleration measurements are used to deal with general motion of
the lidar, while the program takes care of the linear motion.

The program is tested on a laptop with 2.5 GHz quad cores and 6 Gib
memory (the program consumes two cores). It uses a continuous spin lidar
(see following figure). Another two versions of the program using a
[back and forth spin lidar](http://wiki.ros.org/loam_back_and_forth) and
a [Velodyne lidar](http://wiki.ros.org/loam_velodyne) are available.

![](attachment:lidar2.jpg)

## Usage

To run the program, users need to download the code from
[GitHub](https://github.com/jizhang-cmu/loam_continuous), or follow the
link on the top of this page. The program can be started by ROS launch
file (available in the downloaded folder), which starts four nodes and
rivz:

```
roslaunch loam_continuous.launch
```

Datasets are available for download at the bottom of this page. Please
make sure the data files are for the continuous spin version (not back
and forth spin or Velodyne version). With the program running (from the
launch file), users can play the data file:

```
rosbag play data_file_name.bag
```

Note that if a slow computer is used, users can try to play the data
file at a low speed, e.g. play the data file at half speed:

```
rosbag play data_file_name.bag -r 0.5
```

## Datasets

[Robot city bridge](https://drive.google.com/open?id=1uXl5mgWLGCWewN8Q6Zquwv7S7dbGslWP)
([Video](https://drive.google.com/open?id=1fK1Yey1uWg6XARYGfBAi2Dr-d3mmWz5m)):
mapping a bridge with an UAV

![](attachment:robot_city_bridge.jpg)

## References

[J. Zhang](https://frc.ri.cmu.edu/~zhangji/) and
[S. Singh](https://frc.ri.cmu.edu/~ssingh/Sanjiv_Singh/home.html). LOAM:
Lidar Odometry and Mapping in Real-time. Robotics: Science and Systems
Conference (RSS). Berkeley, CA, July 2014.

## More Info

[Research videos](http://www.youtube.com/channel/UCEEqrCpT8lnp0q1HBzS3rtQ?feature=watch)
[Kaarta](http://www.kaarta.com/)
