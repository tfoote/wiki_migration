## Deprecated

Please use the [uvc_camera](uvc_camera) package's
[stereo_node](uvc_camera#Stereo) or nodelet, both of which provide an
interface that's compatible with `uvc_stereo`.

## Nodes



```clearsilver
node.0 {
 name = uvc_stereo
 desc = `uvc_stereo` publishes a synchronized pair of ROS cameras using two UVC cameras.
 pub{
  0.name= left/image_raw
  0.type= sensor_msgs/Image
  0.desc= Image from left camera
  1.name= left/image_raw/compressed
  1.type= sensor_msgs/CompressedImage
  1.desc= Image from left camera (using [[compressed_image_transport]])
  2.name= left/camera_info
  2.type= sensor_msgs/CameraInfo
  2.desc= Information about left camera
  3.name= right/image_raw
  3.type= sensor_msgs/Image
  3.desc= Image from right camera
  4.name= right/image_raw/compressed
  4.type= sensor_msgs/CompressedImage
  4.desc= Image from right camera
  5.name= right/camera_info
  5.type= sensor_msgs/CameraInfo
  5.desc= Information about right camera
 }
 param{
  0.name= ~left/camera_info_url
  0.default=
  0.type= string
  0.desc= URL to left camera's calibration file. See [[camera_info_manager]].
  1.name= ~right/camera_info_url
  1.default=
  1.type= string
  1.desc= URL to right camera's calibration file.
  2.name= ~left/device
  2.default= /dev/video0
  2.type= string
  2.desc= Path to left camera's device file
  3.name= ~right/device
  3.default= /dev/video1
  3.type= string
  3.desc= Path to right camera's device file
  4.name= ~fps
  4.default= 10
  4.type= int
  4.desc= Frames per second to request from camera
  5.name= ~skip_frames
  5.default= 0
  5.type= int
  5.desc= Number of frames to skip between each published frame
  6.name= ~left/rotate
  6.default= false
  6.type= bool
  6.desc= Left image will be rotated 180 degrees if `true`.
  7.name= ~right/rotate
  7.default= false
  7.type= bool
  7.desc= Right image will be rotated 180 degrees if `true`.
  8.name= ~width
  8.default= 640
  8.type= int
  8.desc= Width of image to request from camera
  9.name= ~height
  9.default= 480
  9.type= int
  9.desc= Height of image to request from camera
  10.name= ~frame_id
  10.default= frame
  10.type= string
  10.desc= TF frame representing position, orientation of left camera
  }
```


