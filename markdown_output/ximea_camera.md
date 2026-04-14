## Overview

This software provides ROS drivers for the ximea xiQ USB 3.0 Cameras.
This driver supports image acquisition from an arbitrary number of
cameras, so long as there is sufficient bandwidth on the USB 3.0 bus to
perform the data transfer. In order to operate the cameras, the serial
numbers of the devices must be known.

This package is working in ROS Indigo. For a working package in ROS
Melodic see [http://wiki.ros.org/ximea_ros_cam](ximea_ros_cam)

## Dependencies

This software requires the Ximea Linux Software Package. See
<http://www.ximea.com/support/wiki/apis/XIMEA_Linux_Software_Package>
for details.

## Usage

1\) Create a configuration file for each camera. The configuration file
should be kept in the /config folder. A configuration file will look as
follows:

```
serial_no: 32301951
cam_name: "camera1"
yaml_url: "package://mcptam/calibrations/camera1.yaml"
exposure_time: 30000
rect_left: 200
rect_top: 200
rect_height: 600
rect_width: 900
image_data_format: "XI_MONO8"
```

-   `serial_no` refers to the serial number of the camera
-   `cam_name` is the name you wish to give to the camera
-   `yaml_url` is the location of the calibration information file,
    which is used by the camera info manager to publish the calibration
    parameters
-   `exposure_time` refers to the image exposure time in microseconds
-   `rect_left, rect_top, rect_height, rect_width` are used to set the
    image region of interest (ROI). See the Ximea xiQ API for more
    information <http://www.ximea.com/support/wiki/apis/XiAPI_Manual>.
-   `image_data_format` sets the data format for the image. Currently,
    formats XI_MONO16, XI_RGB24, XI_RGB32, XI_RAW8, XI_RAW16, and
    XI_MONO8 are supported

2\) Create a launch file for your camera configuration. A typical launch
file will look as follows:

```xml
<launch>
<!-- Camera Node -->
<node name="ximea" pkg="ximea_camera" type="ximea_camera_node" output="screen" >
  <param name="frame_rate" type="int" value="60" />

  <rosparam param="camera_param_file_paths" subst_value="true">[$(find ximea_camera)/config/ximea1.yaml, $(find ximea_camera)/config/ximea2.yaml]</rosparam>

</node>
</launch>
``` The main parameters of interest are the frame
rate and the file paths.

-   `frame_rate` corresponds to the frame rate for all of the cameras in
    the group.

```{=html}
<!-- -->
```
-   `camera_param_file_paths` is a list of file names corresponding to
    the configuration files made for each camera in step 1. For a single
    camera setup, the `camera_param_file_paths` parameter would look
    something like:

```xml
<rosparam param="camera_param_file_paths" subst_value="true"> [$(find ximea_camera)/config/ximea1.yaml] </rosparam>
``` while a three camera setup would have a list
containing the file names for the configuration files of all three
cameras, separated by commas:

```xml
<rosparam param="camera_param_file_paths" subst_value="true">[$(find ximea_camera)/config/ximea1.yaml, $(find ximea_camera)/config/ximea2.yaml, $(find ximea_camera)/config/ximea3.yaml]</rosparam>
``` 3) You should now be able to plug in the
cameras and launch the file created in step 2.

## Published Topics

Each set of published topics will be under the namespace corresponding
to the camera name. Each camera will publish:

`/camera_info`, which is of ROS message type `sensor_msgs/CameraInfo`.
This message carries all of the camera specific calibration information.

`/image_raw/`, which of of ROS message type `sensor_msgs/Image`. This
message carries the image data.
