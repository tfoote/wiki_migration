## Overview

The RGB-D assembler is designed to generate synchronised RGB-D data for
the monochrome narrow stereo cameras of the PR2. This can be useful for
segmentation approaches such as in the package
[active_realtime_segmentation](active_realtime_segmentation) that rely
on disparity and RGB data.

In detail, we transfer the RGB data from the color wide-field cameras of
the PR2 into the narrow stereo optimcal frame by going through the
following steps:

1\. Collect disparity and camera_info from the narrow stereo cameras. 1.
Reconstruct point cloud. 1. Transfer point cloud into wide field camera
frame using [tf](tf). 1. Project point cloud to wide field image to
create an RGB lookup. 1. Fill the monochome image of the narrow stereo
camera with these RGB values while keeping the intensity value of the
wide field cameras (through transforming RGB to HSV and back to RGB).

If you are using the kinect, then the RGB and disparity data is readily
available. The RGB-D Assembler collects them such that these two types
of information are roughly synchronised.

## Starting the RGB-D Assembler

Bring up the RGB-D Assembler on the robot using the following launch
file:



```
roslaunch rgbd_assembler rgbd_assembler.launch
```



For bringing up the RGB-D Assembler using the kinect, use the following
launch file:



```
roslaunch rgbd_assembler rgbd_kinect_assembler.launch
```



## Example Output

Here are two example images generated based on disparity values coming
from the textured light projector of the PR2. Note that at places where
no disparity information is available, no RGB data can be looked up in
the wide field stereo. At these places the original grey level values
are kept.

![](attachment:rgbd_assembler_1.jpg)
![](attachment:rgbd_assembler_2.jpg)
