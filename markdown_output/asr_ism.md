![\|height=\"200\",width=\"333\"](attachment:Logo-white-medium.jpg)

## Description

This package serves as the Passive-Scene-Recognition interface to the
functionality provided by the [asr_lib_ism](asr_lib_ism) library in the
ROS environment. The Active-Scene-Recognition interface to ISM trees is
located in
[asr_recognizer_prediction_ism](asr_recognizer_prediction_ism), instead.
The core functions of this package are the training and recognition of
scenes which consist of various objects using Implicit Shape Model (ISM)
trees. In addition to the implementation of the tools provided by
[asr_lib_ism](asr_lib_ism) there are several visualization (based on
[asr_ism_visualizations](asr_ism_visualizations)) and utility tools to
make the usage of the scene recognition system more convenient.

![\|height=\"380\",width=\"234\"](attachment:example_recognizer_viz.png)

## Functionality

As mentioned above the basic functionality of the scene recognition
system consists of two main parts: The training of a scene model and the
recognition of a trained model in a new scene afterwards.

There are two training approaches implemented, one simply being called
\'\'Trainer\'\', the other \'\'CombinatorialTrainer\'\'. They are
interchangeable but as they use different algorithms the trained models
result in a difference in recognition quality mostly in terms of speed
as the latter has a shorter computation time. The input of both trainers
is a recording of a scene consisting of multiple objects which is stored
in a sqlite database and can be created using the \"Recorder\" tool. The
\"Recognizer\" tool uses the trained models and tries to find the most
likely match given a set of objects.

In general the steps required are the recording of a scene, training a
model from this recording and then using the recognizer to get the most
likely scene match from a new object configuration. Below you can see a
list of all tools this package provides including the mentioned ones and
tutorials on how to use them. For more information about the
functionality see the [asr_lib_ism](asr_lib_ism) package.

### Wrapper Nodes

The nodes in this list wrap tools from [asr_lib_ism](asr_lib_ism) to
provide them in the ROS environment:

-   combinatorialTrainer
-   data_cleaner
-   data_merger
-   marker_rotator
-   pose_interpolator
-   recognizer
-   recorded_objects_transformer
-   recorder
-   rotation_invariant_objects_rotator
-   trainer

### Visualization Nodes

Although many nodes of this package publish some kind of visualization,
the purpose of these nodes is solely to visualize ism data in
[rviz](rviz).

\'\'\'recordViewer\'\'\': Visualize recorded data of a given pattern as
a path for each object on which these objects moved while recording.

\'\'\'modelViewer\'\'\': Expand the \'\'recordViewer\'\' visualization
with vectors from positions of an object on its path at a certain point
in time to its reference path at the same point in time. This
visualization can help the user to understand how the model was created
from each record data point.

\'\'\'voteViewer\'\'\': Provide two different vote visualizations, the
first just visualizes all votes from a fixed pose for a selected object
in a selected subpattern and the second visualizes a given configuration
with each object\'s votes that the model of a selected pattern provides.

### Additional Nodes/Classes

\'\'\'!ObjectConverter (class)\'\'\': This class can be used for custom
nodes to convert ros messages (\'\'asr_msgs::!AsrObject\'\') to
data-types used by the [asr_lib_ism](asr_lib_ism) library. This class is
implemented in the \'\'ism_helper.hpp/.cpp\'\' file.

\'\'\'scene_configurator (class)\'\'\': This class expands a node with
the functionality to configure an object configuration interactively.
Main features of this class are the multi-threaded processing of
incoming messages (number of threads set by the user) and the processing
of keyboard input (polling on its own dedicated thread). With this
approach the actual node runs on its own thread(s) and decouples the
\'\'!SceneConfigurator\'\' logically and computationally from the node.

\'\'\'fake_data_publisher (node)\'\'\': This node republishes recorded
data from a given database as ros messages
(\'\'asr_msgs::!AsrObject\'\').

\'\'\'object_configuration_generator (node)\'\'\': This node generates
an object configuration by editing object data from a given database or
XML-file and writes it to an XML-file.

## Usage

Because this package is a collection of nodes and helper classes to
enable the user to write his own nodes, it is recommended to use the
tutorials on how to use the particular tool, however in most cases the
description of the nodes and their parameters should be sufficient.

### Needed packages

-   [asr_msgs](asr_msgs)
-   [asr_lib_ism](asr_lib_ism)
-   [asr_ism_visualizations](asr_ism_visualizations)
-   [asr_lib_pose_prediction_ism](asr_lib_pose_prediction_ism)
-   [asr_object_database](asr_object_database)
-   [asr_rapidxml](asr_rapidxml)

## ROS Nodes

### Subscribed Topics

-   \'\'\'asr_msgs/AsrObject\'\'\': This topic is the source for new
    object estimations, e.g. from an object detector like
    [asr_descriptor_surface_based_recognition](asr_descriptor_surface_based_recognition).
    (see \'\'objectTopic\'\' parameter for topic name)

### Published Topics

-   \'\'\'visualization_msgs/MarkerArray\'\'\': This topic is used to
    visualize all kinds of data in [rviz](rviz). (see
    \'\'visualization_topic\'\' or
    \'\'input_objects_visualization_topic\'\' parameters for topic name)
-   \'\'\'asr_msgs/AsrObject\'\'\': This topic is used by the
    \'\'fake_data_publisher\'\' to republish object data from a given
    database as new object estimations. (see objectTopic parameter for
    topic name)

### Parameters

#### Launch files

\'\'\'launch/combinatorialTrainer.launch:\'\'\'

-   \'\'outputDataPath (string)\'\': The path to a directory. Data such
    as the visualization of the ISMs created during the training process
    are stored here. (default: \"\")
-   \'\'swapRelations (bool)\'\': This parameter influences the
    neighbourhood of a topology T. If \'\'swapRelations\'\' == true,
    then topologies that can be created by swapping one relation that is
    part of that topology T with one that is not are considered
    neighbours of T. This parameter only effects
    !TopologyGeneratorPaper. (default: true)
-   \'\'removeRelations (bool)\'\': This parameter influences the
    neighbourhood of a topology T. If \'\'removeRelations\'\' == true,
    then topologies that can be created by removing one relation from
    topology T are considered neighbours of T. This parameter only
    effects !TopologyGeneratorPaper. (default: true)
-   \'\'loadValidTestSetsFrom (string)\'\': The path to the sql database
    that contains valid testsets. If \'\'loadValidTestSetsFrom\'\' ==
    \"\" new valid testsets are generated. (default: \"\")
-   \'\'loadInvalidTestSetsFrom (string)\'\': The path to the sql
    database that contains invalid testsets. If
    \'\'loadInvalidTestSetsFrom\'\' == \"\" new invalid testsets are
    generated. (default: \"\")
-   \'\'loadStartTopologiesFrom (string)\'\': The path(s) to the file(s)
    that contain the topologies from which to optimization process is
    started. Paths must be separated by a semicolon. If
    \'\'loadStartTopologiesFrom\'\' is not specified for a pattern, new
    start topologies are generated. (default: \"\")
-   \'\'startFromRandomTopology (bool)\'\': If no start topology was
    provided, the optimization will be started from a random topology.
    If \'\'startFromRandomTopology\'\' == true, else the best star
    topology will be selected and the optimization will start from that
    topology. (default: true)
-   \'\'storeValidTestSetsTo (string)\'\': The path to where the valid
    testsets will be stored. If left empty, the testsets are not stored.
    (default: \"\")
-   \'\'storeInvalidTestSets (string)\'\': The path to where the invalid
    testsets will be stored. If left empty, the testsets are not stored.
    (default: \"\")
-   \'\'storeFullyMeshedISM (bool)\'\': Whether to write the ism of the
    fully meshed topology to a sql database or not. (default: false)
-   \'\'storeStartTopologyISM (bool)\'\': Whether to write the ism of
    the selected start topology to a sql database or not. (default:
    true)
-   \'\'testSetCount (uint)\'\': The amount of valid and invalid test
    sets that are generated. (default: 600)
-   \'\'confidenceThreshold (double)\'\': Threshold for how big the
    confidence for a recognition result must be to be accepted.
    (default: 0.99)
-   \'\'evaluatorId (uint)\'\': Which evaluator is used. (default: 0)
    (\'\'evaluatorId\'\' == 0 =\> Tester)
-   \'\'testForFalseNegatives (bool)\'\': Whether the test for false
    negatives should be run or not. False negatives have no influence on
    the rating of topologies. (default: false)
-   \'\'costFunctionId (uint)\'\': Which cost function is used.
    (default: 0) (\'\'costFunctionId\'\' == 0 =\> !WeightedSum)
-   \'\'alpha (double)\'\': The weight for the normalised false
    positives. (default: 5)
-   \'\'beta (double)\'\': The weight for the normalised average
    recognition runtime. (default: 1)
-   \'\'topologyGeneratorId (uint)\'\': Which topologyGenerator is used
    (default: 0) (0 =\> !TopologyGeneratorPaper; 1 =\>
    !TopologyGeneratorNaive)
-   \'\'treeValidatorId (uint)\'\': Which treeValidator is used.
    (default: 0) (\'\'treeValidatorId\'\' == 0 =\> !HeightChecker)
-   \'\'optimizationAlgorithmId (uint)\'\': Which optimization algorithm
    is used. (default: 2) (0 =\> HillClimbing; 1 =\>
    !SimulatedAnnealing; 2 =\> !RecordHunt)
-   \'\'hillClimbingStrictMonoton (bool)\'\': Whether hillclimbing
    continues if a new evaluation result is exactly equal to the best
    evaluation result (\'\'hillClimbingStrictMonoton\'\' = false) or
    whether a true improvement is requiered and the optimization stops
    if both are equal (\'\'hillClimbingStrictMonoton\'\' = true).
    (default: true)
-   \'\'maxTreeHeight (uint)\'\': The maximum tree height that is
    accepted by !HeightChecker. (default: 3)
-   \'\'maxNeighbourCount (int)\'\': The maximum number of neighbours
    that are visited during ONE optimization step. If
    \'\'maxNeighbourCount\'\' == -1, all neighbours will be visited.
    (default: 30)
-   \'\'randomRestartProbability (double)\'\': The probability of
    performing a random restart. Value must be between 0 and 1. Only
    used if Hill Climbing is used for the optimization. (default: 0.0)
-   \'\'randomWalkProbability (double)\'\': The probability of
    performing a walk. Value must be between 0 and 1. Only used if Hill
    Climbing is used for the optimization. (default: 0.0)
-   \'\'startTemperature (double)\'\': The starting temperature of
    simulated annealing. Only used if Simulated Annealing is used for
    the optimization. (default: 1)
-   \'\'endTemperature (double)\'\': The end temperature of simulated
    annealing, if temperature \< \'\'endTemperature\'\' simulated
    annealing stops. Only used if Simulated Annealing is used for the
    optimization. (default: 0.005)
-   \'\'temperatureFactor (double)\'\': Used to calculate the next
    temperature, temperature_t+1 = temperature_t \*
    \'\'temperatureFactor\'\'. Only used if Simulated Annealing is used
    for the optimization. (default: 0.85)
-   \'\'repetitionsBeforeUpdated (uint)\'\': How many topologies are
    visited in simulated annealing before the temperature is updated.
    Only used if Simulated Annealing is used for the optimization.
    (default: 8)
-   \'\'initialAcceptableCostDelta (double)\'\': Used to initialize
    currentAcceptableCostDelta in !RecordHunt. If new_cost is the cost
    we want to check and lowest_cost is the lowest cost we have
    encountered so far, then new_cost is accepted if: new_cost \<= (1 +
    currentAcceptableCostDelta) \* lowest_cost. Only used if Record Hunt
    is used for the optimzation. (default: 0.02)
-   \'\'costDeltaDecreaseFactor (double)\'\': Used to update the current
    costDifferenceDelta. Only used if Record Hunt is used for the
    optimzation. (default: 0.01)

\'\'\'launch/data_cleaner.launch:\'\'\'

-   \'\'databases \'\'(string\[\]): A list of databases from which the
    data should be cleaned/deleted. (default: empty-list)
-   \'\'clean_records\'\' (bool): Whether recordings should be deleted.
    (default: false).
-   \'\'clean_models \'\'(bool): Whether trained models should be
    deleted. (default: false).

\'\'\'launch/data_merger.launch:\'\'\'

-   \'\'target \'\'(string): Resulting merged database. (default: \"\")
-   \'\'sources \'\'(string\[\]): A list of databases which should be
    merged into target. (default: empty-list)
-   \'\'merge_records \'\'(bool): Whether recordings should be merged
    into target. (default: true)
-   \'\'merge_models\'\' (bool): Whether trained models should be merged
    into target. (default: true).

\'\'\'launch/fake_data_publisher.launch:\'\'\'

-   \'\'usedPattern\'\' (int): Used to pick a specific pattern from a
    database. \'\'\'(optional)\'\'\'
-   \'\'firstUsedSet \'\'(int): Determine the lower boundary for the
    used subset of recorded object datasets.\'\'\' (optional)\'\'\'
-   \'\'lastUsedSet \'\'(int): Determine the upper boundary for the used
    subset of recorded object datasets. \'\'\'(optional)\'\'\'

\'\'\'launch/marker_rotator.launch:\'\'\'

-   \'\'source \'\'(string): Source database. (default: \"\")
-   \'\'target \'\'(string): Resulting database. (default: \"\")

\'\'\'launch/modelViewer.launch:\'\'\'

-   \'\'sceneName\'\' (string): Name of the scene which should be
    visualized. (default: \"\")

\'\'\'launch/object_configuration_generator.launch:\'\'\'

-   \'\'object_configuration_pattern_names \'\'(string\[\]): List of
    selected patterns from database. (default: empty-list)
    \'\'\'(optional)\'\'\'
-   \'\'output_file_path \'\'(string): Output path for the resulting
    XML-file. (default: \"\")
-   \'\'config_file_path \'\'(string): Path to a previously created
    configuration XML-file. If this parameter is defined the data from
    the given database will be ignored. (default: \"\")
    \'\'\'(optional)\'\'\'

\'\'\'launch/pose_interpolator.launch:\'\'\'

-   \'\'source \'\'(string): Source database. (default: \"\")
-   \'\'target \'\'(string): Resulting interpolated database. (default:
    \"\")
-   \'\'step_number \'\'(int): Number of interpolated poses between two
    object poses (default: \"\")

\'\'\'launch/recognizer.launch:\'\'\'

-   \'\'ignoreIds\'\' (bool): Object id information in recognition
    result is ignored. (defaut: false)
-   \'\'ignoreTypes\'\' (bool): Object type information in recognition
    result is ignored. (default: false)
-   \'\'maxNumberOfResultsPerPattern \'\'(int): The maximum number of
    results per pattern which you want to receive from the recognizer.
    (default: 1)
-   \'\'raterType\'\' (int): Which rater to rate/score an recognition
    result should be used. (default: 0) (0 = !SimpleRater: conisders
    only if certain conditions are met and rate it with 1 if conditions
    are met else with 0.; 1 = APORater: consider appearance, position
    and orientation for the rating. The score/rate is in \[0,1\].)
-   \'\'enableStoringConfigToXml\'\' (bool): Whether to store input
    object configurations as xml files on disk or not. Disabled if
    !SceneConfigurator is Auto Processing. (default: false)
-   \'\'configurationFolderPath\'\' (string): Path to the folder where
    the configuration xml files should be stored. If left empty, no
    configuration files are created. (default: \"\")

\'\'\'launch/recorded_objects_transformer.launch:\'\'\'

-   \'\'source\'\' (string): Source database. (default: \"\")
-   \'\'target \'\'(string): Resulting transformed database. (default:
    \"\")
-   \'\'object_type \'\'(string): Type of a reference object. (default:
    \"\")
-   \'\'object_id\'\' (string): Id of a reference object. (default:
    \"\")
-   \'\'position \'\'(double\[\]): Define a reference position.
    (default: empty-list)
-   \'\'orientation\'\' (double\[\]): Define a reference orientation.
    (default: empty-list)

\'\'\'launch/recorder.launch:\'\'\'

-   \'\'sceneName\'\' (string): Name of the scene to which demonstration
    being recorded belongs. (default: test)

\'\'\'launch/recordViewer.launch: \'\'\'

-   \'\'sceneName \'\'(string): Name of the scene which should be
    visualized. (default: \"\")

\'\'\'launch/rotation_invariant_objects_rotator.launch:\'\'\'

-   \'\'source \'\'(string): Source database. (default: \"\")
-   \'\'target \'\'(string): Resulting transformed database. (default:
    \"\")
-   \'\'object_type\'\' (string): Type of a reference object. (default:
    \"\")
-   \'\'object_id\'\' (string): Id of a reference object. (default:
    \"\")
-   \'\'rotation_invariant_types \'\'(string\[\]): List of rotation
    invariant object-types, which should be normalized. (default:
    empty-list)

\'\'\'launch/trainer.launch:\'\'\'

-   \'\'useClustering\'\' (bool): Whether normal ISMs (=false) or
    hierarchical ISMs (=true) should be learned. (default: true)
-   \'\'dropOldModelTables\'\' (bool): Whether exiting model data should
    be dropped or kept. (default: true)
-   \'\'useUserDefCluster\'\' (bool): Whether user defined cluster from
    clusterListFile should be used. (default: false)
-   \'\'clusterListFile\'\' (string): Path to a file with user defined
    cluster. (default: \"\")
-   \'\'preDefRefListFile\'\' (string): Path to a file with predefined
    references for (sub-)patterns. (default: \"\")
-   \'\'staticBreakRatio\'\' (double): Threshold for directional
    heuristic. (default: 0.01)
-   \'\'togetherRatio\'\' (double): Threshold for directional heuristic.
    (default: 0.90)
-   \'\'maxAngleDeviation \'\'(double): Threshold for directional
    heuristic. (default: 45)

\'\'\'launch/voteViewer.launch: \'\'\'

-   \'\'sceneName\'\' (string): Name of the scene which should be
    visualized. (default: \"\")
-   \'\'config_file_path \'\'(string): The path to a previously created
    configuration XML-file. (default: \"\") \'\'\'(optional) \'\'\'

#### YAML files

\'\'\'param/capturing.yaml:\'\'\'

-   \'\'objectTopic \'\'(string): The topic a !SceneConfigurator node is
    listening to for new object estimations. (default: /stereo/objects)
-   \'\'capture_interval \'\'(double): The interval in which a object
    configuration is processed when an !SceneConfigurator node is set to
    "Auto Processing". (default: 3)
-   \'\'queueSizePbdObjectCallback\'\' (int): The queue size for the
    objectTopic-Subscriber to buffer messages if the processing of new
    messages is slower as the time for new estimations to arrive.
    (default: 100)\'\'\'\' \'\'\'
-   \'\'object_input_thread_count \'\'(int): The amount of threads used
    to process incoming object estimation messages. (default: 4)
-   \'\'use_confidence_from_msg \'\'(bool): Whether to use the
    confidence from the object messages or just assume perfect object
    recognition and use confidence 1.0 for every recognized object.
    (default: false)
-   \'\'enableRotationMode\'\' (int): Whether the object orientation
    should be rotated to the baseFrame or to an object. This only
    affects rotation invariant objects. (0: don\'t rotate; 1: rotate to
    rotationFrame; 2: rotate to rotationObject) (default: 1)
-   \'\'rotationFrame\'\' (string): Defines the frame to which the
    objects should be rotated. The rotation only takes place if
    baseFrame == rotationFrame and enableRotationMode = 1 . This only
    affects rotation invariant objects. (default: /map)
-   \'\'rotationObjectType\'\' (string): Defines the object type to
    which the objects should be rotated. The rotation only takes place
    if enableRotationMode = 2. This only affects rotation invariant
    objects.(default: \"\")\'\' \'\'\'\'\' \'\'\'
-   \'\'rotationObjectId\'\' (string): Defines the object id to which
    the objects should be rotated. The rotation only takes place if
    enableRotationMode = 2. This only affects rotation invariant
    objects. (default: \"\")
-   \'\'keyboard_poll_rate \'\'(int): The rate (Hz) in which the
    keyboard-thread polls the keyboard for user input. (default: 10)
-   \'\'input_objects_visualization_topic\'\' (string): The topic on
    which the visualization of a !SceneConfigurator node is published.
    (default: /input_objects_scene_configurator_viz)
-   \'\'enableNeighborhoodEvaluation\'\' (bool): Whether to use
    neighborhood evaluation or not. (default: false)
-   \'\'angleNeighbourThreshold \'\'(double): Maximal angle deviation
    accepted between two estimations of the same object. Only used if
    neighborhood evaluation is enabled. (default: 30)
-   \'\'distanceNeighbourThreshold \'\'(double): Maximal distance
    accepted between two estimations of the same object. Only used if
    neighborhood evaluation** is enabled. (default: 0.05)**

\'\'\'param/sensitivity.yaml: \'\'\'

-   \'\'bin_size\'\' (double): Side length of cubes (bins) making up a
    voxel grid in which hough voting is performed. Maximal accepted
    distance between scene reference hypotheses of different objects in
    a bin. (default: 0.1)
-   \'\'maxProjectionAngleDeviation\'\' (double): Maximal accepted
    difference in orientations of scene reference hypotheses of
    different objects in a bin. (default: 30)

\'\'\'param/sqlitedb.yaml: \'\'\'

-   \'\'dbfilename\'\' (string): The path to the database which should
    be used in the system. The recorder node will create this database
    if no such database exists. (default: \"\")
-   \'\'baseFrame\'\' (string): Frame to which incoming object messages
    are transformed. Used to unify their coordinate frames. (default:
    /map)

\'\'\'param/visualization.yaml: \'\'\'

-   \'\'visualization_topic\'\' (string): The name of the topic where
    the visualization markers are published to. (default:
    /ism_results_visualization)

### Needed services

\'\'\'/asr_object_database/object_meta_data\'\'\': This service is only
called by the !ObjectConverter class and provides it with additional
information about recognizable objects from the
[asr_object_database](asr_object_database).

## Tutorials

[How to use a SceneConfigurator-Node](asr_ism/tutorial_scene_configurator)

[How to use the recorder](asr_ism/tutorial_recorder)

[Training an ISM](asr_ism/tutorial_trainer)

[Training an ISM using the Combinatorial-Trainer](asr_ism/tutorial_combinatorial_trainer)

[How to use the recognizer](asr_ism/tutorial_recognizer)

[How to use the visualization nodes](asr_ism/tutorial_visualization_nodes)

[How to use the fake_data_publisher](asr_ism/tutorial_fake_data_publisher)

[How to use the object_configuration_generator](asr_ism/tutorial_object_configuration_generator)

## Troubleshooting

\'\'\'Problem:\'\'\' Missing object estimations when using a
!SceneConfigurator -Node and the [asr_flir_ptu](asr_flir_ptu)\_driver
GUI.

If you are using the \'\'ptu_gui.launch\'\' from
[asr_flir_ptu_driver](asr_flir_ptu_driver) and you checked the option
"update current angle immediately", it may happen that the
!SceneConfigurator clears the object estimations in the current view,
because the ptu toggles its "reached_desired_position" parameter.

\'\'\'Solution:\'\'\' Make sure to uncheck the "update current angle
immediately" option if you want to work with the current view.

When using ISMs, please cite the following publication. Thank you!

-   P. Meißner, R. Reckling, R. Jäkel, S. R. Schmidt-Rohr and R.
    Dillmann. \'\'Recognizing scenes with hierarchical implicit shape
    models based on spatial object relations for programming by
    demonstration\'\'. In International Conference on Advanced Robotics,
    2013.

When using Combinatorial Trainer, please cite the following publication.
Thank you!

-   P. Meißner, F. Hanselmann, R. Jäkel, S. R. Schmidt-Rohr and R.
    Dillmann. \'\'Automated selection of spatial object relations for
    modeling and recognizing indoor scenes with hierarchical implicit
    shape models\'\'. In International Conference on Intelligent Robots
    and Systems, 2015.
