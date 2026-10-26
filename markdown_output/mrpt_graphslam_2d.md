## Description

mrpt_graphslam_2d provides support for running either single-robot or
multi-robot pose-only graphSLAM, using simulated data (e.g. from Gazebo)
or in a real-time setup. Algorithm practically utilises the
[mrpt-graphslam library](http://reference.mrpt.org/devel/group__mrpt__graphslam__grp.html)
to execute graphSLAM, using the ROS communication mechanisms and the
[multimaster_fkie](http://wiki.ros.org/multimaster_fkie) stack.

## Usage Information

Information on how to use the algorithm for either simulation or
real-time usage is provided in the Appendix of
[this document](http://controlsystemslab.gr/code/bergercookie/mr-slam-thesis-text/src/master/report.pdf)

### Running real-time graphSLAM

Additional support for running real-time graphSLAM with either one or
with multiple agents is provided in the
[csl_hw_setup](https://github.com/bergercookie/csl_mr_slam/tree/master/csl_hw_setup)
ROS package. The latter provides launchfiles and generic scripts for
setting up common tasks in real robot agents (setting up sensor data
acquisition processes, processes for starting robot motors etc.) Package
is specialized for the robots and equipment of the
[Control Systems Lab](https://controlsystemslab.gr) of the
[National Technical University of Athens](https://www.ntua.gr/en/) but
can be easily extended to suppport different platforms, sensors etc.

### Running multi-robot simulations in Gazebo

Additional support for running simulations in Gazebo is provided in the
[csl_robots_gazebo](https://github.com/bergercookie/csl_mr_slam/tree/master/csl_robots_gazebo)
ROS package

## Demos

### Demo videos

Following is a list of demo videos that showcase the algorithm
capabilities both in simulations as well as real-time experiments:

#### Single-robot MRPT graphslam-engine

[Youtube](https://www.youtube.com/watch?v=Pv0yvlzrcXk)

#### Multi-robot simulation in Gazebo

[Youtube](https://www.youtube.com/watch?v=4RKS2jrvsYE)

#### Multi-robot real-time experiment

See
[here](https://www.dropbox.com/s/zm2njljeprnsfaf/20170426_mr_graphslam_real_2.mp4?dl=0)

### Running provided demos

Package also contains sample datasets, along with the corresponding
roslaunch files for easy execution, for both the single- and multi-robot
SLAM cases. For more on this see the
[package README](https://github.com/mrpt-ros-pkg/mrpt_slam/blob/master/mrpt_graphslam_2d/README.md).

## API Documentation

Use the `rosdoc_lite` tool to generate the complete API of this
package:

## Relevant Links

- [MRPT graphslam-engine application](http://www.mrpt.org/list-of-mrpt-apps/application-graphslamengine/)

<!-- -->

- [MRPT graphslam-lib](http://reference.mrpt.org/devel/group__mrpt__graphslam__grp.html)

<!-- -->

- [Multi-robot graphSLAM diploma thesis PDF](http://controlsystemslab.gr/code/bergercookie/mr-slam-thesis-text/src/master/report.pdf)
