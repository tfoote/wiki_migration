stereo_slam is a ROS node to execute Simultaneous Localization And
Mapping (SLAM) using only one stereo camera. The algorithm was designed
and tested for underwater robotics. This node is based on the
[G2O](http://wiki.ros.org/g2o) library for graph optimization and uses
the power of [libhaloc](https://github.com/srv/libhaloc) to find loop
closures between graph nodes. It uses a keyframe to multi-keyframe loop
closing mechanism, based on keypoint clustering, to improve the SLAM
corrections on feature-poor environments.

See the documentation on [Github](https://github.com/srv/stereo_slam).
