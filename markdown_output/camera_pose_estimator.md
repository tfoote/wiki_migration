## Package Proposal

We propose the camera pose estimator to estimate the pose of objects
using a camera and a tbd_msgs/ObjectInImage message.

## ROS Subscriptions

-   tbd_msgs/ObjectInImage object: The object we wish to compute a pose
    for
-   sensor_msgs/CameraInfo camera_info: Information from the camera the
    image came from

## ROS Publications

-   geometry_msgs/PoseStamped object_pose: The resulting pose of the
    object
