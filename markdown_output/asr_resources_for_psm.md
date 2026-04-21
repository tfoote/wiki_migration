![\|width="333",height="200"](attachment:Logo-white-medium.jpg)

## Description

This package contains resources for probabilistic scene modelling (PSM)
for use in PSM-related packages like [asr_psm](asr_psm).

It specifically contains a class representing an object pose and
operations on it.

## Functionality

The class *Pose* describes an object pose in 3D. The position is
represented as an *Eigen::Vector3d*, the orientation as an
*Eigen::Quaternion<double>*. It offers the possibility to transform a
Pose into another frame.

## Usage

A *Pose* can be constructed from an *asr_msgs::!AsrObject*, a
*geometry_msgs::Pose* or a *!SceneModel::Object* (from the package
[asr_relation_graph_generator](asr_relation_graph_generator)).

Access position and orientation through `getPosition()` and
`getOrientation()`, respectively. To transform an pose into another
frame use `convertPoseIntoFrame(frame, result)`, where both parameters
are boost shared pointers to *Pose*.

### Needed packages

-   [asr_relation_graph_generator](asr_relation_graph_generator)
-   [asr_msgs](asr_msgs)

### Needed software

-   Eigen

### Start system

Used in [asr_psm](asr_psm). Has no parameters.
