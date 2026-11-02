## Overview

This package provides a node that the
[pr2_navigation_perception](https://index.ros.org/p/pr2_navigation_perception)
package uses for removing hits on the ground from
[geometry_msgs/msg/PointCloud.msg](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PointCloud.msg.html)
messages.

## API Stability

Since the
[geometry_msgs/msg/PointCloud.msg](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PointCloud.msg.html)
message will be deprecated in the near future, and the code in this
package will be replaced with code using the new !PointCloud format,
there are no guarantees about the stability of this package. After the
[navigation](https://index.ros.org/p/navigation) stack switches to the
new !PointCloud structure, this package will likely be removed. You
should feel free to use the code in this package, but it will not be
supported and is at your own risk.
