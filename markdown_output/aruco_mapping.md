## Overview

Using [Markers](http://www.uco.es/investiga/grupos/ava/node/26) to
estimate full 6 DOF position only by means of single calibrated camera
is well known approach that has been utilized for quite a long time now.
This package leverages basic [aruco_ros](aruco_ros) functionality and
provides tools to create a map of detected markers in 2D/3D space. It is
designed for **static markers - moving camera **scenario** **and can be
used for various navigation tasks for UAVs, UGVs, etc.

[Youtube](https://www.youtube.com/watch?v=MlOy9qt_K4Y&rel=0)

## Usage

### Marker placement

Mapping utilizes chaining principle:

1\. first marker is identified with world´s origin 1. second marker's
position is computed with respect to first one 1. third's marker
position is computed with respect to second one 1. \...

In order to achieve successfull mapping, everytime when a new marker is
detected, previous marker needs to be visible in the actual image to
allow computing new marker's position. (See
[demonstration video](https://www.youtube.com/watch?t=2&v=3mCu_7Ek2fs)
for better understanding). Keep this principle in mind when placing
markers in your environment and do not overdo their mutual distances.

### Camera calibration

Proper camera calibration strongly affects overall system accuracy.
Aruco mapping expects calibration file in Videre INI format, see the
example of expected calibration file below:

```
# Prosilica camera intrinsics

[image]

width
2448

height
2050

[prosilica]

camera matrix
4827.93789 0.00000 1223.50000
0.00000 4835.62362 1024.50000
0.00000 0.00000 1.00000

distortion
-0.41527 0.31874 -0.00197 0.00071 0.00000

rectification
1.00000 0.00000 0.00000
0.00000 1.00000 0.00000
0.00000 0.00000 1.00000

projection
4827.93789 0.00000 1223.50000 0.00000
0.00000 4835.62362 1024.50000 0.00000
0.00000 0.00000 1.00000 0.00000
``` In order to to calibrate your camera and get
results in INI format, we stongly suggest
[camera_calibrator](http://wiki.ros.org/camera_calibration) package.

### Launch file

Here is an example of launch file to run **Rviz**, **usb_cam** driver
and **aruco_mapping**:

```
<launch>

  <!-- RVIZ -->
  <node name="rviz" pkg="rviz" type="rviz" args="-d $(find aruco_mapping)/launch/aruco_config.rviz" />

   <!--   usb_cam node -->
  <node name="usb_cam" pkg="usb_cam" type="usb_cam_node" output="screen">
    <param name="video_device" value="/dev/video0" />
    <param name="image_width" value="640" />
    <param name="image_height" value="480" />
    <param name="pixel_format" value="mjpeg" />
    <param name="camera_frame_id" value="usb_cam" />
    <param name="io_method" value="mmap"/>
  </node>

  <!-- ArUco mapping -->
  <node pkg="aruco_mapping" type="aruco_mapping" name="aruco_mapping" output="screen">
    <remap from="/image_raw" to="/usb_cam/image_raw"/>

    <param name="calibration_file" type="string" value="$(find aruco_mapping)/data/F100.ini"/>
    <param name="num_of_markers" type="int" value="20" />
    <param name="marker_size" type="double" value="0.135"/>
    <param name="space_type" type="string" value="plane" />
    <param name="roi_allowed" type="bool" value="false" />
  </node>
</launch>
``` In case you use other camera driver, remap
**image_raw** to your topic name. Do not forget to adopt
**calibration_file**, **marker_size** and other params to your setup. If
everything is set and ready, launch the aruco_mapping by following
command:

```
roslaunch aruco_mapping aruco_mapping.launch
```

### Additional image filter

If you are experiencing problems with basic aruco detector caused by
lighting conditions (strong reflections, poor lighting, bad focus) try
to include our
[image filter](https://github.com/SmartRoboticSystems/image_filtering_for_aruco.git)
into your processing pipeline in order to improve the raw image.

[Youtube](https://www.youtube.com/watch?v=fgW7b1jf4R8)

## ROS API

```clearsilver
name = aruco_mapping
desc = Node for Aruco Marker detection and mapping.
sub {
  0.name = image_raw
  0.type = sensor_msgs/Image
  0.desc = subscribe to camera image_raw
}
pub {
  0.name = aruco_markers
  0.type = visualization_msgs/Marker
  0.desc = publishes Marker for visualization purposes
  1.name = aruco_poses
  1.type = aruco_mapping/ArucoMarker
  1.desc = marker ID, visibility, relative and global poses
}
param {
  0.name = calibration_file
  0.type = std_msgs/String
  0.desc = path to txt file with camera calibration data in INI format
  1.name = num_of_markers
  1.type = std_msgs/UInt8
  1.desc = Maximum number of markers to detect and track
  2.name = marker_size
  2.type = std_msgs/Double64
  2.desc = Real marker size in meters
  3.name = space_type
  3.type = std_msgs/String
  3.desc = plane/3D space type
  4.name = roi_allowed
  4.type = std_msgs/Bool
  4.desc = ROI on/off flag
  5.name = roi_x
  5.type = std_msgs/UInt8
  5.desc = ROI start x - coordinate
  6.name = roi_y
  6.type = std_msgs/UInt8
  6.desc = ROI start y - coordinate
  7.name = roi_w
  7.type = std_msgs/UInt8
  7.desc = ROI width
  8.name = roi_h
  8.type = std_msgs/UInt8
  8.desc = ROI height
}

prov_tf{
  0.from = world
  0.to   = camera_pose
  0.desc = Global camera pose
}
```

## Demonstration

Aruco_mapping has been successfully used for autonomous indoor UAV
navigation:

[Youtube](https://www.youtube.com/watch?v=3mCu_7Ek2fs)

## Report a Bug

<<GitHubIssues(SmartRoboticSystems/aruco_mapping)>>
