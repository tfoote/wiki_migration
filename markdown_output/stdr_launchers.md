# Overview

The **stdr_launchers** package provides ROS launchers for the basic
[STDR Simulator](stdr_simulator) functionalities. Specifically the
launchers available are:

## server_no_map.launch

Initializes a bare [stdr_server](stdr_server).

## server_with_map.launch

Initializes an [stdr_server](stdr_server) and automatically loads the
**sparse_obstacles** map (found in the [stdr_resources](stdr_resources)
package).

## server_with_map_and_gui.launch

Initializes an [stdr_server](stdr_server) and automatically loads the
**sparse_obstacles** map (found in the [stdr_resources](stdr_resources)
package. Also an instance of [stdr_gui](stdr_gui) is executed.

## server_with_map_and_gui_plus_robot.launch

Initializes an [stdr_server](stdr_server) and automatically loads the
**sparse_obstacles** map (see [stdr_resources](stdr_resources)). Also an
instance of [stdr_gui](stdr_gui) is executed. Finally a robot of type
**pandora_robot** (see [stdr_resources](stdr_resources)) is spawned in
the map.

## rviz.launch

Wrapper launcher for the [ROS rviz](rviz), modified so that the
essential information about [STDR Simulator](stdr_simulator) are
visible.
