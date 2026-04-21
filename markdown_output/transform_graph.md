## Overview

`transform_graph` is a library for computing transformations between
coordinate frames in an arbitrary graph structure.

-   `transform_graph` is not a distributed system. Programmers simply
    create and use the transform_graph graph as an object in memory.
-   `transform_graph` does not keep track of transformations over
    time.
-   The transform graph does not have to be structured in a tree.
    Instead, frames can be arranged in an arbitrary graph (weakly
    connected, cyclic, disconnected, etc.)
-   `transform_graph` does not depend on ROS except to convert from
    common message types. As a result, you do not need to run a ROS
    master to use `transform_graph`, and it is suitable for use in
    pure unit tests.

## Quick start

The library's generated documentation explains how to use
`transform_graph` in detail. Below are a few quick examples
illustrating how it can be used.

`transform_graph::Graph` maintains the graph of transformations and is
the primary interface to transform_graph: 

```cplusplus
#include "transform_graph/transform_graph.h"

int main(int argc, char** argv) {
  transform_graph::Graph graph; 
  return 0;
}
```



Add frames to the graph using `transform_graph::Graph::Add`:


```cplusplus
transform_graph::Graph graph;

geometry_msgs::Pose torso_pose;
pose.position.z = 0.4;
pose.orientation.w = 1;

graph.Add("torso_lift_link", transform_graph::RefFrame("base_link"), torso_pose);
```



Get points in different frames using
`transform_graph::Graph::DescribePosition`. In this example, we want
to know what a point 10 cm in front of the robot's wrist is, expressed
in the base frame: 

```cplusplus
geometry_msgs::Point pt;
pt.x = 0.1;
transform_graph::Transform pt_in_base;
graph.DescribePosition(pt, transform_graph::Source("wrist"), transform_graph::Target("base_link"), &pt_in_base);
Eigen::Vector3d v = pt_in_base.vector();
```


