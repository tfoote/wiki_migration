## Downloading

The opencupboard_action package is a part of the
[mit-ros-pkg](mit-ros-pkg) repository. To download the most recent
version of the stack without downloading the whole repository use

```
$ svn co `roslocate svn opencupboard_action`
```

## Overview

This is the action interface to the opencupboard stack. The opencupboard
action executes the detection, grasping, and opening.

## Explanation

### Detection

The detection is done using tabletop detection. It finds the dominant
plane and returns that as the door. It also returns the objects in front
of the door. The object processing then uses several optional
parameters, orientation, position, and size, to determine the handle.

![](attachment:Screenshot-RViz-4.png)

### Grasping

The grasping uses the GraspHandleAction to find a collision free path to
the handle.

### Opening

The door opening uses hybrid force and position control

## Action Interface

### Opencupboard Action

#### Parameters

Can be specified for specific handles and doors. All of the default
values were determined from our specific cupboard.

```clearsilver
param {
  0.name=door_width
  0.type=double
  0.default=0.18
  0.desc=The width(in meters) of the door in the direction it opens. This is a REQUIRED parameter and is used to determine the final goal position of the door. The width corresponds to the distance the handle opens, so its original position to the final open position, assuming a door opening to 90 degrees. 
  1.name=which_arm
  1.type=String
  1.default="left_arm"
  1.desc=Determines which arm should be used to open the door. This is a REQUIRED parameter.
  2.name=handle_pos
  2.type=String
  2.default="left"
  2.desc=The relative position of the handle on the door. So whether the handle is on the "top","bot","left", or "right" side of the door. This is a REQUIRED parameter.
  3.name=adjust_head
  3.type=array
  3.default=[0.8,0.0,0.65]
  3.desc=The point the head should be looking at to see the cupboard door. This will vary depending on where the robot should be positioned to open the door easiest. This is a REQUIRED parameter.
  4.name=handle_orientation
  4.type=String
  4.default=None
  4.desc=An optional parameter for the orientation of the handle. The handle can either be "horizontal" or "vertical"
  5.name=handle_z
  5.type=double
  5.default=None
  5.desc=An optional parameter for the height range the handle can be found in. Will only successfully find a handle if it within a tolerance of 0.05 meters of this specified height.
```
