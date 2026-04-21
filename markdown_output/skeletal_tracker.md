The skeletal_tracker package is used in the:

-   [ hand detection demo](mit-ros-pkg/KinectDemos/HandDetection)
-   [ finger detection demo](mit-ros-pkg/KinectDemos/HandDetection)
-   [ piano demo](mit-ros-pkg/KinectDemos/HandDetection)

### Description

The **skeletal_tracker** is a ROS driver wrapper for user tracking. This
package was mostly copied from the niUserTracker demo, and ROS hooks
were added. This package is similar in functionality to the
openni_tracker, only the skeletal positions are given in
body_msgs/Skeleton message.
