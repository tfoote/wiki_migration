## External Documentation

For detailed documentation on the Stage .world file format, consult the
[Stage manual v3.2.1 (2009)](http://playerstage.sourceforge.net/doc/Stage-3.2.1)
, [Stage manual v4.0.0 (2011)](http://rtv.github.io/Stage/) or
[Stage manual v4.1.1 (2012+)](https://codedocs.xyz/CodeFinder2/Stage/md_README.html).

## Tutorials

- [Creating Custom World in Stage](#creating-custom-world-in-stage):
  In this tutorial a whole custom simulation will be created, including
  the .world file, custom objects and a simple custom robot model.
- [Introduction to Stage Controllers](#introduction-to-stage-controllers):
  Stage (ver 3.0.0 and above) is equipped to work as standalone, wherein
  controllers integrated into stage enables motion, behaviour and
  processes for the robot(s). This tutorial discusses two such stage
  controllers.
- [Making Maps Using Stage's Wander Controller](#making-maps-using-stages-wander-controller):
  This tutorial assumes that you have mastered stage simulations and you
  are well acquainted with the wander controller.This tutorial uses
  stage's wander controller to obtain a map of the robot's environment
  in an incremental manner.
- [Simulating One Robot in Stage](#simulating-one-robot-in-stage):
  This tutorial shows you how to use the Stage simulator to simulate a
  single, Erratic-like robot, roaming an environment that looks a lot
  like the Willow Garage building.

Create a new tutorial:

## Troubleshooting

### Errors when running stageros

#### Error: Segmentation fault

There may be two different types of problems with stage when using
certain graphics drivers. The patches below may help some users with
certain graphics cards (non-nVidia).

##### Problems with stageros

Edit src/stageros.cpp with this change: 

```
190c190
<     this->world = new Stg::WorldGui(200, 200, "Stage (ROS)");
---
>     this->world = new Stg::WorldGui(800, 700, "Stage (ROS)");
```

 and
then (ros)make. You need to mv/rm ROS_NOBUILD for the make process to
actually do something.

There may be a more elegant way to do this, see.

##### Problems with Stage

On machines with certain graphics cards and certain drivers, rosstage
will die on startup with a Segmentation fault (SIGSEGV). In this case,
gdb shows an error inside a gl routine. Some information, including a
possible workaround:

- <http://www.nabble.com/Stage-crashing-on-Ubuntu-Intrepid-td20316050.html>
- <http://sourceforge.net/mailarchive/message.php?msg_id=14C30C8B-5BB9-4664-B4C5-1A7939E3E813%40gerkey.org>
  This problem will hopefully go away with a future upgrade of the
  underlying Stage library, which has significantly re-written graphics
  infrastructure.

## Creating Custom World in Stage

**Description:** In this tutorial a whole custom simulation will be
created, including the .world file, custom objects and a simple custom
robot model.

### Verifying stageros node

Stageros node simulates a world defined in a .world file, which contains
details for sensors, robots and obstacles in the simulated world. Before
all we have to build Stage stack with the following command



```bash
$rosmake stage
```



After this, start an instance of roscore with: 

```bash
$roscore
```


And run stageros node from stage stack with an example world in other
terminal, and then a stage window must appear: 

```bash
$rosrun stage stageros `rospack find stage`/world/willow-erratic.world
```


![alt stage\|width=750](https://lh3.googleusercontent.com/1PLVqz1ZQuSCB7G-GPRuwcNXbJVEofgFXarg4tTHdvbSed1TS_mMPAFir26OcKeVIt9oA9BF1c_sNtUbmq_rXb-_mkqwjc1IwWRy4t2OgI6lcmZx-Tc)

Now that we run stage, we can make our own simulation.

### Creating our simualtion scenario

As said before, the .world file contains definition of the world and
what is in it. From obstacles, walls, through sensors and robot. All
these entities are defined as models and are made using the following
syntax:



```
define model_name model
(
   # parameters
)
```



Now let start creating a map of the world from a image file.

#### Creating our map

#### Creating a simple custom robot model

#### Adding some custom objects

## Introduction to Stage Controllers

- **Note:** This tutorial works on ROS Electric but has known issues in
  ROS Fuerte and ROS Groovy.
- **Description:** Stage (ver 3.0.0 and above) is equipped to work as
  standalone, wherein controllers integrated into stage enables motion,
  behaviour and processes for the robot(s). This tutorial discusses two
  such stage controllers.
- **Keywords:** Stage
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [Making Maps Using Stage's Wander Controller](http://www.ros.org/wiki/stage/Tutorials/MakingMapsUsingStagesWanderController)

### Why Stage Controllers ?

Those of us who have used Stage (or Player/Stage) would have probably
used Stage to set up the environment and the robot and then to implement
behaviour used a C++ or Python code or another ROS node. However, from
Stage ver 3.0.0 onwards there is a facility of Stage Controllers; which
enables some very basic behaviour inbuilt into Stage. Thus, without
using any other code script or ROS node it is possible to implement
behaviour in the robot.

The primary motivation for such was to develop Stage as a swarm robotics
simulator - implement same behaviour to a large number of robots all at
the same time.

### Codes

Download the codes from
<https://code.google.com/archive/p/mobotica/downloads> and extract the
stage_controllers file and make sure that it is in the
[ROS path](http://www.ros.org/wiki/ROS/EnvironmentVariables#ROS_PACKAGE_PATH).

Build the package;



```
rosmake stage_controllers
```



Check if the package can be found by rospack;



```
rospack find stage_controllers
```



### Wander Controller

Wander Controller is a basic stage controller where the robot moves
around wandering and avoiding obstacles. Start an instance of the master
and run this controller for the roomba robot;



```
rosrun stage stageros `rospack find stage_controllers`/world/roomba-wander.world
```



The following screen should pop up with the roomba robot wandering
around.

![alt text/\|width=720](http://4.bp.blogspot.com/-z0QmyYU3_KU/TqRQk2KCLMI/AAAAAAAABsM/MaEz06myic4/s1600/Screenshot-2.png)

What is worth an appreciation is that robot's movement and obstacle
avoidance is obtained from a world file and no other process had to be
run in tandem.

**Discussing the roomba-wander.world file :**

The wander controller is made to work by the part of code at very end of
the file roomba-wander.world, *ctrl "wander"* invokes this controller;



```
roomba
(		  
  # can refer to the robot by this name
  name "roomba"
  pose [ -8 6 0 0 ] 

  sicklaser()
 
  ctrl "wander"
)
```



### Laser Noise Controller

Laser Noise Controller works in tandem with the Wander Controller and
generates laser noise. Start an instance of the master and run this
controller for the roomba robot;



```
rosrun stage stageros `rospack find stage_controllers`/world/roomba-lasernoise.world
```



The following screen should pop up.

![alt text/\|width=720](http://1.bp.blogspot.com/-bjiFEI1Yq38/TqRRtg_x8dI/AAAAAAAABsU/YPRgddriMsQ/s1600/Screenshot-1.png)

**Discussing the roomba-lasernoise.world file :**

In the corresponding world file, roomba-lasernoise.world the Laser Noise
Controller is invoked by *ctrl "lasernoise"* this is made to works in
tandem with the Wander Controller;



```
roomba
(		  
  # can refer to the robot by this name
  name "roomba"
  pose [ 2 2 0 135 ] 

  sicklaser(ctrl "lasernoise")
 
  ctrl "wander"
)
```



### Other Such Stage Controllers

Stage has other such controllers; some deal with multirobot tasks, swarm
robotics etc. Later tutorials may discuss these controllers and also
about writing custom stage controllers.

Also, similar approach is possible in gazebo using the libgazebo client
library to develop controllers.

### References

[Richard T. Vaughan. Massively Multi-Robot Simulations in Stage. Swarm Intelligence, 2(2-4):189-208, 2008](http://autonomy.cs.sfu.ca/doc/vaughan_si08.pdf)

## Making Maps Using Stage's Wander Controller

- **Note:** This tutorial works on ROS Electric but has known issues in
  ROS Fuerte and ROS Groovy.
- **Description:** This tutorial assumes that you have mastered stage
  simulations and you are well acquainted with the wander
  controller.This tutorial uses stage's wander controller to obtain a
  map of the robot's environment in an incremental manner.
- **Keywords:** Stage, SLAM, map
- **Tutorial Level:** ADVANCED

### SLAM Using Stage's Wander Controller

SLAM can be realised using wander controller in stage. The robot can
move around and avoid obstacles by the virtue of the wander controller,
the mapping tools can be used to get 2D map of the environment.

It is worth a note that this tutorial works only for one robot,
multirobot SLAM is not within the scope of this tutorial.

#### Codes

Download the codes from
<http://mobotica.googlecode.com/files/stage_controllers.tar.gz> and
extract the stage_controllers file and make sure that it is in the
[ROS path](http://www.ros.org/wiki/ROS/EnvironmentVariables#ROS_PACKAGE_PATH).

Build the package;



```
rosmake stage_controllers
```



#### Start the stage simulation

Start an instance of the master and start the stage simulation in a new
terminal window



```
rosrun stage stageros `rospack find stage_controllers`/world/roomba-wander-slam.world
```



**NOTE**: The world file employs stage controller 'wander' hence the
robot will start to move immediately and will be in a wandering mode.
For more details on the 'wander' controller, see here -
<http://www.ros.org/wiki/stage/Tutorials/IntroductiontoStageControllers>

#### Start gmapping

Start gmapping in a new terminal window



```
rosrun gmapping slam_gmapping scan:=base_scan
```



#### Start map server

Start map server in a new terminal window



```
rosrun map_server map_saver
```



The map will get saved in the directory from where the command for
`map_server` is issued, as a pgm file. The map may be visible by
clicking on it while the simulation is running, run the simulation till
a desired level of accuracy has been attained.

### Results etc

A sample result;

![alt text/\|width=720](http://3.bp.blogspot.com/-wX3fZADcnso/TvGDsE6DcqI/AAAAAAAABzI/ZP7belD2xWw/s1600/SLAM.png)

A shortcoming of this approach is that, the robot being in 'wander'
mode prefers open spaces compared to narrow lanes. So, one may have to
be patient until the robot covers those congested parts of the
environment thus yielding a better map.

The `rxgraph` of this simulation shows the nodes in use;

![alt text/\|width=720](http://1.bp.blogspot.com/-D3K0tmRW6ts/Tqz-UgP-jWI/AAAAAAAABtA/HfERsysc0cs/s1600/rxgraph.png)

## Simulating One Robot in Stage

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [ROS tutorials](ROS/Tutorials).
- **Description:** This tutorial shows you how to use the Stage
  simulator to simulate a single, Erratic-like robot, roaming an
  environment that looks a lot like the Willow Garage building.
- **Tutorial Level:** BEGINNER

### Build stage

If necessary (e.g., if you're running from your own source tree), build
the stage package:



```
rosmake stage
```

 For the keyboard teleoperation part of this
tutorial, you also need to get the [teleop_base](teleop_base) package,
which has not, at the time of writing, been released. Check it out from
SVN:



```
svn co https://code.ros.org/svn/wg-ros-pkg/branches/trunk_cturtle/sandbox/teleop_base teleop_base
```

 You may need to install the joystick drivers
that teleop_base depends on:



```
sudo apt-get install ros-groovy-joystick-drivers
```

 And (in fuerte and groovy, at least), patch
according to
<http://answers.ros.org/question/40096/cannot-rosmake-teleop_base-getting-fatal-error-in-fuerte/>

Then make sure that the resulting working copy is in your
[ROS_PACKAGE_PATH](ROS/EnvironmentVariables#ROS_PACKAGE_PATH), and build
it:



```
rosmake teleop_base
```



### Run roscore

If necessary, bring up an instance of roscore:



```
roscore
```



### Run stageros with an existing world file

The stage package ships with some example world
files, including one that puts an Erratic-like robot in a Willow
Garage-like environment. To run it:



```
rosrun stage_ros stageros $(rospack find stage_ros)/world/willow-erratic.world
```

 You should see a Stage window pop up that looks
something like this:

![alt text/\|width="720"](https://4.bp.blogspot.com/-Ji_hrhCDN8A/UGkfNRATGpI/AAAAAAAACGg/wKMXlHRuXPc/s1600/p.png)

Browsing the stage window should show up 2 little squares, a red square
which is a red box and a blue square which is the erratic robot.

![alt text/\|width="720"](https://2.bp.blogspot.com/-_BH1Yfsk9-4/UGkfOjpAcXI/AAAAAAAACGo/DBrTxTHGEIc/s1600/q.png)

Click on the stage window and press R to see the perspective view.

![alt text/\|width="720"](https://3.bp.blogspot.com/-mOMMprFWuGM/UGkfP5XiOBI/AAAAAAAACGw/fP1J4Dk2bow/s1600/r.png)

### Drive the robot around

You have a simulated robot; let's make it move. An easy way to do this
is keyboard-based teleoperation. If necessary, build the teleop_base
package:



```
rosmake teleop_base
```

 Now run teleop_base_keyboard:



```
rosrun teleop_base teleop_base_keyboard base_controller/command:=cmd_vel
```

 You should see console output that gives you
the key-to-control mapping, something like this:



```
Reading from keyboard
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

anything else : stop
---------------------------
```

 Hold down any of those keys to drive the robot.
E.g., to drive forward, hold down the **i** key. When you do this, you
should see the robot move in the Stage window. Note that you need focus
in the window where you ran teleop_base_keyboard (e.g., you may need to
click in that window).

### Visualize sensor data

The simulation isn't just for driving; it's also producing sensor
data, some of which can be easily visualized. Let's start with laser
data. If necessary, build rviz:



```
rosmake rviz
```

 Now run [rviz](https://index.ros.org/p/rviz),
using a configuration file in the stage package:



```
roscd stage
rosrun rviz rviz -d `rospack find stage_ros`/rviz/stage.rviz
```

 You should see an rviz window pop up. Now
drive the robot around some more. You should see a kind of "map" start
to accumulate in rviz, looking something like this:

![alt text/\|width="720"](https://2.bp.blogspot.com/-l_fAED3zeTk/UGk7mmsri9I/AAAAAAAACHQ/Sw1Eyr-FoGw/s1600/8.png)

Note that you're just accumulating Stage's perfect laser scans with
perfect odometry. Real robots and real lasers exhibit noise that Stage
isn't simulating (Stage can simulate noisy odometry; see the
[Stage manual](http://playerstage.sourceforge.net/doc/Stage-2.0.0/) for
details). Mapping with noisy sensors requires a SLAM system; check the
[gmapping tutorials](https://index.ros.org/p/gmapping) for more on that
topic.

By the way, the "map" that you've built will disappear over time,
because rviz can only buffer a finite number of laser scans.

------------------------------------------------------------------------
