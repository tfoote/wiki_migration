This package is meant to be a simple stub for use in the NIST Solutions
in Perception contest.

# Install

## Prerequisites

First, make sure that you have installed the Diamondback release of ROS

-   <http://www.ros.org/wiki/diamondback/Installation/Ubuntu>

Then, verify that you have rosinstall :

-   <http://www.ros.org/wiki/rosinstall>

Also please make sure that you install:

-   The openni kinect drivers - <http://www.ros.org/wiki/openni_kinect>



```
sudo apt-get install ros-diamondback-openni-kinect
```



-   pcl_visualization - <http://www.ros.org/wiki/perception_pcl_addons>



```
sudo apt-get install ros-diamondback-perception-pcl-addons
```



## install tod_stub

Now, open a terminal and create a directory to work in. We'll use
rosinstall to setup a directory that has all the dependencies. The
following will install everything you need to get started in you.

The following line will install everything in under the path:
`~/tod_stub_dev`



```
rosinstall ~/tod_stub_dev https://code.ros.org/svn/wg-ros-pkg/branches/trunk_diamondback/stacks/object_recognition/tod_stub/tod_stub.install
```



-   You must then source `setup.bash` in /tod_stub_dev either "by
    hand" or put `source ~/tod_stub_dev/setup.bash` in your `.bashrc`
    file.

That just installed:

-   **tod_stub** - The code you'll be working with directly.
-   **tod_core** - Core Textured Object Recognition library.
-   **tod_training** - Textured Object Training library.
-   **vision_bleeding** - misc vision algorithms 3

------------------------------------------------------------------------

# For CS324 Class, use of fiducial tracking:

"Fiducial" will become your perception code stub as it connects with
OpenCV, PCL and the kinect camera. So:

-   `roscd fiducial`

Print out the calibration fiducial pattern in `data/5x3.svg`

Check that everything runs: 1. plug in a kinect camera 1. Open up 4
terminals (or 4 tabs in one terminal) 1. In the first, run `roscore` 1.
In the second, run `roslaunch openni_camera openni_node.launch ` 1. In
the third, go to the data directory `roscd fiducial/data`

-   We go to this directory because that's where the `fiducial.yml`
    file is.
-   Otherwise, you may append the argument
    `--fiducial data/fiducial.yml`
-   Then: `rosrun fiducial pose_estimator camera:=/camera/rgb` 1. In the
    forth window, to view all this: `rosrun rviz rviz`
-   Set rviz settings as follows: . ![](attachment:fiducial_rviz.jpg)

```{=html}
<!-- -->
```
-   You can run `rosrun fiducial pose_estimator camera:=/camera/rgb `
    with other options (*append \--help to get these options*):
-   Append `--use_3d` To use 3D information for pose fitting instead of
    OpenCV's `solvePNP()`.
-   3D information is more accurate since small differences in 2D
    estimation of points can cause large pose differences.
-   Append `--verbose` To show an OpenCV window tracking the chessboard
-   Both options may be used together
