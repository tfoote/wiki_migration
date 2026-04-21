This is a C++ library with ROS interface to manage two-dimensional grid
maps with multiple data layers. It is designed for mobile robotic
mapping to store data such as elevation, variance, color, friction
coefficient, foothold quality, surface normal, traversability etc.

Features:

-   **Multi-layered:** Developed for universal 2.5-dimensional grid
    mapping with support for any number of layers.
-   **Efficient map re-positioning:** Data storage is implemented as
    two-dimensional circular buffer. This allows for non-destructive
    shifting of the map\'s position (e.g. to follow the robot) without
    copying data in memory.
-   **Based on Eigen:** Grid map data is stored as
    [Eigen](http://eigen.tuxfamily.org/) data types. Users can apply
    available Eigen algorithms directly to the map data for versatile
    and efficient data manipulation.
-   **Convenience functions:** Several helper methods allow for
    convenient and memory safe cell data access. For example, iterator
    functions for rectangular, circular, polygonal regions and lines are
    implemented.
-   **ROS interface:** Grid maps can be directly converted to and from
    ROS message types such as *PointCloud2*, *OccupancyGrid*,
    *GridCells*, and our custom *GridMap* message.
-   **OpenCV interface:** Grid maps can be seamlessly converted from and
    to OpenCV image types to make use of the tools provided by OpenCV.
-   **Visualizations:** The *grid_map_rviz_plugin* renders grid maps as
    3d surface plots (height maps) in RViz. Additionally, the
    *grid_map_visualization* package helps to visualize grid maps as
    point clouds, occupancy grids, grid cells etc.

More documentation on the grid map library is given
[here](https://github.com/anybotics/grid_map).

![](attachment:grid_map_rviz_plugin_example.png)

\<\<MsgSrvDoc(grid_map_msgs)\>\>

## Reporting bugs

<https://github.com/anybotics/grid_map/issues>
