## Overview

### LaserScan

<<MsgLink(sensor_msgs/LaserScan)>> projected on top of the
<<MsgLink(sensor_msgs/DepthCloud)>>.

![](attachment:Laserscan_pointcloud2.png)

### 3D LaserScan Example

Example view of the <<MsgLink(sensor_msgs/LaserScan)>> working like
a 3D Laserscan.

![](attachment:Laserscann3D.png)

### Top View Laserscan - DepthCloud

The image shows the <<MsgLink(sensor_msgs/LaserScan)>> overlayed in
color on the <<MsgLink(sensor_msgs/DepthCloud)>>. Red is close to
camera, purple is far from camera.

![](attachment:Laserscan_colors.png)

## Node

```clearsilver
node.0 {
 name = iav_depthimage_to_laserscan
 desc = `iav_depthimage_to_laserscan` convert a depth image to a laser scan for use with navigation and localization. Furthermore, it allows the use for one camera or more (launch example for two cameras Asus Xtion Pro Live) and generates only one general laser scan for all of them, i.e. it allows create a 360° laser scan with using up to two cameras. For this just add one subscriber (with callback) and one variable Param (the parameters of the new camera) for each camera. It was implemented a Resolution Mapping that allows a bigger or smaller number of laser points than the resolution of the cameras. The generated laser works like a 3D laser since shows not only what there are directly in front of the camera but what there are below and above as well, ensuring a better environmental vision. This is done through the parameters height_max (> 0) and height_min (< 0).
 sub{
  0.name= image
  0.type= sensor_msgs/Image
  0.desc= Input image of the camera 1.
  1.name= image2
  1.type= sensor_msgs/Image
  1.desc= Input image of the camera 2.
  }
 pub {
  0.name= Laser_Scan
  0.type= sensor_msgs/LaserScan
  0.desc= The output laser scan.  It will output range arrays.
 }
 param {
  0.name= height_min
  0.default= -0.65m
  0.type= double
  0.desc= value < 0 (considering 0 the laser_height), wich limits the height below the laser scan.
  1.name= height_max
  1.default= 0.20m
  1.type= double
  1.desc= value > 0 (considering 0 the laser_height), wich limits the height above the laser scan.
  2.name= Note:
  2.type= the x in following camera's parameters means 1 and 2, the launch file is for two cameras
  2.desc=.
  3.name= cam_x_AOV_h
  3.default= 1.01229097
  3.type= double
  3.desc=  Horizontal angle of view.
  4.name= cam_x_AOV_v
  4.default= 0.785398163
  4.type= double
  4.desc= Vertical angle of view.
  5.name= cam_x_yaw
  5.default= 0.0
  5.type= double
  5.desc= Yaw is positive leftwards.
  6.name= cam_x_pitch
  6.default= 0.0
  6.type= double
  6.desc= Pitch is positive downward.
  7.name= cam_x_offset
  7.default= 0.0
  7.type= double
  7.desc= Offset (short distance) between camera and laser.
  8.name= cam_x_image_width
  8.default= 640
  8.type= int
  8.desc= Image width.
  9.name= cam_x_image_height
  9.default= 480
  9.type= int
  9.desc= Image height.
  10.name= cam_x_focal_length_x
  10.default= 570
  10.type= double
  10.desc= Focal length in x.
  11.name= cam_x_focal_length_y
  11.default= 570
  11.type= double
  11.desc= Focal length in y.
  12.name= cam_x_frame_id
  12.default= camera_link
  12.type= string
  12.desc= Camera header.frame_id.
  13.name= laser_max_range
  13.default= 5
  13.type= double
  13.desc= Max. ranges of the laser.
  14.name= laser_min_range
  14.default= 0.5
  14.type= double
  14.desc= Min. ranges of the laser.
  15.name= laser_max_angle
  15.default= 3.14
  15.type= double
  15.desc= Angle of View of the laser (max).
  16.name= laser_min_angle
  16.default= -3.14
  16.type= double
  16.desc= Angle of View of the laser (min).
  17.name= laser_rays
  17.default= 640
  17.type= int
  17.desc= Amount of rays (for the resolution).
  18.name= laser_output_frame_id
  18.default= laser_link
  18.type= string
  18.desc= Laser header.frame_id.
 }
}
}
```
