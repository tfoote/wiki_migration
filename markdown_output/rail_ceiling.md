## About

Rail_ceiling is an overhead camera system for tracking the positions of
obstacles in a closed space and publishing maps containing those
obstacles for use in robot navigation. Rail_ceiling supports multiple
cameras and can publish multiple maps with different obstacle
footprints. Obstacle tracking is accomplished using ar tags and the
[ar_track_alvar](http://wiki.ros.org/action/quicklink/ar_track_alvar)
ros package.

## Nodes

```clearsilver
node.0 {
  name = calibration
  desc = Calibrates transforms between a global coordinate frame and the array of ceiling cameras based on AR markers of known location.
  sub {
    0.name = ceiling_cam_tracker_[i]/ar_pose_marker
    0.type = ar_track_alvar_msgs/AlvarMarkers
    0.desc = Topics for incoming marker data, one topic per camera, replace [i] with the camera index.
  }
  param {
    0.name = fixed_frame
    0.type = string
    0.desc = Global coordinate frame.
    0.default = map
  }
  param {
    1.name = camera_frame_id_prefix
    1.type = string
    1.desc = Prefix to camera coordinate frames.
    1.default = ceiling_cam_
  }
  param {
    2.name = num_cameras
    2.type = int
    2.desc = Number of cameras in the ceiling array.
    2.default = 1
  }
  param {
    3.name = num_samples
    3.type = int
    3.desc = Number of samples to be taken for calibration.
    3.default = 10
  }
  param {
    4.name = ceiling_cam_[i]_pos_x
    4.type = double
    4.desc = x position (in the global coordinate frame) of the marker used to calibrate camera [i].
    4.default = 0.0
  }
  param {
    5.name = ceiling_cam_[i]_pos_y
    5.type = double
    5.desc = y position (in the global coordinate frame) of the marker used to calibrate camera [i].
    5.default = 0.0
  }
  param {
    6.name = ceiling_cam_[i]_pos_z
    6.type = double
    6.desc = z position (in the global coordinate frame) of the marker used to calibrate camera [i].
    6.default = 0.0
  }
  param {
    7.name = ceiling_cam_[i]_rot_x
    7.type = double
    7.desc = Quaternion x component (in the global coordinate frame) of the marker used to calibrate camera [i].
    7.default = 0.0
  }
  param {
    8.name = ceiling_cam_[i]_rot_y
    8.type = double
    8.desc = Quaternion y component (in the global coordinate frame) of the marker used to calibrate camera [i].
    8.default = 0.0
  }
  param {
    9.name = ceiling_cam_[i]_rot_z
    9.type = double
    9.desc = Quaternion z component (in the global coordinate frame) of the marker used to calibrate camera [i].
    9.default = 0.0
  }
  param {
    10.name = ceiling_cam_[i]_rot_w
    10.type = double
    10.desc = Quaternion w component (in the global coordinate frame) of the marker used to calibrate camera [i].
    10.default = 1.0
  }
}
node.1 {
  name = calibration_from_carl
  desc = Calibrates transforms between a global coordinate frame and the array of ceiling cameras based on an AR marker located on a localized robot.
 sub {
    0.name = ceiling_cam_tracker_[i]/ar_pose_marker
    0.type = ar_track_alvar_msgs/AlvarMarkers
    0.desc = Topics for incoming marker data, one topic per camera, replace [i] with the camera index.
  }
  sub {
    1.name = start_calibration
    1.type = std_msgs/Int16
    1.desc = Enable calibration for the camera of a given index.
  }
  param {
    0.name = num_cameras
    0.type = int
    0.desc = The number of cameras in the ceiling array.
    0.default = 5
  }
  param {
    1.name = calibration_marker_id
    1.type = int
    1.desc = The ID of the marker on the robot.
    1.default = 200
  }
}
node.2 {
  name = furniture_tracker
  desc = Using the furniture configuration files, track positions of furniture obstacles from AR marker data and publish significant changes of furniture footprint positions to costmap layers.
 sub {
    0.name = ceiling_cam_tracker_[i]/ar_pose_marker
    0.type = ar_track_alvar_msgs/AlvarMarkers
    0.desc = Topics for incoming marker data, one topic per camera, replace [i] with the camera index.
  }
  sub {
    1.name = start_calibration
    1.type = std_msgs/Int16
    1.desc = Enable calibration for the camera of a given index.
  }
  pub {
    0.name = furniture_layer/update_obstacles
    0.type = rail_ceiling/Obstacles
    0.desc = Updated obstacle information to be published to costmap layers.
  }
  srv {
    0.name = furniture_tracker/get_all_poses
    0.type = rail_ceiling/getAllObstacles
    0.desc = Service server which returns the most recently published footprint polygons for all initialized pieces of tracked furniture.
  }
  param {
    0.name = num_marker_topics
    0.type = int
    0.desc = The number of indepent marker tracking topics (this should be equal to the number of cameras in the ceiling array).
    0.default = 5
  }
  param {
    1.name = read_initial_poses
    1.type = bool
    1.desc = True if initial positions should be read in, false if furniture should not be added to the map until it is first detected.
    1.default = false
  }
  param {
    2.name = markers_config
    2.type = string
    2.desc = Config file for marker layout on pieces of furniture.
    2.default = (path to rail_ceiling)/config/markers.yaml
  }
  param {
    3.name = furniture_footprints_config
    3.type = string
    3.desc = Config file for furniture localization and navigation footprints.
    3.default = (path to rail_ceiling)/config/furniture_footprints.yaml
  }
}
```

## Installation

To install the rail_ceiling package, you can install from source with
the following commands:

```
cd /(your catkin workspace)/src
git clone https://github.com/WPI-RAIL/rail_ceiling.git
cd ..
catkin_make
```

## Camera Transform Calibration

The transforms between the global coordinate frame and the camera frames
need to be accurately calibrated for furniture tracking to work
properly. This can be done one of three ways: calibration from markers
of known fixed position, calibration from a marker on a localized robot,
or direct measurement.

### Calibration from Floor Markers

The `calibration` node will run an automatic calibration procedure
where each camera will take sample poses of an associated marker of
known position in the environment. Once a sufficient number of samples
have been taken for each camera, the transforms will be calculated and
written to the `ceiling.urdf.xacro` file in your home directory, and
must then be copied into the `urdf` directory of the `rail_ceiling`
package if you wish to use it.

This process is fully automated and is recommended if you have a marker
in a fixed, accurately measured location in the environment. Each marker
must have an ID equal to the camera index plus 100 (camera 0 will be
associated with marker 100, camera 1 will be associated with marker 101,
etc.).

This process can be launched with the following launch file, which will
also start the cameras and ar tracking nodes: . ```
roslaunch rail_ceiling calibration.launch
```

The process can be visualized with: . ```
roslaunch rail_ceiling view_calibration.launch
```

### Calibration from Mobile Robot

The `calibration_from_carl` node provides a method of calibrating the
camera transforms from a marker placed on a localized mobile robot, such
as the CARL platform. This calibration method is executed as follows: .
```
roslaunch rail_ceiling cameras.launch
roslaunch rail_ceiling ar_trackers.launch marker_size:=12.0
roslaunch rail_ceiling calibration_from_carl.launch
```

Next, the robot must be driven into the field of view of a camera to be
calibrated. Once the robot is in the camera's field of view and it is
confirmed to be accurately localized, publishing to the
`start_calibration` topic with the id number of the camera to be
calibrated replacing \[camera_id\]: . ```
rostopic pub /start_calibration std_msgs::Int16 "data: [camera_id]"
``` This will
initiate sample collecting for the selected camera, and completion of
sample collection will be denoted in the terminal. The process must then
be repeated for all cameras. Note that if the robot is within the field
of view of multiple cameras, they can be calibrated simultaneously.

Once sufficient samples are collected for all of the cameras, the
transforms will be calculated and written to the `ceiling.urdf.xacro`
file in your home directory, and must then be copied into the `urdf`
directory of the `rail_ceiling` package if you wish to use it.

### Calibration from Direct Measurement

The transforms can also be edited directly in the human-readable urdf
file, `urdf/ceiling.urdf.xacro`. This should only be done if the
camera positions and orientations can be accurately measured.

## Furniture Configuration

Furniture footprints and marker information can be configured in the
`furniture_footprints.yaml` and `markers.yaml` file in the
`config` directory. The `furniture_footprints.yaml` configuration
file defines general pieces of furniture with convex polygon footprints
for localization and navigation, and the `markers.yaml` configuration
file defines instances of furniture with attached markers and their
associated poses.

### Defining Furniture Footprints

To add a new type of furniture, simply add a new entry to the
`furniture_footprints.yaml` file. Each entry must have a name (for
identifying the type of furniture) a localization footprint (a set of
convex polygons that a laser scanner will detect), and a navigation
footprint (a set of convex polygons that represent the full area
occupied by the piece of furniture that should be avoided during
navigation). The entry format is as follows: . ```
- name: furniture_name
  localization_footprint:
    - polygon: [[x1, y1], [x2, y2], [x3, y3], ..., [xn, yn]]
    - polygon: [[x1, y1], [x2, y2], [x3, y3], ..., [xn, yn]]
    - ...
  navigation_footprint:
    - polygon: [[x1, y1], [x2, y2], [x3, y3], ..., [xn, yn]]
    - polygon: [[x1, y1], [x2, y2], [x3, y3], ..., [xn, yn]]
    - ...
```
Points composing the polygons are defined with respect to the center of
the piece of furniture, according to a coordinate system with x
increasing right, y increasing forward, and z increasing up. In
practice, the reference frame's position does not have to be at the
center of the furniture piece, as long as it is consistent with the
reference frame defined for instances of the furniture type in the
`markers.yaml` file.

Note that polygons must consist of a minimum of 3 points, and an object
can be defined with zero or more localization footprint polygons and
zero or more navigation footprint polygons.

### Defining Furniture Instances

Each piece of furniture in th eenvironment must have its own entry in
the `markers.yaml` file. Each entry consists of a required type
(corresponding with the furniture names defined in
`furniture_footprints.yaml`), an optional initial_pose (an initial
pose for the piece of furniture in the global coordinate frame), and a
required set of markers. Markers are defined with the unique id used to
generate them, and the pose of the marker with respect to the furniture
reference frame. The entry format is as follows: .
```
- type: furniture_name
  initial_pose: [x0, y0, theta0]
  markers:
    - id: 1
      x: x1
      y: y1
      theta: theta1
    - id: 2
      x: x2
      y: y2
      theta: theta2
    - ...
``` Note that each furniture instance requires one
or more markers, and no two furniture instances can use the same marker
id.

## Startup

Once calibrated, a pose publisher for the camera positions can be run
with: . ```
roslaunch rail_ceiling ceiling_description.launch
```

The main functionality of the `rail_ceiling` package is furniture
tracking. This can be launched with: . ```
roslaunch rail_ceiling furniture_tracker.launch
```

Alternatively, the cameras, the cameras and AR trackers can be launched
individually with: . ```
cd /(your catkin workspace)/src
git clone https://github.com/WPI-RAIL/rail_ceiling.git
cd ..
catkin_make
```0

## Support

Please send bug reports to the
[github issue tracker](https://github.com/WPI-RAIL/rail_ceiling/issues).
