

```wiki
'''Newly supported `apriltag_ros` package'''

The April Robotics Lab's Github repository has a supported `apriltag_ros` [[https://github.com/AprilRobotics/apriltag_ros|package]]. The ROS Wiki documentation is  [[apriltag_ros|here]].
```



## Overview

A ROS wrapper for the
[AprilTags C++ library](http://people.csail.mit.edu/kaess/apriltags/).

Currently only supports 36h11 Tag family.

## Nodes



```clearsilver
node.1 {
  name = apriltag_detector_node
  desc = Node to detect apriltags in an image.
  sub {
    0.name = camera_info
    0.type = sensor_msgs/CameraInfo
    0.desc = Camera calibration and metadata.
    1.name = image_rect
    1.type = sensor_msgs/Image
    1.desc = Rectified image to detect tags in.
  }
  pub {
    0.name = tag_detections
    0.type = apriltags_ros/AprilTagDetectionArray
    0.desc = An array of the detected tags.
    1.name = tag_detections_pose
    1.type = geometry_msgs/PoseArray
    1.desc = An array of detected tags as poses.
    2.name = tag_detections_image
    2.type = sensor_msgs/Image
    2.desc = The input image with the detected tags drawn on it.
  }
  prov_tf {
    0.from = sensor_frame_id
    0.to   = tag_frame_id
    0.desc = Publishes a transform from the specified sensor_frame_id to each tag_frame_id
  }
  param {
    0.name = ~sensor_frame_id
    0.type = string
    0.default =
    0.desc = The name of the frame that the tag transforms are published relative to. If unset the frame_id specified in the image header.
  }
}
```



## Nodelets

### apriltags_ros/AprilTagDetectorNodelet

The nodelet functions equivalently to the `apriltag_detector_node`
node.
