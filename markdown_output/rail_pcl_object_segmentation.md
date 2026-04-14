This package provides an implementation of object and surface extraction
from a point cloud using the Point Cloud Library ([pcl_ros](pcl_ros)).
It is based on the
[Euclidean Cluster Extraction tutorial](http://www.pointclouds.org/documentation/tutorials/cluster_extraction.php)
on pcl.org.

Facilities for extracting objects, measuring their apparent size,
distance from the coordinate frame origin, and color, and filtering by
these attributes are provided. In addition, this package also provides
facilities for discovering surfaces and filtering out those which do not
appear level with respect to the x-y plane. See the Code API for more
information about these and how to use them.

For convenience, a ROS service and a handful of command line tools are
provided.

## Example

Given the example input point cloud captured with a Microsoft Kinect:

![Example Point Cloud\|width=100%](attachment:original.png)

The following objects are discovered, filtering by objects with a
minimum bounding sphere radius in \[3cm, 5cm\]:

![Discovered Object Clouds, Original Color, Filtered by Size\|width=100%](attachment:3-5cm_radius_objects_color_diluted.png)

And the following level planes are discovered:

![Discovered Surfaces, Artificial Color, Non-Level Surfaces Removed\|width=100%](attachment:level_planes_recolored_diluted.png)

Your mileage may vary. See the Code API for parameters that can be tuned
for best results.

## Services

### Object Extraction - provided by extract_objects_srv

This service provides a convenient implementation of object and surface
discovery in accordance with !ExtractObjects.srv. A caller may specify
the minimum and maximum acceptable bounding sphere radii and the minimum
and maximum acceptable distances from the origin for discovered objects,
as well as the acceptable tolerance for determining whether a surface is
level. Given a sensor_msgs/PointCloud2 to process, the satisfactory
objects and surfaces are returned.

## Nodes

### extract_objects_srv

Provides an implementation of !ExtractObjects.srv using the
object/surface discovery and filtering primitives provided by this
package.

This service always assumes the name \"extract_objects\" in ROS.

#### Parameters

No parameters are accepted at this time.

## Command-line Tools

### extract_objects

This tool extracts objects from a given .pcd point cloud file and saves
the resulting objects as \"object\_\*.pcd\" with unique numbers in the
current working directory. Run the tool with no arguments for additional
usage information.

### extract_objects_rgb

This tool provides the same functionality as extract_objects, but
preserves RGB information if it is available in the given input .pcd
file.

### measure_objects

Given one or more .pcd point clouds to process, this tool prints out:

-   The number of points in each given point cloud
-   The centroid of each given point cloud, as (x, y, z)
-   The minimum bounding sphere radius of each given point cloud

### measure_objects_rgb

This tool provides the same functionality as measure_objects, but for
point clouds with RGB color information available.

In addition to the information printed by measure_objects,
measure_objects_rgb also produces:

-   The average hue of all points in each given point cloud
