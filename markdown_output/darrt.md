## Download and Run

**Version:** DARRT only compiles and runs against Fuerte.

### Downloading DARRT+Sushi code

You need both the DARRT code and the Fuerte version of the
"[sushi code](http://kforge.ros.org/Sushi/trac/)" developed for the
mobile manipulation challenge. To obtain both pieces of code:

1\. Download [the rosinstall file](attachment:darrth.rosinstall).

1\. Install: ```
rosinstall . darrth.rosinstall
```

If you see the error: ```
ERROR: Invalid scm entry having no uri attribute for path /opt/ros/fuerte/setup.sh
``` you are using an older
version of rosinstall. Comment out the setup-file line in the rosinstall
file. After installing everything, rosinstall will give you another
error that you can ignore.

If you are prompted for a password, that is your password to
kforge.ros.org. You must be a member of the sandbox project to download
this code. You may need to hit enter a couple times to clear messages
that rosinstall does not display.

1\. Add the darrth and the sushi_all folders to your ROS_PACKAGE_PATH.
Make sure that your ROS_PACKAGE_PATH points to the version of the
distance_field package in darrth. There is currently a bug in the
released version of the distance_field that keeps DARRT from doing
collision checking (it also causes some errors with the 3D Nav stack in
sushi). The folks in charge are looking into this but for now you need
the patched version in the darrth folder. Ensure that
```
roscd distance_field
``` takes you to darrth/distance_field.

1\. Make everything by rosmaking the darrt_actions package
```
rosmake darrt_actions
``` Compilation, especially of darrt_msgs, may take
up to five or ten minutes.

### Downloading DARRT

If you already have the sushi code, you can download DARRT alone using
```
svn co https://kforge.ros.org/sandbox/darrt/fuerte-tag-July-18-2012-Bug-Fix darrth
``` If you are not a member of the kforge project,
you can also get it from the mit-ros-pkg: ```
svn co https://svn.csail.mit.edu/mit-ros-pkg/branches/sandbox-uncrawled/darrt/fuerte-tag-July-18-2012-Bug-Fix darrth
```

The most recent version of DARRT is also in the mit-ros-pkg. This is my
experimental code and not guaranteed to work. The instructions on this
wiki are out of date for this version of the code:
```
svn co https://svn.csail.mit.edu/mit-ros-pkg/branches/sandbox/darrth darrth
```

You should then follow steps 3-4 under Downloading DARRT+Sushi.

### Run

To run DARRT, just launch darrt.launch on the robot or in simulation
using the laser data as an octomap, use ```
roslaunch darrt darrt.launch
```

There may be warnings, but should be no errors while launching this
file. It expects a local version of the objects database.

This starts [interactive manipulation](pr2_interactive_manipulation) on
the robot side and the sushi code for use in executing DARRT plans. It
also starts the darrt_action which can be sent DARRTGoal messages. If
you want to use interactive manipulation while running DARRT, you only
need to launch the desktop file. On the **desktop computer** (not the
robot) launch

```
roslaunch pr2_interactive_manipulation pr2_interactive_manipulation_desktop.launch
```

## ROS API

All interactions with the DARRT planner can take place through the
action interface. This section describes that interface and its input
and output.

### Action Interface

The DARRTAction provides an
[ action server](actionlib#Implementing_an_ActionServer ) that takes in
goals of the type <<MsgLink(darrt_msgs/DARRTGoal)>>.

```clearsilver
sub {
  0.name=darrt_planning/darrt_action/goal
  0.type=darrt_msgs/DARRTGoal
  0.desc=The goal describes the object to move and the place to move it to.
  1.name=darrt_planning/darrt_action/cancel
  1.type=actionlib_msgs/GoalID
  1.desc=A request to cancel a specific goal.
}
```

### Goal

The DARRTGoal message is long and complicated but most of the parameters
are optional. For a
[simple pick and place](darrt/Tutorials/Simple Pick and Place), for
example, only two fields matter: the `pickup_goal` and the `place_goal`.
For [other tasks](darrt/Tutorials/Using Other Primitives), it is
necessary to tell DARRT which primitives it should use.

**Pickup Goal**

Within the pickup message, the following fields must be defined. All
other fields are ignored.

-   arm_name: The arm you want to use. DARRT currently plans for only
    one arm and the base and needs to be told which arm to use
    (eventually it should be able to plan for both).

```{=html}
<!-- -->
```
-   collision_object_name: The object must already be in the collision
    map and this must be its ID in the map.

```{=html}
<!-- -->
```
-   collision_support_surface_name: The object must be sitting on a
    support surface and this surface must be in the collision map. DARRT
    reasons about support surfaces so it needs this information.

```{=html}
<!-- -->
```
-   At least ONE OF desired_grasps or target: DARRT uses pre-defined
    grasps for objects. Either you can pass these in or it calls the
    database or cluster grasp planners.

```{=html}
<!-- -->
```
-   target.reference_frame_id: If you passed in desired_grasps, this
    should be the frame in which those grasps are defined. Otherwise, it
    should be the frame in which the cluster (unrecognized object) or
    the model pose (recognized object) is defined. This is consistent
    with the return from the
    [tabletop_object_detector](tabletop_object_detector) package.

```{=html}
<!-- -->
```
-   lift: The direction and distances to lift after an object is
    grasped. Right now the direction has to be defined in the same frame
    as the root of the arm group, which is the /torso_lift_link frame.
    The distances can be left at zero.

**Place Goal**

The place goal just tells the planner where the object should end up.
This may or may not actually be a "place" on a surface. It is fine for
the place goal to in fact be in midair somewhere. The gripper will open
at the end of the execution only if the object is actually placed on a
support surface. The following fields of the place goal are used (all
others are ignored):

-   place_locations (REQUIRED): Goal locations for the object. By
    default the orientation is ignored; set use_goal_orientation to
    change that.

```{=html}
<!-- -->
```
-   approach (REQUIRED): The direction and distance of the approach to a
    place. Currently the direction must be in the world frame (map if
    using a map, odom_combined otherwise). This field is always
    required, but will only be used if the object is actually ending on
    a support surface. The distances may be left at 0.

```{=html}
<!-- -->
```
-   collision_support_surface_name (OPTIONAL): The name of the support
    surface on which the object will rest if such exists. If the object
    is actually placed onto this support surface (not just if it is
    defined), the plan will return that the last action is a PLACE (at
    the moment it does not plan a retreat from a final place). If the
    object is not placed onto a support surface, the last action will be
    a rigid transfer.

**Primitives**

DARRT plans over primitives that can be used to manipulate objects. At
the moment, DARRT can plan with five different primitives:

-   PICK: Rigidly grasp an object
-   PLACE: Place an object onto a support surface
-   PUSH: Push an object sitting on a support surface
-   BASE_TRANSIT (cannot be used with WARP): Move the PR2 base to better
    manipulate an object. Plans for a full path for the robot base.
-   WARP (cannot be used with BASE_TRANSIT): Move the PR2 base to better
    manipulate an object by "warping" to a good manipulation location
    rather than planning the full path. This assumes you will use a
    different planner for the base path. The planner also assumes that
    after a WARP, any arm being planned for moves down to the robot's
    side. This defaults to the position used for move_base in the sushi
    code, but can be set using the last joint configuration of
    `/arm_configurations/side_tuck/trajectory`.

The primitives DARRT will use to plan are assigned using the primitives
field. If this field is left empty, it defaults to PICK, PLACE, and
WARP. If no primitives that allow base movement are given (i.e. no
BASE_TRANSIT or WARP), DARRT will only do collision checking for the arm
rather than the whole robot.

**Optional Parameters**

The DARRT action also has a number of optional parameters:

-   object_sampling_fraction: This is the fraction of the time that a
    random state will be sampled for the object rather than the robot.
    If you are only using pick and place, this can be left at 0.
    Otherwise, 0.5 is recommended.

```{=html}
<!-- -->
```
-   additional_support_surfaces: Support surfaces other than the ones
    given by the pickup and place goals. Eventually, these will be used
    for re-grasping but they are not actually helpful now.

```{=html}
<!-- -->
```
-   lower_bounds/upper_bounds: The planning bounds in x, y, z for the
    robot. If left empty, the planner uses the initial position, the
    place goal and the support surfaces in the environment to pick
    reasonable bounds.

```{=html}
<!-- -->
```
-   use_place_orientation: Since most of the objects we work with are
    rotationally symmetric, DARRT by default ignores the orientation in
    the place goal. If you want it to respect the orientation set this
    flag.

```{=html}
<!-- -->
```
-   planning_time: The amount of time in seconds for DARRT to plan
    before declaring failure. Set this low for easy environments with
    many restarts and higher for hard environments.

```{=html}
<!-- -->
```
-   tries: The number of planning tries (each of length planning_time)
    before declaring failure.

```{=html}
<!-- -->
```
-   goal_bias: The fraction of the time DARRT should sample a goal
    state.

```{=html}
<!-- -->
```
-   min_grasp_distance_from_surface: Require that a grasp only be
    considered if the wrist is at least this far (in m) from any support
    surface. This is very helpful (probably necessary) when using
    pushing to prevent the planner from considering and
    collision-checking a huge number of infeasible grasps.

```{=html}
<!-- -->
```
-   threshold: The distance in meters that an object can be from its
    goal location and still be considered as satisfying the goal. If
    left at 0, this defaults to 0.02.

```{=html}
<!-- -->
```
-   retreat_distance: The desired distance in meters to retreat after a
    push, pick, or place. If left at 0, this defaults to 0.3 (a high
    retreat is helpful with pushing).

```{=html}
<!-- -->
```
-   primitives: These are the primitives that DARRT is allowed to use.
    If left empty, this defaults to \[PICK, PLACE, WARP\]

### Result

DARRT returns a plan but does not execute it. The DARRTResult message
duplicates some of the fields of the DARRTGoal message to make it
possible to execute a DARRT plan by just sending the result. The
[darrt_actions](darrt_actions) package provides a Python script
(darrt_actions/src/darrt_actions/darrt_trajectories.py) that can execute
DARRT plans. For using the Python script, see the
[tutorials](darrt/Tutorials).

**Primitive Trajectories**

DARRT returns a plan consisting of many trajectories each corresponding
to one primitive. The primitives in DARRTResult do not match those in
DARRTGoal because extra information is needed to accurately execute the
primitives. In fact, the primitives in DARRTResult much more closely
match the underlying primitives used in planning. The primitives are:

-   ARM_TRANSIT: A collision-free path for just an arm. If the arm is
    holding an object this will be collision free for the object and
    arm.
-   PICK: A straight line path for the gripper that corresponds to
    rigidly grasping an object and moving it away from its support
    surface. You should close the gripper before a pick.
-   PLACE: A straight line path for the gripper that corresponds to
    setting an object down on a surface and releasing it. You should
    open the gripper after a place.
-   PUSH: A straight line path for the gripper that corresponds to
    pushing an object across a surface.
-   APPROACH: A straight line path for the gripper that corresponds to
    an approach to a PICK or a PUSH. You should open the gripper before
    an APPROACH.
-   RETREAT: A straight line path for the gripper that corresponds to a
    retreat from PUSH or PLACE.
-   BASE_TRANSIT: A collision free path for the base with the arms and
    objects in their current configuration (if an object is rigidly
    grasped, this path will be collision free for the object as well).
-   BASE_WARP: A jump in the plan to a new configuration. You need to
    plan from the end of the last trajectory to this point because the
    planner has not done that for you.

DARRT returns a list of primitive types (primitive_types) and
corresponding trajectories (primitive_trajectories).
primitive_trajectories\[i\] is an execution of primitive_type\[i\].
Every trajectory is a trajectory for the full robot - it fills in all of
the joints, not just the ones that move. For example if
primitive_type\[3\] = ARM_TRANSIT this means that
primitive_trajectories\[3\] is a collision-free path for the arm.
primitive_trajectories\[3\] is an
<<MsgLink(arm_navigation_msgs/RobotTrajectory)>> and each point
contains a joint value for every joint on the robot regardless of
whether that joint moves or even whether DARRT planned for the joint.
However, it is guaranteed that throughout primitive_trajectories\[3\]
only the arm joints actually do change.

For examples of interpreting and executing DARRT plans, see
[the tutorials](darrt/Tutorials).

**Error Codes**

DARRT also returns an error code. The possible values for this code are:

-   SUCCESS: The planning succeeded and the returned plan is valid.
-   PLANNING_FAILED: The input was valid but DARRT could not find a
    plan. This is a distressingly common return.
-   OBJECT_DOES_NOT_EXIST: The collision_object_name from the
    pickup_goal field could not be found in the collision environment.
    This most often happens when you forget to fill in the field.
-   NO_PLACE_LOCATIONS: You didn't fill in any place locations in the
    place_goal field.
-   CONFIGURE_ERROR: There was a problem with configuring the DARRT
    planner. This can happen if you have the wrong planning description
    on the server (see the
    [discussion about the planning description](darrt#Planning Description File)).
-   NO_GRASPS: Unable to find any grasps for the object.
-   INVALID_PICK_TABLE: An error with the pick support surface. Unlike
    with normal pick and place, DARRT requires knowledge about the
    support surfaces. If the pick table does not exist or the object is
    not sitting on it, DARRT will return this error.
-   OTHER_ERROR: An error that the human needs to fix. Usually this
    means a direction was specified in the wrong frame, but it can also
    be returned if a service call fails. Check rosout for details.

**Notes**

-   DARRT returns a plan not a trajectory; none of the points have any
    time information.

```{=html}
<!-- -->
```
-   Warp assumes that any groups not planned for by DARRT (i.e. the
    other arm) stay in their current configuration.

```{=html}
<!-- -->
```
-   collision_object_name and arm_name are returned even though the user
    specified them in the goal so that it is possible to easily execute
    the returned trajectory without also needing the goal.

### Planning Description File

DARRT uses its own version of pr2_planning_description.yaml both to
change the world frame of the robot when using an Octomap (see
[Using an Octomap](darrt#Using an Octomap)) and to define more planning
groups than just the arms. Be careful when running DARRT that you do not
load a different version of the planning description onto the parameter
server! The /robot_description_planning should include the pr2_base as a
group (which it does not by default): ```
ERROR: Invalid scm entry having no uri attribute for path /opt/ros/fuerte/setup.sh
```0

## Using an Octomap

DARRT does collision checking using the
[planning_environment](planning_environment). This means that it does
collision checking only with objects added to the collision environment
and with the collision map. By default the collision map is the one
collected by the tilting laser. However, it is also possible to use a
pre-constructed octomap as the collision map. This allows much more
accurate collision checking when moving the base. If you have a 3D map,
you should launch darrt with the use_map argument set to true:

```
ERROR: Invalid scm entry having no uri attribute for path /opt/ros/fuerte/setup.sh
```1 This will by default use the Willow Garage
sushi environment maps. You can change the maps being used by setting
the map_suffix argument. Currently the other map available in the
repository is g415, which is a map of the robot environment at MIT. You
can add maps by adding the appropriate map-<map_suffix>.pgm,
map-<map_suffix>.yaml, and octomap-<map_suffix>.bt files to
darrt/config and a pr2_both_arms_<map-suffix>.yaml file to
sbpl_full_body_planner/config.

The darrt.launch file also brings up localization when running with a 3D
map. Because you may want to add things from many parts of the
environment to the collision environment, it's important that any
object added to the collision environment be added in the localized /map
frame and not the /odom_combined frame. This is done by changing the
parent_frame_id of the multi DOF joint defined in
pr2_planning_description.yaml to be map so the planning description that
DARRT loads on the parameter server depends on the use_map argument.
```
ERROR: Invalid scm entry having no uri attribute for path /opt/ros/fuerte/setup.sh
```2

Note that running with an octomap as the collision map may make DARRT
significantly slower.

## Examples

See the [tutorials](darrt/Tutorials) for examples of using DARRT.

## Known Problems

DARRT is very much a work in progress. There are several known bugs.

-   **Running without use_map doesn't work:** It has been a while since
    I have tried running this without an octomap. It's possible that is
    broken. Let me know if that is the case.

```{=html}
<!-- -->
```
-   **Object/Robot Collision:** The July 18 tag has a known bug that
    will allow the robot to collide with objects it can manipulate in
    the environment. The July-18-2012-Bug-Fix tag (currently the one
    downloaded from the rosinstall) should have fixed that bug. Let me
    know if you still see it.

```{=html}
<!-- -->
```
-   **Object not on support surface:** Because DARRT reasons about
    support surfaces and knows objects cannot float in midair, objects
    need to start on a support surface (at the planner level they could
    start in the robot's gripper but this is not implemented in the
    action wrapper). DARRT finds the surface supporting an object by
    checking that the bottom of the object is on the support surface.
    However, the object detection sometimes fails to find the full
    length of the object causing this check and consequently the
    planning to fail.

```{=html}
<!-- -->
```
-   **Self-Collisions with Unused Arm:** When given primitives that
    involve moving the base (WARP or BASE_TRANSIT), DARRT has to do
    full-body collision checks. This includes checking collisions for
    the unused arm so if that arm starts in a self-collision with the
    robot the planning will fail.

```{=html}
<!-- -->
```
-   **It takes too long:** I am working on this problem - this newest
    release actually represents a big improvement. There is a higher
    initial startup cost right now that I could bring down but I've
    been focusing on speeding up the planning. Note that placing on
    tables is still hard for it because, even if you are using warp, it
    has to find a good collision-free base pose near the table. I will
    be trying to make that better in coming months but for now, expect
    that to be slow. To speed DARRT up, the first thing you can do is
    try using the laser map rather than an octomap. In addition,
    adjustments to planning_time, tries, and goal_bias can help a lot.
    If the scene is mostly empty, set planning time low (about 5 s) and
    increase tries (to probably 10) and increase the goal_bias (to about
    0.3 or even higher if you think it should be easy). If the scene is
    very difficult, decrease the goal_bias (to 0.1 or even below) and
    increase the planning_time (30s or so).

```{=html}
<!-- -->
```
-   **Trajectory filter fails on arm plans with a collision:** I think
    this is a problem with different link padding between the planner
    and the filter. When I allow those plans to run they do not have
    collisions although they do usually get close to objects. If the
    trajectory filter fails, I would recommend just assigning times
    yourself and letting the plan run.

```{=html}
<!-- -->
```
-   **Canceling doesn't cancel the planning:** I have tried to make it
    possible to cancel the planning but it is not completely consistent
    yet.

```{=html}
<!-- -->
```
-   **The planner just stops. I see an error message in the output that
    has something to do with the planning:** For debugging, I have
    certain errors halt the planning. I tried to remove it in the tagged
    version but it might still happen. Just press enter.

```{=html}
<!-- -->
```
-   **The Executor class uses 3D Nav to plan even when DARRT has
    returned a plan for the base:** My current base controller is
    terrible. I'm working on a better one but for now it's best to use
    3D nav even though that re-plans.

```{=html}
<!-- -->
```
-   **Plans collide with everything:** The released version of
    distance_field will break collision checking for DARRT. Make sure
    that ```
ERROR: Invalid scm entry having no uri attribute for path /opt/ros/fuerte/setup.sh
```3 takes you to the version of the
    distance field in the darrth folder. The only difference between
    this version and the released version should be in
    src/propagation_distance_field.cpp. In the patched version, line 374
    in the reset() function should have: ```
ERROR: Invalid scm entry having no uri attribute for path /opt/ros/fuerte/setup.sh
```4

```{=html}
<!-- -->
```
-   **Plans collide with spheres and cylinders:**: Collision checking
    currently only works for boxes, meshes and collision maps. Plans
    will collide with anything modelled in the collision map as a sphere
    or cylinder. You have to explicitly add these (tabletop detection
    only adds boxes and meshes) so in common use this should not be a
    problem. We're working on updating this though.

```{=html}
<!-- -->
```
-   **abort: consistency error adding group!** When using rosinstall to
    add the sushi repository. This appears to be an issue with mercurial
    and large files. Everything else will be installed so just manually
    install the sushi repository into sushi_all:
    ```
ERROR: Invalid scm entry having no uri attribute for path /opt/ros/fuerte/setup.sh
```5 This may take several tries - the
    mercurial error appears to be non-deterministic.

```{=html}
<!-- -->
```
-   **Rosinstall throws an error:** You need the latest version of
    rosinstall for the darrth.rosinstall file. If you have an earlier
    version, comment out the setup-file line. You may get some later
    errors about not finding ros stacks but it will install everything
    OK.
