## Overview

`multi_jackal_tutorials` provides examples on how to simulate multiple
[Clearpath Jackals](http://wiki.ros.org/Robots/Jackal) in Gazebo.

![multi_jackal\|width=800](attachment:multi_jackal_tutorials_gazebo.png)

## Tutorials

### Installation

This package (and all dependencies) can be installed the standard way
through rosdep:



```
rosdep install multi_jackal_tutorials
```

 If Gazebo is not yet installed, this may take
some time. Alternatively, you can install it by:


```
sudo apt-get install ros-kinetic-multi-jackal-tutorials
```



### Simulating a Jackal



```
roslaunch multi_jackal_tutorials one_jackal.launch rviz:=true
```

 This launch file does three things. Firstly, it
starts up Gazebo:



```xml
<!-- Start Gazebo with an empty world. -->
<include file="$(find gazebo_ros)/launch/empty_world.launch">
  <arg name="use_sim_time" value="true"/>
  <arg name="gui"          value="$(arg gui)"/>
  <arg name="world_name"   value="$(find multi_jackal_tutorials)/worlds/$(arg world)"/>
</include>
```

 Gazebo will be generating the ROS clock, so it
can simulate faster or slower than real time (this is set in the world
description). If `gui` is set to `true`, the Gazebo client will also
appear. This can also be done after launching by running `gzclient` in
a new terminal.

Secondly, the launch file spawns a robot into Gazebo:



```xml
<!-- Spawn the robot. -->
<include file="$(find multi_jackal_base)/launch/jackal_base.launch">
  <arg name="ns"            value="$(arg ns)"/>
  <arg name="config"        value="$(arg config)"/>
  <arg name="config_id"     value="$(arg config_id)"/>
  <arg name="use_move_base" value="true"/>
</include>
```

 The namespace `ns` must be unique (like
jackal0, jackal1, etc), so that individual robots can be identified. The
configuration type `config` specifies the components on the jackal.
This string must match a file located in
[multi_jackal_description/urdf/configs](https://github.com/NicksSimulationsROS/multi_jackal/tree/ros-kinetic/multi_jackal_description/urdf/configs).
The configuration ID `config_id` is used if required by the
configuration. Movement to goal locations is provided through
[move_base](http://wiki.ros.org/move_base). The model description
([multi_jackal_description](http://wiki.ros.org/multi_jackal_description)),
navigation ([multi_jackal_nav](http://wiki.ros.org/multi_jackal_nav)),
and controllers
([multi_jackal_control](http://wiki.ros.org/multi_jackal_control)), are
all called through the Jackal base
([multi_jackal_base](http://wiki.ros.org/multi_jackal_base)).

Thirdly, the launch file starts up RVIZ: 

```xml
<!-- View in RVIZ. -->
<node name="rviz" pkg="rviz" type="rviz" ns="$(arg ns)" args="-d $(find multi_jackal_tutorials)/rviz/one_jackal.rviz" >
    <remap from="/move_base_simple/goal" to="/$(arg ns)/move_base_simple/goal"/>
</node>
```

 This
displays the robot model, sensor output, and controllers to move the
robot:

![config=base\|width=600](attachment:multi_jackal_tutorials1.png)![config=flea3\|width=600](attachment:multi_jackal_tutorials2.png)![config=apriltags\|width=600](attachment:multi_jackal_tutorials3.png)

Robot topics have been prefixed with the selected namespace (jackal0):

![rostopic list\|width=600](attachment:multi_jackal_tutorials_topics.png)

Frames have also been prefixed by the namespace (right click -> view
image to zoom in):

![rosrun rqt_tf_tree rqt_tf_tree\|width=800](attachment:multi_jackal_tutorials_tf.png)

### Simulating Multiple Jackals



```
roslaunch multi_jackal_tutorials two_jackal.launch rviz:=true
```

 The only difference for multiple Jackals is
that the robots need to be created with different namespaces and
positions.



```xml
<!-- Spawn the robots. -->
<include file="$(find multi_jackal_base)/launch/jackal_base.launch">
  <arg name="ns"            value="$(arg ns0)"/>
  <arg name="config"        value="$(arg config0)"/>
  <arg name="config_id"     value="$(arg config0_id)"/>
  <arg name="use_move_base" value="true"/>
</include>
<include file="$(find multi_jackal_base)/launch/jackal_base.launch">
  <arg name="ns"            value="$(arg ns1)"/>
  <arg name="config"        value="$(arg config1)"/>
  <arg name="config_id"     value="$(arg config1_id)"/>
  <arg name="use_move_base" value="true"/>
  <arg name="x"             value="2"/>
</include>
```



![configs=front_bumblebee2,apriltags\|width=600](attachment:multi_jackal_tutorials4.png)

### Options

A number of arguments can be specified when creating a Jackal. These are
listed in ([multi_jackal_base](http://wiki.ros.org/multi_jackal_base)).
