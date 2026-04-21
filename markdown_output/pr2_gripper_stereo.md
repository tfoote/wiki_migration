## Overview

This package provides various files needed to use a gripper stereo
sensor on the PR2. Launch, urdf, mesh, and config files are provided.
This package will run correctly in simulation, enabling anyone to
experiment with use of this sensor strategy even without the custom
hardware.

## Video

[Youtube](https://www.youtube.com/watch?v=xY3cnMdjbow)

## Hardware

At Willow Garage, a gripper stereo camera exists using WGE100 cameras.
This camera operates the same as the narrow_stereo cameras on the PR2.

It is also possible to make a gripper stereo pair out of Logitech C905
webcameras. The CAD and other helpful information will be posted here in
the near future so that anyone with access to a machine shop can create
this hardware.

## Robot Description

The robot description file used to launch the robot must include frames
and other information about the gripper stereo cameras. The
pr2.urdf.xacro file in pr2_gripper_stereo/urdf shows how to include the
necessary modifications.

## Calibration

After doing a number of calibration tests it was found that full-robot
calibration does not significantly alter the CAD-based frame position of
the gripper cameras.

As a result it seems sufficient to copy the gripper stereo urdf
information into the bottom of any existing robot's calibrated urdf.

A patch to pr2_calibration_launch is available for those who would like
to investigate it further.
