## Overview

This package provides a graphical user interface in form of an rviz
plugin for interactive object segmentation. The segmentation method
comes from the
[active_realtime_segmentation](active_realtime_segmentation) package.
This iterative methods needs initialisation of object hypotheses. In
this interactive segmentation scenario, this is provided by the user
through clicks or selection of rectangular regions. The GUI also
provides the possibilities to change the parameters of the segmentation
method.

## Example Inputs and Results

Here is an example initialisation on RGB-D data from the textured light
stereo on the PR2 and the corresponding result. Color information from
the wide-field stereo is ported to the monochrome narrow-stereo of PR2
through the [rgbd_assembler](rgbd_assembler) package.

![](attachment:PR2_Stereo_init.jpg) ![](attachment:PR2_stereo.jpg)

Here are examples for RGB-D data collected from the kinect.

![](attachment:kinect_init.jpg) ![](attachment:kinect_result.jpg)
