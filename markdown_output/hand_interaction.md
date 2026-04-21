The hand_interaction package is used in the:

-   [ hand detection demo](mit-ros-pkg/KinectDemos/HandDetection)
-   [ finger detection demo](mit-ros-pkg/KinectDemos/HandDetection)
-   [ piano demo](mit-ros-pkg/KinectDemos/HandDetection)

[Youtube](https://www.youtube.com/watch?v=haCyDo7y3BE)

The hand interaction package has several nodes that facilitate hand
interaction Hands are made available through the Hand/Hands message. A
Hands message is just two Hand messages with the header of the point
cloud it came from.

### Hand Field descriptions:

-   **thumb**: index of which finger was determined to be the thumb. a
    negative number means no thumb was detected, (does not mean no
    fingers)
-   **arm**:
-   in **detecthands**: points near, but not in the hand are clustered
    and marked as the arm. It is pretty accurate in giving the direction
    that the arm is facing.
-   in **detectskelhands**: arm represents the skeleton\'s elbow.
-   **palm**: 6D pose of the palm (orientation may not be fully
    functional yet)
-   **fingers**: for each finger detected, the centroid is given.
    Because of how finger segmentation is done, this point will not
    always be the center of the finger, at least in the direction away
    from the palm.
-   **state**: Currently unused. Soon, when pointing is implemented,
    this will indicate what type of gesture is being made (ie: fist,
    peace, openpalm, etc.)

```clearsilver
name = detectskelhands
desc = This node finds the point clouds corresponding to the hands indicated by a skeletal model.
sub {
  0.name = /skeletons
  0.type = body_msgs/Skeletons
  0.desc = The skeleton extracted by the skeletal_tracker.
  1.name = /camera/depth/points2
  1.type = sensor_msgs/PointCloud2
  1.desc = The 3D point cloud provided by the Kinect sensor.
}
pub {
  0.name = /hands
  0.type = body_msgs/Hands
  0.desc = The Hand message, which contains a point cloud of the hands
  1.name = /hand0_fullcloud
  1.type = sensor_msgs/PointCloud2
  1.desc = The left hand point cloud.
  2.name = /hand1_fullcloud
  2.type = sensor_msgs/PointCloud2
  2.desc = The right hand point cloud.
}
```

```clearsilver
name = detectfingers
desc = This node segments a hand into fingers and palm.  It takes in incomplete Hand messages, and fills in information.
sub {
  0.name = /hands
  0.type = body_msgs/Hands
  0.desc = The Hand message in, which contains a point cloud of the hands
}
pub {
  0.name = /hands_pros
  0.type = body_msgs/Hands
  0.desc = The Hand message out, which contains locations and orientations of the fingers
}
```
