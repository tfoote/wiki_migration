The **iap_common** package provides basic functions and classes for the
interactive perception library (IAP).

## Core Concepts

In the following we describe some of the core classes in the iap_common
framework.

### Features, Sets, Trajectories

Visual features are a central part of the library to define rigid bodies
and joints. The following terminology (and corresponding classes)
facilitates dealing with features.

#### Feature

A feature is a point with an ID, either a 3D point in Euclidean space or
a 2D point in image space. Every different feature must have unique ID -
it Feature class has an internal feature counter and takes care of
giving you a unique feature ID, when you instantiate an object.

Note that there is no notion of time in the feature class - it can
appear in a sequence of frames, but the feature class does not know
anything about this.

#### FeatureSet

A Feature\`\`Set is a set of *different* features at some time
\$frame\$. In particular, a feature set has the notion of time: you can
assign a frame number \$frame\$ to it (which corresponds to the frame in
your sequence). It can be viewed as a snapshot of different features at
some time.

It can be constructed from and exported to a PCL point cloud.

#### FeatureTrajectory

A Feature\`\`Trajectory contains the **same** feature at different time
frames. It can be seen as the trajectory of one feature over time in a
sequence.

#### FeatureTrajectorySet

As the name suggests, a Feature\`\`Trajectory\`\`Set is the combination
of a Feature\`\`Set and Feature\`\`Trajectory: It contains a set of
features at different points in time.

### Clusters

Segmentation algorithms provide a clustering of the features. The
following classes allow dealing with them in an easy manner.

#### Cluster

A Cluster is a specialization of Feature\`\`Set: It contains a set of
*different* features at some time \$frame\$, with an additional *cluster
id*. It usually appears in the context of segmenting a feature set.

#### ClusterSet

A Cluster\`\`Set is a set of clusters at a fixed time frame. It has no
correspondance to any of the Feature**\* classes.**

#### ClusterTrajectorySet

A Cluster\`\`Trajectory\`\`Set is a specialization of
Feature\`\`Trajectory\`\`Set. It is a set of Feature\`\`Trajectories all
belonging to the group (cluster) at a fixed time frame.

### Body Motion

Sometimes you want to abstract away from feature cloud motion and
express the motion of bodies using transformations. The following
classes allow to easily generate and manipulate these transformations.

#### RigidTransformation

A rigid transformation is a special case of linear transformations,
comprising rotations and translations. The class provides different
convience functions for calculating rotation axis/angle, chaining
transformations etc. (Under the hood it uses Eigen for representing
transformations)

#### BodyTrajectory

A body trajectory can be regarded as a timed sequence of rigid
transformations. It provides additional methods for characterizing the
trajectory, like the accumulated translation distance, rotation angle,
etc.

#### BodyTrajectoryPair

In particular for the analysis of joints, we are interested in the
motion of two bodies relative to each other. This relative motion is
represented using the Body\`\`Trajectory\`\`Pair class which allows for
the extraction of the local trajectory, i.e. a Body\`\`Trajectory
expressing the movement of one body with respect to the other.

### Kinematic Structure

iap_common provides messages for sending around kinematic structures. A
**Kinematic\`\`Structure\`\`Msg** consists of
**Joint\`\`Estimator\`\`Result\`\`Msg**s, each containing a hypothesis
per joint type, encoded in **Joint\`\`Msg**. This means a
Kinematic\`\`Structure\`\`Msg does not only contain the \"most
probable\" kinematic structure, but for every pair of links an
estimation of all possible joint types.

## Package Description

### ROS Messages

**/iap_common/KinematicStructureMsg**

-   description: The kinematic structure. Contains a list of
    Joint\`\`Estimator\`\`Result\`\`Msg, i.e. the estimation of all
    joints

**/iap_common/JointEstimatorResultMsg**

-   description: A set of joint hypothesis with according probabilities

**/iap_common/JointMsg**

-   description: A joint with axis information, goodness of fit etc.

**/iap_common/AxisMsg**

-   description: An axis definition for prismatic or revolute joints

**/iap_common/BodyTrajectoryMsg**

-   description: Message to encode a Body\`\`Trajectory

**/iap_common/BodyTrajectoryPairMsg**

-   description: Message to encode a Body\`\`Trajectory\`\`Pair

**/iap_common/ClusteredFeatureSetMsg**

-   description: Message to encode Clustered\`\`Feature\`\`Set
