## Overview

This package provides an RViz view controller plugin that allows users
to control the RViz camera by publishing `CameraPlacement` messages
(from the
[view_controller_msgs](https://index.ros.org/p/view_controller_msgs)
package) to the `/rviz/camera_placement` topic.

## Installation

This package has been released into Hydro and Indigo. Installation
through `apt-get` is easiest in most cases:

{ }}}} { }}}}

Systems for which no binary packages are available will have to build
from source. See the relevant tutorials for more information.

## Usage

See the `CameraTest`, `ControlsTest` and `SquareTest` scripts in
the [view_controller_msgs](https://index.ros.org/p/view_controller_msgs)
package for examples of how to use the functionality provided by this
package.
