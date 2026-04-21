## Overview

OpenNI is an open-source framework for "natural interaction" - using
your hands and body to interact with your digital devices. See
[OpenNI.org](http://openni.org) for more information about OpenNI.

Most ROS users will not need to use OpenNI directly.
[openni_camera](openni_camera) already implements a fully-featured ROS
camera driver on top of OpenNI. See [openni_kinect](openni_kinect) to
get started with your Kinect in ROS.

In Electric and Diamondback, to use OpenNI directly in your packages you
would depend on the `openni` wrapper package. As of Fuerte the
`openni` package is deprecated, and you should link against the system
installation of OpenNI as described in the
[migration guide](#Fuerte_migration_guide).

## Repositories

Willow Garage maintains the system installs of OpenNI (the framework)
and ps-engine (the device driver from !PrimeSense) required by ROS.
These track the [OpenNI](https://github.com/OpenNI/OpenNI) and
[PrimeSense/Sensor](https://github.com/PrimeSense/Sensor) projects on
!GitHub.

We apply some patches to the !GitHub sources (e.g. for recognizing
Kinects, as well as the ASUS Xtion and !PrimeSense's prototype
devices). These patches and build scripts are located in our
[openni/drivers](https://kforge.ros.org/openni/drivers) project.

## Fuerte migration guide

### manifest.xml (depending on OpenNI)

Instead of depending on the `openni` package, declare the following
[rosdeps](rosdep) in your [manifest.xml](Manifest):


```
<rosdep name="openni-dev" />
<rosdep name="ps-engine" />
```



Now `rosdep install MY_AWESOME_PACKAGE` will install OpenNI and the
`ps-engine` device driver.

If you provide headers included by code in other packages, and those
headers use OpenNI, then you must also export the flags to find OpenNI:


```
<export>
  <cpp cflags="-I/usr/include/openni" />
</export>
```



### CMakeLists.txt (linking against OpenNI)

The OpenNI headers are installed in `/usr/include/openni`. The
libraries are in the standard search path `/usr/lib`. In your
[CMakeLists.txt](rosbuild/CMakeLists), add the include directory:


```
include_directories(/usr/include/openni)
```



And link your binaries: 

```
rosbuild_add_executable(my_awesome_demo src/my_awesome_demo.cpp)
target_link_libraries(my_awesome_demo OpenNI)
```



### my_code.cpp (using OpenNI in your code)

You can access the OpenNI C++ wrapper in your code with:


```cplusplus
#include <XnCppWrapper.h>
```



See the [OpenNI documentation](http://openni.org/Documentation/) for
more information.
