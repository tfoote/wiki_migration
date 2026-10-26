`pr2_bringup` is a package that collects together the scripts,
[roslaunch](roslaunch) files, and dependencies that are required to
bring a PR2 robot into a running state.

## pr2.launch

The user's entry point for this package is the file `pr2.launch`.
This launch file contains all nodes to run a complete PR2 system.
However, you cannot use pr2.launch to start up the robot (see
[pr2_robot](pr2_robot) for instructions), because pr2.launch requires
another launch file to load the robot description and robot analyzer on
the parameter server first.

### Disable Prosilica Camera

To disable the [prosilica_camera](prosilica_camera) set the
"no-prosilica" arg to "true" in "/etc/ros/robot.launch" when
launching your PR2:



```
<launch>
  <arg name="no-prosilica" value="true" />
  <include file="$(find pr2_bringup)/pr2.launch" />

  <!-- Other stuff -->
</launch>
```



## Running the PR2

This manual will take you step by step through starting the PR2 robot,
<attachment:pr2_robot/pr2_bringup.pdf>. Note: If you have a PR2 that is
running both ROS Groovy and ROS Hydro, this is then the start sequence:

**For Groovy:**



```
robot groovy
```

 

```
export ROS_ENV_LOADER=/etc/ros/env.sh
```




```
roslaunch /etc/ros/robot.launch
```

 **For Hydro:**



```
robot hydro
```

 

```
export ROS_ENV_LOADER=/etc/ros/env.sh
```




```
roslaunch /etc/ros/robot.launch
```

 For your knowledge:



```
robot start
```

 can be used to replace /etc/ros/robot.launch.
The sequence these commands are executed are crucial, otherwise if you
try to export ROS_ENV_LOADER before specifying robot groovy or robot
hydro, then the env loader will load the environment to be whatever was
last typed. Typing robot groovy after env.sh will still have it set to
Hydro if Hydro was the ROS distro set beforehand.

## PR2 Bringup calibration

When the PR2 starts up for the first time since a power down, it will
move its arms, casters, head and later platform to find the reference
position of each joint. This is done by the calibration script
`pr2_bringup/scripts/calibrate_pr2.py`. When finished, the PR2 joint
calibration script stores the joint reference positions locally in the
motor controller board (MCB) of the corresponding joint. So the next
time you start the PR2, it will remember the reference positions and
won't have to repeat the same calibration routine over and over again.

If you want to force the PR2 to run the calibration routine again, you
can erase the stored reference positions from the MCBs by disabling the
breakers (setting the breakers to standby will NOT erase the reference
positions). With the breakers disabled, the power to the MCBs is cut
off, and all the local memory is wiped. Now simply restore power by
enabling the breakers, and the PR2 will re-calibrate its joint reference
positions. Powering down the entire PR2 will obviously have the same
effect. Note that simply restarting the computers does not wipe the
reference positions; the reference positions are stored on the MCBs, not
on the computers.
