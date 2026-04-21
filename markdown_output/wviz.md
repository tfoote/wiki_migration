# Overview

The goal of wviz is to provide web based visualization similar in the
webgl enabled web browsers without any required plugins or additional
software. wviz also allows users to view data on remote systems running
ROS without requiring ROS be installed on their local machine. The goal
of the wviz project is to provide visualization capabilities much like
those of rviz with additional mechanisms to allow the user to control
the robot.

![Cameras and Robot Model in Wviz\|width=250](attachment:wviz_cameras.png)
![Interactive Markers in Wviz\|width=250](attachment:wviz_intmarkers.png)
![PCL2 in Wviz\|width=250](attachment:wviz_pcl_filter.png)

Figures above show the currently available visualization.

## Currently Implemented Display Types

1\. Image 1. Axes 1. Robot Model 1. Grid 1. Laser Scan 1. TF 1. Point
Cloud 2 1. Interactive Markers 1. Markers

## Display Types That Are Not Implemented

1\. Map 1. Grid Cells 1. Path 1. Pose 1. Pose Array 1. Marker Array 1.
Camera

# Installation

To use wviz, there should be a web server and rosbridge_server running,
either on your computer or somewhere on the network accessible by your
computer.

Wviz is depending on several packages in
[bosch_web_visualization](bosch_web_visualization) stack. Please see
[this page](bosch_web_visualization) for installation.

/\* If you downloaded the stack using apt-get you should run
postinstallation.sh. See description of the file below. \*/

# Launching



```
$ roslaunch wviz wviz.launch
```



Should launch all the nodes you need for visualizing your simulator or
robot over the web.

# Tutorials

Please see the [introduction tutorial here](wviz/Tutorials).

# Files

## Makefile.wviz

If you check out the stack from the repository you will need to make it.
When you make the stack, this file runs, and creates symbolic links to
several javascript files provided in different packages (such as
rosjs_resources, rosjs_common and rosjs_visualization).
