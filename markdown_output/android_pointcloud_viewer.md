android_pointcloud_viewer

-   Author: Omri Lavi (omri AT cogniteam.com)
-   Licence: MIT
-   Source: git
    <https://github.com/cogniteam/android_ros_pointcloud_viewer>
    (branch: Indigo)

This android application extends [rosjava](rosjava) features, to enable
viewing
[ sensor_msgs/PointCloud2](http://docs.ros.org/api/sensor_msgs/html/msg/PointCloud2.html )
messages via ros.

[Youtube](https://www.youtube.com/watch?v=8wnQHwsjWi8)

## Using out-of-the-box

For using this application as-is, without code modifications: 1. Install
the app on your phone, using android-studio. 1. Run the application. 1.
Enter details for ros-master, and press connect. 1. Publish a
PointCloud2 message that you wish to view. \'\'\'\'\'NOTE\'\'\'\'\': it
may take a few seconds (up to 30 seconds) until the message is being
fully processed. Details about the default structure of the message can
be found [here](#structure). 1. Use the different controls available to
view the Pointcloud2 message. Details about the controls can be found
[here](#controls).

## Controls

There are 3 main controls for viewing the PointCloud: 1. A vertical
slider, which can be found on the right side of the screen. Sliding this
contol up will move the camera in (\"step in\"), and sliding it down
will have the same effect to the opposite direction. 1. A 2-dimensional
joystick, which can be found beneath the slider. Use it to move the
camera vertically or horizontally. 1. Gestures: a. \'\'Rotation\'\' -
will rotate the camera on its z-axis (clockwise/counter-clockwise). a.
\'\'1-Finger swiping\'\' - will move the camera\'s view horizontally or
vertically. a. \'\'2-Finger swiping\'\' - will rotate the point cloud on
its center. a. \'\'Double click\'\' - will reset the view, and move the
camera to the center of the point cloud.

## Default structure for PointCloud2 message

By default, each point in the message should have the following fields
(in order): 1. Float representing x. 1. Float representing y. 1. Float
representing z. 1. Empty float (is being discarded). 1. Intensity, which
is used to set each point\'s grayscale color. Parsing of the message can
be easily changed in the code.

## ROS API

```clearsilver
node.0 {
name=android/pcd_view
desc=`android_pcd` is a node which run on the android, that is used for displaying pointclouds.

sub{
0.name= cloud/source
0.type= sensor_msgs/PointCloud2
0.desc= The pointcloud to view
}
```
