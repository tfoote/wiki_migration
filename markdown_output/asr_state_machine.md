![\|height="200",width="333"](attachment:Logo-white-medium.jpg)

# Description

This package implements the logic which connects different
functionalities such as (passive) scene recognition, object pose
prediction and Next-Best-View estimation to Active Scene Recognition. In
particular, it is the interface for executing different 3D-object-search
procedures one of which Active Scene Recognition is. Active Scene
Recognition is equivalent to the "object search", which consists of
the "direct search" and "indirect search" modes. The search will be
executed by using different packages of the asr framework.

# Functionality

The state_machine controlls the flow of the 3D-object-search. There are
different approches (modes) implemented to realise the 3D-object-search.
The common goal is to search for objects in the search space and to
conclued which scenes they represent. The procedure is called the
*active_scene_recognition*. To conclude which scenes the found objects
represent a scene model is needed. Checkout
[AsrResourcesForActiveSceneRecognition](http://wiki.ros.org/asr_resources_for_active_scene_recognition)
to look up how scenes are recorded and trained.

During the 3D-object-search different run time information will be
generated and saved under the path "/log/" according to the start
time. The information are log-files, a rosbag file and some other. So it
is possible to reproduce and comprehend the executed searches.

There are two abort criteria for the 3D-object-search. One is if all
objects of all scenes are detected and found. The second depends on a
subset of the complete patterns (found scenes) and their confidence.
This can be useful if scenes overlap and only one has to be recognized
and the object sets do not fit. The subset can be specified over a
custom python script specified for a concrete scene set. An example:

1.  !/usr/bin/env python

from asr_world_model.msg import !CompletePattern

def evaluateCompletePatterns(completePatterns): for completePattern in
completePatterns: if ((completePattern.patternName = "Gedeck_Ende" or
completePattern.patternName = "Gedeck_Schrank_2" or
completePattern.patternName = "Spuelkorb_3" or
completePattern.patternName = "gedeck") and completePattern.confidence
>= 0.85): return True

return False

## Indirect Search

To start *active_scene_recognition* in indirect search mode, you have to
change the param/params.yaml. There are multiple configs which you can
change:

-   **mode**: For indirect search set it to 2
-   **UseFakeMoveBase**: In simulation, you can set it true -> The
    robot will not move anymore, instead, he will be set directly to the
    target location -> faster
-   **percentageTooManyDeactivatedNormals**: This can be useful if many
    similiar !PosePredictions of the asr_recognizer_prediction_ism were
    made. So that some of them will be skipped later on
-   **min_utility_for_moving**: The NBV could produce a pose which has a
    poor utility. It could be better to skip them for waiting for better
    !PosePredictions of the asr_recognizer_prediction_ism
-   **filter_viewports**: The NBV has a build in function not to take
    similiar views which were took earlier on. However, the criterio
    used there does not prevent always similar views. If enabled this
    function filters the produced pose of the NBV with a other criterio
-   **recoverLostHypothesis**: The hypothesis delted by
    **percentageTooManyDeactivatedNormals **or**
    min_utility_for_moving** could, combined with later used hypothesis,
    be useful. To prevent loosing them they can be stored and added
    later on to new !PosePredictions of the
    asr_recognizer_prediction_ism

The basic idea behind the indirect search is to use prior knowledge to
reduce the number of poses and time to search for objects. The prior
knowledge consists of scenes which represent objects and their relative
relations between each other. Starting from a found object hypothesis
will be generated (in the SCENE_RECOGNITION and OBJECT_POSE_PREDICTION)
were the other objects of the scenes could be located. The hypothesis
will be used to generate a NBV (in NBV_SET_POINT_CLOUD and
NBV_CALCULATION) to search for the missing objects. If no objects are
found the rest of the hypothesis will be used for generating new NBVs.
If one is found new predictions will be made for the missing objects and
the cylce starts again.

To start the indirect search an object has to be in front of the robot
so that it is possible to predict poses of the missing objects. Because
of that the search starts in INDIRECT_SEARCH_INIT with an
OBJECT_DETECTION. To overcome this restriction the indirect search can
be combined with the direct search to the object search.

![\|height="400",width="680"](attachment:indirect_ebene0.png)

![\|height="400",width="400"](attachment:indirect_ebene11.png)

-   **INDIRECT_SEARCH_INIT**: Init search and get first found object(s)
    to predict poses
-   **VISUALIZE_WAYPOINT**: Generates a marker visualising the current
    view
-   **SCENE_RECOGNITION**: Uses the found object(s) to map them to the
    currently used scenes. For each scene in the database a confidence
    will be determined if the current set of found objects represents
    the scene
-   **OBJECT_POSE_PREDICTION**: The recognized scenes will be used to
    predict poses of the missing objects. Normally not all scenes will
    be used for predictions, because there can be a lot hypothesis,
    which would slow down the NBV massively. Instead the
    **OBJECT_POSE_PREDICTION **will be executed iteratively if the old
    hypothesis were not helpful to find new objects
-   **NBV_SET_POINT_CLOUD**: The hypothesis of the
    **OBJECT_POSE_PREDICTION** will be forwarded to the
    asr_next_best_view.
-   **NBV_CALCULATION**: Depending on the set *point cloud* a *next best
    view* will be determined.
-   **MOVE_ROBOT_TO_VIEW**: To reach the view the robot has to
    **MOVE_PTU** and **MOVE_BASE**. They will be executed concurrently.
    The !MoveBase can be real/simulated moving or the !FakeMoveBase
    which sets the robot to the given pose
-   **PTU_POSE_CORRECTION**: The navigation of the **MOVE_BASE** can
    produce errors in the accuracy of the taken pose. To compensate the
    error the PTU will be adjust for a better fitting of the *goal view*
-   **OBJECT_DETECTION**: After the view has be reached the robot
    searches for objects at the location. To save time not all objects
    will be searched, but rather a subset given by the
    **NBV_CALCULATION**. There can be different object_recognizer for
    different object_types. In simulation the recognition can be
    simulated with asr_fake_object_recognition
-   **NBV_UPDATE_POINT_CLOUD**: If no objects have been found the
    hypothesis leading to the view will be deleted and a new NBV will be
    calculated. There are different functions included to detect and
    handle erroneous behaviour of the search procedure

![\|height="800",width="500"](attachment:indirect_ebene12.png)

## Direct Search

To start *active_scene_recognition* in direct search mode, you have to
change the param/params.yaml. There are multiple configs which you can
change:

-   **mode**: For indirect search set it to 1
-   **!UseFakeMoveBase**: In simulation, you can set it true -> The
    robot will not move anymore, instead, he will be set directly to the
    target location -> faster
-   **!SearchAllobject**: Search for all objects or only intermediate
    objects specified in !**IntermediateObject _XXX.xml**
-   **!StopAtfirst**: Stop search after first object is found

The basic idea behind the direct search is to search for objects without
the use of prior knowledge. The views to take (GET_GOAL_CAMERA_POSE)
will be handled by the asr_direct_search_manager. There are different
approches to generate the views. All share the common goal to cover the
search space with the views. So that sooner or later the objects will be
found.

However, without the use of prior knowledge the 3D-object-search can
take a while if each view covers only a small amout of the search space.
To overcome this issue the direct search can use prior knowledge to
prioritise some views over some other. At the current time the knowlege
is based on the **object_poses_from_demonstrations_given**. As long as
views are left the OBJECT_LOCATIONS_BASED_SEARCH will be executed. After
that the SCENE_EXPLORATION starts which just takes the views in a given
order.

The use of the prior knowledge will be encapsulated by the
asr_direct_search_manager. For the state_machine the
OBJECT_LOCATIONS_BASED_SEARCH and SCENE_EXPLORATION works the same way.
So only the state_machine of the OBJECT_LOCATIONS_BASED_SEARCH will be
shown.

The CHECK_SEARCH_FINISHED wil be used to handle an early end of the
search, because of **StopAtfirst **or** **!**SearchAllobject **.

![\|height="400",width="500"](attachment:direct_ebene0.png)

![\|height="600",width="300"](attachment:direct_ebene-1-part.png)

## Object Search

To start *active_scene_recognition* in object search mode, you have to
change the param/params.yaml. There are multiple configs which you can
change:

-   **mode**: For direct and indirect search (combined) set it to 3
-   the others are the same as in the indirect and direct search

The basic idea behind the object search is to combine the indirect and
direct search. The main weak spot of the indirect search is that it
needs a found object to generated predictions for the other missing
objects. Because of that, the direct search will be executed beforehand
until an object has been found.

It is possible that the indirect search is not able to produce new
predictions of hypothesis for the missing objects, because the robot has
searched at each possible spot were hypothesis have been predicted. This
could happen if there are multiple scenes which do not share the same
objects. If this happens the direct search will be executed again.

The object search is designed in a way that the direct and indirect
search do search at similiar spots after the same objects.

![\|height="300",width="500"](attachment:object_ebene0-ueb.png)

## Random Search

To start *active_scene_recognition* in random search mode, you have to
change the param/params.yaml. There are multiple configs which you can
change:

-   **mode**: For random search set it to 4
-   **!UseFakeMoveBase**: In simulation, you can set it true -> The
    robot will not move anymore, instead, he will be set directly to the
    target location -> faster
-   **!AllowSameViewInRandomSearch**: If set to false the robot is not
    allowed to have a similar robot_state twice

The basic idea behind the random search is, that the robot will move to
a random position with a random orientation and tilt, in each iteration
step. A simplified iteration looks like

GENERATE_RANDOM_POSE -> MOVE_ROBOT -> OBJECT_DETECTION ->
SCENE_RECOGNITION (if an object was found) -> GENERATE_RANDOM_POSE ->
\...

![\|height="300",width="600"](attachment:random_ebene0.png)

In this mode, the asr_next_best_view will not be used. The key
difference to the others modes is GENERATE_RANDOM_POSE. It generates a
pose and validates if the pose is allowed.

The generated position of the robot will be limited by the size of the
room. The orientation is generated between 0° and 360°. The tilt of the
PTU config will be in its possible range and pan will be constant 0,
because pan is almost redundant to the orientation of the robot.

The validation starts by checking if the generated position is
approachable by the robot (uses the asr_robot_model_services).

If !**AllowSameViewInRandomSearch is false** it will be checked if the
generated pose is approximately equal to one of the earlier poses. Two
robot states are approx_equal if the difference of the position,
orientation and PTU config are under a specific threshold. The threshold
of the position is the radius of the robot's volume. For orientation,
it is the half of the frustum's width. And for the tilt the half of the
frustum's height.

In the progress of the random search, the generation will take longer
time, because there are more old robot_states to compare with and the
possibility that two states are approx_equal increases.

## Cropbox Search

To start *active_scene_recognition* in cropbox search mode, you have to
change the param/params.yaml. There are multiple configs which you can
change:

-   **mode**: For cropbox search set it to 5
-   **!UseFakeMoveBase**: In simulation, you can set it true -> The
    robot will not move anymore, instead, he will be set directly to the
    target location -> faster
-   **min_utility_for_moving**: This param should be set to 0 or a very
    low number. In this mode every view has a poor utility, because the
    placeholders are evenly distributed over the cropboxes
-   **!PlaceholderObjectTypeInCropboxSearch**: A custom type for the
    points in the *point cloud.* It can be anything: a type of the
    scene, a type in the asr_object_database or something own defined.
    The type is only for information purpose
-   **!PlaceholderIdentifierInCropboxSearch**: The corresponding
    identifier to the type. The identifier represents the color of the
    *point cloud point* (0 is standard)
-   **!RoomHeight**: The *point cloud points* will be generated between
    0 and the !RoomHeight

The basic idea behind the cropbox search is to define cropboxes where
the robot should search for objects. The cropboxes can be tables and
shelfs. If the searched objects are in the cropboxes, they should be
found sooner or later.

The state automat works similar to the one of the indirect_search. The
key difference is that the point_cloud will be set only once in the
beginning in CROPBOX_SEARCH_INIT. The CROPBOX_SEARCH is the same as the
RELATION_BASED_SEARCH of the indirect_search.

![\|height="300",width="500"](attachment:cropbox_ebene0-overview.png)

The mOmegaUtility and mOmegaBase, params of asr_next_best_view, can be
adjusted with dynamic reconfigure so that asr_next_best_view will take
views with more normals.

The generation of the *point cloud* takes place in two steps. At first,
the points will be generated in the area of the whole room. The step
between two points on the ground is the half of the frustums width and
in the height the half of the frustums height.

The second part takes place in the NBV::setPointCloud. The *point
cloud*, received from the state_automat, will be filtered to the
cropboxes. Additionally, normals will be added to the *point cloud
points*, which are defined per cropbox. The mesh of the points will be
spheres (also defined in the asr_next_best_view).

Before you can run the *active_scene_recognition* you have to define the
cropboxes. Each cropbox is defined by a min_x, min_y, min_z and max_x,
max_y, max_z. To get more flexibility you can define multiple normals
per cropbox. The normals will be added to all points which are in the
cropbox. The cropboxes can overlap.

![\|height="250",width="400"](attachment:cropbox_tisch-k.png)

## Cropbox Record

To start *active_scene_recognition* in cropbox record mode, you have to
change the param/params.yaml.

-   **mode**: For cropbox record set it to 6
-   the others are the same as by cropbox search

This mode works similar to cropbox search. The key difference is that in
this mode no object will be searched and scenes recognized. Instead the
Views of the asr_next_best_view will be recorded and saved in a XML
file. The path for the XML file will be configured in the launch file(s)
(param name= !**CropBoxRecordingPath**).

The recorded poses can be retraced later with the
asr_direct_search_manager (mode 2: *recording_manager*). This mode is
useful when a cropbox for the whole room will be used, because the
asr_next_best_view needs much time. Also the generated poses can be
filtered and sorted later on.

A tutorial can be found under !AsrDirectSearchManagerTutorialRecord.

## Grid init record search

To start *active_scene_recognition* in grid init record search mode, you
have to change the param/params.yaml.

-   **mode**: For grid init record search set it to 7

This mode works similar to direct search. The key difference is that in
this mode no object will be searched and scenes recognized. Instead the
Views of the asr_direct_search_manager will be recorded and saved in a
XML file. The path for the XML file will be configured in the launch
file(s) (param name= **initializedGridFilePath**).

The recorded poses can be retraced later with the
asr_direct_search_manager (mode 1: *grid_manager*). This mode is needed
to initialize the grid (with asr_direct_search_manager: mode 3
*grid_initialisation*). Before the initialisation the grid is saved as
an xml file containing the grid points (*robot poses*). However, we need
the corresponding *camera poses* to use the reorder function based on
prior knowledge. Instead of doing the manual transforming between the
*robot and camera poses*, we save the transforming from TF.

This mode is part of the tutorial !AsrDirectSearchManagerTutorialGrid.

# Usage

Create "log" directory under home -> /log/

## Needed packages

[asr_next_best_view](http://wiki.ros.org/asr_next_best_view)

[asr_direct_search_manager](http://wiki.ros.org/asr_direct_search_manager)

[asr_recognizer_prediction_ism](http://wiki.ros.org/asr_recognizer_prediction_ism)

[asr_world_model](http://wiki.ros.org/asr_world_model)

[asr_robot_model_services](http://wiki.ros.org/asr_robot_model_services)

[asr_flir_ptu_controller](http://wiki.ros.org/asr_flir_ptu_controller)

[asr_flir_ptu_driver](http://wiki.ros.org/asr_flir_ptu_driver)

[asr_msgs](http://wiki.ros.org/asr_msgs)

[asr_aruco_marker_recognition](http://wiki.ros.org/asr_aruco_marker_recognition)

[asr_descriptor_surface_based_recognition](http://wiki.ros.org/asr_descriptor_surface_based_recognition)

[asr_fake_object_recognition](http://wiki.ros.org/asr_fake_object_recognition)

[asr_visualization_server](http://wiki.ros.org/asr_visualization_server)

## Start system

The system can be started through the start-scripts in the package
[asr_resources_for_active_scene_recognition](http://wiki.ros.org/asr_resources_for_active_scene_recognition).

To start them manually most of the packages of the
*active_scene_recognition* have to be started before.

After the start the initialObjects can be entered. They can be used in
the indirect search so save time in the first search step. They will not
be used in the other modes.

### Simulation

In simulation the object_detection and moving of the robot will be
simulated.

**roslaunch asr_state_machine scene_exploration_sim.launch**

### Real

**roslaunch asr_state_machine scene_exploration.launch**

# ROS Nodes

## Subscribed Topics

-   **/stereo/objects** *(!AsrObject)*: Gets the recognized objects by
    the object recognizer
-   **/asr_flir_ptu_driver/state** *(!JointState)*: Gets the current PTU
    config
-   **/map** *(!OccupancyGrid)*: Gets the map

## Published Topics

-   **/initialpose** *(!PoseWithCovarianceStamped)*: Used for
    !FakeModeBase to set the robot at the goal position without moving
-   **/waypoints** *(Marker)*: Visualize the *camera poses* the robot
    took during the 3D-object-search

## Parameters

### Launch file

**asr_state_machine/launch/scene_exploration(_sim).launch**

!**IntermediateObject _XXX.xml:_** A file containing the
_intermediate_objects, which can be used in the **direct_search** mode.
If !**SearchAllobject==false** only the contained objects will be
searched and not all. The XXX will be replaced with the current database
name. So the name has not to be changed manually after a database change
!**CompletePatterns_XXX.py**: A optional file which can be used to have
a different abort criterion, beside **found_all_objects**. The abort
criterion is **found_all_required_scenes**. The python snippet should
contain a method which gets all !CompletePatterns and returns true or
false depending on the !CompletePatterns. The XXX works analog here,
too. For an example see chapter functionality

!**CropBoxRecordingPath**: The path to a file to store the recorded
poses by the **Cropbox Record** mode

**initializedGridFilePath**: The path to a file to store the recorded
poses by the **Grid init record search** mode

### yaml file

**asr_state_machine/param/params.yaml**

**mode**: The mode of the 3D-object-search. 1 for direct search only, 2
for indirect search only, 3 for object search, 4 for random search, 5
for cropbox search, 6 for cropbox record, 7 for grid init record search
!**UseFakeMoveBase**: Use !FakeMoveBase if robot should be set on target
pos, instead of moving to it. This can be useful in simulation to save
time and ignore errors in navigation !**SearchAllobject**: Only for
direct search -> search for all objects or only intermediate objects
specified in !**IntermediateObject _XXX.xml** !**StopAtfirst**: Only
for direct search -> stop search after first object is found

**enableSmachViewer**: If you want to use smach viewer you can set this
to true. However, it will cost a lot of CPU usage, despite if smach
viewer runs

**percentageTooManyDeactivatedNormals**: The percentage to determine
when too many normals are deactivated during SET_NBV_POINT_CLOUD. ->
Abort if numberOfDeletedNormals / numberOfActiveNormals <=
percentageTooManyDeactivatedNormals **min_utility_for_moving**: The
minimum utility value of a NBV estimate that is required to consider
moving to it. If utility (not rating!) is below, return *no_nbv_found*
**filter_viewports**: Filter viewports of NBV which are approx equale to
already visited viewports !**AllowSameViewInRandomSearch**: Only for
random search -> if false robot will not move to approx equale robot
states again

**Placeholder(**!**ObjectType **/**Identifier) **!**InCropboxSearch**:
Only for cropbox search/record -> the Type/Identifier of the *points*
in the *point cloud*. Only for information purpose !**RoomHeight**: Only
for cropbox search/record -> the height of the room. Will be used for
generating the *point cloud *!**SavePointClouds**: Used to save
pointclouds in the log folder so they can be debugged in nbv later

**recoverLostHypothesis**: If pointcloud hypothesis should be kept when
they are removed by **percentageTooManyDeactivatedNormals **or**
min_utility_for_moving**

## Needed Services

-   **object recogition** (asr_fake_object_recognition,
    asr_descriptor_surface_based_recognition,
    asr_aruco_marker_recognition)
-   recognizer_node_name/get_recognizer
-   recognizer_node_name/release_recognizer
-   recognizer_node_name/clear_all_recognizers
-   **asr_next_best_view**
-   nbv/trigger_frustum_visualization
-   nbv/trigger_old_frustum_visualization
-   nbv/trigger_frustums_and_point_cloud_visualization
-   nbv/set_init_robot_state
-   nbv/next_best_view
-   nbv/set_point_cloud
-   nbv/update_point_cloud
-   nbv/get_point_cloud
-   nbv/remove_objects
-   **asr_robot_model_services**
-   asr_robot_model_services/GetCameraPose
-   asr_robot_model_services/GetRobotPose
-   asr_robot_model_services/IsPositionAllowed
-   asr_robot_model_services/CalculateCameraPoseCorrection
-   **asr_world_model**
-   env/asr_world_model/push_found_object_list
-   env/asr_world_model/push_viewport
-   env/asr_world_model/empty_found_object_list
-   env/asr_world_model/empty_viewport_list
-   env/asr_world_model/empty_complete_patterns
-   env/asr_world_model/get_all_object_types
-   env/asr_world_model/get_missing_object_list
-   env/asr_world_model/get_found_object_list
-   env/asr_world_model/get_complete_patterns
-   env/asr_world_model/get_viewport_list
-   env/asr_world_model/get_recognizer_name
-   env/asr_world_model/get_viewport_list
-   env/asr_world_model/filter_viewport_depending_on_already_visited_viewports
-   **asr_recognizer_prediction_ism**
-   rp_ism_node/get_point_cloud
-   rp_ism_node/find_scenes
-   rp_ism_node/reset
-   **move_base**
-   move_base/clear_costmaps
-   **asr_visualization_server**
-   visualization/draw_all_models_mild
-   **asr_flir_ptu_driver**
-   asr_flir_ptu_driver/get_range

## Needed Actions

-   **move_base** *(!MoveBaseAction)*: Send move goals
-   **ptu_controller_actionlib** *(!PTUMovementAction)*: send PTU
    configs
-   **asr_direct_search_manager** *(directSearchAction)*: get views for
    direct search mode.

# Tutorials

Tutorial to start indirect search:
[AsrStateMachineIndirectSearchTutorial](http://wiki.ros.org/asr_state_machine/IndirectSearchTutorial)

Tutorial to start direct search:
[AsrStateMachineDirectSearchTutorial](http://wiki.ros.org/asr_state_machine/DirectSearchTutorial)

To start the object search do all steps like described in
!AsrStateMachineIndirectSearchTutorial and
!AsrStateMachineDirectSearchTutorial. After that the **mode** has to be
changed to 3 for* object search*

Tutorial to start random search:
[AsrStateMachineRandomSearchTutorial](http://wiki.ros.org/asr_state_machine/RandomSearchTutorial)

Tutorial to start cropbox search:
[AsrStateMachineCropboxSearchTutorial](http://wiki.ros.org/asr_state_machine/CropboxSearchTutorial)

Cropbox record is part of
[AsrDirectSearchManagerTutorialRecord](http://wiki.ros.org/asr_direct_search_manager/AsrDirectSearchManagerTutorialRecord)

Grid init record is part of
[AsrDirectSearchManagerTutorialGrid](http://wiki.ros.org/asr_direct_search_manager/AsrDirectSearchManagerTutorialGrid)
