## Overview

`pr2_ogre` defines the PR2 materials for Gazebo/Ogre and provides
texture files for the PR2 casters.

## GAZEBO_RESOURCE_PATH

In order to use the `pr2_ogre` media with `gazebo`, add the root of
the `pr2_ogre` package to your `GAZEBO_RESOURCE_PATH`. For example,
in [roslaunch](roslaunch): 

```
<env name="GAZEBO_RESOURCE_PATH" value="$(find pr2_ogre):$(find pr2_description):$(find gazebo_worlds):$(find gazebo)/gazebo/share/gazebo" />
```


