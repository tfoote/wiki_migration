This package contains a controller that tries to move around obstacle
dynamically. In order to load the controller you have to unload the
currently running controller.



```
rosrun pr2_controller_manager pr2_controller_manager kill l_arm_controller r_arm_controller
```

 The controller needs an environment server and
IK/FK solvers to find a way around things in the way.



```
roslaunch reactive_trajectory_controller reactive_trajectory_controller_environment.launch
```

 Now everything is prepared for loading and
starting the controller for both arms



```
roslaunch reactive_trajectory_controller reactive_trajectory_controller.launch
```

 The controller can be used under whatever
application that moves the arms around for example the teleop in
[pr2_arm_teleop_skin](pr2_arm_teleop_skin)
