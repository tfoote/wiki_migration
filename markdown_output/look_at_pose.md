## Description

A ROS service that rotates a camera to look at any given pose, while
maintaining an upright camera. We use this to track positions in the
world as the base of the robot moves.

*<Example://> This camera has a rough initial alignment with the object
of interest (the pink cylinder) and it is nearly upside-down. The pose
returned from a call to look_at_pose is well-aligned and the camera is
upright.*

![alt text\|width=400](attachment:init_cam_pose.png)

![alt text\|width=400](attachment:new_cam_pose.png)

## Installation

```
sudo apt install ros-kinetic-look-at-pose
```

or, clone and build from
[ Github]( https://github.com/UTNuclearRoboticsPublic/look_at_pose ).

## Usage

To launch the server and send a set of test data:

```
rosrun rviz rviz
```

In RViz, turn on **TF** and **Marker** (topic: visualization_marker) to
see the original camera frame, new camera frame, and point of interest.

```
rosrun look_at_pose look_at_pose_server
```

```
rosrun look_at_pose test_client
```

![alt text\|width=800](attachment:rviz.png)

## Inputs and Outputs

The service request requires 3 parts. IMPORTANT: all 3 parts should be
given in the frame of the camera. You may need to use some tf magic to
get things in the correct frame.

-   *geometry_msgs/PoseStamped initial_cam_pose*: The current pose of
    the camera. This should be point (0,0,0) and quaternion (0,0,0,1) in
    the camera\'s own frame.

```{=html}
<!-- -->
```
-   *geometry_msgs/PoseStamped target_pose*: Where should the camera
    look? The orientation actually isn\'t used.

```{=html}
<!-- -->
```
-   *geometry_msgs/Vector3Stamped up*: A vector that defines \"UP.\" If
    Z of the camera frame is up, then it would be (0,0,1).

The service response is another PoseStamped in the initial camera frame:

-   *geometry_msgs/PoseStamped new_cam_pose*

## Issues/Limitations

It\'s currently assumed that X is the \"lens vector\" of the camera and
Z of the camera frame should point up. If your situation requires
something else, please create an issue on the
[ Github issue tracker]( https://github.com/UTNuclearRoboticsPublic/look_at_pose/issues ).
