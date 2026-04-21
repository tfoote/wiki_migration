![Result of the VisualNet for the moving cupboard door\|width=500](attachment:visual_net_img1.png)

The main task of the Visual Net is the segmentation of the whole set of
2D feature points tracked between frames into an unknown number of
clusters.

The Visual Net provides two core components: clustering of features
according to different criteria (represented by so-called *predictors*)
and 3d estimation of the clustered features using structure from motion.
However, structure from motion can be switched off if a 3d sensor such
as kinect is used.

## Package Description

The package contains only one node, called *visual_net*. In the
following we explain which parameters can be set, and how to handle
input and output data.

### Information Flow

-   Visual net subscribes to a feature topic, where some kind of feature
    tracker publishes a set of visual 2D or 3D features (as a PCL point
    cloud) at every time step
-   If certain (definable) thresholds are exceeded, namely that the
    *global_motion* of the features is sufficient and that at least
    *min_cluster_size* feature move by an amount of *min_motion*
    pixels/cm (depending on the sensor), the segmentation is triggered.
    If a 2d sensor is used, the structure from motion computation is
    triggered, too.
-   After computation, visual net publishes the segmentation and (if
    structure from motion is used) the estimated 3d positions of the
    features.

### Parameters

**/number_features**

-   type: *int*
-   description: Set how many features will be published (can be set
    dynamically using topic /iap/num_features). The parameter is also
    used by visual net, feature tracker etc.

**/video_sensor_type**

-   type: *string*
-   description: Which video sensor you are using. Possible values are
    *kinect* (kinematic analyzer will subscribe to topic
    *camera/rgb/image_color*) and *usb_cam* (kinematic analyzer will
    subscribe to topic *camera/image_raw*)

**/min_cluster_size**

-   type: *int*
-   description: *min_cluster_size* features have to move at least
    *min_motion* to trigger the segmentation (and *min_global_motion*
    has to be exceeded)

**/min_motion**

-   type: *double*
-   description: *min_cluster_size* features have to move at least
    *min_motion* to trigger the segmentation (and *min_global_motion*
    has to be exceeded)

**/min_global_motion**

-   type: *double*
-   description: The minimal global motion to trigger a segmentation (if
    also min_motion and min_cluster_size are exceeded, see above)

**/segmenting_in_3d**

-   type: *bool*
-   description:

**/visual_net/external_trigger**

-   type: *bool*
-   description:

**/3d_from_sensor**

-   type: *bool*
-   description: If true, kinematic analyzer subscribes to topic
    */iap/feature_set_3d*, otherwise to */iap/estimated_feature_set_3d*

If */3d_from_sensor* is true, visual net also expects data from the
following topics: **/video_height** **/video_width** **/focal_length**

Predictors and parameters:

**/visual_net/use_rm_predictor**

-   type: *bool*
-   description: Use (2D) relative motion predictor

**/visual_net/rm_min_dist**

-   type: *double*
-   description: Distance for 2D relative motion predictor

**/visual_net/use_rm3d_predictor**

-   type: *bool*
-   description: Use (3D) relative motion predictor

**/visual_net/rm3d_min_dist**

-   type: *double*
-   description: Distance for 3D relative motion predictor

**/visual_net/use_fm_predictor**

-   type: *bool*
-   description: Use fundamental matrix predictor

**/visual_net/fm_num_hypo**

-   type: *double*
-   description: Number of hypothesis for fundamental matrix predictor

**/visual_net/fm_num_trials_per_hypo**

-   type: *double*
-   description: Number of trials per hypothesis for fundamental matrix
    predictor

**/visual_net/use_sd_predictor**

-   type: *bool*
-   description: Use short distance predictor

**/visual_net/sd_min_dist**

-   type: *double*
-   description: Minimal distance for short distance predictor

**/visual_net/use_ld_predictor**

-   type: *bool*
-   description: Use long distance predictor

**/visual_net/ld_min_dist**

-   type: *double*
-   description: Minimal distance for long distance predictor

**/visual_net/ld_max_dist**

-   type: *double*
-   description: Maximal distance for long distance predictor

**/visual_net/use_t_predictor**

-   type: *bool*
-   description: Use triangulation predictor

**/visual_net/use_csegm_predictor**

-   type: *bool*
-   description: Use color segmentation predictor

**/visual_net/use_csimil_predictor**

-   type: *bool*
-   description: Use color similarity predictor

### ROS Subscribers

**/iap/feature_set_2d**

-   type:*sensor_msgs/PointCloud2*
-   description: A set of 2D features at a time.

**/iap/feature_set_3d**

-   type: *sensor_msgs/PointCloud2*
-   description: A set of 3D features at a time.

**/iap/visual_net/run_segm_and_sfm**

-   type: *std_msgs/Empty*
-   description: Trigger segmentation and structure from motion
    computation

### ROS Publishers

**/iap/segmentation**

-   type: *sensor_msgs/PointCloud2*
-   description: A segmentation of the features into clusters. Returns a
    list of the same length as indicated by parameter *number_features*,
    containing the cluster ID for every feature.

**/iap/estimated_feature_set_3d**

-   type: *sensor_msgs/PointCloud2*
-   description: If structure from motion is activated, visual net
    publishes the 3D feature set here

### ROS Services

None.

### ROS Messages

None. See [iap_common](iap_common).
