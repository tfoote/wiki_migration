/!\\ camera_pose has moved to github:
<https://github.com/ros-perception/camera_pose>

## Stability

Note that [kinect_depth_calibration](kinect_depth_calibration) is part
of a \<1.0 stack, and thus it is still unreviewed and unstable. We are,
however, actively using this stack in-house at Willow Garage with good
results, and we\'re actively making improvements along the way.

We would definitely love to hear about any issues you encounter (via
answers.ros.org) or any other feedback you may have during the
development process. Also check out the
[troubleshooting page](kinect_depth_calibration/Troubleshooting).

## Overview

### Kinect only setup

The kinect_depth_calibration package was designed primarily to verify
the intrinsic calibration of the Kinect infrared camera. It does this by
comparing the pose of a checkerboard detected in the infrared image, to
the pose reported by the Kinect\'s internal depth computation.

**High Level Operation**

-   User mounts a checkerboard rigidly in front of a Kinect
-   User covers the Kinect\'s IR projector (e.g. with post-it notes),
    and captures the checkerboard pose in the IR camera.
-   User uncovers the Kinect\'s IR projector, and captures the
    checkerboard 3D pointcloud.
-   The kinect_depth_calibration package computes the difference in
    depth between the two data sets, resulting in a measure for the
    Kinect intrinsic calibration accuracy.

**Requirements**

-   Checkerboard is mounted rigidly in front of the Kinect. It cannot
    move between samples.
-   Kinect IR sensor has its intrinsics calibrated. See
    [openni_camera/calibration](openni_camera/calibration) for more
    details.

**Running** Bring up the Kinect camera first. Then, launch the
calibration: ```
roslaunch kinect_depth_calibration test_calibration.launch image_ns:=camera/ir depth_ns:=camera/depth
```

### Setup with other cameras

You can also use this package to verify both the intrinsics and
extrinsics of an external camera attached to a Kinect.

**Requirements**

-   Checkerboard is mounted rigidly in front of the Kinect. It cannot
    move between samples.
-   Kinect IR sensor has its intrinsics calibrated. See
    [openni_camera/calibration](openni_camera/calibration) for more
    details.
-   Kinect IR camera intrinsics have been verified (see section above)
-   External camera is intrinsicly calibrated (see
    [camera_calibration](camera_calibration))
-   External camera is rigidly attached to the Kinect, and is
    extrinsicly calibrated to the Kinect (see
    [camera_pose_calibration](camera_pose_calibration))

**Running** Bring up the Kinect camera and the external camera. Then,
launch the calibration: ```
roslaunch kinect_depth_calibration test_calibration.launch image_ns:=external_camera/rgb depth_ns:=camera/depth
```
