## Overview

A ROS driver for the
[ELP-1MP2CAM001 Dual Lens](http://www.amazon.com/gp/product/B00VG32EC2)
stereo camera. Included in the package is:

-   a URDF macro for the camera
-   a usable calibration
-   udev rules to reliably access the two cameras
-   a launch file to start two usb_cam nodes and a stereo_image_proc
    node
-   a launch file to start the calibration process
-   Source: git
    <https://github.com/joshvillbrandt/elp-stereo-camera-ros-pkg>

## Setup

To install from apt, use:



```
sudo apt-get install ros-*-elp-stereo-camera
```

 Please see README.md in the source repository
for instructions on checking the code out from source.

## Usage

To start the cameras, run the following two launch files:



```
# terminal 1
roslaunch elp_stereo_camera elp_stereo_camera.launch

# terminal 2
roslaunch elp_stereo_camera stereo_image_proc.launch
```

 You now have available topics such as
`/elp/left/image_rect_color`, `/elp/left/image_rect_color`, and
`/elp/points2`. You'll likely also want to include the
`elp_stereo_camera` macro in your urdf file. Look at the
[elp_standalone.urdf.xacro](https://github.com/joshvillbrandt/elp-stereo-camera-ros-pkg/blob/master/description/elp_standalone.urdf.xacro)
file in the source code for an example of how to do that.

To quickly view a camera image and the resulting point cloud, try out
the included rviz configuration:



```
# terminal 3
roslaunch elp_stereo_camera rviz.launch
```

 Click the "Point Cloud" saved camera view in
the Views pane on the right. You should now be able to your objects in
3D! Keep in mind that objects closer than 70 cm won't show up in the
point cloud with this particular camera.

![rviz screenshot](attachment:rviz-screenshot.jpg)

## Calibration

The calibration process removes distortion from the individual cameras
and surrounding enclosure. This process is essential for producing a
quality disparity image. While this package includes generic calibration
files for the camera, performing a calibration for each unique camera
can improve the quality of the resulting point could. The following is a
tailored version of the
[StereoCalibration](camera_calibration/Tutorials/StereoCalibration)
tutorial specifically for this camera.

To calibrate the cameras, first print out the 8x6 checkerboard on an
8.5x11 inch piece of paper. Attach the checkerboard printout to
something firm like a clipboard. (Add a bit of tape to the bottom two
corners to keep the page flat.) Then run the following:



```
roslaunch elp_stereo_camera calibrate.launch
```

 The calibration process measures a range of
four key attributes: X, Y, size, and skew. Hold the checkerboard up in
front of the cameras and vary each of the parameters. (So move the
checkerboard left and right, up and down, father and closer, and at
different angles.) Make sure that the entire calibration grid stays
within view of both cameras. You'll know the calibration process is
working when you can see a colored grid in each camera view and when the
size of attribute bars are increasing.

![calibration screenshot](attachment:calibration-screenshot.jpg)

When the calibration process has gathered enough information about a
particular attribute, the corresponding bar will turn green. With
practice, the calibration process should take about one minute to
complete. Hit the "calibrate" button once all four bars are green.
After a few moments, new rectified images should be displayed.
Real-world straight edges should now appear straight in the video feed.

Hit the "commit" button to complete the process. This saves the
calibration information locally to `~/.ros/camera_info/`. Check out
[elp_stereo_camera.launch](https://github.com/joshvillbrandt/elp-stereo-camera-ros-pkg/blob/master/launch/elp_stereo_camera.launch)
for an example of how to specify the calibration files.

## Video Modes

The ELP module used in the ELP stereo camera supports these MJPEG video
modes:

  -- ----------------------------- -- --------------------- --
     **Width x Height (pixels)**      **Framerate (fps)**   
     1280x720                         15, 25, 30            
     800x600                          30                    
     640x360                          60                    
     640x480                          15, 30                
     352x288                          15, 30                
     320x240                          15, 30                
  -- ----------------------------- -- --------------------- --

## Tips and Tricks

Some helpful debugging commands:

-   Quick check of available cameras: `ls /dev | grep video`
-   Quick check of the support video modes of a camera:
    `v4l2-ctl --list-formats-ext -d /dev/video0`
-   Camera viewer with extensive camera configuration:
    `guvcview or guvcview -d /dev/video0`
-   View udev attributes to create different udev rules:
    `udevadm info -a -n /dev/video0` (also see
    [this syntax guide](http://www.reactivated.net/writing_udev_rules.html#syntax))
