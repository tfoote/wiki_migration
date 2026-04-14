## About

This stack is an implementation of the [navigation](navigation) stack
for the youBot. It has launch files for navigating with a map provided
by [map_server](map_server) or without a map. When navigating without a
map, slam can be performed using [slam_gmapping](slam_gmapping). It also
has a lowpass filter node to reduce noise from odometry.

This stack has three packages: \`youbot_navigation_common\`,
\`youbot_navigation_local\`, and \`youbot_navigation_global\`.

This documentation is not yet complete.

## Launch Files

### base_front_hokuyo_node.launch

Launches the [hokuyo_node](hokuyo_node) and transform publisher for the
Hokuyo laser scanner. This will generate laser scans on the topic
\`/base_scan\`.

### move_base_local.launch

\`move_base_local.launch\` will start all necessary nodes for navigation
without a map.

### bringup_navigation.launch

This calls the two launch files necessary for navigation without a map,
\`base_front_hokuyo_node.launch\` and \`move_base_local.launch\`.

### slam.launch

This will start SLAM from [slam_gmapping](slam_gmapping). Run it after
running \`bringup_navigation.launch\` if you want to generate a map of
the area the robot is navigating.

### move_base_global.launch

### amcl.launch

Launches the Adaptive Monte-Carlo Localization node, [amcl](amcl), which
uses a particle filter to determine the robot\'s location with respect
to the map.

### bringup_navigation_with_map.launch

## Using this Package

Before launching anything, make sure \`youbot_wrapper\` and
\`youbot_joint_state_publisher\` are running from
[youbot_common](youbot_common).

### For slam

Bring up the navigation nodes without a map, then launch slam.
```
roslaunch youbot_navigation_common bringup_navigation.launch
roslaunch slam.launch
``` \`slam.launch\` assumes that the Hokuyo is
mounted upside down, so it launches a \`laser_flipper\` to compensate.
The suggested way to map a room is to manually teleoperate the robot
around the room until it is reliably mapped. This can be done with
[youbot_teleop](youbot_teleop). ```
roslaunch youbot_teleop youbot_keyboard_teleop_safe.launch
``` When the map of
the room is sufficiently complete, save it with
[map_server](map_server)\'s \`map_saver\` node.

### For click-to-nav

Start a [map_server](map_server) with the desired map. If you just ran
slam, run the \`map_server\` with the \`map.yaml\` file that
\`map_saver\` created.

Bring up navigation: ```
roslaunch youbot_navigation_common bringup_navigation_with_map.launch
```

The robot should now be ready to navigate. Open \`rviz\` and add the
necessary displays. You\'ll need a Robot Model for the youBot, a Map on
the /map topic for the map, a Grid Cells on the
\`/move_base_node/local_costmap/obstacles\` topic for the local map, and
a Laser Scan on the \`/base_scan\` topic for the laser scan. Set the
fixed frame to \`/map\`. Use the \'2D Nav Goal\' tool to select a
desired position and orientation, then watch the robot move to them.

------------------------------------------------------------------------

  -- ------------------------------------------------- -- ---------- -- -------------------------- --
     \<tablewidth=\"100%\"\> ![](attachment:wpi.png)      \<:99%\>      ![](attachment:rail.png)   
  -- ------------------------------------------------- -- ---------- -- -------------------------- --
