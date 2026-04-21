NOTE: The modern, Catkinized source is now here:
<https://github.com/ethz-asl/vicon_bridge>

## Quick Start

```
roslaunch vicon_bridge vicon.launch
``` You may need to set the \"datastream_hostport\"
parameter to your vicon computer\'s ip/hostname

## Operation

The vicon_bridge node initiates a connection with the Vicon data source
(e.g. Nexus or Tracker) via the !DataStream API. The parameter
datastream_hostport should be set to the IP address or hostname and port
(joined with a colon) of the !DataStream server machine, e.g.
192.168.0.254:801 (801 is the default port). The parameter
\`stream_mode\` is used for the call to the !DataStream
\`SetStreamMode()\` method; valid values are \`ServerPush\` and
\`ClientPull\`. **Note:** We experienced buffering problems and
framedrops when using \`ServerPush\` when more than one object is
successfully tracked. We therefore recommend \`ClientPull\`,
unfortunately at the cost of some additional delay.

All available subjects and segments are recognized automatically and are
published as tf transform and
\<\<MsgLink(geometry_msgs/TransformStamped)\>\> as
\`vicon/\<subject_name\>/\<segment_name\>\`.

## Segment Origin Calibration

when an object is created in vicon tracker, it places the origin more or
less arbitrary in the object. To calibrate the origin of a segment,
place the vehicle at the vicon origin that you set during vicon
calibration, and measure/estimate the height (z offset) of your desired
origin from the floor. Then run ```
rosrun vicon_bridge calibrate <subject name> <segment name> <z offset>
``` Poses are
grabbed, averaged and the vehicle is placed in the vicon\'s origin. The
calibration parameters are stored on the parameter server as
/\<subject_name\>/\<segment_name\>/zero_pose (see
[Origin Calibration Parameters](#Origin_Calibration_Parameters)). On
startup, the node checks if calibration parameters are available. Do
this the first time while running rviz and observe what happens (and if
everything went correct ;-) ).

## Simulating bad Data

Sometimes vicon data is too perfect ;-) This motivated \`tf_distort\`,
which adds different types of noise, adds delay or reduces the framerate
to test how robots work with bad data. ```
rosrun vicon_bridge tf_distort
``` Then run
[reconfigure_gui](dynamic_reconfigure#reconfigure_gui) to set the
parameters. This is work in progress, suggestions are welcome.

## Nodes

```clearsilver
node.0{
  name = vicon_bridge
  desc = interface to the Vicon !DataStream SDK
  pub {
    0.name = vicon/<subject_name>/<segment_name>
    0.type = geometry_msgs/TransformStamped
    0.desc = pose of the <subject>/<segment>
    1.name = vicon/markers
    1.type = vicon_bridge/Markers
    1.desc = publishes all labeled and unlabeled markers. Labeled markers are not affected by origin calibration.
  }
  srv {
    0.name = ~/calibrate_segment
    0.type = vicon_bridge/viconCalibrateSegment
    0.desc = service to calibrate the origin of a segment, see also [[#Segment_Origin_Calibration|segment origin calibration]].
    1.name = ~/grab_vicon_pose
    1.type = vicon_bridge/viconGrabPose
    1.desc = grabs n poses for a given <subject>/<segment> and returns the averaged pose
  }
  param {
    group.0{
      name = Static Parameters
      desc = parameters that are statically set
      1.name = ~stream_mode
      1.type = string
      1.desc = mode to connect to the !DataStream server. Values: "!ClientPull", "!ServerPush".
      1.default = "!ClientPull
      2.name = ~datastream_hostport
      2.type = string
      2.desc = host and port of the !DataStream server (<ip/hostname>:<port>).
      2.default = vicon:801
      3.name = ~tf_ref_frame_id
      3.type = string
      3.desc = tf reference frame id
      3.default = world
    }
    group.1 {
      name = Origin Calibration Parameters 
      desc = Origin pose for each <subject/segment>, i.e. the pose of the segment seen from the vicon frame.
      0.name = ~/<subject_name>/<segment_name>/zero_pose/orientation/w
      0.type = double
      0.desc = .
      0.default = 1
      1.name = ~/<subject_name>/<segment_name>/zero_pose/orientation/x
      1.type = double      
      1.desc = .
      1.default = 0
      2.name = ~/<subject_name>/<segment_name>/zero_pose/orientation/y
      2.type = double
      2.desc = .
      2.default = 0
      3.name = ~/<subject_name>/<segment_name>/zero_pose/orientation/z
      3.type = double
      3.desc = .
      3.default = 0
      4.name = ~/<subject_name>/<segment_name>/zero_pose/position/x
      4.type = double
      4.desc = .
      4.default = 0
      5.name = ~/<subject_name>/<segment_name>/zero_pose/position/y
      5.type = double
      5.desc = .
      5.default = 0
      6.name = ~/<subject_name>/<segment_name>/zero_pose/position/z
      6.type = double
      6.desc = .
      6.default = 0
    }
  }
  param_set{
      group.0 {
      name = Origin Calibration Parameters 
      desc = Origin pose for each <subject/segment>, i.e. the pose of the segment seen from the vicon frame.
      name = Origin Calibration Parameters 
      desc = Origin pose for each <subject/segment>, i.e. the pose of the segment seen from the vicon frame.
      0.name = ~/<subject_name>/<segment_name>/zero_pose/orientation/w
      0.type = double
      0.desc = .
      0.default = 1
      1.name = ~/<subject_name>/<segment_name>/zero_pose/orientation/x
      1.type = double      
      1.desc = .
      1.default = 0
      2.name = ~/<subject_name>/<segment_name>/zero_pose/orientation/y
      2.type = double
      2.desc = .
      2.default = 0
      3.name = ~/<subject_name>/<segment_name>/zero_pose/orientation/z
      3.type = double
      3.desc = .
      3.default = 0
      4.name = ~/<subject_name>/<segment_name>/zero_pose/position/x
      4.type = double
      4.desc = .
      4.default = 0
      5.name = ~/<subject_name>/<segment_name>/zero_pose/position/y
      5.type = double
      5.desc = .
      5.default = 0
      6.name = ~/<subject_name>/<segment_name>/zero_pose/position/z
      6.type = double
      6.desc = .
      6.default = 0
    }
  }
  prov_tf {
    0.from = world
    0.to   = vicon/<subject_name>/<segment_name>
    0.desc = tf transform from world to vicon/<subject_name>/<segment_name>.`from` can be changed with `~tf_ref_frame_id`.
  }
}
node.1{
  name = calibrate
  desc = Node to call the origin pose calibration service for a give subject and segment name plus additional height of the origin. 
  srv_called {
    0.name = ~/calibrate_segment
    0.type = vicon_bridge/viconCalibrateSegment
    0.desc = service to calibrate the origin of a segment, see also [[#Segment_Origin_Calibration|segment origin calibration]].
  }
}
```
