## Overview

This package contains configuration and launch files to run a simple
simulation using stageros. The simulated robot is generic, it could be
adapted to a specific robot. The robot is able to navigate around using
the [ navigation stack](navigation ). In a nutshell, this package
presents a simulated scenario created following
[ navigation_stack tutorials](http://www.ros.org/wiki/navigation/Tutorials),
so it could be considered another [navigation stack](navigation) example
also. [MTTD_interface](MTTD_interface) will use this scenario as
twoLevelMTTD testing environment.

## Nodes



```clearsilver
node.0 {
  name= initial_sender
  desc=`initial_sender` set the robot initial pose.
  pub{
    0.name= initialpose
    0.type= geometry_msgs/PoseWithCovarianceStamped
    0.desc= Just set the initial pose.
  }
 param{
    0.name=~x_pose
    0.default = `8.0`
    0.type= double
    0.desc= x initial position
    1.name=~y_pose
    1.default = `31.0`
    1.type= double
    1.desc= y initial position
    2.name=~z_pose
    2.default=`0.0`
    2.type=double
    2.desc= z initial position
    3.name=~theta_pose"
    3.default=`0.0`
    3.type= double
    3.desc= theta initial orientation
 }
```



## Running

In order to run the simulation, just typing 

```
$ roslaunch MTTD_simulation simulation.launch
```

 and
then set the robot initial pose using [rviz](rviz), or typing (in a new
terminal) 

```
$ rosrun MTTD_simulation initial_sender
```

 Remember to kill `initial_sender`
node after.
