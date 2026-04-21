This page describes the RGB-D SLAM system for ROS Fuerte. **There is a
successor**, `rgbdslam_v2` for** ROS Hydro and Indigo**. See
[README](https://github.com/felixendres/rgbdslam_v2/blob/indigo/README.md).

For the electric version and many details that still hold true, see
[this page](rgbdslam_electric).

# Download and Installation

If you are not a ROS user yet, follow the instructions at the bottom of
this page.

Download rgbdslam with the following command to your
[ros workspace](ROS/Tutorials/InstallingandConfiguringROSEnvironment).

```
svn co http://alufr-ros-pkg.googlecode.com/svn/trunk/rgbdslam_freiburg
```
**`'ROS needs to be aware of the folder into which you download rgbdslam_freiburg! Make sure that the folder containing rgbdslam_freiburg is in your ROS_PACKAGE_PATH (see [[ROS/Tutorials/InstallingandConfiguringROSEnvironment|ros workspace]] for how to modify the ROS_PACKAGE_PATH. It is a bad idea to put rgbdslam_freiburg into /opt/ros/fuerte/...). If properly configured  "roscd rgbdslam" will take you to the rgbdslam package directory`**'

If not yet installed, install [rosdep](rosdep) first, then execute

```
rosdep update
rosdep install rgbdslam_freiburg
``` This should take care of all system
dependencies (e.g. libg2o, octomap).

You can then compile it with

```
rosmake rgbdslam_freiburg
``` which will take a while. If you encounter
problems, here is an example
[build logfile](attachment:example_rgbdslam_build_output.log) for a
successful build for reference (Revision 3949).

As mentioned in [rgbdslam_electric](rgbdslam_electric), if ROS
dependencies are still not met for some reason, you might need to
install the following dependencies

```
sudo apt-get install libglew1.5-dev libdevil-dev libsuitesparse-dev
```

# Configuration

There are several example launch-files that set the parameters of RGB-D
SLAM for certain use cases, a complete list of all options and their
current settings can be found in the GUI: "Settings"->"View Current
Settings". For a definitive list of all settings and the default values
have a look at their quite readable definition in
src/parameter_server.cpp.

I am still adapting the various use-case launch-files to fuerte and the
new openni stack, so some of the launchfiles might not work correctly
yet. You should get them running if you fiddle with the topics
("rostopic list" and "rosnode info" will help you. "rxgraph" is
great too).

# Usage

If you want to use RGB-D SLAM with a Kinect or Xtion Pro, you should
install [openni_launch](openni_launch). If you want to edit the saved
point clouds you might want to install meshlab.

Most people seem to want the registered point cloud. It is by default
sent out on /rgbdslam/batch_clouds when you command RGB-D SLAM to do so
(see below). The clouds sent are actually the same as before, but the
according transformation - by default from /map to /openni_camera - is
sent out on /tf.

This is also the way the octomap_server gets the point clouds. Just make
it listen to the mentioned topic and set the fixed frame_id to /map (See
the launch file octomap_server.launch)

## USAGE with GUI

To start RGBDSLAM launch

```
roslaunch rgbdslam kinect+rgbdslam.launch
``` Alternatively you can start the openni nodes
and RGBDSLAM separately, e.g.:

```
roslaunch openni_launch openni.launch
  rosrun rgbdslam rgbdslam
``` To capture models either press space to start
recording a continuous stream or press enter to record a single frame.
To reduce data redundancy, sequential frames from (almost) the same
position are not included in the final model. The 3D visualization
always shows the globally optimized model. Neighbouring points are
triangulated except at missing values and depth jumps.

## Usage via ROS service calls (possibly headless)

The RosUI is an alternative to the Grapical_UI and lets you use rgbdslam
via service-calls. This allows you, e.g. to run the rgbdslam headless,
for example on the PR2. The possible calls are:

-   /rgbdslam/ros_ui {reset, quick_save, send_all, delete_frame,
    optimize, reload_config, save_trajectory}
-   /rgbdslam/ros_ui_b {pause, record} {true, false}
-   /rgbdslam/ros_ui_f {set_max} {float}
-   /rgbdslam/ros_ui_s {save_octomap, save_cloud, save_g2o_graph,
    save_trajectory, save_features, save_individual} {filename}

See below for a detailed description of all options. To start the
rgbdslam headless use the headless.launch:

```
roslaunch rgbdslam headless.launch
``` Example service calls:

```
rosservice call /rgbdslam/ros_ui frame # Capture single frames via
        rosservice call /rgbdslam/ros_ui_b pause false # Capture a stream of data
        rosservice call /rgbdslam/ros_ui send_all # Send point clouds with computed transformations (e.g., to rviz or octomap_server)
        rosservice call /rgbdslam/ros_ui_s save_cloud /tmp/mycloud.pcd # Save the registered pointclouds in the given file
        rosservice call /rgbdslam/ros_ui_s save_individual /tmp/filenameprefix # As above, but save every pointcloud in its own file
``` Detailed command descriptions:

/rgbdslam/ros_ui:

-   reset *resets the graph, delets all nodes (refreshes only when
    capturing new images)*
-   frame *capture one frame from the sensor*
-   optimize *trigger graph optimizer*
-   reload_config *reloads the paramters from the ROS paramter server*
-   quick_save *saves all pointclouds in one file quicksave.pcd in
    rgbdslam/bin-directory*
-   send_all *sends all pointclouds to /rgbdslam/transformed_cloud (can
    be visualized with rviz)*
-   delete_frame *delete the last frame from the graph (refreshes only
    when capturing new images)*

/rgbdslam/ros_ui_b:

-   pause <flag> *pauses or resumes the capturing of images*
-   record <flag> *pauses or stops the recording of bag-files, can be
    found in the rgbdslam/bin-directory*

/rgbdslam/ros_ui_f:

-   set_max <float> *filters out all datapoints further away than this
    value (in cm, only for saving to files)*

/rgbdslam/ros_ui_s:

-   save_features <filename> *saves the feature locations and
    descriptors in a yaml file with the given filename*
-   save_cloud <filename> *saves the cloud to the given filename
    (should end with .ply or .pcd)*
-   save_individual <fileprefix> *saves every scan in its own file
    (appending a suffix to the given prefix)*
-   save_octomap <filename> *saves the cloud to the given filename*
-   save_trajectory <fileprefix> *saves the sensor trajectory to the
    file <fileprefix>_estimate.txt*

# Performance

RGB-D SLAM has many options to customize its behavior. You can speed it
up significantly by

-   enabling concurrency on multi-core machines. The three corresponding
    parameter names start with "concurrent_\..."
-   using SIFTGPU features, if you have a GPU, ORB otherwise
-   compile in "Release" configuration (see build type options in
    CMakeLists.txt)
-   decreasing the "max_keypoints" parameters
-   decreasing the "geodesic_candidates" and
    "min_sampled_candidates"
-   setting the kinect driver to QVGA (There's a bug in the camera_info
    of the driver. See/use the launchfile qvga-kinect+rgbdslam.launch
    for a workaround)

However, the last three options and using ORB will probably decrease the
accuracy.

# Problems

-   Error in this wiki: Please fix it!
-   Installation/Compilation: Report via e-mail. Patches are welcome!
-   Bug in the code: As above.
-   Crashes:
    [A brief debugging help can be found here](http://answers.ros.org/question/59930/rgbdslam-crashes-after-a-few-minutes-of-running/?answer=60342#post-id-60342)
-   Questions: See the
    [FAQ](http://answers.ros.org/questions/scope:all/sort:activity-desc/tags:rgbdslam/page:1/)

# RGB-D SLAM for "Not-yet" ROS Users

If you aren't using ROS yet and just want to use RGB-D SLAM on Ubuntu
(tested with Ubuntu "precise pangolin" 12.04), here's an installation
walkthrough:

```
# Better pick a mirror close to you.
# See http://ros.org/wiki/ROS/Installation/UbuntuMirrors
sudo sh -c '. /etc/lsb-release && echo "deb http://packages.ros.org/ros/ubuntu $DISTRIB_CODENAME main" > /etc/apt/sources.list.d/ros-latest.list'

wget http://packages.ros.org/ros.key -O - | sudo apt-key add -

sudo aptitude update

# This will draw gigabytes from the network:
sudo apt-get install ros-fuerte-perception-pcl ros-fuerte-vision-opencv ros-fuerte-octomap-mapping python-rosdep

echo 'source /opt/ros/fuerte/setup.bash' >> ~/.bashrc

echo 'export ROS_PACKAGE_PATH=~/ros:$ROS_PACKAGE_PATH' >> ~/.bashrc

. ~/.bashrc

svn co http://alufr-ros-pkg.googlecode.com/svn/trunk/rgbdslam_freiburg ~/ros/rgbdslam_freiburg

sudo rosdep init

rosdep update

rosdep install rgbdslam_freiburg

roscd rgbdslam

# This will take a while:
rosmake rgbdslam_freiburg
``` If this reports no failures, you successfully
installed the RGB-D SLAM system.

To use it with a Kinect/Xtion Pro you need to install the camera driver:

```
sudo apt-get install ros-fuerte-openni-launch
``` For usage, see above.
