# Overview

The HEBI description package `hebi_description` is a collection of
XACRO files and meshes that help to create URDF files for standard or
custom HEBI robotics kits.

For more information about HEBI, see: www.hebi.us

For technical documentation about HEBI components, see: docs.hebi.us

The source code of this package is located at:
<https://github.com/HebiRobotics/hebi_description>

## Using existing standard kits

In the `urdf/kits` folder are several standard HEBI kits, stored as
xacro macros so they can be easily edited. To use one of these (for
example, a 6-DOF arm with a gripper) in a launch file, you could add the
following tag:

```
<param name="robot_description" command="$(find xacro)/xacro --xacro-ns '$(find hebi_description)/urdf/kits/A-2085-06-parallel-gripper.xacro'" />
```

### Simple RViz example

Below is a complete example of a launch file that will visualize this
system in rviz:

```
<launch>
  <node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher" respawn="true" output="screen">
    <param name="ignore_timestamp" value="true"/>
  </node>
  <param name="robot_description" command="$(find xacro)/xacro --xacro-ns '$(find hebi_description)/urdf/kits/A-2085-06-parallel-gripper.xacro'" />
  <node name="rviz" pkg="rviz" type="rviz"/>
</launch>
```

To initialize/update the joint angle, you can publish joint angles on
the joint_states channel as follows:

```
rostopic pub /joint_states sensor_msgs/JointState "header:
  seq: 0
  stamp: {secs: 0, nsecs: 0}
  frame_id: ''
name: ['HEBI/base/X8_9', 'HEBI/elbow/X8_9', 'HEBI/shoulder/X8_16', 'HEBI/wrist1/X5_1', 'HEBI/wrist2/X5_1', 'HEBI/wrist3/X5_1', 'end_effector/input_l_finger']
position: [0, 1, 1, 0, 0, 0, 0]
velocity: [0, 0, 0, 0, 0, 0, 0]
effort: [0, 0, 0, 0, 0, 0, 0]"
```

## Creating custom URDF

Currently, the best reference for creating a custom URDF is looking at
the available kits files as a starting point, as well as reading the
README at

<https://github.com/HebiRobotics/hebi_description>
