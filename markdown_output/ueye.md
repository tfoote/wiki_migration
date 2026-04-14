## Overview

This package contains a ROS driver node for
[IDS Imaging uEye cameras](https://en.ids-imaging.com/).

The driver node has been tested with the version 4.60
<https://en.ids-imaging.com/download-ueye.html> for USB cameras. Future
versions should be ABI compatible, and therefore should work.

This package can be installed with apt-get. However, the IDS Imaging
driver mentioned above must also be installed.

The driver node has been tested with the following cameras:

-   UI-1225LE-C
-   UI-124xLE-C
-   UI-164xLE-C
-   UI-222xSE-C (two cameras synchronized for stereo)
-   UI-324xCP-C

## Nodes

```clearsilver
name = camera
desc = ROS driver node for uEye cameras.
pub {
  group.0 {
    0.name = image_raw
    0.type = sensor_msgs/Image
    0.desc = The raw image topic.
    1.name = camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = Calibration info for each image.
  }
}
srv {
  group.0 {
    0.name = set_camera_info
    0.type = sensor_msgs/SetCameraInfo
    0.desc = Sets the calibration parameters saved to a file.
  }
}
param {
group.0 {
  0.name = ~cameraId
  0.type = int
  0.desc = Id of the camera to open. Zero for any.
  1.name = ~force_streaming
  1.type = bool
  1.desc = Force camera to stream images. If false, streaming will stop if no nodes subscribe to the image topic.
  2.name = ~hardware_gamma
  2.type = bool
  2.desc = Enable hardware gamma correction if the camera supports it.
  3.name = ~auto_exposure
  3.type = bool
  3.desc = Enable auto-exposure time if the camera supports it.
  4.name = ~exposure_time
  4.type = double
  4.desc = Exposure time in milliseconds if ~auto_exposure is false.
  5.name = ~zoom
  5.type = int
  5.desc = Zoom level with global binning.
  6.name = ~frame_rate
  6.type = double
  6.desc = Image stream rate. The node will not allow ~frame_rate to exceed the limits of the camera with the constraints of other parameters such as ~zoom and ~pixel_clock.
  7.name = ~pixel_clock
  7.type = int
  7.desc = Pixel clock speed for USB in MHz.
  8.name = ~frame_id
  8.type = string
  8.desc = The tf frame_id in the published message headers.
  9.name = ~auto_gain
  9.type = bool
  9.desc = Enable automatic hardware gain if the camera supports it.
  10.name = ~gain_boost
  10.type = bool
  10.desc = Enables constant hardware analog gain boost if the camera supports it.
  11.name = ~gain
  11.type = int
  11.desc = Sets the image hardware gain if ~auto_gain is false.
}
}
``` ```clearsilver
name = framerate
desc = Node that displays the actual rate of an image stream.
sub {
  group.0 {
    0.name = image_raw
    0.type = sensor_msgs/Image
    0.desc = The raw image topic.
  }
}
param {
group.0 {
desc=asdf
  0.name = ~topic
  0.type = string
  0.desc = Topic name of the image stream to subscribe to.
}
}
```

## Usage

### To run stereo cameras

```
$ rosrun ueye stereo
```

You might want to lower resolution by setting the zoom parameter
```
$ rosrun ueye stereo _zoom:=2
```

In case there are multiple cameras connected, you can choose the cameras
that will be used by specifying the camera ids. ```
$ rosrun ueye stereo _lCameraId:=1 _rCameraId:=3
```

### Camera Calibration

The camera node supports calibration with the
[camera_calibration](camera_calibration) package.

There are tutorials on how to run the calibration tool for
[monocular](camera_calibration/Tutorials/MonocularCalibration) and
[stereo](camera_calibration/Tutorials/StereoCalibration) cameras.
