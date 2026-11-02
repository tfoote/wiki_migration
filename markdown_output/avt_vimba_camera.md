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

### avt_vimba_camera_node

ROS driver for AVT GigE cameras. Note that the ROS API varies depending
on the driver streaming mode.\
\
[image_transport](https://index.ros.org/p/image_transport) is used for
all image publications.

#### Published Topics

##### Streaming mode

- `camera/image_raw`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  The raw image topic.
- `camera/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Calibration info for each image.

#### Services

- `set_camera_info`
  ([sensor_msgs/srv/SetCameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/srv/SetCameraInfo.html)):
  Sets the calibration parameters stored internally on the camera.

#### Parameters

##### Camera selection

If `ip_address` is set, the node opens the camera at that IP. If only
`guid` is set, the node opens the camera with that unique ID. If both,
the camera is opened by IP address and the GUID verified. If neither,
the node opens the first available camera.

- `~ip_address` (`string`): IP address of the camera to open.
- `~guid` (`string`): Unique ID of the camera to open.
