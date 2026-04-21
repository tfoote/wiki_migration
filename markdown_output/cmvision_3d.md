## Overview

![](attachment:cmvision_3d.png) Cmvision_3d uses the /blobs topic
produced by cmvision, in addition to 3D data from a registered depth
image, to publish both 1. the position of each color blob relative to
its camera frame, and 2. frames in the tf stack for each color.

Frames are broadcasted with the camera's frame_id as their
parent_frame, and from there they can be transformed as necessary.
**Note:** this package depends on cmvision's commit
[fac7a32](https://github.com/utexas-bwi/cmvision/commit/fac7a32665366236397955011734dd1092d977e5#diff-d41d8cd98f00b204e9800998ecf8427e).
This should be released into Hydro, but if it is not yet, make sure to
grab the latest changes.

## Usage

### Selecting Blob Colors

Please see the [cmvision package](http://wiki.ros.org/cmvision) for
instructions to select blob colors, after which you can place your
colors.txt file within the /colors folder, and link to it via modifying
color_tracker.launch.

### Detecting and Projecting Blobs to 3D

You will need to modify launch/color_tracker.launch to do the following:

1\. Set the "image" arg to your image topic. 1. Set the
"depth_image" to your depth image topic (which must be registered
depth to produce meaningful results). 1. Set the "camera_topic" arg to
your camera_topic. 1. Set the "color_file" file parameter to your .txt
colors file, as described in
[cmvision](http://wiki.ros.org/cmvision#Selecting_Blob_Colors).



```
<launch>
        <arg name="image" default="/your/image/topic"/>
        <arg name="depth_image" default="/your/depth_image/topic"/>
        <arg name="camera_topic" default="/your/camera_info/topic"/>
        <!-- Do we want to publish our blobs to tf? -->
        <arg name="publish_tf" default="true"/>


  <node name="cmvision" pkg="cmvision" type="cmvision" args="image:=$(arg image)" output="screen">
          <!-- Location of the cmvision color file -->
          <param name="color_file" type="string"
                 value="$(find cmvision_3d)/colors/yourColors.txt" />
```

 After you've done this, you can proceed to run
both cmvision and color_controller using



```
roslaunch cmvision_3d color_tracker.launch
```



**Note:** This stuff will pretty much work out of the box if you're
running *openni_launch openni.launch depth_registration:= true* on a
Microsoft Kinect, as the defaults for the above arguments are set to the
relevant topics for the Kinect environment.

## Nodes



```clearsilver
node.0 {
  name = color_controller
  desc = Subscribes to /blobs and publishes /blobs_3d, which includes the 3d points of each found color.
  sub {
    0.name = blobs
    0.type = cmvision/Blobs
    0.desc = A list of color blobs and their locations. We project each one of these colors into 3D and republish to /blobs_3d.
    1.name = depth_image
    1.type = sensor_msgs/Image
    1.desc = The '''depth registered image''' topic. Should be remapped to the name of the real depth image topic.
    2.name = camera_topic
    2.type = sensor_msgs/CameraInfo
    2.desc = We need camera info in order to perform the correct calculations in mapping from the image plane to 3D space. Should be remapped to the name of the real camera info topic (e.g, on a Microsoft Kinect this is camera/rgb/camera_info).
  }
  pub {
    0.name = blobs_3d
    0.type = cmvision_3d/Blobs3d
    0.desc = a modified version of cmvision/Blobs that replaces pixel x,y information with geometry_msgs/Point info.
  }
  param {
    0.name = publish_tf
    0.type = bool
    0.desc = Are we going to publish our blobs to tf? NOTE: If there are multiple catches for a single color, it only publishes the one with the largest area.
    0.default = true
  }
}
```


