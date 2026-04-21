## Overview

This package is used to calibrate the intrinsic parameters of the
camera.

## Hardware Requirements

Point Grey Chamelon USB2.0 Camera

## Software Requirements

Point Grey flyCapture SDK

## Usage



```shell
rosrun dlut_vision pgr_camera [video_mode] [frame_rate]
```

 \[video_mode\] : 1280x960 or 640x480

\[frame_rate\] : 15 or 7.5

## Nodes



```clearsilver
node.0 {
name = pgr_camera
desc = This node is used to generate the file "Intrinsics.xml" and the file "Distortion.xml".

pub {
0{
name = /pgr_camera/image
type = sensor_msgs/ImagePtr
desc = Publish the image information.
}

}
}
```



## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.
