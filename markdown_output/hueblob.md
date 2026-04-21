## Overview

The tracking is separated into two main steps:

-   2d blob tracking using OpenCV histogram computation feature,
-   3d position computation using a disparity image.

These two steps are available as nodelets which can be combined into a
unique node. It also provides the ability to realize the whole vision
process using the ROS vision pipeline into one single process.

## ROS API



```clearsilver
name = tracker_2d
desc = hue color blob 2d tracking node

param {
  0.name = ~image
  0.type = std_msgs/String
  0.desc = topic name streaming images on which the blob will be tracked
  0.default = left/image_rect_color

  1.name = ~name
  1.type = std_msgs/String
  1.desc = model name
  1.default = rose

  2.name = ~model
  2.type = std_msgs/String
  2.desc = model image
  2.default = package://hueblob/data/models/ball-rose-3.png
}
```





```clearsilver
name = projector
desc = Use disparity information to retrieve tracked color blob 3d position
param {
  0.name = ~name
  0.type = std_msgs/String
  0.desc = object name

  1.name = ~frame_name
  1.type = std_msgs/String
  1.desc = Object frame name
  1.default = roseball
}
```





```clearsilver
name = monitor
desc = Graphical tool displaying the tracking result
param {
  0.name = ~name
  0.type = std_msgs/String
  0.desc = object name

  1.name = ~image
  1.type = std_msgs/String
  1.desc = topic name streaming images on which the blob will be tracked
  1.default = left/image_rect_color
}
```



## Tutorial



```shell
roslaunch hueblob track2-nodelet.launch
```



## Report a bug

Use !GitHub to
[report a bug or suggest a feature](https://github.com/laas/hueblob/issues).
