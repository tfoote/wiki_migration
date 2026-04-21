## ROS API

### Actions and Services Provided

The object_manipulator provides two
[SimpleActionServers](actionlib_tutorials/Tutorials/SimpleActionServer(ExecuteCallbackMethod)):

-   `/object_manipulator_pickup`: requests that an object be picked
    up.
-   action definition:
-   goal:
    [PickupGoal.msg](http://www.ros.org/doc/api/object_manipulation_msgs/html/msg/PickupGoal.html)
-   result:
    [PickupResult.msg](http://www.ros.org/doc/api/object_manipulation_msgs/html/msg/PickupResult.html)
-   feedback: no feedback provided
-   the object must be of type
    [GraspableObject.msg](http://www.ros.org/doc/api/object_manipulation_msgs/html/msg/GraspableObject.html)
-   the object must have been previously segmented from the background,
    added to the collision environment and have a collision name defined
-   grasp definitions are encapsulated in the
    [Grasp](http://www.ros.org/doc/api/object_manipulation_msgs/html/msg/Grasp.html)
    message
-   the action will then:
-   plan a list of potential grasps on the requested object, unless a
    list of desired grasps is already supplied by the caller in the
    pickup goal
-   test each grasp in the list for feasibility in the current
    environment
-   execute the first grasp deemed feasible
-   see message definitions for more details
-   `/object_manipulator_place`: requests that a previously picked up
    object be placed somewhere in the environment
-   action definition:
-   goal:
    [PlaceGoal.msg](http://www.ros.org/doc/api/object_manipulation_msgs/html/msg/PlaceGoal.html)
-   result:
    [PlaceResult.msg](http://www.ros.org/doc/api/object_manipulation_msgs/html/msg/PlaceResult.html)
-   feedback: no feedback provided
-   the object must be of type
    [GraspableObject.msg](http://www.ros.org/doc/api/object_manipulation_msgs/html/msg/PlaceGoal.html)
-   the object must have been previously segmented from the background,
    added to the collision environment and have a collision name defined
-   information is required about how the robot is currently holding the
    object, encapsulated in a
    [Grasp](http://www.ros.org/doc/api/object_manipulation_msgs/html/msg/Grasp.html)
    message. In particular, if the object if held as the result of a
    previous Pickup action execution, this information is returned by
    the Pickup action.
-   Note that, in general place_location is intended to show where you
    want the **object to go in the world**, while grasp is meant to show
    how the object is grasped (where the **hand is relative to the
    object**). Ultimately, what matters is where the hand goes when you
    place the object; this is computed internally by simply
    **multiplying the two transforms** above. If you already know where
    you want the **hand to go in the world** when placing, feel free to
    put that in the place_location, and make the transform in grasp
    equal to identity.
-   the action will then:
-   check if it possible to place the object at the desired location
    without colliding with the environment
-   if place is deemed feasible, place the object at the desired
    location

### Actions and Services Required

The object manipulator assumes a number of actions and services are
available for it to call. Note that, for the PR2 robot equipped with a
gripper, default implementations are available for all of these. The
launch files in
[pr2_object_manipulation_launch](pr2_object_manipulation_launch) will
bring up all of these components and make sure all the topics are mapped
correctly.

Services internal to the manipulation pipeline:

-   grasp planning
-   if no desired grasps are supplied by the caller of the Pickup
    action, the object manipulator will call a grasp planner to create
    its own list of grasps.
-   grasp planning is requested using a
    [GraspPlanning](http://www.ros.org/doc/api/object_manipulation_msgs/html/srv/GraspPlanning.html)
    service call
-   by default, the object manipulator will look for this service on the
    following topics:
-   `/default_database_planner` if the target object is a known model
    from a database of objects
-   `/default_cluster_planner` if the target object is an unrecognized
    point cloud
-   the manipulation pipeline provides default implementations for both
    of these cases.
-   a generic database-backed grasp planner in
    [household_objects_database](household_objects_database)
-   a PR2 gripper-specific planner for unknown point clouds in
    [pr2_gripper_grasp_planner_cluster](pr2_gripper_grasp_planner_cluster)
-   hand posture controller for grasping
-   this component has the ability to:
-   shape the hand in the (pre-)grasp posture specified in a
    [Grasp](http://www.ros.org/doc/api/object_manipulation_msgs/html/msg/Grasp.html)
    message, and to apply the desired joint efforts. This is performed
    using the
    [GraspHandPostureExecutionAction](object_manipulation_msgs/GraspHandPostureExecutionAction)
-   check if a grasp has been correctly executed using proprioception
    (joint values, tactile sensors, etc.). This query is performed using
    the
    [GraspHandPostureQuery](http://www.ros.org/doc/api/object_manipulation_msgs/html/srv/GraspHandPostureQuery.html)
    service.
-   a PR2 gripper-specific implementation is available in
    [pr2_gripper_grasp_controller](pr2_gripper_grasp_controller)
-   reactive grasp (optional)
-   executes the last stages of a grasp using tactile sensor feedback to
    correct for execution errors
-   implemented using the
    [ReactiveGraspAction](object_manipulation_msgs/ReactiveGraspAction)
-   a PR2 gripper-specific implementation is provided in
    [pr2_gripper_reactive_approach](pr2_gripper_reactive_approach)
-   reactive lift (optional)
-   lifts an object while using tactile sensor feedback to apply the
    necessary levels of force to prevent object slip
-   implemented using the
    [ReactiveLiftAction](object_manipulation_msgs/ReactiveLiftAction)
-   a PR2 gripper-specific implementation is available in
    [slipgrip_controller](slipgrip_controller)

Services external to the manipulation pipeline:

-   inverse kinematics
-   arm navigation
-   interpolated inverse kinematics
-   joint trajectory normalization and execution
-   collision map services
-   state validity check (i.e. check a given state for collisions)

### Arm/Hand Description

The manipulator also requires information about the arm/hand combo used
for grasping. This information is expected to be on the parameter
server, as described below. An example configuration file with these
parameters for the PR2 arm and gripper can be found in the
[pr2_object_manipulation_launch](pr2_object_manipulation_launch)
package.

A hand description must contain the following:

-   `hand_description`: this is the root of the tree on the parameter
    server. All arm descriptions must be its children
-   `arm_name`: this is an identifier for the arm/hand combination
    used throughout the system. All individual arm parameters below must
    be its children.
-   `hand_frame`: the tf frame for the "palm" of the hand; this is
    used to define hand poses.
-   `robot_frame`: a frame that is external to the arm, that the
    entire arm is relative to.
-   `attached_objects_name`: the collision environment name that
    object attached to the hand receive when they are attached
-   `attach_link`: the link of the hand that attached objects should
    be considered attached to once they are picked up
-   `hand_group_name`: the name of the group in the collision
    environment that contains all the links of the hand
-   `arm_group_name`: the name of the group in the collision
    environment that contains all the links of the arm and the hand
-   `hand_database_name`: the name of this hand in the
    [household_objects_database](household_objects_database) (if any),
    used for retrieving pre-computed grasps for this hand from the
    database
-   `hand_joints`: the joints of the hand
-   `hand_touch_links`: the link of the hand that are expected to be
    in contact with grasped objects. When a grasped object is attached
    to the hand in the collision environment, collision checks are
    disabled between the links in this group and the object itself
-   `hand_fingertip_links`: the links of the hand that are expected to
    be close to other obstacles in the environment while grasping.
    During the final stages of the grasp, collision padding for these
    links is reduced to 0 to allow grasps that bring the hand very close
    to obstacles (e.g. the table than an object is resting on).
-   `hand_approach_direction`: the direction that the hand uses to
    approach objects, meaning the path from pre-grasp to grasp,
    specified in the coordinate frame of the hand (the one specified as
    `hand_frame` above). The grasp planner(s) and grasp executor(s)
    must be in agreement on how a grasp is to be executed, and this is
    where they get that information.
-   `arm_joints`: the names of the joints that comprise the arm

## Running the Manipulation Pipeline

To launch the manipulation pipeline and execute pickup and place tasks
using the PR2 robot, tutorials and launch files are provided in
[pr2_tabletop_manipulation_apps](pr2_tabletop_manipulation_apps).

Note that, in addition to the functionality covered here, the
manipulation pipeline requires external input for sensor processing,
identifying graspable objects, managing a collision environment, etc. A
default implementation of these, sufficient for running the manipulation
pipeline, is available on the
[tabletop_object_perception](tabletop_object_perception) page.

## Grasping and Placing: Details and Implementation

The main goals of the manipulation pipeline are:

-   to pick up and place both known objects (recognized from a database)
    and unknown objects
-   to perform these operations collision-free, in a largely
    unstructured environment

### A Complete Pickup Task

Chronologically, the process of grasping an object goes through the
following stages:

-   the target object is identified in sensor data from the environment
-   a set of possible grasp points are generated for that object
-   a collision map of the environment is built based on sensor data
-   a feasible grasp point (no collisions with the environment) is
    selected from the list
-   a collision-free path is generated and executed, taking the arm from
    its current configuration to a pre-grasp position for the desired
    grasp point
-   the final path from pre-grasp to grasp is executed
-   optional: tactile sensors are used to correct for errors
-   the gripper is closed on the object and tactile sensors are used to
    detect presence or absence of the object in the gripper
-   optional: the gripper is closed adaptively, using tactile sensors to
    select the right closing force for the target object
-   the object is lifted from the table
-   optional: the object is lifted adaptively, using tactile sensors to
    adjust contact forces in order to prevent slip

Placing an object goes through very similar stages. In fact, grasping
and placing are mirror images of each other, with the main difference
that choosing a good grasp point is replaced by choosing a good location
to place the object in the environment.

### Object Perception

Object perception is an active area of research; it is not internal to
the manipulation pipeline, but rather expected to provide input for
grasping. For running the manipulation pipeline, a simple implementation
for object perception is provided in
[tabletop_object_detector](tabletop_object_detector).

### Grasp Point Selection

For either a recognized object (with an attached database model id) or
an unrecognized cluster, the goal of this component is to generate a
list of good grasp points. Here the object to be grasped is considered
in isolation: a good grasp point refers strictly to a position of the
gripper relative to the object, and knows nothing about the rest of the
environment.

For unknown objects, we use a module that operates strictly on the
perceived point cluster. Details on this module can be found in the
following paper: **Contact-Reactive Grasping of Objects with Partial
Shape Information** that Willow researchers presented at the
[ICRA 2010 Workshop on Mobile Manipulation](http://mobilemanipulation.org/mediawiki/index.php/Schedule).

For recognized objects, our model database also contains a large number
of pre-computed grasp points. These grasp points have been pre-computed
using [GraspIt!](http://grasping.cs.columbia.edu/), an open-source
simulator for robotic grasping.

The output from this module consists of a list of grasp points, ordered
by desirability (it is recommended that downstream modules in charge of
grasp execution try the grasps in the order in which they are
presented).

### Environment Sensing and Collision Map Processing

For collision-free operation, it is important to perceive not only the
target object, but also the rest of the environment, containing
potential obstacles. We rely on collision free operation using the
[arm_navigation](arm_navigation); the additional sensor processing
performed to provide input to the
[collision_environment](collision_environment) see the
[tabletop_collision_map_processing](tabletop_collision_map_processing)
package.

### Motion Planning

Motion planning is also done using the [arm_navigation](arm_navigation)
stack. The algorithm that is being used is an RRT variant.

The motion planner reasons about collision in a binary fashion - that
is, a state that does not bring the robot in collision with the
environment is considered feasible, regardless of how close the robot is
to the obstacles. As a result, the planner might compute paths that
bring the arm very close to the obstacles. To avoid collisions due to
sensor errors or mis-calibration, we pad the robot model used for
collision detection by a given amount (normally 2cm).

### Grasp Execution

The motion planner only works in collision-free robot states. Grasping,
by nature, means that the gripper must get very close to the object, and
that immediately after grasping, the object, now attached to the
gripper, is very close to the table. Since we can not use the motion
planner for these states, we introduce the notion of a **pre-grasp
position**: a pre-grasp is very close to the final grasp position, but
far enough from the object that the motion planner will compute a path
to it. The same happens after pickup: we use a **lift position** which
is far enough above the table that the motion planner can be used from
there.

To plan motion from pre-grasp to grasp and from grasp to lift we use the
[interpolated_ik_motion_planner](interpolated_ik_motion_planner), while
also doing more involved reasoning about which collisions must be
avoided and which collisions are OK. For example, during the lift
operation (which is guaranteed to be in the "up" direction), we can
ignore collisions between the object and the table.

The motion of the arm for executing a grasp is: ```
starting_arm_position
               |
               | <-(motion planner)
               |
              \ /
               V
        pre-grasp position
               |
               | <-(interpolated IK)
               |   (with tactile sensor reactive grasping)
              \ /
               V
         grasp position
      (fingers are closed)
(object model is attached to gripper)
               |
               | <-(interpolated IK)
               |
              \ /
               V
         lift position
               |
               | <-(motion planner)
               |
              \ /
               V
    some desired arm position
```

![](attachment:grasp1.png)

*Interpolated IK path from pre-grasp to grasp planned for a grasp point
of an unknown object*

![](attachment:grasp2.png)

*A path to get the arm to the pre-grasp position has been planned using
the motion planner and executed.*

![](attachment:grasp3.png)

*The interpolated IK path from pre-grasp to grasp has been executed.*

![](attachment:grasp4.png)

*The object has been lifted. Note that the object Collision Model has
been attached to the gripper.*

### Reactive Grasping Using Tactile Sensing

There are many possible sources of error in the pipeline, including
errors in object recognition or segmentation, grasp point selection,
mis-calibration, etc. A common result of these errors will be that a
grasp that is thought to be feasible will actually fail, either by
missing the object altogether or by hitting the object in an unexpected
way and displacing it before the fingers are closed.

We can correct for some of these errors by using the tactile sensors in
the fingertips. We use a grasp execution module that slots in during the
move from pre-grasp to grasp and uses a set of heuristics to correct for
errors detected by the tactile sensors. Details on this module can be
found in the following paper: **Contact-Reactive Grasping of Objects
with Partial Shape Information** that Willow researchers presented at
the
[ICRA 2010 Workshop on Mobile Manipulation](http://mobilemanipulation.org/mediawiki/index.php/Schedule).
