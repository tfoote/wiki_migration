## About

This package contains an USB camera driver which is almost compatible to
[usb_cam](http://wiki.ros.org/usb_cam) but based on
[ros_control](http://wiki.ros.org/ros_control). Major enhancements over
usb_cam are;

-   impremented as a nodelet
-   supports h264 pixel format (1/10 network usage compared with mjpeg)
-   publishes raw packets from the camera (1/10 cpu usage and less
    latency compared with decoding mjpeg packets in the node)
-   accepts 3rd party controllers

[Slides from ROS Japan UG #28 (in Japanese)](https://drive.google.com/file/d/15ueFzd4BfJbSNH38vfEatP0qbntPlJCy/view)

## Nodelets

```clearsilver
name = usb_cam_hardware/USBCamHardware
desc = an USB camera driver based on ros_control
pub {
 0.name = <controller-defined>
 0.type = <controller-defined>
 0.desc = see the controller section below
}
param {
 0.name = ~video_device
 0.type = string
 0.default = "/dev/video0"
 0.desc = path to the camera device
 1.name = ~image_width
 1.type = int
 1.default = 640
 1.desc = image width in pixels
 2.name = ~image_height
 2.type = int
 2.default = 480
 2.desc = image height in pixels
 3.name = ~pixel_format
 3.type = string
 3.default = "mjpeg"
 3.desc = pixel format of the camera device. supported formats are "grey", "h264", "mjpeg", "rgb24", "uyvy", and "yuyv".
 4.name = ~framerate
 4.type = int
 4.default = 30
 4.desc = desired framerate per second
}
```

## Controllers

All topics and parameters are defined in each controller\'s namespace

```clearsilver
name = usb_cam_controllers/CameraInfoController
desc = publishes camera information syncronized to packets from the camera
pub{
 0.name = camera_info
 0.type = sensor_msgs/CameraInfo
 0.desc = camera info
}
param {
 0.name = camera_frame_id
 0.type = string
 0.default = "head_camera"
 0.desc = camera frame id
 1.name = camera_info_url
 1.type = string
 1.default = ""
 1.desc = camera info URI
 2.name = camera_name
 2.type = string
 2.default = "head_camera"
 2.desc = camera name
```

```clearsilver
name = usb_cam_controllers/PacketController
desc = publishes raw packets from the camera as images
pub {
 0.name = image
 0.type = sensor_msgs/Image
 0.desc = images in raw image format
}
param {
 0.name = image_width
 0.type = int
 0.default = 640
 0.desc = value of Image::width
 1.name = image_height
 1.type = int
 1.default = 480
 1.desc = value of Image::height
 2.name = encoding
 2.type = string
 2.default = "bgr8"
 2.desc = value of Image::encoding
 3.name = skip
 3.type = int
 3.default = 0
 3.desc = number of packets skipped after publishment. useful to throttle network usage.
}
```

```clearsilver
name = usb_cam_controllers/CompressedPacketController
desc = publishes raw packets from the camera as compressed images
pub {
 0.name = packet
 0.type = sensor_msgs/CompressedImage
 0.desc = compressed images
}
param {
 0.name = format
 0.type = string
 0.default = "jpeg"
 0.desc = value of CompressedImage::format
 1.name = skip
 1.type = int
 1.default = 0
 1.desc = number of packets skipped after publishment. useful to throttle network usage.
}
```

```clearsilver
name = usb_cam_controllers/MjpegController
desc = decodes mjpeg-compressed packets and publishes decoded images
pub {
 0.name = image
 0.type = sensor_msgs/Image
 0.desc = decoded images
}
```

```clearsilver
name = usb_cam_controllers/H264Controller
desc = decodes h264-compressed packets and publishes decoded images
pub {
 0.name = image
 0.type = sensor_msgs/Image
 0.desc = decoded images
}
```

```clearsilver
name = usb_cam_controllers/RGB24Controller
desc = converts rgb-formatted packets to bgr images and publishes them
pub {
 0.name = image
 0.type = sensor_msgs/Image
 0.desc = bgr-formatted images
}
param {
 0.name = image_width
 0.type = int
 0.default = 640
 0.desc = value of Image::width
 1.name = image_height
 1.type = int
 1.default = 480
 1.desc = value of Image::height
}
```

```clearsilver
name = usb_cam_controllers/UYVYController
desc = converts uyvy-formatted packets to bgr images and publishes them
pub {
 0.name = image
 0.type = sensor_msgs/Image
 0.desc = bgr-formated images
}
param {
 0.name = image_width
 0.type = int
 0.default = 640
 0.desc = value of Image::width
 1.name = image_height
 1.type = int
 1.default = 480
 1.desc = value of Image::height
}
```

```clearsilver
name = usb_cam_controllers/YUYVController 
desc = converts yuyv-formatted packets to bgr images and publishes them
pub {
 0.name = image
 0.type = sensor_msgs/Image
 0.desc = bgr-formatted images
}
param {
 0.name = image_width
 0.type = int
 0.default = 640
 0.desc = value of Image::width
 1.name = image_height
 1.type = int
 1.default = 480
 1.desc = value of Image::height
}
```

## Examples

See the
[github repository](https://github.com/yoshito-n-students/usb_cam_hardware).

## Related ROS packages

[codec_image_transport](https://github.com/yoshito-n-students/codec_image_transport)

-   for subscriber-side decoding of h264 packets published by the
    CompressedPacketController
