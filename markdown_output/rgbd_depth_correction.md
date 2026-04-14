## Overview

The \`rgbd_depth_correction\` package provides a tool for calculating
and correcting the depth error (distortion and bias) of a RGBD camera.
This is done by placing a calibration target on a flat surface, then
comparing the sensor depth data to the position found using the
calibration target.

This method requires two things:

-   The camera intrinsic parameters have been accurately calibrated
    using the [intrinsic_cal](intrinsic_cal) package or some other
    method
-   The calibration target is placed on a flat, featureless wall which
    completely fills the field of view of the camera.

The calibration results are then used by the depth correction nodelet
which runs in the camera nodelet manager and publishes a corrected point
cloud.

![RGBD point cloud prior to correction\|width=\"300\"](attachment:uncorrected.jpg)
![RGBD point cloud after correction\|width=\"300\"](attachment:corrected.jpg)

## Motivation

As was found by Daniel Herrera C., Juho Kannala, and Janne Heikkila,
(<http://www.cse.oulu.fi/~dherrera/papers/2012-KinectJournal.pdf>), RGBD
cameras have not only depth error that is radial, but is depth
dependent. In order to correct for this depth error, a series of images
must be taken of a calibration target on a flat surface. This package
provides a method for calibrating and correction this depth error.

## Tutorials

. Examples can be found in the
[tutorials](rgbd_depth_correction/Tutorials) section.
