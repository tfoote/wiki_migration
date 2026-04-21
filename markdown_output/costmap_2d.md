## Overview

![\|width="100%"](attachment:costmap_rviz.png) *Note: In the picture
above, the red cells represent obstacles in the costmap, the blue cells
represent obstacles inflated by the inscribed radius of the robot, and
the red polygon represents the footprint of the robot. For the robot to
avoid collision, the footprint of the robot should never intersect a red
cell and the center point of the robot should never cross a blue cell.*

The `costmap_2d` package provides a configurable structure that
maintains information about where the robot should navigate in the form
of an occupancy grid. The costmap uses sensor data and information from
the static map to store and update information about obstacles in the
world through the `costmap_2d::Costmap2DROS` object. The
`costmap_2d::Costmap2DROS` object provides a purely two dimensional
interface to its users, meaning that queries about obstacles can only be
made in columns. For example, a table and a shoe in the same position in
the XY plane, but with different Z positions would result in the
corresponding cell in the `costmap_2d::Costmap2DROS` object's costmap
having an identical cost value. This is designed to help planning in
planar spaces.

As of the Hydro release, the underlying methods used to write data to
the costmap is fully configurable. Each bit of functionality exists in a
layer. For instance, the static map is one layer, and the obstacles are
another layer. By default, the obstacle layer maintains information
three dimensionally (see [voxel_grid](voxel_grid)). Maintaining 3D
obstacle data allows the layer to deal with marking and clearing more
intelligently.

The main interface is `costmap_2d::Costmap2DROS` which maintains much
of the ROS related functionality. It contains a
`costmap_2d::LayeredCostmap` which is used to keep track of each of
the layers. Each layer is instantiated in the `Costmap2DROS` using
[pluginlib](pluginlib) and is added to the `LayeredCostmap`. The
layers themselves may be compiled individually, allowing arbitrary
changes to the costmap to be made through the C++ interface. The
`costmap_2d::Costmap2D` class implements the basic data structure for
storing and accessing the two dimensional costmap.

The details about how the Costmap updates the occupancy grid are
described below, along with links to separate pages describing how the
individual layers work.

## Marking and Clearing

The costmap automatically subscribes to sensors topics over ROS and
updates itself accordingly. Each sensor is used to either mark (insert
obstacle information into the costmap), clear (remove obstacle
information from the costmap), or both. A marking operation is just an
index into an array to change the cost of a cell. A clearing operation,
however, consists of raytracing through a grid from the origin of the
sensor outwards for each observation reported. If a three dimensional
structure is used to store obstacle information, obstacle information
from each column is projected down into two dimensions when put into the
costmap.

## Occupied, Free, and Unknown Space

While each cell in the costmap can have one of 255 different cost values
(see the [inflation](#Inflation) section), the underlying structure that
it uses is capable of representing only three. Specifically, each cell
in this structure can be either free, occupied, or unknown. Each status
has a special cost value assigned to it upon projection into the
costmap. Columns that have a certain number of occupied cells (see
[mark_threshold](costmap_2d/hydro/obstacles#VoxelCostmapPlugin)
parameter) are assigned a `costmap_2d::LETHAL_OBSTACLE` cost, columns
that have a certain number of unknown cells (see
[unknown_threshold](#Map_type_parameters) parameter) are assigned a
`costmap_2d::NO_INFORMATION` cost, and other columns are assigned a
`costmap_2d::FREE_SPACE` cost.

## Map Updates

The costmap performs map update cycles at the rate specified by the
[update_frequency](#Rate_parameters) parameter. Each cycle, sensor data
comes in, marking and clearing operations are perfomed in the underlying
occupancy structure of the costmap, and this structure is projected into
the costmap where the appropriate cost values are assigned as described
[above](#Occupied.2C_Free.2C_and_Unknown_Space). After this, each
obstacle inflation is performed on each cell with a
`costmap_2d::LETHAL_OBSTACLE` cost. This consists of propagating cost
values outwards from each occupied cell out to a user-specified
inflation radius. The details of this inflation process are outlined
[below](#Inflation).

## tf

In order to insert data from sensor sources into the costmap, the
`costmap_2d::Costmap2DROS` object makes extensive use of [tf](tf).
Specifically, it assumes that all transforms between the coordinate
frames specified by the
[global_frame](#Coordinate_frame_and_tf_parameters) parameter, the
[robot_base_frame](#Coordinate_frame_and_tf_parameters) parameter, and
sensor sources are connected and up-to-date. The
[transform_tolerance](#Coordinate_frame_and_tf_parameters) parameter
sets the maximum amount of latency allowed between these transforms. If
the [tf](tf) tree is not updated at this expected rate, the
[navigation stack](navigation) stops the robot.

## Inflation

![\|width="100%"](attachment:costmapspec.png)

Inflation is the process of propagating cost values out from occupied
cells that decrease with distance. For this purpose, we define 5
specific symbols for costmap values as they relate to a robot.

-   "Lethal" cost means that there is an actual (workspace) obstacle
    in a cell. So if the robot's center were in that cell, the robot
    would obviously be in collision.

```{=html}
<!-- -->
```
-   "Inscribed" cost means that a cell is less than the robot's
    inscribed radius away from an actual obstacle. So the robot is
    certainly in collision with some obstacle if the robot center is in
    a cell that is at or above the inscribed cost.

```{=html}
<!-- -->
```
-   "Possibly circumscribed" cost is similar to "inscribed", but
    using the robot's circumscribed radius as cutoff distance. Thus, if
    the robot center lies in a cell at or above this value, then it
    depends on the orientation of the robot whether it collides with an
    obstacle or not. We use the term "possibly" because it might be
    that it is not really an obstacle cell, but some user-preference,
    that put that particular cost value into the map. For example, if a
    user wants to express that a robot should attempt to avoid a
    particular area of a building, they may inset their own costs into
    the costmap for that region independent of any obstacles. Note, that
    although the value is 128 is used as an example in the diagram
    above, the true value is influenced by both the inscribed_radius and
    inflation_radius parameters as defined in the
    [code](https://github.com/ros-planning/navigation/blob/jade-devel/costmap_2d/include/costmap_2d/inflation_layer.h#L113).

```{=html}
<!-- -->
```
-   "Freespace" cost is assumed to be zero, and it means that there is
    nothing that should keep the robot from going there.

```{=html}
<!-- -->
```
-   "Unknown" cost means there is no information about a given cell.
    The user of the costmap can interpret this as they see fit.

```{=html}
<!-- -->
```
-   All other costs are assigned a value between "Freespace" and
    "Possibly circumscribed" depending on their distance from a
    "Lethal" cell and the decay function provided by the user.

The rationale behind these definitions is that we leave it up to planner
implementations to care or not about the exact footprint, yet give them
enough information that they can incur the cost of tracing out the
footprint only in situations where the orientation actually matters.

## Map Types

There are two main ways to initialize a `costmap_2d::Costmap2DROS`
object. The first is to seed it with a user-generated static map (see
the [map_server](map_server) package for documentation on building a
map). In this case, the costmap is initialized to match the width,
height, and obstacle information provided by the static map. This
configuration is normally used in conjunction with a localization
system, like [amcl](amcl), that allows the robot to register obstacles
in the map frame and update its costmap from sensor data as it drives
through its environment.

The second way to initialize a `costmap_2d::Costmap2DROS` object is to
give it a width and height and to set the
[rolling_window](#Map_management_parameters) parameter to be true. The
[rolling_window](#Map_management_parameters) parameter keeps the robot
in the center of the costmap as it moves throughout the world, dropping
obstacle information from the map as the robot moves too far from a
given area. This type of configuration is most often used in an
odometric coordinate frame where the robot only cares about obstacles
within a local area.

## Component API



```wiki
<<Version(ROS hydro)>>
[[Included page costmap_2d/layered not found]]
```


