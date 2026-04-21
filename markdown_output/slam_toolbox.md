## Overview

The Slam Toolbox package incorporates information from laser scanners in
the form of a LaserScan message and TF transforms from odom->base link,
and creates a map 2D map of a space. This package will allow you to
fully serialize the data and pose-graph of the SLAM map to be reloaded
to continue mapping, localize, merge, or otherwise manipulate. We allow
for SLAM Toolbox to be run in synchronous (process all valid sensor
measurements, regardless of lag) and asynchronous (process valid sensors
measurements on an as-possible basis) modes.

You can find a paper about this work
<https://joss.theoj.org/papers/10.21105/joss.02783>.

ROS drop in replacement to gmapping, cartographer, karto, hector, etc
featuring a feature complete SLAM build on the robust scan matcher at
the heart of Karto that's been souped up and sped up for use in this
package. A new optimization plugin based on Google Ceres is also
introduced. We also introduce a new localization method called "elastic
pose-graph localization" that takes a sliding window of measurements
and adds them to the graph to optimize and refine. This allows for the
tracking of local features which have changed in the environment rather
than viewing them as deviations and removes these extra nodes when you
leave an area to not effect the long term map.

This was created in response to inadequate mapping and localization
quality from GMapping, Karto, Cartographer and AMCL in massive and
dynamic indoor environments, though it has been tested and deployed on
sidewalk robots as well.

There is included an RVIZ plugin for interacting with SLAM Toolbox over
ROS topics and services. While it is included as a debug tool, for
production use its recommended to wrap your own operation interface. I
allow for manual pose-graph manipulation through the RVIZ plugin which
works well for small maps. In larger maps, the interactive markers will
overload RVIZ so its mostly useful as a debug instrument in smaller maps
or for introspection. In the interactive pose-graph manipulation mode,
you can move and rotate nodes in the graph, while being displayed the
laser scan of that node to align it better with a loop closure or match,
then rerun the optimizer over that section of the pose-graph. It is also
very useful to rotate maps to be axially aligned.

More information, ROS API, demos, and resources are given in the
[GitHub](https://github.com/SteveMacenski/slam_toolbox) page.

Macenski, S., Jambrecic I., "SLAM Toolbox: SLAM for the dynamic
world", Journal of Open Source Software, 6(61), 2783, 2021.

Macenski, S., "On Use of SLAM Toolbox, A fresh(er) look at mapping and
localization for the dynamic world", ROSCon 2019.
