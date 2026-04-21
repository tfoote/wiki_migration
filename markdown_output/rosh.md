## Overview

[rosh](rosh) is a Python-based shell and runtime environment for ROS. It
leverages the IPython shell environment to provide tab-completion
introspection across various ROS APIs, like topics, services,
parameters, and nodes. It is similar to using tools like
[rostopic](rostopic) and [rosservice](rosservice), but with Pythonic
semantics and the convenience of a Python interpreter. You can also
develop ROS nodes using rosh, which we call "roshlets".

## Setup and Install

Please see the [installation instructions](/Install).

## Run

```
rosrun rosh rosh
```

## Using

See [ROSH Overview](rosh/Overview)

## Cookbook

See [Cookbook](/Cookbook)

## Customize

In order customize your default `rosh` shell, you can write a
[roshrc file](/roshrc).

## plugins

-   [rosh_common](rosh_common) (unstable)
-   actions
-   cameras
-   [rosh_geometry](rosh_geometry) (unstable)
-   transforms
-   [rosh_visualization](rosh_visualization) (unstable)
-   `show(cameras.camera)`
-   [rosh_robot](rosh_robot): meta-plugin that loads
    [rosh_common](rosh_common) and [rosh_geometry](rosh_geometry)
-   [rosh_desktop](rosh_desktop): meta-plugin that loads
    [rosh_visualization](rosh_visualization), [rosh_common](rosh_common)
    and [rosh_geometry](rosh_geometry)

## Development Status

-   [rosh](rosh): API reviewed, stable.
-   [rosh_common](rosh_common): unstable (part of `rosh_robot`).
    Integrated with actionlib,
-   [rosh_geometry](rosh_geometry): unstable (part of `rosh_robot`).
    Developing APIs for [tf](tf) and [geometry_msgs](geometry_msgs)
-   [rosh_visualization](rosh_visualization):

## TODO

See [TODO list](/TODO).
