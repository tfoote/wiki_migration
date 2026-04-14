## \-\--\>\>\> The Dokumentation is currently outdated, March 2011\<\<\<\-\-\-\--

## Overview

The checkerboard_detection package can be used to determinate the
position and the orientation of a checkerboard of the known size within
an image and calibration information (\'\'\'checkerboard_pose
node\'\'\'). The position of the board/camera will be published as
[tf frame](tf). In the background the node uses the OpenCV functions
cv::findChessboardCorners, cvFindCornerSubPix and cv::solvePnP. The pose
can be optional stored in a yml file. Stored data can be published again
with using by using \'\'\'static_pose node\'\'\' with constant frequency
or synchronized with published frames using the \'\'\'checkerboard_pose
node\'\'\'.

  -- ------------------------------------------------------------------------------------------------------------- --
     \<tablewidth=\"100px\" tablestyle=\"text-align: center;\"\> ![](attachment:boardpose.jpg) checkerboard pose   
     ![](attachment:camerapose.jpg) camera pose                                                                    
  -- ------------------------------------------------------------------------------------------------------------- --

## Nodes

```clearsilver
node.0 {
name = checkerboard_pose
desc = This node detects a checkerboard and publishes the camera or board pose, the pose can optional stored in a yml file.
sub {
0.name = /image
0.type = sensor_msgs/Image
0.desc = The image topic. Images from this topic are passed to checkerboard_detector for analysis.
1.name = /camera_info
1.type = sensor_msgs/CameraInfo
1.desc = The camera info topic. This contains the calibration information.
}
pub {
1.name = visualization_marker
1.type = visualization_msgs/Marker
1.desc = Visualization marker for [[rviz]]
}
param {
0.name = base_frame
0.type = string
0.desc = name of the tf base
0.default = `"base_link"`
1.name = frame_id
1.type = string
1.desc = name of the published tf
1.default = `"checkerboard_link"`
2.name = publish_camera_pose
2.type = bool
2.desc = when true it will publish the camera pose, when false it will publish the board pose
2.default = false
3.name = marker_ns
3.type = string
3.desc = Marker name space
3.default = `"checkerboard"`
4.name = pose_file
4.type = string
4.desc = if set then on every iteration the pose will be saved to this file or if the read_pose_file == true it will be used as source to publish stored data.
4.default = empty
5.name = read_pose_file
5.type = bool
5.desc = if true it will read a stored pose file and publish data on every received frame without running any detection
5.default = false
6.name = draw_debug_image
6.type = bool
6.desc = when true opencv window will be opened and the checkerboard will be drawn
6.default = false
7.name = publish_tf_link
7.type = bool
7.desc = when false no tf frames will be published
7.default = true
8.name = publish_rviz_marker
8.type = bool
8.desc = when false no marker will be published
8.default = true
9.name = publish_last_success
9.type = bool
9.desc = when true the last seen board pose will be published even if it is out of the current view
9.default = true
10.name = use_sub_pixel
10.type = bool
10.desc = when true sub pixel accuracy is used
10.default = true
11.name = checkerboard_width
11.type = int
11.desc = number of inner corners in x direction
11.default = 8
12.name = checkerboard_height
12.type = int
12.desc = numebr of inner corners in y direction
12.default = 6
13.name = checkerboard_box_width
13.type = double
13.desc = size of one rectangle in x direction (note that you can change Z-angle by setting this value to minus)
13.default = 0.028
14.name = checkerboard_box_height
14.type = double
14.desc = size of one rectangle in y direction
14.default = 0.028
15.name = frame_rate
15.type = double
15.desc = "not used"
15.default = 1.0
16.name = skip_frames
16.type = int
16.desc = on 0 the node provides only service functionality, 1 means it tries to find the board in every frame, 2 in every second frame and so on ...
16.default = 1.0
17.name = service_name
17.type = string
17.desc = name under which the pose service is provided
17.default = `"pose"`
}
srv {
  0.name = pose --> defined by the shared parameter `"service_name"`
  0.type = checkerboard_detection/GetPose
  0.desc = the pose of the board or the camera relative to the base_frame (the names are defined by the parameters)
}

prov_tf{
0.from = base_frame (name is defined by the parameter base_frame)
0.to = frame_id (name is defined by the parameter frame_id)
0.desc = the pose of the board or the camera relative to the base_frame (the names are defined by the parameters)
}
}
node.1 {
name = static_pose
desc = This node publishes a stored pose with a constant frequency.
param {
0.name = pose_file
0.type = string
0.desc = this file includes the transformation details, and will be created with dummy values if it does not exist
0.default = empty
1.name = frame_rate
1.type = double
1.desc = "loop frequenz "
1.default = 10.0
2.name = service_name
2.type = string
2.desc = name under which the pose service is provided
2.default = `"pose"`
}
srv {
  0.name = pose --> defined by the shared parameter `"service_name"`
  0.type = checkerboard_detection/GetPose
  0.desc = the pose of the board or the camera relative to the base_frame (the names are defined by the parameters)
}
prov_tf{
0.from = base_frame (name is defined by the parameter stored in the yml file)
0.to = frame_id (name is defined by the parameter stored in the yml file)
0.desc = the pose of the board or the camera relative to the base_frame
}
}
```
