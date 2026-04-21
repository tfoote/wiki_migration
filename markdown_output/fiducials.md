## Overview

This package provides a system that allows a robot to determine its
position and orientation by looking at a number of fiducial markers
(similar to QR codes) that are fixed in the environment of the robot.
Initially, the position of one marker is specified, or automatically
determined. After that, a map (in the form of a file of 6DOF poses) is
created by observing pairs of fiducial markers and determining the
translation and rotation between them.

## How it works

The Ubiquity Robotics localization system uses a number of fiducial
markers of known size to determine the robot's position. Detection of
the markers is done by the
[aruco_detect node](http://wiki.ros.org/aruco_detect). For each marker
visible in the image, a set of vertices in image coordinates is
produced. Since the *intrinsic parameters* of the camera and the size of
the fiducial are known, the pose of the fiducial relative to the camera
can be estimated. Note that if the camera intrinsics are not known, they
can be determined using the process described in the
[camera calibration tutorial](https://github.com/UbiquityRobotics/raspicam_node/#calibration).

The diagram below shows the coordinate system of a fiducial marker,
which has a length of *2d*. The image coordinates *(x, y)* of each
vertex correspond to a ray from the camera. The pose estimation code
solves a set of linear equations to determine the world *(X, Y, Z)*
coordinate of each of the vertices. From this, we obtain the
\*transform\* of the fiducial's coordinate system to the camera's
coordinate system *`T_fid_cam`*. This represents the \*pose\* of the
marker in the camera's coordinate system. Since we know the camera's
pose in the coordinate system of the robot,c image. In the diagram
below, two fiducials, *fid1* and *fid2* are shown. If *fid1* is at a
known pose in the world, *`T_map_fid1`* and we know the marker to
camera transforms for both markers, we can compute the pose of *fid2*
thus:

*`T_map_fid2` = `T_map_fid1` \* `T_cam_fid2` \* `T_fid1_cam`*

In this way, the map is built up as more fiducial pairs are observed.
multiple observations are combined with weighting, to produce an
estimate of the 6DOF pose of each fiducial marker.

![\|width="300px"](attachment:two_fiducials.png)

## Getting Started

A camera is required, and it is necessary to know the position of the
camera relative to the robot's `base_link`. Software for the
Raspberry Pi is available at:

<https://github.com/UbiquityRobotics/raspicam_node>

To install the fiducial software from binary packages:



```
sudo apt-get install ros-kinetic-fiducials
```



Fiducial markers can be generated with a command like this:



```
rosrun aruco_detect create_markers.py 100 112 fiducials.pdf
```

 Once printed, they can be affixed to the
environment. They don't need to be placed in any particular pattern but
the density should be such that two or more markers can be seen by the
camera on the robot, so the map can be built. Placing them on the
ceiling reduces problems with occlusion, but is not required, since a
full 6DOF pose is estimated.

Two nodes should be run, [aruco_detect](aruco_detect), which handles the
detection of the fiducials, and [fiducial_slam](fiducial_slam), which
combines the fiducial pose estimates and builds the map and makes an
estimate of the robot's position. The map is in the form of a text file
specifying the 6DOF pose of each of the markers, and is automatically
saved.

There are launch files for both of these nodes:



```
roslaunch aruco_detect aruco_detect.launch
roslaunch fiducial_slam fiducial_slam.launch
```



A launch file is also provided to visualize the map in [rviz](rviz).


```
roslaunch fiducial_slam fiducial_rviz.launch
```



This will produce a display as shown below. The bottom left pane shows
the current camera view. This is useful for determining if the fiducial
density is sufficient. The right-hand pane shows the map of fiducials as
it is being built. Red cubes represent fiducials that are currently in
view of the camera. Green cubes represent fiducials that are in the map,
but not currently in the view of the camera. The blue lines show
connected pairs of fiducials that have been observed in the camera view
at the same time. The robustness of the map is increased by having a
high degree of connectivity between the fiducials. If the mapping is
working, the spatial layout of the fiducials in the map will match the
layout of the physical markers.

### Automatic Map Initialization

If the map is empty, then it will auto-initialize when a fiducial is
visible. The auto-initialization calculates the pose of the nearest
fiducial in the `map` frame, such that `base_link` of the robot is
at the origin of `map`. For best results, this should be done with the
robot stationary.

### Clearing the Map

The map can be cleared with the following command:



```
rosservice call /fiducial_slam/clear_map
```



After this command is issued, the map can be auto-initialized, as
described above.

![\|width="750px"](attachment:fiducial_rviz.png)
