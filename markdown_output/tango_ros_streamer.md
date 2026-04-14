## App summary

\<\<Youtube(VTHlHgoBgvo&rel=0)\>\>

Tango ROS Streamer is an android application and ROS node for
Tango-enabled devices. Its main purpose is to provide Tango sensor data
to the ROS ecosystem in order to easily use the Tango functionalities on
robots.

## Installation

-   From the
    [Play Store\|target=\"\_blank\"](http://play.google.com/store/apps/details?id=eu.intermodalics.tango_ros_streamer&hl=en)
-   From
    [source\|target=\"\_blank\"](https://github.com/Intermodalics/tango_ros/blob/master/README.md#installation-from-source)

The app has been developed and tested with ROS indigo on Ubuntu 14.04,
and kinetic on Ubuntu 16.04.

## Tutorials

\<\<TutorialChain(tango_ros_streamer/Visualisation)\>\> \'\'\'Create a
new tutorial:\'\'\'

## Known Usages

-   [Tangobot\|target=\"\_blank\"](http://wiki.ros.org/Robots/Tangobot)
-   [RTAB-Map](http://wiki.ros.org/rtabmap_ros/Tutorials/Tango%20ROS%20Streamer)

## ROS API

```clearsilver
name = tango
desc = This node is the core of the application, it is responsible for streaming Tango data to ROS.
pub {
  0.name = android/imu
  0.type = sensor_msgs/Imu
  0.desc = IMU message from the Android sensors.

  1.name = tango/camera/color_1/camera_info
  1.type = sensor_msgs/CameraInfo
  1.desc = Camera info of the Tango device color camera.

  2.name = tango/camera/color_1/image_raw
  2.type = sensor_msgs/Image
  2.desc = Image of the Tango device color camera.

  3.name = tango/camera/color_1/image_rect
  3.type = sensor_msgs/Image
  3.desc = Rectified image of the Tango device color camera.

  4.name = tango/camera/fisheye_1/camera_info
  4.type = sensor_msgs/CameraInfo
  4.desc = Camera info of the Tango device fisheye camera. The fisheye camera data is not available on devices with API level > 23. This topic is therefore not advertised for these devices.

  5.name = tango/camera/fisheye_1/image_raw
  5.type = sensor_msgs/Image
  5.desc= Image of the Tango device fisheye camera. The fisheye camera data is not available on devices with API level > 23. This topic is therefore not advertised for these devices.

  6.name = tango/camera/fisheye_1/image_rect
  6.type = sensor_msgs/Image
  6.desc = Rectified image of the Tango device fisheye camera. The fisheye camera data is not available on devices with API level > 23. This topic is therefore not advertised for these devices.

  7.name = tango/laser_scan
  7.type = sensor_msgs/LaserScan
  7.desc = Laser scan message created from the Tango point cloud, expressed in laser frame.

  8.name = tango/point_cloud
  8.type = sensor_msgs/PointCloud2
  8.desc = Point cloud of the Tango device depth sensor, expressed in camera_depth frame.

  9.name = tango/reconstruction/mesh_marker
  9.type = visualization_msgs/MarkerArray
  9.desc = Marker array containing meshes built by the [[https://developers.google.com/tango/apis/c/reconstruction/reference/|Tango 3D reconstruction API|target="_blank"]].

  10.name = tango/reconstruction/occupancy_grid
  10.type = nav_msgs/OccupancyGrid
  10.desc = Occupancy grid built from the Floorplan of the [[https://developers.google.com/tango/apis/c/reconstruction/reference/|Tango 3D reconstruction API|target="_blank"]].

  11.name = tango/static_occupancy_grid
  11.type = nav_msgs/OccupancyGrid
  11.desc = Static occupancy grid after loading it with the `tango/load_occupancy_grid` service.

  12.name = tango/status
  12.type = std_msgs/Int8
  12.desc = Current status of the Tango service. 0: UNKNOWN, 1: SERVICE_NOT_CONNECTED, 2: NO_FIRST_VALID_POSE, 3: SERVICE_CONNECTED.

  13.name = tango/transform/area_description_T_start_of_service
  13.type = geometry_msgs/TransformStamped
  13.desc = Current transform between area_description and start_of_service frames.

  14.name = tango/transform/start_of_service_T_device
  14.type = geometry_msgs/TransformStamped
  14.desc = Current transform between start_of_service and device frames.
}
srv {
  0.name = tango/connect
  0.type = tango_ros_messages/TangoConnect
  0.desc = Doc [[http://docs.ros.org/indigo/api/tango_ros_messages/html/srv/TangoConnect.html|here|target="_blank"]]. Service to disconnect/connect to the Tango service. 0: DISCONNECT, 1: CONNECT, 2: RECONNECT (disconnect and connect cycle).

  1.name = tango/get_map_name
  1.type = tango_ros_messages/GetMapName
  1.desc = Doc [[http://docs.ros.org/indigo/api/tango_ros_messages/html/srv/GetMapName.html|here|target="_blank"]]. Get the name of a map given its uuid.

  2.name = tango/get_map_uuids
  2.type = tango_ros_messages/GetMapUuids
  2.desc = Doc [[http://docs.ros.org/indigo/api/tango_ros_messages/html/srv/GetMapUuids.html|here|target="_blank"]]. Get uuid and name lists of all maps available.

  3.name = tango/load_occupancy_grid
  3.type = tango_ros_messages/LoadOccupancyGrid
  3.desc = Doc [[http://docs.ros.org/indigo/api/tango_ros_messages/html/srv/LoadOccupancyGrid.html|here|target="_blank"]]. Load an occupancy grid from disk (path set via the `tango/occupancy_grid_directory` parameter) and publish it on the `/tango/static_occupancy_grid` topic. If the yaml file of the occupancy grid contains a ''uuid'' field and it is not empty, then the origin of the occupancy grid is expressed wrt the [[https://developers.google.com/tango/apis/c/reference/group/enums#group___enums_1gga4bf43117ed28a7eaa29a77e83683555ea65df443a022c995eea49ac96e820f0f6|AREA_DESCRIPTION|target="_blank"]] frame. Otherwise, its origin is expressed wrt the [[https://developers.google.com/tango/apis/c/reference/group/enums#group___enums_1gga4bf43117ed28a7eaa29a77e83683555eaf83a90390331fc02183ab5489a0f5841|START_OF_SERVICE|target="_blank"]] frame. Also, in the case where a localization map is loaded (`/tango/localization_map_uuid` parameter set before connecting to Tango) and its uuid corresponds to the ''uuid'' field of the occupancy grid yaml file, then the occupancy grid is aligned with the localization map.

  4.name = tango/save_map
  4.type = tango_ros_messages/SaveMap
  4.desc = Doc [[http://docs.ros.org/indigo/api/tango_ros_messages/html/srv/SaveMap.html|here|target="_blank"]]. Save the current localization map and/or the occupancy grid with the given name. 1: SAVE_LOCALIZATION_MAP, 2: SAVE_OCCUPANCY_GRID. The localization map saved is internal to Tango and can not be accessed directly. To be able to save it the `/tango/create_new_map` parameter needs to be true. The occupancy grid is saved to disk (path set via the `tango/occupancy_grid_directory` parameter) as a pair of files: a pgm file encoding the occupancy data and a yaml file describing the metadata. This is compatible with the existing ROS node [[map_server]]. If the occupancy grid is saved together with the localization map or while a localization map is already loaded (`/tango/localization_map_uuid` parameter was set before connecting to Tango), the origin of the occupancy grid is saved wrt the [[https://developers.google.com/tango/apis/c/reference/group/enums#group___enums_1gga4bf43117ed28a7eaa29a77e83683555ea65df443a022c995eea49ac96e820f0f6|AREA_DESCRIPTION|target="_blank"]] frame and the uuid of the localization map is saved in the occupancy grid yaml file. This way, the occupancy grid will be aligned with the localization map if loaded later. Otherwise, it is saved wrt the [[https://developers.google.com/tango/apis/c/reference/group/enums#group___enums_1gga4bf43117ed28a7eaa29a77e83683555eaf83a90390331fc02183ab5489a0f5841|START_OF_SERVICE|target="_blank"]] frame and the uuid field is left empty in the yaml file. In this case the occupancy grid will not be aligned with the localization map when loaded later.

  5.name = tango/set_parameters
  5.type = dynamic_reconfigure/Reconfigure
  5.desc = Dynamic reconfigure service to change runtime parameters.
}
param {
  0.name = tango/area_description_frame_id
  0.type = string
  0.desc = Frame id used for the Tango frame [[https://developers.google.com/tango/apis/c/reference/group/enums#group___enums_1gga4bf43117ed28a7eaa29a77e83683555ea65df443a022c995eea49ac96e820f0f6|AREA_DESCRIPTION|target="_blank"]].
  0.default = area_description

  1.name = tango/create_new_map
  1.type = bool
  1.desc = True to create a new map. If true, `tango/localization_mode` is not used.
  1.default = false

  2.name = tango/enable_3dr_mesh
  2.type = bool
  2.desc = True to enable extraction of mesh using the Tango 3D reconstruction API. To allow Tango 3D reconstruction, `enable_color_camera` and `enable_depth` also need to be true.
  2.default = true

  3.name = tango/enable_3dr_occupancy_grid
  3.type = bool
  3.desc = True to enable extraction of occupancy grid using the Tango 3D reconstruction API. To allow Tango 3D reconstruction, `enable_color_camera` and `enable_depth` also need to be true.
  3.default = true

  4.name = tango/enable_color_camera
  4.type = bool
  4.desc = True to enable color camera. If false, Tango will not connect to the color camera of the device, which can save battery, but topics that need color image will not be advertised (color camera, mesh, occupancy_grid). Also, note that this parameter has effect only for devices with Android API level > 23. For devices with lower API levels, the color camera is always enable.
  4.default = true

  5.name = tango/enable_depth
  5.type = bool
  5.desc = True to enable depth camera. If false, Tango will not connect to the depth camera of the device, which can save battery, but topics that need depth data will not be advertised (pointcloud, laser, mesh, occupancy_grid).
  5.default = true

  6.name = tango/laser_scan_max_height
  6.type = double
  6.desc = Maximum height of the tango laser scan in meter
  6.default = 1

  7.name = tango/laser_scan_min_height
  7.type = double
  7.desc = Minimum height of the tango laser scan in meter
  7.default = -1

  8.name = tango/localization_map_uuid
  8.type = string
  8.desc = Uuid of the map to use for localization. Used only if `tango/localization_mode` is set to 3.
  8.default = ""

  9.name = tango/localization_mode
  9.type = int
  9.desc = Localization method to use. 1: ODOMETRY (only VIO, no map required), 2: ONLINE_SLAM (VIO + drift correction, no map required), 3: LOCALIZATION (localization in map). To know more about the localization modes, read [[tango_ros_streamer/Use Tango localization|Use Tango localization]].
  9.default = 2

  10.name = tango/occupancy_grid_directory
  10.type = string
  10.desc = Path to the directory where occupancy grids are saved/loaded.
  10.default = /sdcard/tango_ros_streamer/occupancy_grids/

  11.name = tango/publish_pose_on_tf
  11.type = bool
  11.desc = True to publish transforms on /tf
  11.default = true

  12.name = tango/reconstruction/floorplan_max_error
  12.type = double
  12.desc = Used by the Tango 3D reconstruction API. According to its [[https://developers.google.com/tango/apis/c/reconstruction/reference/group/config-params|documentation|target="_blank"]]: "Upper bound on geometric error in meters during polygon simplification. Set to zero to disable simplification.".
  12.default = 0.0

  13.name = tango/reconstruction/max_voxel_weight
  13.type = int
  13.desc = Used by the Tango 3D reconstruction API. According to its [[https://developers.google.com/tango/apis/c/reconstruction/reference/group/config-params|documentation|target="_blank"]]: "The maximum voxel weight for the integration filter. Defaults to 16383. Roughly corresponds to the number of observations. A higher value gives better geometric quality and stability; a lower value gives more responsiveness to dynamic objects.".
  13.default = 16383

  14.name = tango/reconstruction/min_num_vertices
  14.type = int
  14.desc = Used by the Tango 3D reconstruction API. According to its [[https://developers.google.com/tango/apis/c/reconstruction/reference/group/config-params|documentation|target="_blank"]]: "Minimum number of vertices that every connected component in the mesh should consist of. Defaults to 1. Smaller components (typically noise) will be deleted.".
  14.default = 1

  15.name = tango/reconstruction/occupancy_grid_threshold
  15.type = int
  15.desc = Threshold to decide if a pixel value should correspond to a free or occupied cell when converting the image of Tango 3D reconstruction to an occupancy grid. Should be between 0 and 255: pixel value <= threshold --> cell is free, pixel value > threshold --> cell is occupied.
  15.default = 180

  16.name = tango/reconstruction/resolution_3d
  16.type = double
  16.desc = Resolution used by the [[https://developers.google.com/tango/apis/c/reconstruction/reference/|Tango 3D reconstruction API|target="_blank"]], in meter. It also corresponds to the resolution of the occupancy grid.
  16.default = 0.05

  17.name = tango/reconstruction/update_method
  17.type = int
  17.desc = Used by the Tango 3D reconstruction API. According to its [[https://developers.google.com/tango/apis/c/reconstruction/reference/group/config-params|documentation|target="_blank"]]: "Update method to be used when caling Tango3DR_update. See [[https://developers.google.com/tango/apis/c/reconstruction/reference/group/enums#group___enums_1ga68b9b760afda90cd0c8b0cfdb1ad3fcc|Tango3DR_UpdateMethod|target="_blank"]].".
  17.default = 0

  18.name = tango/reconstruction/use_space_clearing
  18.type = bool
  18.desc = Used by the Tango 3D reconstruction API. According to its [[https://developers.google.com/tango/apis/c/reconstruction/reference/group/config-params|documentation|target="_blank"]]: "When true, will clear away free space along the depth observations. Default is false. If enabled, 3D reconstruction will create higher quality meshes at a cost to performance.".
  18.default = false

  19.name = tango/start_of_service_frame_id
  19.type = string
  19.desc = Frame id used for the Tango frame [[https://developers.google.com/tango/apis/c/reference/group/enums#group___enums_1gga4bf43117ed28a7eaa29a77e83683555eaf83a90390331fc02183ab5489a0f5841|START_OF_SERVICE|target="_blank"]].
  19.default = start_of_service

  20.name = tango/use_tf_static
  20.type = bool
  20.desc = True to use /tf_static latched static transform broadcaster. If set to false static transforms are published on the /tf topic.
  20.default = true

  21.name = tango/android_api_level
  21.type = int
  21.desc = API level of the Tango device running the node. It should be set only if the node is running on an Android device. In this case it should be set by the Android application running the node, before connecting to the Tango service.
  21.default = 0
}
prov_tf {
  0.from = area_description
  0.to = start_of_service
  0.desc = Transform between area_description and start_of_service frames. This transform is available only if tango/localization_mode is set to 2 or 3. Tango is updating this transform quite slowly (~10 Hz), which can cause some applications that need high rate for odometry (e.g. navigation) to not work properly. As a workaround, this transform is published as a static transform even though it changes over time.

  1.from = start_of_service
  1.to   = device
  1.desc = Transform between start of service frame (first device pose after starting the Tango service) and current device frame.

  2.from = device
  2.to = camera_depth
  2.desc = Depth camera pose expressed in the device frame (static transform)

  3.from = camera_depth
  3.to = laser
  3.desc = Laser pose expressed in the depth camera frame (static transform)

  4.from = device
  4.to = camera_fisheye
  4.desc = Fisheye camera pose expressed in the device frame (static transform)

  5.from = device
  5.to = camera_color
  5.desc = Color camera pose expressed in the device frame (static transform)

  6.from = device
  6.to = imu
  6.desc = IMU pose expressed in the device frame (static transform)
}
```

Note that all image topics are published via
[image_transport](image_transport). Therefore, for each image topic, a
compressed version of the image is available together with its
compression parameters.

Also note that the service \`tango/connect\` seems to not work properly
on Tango Tablet Development Kit.

## Report a bug

\<\<GitHubIssues(Intermodalics/tango_ros)\>\>
