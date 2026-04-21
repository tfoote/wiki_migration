## Overview

This package drives the robot around and moves the head, taking
snapshots. It is useful for data collection, and annotation can be done
by mechanical turk.

## Usage Notes

1\. Follow the bring up instructions to get a working checkout on the
robot 1. 

```
rosmake annotated_map_builder
```

 1. You will also need rviz, so make it
if you have not yet. 1. 

```
export ROBOT=pr[e/f/g]
```

 1. In one console
window on the robot 1. 

```
roscd pr2_alpha
```

 1.


```
roslaunch pr[e/f/g].launch
```

 1. You will will probably need to bring up the
dashboard and make sure the power is ready as described on the bringing
up page 1. In another console on the robot: 1. 

```
rosrun pr2_experimental_controllers tuckarm.py r
```


(If it just hangs, check that you are running it on the robot) 1. In a
third console on the robot: 1. 

```
roscd annotated_map_builder
```

 1. Ensure that
the bags directory has a subdirectory called *annotated_maps* 1.


```
roslaunch record_1.launch
```

 1. At this point the robot will start moving
around but will not have good localization, so be careful and complete
the next step quickly 1. In a fourth console window (probably not on the
robot) 1. 

```
rosrun rviz rviz
```

 1. Follow the instructions at
<http://pr.willowgarage.com/wiki/rviz/UsingTheVisualizer> to initialize
the robot pose

**NOTE:** You may need to run the following in the annotated_map_builder
directory 

```
chmod a+x src/annotated_map_builder/wait_for_multiple_head_configs.py
chmod a+x src/annotated_map_builder/move_head_action.py
```



Also, to change the head positions that are used as the robot wanders
around change the **head_configs** parameter in the file
"*test/move_head.launch*".
