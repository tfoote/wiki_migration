## Overview

This package provides for camera intrinsic calibration. The camera
intrinsics such as focal length, center point, and distortion
parameters, are important if the camera position (extrinsic calibration)
is to be determined with a high degree of accuracy. Incorrect camera
intrinsics can lead to improper extrinsic calibration which can result
in poor process results.

The procedure uses a slightly different cost function than OpenCV and
Matlab. It relies on knowing the distance the camera is moved between
successive images. When performed precisely, the routine is both quicker
because it requires fewer images and more accurate because the
parameters have lower co-variance. In order to run the calibration, you
will need a linear rail or guide in order to precisely position the
camera prior to taking each image

![target and rail setup\|width="300"](attachment:rail_setup.jpg)

## Motivation

While a [camera_calibration](camera_calibration) method does already
exist, for some industrial and high precision applications, the results
may not be sufficient. Depending on the number and quality of the images
collected by the user, the calibration method can result in widely
varying focal length values.

![Focal length results, red - ROS camera calibration, green - rail calibration\|width="800"](attachment:focal_length_graph.jpg)

A 1-2% error in the focal length calculation could lead to a position
error of 2cm or more. Such position error could lead to problems if the
robotic system is not designed to compensate for the error. Grippers
could miss grasping parts or run into the part they are trying to grab.

## Technical Notes/Definitions

Error per observation: The industrial calibration package utilizes the
[Ceres solver\|target="_blank"](http://ceres-solver.org/) to collect
all the image observations and optimize the camera parameters (intrinsic
or extrinsic) to minimize the error. For the intrinsic calibration
package, an observation is a single circle found in the calibration
target. So for a single image of an 18x24 grid calibration target, there
are 432 observations made, and 4320 observations made for a series of 10
images. After optimization, the total error is then divided by the
number of observations in order to obtain the average error per
observation. This is the measure of how accurately the algorithm was in
finding the target location. Since the target location in the image is
measured in pixels, then the error units is also in pixels. Thus, an
average error per observation of 1 pixel indicates that final solution
was able to find the actual target location with an accuracy of 1 pixel.
When performed correctly, all calibration attempts should result in less
than 1 pixel of error.

Convergence to a solution that has a low error, however, does not mean
that the final result is correct. If too few images are provided, or the
images are not diverse enough (based upon the calibration routine being
executed), then the algorithm could converge to the wrong solution. To
ensure accurate results, follow the tutorial instructions and any
validation procedure provided.

## Tutorials

. Examples can be found in the [tutorials](intrinsic_cal/Tutorials)
section.
