## Overview

This package provides a [URDF](https://index.ros.org/p/urdf) model of
[Leo Rover](Robots/Leo Rover) in [xacro](https://index.ros.org/p/xacro)
format. ![attachment:leo_model_rviz.png](doc/leo_model_rviz.png)

Here's a graphical representation of the description (click to see the
PDF version):
[![attachment:leo_urdf.png](doc/leo_urdf.png)](doc/leo_urdf.pdf)

## Coordinate frames

base_link:: Rigidly attached to the robot base. Provides an obvious
point of reference for other links in the model. Located on the upper
plane of the robot, in the central mounting hole, with the X axis facing
forward like in the picture below:
![attachment:leo_model_base_link.png](doc/leo_model_base_link.png)

Because it lies so close to the rocker axis, it is assumed to be the
center of rotation in differential driving. base_footprint:: The root
link of the robot. Projection of the `base_link` frame into the ground
(assuming the ground is flat). camera_frame:: Attached to the camera
sensor. Represents the viewport of the camera and allows to express
relative pose in the standard convention. camera_optical_frame:: The
"optical" frame of the camera. Located at the same position as the
`camera_frame`, but uses a slightly different convention for the axis
orientation (see
[REP 103](https://www.ros.org/reps/rep-0103.html#axis-orientation)).

## Usage

The package does not provide any functionality on its own. Rather, it is
used by a variety of other components.

For example, if you want to visualize the model in RViz, see the
[leo_viz](https://index.ros.org/p/leo_viz) package.
