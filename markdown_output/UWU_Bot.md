\'\'\'Welcome Arduino powered UWU_Bot at Uva Wellassa University of Sri
lanka\'\'\'

```
{#!wiki buildsystem catkin
{{{{
{{{
catkin_make
``` }}}} ```
{#!wiki buildsystem rosbuild
{{{
rosmake
```}

# Package Summary

The package UWU_Bot provides all the hardware build description and
drivers to build, develop and run the UWU_Bot

-   Author : Hasitha B. Rathnayake
-   License: BSD
-   Source : git <https://github.com/HasithaBR/UWU_Bot>

# 1. Introduction

This is UWU_Bot which is made for 3D mapping in outdoor purposes but it
is capable for indoor also. Turtlebot\'s keyboard teleop over 3G network
is used instead of short range wifi connection. Teamviewer is used to
control UWU_Bot remotely. The UWU_Bot is made with an low cost concept
with an Arduino pro mini and a RGBD camera (MS Kinect). Arduino recieves
the velocity commands over serial communication and converts thath data
to appropriate motor commands. Then sends to the high power MOSFET motor
controller. Hardware information will be available at
<http://www.t-r-f.info/>

# 2. Installation & Run

-   Guess you have ROS Groovy
-   Install openni, rossreial, ccny_rgbd and turtlebot packages and
    TEAMVIEWER
-   Clone the git to your workspace
-   Upload the provided Arduino sketch in the directory called
    \"UWU_Bot_Arduino\"
-   Switch ON the UWU_Bot
-   Run commands as follows

\'\'\'2.1.0 Launch openni \'\'\'

-   \'\'\$ roslaunch UWU_Bot openni.launch\'\'

\'\'\'2.1.1 Launch map building in a new tab \'\'\'

-   \'\'\$ roslaunch UWU_Bot mapBuilding.launch\'\'

\'\'\'2.1.2 Run the other specific nodes in new sell tabs to get work
UWU_Bot \'\'\'

-   \'\'\$ rosrun UWU_Bot uwu_bot_serial.py\'\' (\'\'\'Starts serial
    communication to send velocity commands\'\'\')
-   \'\'\$ roslaunch UWU_Bot keyboard_teleop.launch\'\' (\'\'\'Starts
    keyboard tele operation\'\'\')
-   \'\'\$ rosrun rviz rviz\'\' (\'\'\'Load the given Mapbuilding.rviz
    config file\'\'\')

\'\'\'2.2 After navigate some distance and SAVE the map to somewhere you
preffered to do\'\'\'

-   \'\'\$ rosservice call /generate_graph\'\'
-   \'\'\$ rosservice call /solve_graph\'\'
-   \'\'\$ rosservice call /save_pcd_map /path/to/dir/myMap.PCD\'\'

\'\'\'2.3\'\'\' \'\'\'Use pcd2ply command to convert saved .pcd files to
convert to .ply format. Because you need .ply file to see the generated
map over \"\'\'meshlab\'\'\" or \"\'\'cloud compare\'\'\" \'\'\'

\'\'\'Ex: \'\'pcd2ply path/myMap.pcd path/myMap.ply\'\'\'\'\'

Above details for the on-bot run. For remote control the UWU_Bot use
teamviewer. SO first start it on UWU_Bot and keep it. Log in to another
base station and connect to the UWU_Bot laptop via teamviewer. Then do
all the above steps. It is simple.

# 3. Report a Bug

<https://github.com/HasithaBR/UWU_Bot/issues>

}}}
