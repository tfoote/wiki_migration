## Overview

This package contains a ROS driver node for
[Allied Vision Tech Gigabit Ethernet (GigE) cameras](http://www.alliedvisiontec.com/us/products/cameras/gigabit-ethernet/manta.html).
It is built on top of the
[VIMBA GigE SDK](http://www.alliedvisiontec.com/emea/products/software/vimba-sdk.html),
the latest SDK from AVT. The prior version of the SDK,
[PvAPI](http://www.alliedvisiontec.com/emea/products/legacy.html) was
used for [prosilica_camera](https://index.ros.org/p/prosilica_camera)

The ROS API of this package is in development. The driver node has been
tested with the
[G-283C](http://www.alliedvisiontec.com/emea/products/cameras/gigabit-ethernet/manta/g-283bc.html)
model and
[G-504C](http://www.alliedvisiontec.com/emea/products/cameras/gigabit-ethernet/manta/g-504bc.html).
The node should work with any AVT/Prosilica GigE camera, and we welcome
reports of use with other cameras.

For basic vision processing of camera images, see the
[image_pipeline](https://index.ros.org/p/image_pipeline).

## Nodes

<a id="NodeAPI"></a>



```clearsilver
name = avt_vimba_camera_node
desc = ROS driver for AVT GigE cameras. Note that the ROS API varies depending on the driver streaming mode.<<BR>><<BR>>[[image_transport]] is used for all image publications.
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
}
srv {
  group.0 {
    0.name = set_camera_info
    0.type = sensor_msgs/SetCameraInfo
    0.desc = Sets the calibration parameters stored internally on the camera.
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
