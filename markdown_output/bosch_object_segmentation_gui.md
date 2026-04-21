## Overview

This package provides a graphical user interface in form of an rviz
plugin for interactive object segmentation. The segmentation method
comes from the [grabcut_3d](grabcut_3d) package.

This package is based on the following paper:

B. Pitzer, M. Styer, C. Bersch, C. DuHadway, and J. Becker, **Towards
Perceptual Shared Autonomy for Robotic Mobile Manipulation,** in Proc.
IEEE International Conference on Robotics & Automation (ICRA), 2011.
[Link to PDF](http://www.pitzer.de/benjamin/_media/pdf/pitzer11_icra.pdf)

### Installation

To use the interactive segmentation, you will need the trunk of the
[pr2_object_manipulation](pr2_object_manipulation) stack and some
additional packages such as [grabcut_3d](grabcut_3d).

The following [rosinstall](rosinstall) file will get everything for you:

```
- svn: 
    local-name: bosch_object_segmentation_gui
    uri: 'https://bosch-ros-pkg.svn.sourceforge.net/svnroot/bosch-ros-pkg/trunk/stacks/shared_autonomy/bosch_object_segmentation_gui'
- svn: 
    local-name: grabcut_3d
    uri: 'https://bosch-ros-pkg.svn.sourceforge.net/svnroot/bosch-ros-pkg/trunk/stacks/shared_autonomy/grabcut_3d'
- svn: 
    local-name: rviz
    uri: 'https://code.ros.org/svn/ros-pkg/stacks/visualization/trunk/rviz'
- svn: 
    local-name: visualization_msgs
    uri: 'https://code.ros.org/svn/ros-pkg/stacks/common_msgs/trunk/visualization_msgs'
- svn: 
    local-name: interactive_marker_tutorials
    uri: 'https://code.ros.org/svn/ros-pkg/stacks/visualization_tutorials/trunk/interactive_marker_tutorials'
- svn: 
    local-name: interactive_markers
    uri: 'https://code.ros.org/svn/ros-pkg/stacks/visualization/trunk/interactive_markers'
- svn: 
    local-name: ogre_tools
    uri: 'https://code.ros.org/svn/ros-pkg/stacks/visualization_common/trunk/ogre_tools'
- svn: 
    local-name: pr2_object_manipulation
    uri: 'https://code.ros.org/svn/wg-ros-pkg/stacks/pr2_object_manipulation/trunk/'
```

Note: To use the rosinstall file, create a new directory (e.g.
interactive_segmentation), create a file named
*interactive_segmentation.rosinstall* in this folder and paste the above
text into it, go to the directory in a terminal and type

```
rosinstall . interactive_segmentation.rosinstall /opt/ros/electric
source ./setup.sh
rosmake pr2_interactive_manipulation
rosmake bosch_object_segmentation_gui
```

Please refer to the [rosinstall](rosinstall) page for more details.

## Running the Application

On the PR2 launch the interactive manipulation stack

```
roslaunch pr2_interactive_manipulation pr2_interactive_manipulation_robot.launch
```

On a desktop run (after exporting the ROS_MASTER_URI to your robot)

```
roslaunch bosch_object_segmentation_gui pr2_interactive_manipulation_desktop.launch
```

Once rviz is started select the interactive segmentation and wait until
the window opens.

![GrabCut3D GUI\|width=370](attachment:grabcut1.png)
![GrabCut3D GUI\|width=370](attachment:grabcut2.png)
