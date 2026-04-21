The Kinematic Analyzer module implements different ways of detecting and
characterizing different joint types. Different methods are implemented
to you can use easily. The Kinematic Analyzer is entirely integrated in
a ROS infrastructure, and reads in and publishes data via ROS.

## Supported Joint Types

-   Revolute joints
-   Prismatic joints
-   Rigid "joints"

## Implemented Joint Detection Methods

In the following we describe which methods are implemented in the
kinematic analyzer method. We assume that each method characterizes the
relative motion of a pair of feature point clusters.

You can switch between the different implementations by setting the ROS
parameter **/kinematic_analyzer/joint_estimator**.

### Transformation based

The most straightforward method is called *transformation_based* since
it examines the rigid transformation of the links between frames. The
general procedure is the following:

1\. Each rigid body is represented as a point cloud of 3D features. We
estimate the rigid body transformation that explains the motion of each
point cloud between the first and the i-th-frame of the interval under
study. We call these motion transformations **global motion**. We use
PCL to find these transformations. 2. For each pair of rigid bodies we
define one of them to be the *reference body* and the other to be the
*moving body*. 3. For each frame we *subtract* the global motion of the
reference body to the global motion of the moving body. To do this we
transform the moving body using the inverse of the global motion of the
reference body. Then we estimate the transformation between the
resulting moved point cloud and the original point cloud at the first
frame. 4. As result of the previous steps we obtain the set of motions
of the moving body without the motion of the reference body, that is,
the **local motions** of the moving body with respect to the reference
body (**careful**, don't mix it with the reference as origin of
coordinates, we refer always the transformations to the same origin of
coordinates, even the local motions).

#### Prismatic Joint

The axis of motion of a prismatic joint is completely defined with its
orientation.

##### Orientation

The orientation of the prismatic joint is defined as the vector that
goes from the center of the moving point cloud to this same center after
being applied the rigid motion transformation of the last frame on it.
This integrates the rotation into the translation. The orientation of
the axis is filtered by the RE framework. That means, the filter
generates a prediction of the orientation of the axis from the believed
orientation and the current control signal (general motion). This
predicted orientation is then compared with the measured one and the
belief is changed according to the difference.

##### Position

The point of application of the joint is unnecessary. As convention, we
select as point of application the middle point between the centers of
both point clusters defining the rigid bodies. Since it is not
necessary, we don't filter it within the RE framework. It is taken as
it is from the last measurement.

#### Revolute Joint

To define completely the axis of rotation of a revolute joint we need to
provide its orientation and position.

##### Orientation

We can easily extract the orientation of the axis and the angle of a
rotation from the quaternion defining the orientation (see
<http://www.euclideanspace.com/maths/geometry/rotations/conversions/quaternionToAngle/index.htm>).
But **careful**, the conversion hat 2 singularities, at 0 and at 180
degrees:

-   At angle = 0 degrees
-   q = 1 + i 0 + j 0 + k 0
-   so working back from above equation qw = 1 so :
-   angle = 2 \* acos(qw) = 0
-   x = qx / sqrt(1-qw\*qw) = divide by zero = infinity
-   y = qy / sqrt(1-qw\*qw) = divide by zero = infinity
-   z = qz / sqrt(1-qw\*qw) = divide by zero = infinity

The orientation of the axis of rotation is filtered in the RE framework.

##### Position

We need to provide **one point**, that the axis of a rotation passes
through, in order to define the axis completely. In the previous
implementation this point was estimated as part of the circle fitting
procedure. Now, we estimate this point from the definition of the rigid
body motion. If we would know the axis of rotation (position and
orientation) we could easily generate the transformation matrix (details
in
<http://www.euclideanspace.com/maths/geometry/affine/aroundPoint/index.htm>)
:

  -- ------ -- ------ -- ------ -- ------------------------------- --
     R_00      R_01      R_02      x - x\*R_00 -y\*R_01 -z\*R_02   
     R_10      R_11      R_12      y - x\*R_10 -y\*R_11 -z\*R_12   
     R_20      R_21      R_22      z - x\*R_20 -y\*R_21 -z\*R_22   
     0         0         0         1                               
  -- ------ -- ------ -- ------ -- ------------------------------- --

We need to extract P=(x,y,z), which is the point that the axis passes
through. We obtain this matrix from PCL when registering the point
clouds between different frames:

  -- ------ -- ------ -- ------ -- ---- --
     R_00      R_01      R_02      tx   
     R_10      R_11      R_12      ty   
     R_20      R_21      R_22      tz   
     0         0         0         1    
  -- ------ -- ------ -- ------ -- ---- --

And then we obtain a system of linear equations on x, y and z:

-   tx = x - x\*R_00 -y\*R_01 -z\*R_02
-   ty = y - x\*R_10 -y\*R_11 -z\*R_12
-   tz = z - x\*R_20 -y\*R_21 -z\*R_22

which we can reformulate in the classical form A\*x = b, were
x=P=(x,y,z), b=t=(tx,ty,tz) and A:

  -- -------- -- -------- -- -------- --
     1-R_00      -R_01       -R_02    
     -R_10       1-R_11      -R_12    
     -R_20       -R_21       1-R_22   
  -- -------- -- -------- -- -------- --

Unfortunately, this system is ill/poorly defined and for small angles of
rotation the solution we can find is inaccurate. We solve it using the
pseudo-inverse based on SVD-decomposition. To estimate the goodness of
the solution we provide the value:

-   Error= \|\|A\*x_estimated - b\|\| / \|\|b\|\|

This value is closer to zero as the x_estimated is closer to a real
solution.

### Circle and Cylinder fitting

The method has been devised by Dov Katz and colleagues:
[Dov Katz's PhD Thesis](http://www.robotics.tu-berlin.de/fileadmin/fg170/Theses/Interactive%20Perception%20of%20Articulated%20Objects%20for%20Autonomous%20Manipulation.pdf)

It is called **feature_based** within the framework.

### Recursive Estimation

The recursive estimation joint estimator is a meta package\... TODO

You will need to select which underlying you use by setting the ROS
parameter **/kinematic_analyzer/joint_estimator_in_re**.

### Implementing your own method

There are some steps to be taken to implement your own joint estimation
method.

-   Create a new folder in *include/joint_estimation* and
    *src/joint_estimation*, e.g. we will use "my_method" in the
    following
-   In the message iap_common::Joint``Msg add a constant for your
    joint type
-   Create a My``Method``Joint class which **virtually** inherits
    from Joint and implement the *getType* and *getTypeStr* as well as
    the *getJoint\...Uncertainty* methods
-   Implement a class for every joint type, i.e.
    My``Method``Revolute``Joint,
    My``Method``Prismatic``Joint etc.
-   Implement a Joint Factory for your method
-   Add an else-branch in the Kinematic``Analyzer``Node, so that
    your method can be selected using a ROS parameter

Take a look at the other methods to see what has to be implemented and
how in detail.

## Package Description

The module provides methods to estimating the joint types between of a
set of moving objects. An object is given a set of visual features,
namely 3D points.

In the package there exists only node named *kinematic_analyzer*. In the
following we explain which parameters can be set, and how to handle
input and output data.

### Information Flow

-   Kinematic analyzer subscribes to a feature topic, where some kind of
    feature tracker publishes a set of visual 3D features (as a PCL
    point cloud) at every time step
-   Additionally, kinematic analyzer subscribes to a segmentation topic.
    A segmentation algorithm (e.g. the visual net) can publish the
    segmentation of the features into different clusters
-   As soon as the kinematic analyzer receives the segmentation it
    automatically triggers the computation and then publishes the
    kinematic structure.

### Parameters

**/number_features**

-   type: *bool*
-   description: Set how many features will be published (can be set
    dynamically using topic /iap/num_features). The parameter is also
    used by visual net, feature tracker etc.

**/video_sensor_type**

-   type: *string*
-   description: Which video sensor you are using. Possible values are
    *kinect* (kinematic analyzer will subscribe to topic
    *camera/rgb/image_color*) and *usb_cam* (kinematic analyzer will
    subscribe to topic *camera/image_raw*)

**/3d_from_sensor**

-   type: *bool*
-   description: If true, kinematic analyzer subscribes to topic
    */iap/feature_set_3d*, otherwise to */iap/estimated_feature_set_3d*

**/min_cluster_size**

-   type: *int*
-   description: How many features are necessary to form a cluster.
    Clusters with less than this amount of features are discarded from
    joint estimation.

**/min_motion**

-   type: *double*
-   description: The minimal displacement of a feature (in Euclidean
    space if using kinect, in image space for RGB data). It is used by
    the joint estimators to characterize the uncertainty of an
    estimation.

**/kinematic_analyzer/joint_estimator**

-   type: *string*
-   description: Select the desired joint estimation method. (See
    [#Implemented Joint Detection Methods](#Implemented Joint Detection Methods)).

**/kinematic_analyzer/joint_estimator_in_re**

-   type: *string*
-   description: When recursive estimation is used as a meta-joint
    estimator, you can select the actual joint estimator used (See
    [#Implemented Joint Detection Methods](#Implemented Joint Detection Methods)).

**/kinematic_analyzer/interval_selection**

-   type: *int*
-   description: Determines how many and which frames can be taken into
    account: *0=Overlapping not advancing*, *1=Not overlapping
    advancing*, *2=overlapping advancing*. (See
    [#Interval Selection](#Interval Selection)).

**/kinematic_analyzer/interval_selection_overlap**

-   type: *int*
-   description: Defines overlap when
    */kinematic_analyzer/interval_selection* is set to *2=overlapping
    advancing*.

**/kinematic_analyzer/trigger_by_segmentation**

-   type: *bool*
-   description: If true, joint estimation is automatically triggered
    when segmentation message arrives (switching this off is usually
    only useful for debugging purposes)

### ROS Subscribers

**/iap/feature_set_3d**

-   type: *sensor_msgs/PointCloud2*
-   description: A set of 3D features at a time. Will be transformed
    into an iap_common::Feature``Set. Kinematic analyzer only
    subscribes if parameter */3d_from_sensor* is true.

**/iap/estimated_feature_set_3d**

-   type: *sensor_msgs/PointCloud2*
-   description: Similar to */iap/feature_set_3d*, but used when if
    parameter */3d_from_sensor* is false.

**/iap/segmentation**

-   type: *sensor_msgs/PointCloud2*
-   description: A segmentation of the features into clusters. Kinematic
    analyzer expects a list of the same length as indicated by parameter
    *number_features*, containing the cluster ID for every feature.

**/iap/num_features**

-   type: *std_msgs/UInt32*
-   description: Set dynamically how many features will be published
    (set statically using parameter /num_features). The Kinematic
    Analyzer will also be reset when it receives this message

**/iap/reset**

-   type: *std_msgs/Empty*
-   description: Trigger a reset of the kinematic_analyzer. You should
    do this if you plan to publish new features from entirely new
    observation

**/iap/external_trigger**

-   type: *std_msgs/Empty*
-   description: Trigger the kinematic analysis (only necessary for
    debugging purposes - usually segmentation triggers the analysis)

### ROS Publishers

**/iap/kinematic_structure**

-   type: *iap_common/KinematicStructureMsg*
-   description: The computed kinematic structure (see
    [iap_common](iap_common))

### ROS Services

None.

### ROS Messages

None. See [iap_common](iap_common).
