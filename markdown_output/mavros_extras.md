## Overview

This package provides additional nodes and plugins not included to
[mavros](https://index.ros.org/p/mavros).

## Nodes

### gcs_image_bridge

Additional proxy with image streaming for GCS. It mux FCU streams from
mavros and images from any source. **REMOVED IN 0.18**

#### Subscribed Topics

- `mavlink/from`
  ([mavros/msg/Mavlink](https://docs.ros.org/en/rolling/p/mavros/msg/Mavlink.html)):
  Mavlink stream from autopilot.
- `mavlink/gcs_image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Image stream to send.

#### Published Topics

- `mavlink/to`
  ([mavros/msg/Mavlink](https://docs.ros.org/en/rolling/p/mavros/msg/Mavlink.html)):
  Mavlink stream to autopilot.

#### Parameters

- `~gcs_url` (`string`, default: `udp://@`): Connection URL.
- `~jpeg_quality` (`int`, default: `60`): JPEG quality level for image
  encoding.

### copter_visualization

Converts information published on mavros topics into
[markers](http://wiki.ros.org/rviz/DisplayTypes/Marker) for
visualization in RVIZ. ![width="720px"](doc/copter_visualization.png)

#### Subscribed Topics

- `local_position`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Position source (e.g. mavros/local_position/local topic)
- `local_setpoint`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Local setpoints (e.g. mavros/setpoint_position/local topic)

#### Published Topics

- `track_markers`
  ([visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)):
  Markers to visualize vehicle path.
- `vehicle_marker`
  ([visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html)):
  Marker to visualize copter model.
- `wp_markers`
  ([visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)):
  Markers to visualize local setpoints.

#### Parameters

- `~fixed_frame_id` (`string`, default: `'local_origin'`): Pose frame
  id.
- `~child_frame_id` (`string`, default: `'fcu'`): Pose child frame id.
- `~marker_scale` (`double`, default: `1.0`): Marker scale factor.
- `~num_rotors` (`int`, default: `4`): Number of rotors in copter model.
- `~arm_len` (`double`, default: `0.22`): Copter model arm length (m).
- `~body_width` (`double`, default: `0.15`): Copter model body width
  (m).
- `~body_height` (`double`, default: `0.10`): Copter model body height
  (m).
- `~max_track_size` (`int`, default: `1000`): Max number of markers in
  track.

## Utility commands

All utilities provides <util> \--help and <util> <command> \--help
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

**PX4** only. Require [fusepy](https://github.com/terencehonles/fusepy)
package, use `sudo pip install fusepy`.



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
[mavros_node](https://index.ros.org/p/mavros).

### cam_imu_sync

Syncronization markers for IMU and Camera. EXPERIMENTAL (TODO)

### distance_sensor

Publish range finders data from FCU; Send data to FCU. (TODO page with
config spec).

#### Subscribed Topics

- `~distance_sensor/<sensor_name>`
  ([sensor_msgs/msg/Range](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Range.html)):
  Send ROS sensor data to FCU.

#### Published Topics

- `~distance_sensor/<sensor_name>`
  ([sensor_msgs/msg/Range](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Range.html)):
  Data from FCU-connected sensor.

#### Parameters

- `~distance_sensor/<sensor_name>/subscriber` (`bool`, default:
  `false`): Subscriber or Publisher
- `~distance_sensor/<sensor_name>/id` (`int`): Sensor Id. **required**
- `~distance_sensor/<sensor_name>/orientation` (`string`): Orientation
  of the sensor. **required** for subscriber.

### image_pub

Publish images from PX4Flow module. **REMOVED IN 0.18**

#### Published Topics

- `~image/camera_image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Image stream from mavlink device.

#### Parameters

- `~image/frame_id` (`string`, default: `px4flow`): Frame ID for
  camera_image topic.

### mocap_pose_estimate

Send ATT_POS_MOCAP message to FCU.

#### Subscribed Topics

- `~mocap/pose`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Pose to send.
- `~mocap/tf`
  ([geometry_msgs/msg/TransformStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TransformStamped.html)):
  Pose to send.

#### Parameters

- `~mocap/use_tf` (`bool`, default: `false`): Vicon mocap system.
- `~mocap/use_pose` (`bool`, default: `true`): Optitrack mocap system.

### px4flow

Publish `OPTICAL_FLOW_RAD` message data from FCU or PX4Flow module.

#### Published Topics

- `~px4flow/raw/optical_flow_rad`
  ([mavros_msgs/msg/OpticalFlowRad](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/OpticalFlowRad.html)):
  Optical flow data.
- `~px4flow/ground_distance`
  ([sensor_msgs/msg/Range](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Range.html)):
  Sonar range data.
- `~px4flow/temperature`
  ([sensor_msgs/msg/Temperature](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Temperature.html)):
  IMU sensor temperature.

#### Parameters

- `~px4flow/frame_id` (`string`, default: `px4flow`): Frame Id.
- `~px4flow/ranger_fov` (`double`, default: `0.0`): Sonar FOV.
- `~px4flow/ranger_min_range` (`double`, default: `0.3`): Sonar minimum
  range.
- `~px4flow/ranger_max_range` (`double`, default: `5.0`): Sonar maximum
  range.

### vibration

Publish VIBRATION message data.

### vision_pose_estimate

Sent VISION_POSITION_ESTIMATE to FCU from PoseStamped topic.

#### Subscribed Topics

- `~vision_pose/pose`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Vision position.
- `~vision_pose/pose_cov`
  ([geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)):
  Vision position (with covariance).

#### Parameters

- `~vision_pose/tf/listen` (`bool`, default: `false`): TF listen switch.
  Disable topic if enabled.
- `~vision_pose/tf/frame_id` (`string`, default: `local_origin`): Origin
  frame_id for TF.
- `~vision_pose/tf/child_frame_id` (`string`, default: `vision`): Child
  frame_id for TF.
- `~vision_pose/tf/rate_limit` (`double`, default: `50.0`): Rate limit
  for TF listener \[Hz\].

### vision_speed_estimate

Send vision speed estimates to FCU.

#### Subscribed Topics

- `~vision_speed/speed_vector`
  ([geometry_msgs/msg/Vector3Stamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3Stamped.html)):
  Send speed vector.
- `~vision_speed/speed_twist`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Send linear speed. (alternative)

#### Parameters

- `~vision_speed/listen_twist` (`bool`, default: `false`): Topic type
  selector.
