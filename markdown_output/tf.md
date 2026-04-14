![\|height=\"431px\",width=\"498px\"](attachment:frames2.png)

## What does tf do? Why should I use tf?

You want to \'\'\'see\'\'\' what tf can do instead of just reading about
it? Check out the
[tf introduction demo](tf/Tutorials/Introduction to tf).

A robotic system typically has many 3D
[coordinate frames](geometry/CoordinateFrameConventions) that change
over \'\'\'time\'\'\', such as a world frame, base frame, gripper frame,
head frame, etc. tf keeps track of all these frames over time, and
allows you to ask questions like:

-   Where was the head frame relative to the world frame, 5 seconds ago?
-   What is the pose of the object in my gripper relative to my base?
-   What is the current pose of the base frame in the map frame?

tf can operate in a \'\'\'distributed system\'\'\'. This means all the
information about the coordinate frames of a robot is available to all
ROS components on any computer in the system. There is \'\'\'no central
server\'\'\' of transform information.

For more information on the design see [/Design](/Design)

## Paper

There is a paper on tf presented at TePRA 2013
[Papers/TePRA2013_Foote](Papers/TePRA2013_Foote)

## Tutorials

We created a set of [tutorials](tf/Tutorials) that walk you through
using tf, step by step. You can get started on the
[introduction to tf](tf/Tutorials/Introduction to tf) tutorial. For a
complete list of all tf and tf-related tutorials check out the
[tutorials](tf/Tutorials) page.

There are essentially two tasks that any user would use tf for,
listening for transforms and broadcasting transforms.

Anyone using tf will need to listen for transforms:

-   \'\'\'Listening for transforms\'\'\' - Receive and buffer all
    coordinate frames that are broadcasted in the system, and query for
    specific transforms between frames. Check out the writing a tf
    listener tutorial
    [(Python)](tf/Tutorials/Writing a tf listener (Python))
    [(C++)](tf/Tutorials/Writing a tf listener (C++)).

To extend the capabilities of a robot you will need to start
broadcasting transforms.

-   \'\'\'Broadcasting transforms\'\'\' - Send out the relative pose of
    coordinate frames to the rest of the system. A system can have many
    broadcasters that each provide information about a different part of
    the robot. Check out the writing a tf broadcaster tutorial
    [(Python)](tf/Tutorials/Writing a tf broadcaster (Python))
    [(C++)](tf/Tutorials/Writing a tf broadcaster (C++)).

Once you are finished with the basic tutorials, you can move on to learn
about tf and time. The tf and time tutorial
[(Python)](tf/Tutorials/tf and Time (Python))
[(C++)](tf/Tutorials/tf and Time (C++)) teaches the basic principles of
tf and time. The advanced tutorial about tf and time
[(Python)](tf/Tutorials/Time travel with tf (Python))
[(C++)](tf/Tutorials/Time travel with tf (C++)) teaches the principles
of time traveling with tf.

## Code API Overview

\<\<Include(tf/Overview)\>\>

## Frequently asked questions

-   [Frequently Asked Questions](tf/FAQ)
-   [Rotation methods](geometry/RotationMethods)
-   [Coordinate Frame Conventions](geometry/CoordinateFrameConventions)

## Command-line Tools

Although tf is mainly a code library meant to be used within ROS
[nodes](Nodes), it comes with a large set of command-line tools that
assist in the debugging and creation of tf coordinate frames. These
tools include:

-   [view_frames](#view_frames): visualizes the full tree of coordinate
    transforms.
-   [tf_monitor](#tf_monitor): monitors transforms between frames.
-   [tf_echo](#tf_echo): prints specified transform to screen
-   [roswtf](roswtf): with the \`tfwtf\` plugin, helps you track down
    problems with tf.
-   [static_transform_publisher](#static_transform_publisher) is a
    command line tool for sending static transforms.

You may also wish to use the [tf_remap](#tf_remap) node, which is a
utility node for remapping coordinate transforms.

### tf_monitor

\`tf_monitor\`

. Print information about the current coordinate transform tree to
console. For example:

```
$ rosrun tf tf_monitor
RESULTS: for all Frames

Frames:
Frame: /base_footprint published by /robot_pose_ekf Average Delay: 0.0469324 Max Delay: 0.0501503
Frame: /base_laser_link published by /robot_state_publisher Average Delay: 0.00891066 Max Delay: 0.009591
Frame: /base_link published by /robot_state_publisher Average Delay: 0.00891147 Max Delay: 0.009592
0.00891431 Max Delay: 0.009595

... editing for the sake of brevity ...

Broadcasters:
Node: /realtime_loop 94.7371 Hz, Average Delay: 0.000599916 Max Delay: 0.001337
Node: /robot_pose_ekf 30.8259 Hz, Average Delay: 0.0469324 Max Delay: 0.0501503
Node: /robot_state_publisher 25.8099 Hz, Average Delay: 0.0089224 Max Delay: 0.00960276
``` \`tf_monitor \<source_frame\>
\<target_target\>\`

. Monitor a specific transform. For example, to monitor the transform
from \`/base_footprint\` to \`/odom\`:

```
$ rosrun tf tf_monitor /base_footprint /odom
RESULTS: for /base_footprint to /odom
Chain currently is: /base_footprint -> /odom
Net delay     avg = 0.00371811: max = 0.012472

Frames:
Frame: /base_footprint published by /robot_pose_ekf Average Delay: 0.0465218 Max Delay: 0.051754
Frame: /odom published by /realtime_loop Average Delay: 0.00062444 Max Delay: 0.001553

Broadcasters:
Node: /realtime_loop 95.3222 Hz, Average Delay: 0.00062444 Max Delay: 0.001553
Node: /robot_pose_ekf 30.9654 Hz, Average Delay: 0.0465218 Max Delay: 0.051754
Node: /robot_state_publisher 25.9839 Hz, Average Delay: 0.00903061 Max Delay: 0.00939562
```

### tf_echo

\`tf_echo \<source_frame\> \<target_frame\>\`

. Print information about a particular transformation between a
\`source_frame\` and a \`target_frame\`. For example, to echo the
transform between \`/map\` and \`/odom\`:

```
$ rosrun tf tf_echo /map /odom
At time 1263248513.809
- Translation: [2.398, 6.783, 0.000]
- Rotation: in Quaternion [0.000, 0.000, -0.707, 0.707]
in RPY [0.000, -0.000, -1.570]
```

### static_transform_publisher

\`static_transform_publisher x y z yaw pitch roll frame_id
child_frame_id period_in_ms\`

. Publish a static coordinate transform to tf using an x/y/z offset in
meters and yaw/pitch/roll in radians. (yaw is rotation about Z, pitch is
rotation about Y, and roll is rotation about X). The period, in
milliseconds, specifies how often to send a transform. 100ms (10hz) is a
good value.

\`static_transform_publisher x y z qx qy qz qw frame_id child_frame_id
period_in_ms\`

. Publish a static coordinate transform to tf using an x/y/z offset in
meters and quaternion. The period, in milliseconds, specifies how often
to send a transform. 100ms (10hz) is a good value.

\`static_transform_publisher\` is designed both as a command-line tool
for manual use, as well as for use within [roslaunch](roslaunch) files
for setting static transforms. For example:

```xml
<launch>
<node pkg="tf" type="static_transform_publisher" name="link1_broadcaster" args="1 0 0 0 0 0 1 link1_parent link1 100" />
</launch>
```

### view_frames

\`view_frames\` is a graphical debugging tool that creates a PDF graph
of your current transform tree.

```
$ rosrun tf view_frames
``` You probably want to view the graph when you
are done, so a typical usage on Ubuntu systems is:

```
$ rosrun tf view_frames
$ evince frames.pdf
``` Therefore an helpful shortcut to add in your
\`.bashrc\` is:

```
alias tf='cd /var/tmp && rosrun tf view_frames && evince frames.pdf &'
```

NOTE: See also [rqt_tf_tree](rqt_tf_tree) that allows dynamic
introspection of the frames.

### roswtf plugin

\`roswtf\` tf comes with a plugin for [roswtf](roswtf) that
automatically runs whenever you run \`roswtf\`. This plugin will analyze
your current tf configuration and attempt to find common problems. To
run, just invoke \`roswtf\` normally:

```
$ roswtf
```

## Nodes

```clearsilver
node.0 {
name = tf_remap
desc = tf_remap listens to the `/tf_old` topic and republishes transforms on the `/tf` topic. This is mainly used with out-of-date [[Bags|bag files]] that need their coordinate frame IDs updated. The typical operation for this node is to play the bag file with `/tf:=/tf_old`. The `tf_remap` node is run with a `~mappings` parameter that describes the mapping of frame IDs from old to new.
sub {
0.name = /tf_old
0.type = tf/tfMessage
0.desc = Old transform tree. This is usually published by remapping playback of a [[Bags|bag file]]. You may need to set use_sim_time true for the bag file transforms to be accepted.
}
pub {
0.name = /tf
0.type = tf/tfMessage
0.desc = Current transform tree. This is the normal `/tf` topic.
}
param {
0.name = ~mappings
0.type = [ {str: str} ]
0.desc = List of dictionaries that map old tf frame IDs to new frame IDs. Each dictionary in the list must have an "old" and "new" key.
0.default = []
}
}
```

```clearsilver
node.0 {
name = change_notifier
desc = `change_notifier` listens to `/tf` and periodically republishes any transforms that have changed by a given amount on the `/tf_changes` topic.
sub {
0.name = /tf
0.type = tf/tfMessage
0.desc = Transform tree.
}
pub {
0.name = /tf_changes
0.type = tf/tfMessage
0.desc = Reduced transform tree.
}
param {
0.name = ~polling_frequency
0.type = float
0.desc = Frequency (hz) at which to check for any changes to the transform tree.
0.default = 10.0
1.name = ~translational_update_distance
1.type = float
1.desc = Minimum distance between the origin of two frames for the transform to be considered changed.
1.default = 0.1
2.name = ~angular_update_distance
2.type = float
2.desc = Minimum angle between the rotation of two frames for the transform to be considered changed.
2.default = 0.1
}
}
```

1.  Keywords Transformation, Transformations, coordinate transform
