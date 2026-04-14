![\|width=\"333\",height=\"200\"](attachment:Logo-white-medium.jpg)

## Description

This packages includes launch and parameter files to start the
navigation components (real or simulated), as well as the maps of the
environment.

## Functionality

Our MILD Robot:

![\|width=\"211\",height=\"390\"](attachment:Mild-Photo.jpg)

Our MILD Robot in simulation and with labor furnishings (Table, PC\...).
You Can see the simulated laserscan data (Red dots/lines), global (pink)
and local costmap (turquoise around the laserscan).

![\|width=\"464\",height=\"276\"](attachment:Mild.jpg)
![\|width=\"461\",height=\"275\"](attachment:Mild1.jpg)
![\|width=\"462\",height=\"275\"](attachment:Mild3.jpg)

### Organization

This graph shows how the components of the MILD and the ROS-Navigation
systems cooperate together. The robot (MILD) has a PC, motor controll
(CAN) and laserscanner (sick). All informations are published at
ROS-Topics. \"move_base_simple/goal\" descripes the goal position.
\"odom\" the odometry of the robot. \"cmd_vel\" the velocity of the
robot and \"scan\" the laserscann data. This information are used by the
navigationsystem to calculate a plan to the goal on the map (move_base)
and locate the robot on the map (amcl).

![\|width=\"652\",height=\"412\"](attachment:navigation-system.JPG)

### Launch

The asr_mild_navigation uses the standard
[ROS_Navigation](http://wiki.ros.org/navigation) with some specific
components. There are three overlay packages:

-   move_base -\>
    [asr_move_base](https://github.com/asr-ros/asr_move_base)
-   nav_core -\> [asr_nav_core](https://github.com/asr-ros/asr_nav_core)
-   navfn -\> [asr_navfn](asr_navfn)

Asr_move_base and asr_navcore are only needed if you use the
asr_ftc_local_planner which is the standard local planner for the
asr_mild_navigation. Look at the
[asr_ftc_local_planner](asr_ftc_local_planner) documentation on how to
use and include the asr_move_base and asr_nav_core packages. The
asr_ftc_local_planner implements a new local planner and is used instead
of the [base_local_planner](http://wiki.ros.org/base_local_planner) or
[dwa_local_planner](http://wiki.ros.org/dwa_local_planner?distro=kinetic).
The asr_navfn package includes an upgraded version of the standard navfn
(check out the asr_navfn documentation). There are also two launch files
to start the gazebo simulation with different rooms.

Now there are different launch files which start all components. They
are divided into simulation launch files and real navigation launch
files:

\'\'\'Simulation:\'\'\'

-   Starts the ROS_Navigation with the overlays and the
    asr_ftc_local_planner.
-   Starts [asr_mild_base_fake_driving](asr_mild_base_fake_driving) to
    simulate driving around with the robot.
-   Loads maps of the environment.

\'\'\'Real:\'\'\'

-   Starts the ROS_Navigation with the overlays and the
    asr_ftc_local_planner.
-   Loads maps of the environment.

## Usage

### Launchfiles

\'\'\'Simulation: \'\'\'

To start the simulation run some of the simulation launch files
depending on your scenario: \"simulation.launch\" is the main launch
file for the simulation. For different maps you can use other launch
files and start out of them the \"launch/simulation/simulation.launch\",
like in \"launch/simulation/simulation_manual_rearranged.launch\".

For example:

```
roslaunch asr_mild_navigation simulation_manual_rearranged.launch
``` Starts simulation.launch, with the
manual_rearranged map. There are also launch files for three other
rooms. How they look you can see on the maps in the folder \"rsc/maps\".

\'\'\'Real:\'\'\'

For the real navigation you only need to start:

```
roslaunch asr_mild_navigation navigation.launch
``` And you must change the map to a map of your
environment:

```
<node name="map_server" pkg="map_server" type="map_server" args="$(find your_package)/your_map.yaml" required="true"/>
``` There are also a launch file
(launch/amcl_diff.launch\") to start [amcl](http://wiki.ros.org/amcl),
this is automaticly started if you launch \"launch/navigation.launch\".

\'\'\'Gazebo:\'\'\'

To start gazebo with the manual_rearranged map/room.

```
roslaunch asr_mild_navigation gazebo_mild_manual_rearranged.launch
```

### Parameters

The package also includes the parameters for the navigation and the maps
of the environment.

You can find them in the folder \"param/\" and \"param/simulation/\".
There you can set the parameters for:

-   [costmap](http://wiki.ros.org/costmap_2d) (Paramertes with are valid
    for global and local costmap)
-   asr_ftc_local_planner
-   [global_costmap](http://wiki.ros.org/costmap_2d)
-   [local_costmap](http://wiki.ros.org/costmap_2d)

For information of the different parameters look at the specific package
documentation.

### Needed packages

All packages form ROS_Navigation (normally included in ROS Installation)
and:

asr_move_base

asr_nav_core

asr_navfn

asr_ftc_local_planner

asr_mild_kinematic_chain

asr_gazebo_models (For gazebo launch)

asr_mild_base_fake_driving (for simulation)

## Tutorials

<http://wiki.ros.org/asr_mild_navigation/StartAllComponents>
