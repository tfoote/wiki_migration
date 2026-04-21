## Overview

This package provides ability to drive Care-O-bot using interactive
markers directly from RViz.

![\|width=90%](attachment:ros_cob_marker_teleop.png)

## System architecture

The package consists of the following components:

-   COB teleop interactive marker

## ROS API

Brief description of provided ROS services, published topics, etc.

### Nodes

An overview of all newly created ROS nodes:

  -- ----------------------- -- ---------------------- -- ---------------------------------------------------------- --
     **Node Name**              **Published Topics**      **Description**                                            
     but_cob_teleop_marker      \-                        This node publishes interactive markers for driving COB.   
  -- ----------------------- -- ---------------------- -- ---------------------------------------------------------- --

## Usage

### How to launch COB interactive teleop

1\. Run COB simulation ```
roslaunch cob_bringup_sim robot.launch
``` 2. Run cob marker teleop
node ```
roslaunch cob_interactive_teleop interactive_teleop.launch
``` 3. Start preconfigured RViz
```
roslaunch cob_interactive_teleop rviz.launch
``` 4. Setup RViz:

-   Switch to **Interaction mode**

### How to control robot using the marker

-   Driving forward and backward is done using red arrows.
-   Strafe to the left and to the right is done using green arrows.
-   Rotating is done using blue disc.
-   You can also drive to specified position by moving with the yellow
    circle.
