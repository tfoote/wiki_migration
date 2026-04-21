

```wiki
'''WARNING:''' This documentation refers to an outdated version of rosjava and is probably incorrect. Use at your own risk.
```



## Overview

As mentioned in the Package Summary, this package includes a variety of
different components that together enable teleoperation of the PR2 from
Clojure. Many of these components may be useful on their own, mainly for
others writing Clojure ROS nodes (although the tf_node may be useful for
users of other fringe languages as well). Since the individual
components are fairly well-documented by file-level comments and
function-level docstrings, this page will limit itself to describing how
to use the package as a whole for teleoperation of the PR2.

## Setup

To use the package, you will first have to follow the setup instructions
for [rosjava](rosjava) and [rosclj](rosclj), then "rosmake clj_pr2".

Then, to bring up the ROS nodes required for teleoperation:

-   First, bring up the robot/simulator and nav stack
-   For a robot, bring up *prx.launch* and
    2dnav_pr2*/move_base/2dnav_pr2.launch*
-   For the simulator, use *launch/sim1.launch* or *launch/sim2.launch*,
    or modify these as desired.
-   Second, roslaunch *launch/both_arms.launch* or
    *launch/right_arm.launch*, depending on the arm configuration of
    your (possibly simulated) robot.

Finally, run *bin/clj* to bring up a REPL with all of the necessary code
on the classpath, and type



```clojure
(load "ros/teleop")
```



to load all of the rosjava, rosclj, and teleoperation code, import/refer
to it in the current namespace, initialize ROS, and define "nh" to
point at a fresh NodeHandle.

## Teleoperation

At this point, you have a wide range of functions available for
controlling the sensors, head, torso, base, arms, and grippers of the
PR2. This page will survey the most useful such functions. For
exhaustive lists of functions and more detailed documentation, look at
the files in *src_clj/ros/pr2/\*.clj*, and *src_clj/ros/teleop.clj*.

### Head

Various methods are provided for pointing the head in desired
directions.

At the lowest level, point-head takes a PointStamped, and points the
head at it. 

```clojure
(point-head nh {:header {:frame_id "/map"} :point (make-point [1 2 3])})
```



Track-head does the same thing, but re-points the head every 100 ms (for
when the robot is moving). Passing nil instead of a PointStamped stops
tracking. 

```clojure
(track-head nh {:header {:frame_id "/map"} :point (make-point [1 2 3])})
```



Look-at is less general; it just looks at a given xyz in base_link.


```clojure
(look-at nh [1 0 2]) ; look up and ahead
```



Finally, there are a handful of functions for looking in general
directions. 

```clojure
(look-l) ; look to the left
```



### Torso

get-current-torso-height gets the current torso height (in meters), and
set-torso-position moves the torso to the specified height.



```clojure
; Move torso up 10 cm.
(set-torso-position nh (+ 0.1 (get-current-torso-height nh)))
```



### Base

As with most of the other robot parts (arms, grippers, torso), you can
get an object representing the current base state like so:


```clojure
(get-current-base-state nh)
```



To move the base (using move_base), pass an x, y, and theta to the
move-base function (assumed to be in map frame).


```clojure
(move-base [2 5 Math/PI])
```



Some methods for moving the base by a given distance, without collision
checking, are also provided. These are unsafe; be careful!


```clojure
(forward 0.1) ; unsafely forward 10 cm.
```



Many other methods for relative, precise, unsafe, etc. base movement can
be found in *src_clj/ros/pr2/base.clj*.

### Arms

The simplest way to move the arms is to call move-arm-to-pose, which
attempts to get the griper_palm_link to the specified pose by calling
IK, then passing move_arm the IK solution. The shorter form expects a
pose in base_link, whereas the longer form takes an explicit frame as
well as other arguments. 

```clojure
(load "ros/teleop")
```

0

To move the gripper relatively (in base_link), use move-arm-rel:


```clojure
(load "ros/teleop")
```

1

If you know the precise set of joint angles you want to move to, you can
use move-arm-to-state instead. It takes a robot-arm-state as argument
(see *src_clj/ros/pr2/arm.clj*). The easiest way to create a
robot-arm-state is to use the arm-joint-state function. For instance, to
move the left arm to straight out (all 0 angles), run



```clojure
(load "ros/teleop")
```

2

There are also some useful predefined joint states, which can be
retrieved by name.



```clojure
(load "ros/teleop")
```

3

These functions all also come in unsafe variants (suffixed with
-unsafe), which directly move the arm using the trajectory controller,
with no collision checking. These and other potentially useful functions
are defined in *src_clj/ros/pr2/arm.clj*.

### Grippers

The grippers can be opened and closed by open-gripper/close-gripper,
which take an argument (like many of the arm functions) that is true for
right gripper, false for left gripper. Close-gripper takes a force as an
optional second argument.



```clojure
(load "ros/teleop")
```

4

You can also attach held objects to the gripper, which will be filtered
by the robot-self-filter and checked for collisions by move_arm.
Currently, the only option is an Odwalla bottle-shaped object.



```clojure
(load "ros/teleop")
```

5

### Sensors

laser-fast and laser-slow change the speed of the tilting laser.
laser-fast is needed for safe base movement; laser-slow is needed for
table object perception or cluttered grasping environments.


```clojure
(load "ros/teleop")
```

6

find-object-table returns a point in base_link for the nearest object on
a table in front of the robot. 

```clojure
(load "ros/teleop")
```

7

### Miscellaneous

If you bring any nodes down then up again, or anything else is behaving
weirdly, reset can often help; it shuts down NodeHandle nh and redefines
nh as a fresh NodeHandle. 

```clojure
(load "ros/teleop")
```

8

Some simple grasps are also defined, which take an arm (true for right,
false for left) and an object position in base_link (i.e., as returned
by find-object-table), and try to move the arm and gripper to grab the
object. These work fairly reliably for Odwalla and water bottles, but
have not been tested on other objects. Grasp-object-base uses unsafe
base movement for the final move into grasp position, and
grasp-object-arm uses unsafe arm movement. 

```clojure
(load "ros/teleop")
```

9

Limited access to TF is provided by transform-point-tf and
transform-pose-tf 

```clojure
(point-head nh {:header {:frame_id "/map"} :point (make-point [1 2 3])})
```

0 These and other useful
geometric primitives are defined in *src_clj/ros/geometry.clj*.

Finally, all of the functionality of [rosclj](rosclj) is provided. For
instance, you can easily publish a single message on a topic, or get a
single message from a topic. 

```clojure
(point-head nh {:header {:frame_id "/map"} :point (make-point [1 2 3])})
```

1
