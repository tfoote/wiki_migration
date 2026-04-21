![\|width="498px"](attachment:frames2.png)

## What does tf2 do? Why should I use tf2?

You want to **see** what tf can do instead of just reading about it?
Check out the
[tf2 introduction demo](tf2/Tutorials/Introduction to tf2).

A robotic system typically has many 3D
[coordinate frames](geometry/CoordinateFrameConventions) that change
over **time**, such as a world frame, base frame, gripper frame, head
frame, etc. tf2 keeps track of all these frames over time, and allows
you to ask questions like:

-   Where was the head frame relative to the world frame, 5 seconds ago?
-   What is the pose of the object in my gripper relative to my base?
-   What is the current pose of the base frame in the map frame?

tf2 can operate in a **distributed system**. This means all the
information about the coordinate frames of a robot is available to all
ROS components on any computer in the system. Tf2 can operate with a
central server that contains all transform information, or you can have
every component in your distributed system build its own transform
information database.

For more information on the design see [design](tf2/Design)

## Paper

There is a paper on tf presented at TePRA 2013
[Papers/TePRA2013_Foote](Papers/TePRA2013_Foote)

## Tutorials

We created a set of [tutorials](tf2/Tutorials) that walk you through
using tf2, step by step. You can get started on the
[introduction to tf2](tf2/Tutorials/Introduction to tf2) tutorial. For a
complete list of all tf2 and tf2-related tutorials check out the
[tutorials](tf2/Tutorials) page.

There are essentially two tasks that any user would use tf2 for,
listening for transforms and broadcasting transforms.

Anyone using tf2 will need to listen for transforms:

-   **Listening for transforms** - Receive and buffer all coordinate
    frames that are broadcasted in the system, and query for specific
    transforms between frames. Check out the writing a tf2 listener
    tutorial [(Python)](tf2/Tutorials/Writing a tf2 listener (Python))
    [(C++)](tf2/Tutorials/Writing a tf2 listener (C++)).

To extend the capabilities of a robot you will need to start
broadcasting transforms.

-   **Broadcasting transforms** - Send out the relative pose of
    coordinate frames to the rest of the system. A system can have many
    broadcasters that each provide information about a different part of
    the robot. Check out the writing a tf2 broadcaster tutorial
    [(Python)](tf2/Tutorials/Writing a tf2 broadcaster (Python))
    [(C++)](tf2/Tutorials/Writing a tf2 broadcaster (C++)).

Once you are finished with the basic tutorials, you can move on to learn
about tf2 and time. The tf2 and time tutorial
[(Python)](tf2/Tutorials/tf2 and time (Python))
[(C++)](tf2/Tutorials/tf2 and time (C++)) teaches the basic principles
of tf2 and time. The advanced tutorial about tf2 and time
[(Python)](tf2/Tutorials/Time travel with tf2 (Python))
[(C++)](tf2/Tutorials/Time travel with tf2 (C++)) teaches the principles
of time traveling with tf2.

If you are looking for an easy tool to manually tweak tf transforms,
such as for quick calibration-by-eye tuning, try
[Manual TF Calibration Tools](tf_keyboard_cal)

## Overview

### High level Design

The [design page](tf2/Design) described the high level design of the tf2
library.

`tf2` is the core of a group of packages which form the 2nd generation
of [tf](tf). There are three types of packages.

### Supported Datatypes

`tf2` implements templated datatype support. This allows the core
packages to have minimal dependencies and there be packages which add
support for converting to and from different datatypes as well as
transforming those data types. Please see
[tf2 conversions](http://docs.ros.org/latest/api/tf2/html/) overview,
and [this tutorial](tf2/Tutorials/Migration/DataConversions) for how to
use tf2 with different datatypes. `tf2` does have an internal
datatypes which are based on `bullet`'s !LinearMath library. However
it's recommended to use a fully supported math datatype which best
supports your application. `tf2` conversion methods also support
converting between and transforming between multiple different datatypes
too.

At it's core `tf2` relies on the
[stamped data types](http://docs.ros.org/latest/api/tf2/html/classtf2_1_1Stamped.html)
which can be conveniently correlated to ROS messages which have a
[Messages#Header](Messages#Header).

#### Data Type Support Packages

These packages provide methods to allow tf2 to work natively with data
types of any external library. Most are either C++ or Python specific.

-   [tf2_bullet](tf2_bullet) tf2 methods to work with [bullet](bullet)
    datatypes natively in c++
-   [tf2_eigen](tf2_eigen) tf2 methods to work with Eigen datatypes
    natively in c++.
-   [tf2_geometry_msgs](tf2_geometry_msgs) tf2 methods to work with
    [geometry_msgs](geometry_msgs) datatypes natively in C++ or Python.
-   [tf2_kdl](tf2_kdl) tf2 methods to work with [kdl](kdl) datatypes
    natively in c++ or python.
-   [tf2_sensor_msgs](tf2_sensor_msgs) tf2 methods to work with
    [sensor_msgs](sensor_msgs) datatypes natively in C++ or Python.

### Coordinate Frame Conventions

An important part of using tf2 is to use standard conventions for
coordinate frames.

There are several sources of conventions for using coordinate frames.

-   Units, orientation conventions, chirality, rotation representations,
    and covariance representations are covered in
    [REP 103](http://www.ros.org/reps/rep-0103.html)
-   Standard names for mobile base coordinate frames are covered in
    [REP 105](http://www.ros.org/reps/rep-0105.html)
-   Standard coordinate frames for Humanoid Robots are in
    [REP 120](http://www.ros.org/reps/rep-0120.html)
-   For definitions of some of the math terms used please see the
    [/Terminology](/Terminology) page.

#### Naming

Coordinate frames in ROS are identified by a string `frame_id` in the
format lower case underscore separated. This string has to be unique in
the system. All data produced can simply identify it's `frame_id` to
state where it is in the world.

** No `tf_prefix`:** In previous versions there was a concept of a
`tf_prefix` which would be prepended to the frame name using a `/`
separator. A leading slash used to indicate that it had already been
prefixed. For backwards compatibility tf2 will strip any leading `/`
character.

**No Remapping:**

The concept of `tf` `frame_ids` is not scoped in the same way as
[ROS Names](Names). In particular, namespacing a specific subpart of a
computation graph does not change the physical layout which the `tf`
tree represents. Because of this `frame_id`s do not follow namespace
remapping rules. It is common to support a
[ROS parameter](Parameter Server) to allow changing `frame_id`s used
in algorithms.

**Multiple Robots:**

For use cases with multiple robots it is generally recommended to use
multiple masters and forward specific tf information between the robots.
There are several different methods of implementing bridges between
masters. For more information please see the
[sig/Multimaster](sig/Multimaster).

### Tools

-   [tf2](tf2) The tf2 package is a ROS independent implementation of
    the core functionality. This can be used outside of ROS if the
    message datatypes are copied out.
-   [tf2_tools](tf2_tools) provides a number of tools to use tf2 within
    ROS

### Geometry

`tf2` provides basic geometry data types, such as
[Vector3](http://docs.ros.org/kinetic/api/tf2/html/Vector3_8h.html),
[Matrix3x3](http://docs.ros.org/kinetic/api/tf2/html/classtf2_1_1Matrix3x3.html),
[Quaternion](http://docs.ros.org/kinetic/api/tf2/html/classtf2_1_1Quaternion.html),
[Transform](http://docs.ros.org/kinetic/api/tf2/html/classtf2_1_1Transform.html).
These data types support linear algebra operations between each other.

### ROS Bindings

These packages provide the primary interface for developers using
[tf2](tf2).

-   [tf2_ros](tf2_ros) Provides [roscpp](roscpp) bindings for tf2,
    including classes for `BufferListener`, `BufferBroadcaster`,
    `BufferServer`, and `BufferClient`
-   [tf2_ros](tf2_ros) also provides [rospy](rospy) bindings for tf2,
    including classes for `BufferListener` `BufferBroadcaster` and
    `BufferClient`

### Migration from tf

For more information about migrating from [tf](tf) see
[the migration guide](tf2/Migration)

### Adding static transform support

The goal of static transforms was to remove the need for recommunicating
things that don't change. The ability to update the values was
implemented in case they are subject to uncertainty and might be
re-estimated later with improved values. But importantly those updated
values are expected to be true at all times.

The adding and deleting of transforms is problematic specifically
because of the assumptions about true for all time. If you have a
detachable arm represented by a static transform, and you go through the
process of 1) Install, 2) Remove, 3) Install 4) Remove with the arm.

If you add a static transform at t=1 and 3 and delete the transform at
t=2 and 4. Any queries for transforms from the gripper to the body
should work with a timestamp of 1.5. However if that query is made
between t=1 and t=2 it will pass, but suddenly the previously working
query with timestamp of t=1.5 will break at t=2 due to the static
transform being deleted. And the other issue holds. At t=2.5 the
transform should never lookup, However if queried at time t=3.5 a lookup
of at timestamp 2.5 will pass if a static transform is used.

These incorrect results will also be produced if you break the tree by
changing the connectivity. If you have a frame that's coming and going
you should really use a standard frame and publish it at an
appropriately low rate that's appropriate to capture the expected
frequency of changing the topology of your robot.

The biggest way that static transforms differ from regular transforms is
that they don't keep a time history This primarily saves storage and
lookup time, though the publishing overhead is also better.

## Frequently asked questions

-   [Common Questions](tf2/CommonQuestions)
-   [tf2 questions on answers.ros.org](http://answers.ros.org/questions/scope:all/sort:activity-desc/tags:tf2/page:1/)
-   [tf questions on answers.ros.org](http://answers.ros.org/questions/scope:all/sort:activity-desc/tags:tf/page:1/)
    (The old API but often relevant)
-   [Rotation methods](geometry2/RotationMethods)
