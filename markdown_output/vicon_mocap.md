## Other Vicon Packages

There are some other packages with different capabilities; it is
recommended that you also consider these in light of your own project's
needs:

-   [vicon_bridge](vicon_bridge) - A fork of vicon_mocap with some
    additional capabilities, e.g. multiple subjects/segments. Like
    vicon_mocap, it uses the !DataStream SDK to access the data.
-   [vicon](vicon) - This package appears to implement its own TCP
    interface to the Vicon host.

## ROS API

```clearsilver
name=vicon_recv_direct
desc=Driver for using data from VICON motion capture system. This driver was geared initially towards tracking a single rigid body (one VICON 'Segment'), but has been extended to include tracking of individual marker locations. It requires the VICON !DataStream SDK library to be installed.

pub{
0.name=~output
0.type=geometry_msgs/TransformStamped
0.desc=Transforms for the segment being tracked.

1.name=~markers
1.type=vicon_mocap/Markers
1.desc=Marker positions.
}
srv{

1.name=~grab_vicon_pose
1.type=vicon_mocap/viconGrabPose
1.desc=Take N consecutive measurements of a specified segment, return the average of these.
}


param {
group.0 {
0.name= ~stream_mode
0.default= `"ClientPullPreFetch"`
0.type= str
0.desc= Streaming mode. Possible values: `"ServerPush"`, `"ClientPull"`, `"ClientPullPreFetch"`.

1.name= ~datastream_hostport
1.default= `""`
1.type= str
1.desc= Hostname or IP address and port, e.g. 192.168.1.1:801.

2.name= ~subject_name
2.default= `""`
2.type= str
2.desc= Name of VICON Subject to track.

3.name= ~segment_name
3.default= `""`
3.type= str
3.desc= Name of VICON Segment to track.

4.name= ~update_rate
4.default= 100
4.type= double
4.desc= Rate in Hz at which to publish output.

5.name= ~vicon_capture_rate
5.default= 50
5.type= double
5.desc= Rate in Hz at which VICON system is capturing data.

7.name= ~tf_ref_frame_id
7.default= `"/enu"`
7.type= str
7.desc= Reference frame for broadcast TF transforms.

8.name= ~tf_tracked_frame_id
8.default= `"/pelican1/flyer_vicon"`
8.type= str
8.desc= ID of tracked frame in broadcast TF transforms.

9.name= ~time_bias_reset
9.default= `0.05`
9.type= double
9.desc= Maximum offset between current clock time and time based on `time_datum + framenumber*(1/vicon_capture_rate)`. If the offset becomes greater than the `time_bias_reset` value then `time_datum` is set to the current time. 

10.name= ~enable_tf_broadcast
10.default= `false`
10.type= bool
10.desc= When `true`, broadcast TF transforms for the tracked segment. 
}
}
prov_tf {
  0.from = <tf_ref_frame_id>
  0.to   = <tf_tracked_frame_id>
  0.desc = Transform of tracked segment (note: only published if `~enable_tf_broadcast` is set).
}
```
