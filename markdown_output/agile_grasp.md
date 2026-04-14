## Overview

This package localizes antipodal grasps in 3D point clouds.
\'\'\'AGILE\'\'\' stands for \'\'\'A\'\'\'ntipodal \'\'\'G\'\'\'rasp
\'\'\'I\'\'\'dentification and \'\'\'LE\'\'\'arning. The reference for
this package is:
[Using Geometry to Detect Grasps](http://www.ccs.neu.edu/home/atp/publications/grasp_poses_isrr2015.pdf).

The package already comes with pre-trained machine learning classifiers
and can be used (almost) out-of-the-box, in particular with an \'\'Asus
Xtion Pro\'\' range sensor.

[Youtube](https://www.youtube.com/watch?v=Dm64UC3uGVY)

For a complete \'\'\'grasping demo\'\'\' on a Baxter robot, check out
our [grasp_selection](http://github.com/atenpas/grasp_selection)
package.

The package contains two command line tools and one ROS node:

1\. \'\'\'train_svm:\'\'\' (command line tool) Train an SVM to localize
grasps in point clouds. 1. \'\'\'test_svm:\'\'\' (command line tool)
Localize grasps in a \'\'.pcd\'\' file using a trained SVM. 1.
\'\'\'find_grasps:\'\'\' (ROS node) Localize grasps in a point cloud
obtained from a range sensor.

## Requirements

1\. [Lapack](http://www.netlib.org/lapack/) (install in Ubuntu: \`\$
sudo apt-get install liblapack-dev\`) 1.
[OpenNI](http://wiki.ros.org/openni_launch) or a similar range sensor
driver

## Installation

### From Source, ROS Indigo

1\. Open a terminal 1. Navigate to the \*src\* folder of your ROS
workspace: \`\$ cd location_of_workspace/src\` 1. Clone the repository:
\`\$ git clone <https://github.com/atenpas/agile_grasp.git>\` 1.
Navigate back to the root of your ROS workspace: \`\$ cd ..\` 1.
Recompile your ROS workspace: \`\$ catkin_make\`

### From Source, ROS Hydro

Follow the instructions for ROS Indigo, except for Step (3):

`$ git clone https://github.com/atenpas/agile_grasp.git -b hydro`

## Localize Grasps with a Robot

Localize grasps on a robot using a range sensor, such as a Kinect:

`$ roslaunch agile_grasp single_camera_grasps.launch`

![Localize grasps on a robot\|height=\"360\",width=\"640\"](https://raw.githubusercontent.com/atenpas/agile_grasp/master/readme/vlc1.png)

Two example ROS launch files, \'\'single_camera_grasps.launch\'\' and
\'\'baxter_grasps.launch\'\', are provided that illustrate how to use
the \'\'\'find_grasps\'\'\' ROS node to localize grasps in a point cloud
obtained from one or two range sensors.

### Instructions for Asus Xtion Pro

1\. Start roscore: \`\$ roscore\` 1. Connect an Asus Xtion Pro range
sensor 1. Launch the Asus ROS driver: \`\$ roslaunch openni2_launch
openni2.launch\` 1. Detect grasps: \`\$ roslaunch agile_grasp
single_camera_grasps.launch\` 1. Start Rviz for visualization: \`\$
rosrun rviz rviz\` 1. Open the config file
\'\'agile_grasp/rviz/single_camera.rviz\'\' in Rviz to visualize the
grasps.

### Launch File Parameters

The most important parameters to increase the number of grasps found are
\'\'num_samples\'\' and \'\'workspace\'\'. A higher sample number means
that a larger subset of points in the point cloud will be considered. A
smaller workspace means that less samples are required to find grasps.

The most important parameters are listed below.

-   cloud_topic: the topic where the input point cloud is published
-   cloud_frame: the frame associated with the input point cloud
-   cloud_type: the cloud type (0:
    [sensor_msgs/PointCloud2](http://docs.ros.org/api/sensor_msgs/html/msg/PointCloud2.html),
    1:
    [agile_grasp/CloudSized](http://docs.ros.org/indigo/api/agile_grasp/html/msg/CloudSized.html))
-   svm_file_name: the location of the file containing the SVM
    classifier
-   num_samples: the number of samples used to localize grasps
-   num_threads: the number of CPU threads used
-   num_clouds: the number of input point clouds
-   workspace: the workspace limits (a box with the center at the
    origin; \[minX, maxX, minY, maxY, minZ, maxZ\])
-   camera_pose: the pose of the camera that produces the input point
    cloud (not required)
-   min_inliers: the minimum number of grasps required to form a cluster
-   plotting: what kind of visualization is used (0: none, 1: PCL, 2:
    Rviz)
-   marker_lifetime: the lifetime of visual markers in Rviz

\'\'\'Remark\'\'\': If you want to adjust the grasp parameters, you can
do this from the launch file. For the available parameters, see
\'\'src/nodes/find_grasps.cpp\'\'.

## Localize Grasps in a Point Cloud File

Localize grasps in a point cloud stored in a \'\'.pcd\'\' file:

`$ rosrun agile_grasp test_svm /home/userABC/data/input.pcd /home/userABC/ros_ws/src/agile_grasp/svm_032015_20_20_same`

![input](https://raw.githubusercontent.com/atenpas/agile_grasp/master/readme/2view_50r.png)
![output\|height=\"225\",width=\"640\"](https://raw.githubusercontent.com/atenpas/agile_grasp/master/readme/output.png)

### Usage

`$ rosrun agile_grasp test_svm pcd_filename svm_filename [num_samples] [num_threads] [min_handle_inliers]`

This localizes grasps in the point cloud file \'\'pcd_filename\'\' using
the SVM stored in the file \'\'svm_filename\'\'. The last three
parameters are optional. \'\'num_samples\'\' sets the number of samples,
\'\'num_threads\'\' sets the number of CPU threads used, and
\'\'min_handle_inliers\'\' sets the minimum number of grasps required to
have a cluster of grasps.

\'\'\'Notice:\'\'\' When no handles or not enough antipodal grasps are
found, please increase the \'\'num_samples\'\' parameter. Another option
is to modify the workspace limits in \'\'src/nodes/test.cpp\'\' (this
requires recompiling the code).

![output\|height=\"225\",width=\"640\"](https://raw.githubusercontent.com/atenpas/agile_grasp/master/readme/pcl_vis.png)

### Parameters

-   pcd_filename: the location plus name of the .pcd file that is
    searched for grasps
-   svm_filename: the location plus name of the file that contains the
    SVM model
-   num_samples: (optional) the number of samples used by the grasp
    search
-   num_threads: (optional) the number of CPU used by the grasp search
-   min_handle_inliers: (optional) the minimum number of grasps required
    to form a cluster

## Training the SVM

To train the SVM to predict grasps, first create a directory that
contains the \'\'.pcd\'\' files used for training.

### Method A

\'\'\'Preparations:\'\'\'

-   Each point cloud file needs to be called \'\'obji.pcd\'\' where
    \'\'i\'\' goes from \'\'0\'\' to \'\'num_files\'\'
-   \'\'pcd_directory\'\' is the location of the directory plus the root
    name of the training files, e.g., \'\'/home/userA/data/obj\'\'.

\'\'\'Training:\'\'\'

`$ rosrun agile_grasp train_svm num_files pcd_directory/obj svm_filename [plots_hands] [num_samples] [num_threads]`

### Method B

\'\'\'Preparations:\'\'\'

-   Set \'\'num_files\'\' to 0.
-   Provide a \'\'files.txt\'\' text file within \'\'pcd_directory\'\'
    that lists all file names that are used for training, and a
    \'\'workspace.txt\'\' that lists the workspace dimensions for each
    file.

\'\'\'Example: files.txt\'\'\'

```
file1
file2
...
``` \'\'\'Example: workspace.txt\'\'\'

```
file1
file2
...
``` \'\'\'Training\'\'\'

`$ rosrun agile_grasp train_svm num_files pcd_directory svm_filename [plots_hands] [num_samples] [num_threads]`

### Parameters

-   num_files: the number of files within \'\'pcd_directory\'\'
-   pcd_directory: the location of the directory plus the root name of
    the \'\'.pcd\'\' files used for training
-   svm_filename: the location plus name of the file that will store the
    SVM model
-   plots_hands: (optional) whether the grasps found are visualized
-   num_samples: (optional) the number of samples used by the grasp
    search
-   num_threads: (optional) the number of CPU used by the grasp search

## Citation

If you like this package and use it in your own work, please cite our
[ISRR2015 paper](http://www.ccs.neu.edu/home/atp/publications/grasp_poses_isrr2015.pdf):

Andreas ten Pas and Robert Platt. \'\'\'Using Geometry to Detect Grasp
Poses in 3D Point Clouds.\'\'\' International Symposium on Robotics
Research (ISRR), Italy, September 2015.
