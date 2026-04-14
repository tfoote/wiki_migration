```wiki
'''Newly supported `apriltag_ros` package'''

The April Robotics Lab's Github repository has a supported `apriltag_ros` [[https://github.com/AprilRobotics/apriltag_ros|package]]. The ROS Wiki documentation is  [[apriltag_ros|here]].
```

## Nodes

```clearsilver
node.0 {
 name = april.ros.TagPublisher
 desc = ROS Wrapper for publishing tags using the April Tag Detection Library
 sub {  
  1.name = image_raw
  1.type = sensor_msgs/Image
  1.desc = Image stream to be used for tag detection
  2.name = camera_info
  2.type = sensor_msgs/CameraInfo
  2.desc = Camera info message corresponding to the image stream
 }
 pub {
  1.name = tags
  1.type = april_msgs/TagPoseArray
  1.desc = Tag information based on detected tags
  2.name = /visualization_marker_array
  2.type = visualization_msgs/MarkerArray
  2.desc = Rviz markers corresponding to detected tags
  3.name = /tf
  3.type = tf/tfMessage
  3.desc = Tag information published on the tf tree
 }
 param {

  1.name = ~tag_family
  1.type = string
  1.desc = The family of tags to be detected
  1.default = `"april.tag.Tag36h11"`

  2.name = ~tag_size
  2.type = double
  2.desc = Tag size (in meters) required to project the tag in 3d space. Different sizes for different tag ids are currently not supported.
  2.default = `0.095`

  3.name = ~use_camera_info
  3.type = bool
  3.desc = Use focal length values from the corresponding camera_info message or not
  3.default = `true`

  4.name = ~focal_length_x
  4.type = double
  4.desc = Focal length in the x axis (in pixels). This value is used if `~use_camera_info` is set to `false`
  4.default = 485.6

  5.name = ~focal_length_y
  5.type = double
  5.desc = Focal length in the y axis (in pixels). This values is used if `~use_camera_info` is set to `false`. This value is typically equal to the focal length in the x axis.
  5.default = `~focal_length_x`

  6.name = ~publish_visualization
  6.type = bool
  6.desc = Publish visualizaion for easy tag display in rviz
  6.default = `true`

  7.name = ~tag_vis_magnification
  7.type = double
  7.desc = Magnify the size of the visualized tag by this amount to make visualization in rviz easier
  7.default = `1.0`

  8.name = ~broadcast_tf
  8.type = bool
  8.desc = Broadcast detected tags on the tf tree. Nodes reading tag information from the tf tree can use this package interchangeably with the [[ar_pose]] package.
  8.default = `true`

  9.name = ~seg_sigma
  9.type = double
  9.desc = Detector parameter. See library documentation/research paper for more details.
  9.default = `0.8`
  
  10.name = ~sigma 
  10.type = double
  10.desc = Detector parameter. See library documentation/research paper for more details.
  10.default = `0.0`

  11.name = ~min_mag
  11.type = double
  11.desc = Detector parameter. See library documentation/research paper for more details.
  11.default = `0.004`
  
  12.name = ~max_edge_cost
  12.type = double
  12.desc = Detector parameter. See library documentation/research paper for more details.
  12.default = `0.5236`

  13.name = ~mag_thresh
  13.type = double
  13.desc = Detector parameter. See library documentation/research paper for more details.
  13.default = `1200.0`

  14.name = ~theta_thresh
  14.type = double
  14.desc = Detector parameter. See library documentation/research paper for more details.
  14.default = `100.0`

  15.name = ~error_bits
  15.type = int
  15.desc = Detector parameter. See library documentation/research paper for more details.
  15.default = `1`

  16.name = ~weight_scale
  16.type = int
  16.desc = Detector parameter. See library documentation/research paper for more details.
  16.default = `100`
  
  17.name = ~seg_decimate
  17.type = bool
  17.desc = Detector parameter. See library documentation/research paper for more details.
  17.default = `false`
 
  18.name = ~debug
  18.type = bool
  18.desc = Detector parameter. See library documentation/research paper for more details.
  18.default = `false`
  
 }
```

## Usage

### Running the node directly (with default parameters)

```
rosrun april_tags_node execute
```

### Using roslaunch

```
roslaunch april_tags_node april_tags_node.launch
```

### Running rviz

```
rosrun rviz rviz -d `rospack find april_tags_node`/config/rviz.vcg
``` ```
roslaunch april_tags_node rviz.launch
```

## Report a Bug

This package just serves as a wrapper for the APRIL toolkit. If you
detect a bug in the wrapper, please report it on the repository
page(<http://code.google.com/p/utexas-ros-pkg/issues/list>). If you find
a bug in the APRIL toolkit, please contact the original developers.
