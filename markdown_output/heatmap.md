## Overview

This package allows you to automatically build visual WiFi heatmaps.

### Functionality

The heatmap package allows the user to select a previously recorded map
(e.g. by gmapping) and define a measurement area on it. Then a coverage
path gets planned and the robot takes Wifi signal strength samples while
covering the area. These samples are visualized in RViz. On its way the
robot uses the navigation_stack to avoid ostacles in the measuring area.
When robot is done the package offers the possibility to do an
interpolation to get a continuous heatmap from the scattered samples.

### Requirements

The only hardware requirements are a mobile robot platform supporting
move_base and a WiFi device.

### Example

ToDo
