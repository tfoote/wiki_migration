# DCM Bringup for Nao robot

The package contains launch and configuration files required to bring
the robot's DCM Driver up and start the robot controllers. The package
allows to control a robot from ROS, while communicating with Naoqi. You
can control the robot either by calling DCM commands or ALMotion (by
default).

## Installation

-   install dependencies ```
sudo apt-get install ros-indigo-nao-robot ros-indigo-nao-meshes ros-indigo-nao-control
```

```{=html}
<!-- -->
```
-   go to a workspace/src
-   clone [naoqi_dcm_driver](naoqi_dcm_driver)
-   clone [nao_dcm_bringup](nao_dcm_bringup)
-   optionally, clone [nao_moveit_config](nao_moveit_config)
-   compile all packages with ```
catkin_make
```

## How to use it

-   first, wake up your robot and choose a stable pose

### Trajectory control

-   start the DCM Bringup providing the robot's IP
    ```
roslaunch nao_dcm_bringup nao_dcm_H25_bringup_remote.launch robot_ip:=<ROBOT_IP>
```

```{=html}
<!-- -->
```
-   you can launch MoveIt! (if installed previously) and control your
    robot (arms by default) ```
roslaunch nao_moveit_config moveit_planner.launch
```

```{=html}
<!-- -->
```
-   you need to check "Allow approximate IK solutions", and then you
    can control the planning_group via an interactive marker

### Position control

To command joints positions via ROS:

-   start the DCM bringup proving your robot's IP (be aware that the
    package will stop Autonomous Life on your robot):
    ```
roslaunch nao_dcm_bringup nao_dcm_H25_bringup_position.launch robot_ip:=<ROBOT_IP>
```

```{=html}
<!-- -->
```
-   send a position to the desired controller, for example
    ```
rostopic pub /nao_dcm/LWristYaw_position_controller/command std_msgs/Float64 "data: 0"
```
