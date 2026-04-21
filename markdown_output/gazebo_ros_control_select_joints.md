-   Source: git
    <https://github.com/tu-darmstadt-ros-pkg/gazebo_ros_control_select_joints>
    (branch: master)

## Overview

Gazebo ros_control plugin that allows for selecting the controlled
joints (unlike the standard
[gazebo_ros_control](https://github.com/ros-simulation/gazebo_ros_pkgs/tree/indigo-devel/gazebo_ros_control)
which grabs all transmissions available in the model)

## Installation

Using conda: 

```
conda install -c robostack ros-noetic-gazebo-ros-control-select-joints
```



Using apt: 

```
sudo apt-get install os-noetic-gazebo-ros-control-select-joints
```



From source: 

```
git clone https://github.com/tu-darmstadt-ros-pkg/gazebo_ros_control_select_joints.git
```



## Usage

The usage of this plugin is very similar to the original
[gazebo_ros_control](https://github.com/ros-simulation/gazebo_ros_pkgs/tree/indigo-devel/gazebo_ros_control)
plugin, which documentation can be found
[here](https://classic.gazebosim.org/tutorials?tut=ros_control)

To use the plugin, add the following to your robot's URDF:


```
<gazebo>
  <plugin name="gazebo_ros_control_select_joints" filename="libgazebo_ros_control_select_joints.so">
    <robotNamespace>NAMESPACE</robotNamespace>
    <joints>joint_1 joint_2 joint_3</joints>
  </plugin>
</gazebo>
```



with `<joints>` tag being the feature brought by this package. It
expects a space separated list of joint names.

If no `<joints>` tag is specified, or if the list is empty, the
plugin simply grabs all transmissions available in the model (as the
standard gazebo_ros_control would do).
