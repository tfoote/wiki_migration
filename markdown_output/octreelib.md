## Properties

-   The OcTree class is templated for the coordinate type and the value
    type. Each node in the tree contains a value. During the
    construction of a tree, the += operator of the value type is used to
    distribute the value of a point to all its parents in the tree. By
    this, each node in the tree subsumes the values of the subtree below
    itself. For instance, one can use this for fast calculations of
    integral and extremum values.

```{=html}
<!-- -->
```
-   The OcTree class provides methods to apply the value type +=
    operator or other arbitrary operators in box volumes. The box
    operators assume that integral/extremum values already have been
    distributed through the tree such that search can be stopped at
    branching nodes when their volume is fully contained in the search
    query, since their value represents the subtree below the branching
    node. There are also methods to sweep through the tree bottom-up or
    top-down with custom operators.

```{=html}
<!-- -->
```
-   OcTree construction (min. resolution 0.005m, max. range 30m) from a
    640x480 Kinect image takes between 0.15 and 0.25 sec on a HP
    Pavillion dv6 notebook with an Intel Core i7 Q720 CPU.

```{=html}
<!-- -->
```
-   The library supports fast sampling of a point cloud on multiple
    resolutions in parallel (algorithm/downsample.h).

```{=html}
<!-- -->
```
-   The library contains fast computation of normals and curvatures on
    multiple resolutions in parallel in feature/normalestimation.h .

```{=html}
<!-- -->
```
-   OcTree construction (min. resolution 0.005m, max. range 30m) and
    normal estimation on all scales in parallel from a 640x480 Kinect
    image takes between 0.25 and 0.35 sec on a HP Pavillion dv6 notebook
    with an Intel Core i7 Q720 CPU.

```{=html}
<!-- -->
```
-   Fast multiresolution normals can be computed with the
    octreelib/NormalEstimationOctree nodelet. See below for details of
    the nodelet.

![\|Large scale normals](attachment:largescale.png)
![\|Small scale normals](attachment:smallscale.png)

## Getting started

The package contains a launch file that computes multiresolution normals
in a nodelet.



```
$ roslaunch octreelib normalestimation_nodelet.launch
```



The input PointCloud2 topic of the nodelet is mapped to
/camera/depth/points for Kinect depth streams. The launch file also
starts RViz with a proper configuration to visualize output normals from
the PointCloud2 output messages and visualization markers.

## ROS API



```clearsilver
node.0 {
name=normalestimation_nodelet
desc=`normalestimation_nodelet` calculates multiresolution normals on arbitrary point clouds.
sub{
0.name= ~input
0.type= sensor_msgs/PointCloud2
0.desc= The input pointcloud.
}
pub{
0.name= ~output_layerN
0.type= sensor_msgs/PointCloud2
0.desc= A pointcloud containing points of type pcl::PointNormal on resolution layer N. Normals and curvatures are only computed on a layer if the layer topic has been subscribed. 
1.name= ~visualization_marker_array
1.type= visualization_msgs/MarkerArray
1.desc= visualizes normals on each computed (i.e., subscribed) layer with LINE_LIST.
}
param {
0.name= ~fixed_size
0.default= true
0.type= bool
0.desc= preallocate memory for a fixed number of points. Performs re-allocation when the number of points increases
1.name= ~min_resolution
1.default= 0.005
1.type= double
1.desc= minimum resolution of the octree in meters. samples below this resolution are subsumed in leaf nodes.
2.name= ~max_range
2.default= 30.0
2.type= double
2.desc= maximum measurement range
3.name= ~min_points_for_fit
3.default= 25
3.type= int
3.desc= minimum number of points in an octree node required to fit a normal and to compute curvature
}
}
```


