![\|height=\"200\",width=\"333\"](attachment:Logo-white-medium.jpg)

# Description

This package estimates Next-Best-Views as well as configurations (target
positions and orientations) for a robot, where it is most likely to find
and recognize searched objects the poses of which have, e.g., been
predicted by means of ISM trees.

# Functionality

This tool uses an iterative generate-and-test algorithm. Each iteration
results in a NextBestView, the algorithm stops if the NextBestViews of
two consecutive iteration steps have almost no improvement. The idea of
the NextBestView is that it tells you where it is most probable that
objects will be found.

The following images describe basic concepts to understand the
next_best_view node:
![\|height=\"200\",width=\"333\"](attachment:frustum.png)
![\|height=\"200\",width=\"500\"](attachment:hypothesis.png)
![\|height=\"200\",width=\"150\"](attachment:normals.png)

The first image shows the robot and its frustum (view field), which
indicates the area where objects can be found. This view field is also
named \'view\'. The second image shows object hypotheses. An object
hypothesis is a pose (position and orientation) of an object, which are
predictions where this object could probably be found. The more objects
are in a cluster, the more likely the recognizers can find objects at
this location. So the variety of positions and orientations of object
hypotheses determine the possible information gain. The third image
shows the object normals. The camera should search the object from these
directions to increase the likelihood of detecting the object.

In each iteration step, views are generated and then rated. The view
with the best rating is chosen as !NextBestView for that iteration step.

The next_best_view node uses a set of modules:

-   **!SpaceSampler**: Generates positions to generate views. The
    algorithm is given a contractor which specifies the granularity. A
    high contractor value results in huge gaps between views and almost
    the whole world is covered with samples. A low contracor value
    generates high dense samples near a given position.
-   **!UnitSphereSample**r: Generates orientations to generate views.
    The algorithm is given a number of orientations which specifies the
    granularity.
-   **!RatingModule**: Used to rate generated views.
-   **!CameraModelFilter**: Used to find hypotheses inside a camera
    frustum.
-   **!HypothesisUpdater**: Does the update (removes normals inside a
    given frustum).

Each module has at least one implementation, which can be chosen through
parameter configuration.

Implementations:

-   **!HypothesisUpdater**
-   !PerspectiveHypothesisUpdater: Uses the rating to remove only
    normals showing towards the camera.
-   !DefaultHypothesisUpdater: Removes all normals in the frustum.
-   **!CameraModelFilter**
-   !StereoCameraModelFilter: Based on two !SingleCameraModelFilter.
-   !SingleCameraModelFilter: Filters objects in the frustum using
    pcl::!FrustumCulling.
-   Raytracing3DBasedStereoCameraModelFilter: Based on
    !StereoCameraModelFilter. Filters object hypotheses which are
    occluded by the environment.
-   Raytracing3DBasedSingleCameraModelFilter: Based on !
-   !SingleCameraModelFilter. Filters object hypotheses which are
    occluded by the environment.
-   **!SpaceSampler**
-   !MapBasedHexagonSpaceSampler: Default, sampling can be seen in the
    image below.
-   !MapBasedRandomSpaceSampler: Samples a fixed number of positions
    randomly.

To get a set of viewports from a set of positions and orientations, the
cross product between those two sets is used. The resulting set of
viewports is filtered by world and hypotheses information (!MapHelper
and !CameraModelFilter class).

The following two images show the orientation and position sampling.
Each arrow on the sphere shows the endposition of one direction vector
which starts in the center of the sphere. The red rectangle limits the
space sampling area. All hexagon corners and the center of the rectangle
are used to generate viewports.
![\|height=\"270\",width=\"333\"](attachment:orientationsampling.png)
![\|height=\"333\",width=\"333\"](attachment:spacesampling.png)

Filter steps:

1\. Positions that can\'t be navigated by the robot are removed when
generating positions. 1. Orientations that can\'t be reached by the PTU
are removed. 1. Positions that are too far away from hypotheses are
removed using a kd-tree/radius search (this is also used to get a first
set of nearby hypotheses that might be in the frustum of a view). 1.
Views that have no samples in their frustum are removed.

The !NextBestViewCalculator class manages all modules.

# Usage

To find a !NextBestView, we must first call the !SetAttributedPointCloud
and !SetInitRobotState service calls, then we can use the
!GetNextBestView service call to get our !NextBestView.
!SetAttributedPointCloud sets and visualizes the pointcloud as shown
above in the second and third image, triggerFrustumVisualization is used
to display the blue frustum which can be seen above in the first image.

To invalidate hypotheses in a frustum, call the !UpdatePointCloud
service call with the camera pose.

## Needed packages

-   [asr_robot_model_services](http://wiki.ros.org/asr_robot_model_services)
-   [asr_mild_navigation](http://wiki.ros.org/asr_mild_navigation)
-   [asr_world_model](http://wiki.ros.org/asr_world_model)
-   [asr_flir_ptu_driver](http://wiki.ros.org/asr_flir_ptu_driver)
-   [asr_rapidxml](http://wiki.ros.org/asr_rapidxml)
-   [asr_object_database](http://wiki.ros.org/asr_object_database)
-   [asr_msgs](http://wiki.ros.org/asr_msgs)
-   [costmap_2d](http://wiki.ros.org/costmap_2d)

## Needed software

-   [Boost (1.54.0.1)](http://www.boost.org/)
-   [Eigen (3.2.0)](http://eigen.tuxfamily.org/index.php?title=Main_Page)
-   [PCL 1.7](http://pointclouds.org/)
-   [Assimp](http://www.assimp.org/)

## Start system

Just run **roslaunch asr_next_best_view next_best_view_core_sim.launch**
to get the next_best_view node running for the simulation or **roslaunch
asr_next_best_view next_best_view_core_real.launch **to get it running
in a real environment.

# ROS Nodes

## Subscribed Topics

-   **map**
-   message type: nav_msgs/OccupancyGrid
-   published by package: map_server
-   description: 2D map of the world
-   **move_base/global_costmap/costmap**
-   message type: nav_msgs/OccupancyGrid
-   published by package: asr_mild_navigation
-   description: 2D map with consideration of obstacles and the size of
    the robot, so that no collision can take place between the robot and
    the obstacles

## Published Topics

The topics that the next_best_view node publishes are only meant for the
visualization. Those topics are:

-   **/nbv/frustum_marker_array**
-   message type: visualization_msgs/MarkerArray
-   description: publishes the frustum visualization
-   **/nbv/object_normals**
-   message type: visualization_msgs/MarkerArray
-   description: publishes the object normals
-   **/nbv/object_meshes**
-   message type: visualization_msgs/MarkerArray
-   description: publishes all hypotheses with textures
-   **/nbv/frustum_object_meshes**
-   message type: visualization_msgs/MarkerArray
-   description: publishes all hypotheses in the frustum
-   **/nbv/iteration_visualization**
-   message type: visualization_msgs::!MarkerArray
-   description: publishes the visual data of each iteration step when
    the !NextBestView is calculated
-   **/nbv/crop_box**
-   message type: visualization_msgs/MarkerArray
-   description: publishes all visual boxes which are used to crop
    hypotheses
-   **/nbv/voxelGridVisualization**
-   message type: visualization_msgs/MarkerArray
-   description: publishes voxels, which are used to consider visual
    obstacles
-   **/nbv/raytracingVisualization**
-   message type: visualization_msgs/MarkerArray
-   description: publishes rays, which are used to determine visual
    collision between camera origin and hypotheses

## Parameters

-   !NextBestView calculation
-   **maxIterationSteps**: the maximal amount of iteration steps that
    should be used for the calculation of the!NextBestView
-   **epsilon**: if the rating difference between two iteration steps is
    lower than epsilon, the !NextBestView iteration process finishes.
    Lower values result in more precisely calculated !NextBewstViews but
    require more calculation time.
-   **nRatingThreads**: number of rating threads used to rate views. -1
    gets an optimal a number of threads
-   **useMinUtility**: if true, views are filtered by a minimum required
    utility. All generated views that are below are removed
-   **enableCropBoxFiltering**: whether crop box filtering should be
    used, so that all points of the point_cloud which are at the outside
    will be removed. The cropboxes will be read from the
    rsc/CropBoxList\*.xml file (the path is configured in the launch
    file). The XML file will be created with the
    !RegionsToCropBoxAndNormals.py script, which converts the
    regions\_\*.csv to the XML file. In the csv file it is possible to
    configure normals for the cropboxes. If the normals are defined, the
    points in the point_cloud will get these normals and their own will
    be ignored. If no normals are defined, the original normals of the
    objects will be used.
-   Rating
-   **ratingModuleId**: which rating module should be used
-   1 =\> !DefaultRatingModule
-   **useTargetRobotState**: whether it should be checked if the
    calculated target robot state is reachable
-   Weights of the components of the rating for a viewport:
-   **mOmegaUtility**: weight of the utility
-   **mOmegaPan**: weight of the movement costs of the pan-axis for the
    PTU
-   **mOmegaTilt**: weight of the movement costs of the tilt-axis for
    the PTU
-   **mOmegaRot**: weight of the rotation costs of the robot base
-   **mOmegaBase**: weight of the translational movement costs of the
    robot base
-   **mOmegaRecognizer**: weight of the recognition costs
-   **speedFactorRecognizer**: time costs for object detection in
    sec/object
-   **mRatingNormalAngleThreshold**: same as
    mHypothesisUpdaterAngleThreshold, but this one is only for rating
-   **useOrientationUtility**: whether the orientation utility shall be
    used for the computation of the utility (only for testing purposes;
    should normally remain true)
-   **useProximityUtility**: whether the proximity utility shall be used
    for the computation of the utility (only for testing purposes;
    should normally remain true)
-   **useSideUtility**: whether the side utility shall be used for the
    computation of the utility (only for testing purposes; should
    normally remain true)
-   **enableIntermediateObjectWeighting**: whether intermediate object
    weighting should be used for calculating the !
-   NextBestView. The weights will be generated in the
    [intermediate_object_generator](http://wiki.ros.org/asr_intermediate_object_generator).
    The weights will be read from the
    [world_model](http://wiki.ros.org/asr_world_model)where the
    next_best_view node gets them.
-   Camera model filter
-   **cameraFilterId**: which camera filter should be used:
-   1 =\> Raytracing3DBasedStereoCameraModelFilter
-   2 =\> !StereoCameraModelFilter
-   3 =\> Raytracing3DBasedSingleCameraModelFilter
-   4 =\> !SingleCameraModelFilter
-   **fovx**: horizontal field of view in degree
-   **fovy**: vertical field of view in degree
-   **ncp**: distance of near clipping plane in meters
-   **fcp**: distance of far clipping plane in meters
-   If raytracing is used:
-   **voxelSize**: the length of an edge of a voxel
-   **worldHeight**: the height of the world in meters
-   **worldFilePath**: the path to the XML file describing the
    environment
-   **visualizeRaytracing**: whether the raytracing shall be visualized
-   Hypothesis updater
-   **hypothesisUpdaterId**: which hypothesis updater should be used:
-   1 =\> !PerspectiveHypothesisUpdater
-   2 =\> !DefaultHypothesisUpdater
-   **mHypothesisUpdaterAngleThreshold**: maximum angle threshold, used
    by the HypothesisUpdater to remove normals within that angle. The
    angle used for comparison is the angle between the camera
    orientation and the object normal.
-   Space sampler
-   **spaceSamplerId**: which sampler should be used:
-   1 =\> !MapBasedHexagonSpaceSampler
-   2 =\> !MapBasedRandomSpaceSampler
-   **radius**: the radius of the hexagons if using the
    !MapBasedHexagonSpaceSampler
-   **sampleSizeMapBasedRandomSpaceSampler**: the number of samples that
    should be generated if using the !MapBasedRandomSpaceSampler
-   Unit sphere sampler
-   **sphereSamplerId**:
-   1 =\> !SpiralApproxUnitSphereSampler
-   **sampleSizeUnitSphereSampler**: the amount of sampled points on the
    unit sphere
-   Map
-   **colThresh**: the collision threshold for the check whether a
    position is reachable
-   Output
-   **debugLevels**: a list of the debug levels that should be printed\
    possible values: ALL, NONE, PARAMETERS, SERVICE_CALLS,
    VISUALIZATION, CALCULATION, RATING, ROBOT_MODEL, MAP, WORLD,
    VOXEL_GRID, FILTER, IK_RATING, SPACE_SAMPLER, HYPOTHESIS_UPDATER
-   Visualization:
-   **show_point_cloud**: whether the point cloud should be visualized
-   **show_frustum_point_cloud**: whether the point cloud in the frustum
    should be visualized separately
-   **show_frustum_marker_array**: whether the frustum should be
    visualized
-   **show_normals**: whether object normals should be shown

Note that components from the asr_robot_model_services and costmap_2d
packages are used and they also need parameters. So, the launch files of
the asr_next_best_view package include parameter files from the
asr_robot_model_services package and there is a configuration file for
the costmap_2d package under param/costmap_params.yaml.

## Needed Services

-   move_base/make_plan
-   /asr_object_database/object_meta_data
-   /env/asr_world_model/get_recognizer_name
-   /env/asr_world_model/get_intermediate_object_weight

## Provided Services

-   **!GetAttributedPointCloud** (/nbv/get_point_cloud) :
-   returns all hypotheses that have at least minNumberNormals remaining
    normals
-   input:
-   minNumberNormals: minimum number of normals that an object needs
-   output:
-   point_cloud: the point cloud with all the hypotheses
-   **!GetNextBestView** (/nbv/next_best_view) :
-   input:
-   current_pose: current robot pose
-   output:\
-   found: whether a !NextBestView was found
-   object_name_list: list of object type names to be searched for
-   resulting_pose: the camera pose that was chosen
-   robot_state: the robot state corresponding to the resulting pose
-   other rating stats of the !NextBestView:
-   utility: better if there are more hypothesis in the frustum are
    closer to the center and looking more towards the camera lens
-   utility_normalization: best utility of all generated viewports
-   inverse_costs: higher is better, this is a mixture of the following
    stats
-   base_translation_inverse_costs: costs of robot base
    translation/movement
-   base_rotation_inverse_costs: costs of robot base rotation
-   ptu_movement_inverse_costs: costs of ptu movement
-   recognition_inverse_costs: costs to recognize objects in
    object_type_name_list
-   **!ResetCalculator** (/nbv/reset_nbv_calculator) :
-   output:
-   succeeded: whether the calculator was reseted
-   **!SetAttributedPointCloud** (/nbv/set_point_cloud) :
-   input:
-   point_cloud: point cloud to use for the !NextBestView estimation
-   viewports_to_filter: previously found/navigated !NextBestViews
-   output:
-   is_valid: whether the point cloud was set
-   normals_per_object: a list of remaining normals per object.
    !SetPointCloud updates all views that have been seen by the robot
    before. This process will remove normals
-   **!UpdatePointCloud** (/nbv/update_point_cloud) :
-   input:
-   pose_for_update: the current camera pose
-   object_type_name_list: object type list that the object detection
    used at the last !NextBestView
-   output:
-   deactivated_object_normals: number of normals that were removed by
    pose_for_update
-   **!SetInitRobotState** (/nbv/set_init_robot_state) :
-   input:
-   robotState: initial robot state, rotation angle in radian
-   **!RemoveObjects** (/nbv/remove_objects) :
-   removes all hypotheses of a given object that is specified by a type
    and an identifier
-   input:
-   type: object type of the object that should be removed
-   identifier: identifier of the object that should be removed
-   output:
-   is_valid: whether the point cloud is valid after this call. False if
    the point cloud is empty
-   **!RateViewports** (/nbv/rate_viewports) :
-   rates viewports using a current robot pose, a list of viewports to
    be rated and an optional list of object types that shall be used for
    object detection
-   input:
-   current_pose: current robot pose
-   viewports: viewports to be rated
-   object_type_name_list: object types which are searched for
-   use_object_type_to_rate: whether object_type_name_list should be
    used to rate
-   output:
-   sortedRatedViewports: a list containing all valid viewports that are
    sorted by their rating, oldIdx is the position in the given list of
    viewports to undo the sorting
-   **!TriggerFrustumVisualization**
    (/nbv/trigger_frustum_visualization) :
-   displays the frustum in a blue color
-   input:
-   current_pose: camera pose to be displayed in rviz
-   **!TriggerOldFrustumVisualization**
    (/nbv/trigger_old_frustum_visualization) :
-   displays the old frustum in a purple color
-   input:
-   current_pose: camera pose to be displayed in rviz
-   **!TriggerFrustumsAndPointCloudVisualization**
    (/nbv/trigger_frustums_and_point_cloud_visualization) :
-   displays a frustum and object hypotheses inside are marked.
-   input:
-   new_viewport: camera pose to be displayed in rviz

# Tutorials

[AsrNextBestViewSetPointCloud](http://wiki.ros.org/asr_next_best_view/AsrNextBestViewSetPointCloud)

[GetNextBestView](http://wiki.ros.org/asr_next_best_view/GetNextBestView)

[UpdatePointCloud](http://wiki.ros.org/asr_next_best_view/UpdatePointCloud)

When using this package, please cite the following publication. Thank
you!

-   P. Meißner, R. Schleicher, R. Hutmacher, S. R. Schmidt-Rohr and R.
    Dillmann. *Scene Recognition for Mobile Robots by Relational Object
    Search using Next-Best-View Estimates from Hierarchical Implicit
    Shape Models*. In International Conference on Intelligent Robots and
    Systems, 2016.
