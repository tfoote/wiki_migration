## Overview

This package contains launch files for using a Microsoft Kinect using
the libfreenect library. This folder replicates the API offered by
[openni_launch](openni_launch) in an effort to maintain maximum
compatibility with the OpenNI driver. Differences are mentioned below.

To use this package, please refer to [openni_launch](openni_launch) and
[rgbd_launch](rgbd_launch) documentation. The migration guide to/from
the OpenNI driver is documented [here](freenect_camera#Migration_guide).

The main launch script can be run using the following command:
```
roslaunch freenect_launch freenect.launch
```

## Modifications from openni_launch

`freenect_launch` contains a few modifications from
[openni_launch](openni_launch) apart from running the libfreenect based
driver. These are documented below.

### freenect_launch vs openni_launch

-   `freenect.launch` does not support selecting the Kinect using the
    USB bus address. It also does not support every image mode provided
    by `openni.launch`. See the
    [migration guide](http://ros.org/wiki/freenect_camera#Migration_guide)
    for more info.
-   `freenect.launch supports` additional parameters for launching
    kinects under different namespaces. See `freenect-ns.launch` for
    an example.
-   `freenect.launch` includes parameters for enabling diagnostics
    support in the freenect_camera driver. Useful for debugging a
    working system. See `freenect-diagnostics.launch` for an example
    on how to use these parameters.
-   `freenect.launch` can also enable verbose libfreenect output.
    Useful for debugging errors. Use `freenect-debug.launch` to see
    how to enable verbose output.

### Additional Launch Files

There are a few additional launch files in `freenect_launch` that
demonstrate running a different constellation of nodelets. This is
useful for launching the minimum set of required processing nodelets, as
well as avoid unnecessary warnings during launch. For example:

-   `freenect-xyz.launch` - provides the pointcloud
    `/camera/depth/points`. Disables device registration.
-   `freenect-registered-xyzrgb.launch` - provides the pointcloud
    `/camera/depth_registered/points`. Enables device registration.
