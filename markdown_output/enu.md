Node wrappers for cartesian-!LatLong conversion functions in
[libswiftnav](https://github.com/swift-nav/libswiftnav). Serves as the
glue between <<MsgLink(sensor_msgs/NavSatFix)>>-producing sensor
nodes and [robot_pose_ekf](robot_pose_ekf).

## Nodes



```clearsilver
node.0 {
 name = from_fix
 desc = Receives navigation fixes, and publishes ENU Odometry messages in a local frame cartesian frame, either specified by parameters, or simply taking the initial fix as origin.
 sub{
  0.name = fix
  0.type = sensor_msgs/NavSatFix
  0.desc = Input fixes from a satellite navigation system or other source.
  }
 pub{
  0.name = enu
  0.type = nav_msgs/Odometry
  0.desc = Input fix transformed into local cartesian frame.
  1.name = enu_datum
  1.type = sensor_msgs/NavSatFix
  1.desc = Latitude, longitude, and altitude of the point used as origin in the local cartesian frame.
  }
 param {
  0.name = ~datum_latitude, ~datum_longitude, ~datum_altitude
  0.type = doubles
  0.desc = Location to use as origin in local frame. If unspecified, use location from initial message on `fix` topic. 
  }
 }
```


