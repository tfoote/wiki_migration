## Basic Info

More information including a pointer to our demo video will be posted
soon.

There are two main uses for this package.

1\. Replacing the textured stereo with a point cloud from the kinect in
the manipulation stack 1. Using the system described in the
pr2_playpen/hardware folder for automated data capture of manipulation.

INSTRUCTIONS:

1\. Download gt-ros-pkg and add it to the ROS package path. 1. Make sure
you have the NI stack installed 1. Build the conveyor and playpen system
described in /hardware folder in order to run the full demo.

To see a demo of the playpen, run the following on the computer
controlling the conveyor and playpen:



```
$ rosrun pr2_playpen playpen_server.py
```

 and on the PR2 run:



```
$ roslaunch pr2_playpen/launch_pr2/pr2_UI_segment.launch
```

 This will require the user to select a number
of points in a 2D image. The 3D points inside the polygon defined by the
user are used for the tabletop object segmentation in the manipulation
stack. Points are selected by a left click of the mouse and the user
designates that they are finished with a right click.

We can then run:



```
$ roslaunch pr2_playpen/launch_pr2/pr2_tabletop_manipulation.launch
```

 and



```
$ rosrun pr2_playpen wg_manipulation.py
```

 all on the PR2. This will run a demo where the
PR2 will attempt to grasp each item that is delivered to it at least 2
times before sending a command for the next item to be delivered.

## Design and Setup of Playpen

All parts and dimensions are specified in the /hardware folder which
includes two manuals for constructing the playpen and the conveyor
system as seen below.

![\|height="228px",width="344px"](attachment:playpen_pr2.jpg)
![\|height="227px",width="344px"](attachment:playpen_pr2_shoulder.jpg)

![\|height="146px",width="219px"](attachment:playpen_cone.jpg)
![\|height="146px",width="222px"](attachment:playpen_conveyor.jpg)
![\|height="146px",width="219px"](http://www.ros.org/wiki/pr2_playpen?action=AttachFile&do=get&target=playpen_attached.jpg)

This system is designed to allow the PR2 to manipulate multiple objects
over long periods of time without human interaction.

In order to make this possible and to increase the amount of availble
data that can be mined from the manipulation interactions, we have
custom built a Kinect Sensor mount. The documentation for the mount can
be found at
<http://www.hsi.gatech.edu/hrl-wiki/index.php/Kinect_Sensor_Mount>. We
were able to mount a Kinect to the PR2 head as well as on the conveyor
system. The following is a view in Rviz of the 3D data generated from
the Kinect.

![\|height="469px",width="631px"](attachment:rviz_screenshot.png)

## Autonomous Grasping for 60 Hours

For five days in the month of July, we ran the playpen with our overhead
[grasping code](http://www.ros.org/wiki/pr2_grasp_behaviors) every night
for 12 hours. This meant that each night the PR2 attempted around 800
grasps. Other than initial setup each night, the system was robust
enough to run autonomously for 60 total hours while attempting over 4000
different grasps. See time lapse video below and the data is available
at <ftp://ftp-hrl.bme.gatech.edu/playpen_data_sets/>.

[Youtube](https://www.youtube.com/watch?v=ieS_jzx9aZM)

## Older Work

### Initial Demo

Below is an initial video showing the capabilities of the system. In
this case, we are using the manipulation stack from Willow Garage as
well as a revised version of one of the pick and place demos. In
particular, we are using the Kinect instead of textured stereo and we
require that the head be stationary to aid in segmenting objects from
the table top more easily.

__[Youtube](https://www.youtube.com/watch?v=Fls1WSs5sBE)__

### First Overnight Data Set

We recently (May 2011) ran the playpen with our overhead
[grasping code](http://www.ros.org/wiki/pr2_grasp_behaviors) using
Willow Garage's
[tabletop object detection](http://www.ros.org/wiki/tabletop_object_detector)
and the Kinect for eight hours. We started it at 7:30 PM and it ran
without supervision or human intervention until the specified timeout
eight hours later. We learned a lot about needed changes to our code and
methods of auto detection for success and failure. However, we're very
pleased that the system was robust enough to run overnight.

In the future we hope to objectively compare manipulation code from
different universities as well as capture more useful data for machine
learning (joint torques, tactile sensor readings, etc.).

## Acknowledgements

We'd like to thank Alex Mcneely and Travis Deyle for their work on
early prototyping of the playpen system. We'd also like to acknowledge
Joel Mathew for his work in compiling and building the Solid Works part
assemblies, the assembly manual and the bill of materials which are
included in the /hardware folder.
