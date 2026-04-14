![Nao TF](attachment:nao_tf.png)

## Documentation

Nao\'s URDF description contains all joints and links according to the
[documentation by Aldebaran Robotics](http://www.aldebaran-robotics.com/documentation/)
for V3 and V4 Naos. In accordance with
[REP-105 (Coordinate Frames for Mobile Platforms)](http://www.ros.org/reps/rep-0105.html)
and
[REP-120 (Coordinate Frames for Humanoid Robots)](http://ros.org/reps/rep-0120.html)
the root link is \'\'\'base_link\'\'\', directly connected to
\'\'\'torso\'\'\'. The camera frames are \'\'\'!CameraBottom_frame\'\'\'
and \'\'\'!CameraTop_frame\'\'\'. [nao_remote](nao_remote) publishes the
\'\'\'odom -\> base_link\'\'\' transform and a
\'\'\'base_footprint\'\'\' frame, projected between the feet on the
ground. The defined links for the end effectors are
\'\'\'\[l\|r\]\_gripper\'\'\' for the arms and
\'\'\'\[l\|r\]\_sole\'\'\' for the feet.

![Nao Urdf\|width=1250 height=1032](attachment:NaoUrdf.png)

[CategoryURDF](CategoryURDF)
