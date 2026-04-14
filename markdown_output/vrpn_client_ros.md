To debug connection issues, try to use \`vrpn\`\'s CLI tools, such as
\`vrpn_print_devices \<tracker_name\>@\<vrpn_server\>\`, to verify that
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

```clearsilver
name = vrpn_client_node
desc = The client node connects to a remote VRPN server, and exposes information from the server's Trackers over ROS topics and [[tf2]]. The client node auto-detects, or is provided the Tracker names via ROS params (must be [[http://wiki.ros.org/Names#Valid_Names|valid]] ROS Graph names).
pub{
  0.name = <tracker name>/pose
  0.type = geometry_msgs/PoseStamped
  0.desc = Tracker pose in world frame.
  1.name = <tracker name>/twist
  1.type = geometry_msgs/TwistStamped
  1.desc = Tracker velocity in world frame. Available in VICON Tracker 3.3+.
  2.name = <tracker name>/accel
  2.type = geometry_msgs/AccelStamped
  2.desc = Tracker acceleration in world frame. Available in VICON Tracker 3.3+.
}
param {
  0.name = ~update_frequency
  0.type = double
  0.desc = Frequency to process incoming updates from the VRPN server.
  0.default = 100.0
  1.name = ~refresh_tracker_frequency
  1.type = double
  1.desc = Frequency at which to auto-detect new Trackers from the VRPN server. Mutually exclusive with `~trackers`.
  1.default = 0.0
  2.name = ~trackers
  2.type = list
  2.desc = List of tracker names to expect from the VRPN server. Mutually exclusive with `~refresh_tracker_frequency` > 0.0
  3.name = ~frame_id
  3.type = string
  3.desc = World frame id for the Trackers.
  3.default = "world"
  4.name = ~use_server_time
  4.type = bool
  4.desc = Publish/broadcast using VRPN server's timestamp, or the local ROS time.
  4.default = false
  5.name = ~broadcast_tf
  5.type = bool
  5.desc = Broadcast transforms of Tracker pose on `/tf`.
  5.default = true
}
```
