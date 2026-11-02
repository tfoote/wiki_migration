To debug connection issues, try to use `vrpn`'s CLI tools, such as
`vrpn_print_devices <tracker_name>@<vrpn_server>`, to verify that
a connection to the Tracker object of interest can be established. If
you cannot get this to work, note that debugging networking or VRPN
issues is outside the scope of this ROS interface package, and see
[VRPN documentation](https://github.com/vrpn/vrpn/wiki) for further
guidance.

Please check the for common problems, or open an
[issue](https://github.com/paulbovbel/vrpn_client_ros/issues) if still
unsolved. See sample configuration launch file
[here](https://github.com/clearpathrobotics/vrpn_client_ros/blob/indigo-devel/launch/sample.launch).

## Node API

### vrpn_client_node

The client node connects to a remote VRPN server, and exposes
information from the server's Trackers over ROS topics and
[tf2](https://index.ros.org/p/tf2). The client node auto-detects, or is
provided the Tracker names via ROS params (must be
[valid](http://wiki.ros.org/Names#Valid_Names) ROS Graph names).

#### Published Topics

- `<tracker name>/pose`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Tracker pose in world frame.
- `<tracker name>/twist`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Tracker velocity in world frame. Available in VICON Tracker 3.3+.
- `<tracker name>/accel`
  ([geometry_msgs/msg/AccelStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/AccelStamped.html)):
  Tracker acceleration in world frame. Available in VICON Tracker 3.3+.

#### Parameters

- `~update_frequency` (`double`, default: `100.0`): Frequency to process
  incoming updates from the VRPN server.
- `~refresh_tracker_frequency` (`double`, default: `0.0`): Frequency at
  which to auto-detect new Trackers from the VRPN server. Mutually
  exclusive with `trackers`.
- `~trackers` (`list`): List of tracker names to expect from the VRPN
  server. Mutually exclusive with `refresh_tracker_frequency` > 0.0
- `~frame_id` (`string`, default: `"world"`): World frame id for the
  Trackers.
- `~use_server_time` (`bool`, default: `false`): Publish/broadcast using
  VRPN server's timestamp, or the local ROS time.
- `~broadcast_tf` (`bool`, default: `true`): Broadcast transforms of
  Tracker pose on `/tf`.
