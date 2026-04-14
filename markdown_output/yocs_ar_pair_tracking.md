# Overview

Configured by two AR Markers this package tracks the markers and
computes a relative pose from the robot to the midpoint(of the baseline)
between two markers.

## Why two markers

You can do this with a single ar marker - it will supply you with all
the information you need - a full six degrees of position and
orientation information. However, the orientation data can often be
quite dodgy. Detection rates and the position data on the other hand is
quite reliable, so here we use position data from the two ar markers to
provide more robustness than we could get with ar marker data from one.

# Usage

The node can track a multiple pairs of AR markers. The AR Pair lists are
configurable through subscriber topic.

[Client source code](https://github.com/yujinrobot/yujin_ocs/blob/indigo/yocs_ar_pair_tracking/src/client/client.cpp)
explains what to configure.

## ROS APIs

```clearsilver
node {
 0{
  name = yocs_ar_pair_tracking_node
  descp = Provides ros handles to track AR Pairs, and robot's relative pose.
  param{
   0{
     name = publish_transforms
     type = bool
     default = true
     desc = Publish transform tree
    }
    1{
     name = global_frame
     type = string
     default = ar_global
     desc = global frame of robot. e.g) map
    }
    2{
     name = marker_frame
     type = string
     default = camera_rgb_optical_frame
     desc = frame where marker is detected.
    }
    3{
     name = base_frame
     type = string
     default = base_footprint
     desc = robot's root frame
    }
  }
  sub{
  0{
    name = update_ar_pairs
    type = yocs_msgs/ARPairList
    desc = Updates a list of ar pairs to track.
   }
  }
  pub{
  0{
    name = ~spotted_markers
    type = string
    desc = string identifying which markers are spotted - 'none', 'left', 'right', 'both'.
  }
  1{
    name = ~initial_pose
    type = geometry_msgs/PoseWithCovarianceStamped
    desc = pose with covariance stamped for use to set an initial pose for amcl (assuming /map is at the base of the midpoint of the two ar markers.
  }
  2{
    name = ~relative_target_pose
    type = geometry_msgs/PoseStamped
    desc = 2d pose between sensor and target location, use for an approach controller.
  }
 }
}
```
