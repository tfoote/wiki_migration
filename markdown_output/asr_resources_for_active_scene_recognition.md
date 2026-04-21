![\|height="200",width="333"](attachment:Logo-white-medium.jpg)

# Description

This package contains various helpers and resources for our Active Scene
Recognition - System. The package includes the following submodules:

-   **constellation_transformation_tool **- python script, that allows
    the simultaneous transformation of multiple object poses by a fixed
    rotation and translation.
-   **launch **- contains several launch files to start the
    scene-recognition state machines and all its depending packages
    using tmux.
-   **recognition_manual_manager **- python script, that allows to start
    and stop object detectors manually.
-   **rviz_configurations **- contains predefined rviz-configurations
    that include all available visualization topics for the default
    Active Scene Recognition scenario. Shows object normals by default,
    turn this of if it degrades your rviz performance.
-   **scene_recordings **- resource folder that contains all recorded
    scenes as a database file.
-   **control** - python script to control some parts of the state
    machine, including moving the ptu/robot, detecting objects, finding
    nbvs.

Launch files:

-   **start_modules_sim.sh/sim.launch** - starts all required modules to
    do scene recognition in simulation.
-   **start_modules_real.sh/real.launch** - starts all required modules
    to do scene recognition in simulation, excluding object recognizers.
-   **start_recognizers.sh** - must be run with real.launch on gui/robot
    to start object recognizers.
-   **start_modules_scene_learning.sh** - starts modules for scene
    recording.
-   **control.sh** - starts control script without any dependencies.
-   **start_modules_with_kinect.sh** - starts the real robot platform
    without the Active Scene Recognition. Also starts all components
    required to use the kinect sensor. *Note, that you still need to
    launch the base_modules manually.*
-   **rviz_scene_exploration.launch** starts rviz preconfigured to show
    relevant visualizations.

# Functionality

This package contains bash scripts to start multiple other modules in a
tmux session. It also contains scenes as sqlite databases and a rviz
configuration file. For easier handling with other modules it contains
some python scripts.

# Usage

This module has two main functionalities:

1\. run the scene recognition in simulation/real. 1. record scenes.

This module also contains a rviz configuration file that includes all
required visualization topics for the Active Scene Recognition (formerly
designated as scene-exploration) and related applications. It is in the
rviz_configurations folder and named scene_exploration.rviz. The
scene_recordings folder contains some recorded scenes as sqlite database
files, which can be configured in sqlitedb.yaml in the
[asr_recognizer_prediction](http://wiki.ros.org/asr_recognizer_prediction%20)and
[asr_ism](http://wiki.ros.org/asr_ism%20) package. Depending on the
shell script you are running you will see different tmux windows, their
usage/module is described here. If you are wondering how the tmux
windows should look like after a successful lauch, take a look at the
images.

-   **roscore** - roscore in the upper panel, gazebo in the lower panel.

![\|height="200",width="333"](attachment:roscore.png)

-   **control** - a python script that can be used to interact with some
    modules.
-   **rviz** - rviz visualization.

![\|height="200",width="333"](attachment:roscore.png)

-   **ism** -
    [asr_recognizer_prediction_ism](http://wiki.ros.org/asr_recognizer_prediction_ism)
    module, which is used to detect scenes from known objects, the lower
    panel can be used to start recognizers/object detection to ensure
    objects can be detected from a certain position.

![\|height="200",width="333"](attachment:ism.png)

-   **nbv** - the upper panel is running the
    [asr_next_best_view](http://wiki.ros.org/asr_next_best_view) module
    which is used to determine the next navigation goal, the lower panel
    runs [asr_world_model](http://wiki.ros.org/asr_world_model) which
    holds information about the world, e.g. found objects, navigated
    views.

![\|height="200",width="333"](attachment:nbv.png)

-   **viz_server** - used to publish visualization stuff for rviz.

![\|height="200",width="333"](attachment:viz_server.png)

-   **state_machine** - core that uses all modules to detect scenes. It
    has some configurable modes which change the behavior/requirements
    for scene detection.

![\|height="200",width="333"](attachment:state_machine.png)

-   **direct_search_manager** - used for the direct search/relation
    based search.

![\|height="200",width="333"](attachment:direct_search_manager.png)

-   **move_mock** - responsible for movement in simulation.

![\|height="200",width="333"](attachment:move_mock.png)

-   **ptu_mock** - contains the ptu mock, which is used to rotate the
    camera in simulation. the lower right panels can be used to modify
    its state/show the camera frustum.

![\|height="200",width="333"](attachment:ptu_mock.png)

-   **fake_recognizer** - in simulation we have no real camera
    data/recogizers, so this is used to simulate recognition.

![\|height="200",width="333"](attachment:fake_recognizer.png)

-   **recognition_for_grasping**,
    **descriptor_surface_based_recognition**,
    **aruco_marker_recognition** - used to recognize different type of
    objects in reality.

![\|height="200",width="333"](attachment:recognition_for_grasping.png)
![\|height="200",width="333"](attachment:descriptor_surface.png)
![\|height="200",width="333"](attachment:aruko.png)

-   **object_database** -
    [asr_object_database](http://wiki.ros.org/asr_object_database)
    contains information about object recognizers/types and their model,
    so they can be displayed in rviz.
-   **recorder** - this window is used when recording new scenes, the
    upper panel is used to add detected objects to the list of recorded
    objects. The lower panel can be used to detect objects the same way
    as the ism window.
-   **vision** - guppy_head_full_mild

![\|height="200",width="333"](attachment:vision.png)

-   **kinect** - kinect driver.

![\|height="200",width="333"](attachment:kinect.png)

The control script (in the control tmux window) can be used to do almost
anything the state_machine is capable of, but in a more manual way. The
following list describes functions that can be used thorugh the repl
interface/in other python scripts:

-   setPTU(pan, tilt) - sets ptu to pan/tilt.
-   movePTU(pan, tilt) - moves ptu by pan/tilt from current pan/tile
    position. This can be used for find movement without remembering the
    current ptu position.
-   setBase(x, y, rotation) - rotation in degree, x/y describe the
    center position of the robot base. This can be used in simulation to
    instantly and precisely move the robot to a position, in real it can
    be used to to estimate the real pose.
-   moveBase(x, y, rotation) - moves the base to the given location
    using the navigation.
-   setPositionAndOrientation(((x, y, rotation), (pan, tilt))) - does
    the same as the functions above combined into one function, the
    parameter is a 2-tuple of a position 3-tuple and an orientation
    2-tuple.
-   startRecognition(recognizers, waitTime) - all parameters are
    optional, default waitTime is 2 sec, default recognizers are all.
    The result is a map which contains per object type the number of
    recognitions. This can be used to test views or to find a decent
    start psoition for the indirect search.
-   waitForAllModules() - waits for all modules to make sure everything
    is working.
-   startSM()/stopSM()/waitSMFinished()/isSMFinished() - these methods
    start/stop the state_machine or wait until it has finished/check if
    it is finished, restartSM() can be used to restart the
    state_machine.
-   getSMResult() - false if state_machine has not finished yet,
    otherwise the result as a string.
-   setConfig(cfg_\*) - can be used to swap fast between different
    scenes, the cfg_\* objects contain start positions, scene database
    files, world description files, fake object recognizer configs. This
    command will also restart the required tmux panels/modules after
    writing to the parameter files. CAUTION: This will override your
    current parameter files, so save them better before using this
    function.
-   getCurrentConfig() - retunrs the currently set config if is in the
    cfgs list and set with setConfig().
-   setDefaultPos() - uses getCurrentConfig() to get and set a
    default/start position.
-   getNBV() - calculates the nbv using the currently set pointcloud.
-   getPositionAndOrientationFromNBV(nbv) - returns a 2-tuple (pos,
    orientation) that can be given to
    setPositionAndOrientation(position, orientation).
-   getPoseFromNBV(nbv) - returns a pose from a nbv, the pose can be
    given to showPoses to display the nbv.
-   getCurrentCameraPose() - returns the current camera pose of the
    robot.
-   showPoses(poses)/showNBVs(nbvs) - displays views at
    "/nbv/viewportsVisualization" topic as MarkerArray.
-   rateViewport(pose) - rates a view, the rating result might differ
    from getNBV() since getNBV() uses a different utility normalization.
-   nbvUpdate(pose, obj_types) - does a update/removes normals from a
    frustum at pose. only remoes normals from hypotheses that match
    their type with one of obj_types.
-   nbvUpdateFromNBV(nbv) - does the same as nbvUpdate, but it takes the
    result of getNBV() as parameter.
-   getPC() - return the currently set pointcloud.
-   getPCAndViewportsFromLog(logFolder, idx) - returns a pointcloud (and
    viewports) from a scene recognition logfolder. The idx specifies the
    (idx+1).th pointcloud of the scene recognition. Can be used in
    combination with setPC to set a pointcloud.
-   setPC(pointcloud, viewports) - sets pointcloud using viewports as
    previously seen viewports.
-   setPCAndViewportsFromLog(logDir, idx) -
    setPC(\*(getPCAndViewportsFromLog(logFolder, idx))), sets a
    pointcloud from a log folder.
-   logDir - /log expanded.
-   latestLogFolder() - returns the location of the latest log folder as
    string.
-   logFolders/getLogFolders() - returns a list of logfolders in /log/,
    containing the absolute paths as string, these might nor be valid
    logfolders.
-   getLogSubFolders(folder) - searches recursively all subfolders of
    folder to find log folders, getLogSubFolders(logDir) returns all
    valid log folders and is similiar to getLogFolders().
-   isLogFolder(folder) - returns true if folder is a valid logfolder,
    that contains a state_machine.log which contains the result of the
    scene_recognition.
-   getStartPosition(folder) - returns the start position/orientation
    that was used in the scene recognition run. The returned value is a
    2-tuple (pos, orientation) and can be given to
    setPositionAndOrientation(position, orientation).
-   getConfig(folder) - creates a config object from a logfolder, that
    can be set with setConfig. This function can be used to replay old
    log folders. Keep in mind that the returned config does not contains
    all parameters, instead it returns a minimum to search for a
    different scene.
-   getNBVs(folder) - returns a list of navigated nbvs.

You can use tab complete if you don't know function names. The
personal_stuff.py is for personal python code.

## Needed packages

-   [asr_flir_ptu_controller](http://wiki.ros.org/asr_flir_ptu_controller)
-   ptu_driver
-   [asr_world_model](http://wiki.ros.org/asr_world_model)
-   [asr_next_best_view](http://wiki.ros.org/asr_next_best_view)
-   [asr_recognizer_prediction_ism](http://wiki.ros.org/asr_recognizer_prediction_ism)
-   [asr_resources_for_vision](http://wiki.ros.org/asr_resources_for_vision)
-   [asr_kinematic_chain_mild](http://wiki.ros.org/asr_kinematic_chain_mild)
-   [asr_visualization_server](http://wiki.ros.org/asr_visualization_server)
-   [asr_direct_search_manager](http://wiki.ros.org/asr_direct_search_manager)
-   [asr_mild_navigation](http://wiki.ros.org/asr_mild_navigation)
-   mild_base_launch_files
-   [asr_state_machine](http://wiki.ros.org/asr_state_machine)
-   [asr_descriptor_surface_based_recognition](http://wiki.ros.org/asr_descriptor_surface_based_recognition)
-   [asr_aruco_marker_recognition](http://wiki.ros.org/asr_aruco_marker_recognition)
-   [asr_fake_object_recognition](http://wiki.ros.org/asr_fake_object_recognition)
-   [recognition_for_grasping](http://wiki.ros.org/recognition_for_grasping)

there might be more needed packages which are depending on the ones
above.

## Needed software

[tmux](https://tmux.github.io/)

If you source the ROS environment inside your /.bashrc, **pay
attentation** that tmux reads only /.profile by default. Thus you might
need to source your ROS environment in /.profile too.

## recognition_manual_manager

Contains the **manager.py **script, that allows to manually start and
stop detection of single objects. In order for the script to work, all
required object recognizers need to be launched in advance (See above:
you can use the **start_recognizers** script to do so).

To find the object types of a recognizer you can run e.g. rosservice
call /asr_object_database/object_type_list "recognizer:
'segmentable'" to get all segmentable objects, for more information
see [asr_object_database](http://wiki.ros.org/asr_object_database).

The following commands are supported by the script:

-   **start,markers **- starts detection for all markers
-   **stop,markers **- stops detection for all markers
-   **start,<textured\|segmentable\|descriptor>,<object_name> **-
    starts detection for the given object using a certain recognizer
-   **stop,<textured\|segmentable\|descriptor>,<object_name> **-
    stops detection for the given object using a certain recognizer

## constellation_transformation_tool

Contains the transformation_tool.py script, which allows the
transformation of a list of multiple object poses by a predefined
rotation and translation. Furthermore, the original as well as the
transformed object pose are visualized and printed to the console in a
loop until interrupted. The topic must be added in rviz and it is named
"transformation_tool". You can visualize only the new/original pose
visualization by using the namespaces "transformation_orig" and
"transformation_new".

Note, that currently each object and its pose needs to be added directly
to the code in the main function. The translation and rotation values
also need to be set here before running the script.

In addition, a roscore needs to be up and running before you can launch
the script.

## Available object recognizers

There are currently two recognizers integrated into the system to detect
objects:

-   **aruco_marker_recognition:** Detects objects by atached markers.
    Further information: asr_aruco_marker_recognition.
-   **descriptor_surface_based_recognition**: Detects arbitrary shaped
    objects by their texture. Its usage is free, but it depends on
    Halcon (<http://www.mvtec.com/products/halcon/>, last runtime-tests
    with Halcon 11). Thus it's optional for ASR. Further information:
    asr_descriptor_surface_based_recognition.
-   Two proprietary recognizers (one shape-based (segmentable) for
    unicolored objects and one texture-based (textured) for textured
    objects) used to be supported. However, we suggest integrating
    state-of-the-art object-pose estimation through relying on the
    RecognitionManager structure, instead. Please reach out to us for
    more information.

# ROS Nodes

## Parameters

asr_next_best_view

-   param/next_best_view_settings_real/sim.yaml (used in the simulation)
    and rsc/next_best_view_settings_real/real.yaml (used on real
    robots)\
-   **radius** - to adapt the resolution of position sampling, lower ->
    higher resolution. The value gets adapted during the calculation.
-   **sampleSizeUnitSphereSampler** - to adapt the resolution of
    orientation sampling, higher -> higher resolution (but computation
    takes longer). If you set it too low, the robot might miss objects
    because the robot doesn't take its orientations into account.
-   **colThresh** - Minimum distance between the robot and objects.
    Increase the default if you want the robot to move closer to
    objects, but be aware that if you set it too low, the robot might
    collide with objects. For further information about the threshold,
    take a look at <http://wiki.ros.org/costmap_2d#Inflation>

asr_state_machine

-   param/params.yaml
-   **mode** - the mode specifies the method which is used to find
    scenes (see this file for possible values).
-   **UseFakeMoveBase** - can be set to true in simulation to "jump"
    to the target instead of using the navigation.
-   rsc/CompletePatterns\*.py - a optional file which can be used to
    have a different abort criterion, beside **found_all_objects**. The
    abort criterion is **found_all_required_scenes**. The python snippet
    should contain a method which gets all CompletePatterns and returns
    true or false depending on the CompletePatterns. For an example see
    [asr_state_machine](file:///C:/Users/Felix/Desktop/ROS/twiki%202/bin/view/IlcasProjects/AsrStateMachine.html).

asr_fake_object_recognition

-   param/params.yaml
-   **config_file_path** - path to a xml file that contains the location
    of objects. These objects can be detected in simulation.

asr_world_model

-   launch/\*.launch includes an optional parameter file which is
    located in rsc/world_descriptions. This world_description parameter
    file contains information about objects, that can be found in the
    world. It has a object type and id per object and a recognizer type,
    which is used to detect them. Usually those information can be
    retrieved from the sqlite database explained below, so the
    world_description file isn't necessary.

asr_recognizer_prediction_ism

-   param/scene_recognition.yaml.
-   **dbfilename** - Location of a sqlite database for scene
    recognition. It stores the recorded scene. If the database is
    incomplete or you want to search for a subset ob objects only, it's
    possible to overwrite/add information by using the world_description
    file, see
    \![AsrWorldModel#4_2_3_world_description_optional.](AsrWorldModel#A4_2_3_world_description_optional.)
-   param/sensitivity.yaml
-   **bin_size** - Deviation of the object position of the recognized
    objects against the recorded position (in meters). Depends on the
    "real" deviation of the objects, the inaccuracy of the object
    recognition and the inaccuracy of the robot position.
-   **maxProjectionAngleDeviation** - Deviation the object rotation of
    the recognized objects against the recorded position (in degree).
    Depends on the "real" deviation of the objects, the inaccuracy of
    the object recognition and the inaccuracy of the robot position.

asr_ism

-   param/sqlitedb.yaml
-   **dbfilename** - location of a sqlite database for scene recording

# Tutorials

-   [SimulateSceneRecognition](http://wiki.ros.org/asr_resources_for_active_scene_recognition/SimulateSceneRecognition) -
    do the scene recognition in a simulation
-   [SceneRecording](http://wiki.ros.org/asr_resources_for_active_scene_recognition/SceneRecording) -
    record a scene on a robot
-   [RealSceneRecognition](http://wiki.ros.org/asr_resources_for_active_scene_recognition/RealSceneRecognition) -
    do the scene recognition on a real robot
-   [setPCAndViewportsFromLog](http://wiki.ros.org/asr_resources_for_active_scene_recognition/SetPCAndViewportsFromLog) -
    set a pointcloud from an old log file.
-   [GetNBV](http://wiki.ros.org/asr_resources_for_active_scene_recognition/GetNBV) -
    calculate a nbv and move the robot.
-   [active scene recognition using the control script](http://wiki.ros.org/asr_resources_for_active_scene_recognition/UsingControl)

# Troubleshooting

If running ROS commands in a file (./script.sh) fails in a tmux pane,
run these commands in the current shell (source ./script.sh) instead.
