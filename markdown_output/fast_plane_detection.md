## Overview

This package provides a real time plane detection method extracted from
the package [active_realtime_segmentation](active_realtime_segmentation)
where it is used to find the most likely table plane in the scene.
However, any plane pose can be detected. The plane detection is based on
RANSAC and uses a disparity map as input.

## Starting the Fast Plane Detector

The following launch file will read in disparity maps from a given topic
(by default it takes /narrow_stereo_textured/disparity) and outputs the
table plane parameters as well as a disparity image with the detected
table plane filtered out.

```
roslaunch fast_plane_detection fast_plane_detection_jean.launch
``` To detect a local plane in a region around a
specific pixel position in the image, run the following ros node.

```
rosrun fast_plane_detection fast_region_plane_detector_jean disparity_in:=/plane_detection/disparity disparity_image_topic:=/narrow_stereo_textured/disparity cam_info_in:=/narrow_stereo_textured/left/camera_info
``` Here it takes as input the topics, on which the
node launched by the previous launch file is publishing.

## Example Results

The following results are extracted from the following disparity map
originating from the textured light stereo on the PR2.

![](attachment:orig_disp.jpg)

When using the real time table plane detector, the following disparity
map in which all the values belonging to the detected table are removed
is the result.

![](attachment:without_table_disp.jpg)

Given a specific pixel position and a size of region around that, the
disparity map can be masked and a plane fit to the local region.

![](attachment:masked_disp.jpg)

The detected planes can be visualised in Rviz.

![](attachment:rviz_planes.jpg)
