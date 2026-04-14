## Object Perception

There are two main components of object perception:

-   object segmentation: which part of the sensed data corresponds to
    the object we want to pick up?
-   object recognition: which object is it?

Our manipulation pipeline always requires segmentation. If recognition
is performed and is successful, this further informs the grasp point
selection mechanism. If not, we can still grasp the unknown object based
only on perceived data.

Note that it is possible to avoid segmentation as well and select grasp
points without knowing object boundaries. The current pipeline does not
have this functionality, but it might gain it in the future.

To perform these tasks we rely the following \'\'\'assumptions\'\'\':

-   the objects are resting on a table, which is the dominant plane in
    the scene
-   the minimum distance between two objects exceeds a given threshold
    (3cm in our demo)
-   in addition, object recognition can only handle 2 degrees of
    freedom: translation along the X and Y axes (with the Z axis assumed
    to be pointing \"up\" relative to the table). Therefore, in order to
    recognize an object:
-   it must be rotationally symmetric
-   it must have a known orientation, such as a glass or a bowl sitting
    \"upright\" on the table.

The sensor data that we use consists of a point cloud from the narrow
stereo or Kinect cameras. We perform the following steps:

-   segmentation
-   the table is detected by finding the dominant plane in the point
    cloud using RANSAC;
-   points above the table are considered to belong to graspable
    objects. We use a clustering algorithm to identify individual
    objects. We refer to the points corresponding to an individual
    object as \'\'\'clusters\'\'\'.
-   recognition
-   for each cluster, a simple iterative fitting technique (a distant
    cousin of ICP) is used to see how well it corresponds to each mesh
    in our database of models. If a good fit is found, the database id
    of the model is returned along with the cluster.
-   note that our current fitting method operates in 2D, since based on
    our assumptions (object resting upright on the known surface of the
    table) the other 4 dimensions are fixed

The output from this components consists of the location of the table,
the identified point clusters, and the corresponding database object id
and fitting pose for those clusters found to be similar to database
objects.

![](attachment:detect_1.png)

\'\'Narrow Stereo image of a table and three objects\'\'

![](attachment:detect_2.png)

\'\'Detection result: table plane has been detected (note the yellow
contour). Objects have been segmented (note the different color point
clouds superimposed on them). The bottle and the glass have also been
recognized (as shown by the cyan mesh further superimposed on them)\'\'

## Nodes

```clearsilver
node.0 {
name=tabletop_segmentation
desc=Segmentation is performed by the `tabletop_segmentation` node. It implements the  [[http://www.ros.org/doc/api/tabletop_object_detector/html/srv/TabletopSegmentation.html|TabletopSegmentation]] service.

sub {
0.name=cloud_in
0.type=sensor_msgs/PointCloud2
0.desc=The pointcloud input that is processed to find the table and tabletop objects.
1.name=markers_out
1.type=visualization_msgs/Marker
1.desc=Markers for visualization of objects segmented in rviz.
}

srv{
0.name=segmentation_srv
0.type=tabletop_object_detector/TabletopSegmentation
0.desc=The service to call to get the segmented objects.
}

sub {
0.name=cloud_in
0.type=sensor_msgs/PointCloud2
0.desc=The pointcloud input that is processed to find the table and tabletop objects.
}

pub{
0.name=markers_out
0.type=visualization_msgs/Marker
0.desc=Markers for visualization of objects segmented in rviz.
}

srv{
0.name=segmentation_srv
0.type=tabletop_object_detector/TabletopSegmentation
0.desc=The service to call to get the segmented objects.
}

param {
0.name= quality_threshold
0.default= 0.005
0.type= float
0.desc= a unit-less threshold that is compared to the results of the model recognition to decide if a model recognition is good enough to be used. Lower numbers indicate a better fit. Reduce this if you want the recognition to be more strict.
1.name= clustering_distance
1.default= 0.03
1.type= float
1.desc= the min distance between objects, provided as input to the segmentation algorithm. Objects closer to each other than this threshold will be merged into the same cluster.
2.name= processing_frame
2.default= empty
2.type= string
2.desc= if non-empty, any received point clouds are first transformed in this frame, before any processing. Useful for operating in a frame where intuitive filters can be applied (e.g. tables can usually be found between z=0.5m and z=1.5m if operating in a frame with the origin on the floor and z pointing up, such as the `base_link` frame of the PR2)
3.name=inlier_threshold
3.type= float
3.desc= .
4.name=plane_detection_voxel_size
4.type= float
4.desc= .
5.name=flatten_table
5.type= bool
5.desc= .
6.name=table_padding
6.type= float
6.desc= .
}
}
```

#### Filtering Parameters

All of these parameters are applied to decide what part of the point
cloud the detector should focus on. They must make sense in the
\`processing_frame\`. If \`processing_frame\` is unspecified, all
processing takes place in the native frame of the incoming cloud, which
on the PR2 robot is the camera frame. Therefore, all these parameters
have default values which makes sense in the camera frame.

```clearsilver
param {
no_header=True
0.name= z_filter_min
0.default= 0.4
0.type= float
0.desc= Incoming point cloud first filtered and only points with z coordinate greater than this value are kept.
1.name= z_filter_max
1.default= 1.0
1.type= float
1.desc= Incoming point cloud first filtered and only points with z coordinate less than this value are kept.
2.name= x_filter_min
2.type= float
2.desc= Incoming point cloud first filtered and only points with x coordinate greater than this value are kept.
3.name= x_filter_max
3.type= float
3.desc= Incoming point cloud first filtered and only points with z coordinate less than this value are kept.
4.name= y_filter_min
4.type= float
4.desc= Incoming point cloud first filtered and only points with x coordinate greater than this value are kept.
5.name= y_filter_max
5.type= float
5.desc= Incoming point cloud first filtered and only points with z coordinate less than this value are kept.
6.name= table_z_filter_min
6.default= 0.01
6.type= float
6.desc= after the table is detected, only points with height above the table by at least this value are kept
7.name= table_z_filter_max
7.default= 0.5
7.type= float
7.desc= after the table is detected, only points with height above the table by at most this value are kept
8.name= up_direction
8.default= -1.0
8.type= float
8.desc= Whether the natural "up" direction (relative to gravity) is closer to positive or negative
}
```

```clearsilver
node.1 {
name=tabletop_object_recognition
desc=Recognition is performed by the `tabletop_object_recognition` node. It implements the  [[http://www.ros.org/doc/api/tabletop_object_detector/html/srv/TabletopObjectRecognition.html|TabletopObjectRecognition]] service. Note that this service directly takes as input the result of the segmentation service above. Note that object recognition needs a connection to the database of known models to perform recognition. This database itself is documented in [[household_objects_database]]. The object recognition service will look for and use the services provided by the `household_object_database_node`.  The names of these services are provided as parameters.

pub{
0.name=markers_out
0.type=visualization_msgs/Marker
0.desc=Markers for visualization of objects recognized in rviz.
}

srv{
0.name=object_recognition_srv
0.type=tabletop_object_detector/TabletopObjectRecognition
0.desc=Runs object recognition.
1.name=clear_exclusions_srv
1.type=tabletop_object_detector/ClearExclusionsList Service
1.desc=Clears the exclusions list.
2.name=add_exclusion_srv
2.type=tabletop_object_detector/AddModelExclusion
2.desc=Adds the given model to the exclusion list.
3.name=negate_exclusions_srv
3.type=tabletop_object_detector/NegateExclusions
3.desc=Negates exclusions
}

param{
0.name=fit_merge_threshold
0.type=float
0.default=0.05
0.desc= .
1.name=min_marker_quality
1.type=float
1.default=0.003
1.desc= .
2.name=model_set
2.desc= .
3.name=get_model_list_srv
3.desc=Service name for get_model_list from the object database node.
4.name=get_model_mesh_srv
4.desc=Service name for get_model_mesh from the object database node.}
}
}

node.2 {
name=tabletop_complete
desc=Most often, segmentation and recognition are used together. To simplify this process, the `tabletop_complete` node will pipe them together, passing the results of segmentation directly to recognition so you don't have to worry about that. It implements the [[http://www.ros.org/doc/api/tabletop_object_detector/html/srv/TabletopDetection.html|TabletopDetection]] service.

srv{
0.type=tabletop_object_detector/TabletopDetection

}
}
```

## Running the Manipulation Pipeline

To launch the manipulation pipeline, complete with the sensor processing
provided here, and execute pickup and place tasks using the PR2 robot,
tutorials and launch files are provided in
[pr2_tabletop_manipulation_apps](pr2_tabletop_manipulation_apps).
