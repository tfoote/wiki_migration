## Motivation

For some shared autonomy or supervisory teleoperation tasks in robot
manipulation it is useful to designate a region of interest to make the
perception algorithms more robust to clutter or noise. In this case, an
image is returned to the user and they can specify a filter region for a
3D point cloud by simply defining a polygon on the 2D image. Or they can
request the 3D location of a single point in an image.

## Running the Code

The package requires that the openni_camera package is also installed
and functional. After running rosmake, the following should start the
server:

```
rosrun UI_segment_object segment_object
``` If the server runs without errors and you can
run

```
roslaunch openni_camera openni_kinect.launch
``` the following two service calls should then
give an idea of how the node works:

```
rosservice call /get_object_on_plane
``` and

```
rosservice call /get_3D_pt
``` The /get_object_on_plane service call sequence
of operation is shown below through four images. It first subscribes to
a PointCloud2 message from the Kinect. it then presents the user with a
2D image. The user is then asked to specify a region in the image by
left clicking points on the image to form a polygon. This operation is
terminated by a right click. The 3D points that would be projected
inside the bounding polygon are then filtered from the original Kinect
point cloud and published. A plane is fit to the data using a RANSAC
method from the Point Cloud Library. Finally, the plane is filtered and
the remaining 3D point cloud is published and also returned as a
possible object in the region that the user defined.

![\|height="251px",width="362px"](attachment:full_kinect_cloud.png)
![\|height="250px",width="339px"](attachment:tabletop_image.png)
![\|height="265px",width="362px"](attachment:table_top_region.png)
![\|height="264px",width="368px"](attachment:object.png)

The main purpose for publishing the two point clouds during the process
is for viewing in Rviz for debugging purposes but can also be used
individually to be passed to nodes like the tabletop_object_detector.
They are published under the topics "segment_plane" and
"segment_object".

The 2D polygon defined by the user is stored in a global variable in the
server node and therefore, any subsequent calls to the node no longer
require user interaction if the Kinect sensor hasn't moved. If it has,
there is also a /UI_reset service call that will allow you to redefine
the region of interest on the next call to /get_object_on_plane or
/get_3D_pt.

A good example of how to use this package is found at
[pr2_playpen](pr2_playpen)
