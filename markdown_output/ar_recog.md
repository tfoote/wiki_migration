## System Dependencies

`ar_recog` requires the `libgstreamer0.10-dev` system dependency.

## Making

```
rosmake ar_recog
```

The `ar_recog` package downloads and compiles the ARToolkit. It must
therefore be able to connect to Sourceforge on the internet. This also
accounts for why this step takes rather longer than many compilations.
ARToolkit will only be downloaded once, with the locally cached version
used thereafter.

## Running

To run code that listens to `/image` messages:

```
rosrun ar_recog ar_recog
```

To run code for a specific image message such as one from gscam:

```
rosrun ar_recog ar_recog image:=/gscam/image
```

## Messages and Services

<<MsgSrvDoc(ar_recog False)>>

`ar_recog` publishes two messages tags contains the
<<MsgLink(ar_recog/Tags)>> message, the information about the found
tags

ar/image contains the image with the tags outlined in the image

If the camera image is a rectified one with appropriate camera
parameters, `ar_recog` will use them to determine the mapping between
image space and physical space. However, the rectification pipeline is
slow and camera calibration brittle, so the package also provides
distance mapping with uncalibrated images. To use this feature, it must
know your camera's horizontal angle of view. This can be provided as a
ROS parameter (`aov`), or determined using the
<<SrvLink(ar_recog/CalibrateDistance)>> service.

## Calibrating Distance

**This is only necessary when *not* using a calibrated camera.**

-   Set up a clear, recognized AR tag at a known distance from the
    camera.
-   Start the `ar_recog` node and monitor the `/tags` message
-   Arrange the AR tag and camera so that the tag coordinates are as
    close as possible to the center of the image, and the xRot, yRot and
    zRot are as close as possible to zero. This will minimize
    distortion.
-   Call the <<SrvLink(ar_recog/CalibrateDistance)>> service, where
    `dist` is the distance between the AR tag and the camera in
    millimeters:

```
rosservice call ar/calibrate_distance dist
```

### Tips

-   The more accurately the distance is known, the better `ar_recog`
    is able to undistort the image. Thus you may have to repeat the
    service call a few times until the reported distance converges on
    the value you are providing.
-   Save this aov value to provide as a ROS parameter next time you use
    `ar_recog` with this camera.

## ARToolKit Compatibility/Interoperability

**ar_recog** is compatible with standard ARToolKit pattern and
object_data files. When not used with ROS' [image_proc](image_proc),
`ar_recog` utilizes an ARToolkit `camera_para.dat` file. See the
files within the `bin` directory and the
[ ARToolKit documentation](http://www.hitl.washington.edu/artoolkit/documentation).
