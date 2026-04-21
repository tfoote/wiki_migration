![\|height="200",width="333"](attachment:Logo-white-medium.jpg)

## Description

This package provides an implementation of the
"[Follow the Carrot](http://www8.cs.umu.se/kurser/TDBD17/VT06/utdelat/Assignment%20Papers/Path%20Tracking%20for%20a%20Miniature%20Robot.pdf)"
algorithm to local robot navigation on a flat plane. Given a global plan
to follow and a costmap, the local planner produces velocity commands to
send to a mobile base. The parameters for this planner are also
dynamically reconfigurable. This package implements the asr_nav_core
interface for a local planner. For this to work the standard
[move_base](http://wiki.ros.org/move_base) and
[nav_core](http://wiki.ros.org/nav_core?distro=kinetic) must be adapted
(look at kapitel 3.1 Needed Packages).

## Functionality

The "Follow the Carrot" planer tries to follow the global plan as
accurately as possible. Based on the global plan it computes velocity
commands to get to a point in that plan. As it uses the global plan to
move around obstacles that plan needs to be updated continuously.

![\|height="281",width="327"](attachment:donkeycarrotbellcurve.jpg)

### Phases

The planner is divided into three phases after setting a new goal:

1\. Rotate on the spot to the global plan orientation.

2\. Drive to the goal.

3\. Rotate on the spot to the goal orientation.

### Calculation

How the calculation of the velocity works can be seen in the following
picture:

![\|height="578",width="673"](attachment:ftc_local_planner.jpg)

The planner goes along the global plan until the maximal distance or
angle is reached. With this maximal distance or angle calculates the
planner the velocity of the robot to follow the global plan. For example
in the first image row you see a calculation of the velocity if the
sim_time = 1s and max_x_vel = 2 m/s. So de robot could drive 2 meters in
the given sim_time. Thereforce we go 2 meters along the global plan. Now
we check the angle of the reached point and the robot orientation. If it
is lower than simt_time \* max_rotation_vel we calculate the two
velocity how you seen under the pictures row.

In the second picture row, we also go 2 meters along the global plan.
Now we check the angle. It is higher than sim_time \* max_rotation_vel.
So we go backward the global plan until the max reachable angle is
reached.

### Slow_down_factor

The slow down factor is only used at the 3. Phase of the planning, also
at the rotation to the goal orientation. It allows to correct the
braking characteristics at the end of rotation to prevent a apprupt
brack. This can indebted by differenc between calculatet velocity and
real driven velocity (The motor controll could produce other velocitys
than required).

In this pictures you can see the function graph of the slow down factor.
The first one depicts braking without a slow down factor -> the robot
rotates a long time with minimal rotation velocity. With the slow down
factor in the second picture the robot rotates not as long with a
minimal rotation velocity.

![\|height="221",width="530"](attachment:slow_down_factor.png)

### Safety function

The planner has a safety function. The robot doesn't drive to an area
which is near an obstacle. For this to work the planner checks the
global costmap: If the to driven way is in high rated area of the global
costmap (very near at a obstacle) the robot will stop! It will only
drives again if a new set global goal drives the robot away from the
obstacle.

### Benefits

-   fast driving: The robot tries to reach the maximal velocity as fast
    as possible.
-   few parameters: Only 11 parameters must be set.
-   few jerks: the robot tries to drive constantly with the maximal
    velocity.
-   for small rooms: the robot drives closely to the global plan, no
    loops (like the dwa_local_planner). So it can drive without
    collision in small rooms.
-   Drive around obstacles with the global plan: guaranteed to find a
    way around the obstacle.
-   short processing time.

### Limitations

-   Only for circular robots.
-   Only differential driven robots.
-   Drives only forward (not backwards).

## Usage

If you follow the points below, you should be able to simply set up the
local planer and drive your robot.

You can also look at this [Tutorial](SetupNavigationForFTCPlanner) with
a point by point description on how to setup the navigation to use the
ftc_local_planner.

### Needed packages

You must adapt the two standard navigation packages move_base and
nav_core. There are two ways to do this:

Either use the provided asr-packages which use the ftc_planner (they are
modified versions of the original ones):

[asr_move_base](https://github.com/asr-ros/asr_move_base)

[asr_nav_core](https://github.com/asr-ros/asr_nav_core)

OR

Manually adapt the two packages
[move_base](http://wiki.ros.org/move_base) and
[nav_core](http://wiki.ros.org/nav_core?distro=kinetic):

**Move_base:**

In the move_base package in file "move_base.cpp" at line 132 add:
(After the initialization of the local planner)



```
tc_->setGlobalCostmap(planner_costmap_ros_);
```

 **Nav_core:**

In the nav_core package in file nav_core/include/base_local_planner.h

1\. Add one public method:



```
void setGlobalCostmap(costmap_2d::Costmap2DROS* global_costmap_ros){
     global_costmap_ros_ = global_costmap_ros;
}
```

 2. Add one protected attribute:



```
costmap_2d::Costmap2DROS* global_costmap_ros_;
```



### Needed Parameters

All .launch and .yaml files can you find in the asr_mild_navigation
package. In the launch and rsc folders. If you allready have launch and
yaml files you can addapt them like descript below.

#### Move_base Parameters

To work correctly the global plan must be calculated periodically. If
the global planner is not updated, the planner will fail.

So you must set the "planner_frequency" at move_base to a number
higher than 0, e.g. 5.

Also, the local planner update frequency must be set higher than 0, e.g.
controller_frequency = 5.

The move_base parameter "base_local_planner" must be set to
"ftc_local_planner/FTCPlanner" in the move_base launch file.

This could look like this:



```
<node name="move_base" pkg="asr_move_base" type="move_base" respawn="false" output="screen">

<param name="controller_frequency" value="5.0"/> <param   name="planner_frequency" value="10"/> <param name="base_local_planner" value="ftc_local_planner/FTCPlanner" />

... yaml files ....

</node>
```

 For example you can look at the launch file
"launch/navigation.launch" in the asr_mild_navigation package.

#### Drive around local obstacles

To drive around local obstacles, with aren't located on the global
costmap you must update the global costmap. You must set the
"update_frequency" higher than 0 in your global_costmap yaml.

Then there are two ways to put a local obstacle into the global costmap:

**1. Activate the obstacle in the global_costmap.yaml:**



```
global_costmap/obstacle_layer:
    enabled: true
```

 **OR**

**2. Set the "join_obstacle" parameter of the ftc_local_planner to
true:**



```
join_obstacle: true
```

 **Don't use both methods together!**

### Start system

You can use the launch files in
[asr_mild_navigation](asr_mild_navigation):

#### Simulation



```
roslaunch asr_mild_navigation simulation_manual_rearranged.launch
```



#### Real



```
roslaunch asr_mild_navigation navigation.launch
```



## ROS Nodes

### Published Topics



```clearsilver
pub {
  no_header=True
  0.name = ~<name>/local_plan
  0.type = nav_msgs/Path
  0.desc = Shows the part of the global plan with is used for velocity calculation.
}
```



### Parameters

These are all the parametes of the planner which you can edit in the
FTCPlanner .yaml:



```clearsilver
param {
  no_header=True
  1.name = ~max_x_vel
  1.type = double
  1.desc = The maximal velocity at forward direction in m/s. The planner tries to reach this velocity as fast as possible.


  2.name = ~max_rotation_vel
  2.type = double
  2.desc = The maximal rotation velocity in rad/s. The planner tries to reach this velocity as fast as possible.

  3.name = ~min_rotation_vel
  3.type = double
  3.desc = The minimal rotation velocity in rad/s. Used to guarantee a rotation towards the goal orientation.

  4.name = ~acceleration_x
  4.type = double
  4.desc = The acceleration limit of the robot in the x direction (m/s^2).

  5.name = ~acceleration_z
  5.type = double
  5.desc = The acceleration limit of the robot for a rotation.

  6.name = ~position_accuracy
  6.type = double
  6.desc = The accuracy of the robot at the goal position. Maximal distance to the goal position in meter.

  7.name = ~rotation_accuracy
  7.type = double
  7.desc = The maximal allowed angle the robot differs from the goal orientation in radian.

  8.name = ~slow_down_factor
  8.type = double
  8.desc = A factor to influence the rotation deceleration. It should compensate inaccuracies at the motor control. If the slow_down_factor > 0 the deceleration starts later.

  9.name = ~sim_time
  9.type = double
  9.desc = The time in seconds to look along the global plan with maximal velocity, to calculate the path.

  10.name = ~local_planner_frequence
  10.type = int
  10.desc = Needs to be set to the same value as the local planner frequency (controller_frequency) in move base.

  11.name = ~join_obstacle
  11.type = bool
  11.desc = If true, local and global costmaps are joined. Local obstacles will be bypassed.

}
```



## Tutorials

<http://wiki.ros.org/asr_ftc_local_planner/SetupNavigationForFTCPlanner>

<http://wiki.ros.org/asr_ftc_local_planner/FindRightParameters>
