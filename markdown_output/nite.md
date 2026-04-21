## Overview

NITE is a binary distribution from !PrimeSense offering skeleton
tracking, hand point tracking, and gesture recognition. It is integrated
with the OpenNI framework. See
<http://www.primesense.com/technology/nite3> for more information about
NITE.

As a ROS user, you may find it more convenient to use
[openni_tracker](openni_tracker) than NITE directly. `openni_tracker`
uses NITE to track your skeleton, and publishes the skeleton frames over
[tf](tf).

In Electric and Diamondback, to use NITE directly in your packages you
would depend on the `nite` wrapper package. As of Fuerte the `nite`
package is deprecated, and you should link against the system
installation as described in the
[migration guide](#Fuerte_migration_guide).

## Fuerte migration guide

### manifest.xml (depending on NITE)

Instead of depending on the `nite` package, declare the following
[rosdeps](rosdep) in your [manifest.xml](Manifest):
```
<rosdep name="openni-dev" />
<rosdep name="ps-engine" />
<rosdep name="nite-dev"/>
```

Now `rosdep install MY_AWESOME_PACKAGE` will install OpenNI, the
`ps-engine` device driver, and NITE.

If you provide headers included by code in other packages, and those
headers use OpenNI and/or NITE, then you must also export the flags:
```
<export>
  <cpp cflags="-I/usr/include/openni -I/usr/include/nite" />
</export>
```

### CMakeLists.txt (linking against NITE)

The OpenNI and NITE headers are installed in `/usr/include/openni` and
`/usr/include/nite`, respectively. In your
[CMakeLists.txt](rosbuild/CMakeLists), add the include directories:
```
include_directories(/usr/include/openni /usr/include/nite)
```

NITE is loaded dynamically by the OpenNI framework, so link your
binaries against OpenNI: ```
rosbuild_add_executable(my_awesome_demo src/my_awesome_demo.cpp)
target_link_libraries(my_awesome_demo OpenNI)
```

### my_code.cpp (using NITE in your code)

You can access the OpenNI C++ wrapper in your code with:
```cplusplus
#include <XnCppWrapper.h>
```

NITE is a module providing APIs like `UserGenerator`. See the
[OpenNI documentation](http://openni.org/Documentation/) for more
information.
