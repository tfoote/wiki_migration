# DCM Bringup for Pepper robot

The package contains launch and configuration files required to bring
the robot's DCM Driver up and start the robot controllers. The package
allows to control a robot from ROS, while communicating with Naoqi. You
can control the robot either by calling DCM commands or ALMotion (by
default).

## Installation

-   install dependencies 

```
sudo apt-get install ros-indigo-pepper-robot ros-indigo-pepper-meshes
```



```{=html}
<!-- -->
```
-   go to a workspace/src
-   clone [pepper_control](pepper_control)
-   clone [naoqi_dcm_driver](naoqi_dcm_driver)
-   clone [pepper_dcm_bringup](pepper_dcm_bringup)
-   optionally, clone [pepper_moveit_config](pepper_moveit_config)
-   compile all packages with 

```
catkin_make
```



## How to use it

### Trajectory control

-   start the DCM bringup providing the IP of your robot
    

```
roslaunch pepper_dcm_bringup pepper_bringup.launch robot_ip:=<ROBOT_IP>
```



```{=html}
<!-- -->
```
-   start Naoqi Driver (to get the odom frame) proving your robot's IP
    

```
roslaunch naoqi_driver naoqi_driver.launch nao_ip:=<ROBOT_IP>
```



#### Control via MoveIt

-   start MoveIt! to control the robot via GUI 

```
roslaunch pepper_moveit_config moveit_planner.launch
```



```{=html}
<!-- -->
```
-   check "Allow approximate IK solutions"
-   control a planning_group via an interactive marker

#### Control via Actionlib

-   you can send a trajectory to the desired controller (actionlib)



```
rosrun actionlib axclient.py <name of the goal topic of the action server>
```



example:



```
rosrun actionlib axclient.py /pepper_dcm/LeftArm_controller/follow_joint_trajectory/goal
```



To choose the controllers you want to load, modify
pepper_control/launch/pepper_control_trajectory.launch. The list of
implemented controllers, you can find in
pepper_control/config/pepper_trajectory_control.yaml. You can start and
stop the ros-controllers using the rqt plugin ControllerManager.

### Position control

To command joints positions via ROS:

-   start the DCM bringup proving your robot's IP (be aware that the
    package will stop Autonomous Life on your robot):
    

```
roslaunch pepper_dcm_bringup pepper_dcm_bringup_position.launch robot_ip:=<ROBOT_IP>
```



```{=html}
<!-- -->
```
-   send a position to the desired controller, for example
    

```
rostopic pub /pepper_dcm/HeadYaw_position_controller/command std_msgs/Float64 "data: 1"
```


