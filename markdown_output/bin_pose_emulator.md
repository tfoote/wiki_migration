## Overview

Generator of random bin poses. It provides **/bin_pose** service which
returns a combination of 3 bin picking points in predefined bin:

1\. **Grasp Point** 1. **Approach Point** 1. **Deapproach point**

The **Grasp point **is the goal pose in predefined Virtual Bin. The
**Approach point** is located at the normal vector given by Grasp Point
orientation and the **Deapproach point** is located right above the
Grasp point.

Following video demonstrates the capabilities of bin_pose_emulator in
combination with ABB IRB1200 and MoveIt.

[Youtube](https://www.youtube.com/watch?v=l4nY1mkcvU8)

## Installation

This package is part of the
[binpicking_utils](http://wiki.ros.org/binpicking_utils) stack, The main
repository have been released into ROS Kinetic on Ubuntu, making
installation through \`apt-get\`or synaptic possible. Other
distributions will have build from source.

```
sudo apt-get install ros-kinetic-binpicking-utils
```

## Config

Bin Pose Emulator uses .yaml config file to parse initial settings.
Configure following settings to adopt for your use-case:

Virtual Bin is defined by bin_center\_ and bin_size\_ parameters, while
allowed orientation is set by **roll_range**, **pitch_range** and
**yaw_range**.

By default we assume approaching in the Z-axis of tool0 link
(**roll_default** : 0, **pitch_default**: 3.14, **yaw_default**: 0).
**roll_range**, **pitch_range** and **yaw_range** extend the default
orientation into allowed grasp cone range.

**Approach distance** defines how far in the direction of the normal
vector given by the Grasp Point orientation is the location of Approach
point.

**Deapproach_height** configures height of vertical movement when moving
away from the Grasp Point.

Example config file is located at the config folder. Change launch file
parameter filepath to adopt launch to your custom config file.

```
bin_center_x: 0.5
bin_center_y: 0
bin_center_z: 0.1

bin_size_x: 0.2
bin_size_y: 0.5
bin_size_z: 0.1

roll_default: 0
pitch_default: 3.14
yaw_default: 0

roll_range: 0.707
pitch_range: 0.707
yaw_range: 0.707

approach_distance: 0.1
deapproach_distance: 0.15
```

## Usage

Following
[launch file](https://github.com/durovsky/binpicking_utils/blob/master/bin_pose_emulator/launch/bin_pose_emulator.launch)
loads example config.yaml from package /config directory.

```
roslaunch bin_pose_emulator bin_pose_emulator
``` Call ROS service with an Emptry Request:

```
rosservice call /bin_pose
``` Service response:

```
grasp_pose:
  position:
    x: 0.582990474831
    y: 0.132920391803
    Z: 0.110564293991
  orientation:
    x: 0.113430335549
    Y: 0.719053265498
    z: -0.11979722548
    w: 0.675089426741
approach_pose:
  position:
    x: 0.589268137291
    Y: 0.132789494959
    z: 0.210369854126
  orientation:
    x: 0.113430335549
    y: 0.719052864976
    z: -0.11979722772
    w: 0.675089066083
deapproach_pose:
  position:
    x: 0.582990474831
    y: 0.132920391803
    z: 0.260564299953
  orientation:
    x: 0.113430355498
    y: 0.719052804787
    z: -0.11979722254
    w: 0.678952364862
```

## Visualization

In order to simplify configuration, bin_pose_emulator publishes two
messages to bin_pose_visualization topic. Use Marker plugin in RViz to
visualize the pose of the virtual bin and the location of the current
grasp point. Both Markers are published with *base_link* as a reference
frame.

![\|height=\"400\",width=\"750\"](attachment:bin_pose_visualization.jpg)
