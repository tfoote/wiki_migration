# Package Summary

A ROS package that automatically configures a swarm robot simulator,
aiming the simulation of large-scale swarms and minimizing the
computational cost, with homogeneous and heterogeneous robots, different
perceptions systems, to the main tasks of robot swarm.

-   Maintainer status: maintained
-   Maintainer: Vivian Cremer Kalempa \<vivian.kalempa AT udesc DOT br\>
-   Author: Vivian Cremer Kalempa \<vivian.kalempa AT udesc DOT br\>,
    André Schneider de Oliveira \<andreoliveira AT utfpr DOT edu DOT
    br\>
-   Source: git <https://github.com/VivianCremerKalempa/swarm_stage_ros>
    (branch: catkin)
-   Developed at the Federal University of Technology - Parana (UTFPR)

# Overview

A playlist with example applications of the system is available on
[YouTube](https://www.youtube.com/channel/UCztalFc6fapGIhQN2Q0jCuw):

[Youtube](https://www.youtube.com/watch?v=Utz85Wnm1QU)

Details can be found in this paper:

```wiki
@INPROCEEDINGS{KalempaTeixeiraOliveiraFabro2018,
 . author={V. Cremer Kalempa and M. A. Simões Teixeira and A. Schneider de Oliveira and J. A. Fabro},
 . booktitle={2018 Latin American Robotic Symposium, 2018 Brazilian Symposium on Robotics (SBR) and 2018 Workshop on Robotics in Education (WRE)},
 . title={Intelligent Dynamic Formation of the Multi-Robot Systems to Cleaning Tasks in Unstructured Environments and with a Single Perception System},
 . year={2018},
 . pages={71-76},
 . doi={10.1109/LARS/SBR/WRE.2018.00022},
 . month={Nov}}
```

# Installation

The swarm_stage_ros package can be installed on your workspace:

```wiki
cd /home/user/catkin_ws/src git clone https://github.com/VivianCremerKalempa/swarm_stage_ros cd .. catkin_make
``` To run your package, you just need this
command:

```wiki
roslaunch swarm_stage_ros swarm_stage.launch
``` Note that roslaunch starts ROS automatically.

At the end of processing, two files are generated: custom.world and
controller.launch. The custom.world file has all the necessary
specification for the scenario to be run on the Stage, for example:

```wiki
  . include "/home/vivian/catkin_ws/src/swarm_stage_ros/launch/include/map.inc"
  . include "/home/vivian/catkin_ws/src/swarm_stage_ros/launch/include/robots.inc"
  . include "/home/vivian/catkin_ws/src/swarm_stage_ros/launch/include/sensors.inc"
  . floorplan (name "cave" size [16.000 16.000 0.800] pose [0 0 0 0] bitmap
  "/home/vivian/catkin_ws/src/swarm_stage_ros/launch/map/image.png")
  . turtlebot (name "r0" pose [0.00 0.00 0 0 ] color "red")
  . roomba (name "r1" pose [-0.30 0.30 0 0 ] color "blue")
  . roomba (name "r2" pose [-0.30 -0.30 0 0 ] color "blue")
  . roomba (name "r3" pose [-0.60 0.60 0 0 ] color "blue")
  . roomba (name "r4" pose [-0.60 -0.60 0 0 ] color "blue")
  . roomba (name "r5" pose [-0.90 0.90 0 0 ] color "blue")
  . roomba (name "r6" pose [-0.90 -0.90 0 0 ] color "blue")
  . roomba (name "r7" pose [-1.20 1.20 0 0 ] color "blue")
  . roomba (name "r8" pose [-1.20 -1.20 0 0 ] color "blue")
  . roomba (name "r9" pose [-1.50 1.50 0 0 ] color "blue")
  . roomba (name "r10" pose [-1.50 -1.50 0 0 ] color "blue")
``` The controller.launch file is generated in
order to run the environment that has just been created:

```wiki
<?xml version="1.0"?>
<launch>
  <!-- ROSCORE -->
        <master auto="start"/>
  <!--  Stage Simulator -->
        <node pkg="stage_ros" type="stageros" name="stageros" args="$(find swarm_stage_ros)/launch/custom.world" respawn="true" output="log"/>
</launch>
``` The swarm_stage.launch requires as a parameter
the arguments passed by the swarm.yaml file:

```wiki
swarm:
   . formation: 'wedge' #no, wedge, square or diamond
   . robots: 10 #used to "no" formation
   . random_colors: 'yes' #yes or no
   . side: 2 #number of robots per side
   . completed: 'no' #when used formation
   . leader: 'no'  #yes or no
   . leader_sonar_sensor: 0 #0, 1  or 3
   . leader_laser_sensor: 'no' #yes or no
   . other_robots_sonar_sensor: 0 #0, 1  or 3, use this field for formation = 'no'
   . other_robots_laser_sensor: 'no' #yes or no
   . scenario: 'forest' #stadium, forest or hospital
   . position_controller: 'yes' #yes or no
   . reference: 'global' #relative(odom) or global
   . publish_tf: 'no' #yes or no, use this field when reference = "relative"

run: 'yes'
``` To simplify the understanding of each parameter
required to the swarm.yaml file, the following table presents a summary,
which contains the values allowed by parameter and a brief description.

```wiki
||||||<tablewidth="100%"border="1"tablestyle="text-align:left"style="text-align:center">'''Parameters of the file swarm.yaml''' ||
||'''Parameter''' ||'''Possible Values''' ||'''Description''' ||
||formation ||no, wedge, square or diamond ||Is the type of formation to be used by the swarm of robots. ||
||robots ||>0 ||Number of robots to be used when the type of formation chosen is "no". For other types of formation this parameter is ignored. ||
||random_colors ||yes or no ||If "yes" is chosen, the colors of the robots will be random. ||
||side ||>0 ||Number of robots for each side of the chosen formation. If no formation was chosen, this field is ignored. ||
||completed ||yes or no ||Used when some type of formation is chosen. When opted for "yes", the formation is filled with robots. ||
||leader ||yes or no ||If a formation is chosen, an additional robot can be added as the leader. ||
||leader_sonar_sensor ||0,1 or 3 ||Leader may have 0, 1 or 3 sonars. ||
||leader_laser_sensor ||yes or no ||A laser sensor can be added to the leader. Only one type of sensor is allowed to the leader. ||
||other_robots_sonar_sensor ||0,1 or 3 ||Robots can have 0, 1 or 3 sonars. ||
||other_robots_laser_sensor ||yes or no ||A laser sensor can be added to the robots. Only one type of sensor is allowed to the robots. ||
||scenario ||stadium, forest or hospital ||The scenario for the simulation can be chosen. In the case of the forest scenario, trees are introduced as obstacles at random. In the case of the hospital, rooms are introduced. ||
||position_controller ||yes or no ||If the value of the position controller parameter is yes, a node is created for each robot of the formation, to call the program posctrl that will receive as an argument the name of the robot. This program should control the \\ position of each robot. ||
||reference ||relative or global ||Allows to choose whether the position of the robot will be relative, that is, based on the odometry or global position of the robot relative to the point of origin of the map. ||
||publish_tf ||yes or no ||If the reference parameter is relative, it is possible to choose between the yes and no values for the publish tf parameter. If yes, the tf.launch file is created and for each robot a transformation is made between its relative position to its overall position on the map. ||
```

------------------------------------------------------------------------

CategoryCategory
