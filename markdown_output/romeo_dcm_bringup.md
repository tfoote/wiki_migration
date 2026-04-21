# DCM Bringup for Romeo robot

The package contains launch and configuration files required to bring
the robot's DCM Driver up and start the robot controllers. The package
allows to control a robot from ROS, while communicating with Naoqi. You
can control the robot either by calling DCM commands or ALMotion (by
default).

## Source code

<https://github.com/ros-aldebaran/romeo_dcm_robot>

## Installation

-   Install packages 

```
sudo apt-get install ros-indigo-romeo-robot ros-indigo-romeo-control
```



```{=html}
<!-- -->
```
-   go to a workspace/src
-   clone [romeo_control](romeo_control)
-   clone [romeo_dcm_driver](romeo_dcm_driver)
-   clone [romeo_dcm_bringup](romeo_dcm_bringup)
-   optionally, clone [romeo_moveit_config](romeo_moveit_config)
-   compile all packages with 

```
catkin_make
```



## How to use it

-   start the DCM bringup providing the IP of your robot
    

```
roslaunch romeo_dcm_bringup romeo_dcm_bringup_remote.launch robot_ip:=<ROBOT_IP>
```



```{=html}
<!-- -->
```
-   you can launch MoveIt! (if installed previously) and control your
    robot (arms, by default) 

```
roslaunch romeo_moveit_config moveit_planner.launch
```


