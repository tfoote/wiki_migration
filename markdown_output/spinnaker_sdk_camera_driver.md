## Getting Started

These are the ros drivers for running the Pt Grey (FLIR) cameras that
use the Spinnaker SDK. This code has been tested with various Point Grey
Blackfly S (BFS) cameras.

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes.

### Prerequisites

The pre-requisites for this repo include:

-   ros-kinetic-desktop-full
-   spinnaker
-   ros-kinetic-cv-bridge
-   ros-kinetic-image-transport \* libunwind-dev

```bash
# after installing spinnaker verify that you can run your cameras with SpinView
# after installing ros, install other pre-requisites with:
sudo apt install libunwind-dev ros-kinetic-cv-bridge ros-kinetic-image-transport
```

### Installation

To install the spinnaker drivers:

```bash
bash mkdir -p ~/spinnaker_ws/src cd spinnaker_ws/src
git clone https://github.com/neufieldrobotics/spinnaker_sdk_camera_driver.git
cd ~/spinnaker_ws/
catkin_make
source ~/spinnaker_ws/devel/setup.bash
# add this to ~/.bashrc to make this permanent
```

### Running the drivers

Modify the \`params/test_params.yaml\` file replacing the cam-ids and
master cam serial number to match your camera\'s serial number. Then run
the code as:

```
roslaunch spinnaker_sdk_camera_driver acquisition.launch

# Test that the images are being published by running rqt_image_view
``` ```clearsilver
name = acquisition_node
desc = The node that runs the spinakker sdk and exports to ROS. All the parameters can be set via the launch file or via the yaml config_file. It is good practice to specify all the 'task' specific parameters via launch file and all the 'system configuration' specific parameters via a config_file.
pub {
  0.name = camera_array/cam0/image_raw
  0.type = sensor_msgs/Image
  0.desc = Depending on number of cameras connected you would have that many publishers for image messages
}
pub {
  1.name = camera_array/cam0/camera_info
  1.type = sensor_msgs/CameraInfo
  1.desc = Depending on number of cameras connected you would have that many publishers for camera info messages if you provide the camera calibration information
}
param {
  0.name = ~binning
  0.type = int
  0.desc = Binning for cameras, when changing from 2 to 1 cameras need to be unplugged and replugged
  0.default = 1
}

param {
  1.name = ~color
  1.type = bool
  1.desc = Should color images be used (only works on models that support color images)
  1.default = false
}
param {
  2.name = ~exp
  2.type = int
  2.desc = Exposure setting for cameras, 0 is auto-exposure
  2.default = 0
}
param {
  3.name = ~frames
  3.type = int
  3.desc = Number of frames to save/view 0=ON
  3.default = 50
}
param {
  4.name = ~live
  4.type = bool
  4.desc = Show images on screen GUI
  4.default = false
}
param {
  5.name = ~live_grid
  5.type = bool
  5.desc = Show images on screen GUI in a grid
  5.default = false
}
param {
  6.name = ~save
  6.type = bool
  6.desc = Flag whether images should be saved or not (via opencv mat objects to disk)
  6.default = false
}
param {
  7.name = ~save_path
  7.type = string
  7.desc = Location to save the image data
  7.default = "~"
}
param {
  8.name = ~save_type
  8.type = string
  8.desc = Type of file type to save to when saving images locally: binary, tiff, bmp, jpeg etc.
  8.default = bmp
}
param {
  9.name = ~soft_framerate
  9.type = int
  9.desc = When hybrid software triggering is used, this controls the FPS, 0=as fast as possible
  9.default = 20
}

param {
  10.name = ~time
  10.type = bool
  10.desc = Show time/FPS on output
  10.default = false
}
param {
  11.name = ~to_ros
  11.type = bool
  11.desc = Flag whether images should be published to ROS. When manually selecting frames to send to rosbag, set this to False. In that case, frames will only be sent when 'space bar' is pressed
  11.default = true
}
param {
  12.name = ~utstamps
  12.type = bool
  12.desc = Flag whether each image should have Unique timestamps vs the master cams time stamp for all
  12.default = false
}
param {
  13.name = ~max_rate_save
  13.type = bool
  13.desc = Flag for max rate mode which is when the master triggers the slaves and saves images at maximum rate possible. This is the multithreaded mode"
  13.default = false
}
param {
  14.name = ~cam_ids
  14.type = array
  14.default = []
  14.desc = This is a list of camera serial numbers in the order which it would be organized. The convention is to start from left to right.
}
param {
  15.name = ~cam_aliases
  15.type = array
  15.default = []
  15.desc = This is the names that would be given to the cameras for filenames and rostopics in the order specified above eg. cam0, cam1 etc.
}
param {
  16.name = ~master_cam
  16.type = int
  16.default = ''
  16.desc = This is the serial number of the camera to be used as master for triggering the other cameras
}
param {
  17.name = ~skip
  17.type = int
  17.default = 20
  17.desc = Number of frames to be skipped initially to flush the buffer
}
param {
  18.name = ~delay
  18.type = float
  18.default = 2.0
  18.desc = Seconds to wait in the deinit/init sequence
}
param {
  19.name = ~distortion_model
  19.type = string
  19.default = plumb_bob
  19.desc = Distortion model for the camera calibration.
}
param {
  20.name = ~distortion_coeffs
  20.type = array of arrays
  20.default = ''
  20.desc = Distortion coefficients of all the cameras in the array. Must match the number of cam_ids provided.
}
param {
  21.name = ~intrinsic_coeffs
  21.type = array of arrays
  21.default = ''
  21.desc = Intrinsic coefficients of all the cameras in the array. Must match the number of cam_ids provided. Specified as [fx 0 cx 0 fy cy 0 0 1]
}
```
