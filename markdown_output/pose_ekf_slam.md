# Package Summary

Package \'\'pose-ekf-slam\'\' is a modular localization and mapping
system for 6DoF vehicles. Standard navigation messages as
[PoseWithCovarianceStamped](http://www.ros.org/doc/api/geometry_msgs/html/msg/PoseWithCovarianceStamped.html),
[TwistWithCovarianceStamped](http://www.ros.org/doc/api/geometry_msgs/html/msg/TwistWithCovarianceStamped.html),
and [Imu](http://www.ros.org/doc/api/sensor_msgs/html/msg/Imu.html)
sensor messages are combined by means of an extended Kalman filter. This
node is capable of estimating vehicle position and linear velocity as
well as the position of detected landmarks in real-time. It is entirely
written in python for ROS Fuerte. It\'s philosophy is similar to package
[robot_pose_ekf](http://www.ros.org/wiki/robot_pose_ekf) but with
several enchancements.

-   Author: Narcís Palomeras
-   License: BSD
-   Source: git <https://github.com/narcispr/pose_ekf_slam>

## How to use Pose EKF-SLAM

Package \'\'pose_ekf_slam\'\' contains two nodes:

-   pose_ekf_slam.py
-   test_pose_ekf_slam.py

### pose_ekf_slam

This node receive position fixes of type
[PoseWithCovarianceStamped](http://www.ros.org/doc/api/geometry_msgs/html/msg/PoseWithCovarianceStamped.html)
in the topic ```
/pose_ekf_slam/pose_update
``` linear velocity updates of type
[TwistWithCovarianceStamped](http://www.ros.org/doc/api/geometry_msgs/html/msg/TwistWithCovarianceStamped.html)
are received through the topic ```
/pose_ekf_slam/velocity_update
``` and vehicle
orientation and angular velocity are expected at
```
/pose_ekf_slam/imu_input
``` using an
[Imu](http://www.ros.org/doc/api/sensor_msgs/html/msg/Imu.html) sensor
message. Finally, landmark updates have to be published at
```
/pose_ekf_slam/landmark_update/landmark_id
``` in order to be discovered by the
\'\'pose_ekf_slam\'\' node. They are also
[PoseWithCovarianceStamped](http://www.ros.org/doc/api/geometry_msgs/html/msg/PoseWithCovarianceStamped.html)
messages.\

Outputs of this node are an
[Odometry](http://www.ros.org/doc/api/nav_msgs/html/msg/Odometry.html)
message published at ```
/pose_ekf_slam/odometry
``` and a custom message,
indicating the position and covariance of each landmark, published at
```
/pose_ekf_slam/map
```

### test_pose_ekf_slam

This node can be used to test \'\'pose_ekf_slam\'\' but the main idea is
to be modified for every user in order to transform their navigation
messages, with position, twist or landmarks information, into the kind
of messages expected by the \'\'pose_ekf_slam\'\' node.

## More information

More information about this node can be found at:

N. Palomeras, S. Nagappa, D. Ribas, N. Gracias and M. Carreras.
Vision-based localization and mapping system for AUV intervention.
OCEANS\'13 MTS/IEEE. Bergen, 2013.
