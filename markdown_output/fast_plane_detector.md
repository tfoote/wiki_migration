## Overview

This package provides a method to detect the dominant 3D plane in a
scene in real time. It is based on RANSAC and uses disparity images as
input. It is an extracted submodule from the package
[active_realtime_segmentation](active_realtime_segmentation) in which it
was used for detecting the dominant table plane. However, any plane
orientation is possible to detect.

## Starting the Fast Plane Detector

For detecting the table plane in a disparity image start the following
launch file:

```
roslaunch fast_plane_detection fast_plane_detection_jean.launch
``` which starts a table plane detection node that
subscribes to the topic /narrow_stereo_textured/disparity.

For detecting the local plane in a region around a specific pixel
position, run the following node:

```
rosrun fast_plane_detection fast_region_plane_detector_jean disparity_in:=/plane_detection/disparity disparity_image_topic:=/narrow_stereo_textured/disparity cam_info_in:=/narrow_stereo_textured/left/camera_info
``` where the remapped topics are the output from
the node run by the previous launch file.

## Example Results

Here are some example results for planes extracted from the following
disparity map in real time.

![](attachment:Orig_disp.jpg)

This is the disparity map in which the detected table plane is filtered
out.

![](attachment:without_table_disp.jpg)

This is the disparity map in which a local plane is detected.

![](attachment:masked_disp.jpg)

The table plane and the local plane detected can be visualised in Rviz.

![](attachment:Planes.jpg)
