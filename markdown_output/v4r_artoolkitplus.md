## Overview

This package uses the ARToolKitPlus to detect visual tags encoded with
an id. Details to the tag detection can be found at
<http://handheldar.icg.tugraz.at/artoolkitplus.php>

This wrapper for the ARToolKitPlus has two modes:

-   Single Marker (Every tag creates a tf)
-   Multi Marker (A predefined set of markers creates only on tf)

The "Multi Marker" mode is especially useful if you would like to
estimate your camera pose and to estimate other markers. Nearly all
parameters can be tuned by using the dynamic reconfigure package
on-line. The note is able to deal with distorted as well as with
undistorted images as long as the provided camera_info message is
correct.

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     <tablewidth="710px" tableheight="590px"> ![](attachment:multi_marker_with_pionerr.png) *This figure shows the node running the multi marker mode; The marker combination/pattern under the robot is used to estimate the camera pose while the marker on top is used to estimate the robot pose. *   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

## Node

There are a large number of ROS [Parameters](Parameters) that can be set
to customize the behavior of the `ARToolKitPlus` wrapper. Most of
these parameters can also be changed using
[dynamic_reconfigure](dynamic_reconfigure) but some of them must be set
at start-up.



```
sub{
  0.name= image
  0.type= sensor_msgs/Image
  0.desc= Image stream from the camera driver see parameter ''distorted_input''
  1.name= camera_info
  1.type= sensor_msgs/CameraInfo
  1.desc= Camera metadata
}
pub{
  0.name= ~<tf_prefix>/tf
  0.type= tf/tfMessage
  0.desc= TF related to the detected markers
}
```

 

```
param{
  0.name = ~<name>/show_camera_image
  0.default = false
  0.type = bool
  0.desc = On true it opens a OpenCV window with debug information
  1.name = ~<name>/skip_frames
  1.default = 0
  1.type = int
  1.desc = Number of frames skipped between processing
  2.name = ~<name>/tracker_single_marker
  2.default = true
  2.type = bool
  2.desc = Sets the single marker mode it does not work with tracker_multi_marker = true
  3.name = ~<name>/tracker_multi_marker
  3.default = false
  3.type = double
  3.desc = Sets the multi marker mode it does not work with tracker_single_marker = true, the multi marker mode requires also a ''~<name>/pattern_file''
  4.name = ~<name>/pattern_file
  4.default = ""
  4.type = string
  4.desc = filename of the pattern file used for the  multi marker mode, there is a file within the packages cfg folder
  5.name = ~<name>/tf_prefix
  5.default = the node_name
  5.type = string
  5.desc = prefix for the tf publisher
  6.name = ~<name>/marker_mode
  6.default = "bch"
  6.type = string
  6.desc = defines the marker id encoding, options are "bch" or "simple"
  7.name = ~<name>/pattern_width
  7.default = 0.1
  7.type = double
  7.desc = size of single markers
  8.name = ~<name>/edge_threshold
  8.default = 0
  8.type = int
  8.desc = Edge threshold used for the detection, zero means automode
  9.name = ~<name>/border_width
  9.default = 0
  9.type = double
  9.desc = ratio of the marker border, zero means defined by marker_mode
  10.name = ~<name>/undist_mode
  10.default = "std"
  10.type = string
  10.desc = undistorted function used to cope with image distortions, options are "none", "std" and "lut". "lut" only works up to 1024x1024
  11.name = ~<name>/undist_iterations
  11.default = 10
  11.type = int
  11.desc = Interactions used on the undistort approximation
  12.name = ~<name>/distorted_input
  12.default = true
  12.type = bool
  12.desc = Defines if the input image is distorted or not.
  13.name = ~<name>/pose_estimation_mode
  13.default = "rpp"
  13.type = string
  13.desc = Defines the algorithm used to estimate a markers pose. Options are "normal", "cont" and "rpp"
  14.name = ~<name>/use_multi_marker_lite_detection
  14.default = true
  14.type = bool
  14.desc = Only for multi marker mode, on true it uses a faster detection algorithm to find markers before the pattern pose is computed. This value should be set to true if one, next to the pattern, also wants to use the detected marker which is not part of an pattern.
  14.name = ~<name>/pattern_frame
  14.default = pattern
  14.type = string
  14.desc = name of the pattern tf related to a multi marker
}
```


