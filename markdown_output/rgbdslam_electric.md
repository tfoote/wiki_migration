## Preamble

This page is about the RGB-D SLAM Version for ROS Electric, i.e. the
subversion repository revisions up to #2924 (checkout via svn co
URL@REVISION. It succeeds our entry at the ROS 3D contest (see
[the contest page](http://www.ros.org/wiki/openni/Contests/ROS%203D)).

See [rgbdslam/evaluation](rgbdslam/evaluation) for instructions on how
to install and evaluate RGB-D SLAM with the
[RGB-D Benchmark Dataset](http://vision.in.tum.de/data/datasets/rgbd-dataset)

## Installation

RGBDSLAM has been developed and tested on Ubuntu 11.10 featuring ROS
electric, but should work on earlier Ubuntus and ROS diamondback with
minor modifications. If you encounter problems, please ask at
[answers.ros.org](http://answers.ros.org/questions/?tags=rgbdslam). Feel
free to send bug fixes, usage reports and suggestions to
endres(at)informatik.uni-freiburg.de.

### Preconditions

The detailed preconditions are:

-   Ubuntu 11.10, 64bit Version (see your `/etc/issue` and the output of
    `uname -m`)
-   ROS electric is installed
-   Qt4 installed as default Qt version (check/change with
    "update-alternatives \--display qmake")
-   Optional: OpenGL Hardware Support, required for visualization and
    SIFTGPU

Installation **should** work with (but hasn't been tested)

-   Ubuntu 11.04 and 10.10
-   ROS diamondback (except ORB features)

If you do not already have a directory for personal ROS packages, create
one like this:

```
mkdir -p ~/ros
echo 'export ROS_PACKAGE_PATH=~/ros:$ROS_PACKAGE_PATH' >> ~/.bashrc
source ~/.bashrc
```

**The remainder of this description assumes you chose /ros/ as your
personal package path.** Otherwise you need to adapt the paths below,
where /ros is contained to fit your directory strucure.

### RGBDSLAM (+ Requirements)

Download RGBDSLAM and g2o to your personal package path:

```
svn co http://alufr-ros-pkg.googlecode.com/svn/trunk/rgbdslam_freiburg/rgbdslam@2924
svn co https://code.ros.org/svn/ros-pkg/stacks/vslam/trunk/g2o ~/ros/g2o
```

Build rgbdslam and g2o. ```
rosmake --rosdep-install rgbdslam
``` This takes quite a time
(20min on an old laptop with core2 cpu T5600 at 1.83GHz). You can
advance to the next section and fetch the benchmark data and tools
meanwhile. Using "export ROS_PARALLEL_JOBS=-jX" with X being the
number of your cpu cors at maximum, will speed the compilation up by a
factor of X, but will need huge amounts of memory (\~ 1GB per core).

If ros dependency resolution failed for your system for some reason, you
might need to install the system dependencies manually:

```
sudo apt-get install libglew1.5-dev libdevil-dev libsuitesparse-dev
``` If this fails and you can not figure out the
solution, please check/ask for solutions at
[answers.ros.org](http://answers.ros.org/questions/?tags=rgbdslam).

Optionally, you might want to install perception_pcl_addons (debian
package: ros-diamondback-perception-pcl-addons) which includes
pcd_viewer, a viewer for the file format used by RGBDSLAM to store
registered point clouds. If you want to process the point cloud you can
save to a ply file and use meshlab (debian-package: meshlab).

## Usage

To start RGBDSLAM launch

```
roslaunch rgbdslam kinect+rgbdslam.launch
``` Alternatively you can start the openni nodes
and RGBDSLAM separately, e.g.:

```
roslaunch openni_camera openni_node.launch
rosrun rgbdslam rgbdslam
``` To capture models either press space to start
recording a continuous stream or press enter to record a single frame.
To reduce data redundancy, sequential frames from (almost) the same
position are not included in the final model. The 3D visualization
always shows the globally optimized model. Neighbouring points are
triangulated except at missing values and depth jumps.

### Octomaps

To generate octomaps from the registered point clouds you need to
install the octomap stacks. The easiest way (for non-colored octomaps)
ist to install from the debian repositories: ```
sudo apt-get install ros-electric-octomap-mapping ros-electric-octomap-visualization
```

Generating Colored Octomap requires the experimental version of the
[octomap stack](http://www.ros.org/wiki/octomap) to be installed.

-   Checkout and compile the experimental version of the octomap stack:

```
svn co http://alufr-ros-pkg.googlecode.com/svn/branches/octomap_mapping-experimental/
```

-   Start rgbdslam as described above, capture a scene
-   Execute `roslaunch rgbdslam octomap_server.launch`
-   In rgbdslam select \*Graph->Send Model\* (or press Ctrl+M)
-   Execute `rosrun octomap_server octomap_saver <filename.bt>`

The parameters in octomap_mapping.launch allow for some fine-tuning of
resolution and sensor range. You can use `rosrun octovis octovis
<filename.bt>` to view the octomap.

## Common Issues

Here are some known issues:

1\. If you have issues compiling, make sure you removed any older
version of RGBDSLAM from your \$ROS_PACKAGE_PATH 1. RGBDSLAM needs
electric or diamondback. Make sure that neither your \$PATH nor
\$ROS_PACKAGE_PATH contains "boxturtle", "cturtle" or
"unstable". 1. If you want to use rgbdslam with **fuerte** have a look
at
[answers.ros.org](http://answers.ros.org/questions/scope:all/sort:activity-desc/tags:rgbdslam/page:1/),
where some people describe how they successfully made it run on
fuerte. 1. If you are located in Germany and get errors loading the
saved ply files into meshlab, try switching to U.S. locale or replace
the decimal point with a comma in your .ply file 1. To speed up compile
times consider to use "export ROS_PARALLEL_JOBS=-j<#cpus>" before
rosmake, but you should have lots of memory as gcc may take up to 2GB
for four parallel jobs. 1. If the rosmake process fails with error
"fatal error: gsl/gsl_linalg.h: No such file" you will need to install
libgsl "sudo apt-get install gsl-bin libgsl0-dev"

## Further Information

\...can be found in the README file in the RGBDSLAM package.

## Publications

Nikolas Engelhard and Felix Endres and Jürgen Hess and Jürgen Sturm and
Wolfram Burgard, **"Real-time 3D visual SLAM with a hand-held RGB-D
camera"**, Proc. of the *RGB-D Workshop on 3D Perception in Robotics at
the European Robotics Forum*, Vasteras, Sweden, 2011.
[pdf](http://vision.in.tum.de/_media/spezial/bib/engelhard11euron.pdf)

```
@InProceedings{ engelhard11euron-workshop,
    TITLE = "Real-time 3D visual SLAM with a hand-held RGB-D camera",
    AUTHOR = "Nikolas Engelhard and Felix Endres and J{\"u}rgen Hess and J{\"u}rgen Sturm and Wolfram Burgard",
    BOOKTITLE = "Proc. of the RGB-D Workshop on 3D Perception in Robotics at the European Robotics Forum",
    ADDRESS = "Vasteras, Sweden",
    YEAR = "2011",
    MONTH = "April",
}
```

Felix Endres and Jürgen Hess and Nikolas Engelhard and Jürgen Sturm and
Daniel Cremers and Wolfram Burgard, **"An Evaluation of the RGB-D SLAM
System"**, In the Proc. of the International Conference on Robotics and
Automation (ICRA) 2012.
[pdf](http://vision.in.tum.de/_media/spezial/bib/endres12icra.pdf)

```
@InProceedings{endres12icra,
author={F. Endres and J. Hess and N. Engelhard and J. Sturm and D. Cremers and W. Burgard},
title={An Evaluation of the {RGB-D SLAM} System},
	booktitle = "Proc. of the IEEE Int. Conf. on Robotics and Automation (ICRA)",
address={St. Paul, MA, USA},
month={May},
year={2012}
}
```
