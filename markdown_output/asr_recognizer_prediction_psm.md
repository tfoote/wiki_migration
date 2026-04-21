![\|height="200",width="333"](attachment:Logo-white-medium.jpg)

# Description

This package provides object pose prediction on the basis of the
alternative scene model PSM (Probabilistic Scene Model): It generates
hypotheses (type and pose) for missing objects in the context of 3D
object search. Moreover, it integrates scene recognition and object pose
prediction (both on the basis of PSM) into Active Scene Recognition. Its
output are asr_next_best_view/AttributedPointCloud.msg messages which
can be processed by asr_next_best_view.

There are two launch files. The first launches the PSM pose prediction
(launch/psm_node.launch). The second starts the PSM pose prediction with
given likelihoods (launch/recognizer_prediction_psm.launch).

# Functionality

Builds a scene graph of each given scene and occupies nodes (objects)
with the given unobserved objects (evidences). Based on the absolute
positions of the observed objects the relative poses are calculated by
sampling the Gaussian Mixture Models of the child nodes. The number of
hypotheses is spread equally to each unobserved object. If there is more
than one observed object, the first object in the object list that is
part of the scene will be treated as reference objects. The reference
object is the root node of the scene graph.

Output: *asr_next_best_view/AttributedPointCloud pose_hypothesis* (see
topics) and *bool all_scene_objects_found*: true if all scene objects of
ALL scenes in the .xml have been found. The automat can then go to
success state, false otherwise.

# Usage

## Needed packages

-   [asr_psm](wiki.ros.org/asr_psm)
-   [asr_msgs](http://wiki.ros.org/asr_msgs)(for !AsrObject)
-   [AsrNextBestView](http://wiki.ros.org/asr_next_best_view) (for
    !AttributedPointCloud msg)
-   [AsrKinematicChain](http://wiki.ros.org/asr_kinematic_chain%20) (for
    the transformation to given frames)

## Needed software

-   [kinematic chain](file:///C:/Users/Felix/Desktop/ROS/twiki%202/bin/view/IlcasProjects/AsrKinematicChainDome.html)
-   [AsrObject](http://i61pc053.itec.uni-karlsruhe.de/twiki/bin/edit/IlcasProjects/AsrObject?topicparent=IlcasProjects.AsrRecognizerPredictionPSM;nowysiwyg=0)
    msgs (so you need
    [asr_flir_ptu_driver](http://wiki.ros.org/asr_flir_ptu_driver),
    [asr_resources_for_vision](http://wiki.ros.org/asr_resources_for_vision%20)
    and a recognizer, e.g.
    [asr_aruco_marker_recognition](http://wiki.ros.org/asr_aruco_marker_recognition))
-   for scene probabilities you need AsrPSM inference.
-   Eigen
-   Boost

## Start system

**with inference:**

start *roscore *and the kinematic chain:

*roslaunch asr_kinematic_chain_dome
transformation_publishers_for_kinect_left.launch*

start the server: *roslaunch asr_recognizer_prediction_psm
psm_node.launch*

**without inference:**

start *roscore *and the kinematic chain (see above).

start the server: *roslaunch asr_recognizer_prediction_psm
recognizer_prediction_psm.launch*

Visualization: Start *RViz *(*rviz*) and open the config file
*doc/recognizer_prediction_psm. rviz*

### Simulation

Only differs from real application in source of observed object
messages.

# ROS Nodes

## Published Topics

-   /stereo/visualization_marker_array
-   /asr_next_best_view::!AttributedPointCloud (see services)

## Parameters

**with inference: **(*psm_node.launch)*

-   *string path* - path to the xml file that contains the scenes (e.g.
    *models/breakfast.xml*)
-   *string\[\] bag_filename_list*: the object trajectories. These are
    generated during
    [AsrPSM](file:///C:/Users/Felix/Desktop/ROS/twiki%202/bin/view/IlcasProjects/AsrPSM.html)
    training.
-   *uint32 num_votes*: the overall number of hypotheses that should be
    generated.
-   *string base_frame_id*: the base frame to which the observed objects
    and the hypothesis should be transformed into.

**without inference:**

-   *string path*: see above
-   *string\[\] scenes*: the name of the scenes. It generates hypotheses
    only for these scenes.
-   *float32\[\] scene_probabilities*: contains the probability of the
    scene.
-   *uint32 num_votes*: the overall number of hypotheses that should be
    created.
-   *asr_msgs::*!*AsrObject\[\] objects*: the list of all observed
    objects.
-   *string base_frame_id*: see above.

The number of the *scene_probabilities* has to be equal to the number of
scenes.

The sum of the *scene_probabilites* should be 1.0, otherwise the number
of hypotheses will not be correct.

There has to be at least one observed object.

**further parameters:**

In the *recognizer_prediction_psm.launch* file you can set the lifetime
of the rviz markers. You can also enable additional console output for
debugging.

AsrPSM parameters (compare [there](http://wiki.ros.org/asr_psm)) are
stored in *param/properties.yaml*

## Needed Services

*asr_msgs::*!*AsrObject\[\] objects*: input. The list of all observed
objects (with inference)

## Provided Services

**/recognizer_prediction_psm**,

**/psm_node**:

Returns an *asr_next_best_view::*!*AttributedPointCloud* message named*
pose_hypothesis.*

This represents the generated hypotheses for all unobserved objects that
are part of the scenes.

Each point in the cloud (!AsrAttributedPoint) consists of a *string
type* and a predicted *geometry_msgs::Pose pose*

of the object.

The point cloud of the poses can be processed by the !AsrNextBestView
package.

Also returns whether all scene objects have been found (true or false).

*psm_node_server*, which offers the */psm_node* service, uses the
*/recognizer_prediction_psm* service offered by
*recognizer_prediction_psm* internally (through the
*asr_recognizer_prediction_psm_client*).

# Tutorials

[AsrRecognizerPSMExample](http://wiki.ros.org/asr_recognizer_prediction_psm/AsrRecognizerPSMExample)
