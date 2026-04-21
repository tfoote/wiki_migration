## Details

[Youtube](https://www.youtube.com/watch?v=YE9eKgek5pI)

## ROS API

![](attachment:rgbd_system.png)

The package provides the following ROS nodes/nodelets:

-   [ rgbd_image_proc](ccny_rgbd/rgbd_image_proc ): processes raw OpenNI
    camera data by performing image rescaling, rectification,
    registration, and depth unwarping. Also see
    [ccny_openni_launch](ccny_openni_launch)
-   [ feature_viewer](ccny_rgbd/feature_viewer ): auxliary node which
    lets users test out different feature detectors, and visualize
    feature locations and covariances in [rviz](rviz)
-   [ visual_odometry ](ccny_rgbd/visual_odometry ): visual odometry
    based on sparse 3D features.
-   [ keyframe_mapper ](ccny_rgbd/keyframe_mapper ): a map server which
    stores RGBD keyframes, performs (offline) graph-based SLAM, and
    handles map generation and disk output.

## Quick usage

First, launch the device and image processing via
[ccny_openni_launch](ccny_openni_launch).

```
roslaunch ccny_openni_launch openni.launch publish_cloud:=true
```

Next, launch
[ visual_odometry.launch](https://github.com/ccny-ros-pkg/ccny_rgbd_tools/blob/master/ccny_rgbd/launch/visual_odometry.launch )
for visual odometry, or
[ vo+mapping.launch](https://github.com/ccny-ros-pkg/ccny_rgbd_tools/blob/master/ccny_rgbd/launch/vo+mapping.launch )
for visual odometry and mapping interfaces.

```
roslaunch ccny_rgbd vo+mapping.launch
```

Launch [rviz](rviz), and load the
[ vo+mapping.vcg](https://github.com/ccny-ros-pkg/ccny_rgbd_tools/blob/master/ccny_rgbd/launch/vo+mapping.vcg )
configuration file.

If you are using the mapping interface, you can call the following
services to perform graph-based SLAM (offline):

```
rosservice call /generate_graph 
rosservice call /solve_graph
```

You can publish the resulting keyframe to rviz:

```
rosservice call /publish_keyframes  ".*"
```

Or save the entire map as a pcd:

```
rosservice call /save_pcd_map /home/your_user_name/my_map.pcd
```

For more options, consult the individual app pages.

## References

Ivan Dryanovski, Roberto G. Valenti, Jizhong Xiao. *Fast Visual Odometry
and Mapping from RGB-D Data*. 2013 International Conference on Robotics
and Automation (ICRA2013).

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports and
feature requests.

Please submit your tickets through
[github](https://github.com/ccny-ros-pkg/ccny_rgbd_tools/issues/)
(requires github account) or by emailing the maintainers.
