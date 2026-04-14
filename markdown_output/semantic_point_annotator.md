## Overview

This package provides a node that the
[pr2_navigation_perception](pr2_navigation_perception) package uses for
removing hits on the ground from
\<\<MsgLink(geometry_msgs/PointCloud.msg)\>\> messages.

## API Stability

Since the \<\<MsgLink(geometry_msgs/PointCloud.msg)\>\> message will be
deprecated in the near future, and the code in this package will be
replaced with code using the new !PointCloud format, there are no
guarantees about the stability of this package. After the
[navigation](navigation) stack switches to the new !PointCloud
structure, this package will likely be removed. You should feel free to
use the code in this package, but it will not be supported and is at
your own risk.
