## Overview

This package contains a ROS driver node for
[Allied Vision Tech Gigabit Ethernet (GigE) cameras](http://www.alliedvisiontec.com/us/products/cameras/gigabit-ethernet/manta.html).
It is built on top of the [Prosilica GigE SDK](prosilica_gige_sdk).

The ROS API of this package is stable. The driver node has been tested
extensively with the
[GC2450C](http://www.alliedvisiontec.com/us/products/cameras/gigabit-ethernet/prosilica-gc/gc2450.html)
model, which was used in the Willow Garage
[Milestone 2](http://www.willowgarage.com/blog/2009/06/03/watch-milestone-2).
The node should work with any AVT/Prosilica GigE camera, and we welcome
reports of use with other cameras.

This page and the [tutorials](prosilica_camera/Tutorials) cover expected
use of this package. Features of interest to advanced users only are
documented [here](prosilica_camera/Advanced).

For basic vision processing of camera images, see the
[image_pipeline](image_pipeline).

## Nodes



```clearsilver
name = prosilica_node
desc = ROS driver for Prosilica GigE cameras. Note that the ROS API varies depending on whether the driver is in streaming or polled mode. In streaming mode it publishes to `camera/image_raw` and `camera/camera_info` like any other camera. In polled mode it publishes on request to a client-specified namespace, following the [[polled_camera]] protocol.<<BR>><<BR>>[[image_transport]] is used for all image publications.
pub {
  group.0 {
    name = Streaming mode
    0.name = camera/image_raw
    0.type = sensor_msgs/Image
    0.desc = The raw image topic.
    1.name = camera/camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = Calibration info for each image.
  }
  group.1 {
    name = Polled mode
    desc = There may be multiple clients, each with their own `response_namespace`. These topics are only published in response to the `request_image` service.
    0.name = <response_namespace>/image_raw
    0.type = sensor_msgs/Image
    0.desc = The polled image topic for a particular client.
    1.name = <response_namespace>/camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = The corresponding camera state.
  }
}
srv {
  group.0 {
    0.name = set_camera_info
    0.type = sensor_msgs/SetCameraInfo
    0.desc = Sets the calibration parameters stored internally on the camera.
  }
  group.1 {
    name = Polled mode
    0.name = request_image
    0.type = polled_camera/GetPolledImage
    0.desc = Captures an image and publishes it in the namespace specified by the request message. Returns the timestamp.
  }
}
param {
group.0 {
name=Camera selection
desc=If `~ip_address` is set, the node opens the camera at that IP. If only `~guid` is set, the node opens the camera with that unique ID. If both, the camera is opened by IP address and the GUID verified. If neither, the node opens the first available camera.
  0.name = ~ip_address
  0.type = string
  0.desc = IP address of the camera to open.
  1.name = ~guid
  1.type = string
  1.desc = Unique ID of the camera to open.
}
}
```



## Command-line tools

### set_ip

Sets the camera to a fixed IP address. The camera must be visible to
[ListCameras](prosilica_gige_sdk#ListCameras), and must be the only
camera listed. The camera must be unopened (i.e. `prosilica_node`
should not be running). This tool is normally used once to configure a
new camera (see the [tutorials](prosilica_camera/Tutorials)).

Usage: 

```
$ set_ip <IP address>
```


