## Overview

This package provides a ROS Node that will encode a stream of images
into an H264 video stream.

```Keywords```: ROS, AWS, Kinesis

### License

The source code is released under
[LGPL 2.1](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).
However, this package uses `h264_encoder_core` which incorporates
several different encoding components which may further restrict the
license. By default, x264 is used for software encoding, thereby
applying GPL to all of h264_video_encoder.

### Supported ROS Distributions

-   Kinetic
-   Lunar
-   Melodic
