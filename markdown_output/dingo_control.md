## Overview

[Dingo](Robots/Dingo)'s mobility is controlled by
[diff_drive_controller](https://index.ros.org/p/diff_drive_controller)
or
[mecanum_drive_controller](https://index.ros.org/p/mecanum_drive_controller)
depending on the model: Dingo-D is a differential drive robot, while
Dingo-O is an omni-directional robot.

This package contains launchfiles for the elements of Dingo which are
common to simulator and real platform, including controller,
localization, and teleop.
