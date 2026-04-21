## Video

Here's a short video to show what the package does and outputs in rviz.

[Youtube](https://www.youtube.com/watch?v=54i8_37aJoo)

## Usage

This package uses [openni_kinect](openni_kinect) so make sure you have
it already installed on your system. 0 You might want to modify
`launch/kinect.launch` as follows if the package `trainer` isn't
found: ```
<node pkg="rviz" name="rviz" type="rviz" args="display-config $(find ppl_detection)/kinect_detect.vcg"/>
``` 1 Run the driver and rviz using the
following command: ```
roslaunch ppl_detection kinect.launch
``` 2 Run the people detection
node: ```
rosrun ppl_detection kinect_detect
```

Also you may have to modify `c++` code when runtime error (e.g.
segmentation fault) occurs. QA threads like
[this](http://answers.ros.org/question/1310/problems-running-ppl_detection-in-astar-ros-pkg?answer=4980#4980)
might be of help.

## Output

Now that the nodes are running, the output can be viewed on rviz that
was just launched. In rviz, a human would be labelled as human(green
text) and a green polygon would be placed around the human's
pointclouds. The number beside the human label is the tracking number of
that particular human. For any other object, it would be labelled as
non-human(red text).

In addition to visualization, the node also publishes a topic called
people which contains information about the tracking number, xyz
location and distance of the human from the kinect.

## Installation

Depending on your environment, you might need to install
`ros-electric-perception-pcl` (see dependencies page up in this page
or `manifest.xml`).
