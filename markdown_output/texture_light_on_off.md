## Overview

texture_light_on_off processes data from a stereo camera (with textured
light). It is currently used with the [rf_detector](rf_detector)
package.

## Nodes

```clearsilver
node.0{
  name= texture_light_on_off
  desc= `texture_light_on_off` processes the sensor data from a narrow-stereo camera to collect images when textured light is off and stereo-point clouds when texture light is on.
  pub {
    0.name= t_on_off/image
    0.type= sensor_msgs/Image
    0.desc= The narrow stereo image when the texture light is off.
    1.name= t_on_off/dense_cloud
    1.type= sensor_msgs/PointCloud
    1.desc= The narrow stereo point cloud when the texture light is on.
    2.name= t_on_off/sparse_cloud
    2.type= sensor_msgs/PointCloud
    2.desc= The narrow stereo point cloud when the texture light is on.
    3.name= t_on_off/caminfo
    3.type= sensor_msgs/CameraInfo
    3.desc= The narrow stereo camera info.
  }
}
```

**There is a launch file "t_on_off.launch"** to start the process. And
the parameters in the launch file are explained below:

-   image_sequence \-- How many frames that the node will wait for the
    status of the camera to be stable (when the texture light is either
    on or off)?
-   off_exposure \-- The exposure of the camera when texture light is
    off.
-   on_exposure \-- The exposure of the camera when texture light is on.
