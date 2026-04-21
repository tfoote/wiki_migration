## Overview

Real Time Streaming Protocol (a.k.a RTSP) is a network control protocol
that IP cams (e.g [foscam](http://foscam.us/)) uses. This package
bridges converts streamed image from ip camera and provides it as ROS
topic.

## Installation



```
> sudo apt-get install ros-<distro>-rocon-rtsp-camera-relay
```



## Execution



```
> export ROCON_RTSP_CAMERA_RELAY_URL=rtsp://YOUR IPCAM URL
 > roslaunch rocon_rtsp_camera_relay rtsp_camera_relay.launch --screen
```



![alt text\|width=50%](attachment:rtsp_camera.png)
