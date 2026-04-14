## Overview

This package provides additional nodes and plugins not included to
[mavros](mavros).

## Nodes

```clearsilver
node.0 {
 name = gcs_image_bridge
 desc = Additional proxy with image streaming for GCS. It mux FCU streams from mavros and images from any source. '''REMOVED IN 0.18'''
 pub {
  0.name= mavlink/to
  0.type= mavros/Mavlink
  0.desc= Mavlink stream to autopilot.
 }
 sub {
  0.name= mavlink/from
  0.type= mavros/Mavlink
  0.desc= Mavlink stream from autopilot.
  1.name= mavlink/gcs_image
  1.type= sensor_msgs/Image
  1.desc= Image stream to send.
 }
 param {
  0.name= ~gcs_url
  0.type= string
  0.desc= Connection URL.
  0.default= udp://@
  1.name= ~jpeg_quality
  1.type= int
  1.desc= JPEG quality level for image encoding.
  1.default= 60
 }
}

node.1 {
 name= copter_visualization
 desc= Converts information published on mavros topics into [[http://wiki.ros.org/rviz/DisplayTypes/Marker|markers]] for visualization in RVIZ. {{attachment:copter_visualization.png||width="720px"}}

 sub {
  0.name= local_position
  0.type= geometry_msgs/PoseStamped
  0.desc= Position source (e.g. mavros/local_position/local topic)
  1.name= local_setpoint
  1.type= geometry_msgs/PoseStamped
  1.desc= Local setpoints (e.g. mavros/setpoint_position/local topic)
 }
 pub {
  0.name= track_markers
  0.type= visualization_msgs/Marker
  0.desc= Markers to visualize vehicle path.
  1.name= vehicle_marker
  1.type= visualization_msgs/MarkerArray
  1.desc= Marker to visualize copter model.
  2.name= wp_markers
  2.type= visualization_msgs/Marker
  2.desc= Markers to visualize local setpoints.
 }
 param {
  0.name= ~fixed_frame_id
  0.type= string
  0.desc= Pose frame id.
  0.default= 'local_origin'
  1.name= ~child_frame_id
  1.type= string
  1.desc= Pose child frame id.
  1.default= 'fcu'
  2.name= ~marker_scale
  2.type= double
  2.desc= Marker scale factor.
  2.default= 1.0
  3.name= ~num_rotors
  3.type= int
  3.desc= Number of rotors in copter model.
  3.default= 4
  4.name= ~arm_len
  4.type= double
  4.desc= Copter model arm length (m).
  4.default= 0.22
  5.name= ~body_width
  5.type= double
  5.desc= Copter model body width (m).
  5.default= 0.15
  6.name= ~body_height
  6.type= double
  6.desc= Copter model body height (m).
  6.default= 0.10
  7.name= ~max_track_size
  7.type= int
  7.desc= Max number of markers in track.
  7.default= 1000
 }
}
```

## Utility commands

All utilities provides \<util\> \--help and \<util\> \<command\> \--help
information.

### mavteleop

```
usage: mavteleop [-h] [-n MAVROS_NS] [-v] (-rc | -att | -vel | -pos)

Teleoperation script for Copter-UAV

optional arguments:
  -h, --help            show this help message and exit
  -n MAVROS_NS, --mavros-ns MAVROS_NS
                        ROS node namespace
  -v, --verbose         verbose output
  -rc, --rc-override    use rc override control type
  -att, --sp-attitude   use attitude setpoint control type
  -vel, --sp-velocity   use velocity setpoint control type
  -pos, --sp-position   use position setpoint control type
```

### mavftpfuse

\'\'\'PX4\'\'\' only. Require
[fusepy](https://github.com/terencehonles/fusepy) package, use \`sudo
pip install fusepy\`.

```
usage: mavftpfuse [-h] [-n MAVROS_NS] [-v] [-d] path

FUSE for MAVLink-FTP mavros plugin

positional arguments:
  path                  mount point

optional arguments:
  -h, --help            show this help message and exit
  -n MAVROS_NS, --mavros-ns MAVROS_NS
                        ROS node namespace
  -v, --verbose         verbose output
  -d, --debug           libfuse debug
```

## Plugins

Extra set of communication plugins loaded by
[mavros_node](mavros#mavros_node).

```clearsilver
node.6 {
 name= cam_imu_sync
 desc= Syncronization markers for IMU and Camera. EXPERIMENTAL (TODO)
}

node.7 {
 name= distance_sensor
 desc= Publish range finders data from FCU; Send data to FCU. (TODO page with config spec).
 pub {
  0.name= ~distance_sensor/<sensor_name>
  0.type= sensor_msgs/Range
  0.desc= Data from FCU-connected sensor.
 }
 sub {
  0.name= ~distance_sensor/<sensor_name>
  0.type= sensor_msgs/Range
  0.desc= Send ROS sensor data to FCU.
 }
 param {
  0.name= ~distance_sensor/<sensor_name>/subscriber
  0.type= bool
  0.desc= Subscriber or Publisher
  0.default= false
  1.name= ~distance_sensor/<sensor_name>/id
  1.type= int
  1.desc= Sensor Id. '''required'''
  2.name= ~distance_sensor/<sensor_name>/orientation
  2.type= string
  2.desc= Orientation of the sensor. '''required''' for subscriber.

  # XXX TODO
  
 }
}

node.1 {
 name= image_pub
 desc= Publish images from PX4Flow module. '''REMOVED IN 0.18'''
 pub {
  0.name= ~image/camera_image
  0.type= sensor_msgs/Image
  0.desc= Image stream from mavlink device.
 }
 param {
  0.name= ~image/frame_id
  0.type= string
  0.desc= Frame ID for camera_image topic.
  0.default= px4flow
 }
}

node.4 {
 name= mocap_pose_estimate
 desc= Send ATT_POS_MOCAP message to FCU.
 sub {
  0.name= ~mocap/pose
  0.type= geometry_msgs/PoseStamped
  0.desc= Pose to send.
  1.name= ~mocap/tf
  1.type= geometry_msgs/TransformStamped
  1.desc= Pose to send.
 }
 param {
  0.name= ~mocap/use_tf
  0.type= bool
  0.desc= Vicon mocap system.
  0.default= false
  1.name= ~mocap/use_pose
  1.type= bool
  1.desc= Optitrack mocap system.
  1.default= true 
 }
}

node.0 {
 name= px4flow
 desc= Publish `OPTICAL_FLOW_RAD` message data from FCU or PX4Flow module.
 pub {
  0.name= ~px4flow/raw/optical_flow_rad
  0.type= mavros_msgs/OpticalFlowRad
  0.desc= Optical flow data.
  1.name= ~px4flow/ground_distance
  1.type= sensor_msgs/Range
  1.desc= Sonar range data.
  2.name= ~px4flow/temperature
  2.type= sensor_msgs/Temperature
  2.desc= IMU sensor temperature.
 }
 param {
  0.name= ~px4flow/frame_id
  0.type= string
  0.desc= Frame Id.
  0.default= px4flow
  1.name= ~px4flow/ranger_fov
  1.type= double
  1.desc= Sonar FOV.
  1.default= 0.0
  2.name= ~px4flow/ranger_min_range
  2.type= double
  2.desc= Sonar minimum range.
  2.default= 0.3
  3.name= ~px4flow/ranger_max_range
  3.type= double
  3.desc= Sonar maximum range.
  3.default= 5.0
 }
}

node.8 {
 name= vibration
 desc= Publish VIBRATION message data.
 # XXX TODO
}

node.2 {
 name= vision_pose_estimate
 desc= Sent VISION_POSITION_ESTIMATE to FCU from PoseStamped topic.
 sub {
  0.name= ~vision_pose/pose
  0.type= geometry_msgs/PoseStamped
  0.desc= Vision position.
  1.name= ~vision_pose/pose_cov
  1.type= geometry_msgs/PoseWithCovarianceStamped
  1.desc= Vision position (with covariance).
 }
 param {
  1.name= ~vision_pose/tf/listen
  1.type= bool
  1.desc= TF listen switch. Disable topic if enabled.
  1.default= false
  2.name= ~vision_pose/tf/frame_id
  2.type= string
  2.desc= Origin frame_id for TF.
  2.default= local_origin
  3.name= ~vision_pose/tf/child_frame_id
  3.type= string
  3.desc= Child frame_id for TF.
  3.default= vision
  4.name= ~vision_pose/tf/rate_limit
  4.type= double
  4.desc= Rate limit for TF listener [Hz].
  4.default= 50.0
 }
}

node.3 {
 name= vision_speed_estimate
 desc= Send vision speed estimates to FCU.
 sub {
  0.name= ~vision_speed/speed_vector
  0.type= geometry_msgs/Vector3Stamped
  0.desc= Send speed vector.
  1.name= ~vision_speed/speed_twist
  1.type= geometry_msgs/TwistStamped
  1.desc= Send linear speed. (alternative)
 }
 param {
  0.name= ~vision_speed/listen_twist
  0.type= bool
  0.desc= Topic type selector.
  0.default= false
 }
}
```
