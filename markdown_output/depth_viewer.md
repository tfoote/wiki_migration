## Overview

This package provides a single node which allows easy viewing of the
depth image published by the [openni_camera](openni_camera) node. It
automatically scales the depth values into an 8-bit, single channel
image.

## Nodes



```clearsilver
node.0 {
name = depth_viewer
desc = This node displays the Kinect depth image.
sub {
0.name = /camera/depth_image
0.type = sensor_msgs/Image
0.desc = The image topic to display
}
param {
0.name = ~min_range
0.type = double
0.desc = Minimum range of points to be displayed (in meters). Used for scaling depths to 8-bit values. 
0.default = 0.5
1.name = ~max_range
1.type = double
1.desc = Maximum range of points to be displayed (in meters). Used for scaling depths to 8-bit values. 
1.default = 5.5
}
}
}
```


