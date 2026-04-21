```wiki
The code has been removed from the public domain. The technology is available as commercial produces from [[http://www.kaarta.com|Kaarta]].
```

## Overview

Depth Enhanced Monocular Odometry (Demo) is a monocular visual odometry
method assisted by depth maps. The program contains three major threads
running parallel. A "feature tracking" thread extracts and tracks
Harris corners by Kanade Lucas Tomasi (KLT) feature tracker. A "visual
odometry" thread computes frame to frame motion using the tracked
features. Features associated with depth (either from the depth map or
triangulated from previously estimated camera motion) are used to solve
the 6DOF motion, and features without depth help solve orientation. A
"bundle adjustment" thread refines the estimated motion. It processes
sequences of images received within certain amount of time using
Incremental Smoothing and Mapping
([iSAM](http://people.csail.mit.edu/kaess/isam/)) open source library.

If an IMU is available, the orientation measurement (integrated from
angular rate and acceleration) is used to correct roll and pitch drift,
while the VO handles yaw and translation.

The program is tested on a laptop with 2.5 GHz quad cores and 6 Gib
memory. It uses a camera and point cloud perceived by a 3D lidar (see
following figure). Another version of the program using an RGBD camera
is available [here](http://wiki.ros.org/demo_rgbd).

![](attachment:camera_lidar.jpg)

## Usage

To run the program, users need to install packages required by the iSAM
library, used by the bundle adjustment:

```
sudo apt-get install libsuitesparse-dev libeigen3-dev libsdl1.2-dev
```

Code can be downloaded from
[GitHub](https://github.com/jizhang-cmu/demo_lidar), or following the
link on the top of this page. The program can be started by ROS launch
file (available in the downloaded folder), which runs the VO and rivz:

```
roslaunch demo_lidar.launch
```

Datasets are available for download at the bottom of this page. Please
make sure the data files are for the camera and lidar (not RGBD camera)
version. With the program running (from the launch file), users can play
the data file:

```
rosbag play data_file_name.bag
```

Note that if a slow computer is used, users can try to play the data
file at a low speed, e.g. play the data file at half speed:

```
rosbag play data_file_name.bag -r 0.5
```

## Datasets

[NSH West no IMU](https://drive.google.com/open?id=1RTQusHWtoTsb723p_-rgOyuG8ZMqc5dU)([Video](https://drive.google.com/open?id=1TKsyju-fJhd1uKnIWbar2SI4J3RQ4vBb)):
visual odometry without using IMU

![](attachment:nsh_west_no_IMU.jpg)

[NSH West with IMU](https://drive.google.com/open?id=1m1C2SN-tShY-vgaYAAFu3xAxH5feaOEl)([Video](https://drive.google.com/open?id=1vVwoLDQ8BTk5Eb_sB_W1K-qjoTaZ20Bc)):
visual odometry assisted by IMU

![](attachment:nsh_west_with_IMU.jpg)

## Notes

Camera intrinsic parameters (K and D matrices) are defined in the
"src/cameraParameters.h" file.

It is possible to accelerate feature tracking with a GPU. To do this,
simply replace the "src/featureTracking.cpp" file with the
"src/featureTracking_ocl.cpp" file and recompile. We use OpenCL to
communicate with the GPU. Users first need to install OpenCL in a
version no earlier than 1.1 with full profile, then install OpenCV using
CMake with flag WITH_OPENCL=ON.

## References

[J. Zhang](https://frc.ri.cmu.edu/~zhangji/),
[M. Kaess](https://frc.ri.cmu.edu/~kaess/), and
[S. Singh](https://frc.ri.cmu.edu/~ssingh/Sanjiv_Singh/home.html).
Real-time Depth Enhanced Monocular Odometry. IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS). Chicago, IL, Sept.
2014.

## More Info

[Research videos](http://www.youtube.com/channel/UCEEqrCpT8lnp0q1HBzS3rtQ?feature=watch)
[Kaarta](http://www.kaarta.com/)
