![\|height="200",width="333"](attachment:Logo-white-medium.jpg)

## Description

This package is used to get poses from Rviz by using the goal tool and
to store them in a XML-file
![\|width="750",height="230"](attachment:pose_manager.png)

## Functionality

To get a Pose you just have to use the destination tool so that rviz
publish the pose in the corresponding topic. You can use this tool if
you need to know a particular pose ( position and orientation ). The
tools works also in simulation mode.

This package subscribes to **move_base/goal **an saves every incoming
Pose in a XML-file. The name of the XML-file is CURRENT_TIMEposen.xml
and will be saved at the location the program starts. The format will
be:

<Pose X="" Y="" Z="" XQ="" YQ="" ZQ="" WQ=""></Pose>

The gotten Pose is also published on the ROS INFO stream for monitoring
or direct copy/paste purposes.

## Usage

Start all needet Components (Look at "Start system)

Then press the "2D Nav Goal" Button.

Click on a desired position on the map.

# > The Pose of this Click on the map is printed on the console and in the xml file.

### Needed software

[Eigen (3.2.0)](http://eigen.tuxfamily.org/index.php?title=Main_Page)

### Start system

1\. You must start the your navigation system, with the standard
ROS-Navigation or asr_mild_navigation.

2\. Start RVIZ

3\. rosrun asr_rviz_pose_manager asr_rviz_pose_manager_node

## ROS Nodes

### Subscribed Topics

**move_base/goal **(geometry_msgs/Pose): The poses to record
