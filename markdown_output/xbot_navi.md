## Overview

The package has many functions such as mapping, positioning, navigation,
path planning, and integrated services demo including navigation, face
recognition, and voice conversations. The package relies on the xbot-u
robot platform and other packages such as [xbot](xbot),
[xbot_talker](xbot_talker) and [xbot_face](xbot_face). See the
[gmapping](gmapping), [move_base](move_base), [amcl](amcl) and
[cartographer](cartographer) package for more details to configure the
mapping and navigation parameters.

## Examples

### map_building

To make a map from xbot-u robot with [gmapping](gmapping) package:
```
roslaunch xbot_navi build_map.launch
``` Then run the visualization program on the PC as
the ROS slave: ```
roslaunch xbot_navi rviz_build_map.launch
``` Or you can choose to use google
open source [cartographer](cartographer) to make a map:
```
roslaunch xbot_navi build_map_carto.launch
```

### SLAM navigation

Navigate via [move_base](move_base) and [amcl](amcl):
```
roslaunch xbot_navi demo.launch
``` Or use [cartographer](cartographer) to
navigate: ```
roslaunch xbot_navi navi_carto.launch
```

### Integrated services demo

The service aggregates navigation, face recognition, and voice
conversation into a single service. Users need to modify the
configuration files \`param/kp.json\`\` and param/greet.json\` to manage
keypoints and face greetings. Operation can refer to:
```
roslaunch xbot_navi demo.launch
```
