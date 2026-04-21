![\|height=\"200\",width=\"333\"](attachment:Logo-white-medium.jpg)

# Description

This package generates a grid of points to cover the map. The grid can
be used as basis to create camera_poses to search the room with the
asr_direct_search_manager.

# Functionality

The grid consists of grid points. Each grid point represents a positon
on the map. A grid point can be reached by the robot or not if it is on
a static obstacle. There are different parameters to adjust the grid on
the map. It is possible to assign a range for some parameters. For each
combination a grid will be generated and the one with the most grid
points will be outputted. At the end the grid points will be sorted with
TSP (nearest_neighbour and two_opt).

![\|height=\"400\",width=\"450\"](attachment:grid_simulated.png)

# Usage

The asr_robot_model_services has to be run.

## Needed packages

ros-kinetic-move-base

asr_robot_model_services

## Start system

roslaunch asr_robot_model_services !RobotModelServiceSim.launch

roslaunch asr_grid_creator grid_creator.launch

# ROS Nodes

## Published Topics

**direct_search/grid_visualization** (!MarkerArray): Visualisation of
the grid

## Parameters

### Launch file

**asr_grid_creator/launch/grid_creator.launch **

**ExitXML: **The path to a file where the generated grid should be saved

### yaml file

**asr_grid_creator/param/labor_param.yaml**

**width: **the width of the grid **height:** the hieght of the grid
!**GridType**: the shape of each *grid point.* It can be Hex or Quad
!**HamiltonCycle**: if the generated positions should make a
[HamiltonCycle](http://i61pc053.itec.uni-karlsruhe.de/twiki/bin/edit/IlcasProjects/HamiltonCycle?topicparent=IlcasProjects.AsrGridCreator;nowysiwyg=0)
or not **startX/startY**: start postition of the robot (for sorting the
postitions)

!**StepSize(Min/Max/Step)**: the size of each cell or rather the half of
the distance between two neighbors of *grid points*
**Htrans(Min/Max/Step)**: horizontal translation offset applied to the
grid **Vtrans(Min/Max/Step)**: vertical translation offset applied to
the grid **Offset(Min/Max/Step)**: rotation offset applied to the grid

The (**Min/Max/Step**) defines the ranges in which the generation took
place. The best one will be saved at the end. The best grid is the one
with the most *grid points*.

## Needed Services

asr_robot_model_services: IsPositionAllowed, !GetDistance

# Tutorials

The generation of the grid is part of the
[AsrDirectSearchManagerTutorialGrid](http://wiki.ros.org/asr_direct_search_manager/AsrDirectSearchManagerTutorialGrid).
