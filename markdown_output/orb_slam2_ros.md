# ORB-SLAM2

\`\`\`ORB-SLAM2 Authors:\`\`\`
[RaulMur-Artal](http://webdiis.unizar.es/~raulmur/),[JuanD.Tardos](http://webdiis.unizar.es/~jdtardos/),
[J.M.M.Montiel](http://webdiis.unizar.es/~josemari/) and
[DorianGalvez-Lopez](http://doriangalvez.com/)
([DBoW2](https://github.com/dorian3d/DBoW2)). The original
implementation can be found
[here](https://github.com/raulmur/ORB_SLAM2.git).

# ORB-SLAM2 ROS node

This is a ROS implementation of the ORB-SLAM2 real-time SLAM library for
\`\`\`Monocular\`\`\`, \`\`\`Stereo\`\`\` and \`\`\`RGB-D\`\`\` cameras
that computes the camera trajectory and a sparse 3D reconstruction (in
the stereo and RGB-D case with true scale). It is able to detect loops
and relocalize the camera in real time. This implementation removes the
Pangolin dependency, and the original viewer. All data I/O is handled
via ROS topics. For vizualization you can use RViz.

## Features

\- Full ROS compatibility

\- Supports a lot of cameras out of the box, such as the Intel RealSense
family. See the run section for a list

\- Data I/O via ROS topics

\- Parameters can be set with the rqt_reconfigure gui during runtime

\- Very quick startup through considerably sped up vocab file loading

\- Full Map save and load functionality

## ROS parameters, topics and services

### Parameters

There are three types of parameters right now: static- and dynamic ros
parameters and camera settings from the config file. The static
parameters are send to the ROS parameter server at startup and are not
supposed to change. They are set in the launch files which are located
at ros/launch. The parameters are:

\- \`\`\`load_map\`\`\`: Bool. If set to true, the node will try to load
the map provided with map_file at startup.

\- \`\`\`map_file\`\`\`: String. The name of the file the map is saved
at.

\- \`\`\`settings_file\`\`\`: String. The location of config file
mentioned above.

\- \`\`\`voc_file\`\`\`:String. The location of config vocanulary file
mentioned above.

\- \`\`\`publish_pose\`\`\`: Bool. If a PoseStamped message should be
published. Even if this is false the tf will still be published.

\- \`\`\`publish_pointcloud\`\`\`: Bool. If the pointcloud containing
all key points (the map) should be published.

\- \`\`\`pointcloud_frame_id\`\`\`: String. The Frame id of the
Pointcloud/map.

\- \`\`\`camera_frame_id\`\`\`: String. The Frame id of the camera
position.

Dynamic parameters can be changed at runtime. Either by updating them
directly via the command line or by using
[rqt_reconfigure](http://wiki.ros.org/rqt_reconfigure) which is the
recommended way. The parameters are:

\- \`\`\`localize_only\`\`\`: Bool. Toggle from/to only localization.
The SLAM will then no longer add no new points to the map.

\- \`\`\`reset_map\`\`\`: Bool. Set to true to erase the map and start
new. After reset the parameter will automatically update back to false.

\- \`\`\`min_num_kf_in_map\`\`\`: Int. Number of key frames a map has to
have to not get reset after tracking is lost.

Finally, the intrinsic camera calibration parameters along with some
hyperparameters can be found in the specific yaml files in
orb_slam2/config.

### Published topics

The following topics are being published and subscribed to by the nodes:

\- All nodes publish (given the settings) a \`\`\`PointCloud2\`\`\`
containing all key points of the map.

\- Live \`\`\`image\`\`\` from the camera containing the currently found
key points and a status text.

\- A \`\`\`tf\`\`\` from the pointcloud frame id to the camera frame id
(the position).

### Subscribed topics

\- The mono node subscribes to \`\`\`/camera/image_raw\`\`\` for the
input image.

\- The RGBD node subscribes to \`\`\`/camera/rgb/image_raw\`\`\` for the
RGB image and

\- \`\`\`/camera/depth_registered/image_raw\`\`\` for the depth
information.

\- The stereo node subscribes to \`\`\`image_left/image_color_rect\`\`\`
and

\- \`\`\`image_right/image_color_rect\`\`\` for corresponding images.

### Services

All nodes offer the possibility to save the map via the service
node_type/save_map. So the save_map services are:

\- \`\`\`/orb_slam2_rgbd/save_map\`\`\`

\- \`\`\`/orb_slam2_mono/save_map\`\`\`

\- \`\`\`/orb_slam2_stereo/save_map\`\`\`
