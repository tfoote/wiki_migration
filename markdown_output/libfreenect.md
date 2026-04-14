## Overview

[libfreenect](http://openkinect.org/wiki/Main_Page) is a library for
accessing the Microsoft Kinect USB camera. This package downloads
revision
[d1d19df895](https://github.com/OpenKinect/libfreenect/commit/d1d19df8957f8d63a562b310413da15d3e6ef7a1)
from the
[libfreenect repository](https://github.com/OpenKinect/libfreenect).

Starting from Oneiric (Ubuntu 11.10), deb packages for libfreenect are
available. However, the downloaded tarball contains a much newer stable
revision. The main advantage of using this revision over the system
package are:

-   The ability to search for a Kinect through serial number, necessary
    for running multiple Kinects.
-   USB 3.0 Support

The tarball is currently hosted
[here](http://z.cs.utexas.edu/users/piyushk/bwi_share/OpenKinect-libfreenect-master-d1d19df895.tar.gz).

## Report a Bug

Bugs should be reported on the relevant github issues page:
<https://github.com/OpenKinect/libfreenect/issues>

If you would like to submit a patch for the ROS wrapper, please open an
issue here: <https://github.com/piyushk/freenect_stack/issues>
