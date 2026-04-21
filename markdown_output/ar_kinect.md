## Overview

This package is an ROS wrapper for
[ARToolkit](http://www.hitl.washington.edu/artoolkit/), which improves
marker localization using point cloud data from a Kinect.

[ar_kinect](ar_kinect) has a single node that can be run, which takes
RGB point clouds from the Kinect and outputs a transform between the
camera and a recognized marker. This is based on the `ar_multi` node
from the [ar_pose](ar_pose) package.

The node works by creating an RGB image from the point cloud, finding
the corners of the marker, and then computing a transformation to an
ideal marker geometry using methods from PCL.

## Nodes



```clearsilver
node.0 {
name = ar_kinect
desc = This node tracks multiple AR Markers in an image/point-cloud and displays theirs relative pose.
sub {
2.name = points
2.type = sensor_msgs/PointCloud2
2.desc = The point cloud data which is used for marker detection and localization. In earlier branches, this was directly mapped to /camera/rgb/points.
}
pub {
0.name = ar_pose_markers
0.type = ar_pose/ARMarkers
0.desc = An array of markers, each marker describe the current pose relative to the camera.
1.name = visualization_marker
1.type = visualization_msgs/Marker
1.desc = Visualization marker for [[rviz]]
}
param {
0.name = marker_pattern_list
0.type = string
0.desc = ARToolKit file describing each pattern.
0.default = `"$(find ar_kinect)/data/object_kinect"`
1.name = marker_data_directory
1.type = string
1.desc = Location of ARToolKit files describing each pattern.
1.default = `"$(find ar_pose)"`
2.name = threshold
2.type = double
2.desc = Threshold passed to ARToolKit
2.default = 100
3.name = publish_visual_markers
3.type = bool
3.desc = Option to enable publishing visual markers for rviz
3.default = true
4.name = publish_tf
4.type = bool
4.desc = Enable broadcasting transforms
4.default = true
}
prov_tf{
0{
from = camera_frame_id
to = marker_frames
desc = the pose of markers relative to the camera frame
}
}
}
```


