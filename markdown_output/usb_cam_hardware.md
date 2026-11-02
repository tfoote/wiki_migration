## About

This package contains an USB camera driver which is almost compatible to
[usb_cam](http://wiki.ros.org/usb_cam) but based on
[ros_control](http://wiki.ros.org/ros_control). Major enhancements over
usb_cam are;

- impremented as a nodelet
- supports h264 pixel format (1/10 network usage compared with mjpeg)
- publishes raw packets from the camera (1/10 cpu usage and less latency
  compared with decoding mjpeg packets in the node)
- accepts 3rd party controllers

[Slides from ROS Japan UG #28 (in Japanese)](https://drive.google.com/file/d/15ueFzd4BfJbSNH38vfEatP0qbntPlJCy/view)

## Nodelets

### usb_cam_hardware/USBCamHardware

an USB camera driver based on ros_control

#### Published Topics

- `<controller-defined>` (`<controller-defined>`): see the controller
  section below

#### Parameters

- `~video_device` (`string`, default: `"/dev/video0"`): path to the
  camera device
- `~image_width` (`int`, default: `640`): image width in pixels
- `~image_height` (`int`, default: `480`): image height in pixels
- `~pixel_format` (`string`, default: `"mjpeg"`): pixel format of the
  camera device. supported formats are "grey", "h264", "mjpeg",
  "rgb24", "uyvy", and "yuyv".
- `~framerate` (`int`, default: `30`): desired framerate per second

## Controllers

All topics and parameters are defined in each controller's namespace

### usb_cam_controllers/CameraInfoController

publishes camera information syncronized to packets from the camera

#### Published Topics

- `camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  camera info

#### Parameters

- `camera_frame_id` (`string`, default: `"head_camera"`): camera frame
  id
- `camera_info_url` (`string`, default: `""`): camera info URI
- `camera_name` (`string`, default: `"head_camera"`): camera name

### usb_cam_controllers/PacketController

publishes raw packets from the camera as images

#### Published Topics

- `image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  images in raw image format

#### Parameters

- `image_width` (`int`, default: `640`): value of Image::width
- `image_height` (`int`, default: `480`): value of Image::height
- `encoding` (`string`, default: `"bgr8"`): value of Image::encoding
- `skip` (`int`, default: `0`): number of packets skipped after
  publishment. useful to throttle network usage.

### usb_cam_controllers/CompressedPacketController

publishes raw packets from the camera as compressed images

#### Published Topics

- `packet`
  ([sensor_msgs/msg/CompressedImage](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CompressedImage.html)):
  compressed images

#### Parameters

- `format` (`string`, default: `"jpeg"`): value of
  CompressedImage::format
- `skip` (`int`, default: `0`): number of packets skipped after
  publishment. useful to throttle network usage.

### usb_cam_controllers/MjpegController

decodes mjpeg-compressed packets and publishes decoded images

#### Published Topics

- `image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  decoded images

### usb_cam_controllers/H264Controller

decodes h264-compressed packets and publishes decoded images

#### Published Topics

- `image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  decoded images

### usb_cam_controllers/RGB24Controller

converts rgb-formatted packets to bgr images and publishes them

#### Published Topics

- `image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  bgr-formatted images

#### Parameters

- `image_width` (`int`, default: `640`): value of Image::width
- `image_height` (`int`, default: `480`): value of Image::height

### usb_cam_controllers/UYVYController

converts uyvy-formatted packets to bgr images and publishes them

#### Published Topics

- `image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  bgr-formated images

#### Parameters

- `image_width` (`int`, default: `640`): value of Image::width
- `image_height` (`int`, default: `480`): value of Image::height

### usb_cam_controllers/YUYVController

converts yuyv-formatted packets to bgr images and publishes them

#### Published Topics

- `image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  bgr-formatted images

#### Parameters

- `image_width` (`int`, default: `640`): value of Image::width
- `image_height` (`int`, default: `480`): value of Image::height

## Examples

See the
[github repository](https://github.com/yoshito-n-students/usb_cam_hardware).

## Related ROS packages

[codec_image_transport](https://github.com/yoshito-n-students/codec_image_transport)

- for subscriber-side decoding of h264 packets published by the
  CompressedPacketController
