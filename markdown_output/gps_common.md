## Experimental Package

This package is a space to stage messages and common GPS-processing
routines that are undergoing a standardization process. Its contents
will probably be moved into [ros-pkg](ros-pkg) once they've matured.

## Messages

gps_common defines two common messages for GPS drivers to output:
<<MsgLink(gps_common/GPSFix)>> and
<<MsgLink(gps_common/GPSStatus)>>.

In most cases, these messages should be published simultaneously, with
identical timestamps.

## Nodes

```clearsilver
node.0 {
 name = utm_odometry_node
 desc = `utm_odometry_node` converts latitude-longitude readings into UTM odometry
 sub{
  0.name= fix
  0.type= sensor_msgs/NavSatFix
  0.desc= GPS measurement and status
  }
 pub{
  0.name= odom
  0.type= nav_msgs/Odometry
  0.desc= UTM-encoded position
  }
 param{
  0.name= ~rot_covariance
  0.type= double
  0.default= 99999
  0.desc= Variance (in meters) to specify for rotational measurements
  1.name= ~frame_id
  1.type= string
  1.default= Copy `frame_id` from `fix` message
  1.desc= Frame to specify in header of outgoing Odometry message
  2.name= ~child_frame_id
  2.type= string
  2.desc= Child frame to specify in header of outgoing Odometry message
  }
```

## Tutorial

See [gpsd_client](gpsd_client) for an example of a sender node that uses
this package's messages.
