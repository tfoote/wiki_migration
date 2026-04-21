## Nodes



```clearsilver
name=fiducial_slam
desc=`fiducial_slam` receives fiducial_poses from [[aruco_detect]] and combines them to build a map of fiducial locations and an estimate of the robot's pose.  
sub{
  0.name= /fiducial_transforms
  0.type= fiducial_msgs/FiducialTransform
  0.desc= Poses of observed fiducials.
  1.name= /tf
  1.type= tf/tfMessage
  1.desc= Transforms.
}
pub {
  0.name= /fiducial_pose
  0.type= geometry_msgs/PoseWithCovarianceStamped
  0.desc= Robot's estimated pose in the map, with covariance.
  1.name= fiducials
  1.type= visualization_msgs/Marker
  1.desc= Markers showing the map, for use with [[rviz]] for diagnostics.
  2.name= /fiducial_map
  2.type= fiducial_msgs/FiducialMapEntryArray
  2.desc= The current state of the map.
  3.name= /tf
  3.type= tf/tfMessage
  3.desc= Transforms.
}
srv{ 
  0.name= ~clear_map
  0.type= std_srvs/Empty
  0.desc= Clears the map and enables auto-initialization. 
}
param{
  0.name= ~map_file
  0.type= string
  0.desc= Path to the file containing the generated map.
  0.default= map.txt
  1.name= ~odom_frame
  1.type= string
  1.desc= If this is set to a non-empty string, then the result of the localization is published as a correction to odometry.  For example, the odometry publishes the `tf` from map to odom, and this node publishes the `tf` from `odom` to `base_link`, with the `tf` from `map` to `odom` removed.
  1.default= not set
  2.name= ~map_frame
  2.type= string
  2.desc= The name of the map (world) frame.
  2.default= map
  3.name= ~base_frame
  3.type= string
  3.desc= The child frame of the `tf` we publish.
  3.default= base_link
  4.name= ~future_date_transforms
  4.type= double
  4.desc= Time with which to post-date the transform that is published, to indicate that this transform is valid into the future.
  4.default= 0.1
  5.name= ~publish_6dof_pose
  5.type= bool
  5.default= false
  5.desc= If true, unmodified poses are published, otherwise they are constrained to have zero `z` translation and only the yaw component of rotation.
  6.name= ~read_only_map
  6.type= bool
  6.default= false
  6.desc= if true, the map is not modified, and only localization is performed.
  7.name= ~tf_publish_interval
  7.type= float
  7.default= 1.0
  7.desc= Specifies an interval at which poses are published, even if no fiducials are observed.  This is useful in cases where the fiducial pose is used as a correction to odometry.
}
```



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
