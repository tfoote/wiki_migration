## Preparation

### Create a static 2D map of the environment

see [cob_mapping_slam](cob_mapping_slam)

record map to srs_user_tests package ```
roscd srs_user_tests/ros/config/ipa-apartment
rosrun map_server map_saver
```

### Create initial environment model

start navigation with new map ```
roscd srs_user_tests/ros/config/ipa-apartment
roslaunch cob_navigation_global 2dnav_ros_dwa.launch map:=$(pwd)/map.yaml
```

record bag file on pc2 (TODO: Check if topics are correct)
```
rosbag record -O /tmp/srs_setup.bag /tf /cam3d/depth_registered/points
```

#### create environment model for BUT version

```
rosbag play /tmp/srs/srs_setup.bag
roslaunch srs_env_model but_envmodel_robot.launch
``` Save map ```
roslaunch srs_user_tests save_octomap.launch
roscd srs_user_tests/data
mv saved_octomap.enm ipa-apartment/octomap.enm
``` Load map
```
roslaunch srs_user_tests load_octomap.launch
```

#### create environment model for IPA version

```
rosbag play /tmp/srs/srs_setup.bag
roslaunch cob_3d_mapping_pipeline mapping.launch
rosrun cob_3d_mapping_point_map trigger_mapping.py <start|stop>
``` Save map to bag file ```
rosrun cob_3d_mapping_geometry_map get_geometry_map /tmp/srs/geomap.bag
roscd srs_user_tests/data/ipa-apartment
cp /tmp/srs/geomap.bag .
```
Load initial map from bag file ```
roscd srs_user_tests/data/ipa-apartment
roslaunch cob_3d_mapping_geometry_map set_geometry_map.launch file_path:=geomap.bag
``` Visualization
```
rosrun rviz rviz
```

## Start user tests

### on robot or simulation machine

Start srs components on robot ```
roscd srs_user_tests/ros/config/ipa-apartment
roslaunch cob_navigation_global 2dnav_ros_dwa.launch map:=$(pwd)/map.yaml
```0

`exp` Experiment.

`task` Code of the task.

`cond` Condition or subtask.

`sim` Set `sim` to true for simulated scenario, otherwise omit this
argument or set to false.

`log` When setted to true, logs will be recorded (to
srs_user_tests/data/logs/p1/e2/man2/a for given example) on the robot.
Topics for logging are specified separately for each task in
configuration directory.

`id` Argument `id` can be arbitrary string and it can be used to tag
test/participant.

### on remote pc

```
roscd srs_user_tests/ros/config/ipa-apartment
roslaunch cob_navigation_global 2dnav_ros_dwa.launch map:=$(pwd)/map.yaml
```1

Arguments `exp`, `task`, `cond`, `sim` and `id` have the same
meaning for both launch files. Just `id` has slightly different
function:

`log` When setted to true, screenshots will be recorded (to
srs_user_tests/data/logs/p1/e2/man2/a for given example) on the remote
machine.

## Simulation environment

We developed a highly realistic model apartment for the Gazebo simulator
with many textured furniture items and household objects with realistic
physical features such as weight, friction resistance, centre of
gravity. The model apartment includes a kitchen with dining area,
several corridors, a living room, and a bedroom with furniture and other
household objects. It resembles actual premises at Fraunhofer IPA in
Stuttgart, Germany.

[![Gazebo environment\|width=640](attachment:gazebo-env.jpeg)](attachment:gazebo-env.jpeg)

### Usage instructions

-   checkout [srs_public](https://github.com/ipa320/srs_public)
    repository
-   get copy of
    [cob_environments](https://github.com/mn033/cob_environments)
    (extended fork)
-   start [some scenario](srs_user_tests#Start_user_tests)
