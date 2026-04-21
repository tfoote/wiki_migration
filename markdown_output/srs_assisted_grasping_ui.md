## Overview

Package contains user interface in form of RVIZ plugin (ROS Electric)
for [srs_assisted_grasping](srs_assisted_grasping).

![User interface of Assisted grasping.\|width=200px](attachment:grasp-ui.png)

When doing grasping, the user can select object category and then press
*Grasp* button. Categories are predefined in configuration file. Each
category has a name, target configuration of SDH joints and desired
forces for all fingers. In the UI, user can see names and corresponding
maximum forces. After executing the grasp, user can decide if it was
successful using tactile data visualization.

## ROS API

TBD
