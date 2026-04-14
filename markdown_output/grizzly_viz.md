## Overview

This package provides launchers and [rviz](rviz) configurations to
assist with visualizing real or simulated [Grizzly](Robots/Grizzly) from
a desktop environment.

For more information on simulating Grizzly, see
[grizzly_simulator](grizzly_simulator).

## Usage

### View Model

To view the Grizzly model and TF transform tree in isolation,
\'\'\'disconnected\'\'\' from a real or simulated robot, use the
following launcher:

```
roslaunch grizzly_viz view_model.launch
```

You can change joint positions using joint state publisher gui:

![\|width=400](attachment:rviz_screenshot.png)
![\|width=250](attachment:joint-publisher.png)

### View Robot

To visualize a real or simulated Grizzly, launch:

```
roslaunch grizzly_viz view_robot.launch
```

You can click the [Interact](interactive_markers) button in rviz, and
use the interactive markers to give Grizzly some motion commands:

![\| width=500](attachment:rviz_view_robot.png )
