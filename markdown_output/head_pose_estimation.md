## Overview

This package provides 6-DoF head pose estimation from depth data.
![](attachment:head_pose.png)

## Installation

## Nodes

```clearsilver
node.0 {
  name = head_pose_estimation
  desc = Node for performing head pose estimation
  param {
    0.name = tree_path
    0.type = string
    0.desc = Defaults to string("trees/tree")

    1.name = ntrees
    1.type = double
    1.desc = Defaults to 10

    2.name = max_variance
    2.type = double
    2.desc = Defaults to 800.0

    3.name = larger_radius_ratio
    3.type = double
    3.desc = Defaults to 1.0

    4.name = smaller_radius_ratio
    4.type = double
    4.desc = Defaults to 6.0

    5.name = stride
    5.type = double
    5.desc = Defaults to 5

    6.name = head_threshold
    6.type = double
    6.desc = Defaults to 400

    7.name = head_target_frame
    7.type = string
    7.desc = Defaults to string("/camera_depth_frame")

    8.name = angular_bias_roll
    8.type = double
    8.desc = Defaults to 0.0

    9.name = angular_bias_pitch
    9.type = double
    9.desc = Defaults to 0.0

    10.name = angular_bias_yaw
    10.type = double
    10.desc = Defaults to 0.0

  }
  sub {
    0.name = cloud
    0.type = sensor_msgs/PointCloud2
    0.desc = The input point cloud

    1.name = /face_detector/people_tracker_measurements_array
    1.type = people_msgs/PositionMeasurementArray
    1.desc = Face detections

  }
  pub {
    0.name = head_pose
    0.type = geometry_msgs/PoseStamped
    0.desc = The head pose output

  }
}
```

## Example Usage

To run the head pose estimator with a Kinect sensor, first start up the
openni driver from [openni_launch](openni_launch).

estimator.launch runs the estimator with default parameters. Assuming
the Kinect camera namespace is `camera`, estimator.launch can be run
with `roslaunch head_pose_estimation estimator.launch`.
