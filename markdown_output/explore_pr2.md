## Usage

### explore_pr2.launch

This launch file will start a demo of the [explore](explore) package
configured to run on the PR2 platform. Launch the demo by calling:


```
$ roslaunch explore_pr2 explore_pr2.launch
```



## Visualization

rviz can be used to track the exploration progress. explore_pr2.vcg is
an rviz configuration file that will display the current map, all
frontiers to be explored, the current goal, and the global and local
planner trajectories.
