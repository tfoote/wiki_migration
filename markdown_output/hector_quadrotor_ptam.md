## Introduction

This package provides launch files and dependencies for starting a
quadrotor visual SLAM simulation mainly based on the
[hector_quadrotor](hector_quadrotor) and [ethzasl_ptam](ethzasl_ptam)
stacks (see both links for relevant publications). A example video can
be seen below.

[Youtube](https://www.youtube.com/watch?v=5BRgu4VBlR0)

## Usage Instructions

Build the package and dependencies: 

```
rosmake hector_quadrotor_ptam
```

 You can now
start the quadrotor simulation: 

```
roslaunch hector_quadrotor_ptam launch_simulation.launch
```

 The use of a
gamepad for UAV control is recommended, for this you can use the
[hector_quadrotor_teleop](hector_quadrotor_teleop) package. When using a
Xbox controller, it can be started like this for instance:


```
roslaunch hector_quadrotor_teleop xbox_controller.launch
```

 Note that you have to do (fly) some purely
translational motion as described on the
[ptam](http://www.ros.org/wiki/ptam#Initialization) page to initialize
the visual SLAM system.
