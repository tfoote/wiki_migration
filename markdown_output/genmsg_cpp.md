## Overview

`genmsg_cpp` implements the message generator for the [roscpp](roscpp)
client library. Normal users are not expected to interact or know about
this package. Instead, users are expected to use to use the `genmsg`
and `gensrv` macros in the [CMakeLists.txt](CMakeLists) to perform
message generation for various client libraries.

## Roadmap/Stability

`genmsg_cpp` is currently slated for replacement with a Python-based
implementation, after which it will likely be moved to
[ros_experimental](ros_experimental) to satisfy dependencies for
experimental ROS client libraries.
