## Usage

### explore.launch

This launch file will start a simple demo of the [explore](explore)
package in the [stage](stage) simulator. Launch the demo by calling:
```
$ roslaunch explore_stage explore.launch
```

This configuration file will launch a [move_base](move_base) node to
provide navigation.

### explore_slam.launch

This launch file will start a demo of the [explore](explore) package in
the [stage](stage) simulator that interacts with a [gmapping](gmapping)
node. Launch the demo by calling: ```
$ roslaunch explore_stage explore_slam.launch
```

This configuration file will launch a [move_base](move_base) node to
provide navigation.

## Visualization

rviz can be used to track the exploration progress. explore.vcg is an
rviz configuration file that will display the current map, all frontiers
to be explored, the current goal, and the global and local planner
trajectories.
