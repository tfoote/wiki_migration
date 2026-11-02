## Nodes

### fiducial_slam

`fiducial_slam` receives fiducial_poses from
[aruco_detect](https://index.ros.org/p/aruco_detect) and combines them
to build a map of fiducial locations and an estimate of the robot's
pose.

#### Subscribed Topics

- `/fiducial_transforms`
  ([fiducial_msgs/msg/FiducialTransform](https://docs.ros.org/en/rolling/p/fiducial_msgs/msg/FiducialTransform.html)):
  Poses of observed fiducials.
- `/tf`
  ([tf/msg/tfMessage](https://docs.ros.org/en/rolling/p/tf/msg/tfMessage.html)):
  Transforms.

#### Published Topics

- `/fiducial_pose`
  ([geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)):
  Robot's estimated pose in the map, with covariance.
- `fiducials`
  ([visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)):
  Markers showing the map, for use with
  [rviz](https://index.ros.org/p/rviz) for diagnostics.
- `/fiducial_map`
  ([fiducial_msgs/msg/FiducialMapEntryArray](https://docs.ros.org/en/rolling/p/fiducial_msgs/msg/FiducialMapEntryArray.html)):
  The current state of the map.
- `/tf`
  ([tf/msg/tfMessage](https://docs.ros.org/en/rolling/p/tf/msg/tfMessage.html)):
  Transforms.

#### Services

- `~clear_map`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Clears the map and enables auto-initialization.

#### Parameters

- `~map_file` (`string`, default: `map.txt`): Path to the file
  containing the generated map.
- `~odom_frame` (`string`, default: `not set`): If this is set to a
  non-empty string, then the result of the localization is published as
  a correction to odometry. For example, the odometry publishes the
  `tf` from map to odom, and this node publishes the `tf` from
  `odom` to `base_link`, with the `tf` from `map` to `odom`
  removed.
- `~map_frame` (`string`, default: `map`): The name of the map (world)
  frame.
- `~base_frame` (`string`, default: `base_link`): The child frame of the
  `tf` we publish.
- `~future_date_transforms` (`double`, default: `0.1`): Time with which
  to post-date the transform that is published, to indicate that this
  transform is valid into the future.
- `~publish_6dof_pose` (`bool`, default: `false`): If true, unmodified
  poses are published, otherwise they are constrained to have zero `z`
  translation and only the yaw component of rotation.
- `~read_only_map` (`bool`, default: `false`): if true, the map is not
  modified, and only localization is performed.
- `~tf_publish_interval` (`float`, default: `1.0`): Specifies an
  interval at which poses are published, even if no fiducials are
  observed. This is useful in cases where the fiducial pose is used as a
  correction to odometry.

#### File Formats

The map file is a text file with a line for each fiducial id: `

`id x y z pan tilt roll variance numObservations links`

`x`, `y` and `z` specify the translation of the fiducial from the
origin in meters, and `pan`, `tilt`, and `roll` specify its
orientation in degrees. The fields `variance` and `numObservations`
represent how good the pose estimate is considered to be, and how many
observations were used to generate it. `links` is a list of the ids of
fiducials that have been observed at the same time as the current
fiducial. The coordinate frame used is the `map` frame, which is
relative to the floor, so markers of the ceiling will have been rotated.
The supplied launch files specify the map file as
`/.ros/slam/map.txt`.
