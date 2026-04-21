## Overview

**tabletop_objects** is a package for detecting and localizing objects
located on some kind of supporting planar surface (table, countertop).

The object detection is performed in two steps: a *bottom-up* step that
tries to come up with initial estimation of the object's pose, followed
by a *top-down* model fitting step that tries to fit 3D models at each
location estimated in the first step.

#### Bottom-up pose estimation

In the bottom-up pose estimation the initial object poses are estimated.
This is currently done by using the dense point cloud coming from the
stereo camera (with projected pattern). The point cloud is first
filtered to remove the points corresponding to the table plane, then the
remaining point clouds are grouped into clustered using a mean-shift
clustering and further filtered using priors on cluster size and
proximity. The remaining clusters used to estimate the initial object
poses.

![](attachment:tabletop_clusters_cloud.png)

![](attachment:tabletop_clusters.png)

We are working on improving the object pose initialization pipeline
described above by incorporating additional cues about the objects's
location and orientation using a set of 3D features.

This step is implemented in the **tabletop_detector** node.

#### Top-down model fitting

In this step, the object pose estimations computed in the bottom-up step
are used to fit 3D models to their respective locations. Doing that
allows us to determine the object identity and refine the object's pose
with high accuracy. For performing the model fitting we are using an
ICP-like (Iterative Closest Point) algorithm combined with a 3D distance
transform for fast nearest point computations.

![](attachment:tabletop_models_cloud.png)

![](attachment:tabletop_models.png)

This step is implemented in the **model_fitter** node.

## Nodes



```clearsilver
node.0 {
 name = tabletop_detector
 desc = `tabletop_detector` performs the first step (bottom-up detection) described above
 sub{
  0.name= narrow_stereo/left/image_rect
  0.type= sensor_msgs/Image
  0.desc= Rectified left narrow stereo image.
  1.name= narrow_stereo/disparity
  1.type= sensor_msgs/Image
  1.desc= Dispartity of the narrow stereo.
  2.name= narrow_stereo/disparity_info
  2.type= stereo_msgs/DisparityInfo
  2.desc= Dispartity info of the narrow stereo.
  3.name= narrow_stereo/right/image_rect
  3.type= sensor_msgs/Image
  3.desc= Rectified right narrow stereo image.
  4.name= tf_message
  4.type= tf/tfMessage
  4.desc= tf transforms.
  5.name= narrow_stereo/cloud
  5.type= sensor_msgs/PointCloud
  5.desc= Narrow stereo pointclound.
  6.name= narrow_stereo/left/camera_info
  6.type= sensor_msgs/CameraInfo
  6.desc= Narrow stereo camera info.
  }
 pub {
  0.name= tabletop_detector/objects
  0.type= sensor_msgs/PointCloud
  0.desc= Publishes a point cloud with all the objects point cloud after table plane was removed.
  1.name= visualization_marker
  1.type= visualization_msgs/Marker
  1.desc= Publishes various markers used for debugging purposes.
  2.name= track_object
  2.type= tabletop_objects/TrackObject
  2.desc= Publishes information used to initialize the `model_tracker` node
 }
 srv {
  0.name= table_top/find_object_poses
  0.type= tabletop_objects/FindObjectPoses
  0.desc= Service called for initiating the object detection.
 }
 param {
  0.name= ~display
  0.default= `false`
  0.type= bool
  0.desc= Used to enable the display of debugging information.
  1.name= ~min_points_per_cluster
  1.default= 10
  1.type= int
  1.desc= Minimum points each cluster representing an object should have.
  2.name= ~max_clustering_iterations
  2.default= 7
  2.type= int
  2.desc= Maximum of clustering iterations to perform.
  3.name= ~min_object_distance
  3.default= 0.05
  3.type= double
  3.desc= Minimum distance between two distinct objects.
  4.name= ~min_object_height
  4.default= 0.05
  4.type= double
  4.desc= Mimimum height of an object.
  5.name= ~target_frame
  5.default= `"odom_combined"`
  5.type= string
  5.desc= Target frame in which to return the object pose.
 }
}
node.1{
 name = model_fitter
 desc = `model_fitter` implements the top-down model fitting described above.
 pub {
  0.name= visualization_marker
  0.type= visualization_msgs/Marker
  0.desc= Publishes various markers used for debugging purposes.
 }
 srv {
  0.name= tabletop_objects/model_fit
  0.type= tabletop_objects/ModelFit
  0.desc= Starts a model fit on a point cloud.
 }
 param {
  0.name= ~template_path
  0.default= `""`
  0.type= string
  0.desc= The path where the object models are stored (currently the node can handle models in [[http://en.wikipedia.org/wiki/PLY_(file_format)|PLY]] format).
 }
}
node.2{
 name = model_tracker
 desc = `model_tracker` tracks a model after it was initially detected by the previous detection pipeline.
 sub{
  0.name= track_object
  0.type= tabletop_objects/TrackObject
  0.desc=  Receives the target object to track from the `tabletop_detector` node and initialized tracking.
  1.name= narrow_stereo/cloud
  1.type= sensor_msgs/PointCloud
  1.desc= Narrow stereo pointclound.
  }
 pub {
  0.name= visualization_marker
  0.type= visualization_msgs/Marker
  0.desc= Publishes various markers used for debugging purposes.
 }
 param {
  0.name= ~template_path
  0.default= `""`
  0.type= string
  0.desc= The path where the object models are stored (currently the node can handle models in [[http://en.wikipedia.org/wiki/PLY_(file_format)|PLY]] format).
 }
}
```



## Tutorials

This is a tutorial on how to use functionality provided by this package.

-   Build the *tabletop_objects* package:

```
rosmake tabletop_objects
```



```{=html}
<!-- -->
```
-   Make sure the robot is up, the projected pattern is on and that the
    stereo camera is working. For help with the stereo camera see
    [this](image_pipeline/Tutorials/IntroductionToUsingTheStereoCameras).

```{=html}
<!-- -->
```
-   Launch the nodes: 

```
roscd tabletop_objects
roslaunch launch/model_fitter.launch
```



```{=html}
<!-- -->
```
-   At this point the tabletop object detection pipeline is up and ready
    to go, however it will only start the detection when the
    **table_top/find_object_poses** service is called. For a quick test
    (to make sure everything is running properly), you can run the
    'test_service' node, which just calls the above service:
    

```
rosrun tabletop_objects test_service
```

For a more complex example, of how to use
    the tabletop_objects detector and integrate it with the planing
    pipeline, see the 'simple.cpp' source file in the
    **tabletop_scripts** package.

## Video

[Youtube](https://www.youtube.com/watch?v=hZgYmo6vxJY)
