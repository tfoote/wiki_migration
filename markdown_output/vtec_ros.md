## Documentation and Citing

[Youtube](https://www.youtube.com/watch?v=r7kZLqQ5xbI)

A
[playlist with example applications of the system is also available on YouTube](https://www.youtube.com/playlist?list=PLZlXR7ILmDx5N0YFYiw_PGoY_rAVYVMr-)

A technical report is available here:
[Tech Report](https://github.com/visiotec/vtec/blob/master/vtec_ibgho_TR.pdf).
It describes the tracker software and its working principles. If you use
this software in an academic context, please cite the technical report,
using:

```
@TechReport{nogueira2019,
  author = {Lucas Nogueira and Ely de Paiva and Geraldo Silveira},
  title  = {Visio{T}ec robust intensity-based homography optimization software},
  number = {CTI-VTEC-TR-01-19},
  institution = {CTI},
  year = {2019},
  address = {Brazil}
}
```

## Installation

### Dependencies

Install the usb_cam driver from ROS repositories.

```
sudo apt-get install ros-[kinetic|melodic]-usb-cam
```

### Build

Setup a ROS workspace.

```
mkdir -p ~/catkin_ws/src
``` Install the vtec cpp library

```
cd ~/catkin_ws/src
git clone https://github.com/visiotec/vtec.git
cd vtec
mkdir build
cd build
cmake ..
make
``` Install the ROS packages

```
cd ~/catkin_ws/src
git clone https://github.com/visiotec/vtec_ros.git
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

### Running

#### From a dataset

Download the dataset from here:
[dataset](https://www.dropbox.com/s/kxv9ahrxhvgebja/vtec_test_tracker.bag?dl=0)

Open two terminal windows, and launch in the first one the tracker node
with:

```
roslaunch vtec_tracker tracker.launch
``` In the other terminal, navigate to the
directory where you downloaded the dataset, and play the bagfile with:

```
rosbag play vtec_test_tracker.bag
``` Now you should see in RViz the tracking process
using the default parameters from the launch file.

#### From a live camera

Open a terminal window and launch the tracker node:

```
roslaunch vtec_tracker tracker_live.launch
``` A Rviz window will pop-up with the camera
images. In the terminal window where you issued the roslaunch command,
press the S key to start tracking. This will select a bounding box in
the current frame to be tracked. You can press S again anytime to
restart the tracking process.

If you want to enable the robust to unknown occlusion mode, use the
following command instead: ```
roslaunch vtec_tracker tracker_live_occlusion.launch
```

## Nodes

```clearsilver
name = ibgho_tracker_node
desc =  Tracks a planar object in an image sequaence.
sub {
  0.name = camera/image
  0.type = sensor_msgs/Image
  0.desc = The incoming image stream from the camera.
  1.name = track_cmd
  1.type = std_msgs/Char
  1.desc = Commands to start tracking.
}
pub {
  0.name = annotated_image
  0.type = sensor_msgs/Image
  0.desc = The image stream annotaded with the tracked image region and the score.
  1.name = stabilized_image
  1.type = sensor_msgs/Image
  1.desc = The warped image patch from the image stream, that tries to match to the reference image patch.
  2.name = reference_image
  2.type = sensor_msgs/Image
  2.desc = The reference template extracted from the reference image file.
  3.name = tracking
  3.type = vtec_msgs/Tracking
  3.desc = Information about the tracking. Includes the estimated homography and the photometric parameters.
}
param{
  0.name = bbox_size_x
  0.default = 200
  0.type = int
  0.desc = The length in pixels of the region of interest along the x direction.
  1.name = bbox_size_y
  1.default = 200
  1.type = int
  1.desc = The length in pixels of the region of interest along the y direction.
  2.name = bbox_pos_x
  2.default = 200
  2.type = int
  2.desc = The x coordinate of the upper left corner of the region of interest in the reference image.
  3.name = bbox_pos_y
  3.default = 150
  3.type = int
  3.desc = The y coordinate of the upper left corner of the region of interest in the reference image.
  4.name = image_topic
  4.default = usb_cam/image_raw
  4.type = string
  4.desc = The name of the image input topic.
  5.name = max_nb_iter_per_level
  5.default = 5
  5.type = int
  5.desc = Maximum number of optimization iterations per pyramid level.
  6.name = max_nb_pyr_level
  6.default = 2
  6.type = int
  6.desc = Maximum number of pyramids levels.
  7.name = sampling_rate
  7.default = 1.0
  7.type = double
  7.desc = The sampling rate used to sample points used in the optimization process. 1.0 means 100% of the points are used.
  8.name = homography_type
  8.default = full
  8.type = string
  8.desc = Specifies the type of homography to be considered by the optimization algorithm. The options are: "full", "affine" and "stretch".
  9.name = robust_flag
  9.default = false
  9.type = bool
  9.desc = Set this to true to enable robust mode. This will try to detect partial occlusions on the current image and discard that information from the estimation procedure.
}
```

## Resources

1\. Technical Report:
<https://github.com/visiotec/vtec/blob/master/vtec_ibgho_TR.pdf> 1.
VisioTec C++ Libraries: <https://github.com/visiotec/vtec> 1. Geraldo
Silveira's website: <https://sites.google.com/site/geraldofsilveira/>

## Acknowledgment

This work was supported in part by the CAPES under Grant
88887.136349/2017-00, in part by the FAPESP under Grant 2017/22603-0,
and in part by the InSAC (CNPq under Grant 465755/2014-3 and FAPESP
under Grant 2014/50851-0).

## Report a Bug

<<GitHubIssues(visiotec/vtec_ros)>>
