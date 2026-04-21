![Blockly_img \| width=800](https://erlerobotics.com/blog/wp-content/uploads/2016/04/erlerobotics_project_5.jpg )

-   Maintainer status: under development
-   Maintainer: Erle Robotics <contact AT erlerobot DOT com>
-   Author: Nestor Gonzalez <nestor94gonzalez AT gmail DOT com > ,
    Alejandro Hernández Cordero <ahcorde AT erlerobot DOT com>, Víctor
    Mayoral Vilches <victor AT erlerobot DOT com>
-   License: GPLv3
-   Bug/feature tracker:
    <https://github.com/erlerobot/robot_blockly/issues>
-   Source: git <https://github.com/erlerobot/robot_blockly.git>
    (branch: master)

## Overview

Blockly is a ROS package that provides web-based visualization and block
programming tools for robots and drones.

## Intro

For several weeks we taught different groups (going from the high-shool
level to the PhD one) how to make use of our robots. While most of the
people quickly understand the different mechanical parts of a robot,
understanding the underlying software is something that took quite a bit
of effort.

When making our training sessions, one of the first things we try to
introduce is the concept of the Robot Operating System (ROS). While
there're many resources on this topic, it's a fact that learning ROS
takes some effort even at the PhD level so we started prototyping ideas
to make this proccess as simple as possible.

We wanted to reach high schools students so we realized that we had to
remove the assumption of "coding skills" from the equation. This made
us look into systems like Scratch for robot programming. The output of
these prototypes has become blockly. A multiplatform web-based tool for
programming robots and drones that use ROS. In fact, Blockly itself is a
ROS package.

This package has been created in order to execute it under
[Erle-Brain 2](http://wiki.ros.org/Robots/Erle-Brain-2),
[Erle-Robotics]( http://erlerobotics.com/blog/home-creative/) artificial
brain for making drones and robots.

## Examples

[Youtube](https://www.youtube.com/watch?v=Zw3-zAJRAkU)
[Youtube](https://www.youtube.com/watch?v=xYQ9GOXgwgo)

## Tutorials

-   [ Tutorial 1: Erle Lidar Laser](http://erlerobotics.com/docs/Robot_Operating_System/ROS/Blockly/Tutorials/Tutorial_1_Erle-Brain_Erle_Lidar_laser.html )

```{=html}
<!-- -->
```
-   [ Tutorial 2: erle-Spider turn degrees](http://erlerobotics.com/docs/Robot_Operating_System/ROS/Blockly/Tutorials/Tutorial_2_Erle-Spider_Turn_degrees_block.html)

```{=html}
<!-- -->
```
-   [ Tutorial 3: Simple maze using Erle-Lidar laser block](http://erlerobotics.com/docs/Robot_Operating_System/ROS/Blockly/Tutorials/Tutorial_3_Erle-Spider_Simple_Maze_using_Lidar.html )

```{=html}
<!-- -->
```
-   [ Tutorial 4: Taking a picture](http://erlerobotics.com/docs/Robot_Operating_System/ROS/Blockly/Tutorials/Tutorial_4_Erle-Brain_Take_a_picture.html )

```{=html}
<!-- -->
```
-   [ Tutorial 5: Detecting color location using the camera](http://erlerobotics.com/docs/Robot_Operating_System/ROS/Blockly/Tutorials/Tutorial_5_Erle-Brain_Camera_color_detection.html )

```{=html}
<!-- -->
```
-   [ Turorial 6: Erle-Spider obstacle avoidance](http://erlerobotics.com/docs/Robot_Operating_System/ROS/Blockly/Tutorials/Tutorial_6_Erle-Spider_Obstacle_avoidance.html )

```{=html}
<!-- -->
```
-   [ Tutorial 7: Erle-Spider SLAM](http://erlerobotics.com/docs/Robot_Operating_System/ROS/Blockly/Tutorials/Tutorial_7_Erle-Spider_localization_and_mapping.html )

```{=html}
<!-- -->
```
-   [ Block creation](http://erlerobotics.com/docs/Robot_Operating_System/ROS/Blockly/Block_creation.html )

## Installation



```
mkdir -p ~/blockly_ws/src
cd ~/blockly_ws/src
git clone https://github.com/erlerobot/robot_blockly
cd robot_blockly/frontend/
git clone https://github.com/erlerobot/ace-builds.git
git clone https://github.com/erlerobot/blockly.git
cd ~/blockly_ws/
catkin_make_isolated -j2 --pkg robot_blockly --install
```



or



```
mkdir -p ~/blockly_ws/src
cd ~/blockly_ws/src
git clone --recurse-submodules https://github.com/erlerobot/robot_blockly
cd ..
catkin_make_isolated -j2 --pkg robot_blockly --install
```



## Launch it



```
source ~/blockly_ws/install_isolated/setup.bash
roslaunch robot_blockly robot_blockly.launch
```



## Support

Please ask your questions not related to bugs/feauture requests on:

-   Erle Robotics Forum: <http://forum.erlerobotics.com/>

We'd like to keep the project bugtracker as free as possible, so please
contact via the above methods.

## Related Links

-   Erle Robotics: <https://erlerobotics.com>
-   Erle-Brain: <https://erlerobotics.com/blog/product/erle-brain-2/>
