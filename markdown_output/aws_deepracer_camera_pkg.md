## Overview

The
[DeepRacer Camera ROS package](https://github.com/aws-deepracer/aws-deepracer-camera-pkg)
creates the camera_node which is part of the core AWS DeepRacer
application and will be launched from the
[deepracer_launcher](https://github.com/aws-deepracer/aws-deepracer-launcher).
More details about the application and the components can be found
[here](https://github.com/aws-deepracer/aws-deepracer-launcher).

### License

The source code is released under
[Apache 2.0](https://aws.amazon.com/apache-2-0/).

### Supported ROS Distributions

-   Foxy

## Node Details

```clearsilver
name = camera_node

pub {
  0{
   name = /camera_pkg/video_mjpeg
   type = msg/CameraMsg
   desc = Publisher to publish the single camera or two camera images read from the cameras connected to the USB slots at the front of the device .
   }
  1{
   name = /camera_pkg/display_mjpeg
   type = sensor_msgs/Image
   desc = Publisher to publish one camera image for display purposes in the device console UI.
   }
}

srv {
  1{
   name = media_state
   type = srv/VideoStateSrv
   desc = Service that is called to activate the camera node and start publishing the images to the video_mjpeg and display_mjpeg topics.
  }
}
```
