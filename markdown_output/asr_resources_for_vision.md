![\|width=\"333\",height=\"200\"](attachment:Logo-white-medium.jpg)

## Description

This package contains launch scripts which start up data acquisition
from vision sensors (stereo camera systems and kinect).

*Example of a stereo rig with two AVT Guppy cameras and a Microsoft
Kinect on top:*

![\|width=\"600\",height=\"337\"](attachment:guppy.png)

## Functionality

The launch system for the stereo cameras is subdivided in a hierarchy
with three levels where the more specific launch files call the more
generic. This is done to group common parts of monolithic launch files
of different stereo systems together.

-   The top level file is *stereo_rig.launch* in the
    *launch/image_acquisition_pipelines* directory which is used by all
    the setups in this package. It uses *unsynced_stereo_proc.launch* in
    the same directory, which starts a
    [stereo_image_proc](stereo_image_proc) node, for the postprocessing
    of raw images as there is no hardware sync of the image capturing in
    both cameras enabled
-   In the *launch/image_acquisition_pipelines/stereo_rigs *directory
    are launch scripts which more or less parametrize the top level
    script depending on the used hardware setup independently of user
    specific settings.
-   The low level scripts are typically located in
    *launch/image_acquisition_pipelines/trunk *and contain the user
    settings for a certain setup. They load up two files which contain
    camera specific settings:
-   The .yaml files contain settings for the mode of a certain camera
    (e.g. resolution, frame rate)
-   The .ini files contain camera calibrations for a certain camera

The launch system of the kinect uses [openni_launch](openni_launch) and
[rgbd_launch](rgbd_launch) to process the data and the scripts in
*launch/image_acquisition_pipelines/kinect *are used to call those nodes
with the correct parameters.

## Usage

### Needed packages

Stereo camera setup:

-   [stereo_image_proc](stereo_image_proc)

Kinect:

-   [openni_launch](openni_launch)
-   [rgbd_launch](rgbd_launch)

### Needed software

libdc1394 needs to be installed for the use of stereo cameras

### Needed hardware

A vision sensor setup of your choice.

### Start system

**For stereo cameras: **

-   You just need to call a single launch file of your choice to get the
    entire rig running together with the necessary postprocessing (see
    the different hierarchy levels mentioned above). By default the
    package contains calibrated launch files for stereo setups using
    [AVT Marlin and Guppy](https://www.alliedvision.com/en/products/cameras/cameras-full-portfolio.html)
    cameras

**For the kinect camera: **

-   Simply start your desired launch file, either
    *kinect_with_registered_guppy_mild.launch* or
    *kinect_with_registered_guppy_dome.launch *depending your specific
    environment (mild or dome) or use those files and change their
    parameters if you want to use your own setup. If you want a textured
    point cloud you need to publish a transformation between the rgb and
    the depth frame (e.g.
    [asr_kinematic_chain_dome](asr_kinematic_chain_dome))

## ROS Nodes

### Subscribed Topics

Kinect** **camera**: **

-   /stereo/left/camera_info: Contains the camera info of the left
    camera of a stereo setup, but can be supplied with the camera info
    of a single rgb camera as well.
-   /stereo/left/image_raw: The raw left image of the stereo setup
    related to camera info (or from a single camera)

This is used only if you want to register an external camera and use the
image of that one instead of the internal rgb-camera of the kinect.

### Published Topics

Stereo camera**: **

-   /stereo/left/camera_info: Holds the calibration for the left camera
    of our stereo setups (after calibration of course\...).
-   /stereo/left/image_raw: Image of left camera, containing raw bayer
    pattern, before demosaicing. Do not mix it up with the grayscale
    image\... and don\'t use it directly.
-   /stereo/left/image_mono: Grayscale image of left camera of stereo
    pair.
-   /stereo/left/image_color: RGB image of left camera of stereo pair.
-   /stereo/left/image_mono_rect: Grayscale image for left camera of
    idealized stereo setup, not our real. Required in some applications.
-   /stereo/left/image_color: RGB image for right camera of idealized
    stereo setup, not our real. Required in some applications.
-   /stereo/right/camera_info: Holds the calibration for the right
    camera of our stereo setups (after calibration of course\...).
-   /stereo/right/image_raw: Image of right camera, containing raw bayer
    pattern, before demosaicing. Do not mix it up with the grayscale
    image\... and don\'t use it directly.
-   /stereo/right/image_mono: Grayscale image of right camera of stereo
    pair.
-   /stereo/right/image_color: RGB image of right camera of stereo pair.
-   /stereo/right/image_mono_rect: Grayscale image for right camera of
    idealized stereo setup, not our real. Required in some applications.
-   /stereo/right/image_color: RGB image for right camera of idealized
    stereo setup, not our real. Required in some applications.

Kinect camera (important ones only):

-   /kinect/depth/image_rect: Rectified depth image from the kinect
-   /kinect/depth/points: Untextured point cloud from the kinect
-   /kinect/depth_registered/points: Textured point cloud from the
    kinect, only if the topics which are named under \'Subscribed
    Topics\' get supplied and a transformation between the kinect and
    that external camera exists

## Tutorials

If you want to use your own stereo camera setting, you will need to
implement your own launch file(s):

1\. If you simply want to use the same rig (with the same cameras) as
one of the ones provided, then you only need to add a launch file to the
*trunk* directory (or modify one of the provided launch/yaml/ini files)
which includes a launch file in the hierarchy level above and use your
own calibration values (see the low level part described in
functionality). Check the [camera_calibration](camera_calibration)
tutorials on how to get those values and also check the provided launch
files for more information on the structure and the used parameters. 1.
In case you want to use your own cameras you will have to add a launch
file to the *stereo_rigs* directory which includes the top level launch
file (*stereo_rig.launc*h) and add the parameters accordingly to your
setup (compare the provided launch files for the guppy or marlin setup).
Then again you can add a low level launch file to the *trunk* directory
containing your camera specific calibration values.

For more information on the image processing parameters and the general
functionality check out the [image_proc](image_proc)/
[stereo_image_proc](stereo_image_proc) packages.
