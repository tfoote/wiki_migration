## Overview

This package allows to localize handles in 3D point clouds. The video
below demonstrates the method in a scenario where a robot has to pick up
objects from a table and deposit them into a box.

[Youtube](https://www.youtube.com/watch?v=qjE5X7pTjKE)

If you like this package and use it in your own work, please cite our
[ISER2014 paper](http://www.ccs.neu.edu/home/atp/publications/affordances_iser2014_final.pdf).

## Requirements

1\. [ROS Hydro](http://wiki.ros.org/hydro), ROS Indigo, or ROS
Kinetic 1. Lapack (install in Ubuntu using: sudo apt-get install
liblapack-dev) 1. [Openni_launch](http://wiki.ros.org/openni_launch)
(install in Ubuntu using: sudo apt-get install
ros-<ROS_VERSION>-openni-launch)

## Installation

### Ubuntu

1\. sudo apt-get install ros-hydro-handle-detector 1. source
/opt/ros/hydro/setup.bash

### From Source

1\. Cd into the 'src' folder of your catkin workspace. 1. Clone the
github repository. 1. Recompile your ROS workspace: \$ catkin_make.

## How to Localize Handles

There are two ways in which handles can be localized using this package:
from a \*.pcd file that contains the point cloud data, or from the point
cloud data provided by a depth sensor such as an RGB-D camera, e.g.,
Microsoft Kinect.

### Using a Point Cloud File

1\. Set the parameter 'file' in
handle_detector/launch/localization_pcd_file.launch to the absolute path
of some pcd file. 1. Start roscore: \$ roscore. 1. Run the handle
localization: \$ roslaunch handle_detector
localization_pcd_file.launch. 1. Use RViz to visualize the results (see
below): \$ rosrun rviz rviz.

For the given point cloud file (*handle_detector/data/table5.pcd*), the
output in rviz should look like this:

![Output for PCD file\|width="340"](attachment:handles_pcd.png)

### Using a Depth Sensor

**Note:** This requires an openni-compatible device, and has only been
tested with an Asus Xtion Pro.

1\. Set-up one or more objects in front of the RGB-D camera, and have
the RGB-D camera running. 1. Start roscore: \$ roscore. 1. Start
openni_launch: \$ roslaunch openni_launch openni.launch. 1. Run the
handle localization: \$ roslaunch handle_detector
localization_sensor.launch. 1. Use RViz to visualize the results (see
below): \$ rosrun rviz rviz.

## Grasp Handles Using Localization Information

1\. Follow the steps described in (4.1) or (4.2). 1. Subscribe to the
ROS topic /localization/handle_list to get a list of handles. 1. This
list gives the pose, radius, extent, major axis, and normal axis for
each affordance (cylindrical shell) in every handle. 1. To see the
structure of the messages published here, use: \$ rosmsg show
handle_detector/nameOfMessage. 1. Use the given localization information
to decide for a target handle, and grasp it using your robot.

## Visualization in RViz

There are ready-to-use configuration files in the rviz folder.

1\. Show input point cloud: add a PointCloud2 and set the topic to
/localization/point_cloud. 1. Show all affordances: add a MarkerArray
and set the topic to /localization/visualization_all_affordances. 1.
Show all handles: add a MarkerArray and set the topic to
/localization/visualization_all_handles. 1. Show handle i (i = 0, 1,
\...): add a MarkerArray and set the topic to
/localization/visualization_handle_i.

![alt text\|height="240",width="320"](http://www.ccs.neu.edu/home/atp/images/stagedcleaning8.png)
![alt text\|height="240",width="320"](http://www.ccs.neu.edu/home/atp/images/handle_visualization.png)

## Commands

-   Run handle localization on a \*.pcd file: \$ roslaunch
    handle_detector localization_pcd_file.launch
-   Run handle localization on range sensor input: \$ roslaunch
    handle_detector localization_sensor.launch
-   Run handle localization with importance sampling on a \*.pcd file:
    \$ roslaunch handle_detector importance_sampling_pcd_file.launch

## Published ROS Topics

-   **/localization/cylinder_list:** contains a list of cylinders
    (affordances) with pose, radius, extent, major axis, and normal
    axis.
-   **/localization/handle_list:** contains a list of handles where each
    handle consists of a list of cylinders (affordances).

## ROS Launch Parameters

### Affordance Localization

file:: the location of the \*.pcd file on the file system (absolute
path) target_radius:: the radius of the target handle
target_radius_error:: the error permitted on the target radius
affordance_gap:: the size of the gap around the affordance sample_size::
the number of point neighborhoods to be sampled from the point cloud
use_clearance_filter:: whether the clearance filter (enough gap around
affordance) is used use_occlusion_filter:: whether the occlusion filter
is used curvature_estimator:: the method that is used to estimate
curvature (0: Taubin Quadric Fitting, 1: Principal Component Analysis,
2: Normals) point_cloud_source:: the source of the point cloud (0:
\*.pcd file, 1: range sensor) update_interval:: the interval in seconds
at which the algorithm is repeated workspace_limits (6 parameters):: the
minimum and maximum values of the workspace in three dimensions
num_threads:: the number of CPU threads to use in Taubin Quadric Fitting

### Handle Localization

alignment_runs:: the number of times that handles are searched for
alignment_min_inliers:: the minimum number of aligned affordances in a
handle alignment_dist_radius:: the axis distance below which two
affordances are considered to belong to the same handle
alignment_orient_radius:: the orientation distance below which two
affordances are considered to belong to the same handle
alignment_radius_radius:: the radius difference below which two
affordances are considered to belong to the same handle

### Importance Sampling

The following parameters are only required if the importance sampling is
launched.

num_iterations:: the number of iterations for which the search is
repeated num_samples:: the number of samples used per iteration
num_init_samples:: the number of initial samples sampling_method:: the
method that is used for drawing samples from the cloud (Sum of Gaussians
or Maximum of Gaussians) visualize_steps:: whether each iteration is
visualized (uses pcl_viewer)

## Citation

If you like this package and use it in your own work, please cite our
[ISER2014 paper](http://www.ccs.neu.edu/home/atp/publications/affordances_iser2014_final.pdf):

Andreas ten Pas and Robert Platt. **Localizing Handle-Like Grasp
Affordances in 3-D Points Clouds Using Taubin Quadric Fitting.**
International Symposium on Experimental Robotics (ISER), Morocco, June
2014.
