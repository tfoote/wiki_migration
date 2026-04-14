Additions to the RSM including all mandatory plugin states and a plugin
routine state. Also an additional service provider is included

## Documentation

This package implements plugins for the Calculate Goal State, the
Navigation State and the Mapping State. Furthermore, the Reversing
Routine State is an optional routine state plugin. The Additions Service
Provider handles the data to be transferred between these plugins.

Replace the dots with the usual parameters for the navigation stack.
Both packages share the same parameters but for the robot base frame. To
use a particular navigation stack, initiate it like in this
[tutorial](navigation/Tutorials/SendingSimpleGoals) and call the action
for forward movement with \"move_base\" and for reverse movement with
\"move_base_reverse\". }}}

## Reverse Robot Movement with the Navigation Stack

The following code needs to be included in your launch file (or the
nodes launched respectively) to allow the robot to navigate in forward
and reverse depending on the set mode: ```
<node pkg="move_base" type="move_base" respawn="false" name="move_base" output="screen">
        ...
        <param name="global_costmap/robot_base_frame" value="$(arg robot_frame)" />
        <param name="local_costmap/robot_base_frame" value="$(arg robot_frame)" />
        <remap from="/cmd_vel" to="$(arg autonomy_cmd_vel_topic)" />
    </node>

    <node pkg="move_base" type="move_base" respawn="false" name="move_base_reverse" output="screen">
        ...
        <param name="global_costmap/robot_base_frame" value="$(arg robot_frame)_reverse" />
        <param name="local_costmap/robot_base_frame" value="$(arg robot_frame)_reverse" />
        <remap from="/cmd_vel" to="$(arg autonomy_cmd_vel_topic)_reverse" />
        <remap from="move_base/goal" to="move_base_reverse/goal" />
        <remap from="move_base/cancel" to="move_base_reverse/cancel" />
        <remap from="move_base/feedback" to="move_base_reverse/feedback" />
        <remap from="move_base/status" to="move_base_reverse/status" />
        <remap from="move_base/result" to="move_base_reverse/result" />
    </node>

    <node pkg="tf" type="static_transform_publisher" name="base_footprint_reverse" args="0 0 0 3.1415 0 0 (arg robot_frame) $(arg robot_frame)_reverse 10" />
``` Replace
the dots with the usual parameters for the navigation stack. Both
packages share the same parameters but for the robot base frame. To use
a particular navigation stack, initiate it like in this
[tutorial](navigation/Tutorials/SendingSimpleGoals) and call the action
for forward movement with \"move_base\" and for reverse movement with
\"move_base_reverse\". }}}

## Nodes

{ }}}}

{ }}}}
