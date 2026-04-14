It takes its estimates from the ar_pose_marker node (ARMarker message)
using the [ar_pose](http://www.ros.org/wiki/ar_pose) package and
publishes fused estimated on the poseWithCovOut node (ARMarker message).
The measurement covariance believe is updated according to the
covariance contained in the ARMarker message. An additional ar_marker
node is published containing a visualization_msgs::Marker message for
rviz visualization.

## Usage

-   Set up an ar_pose_marker node which gets pose estimates from your
    sensor. (demo launch files using prosilica cameras are available in
    the [ar_pose_demo package](http://www.ros.org/wiki/ar_pose_demo))
-   Start the ar_pose_ekf component

```
roscd ar_pose_ekf
./runekf.sh
```

-   Read out the fused estimated with e.g. rviz (demo vcg files are
    available in the
    [ar_pose_demo package](http://www.ros.org/wiki/ar_pose_demo))
