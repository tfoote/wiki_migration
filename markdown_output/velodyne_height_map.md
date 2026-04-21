## Reporting bugs

-   <https://github.com/jack-oquin/velodyne_height_map/issues>

## ROS Nodes and Nodelets

```clearsilver
node.0 {
 name = HeightMapNodelet
 desc = The height map nodelet reads point cloud data, publishing detected obstacles and clear space. The [[velodyne_pointcloud#TransformNodelet|velodyne_pointcloud/TransformNodelet]] publishes data in the appropriate format.
 sub {
  0.name= velodyne_points
  0.type= sensor_msgs/PointCloud2
  0.desc= 3D data points.
 }
 pub {
  0.name= velodyne_obstacles
  0.type= sensor_msgs/PointCloud2
  0.desc= Points belonging to detected obstacles.
  1.name= velodyne_clear
  1.type= sensor_msgs/PointCloud2
  1.desc= Clear space: grid squares containing laser returns and no obstacle.
 }
param {
  1.name= cell_size
  1.type= double
  1.default= 0.5
  1.desc= Grid cell size (meters).
  4.name= full_clouds
  4.type= bool
  4.default= false
  4.desc=  Normally, height map only publishes one obstacle or clear point for each cell, significantly reducing output bandwidth while providing the information needed for most 2D navigation. When `true`, publish all obstacle and clear points.
  5.name= grid_dimensions
  5.type= int
  5.default= 320
  5.desc= Number of grid cells in both the X and Y dimensions.
  6.name= height_threshold
  6.type= double
  6.default= 0.25
  6.desc= Minimum height difference that counts as an obstacle (meters).
 }
}
```

#### Examples

Start the height map nodelet in a separate process. *Running as a
standalone nodelet prevents zero-copy message sharing.*
```
$ rosrun nodelet nodelet standalone velodyne_height_map/HeightMapNodelet
```

This launch file runs the height map nodelet in the same process with
the Velodyne device driver and a
[velodyne_pointcloud](velodyne_pointcloud) nodelet which publishes the
points transformed into the \"/odom\" frame. *This approach minimizes
data copying.*

```
<launch>

  <!-- start nodelet manager and driver nodelets -->
  <include file="$(find velodyne_driver)/launch/nodelet_manager.launch">
    <arg name="pcap"
           value="$(find velodyne_pointcloud)/tests/class.pcap"/>
  </include>

  <!-- start transform nodelet using test calibration file -->
  <include file="$(find velodyne_pointcloud)/launch/transform_nodelet.launch">
    <arg name="calibration"
         value="$(find velodyne_pointcloud)/tests/angles.config"/>
  </include>

  <!-- start heightmap nodelet -->
  <include file="$(find velodyne_height_map)/launch/heightmap_nodelet.launch"/>

</launch>
```

```clearsilver
node.0 {
 name = heightmap_node
 desc = The height map node works exactly like the [[#HeightMapNodelet|HeightMapNodelet]], running as a separate ROS node. All topics and parameters are identical.
}
```

#### Examples

Run the height map algorithm as a separate node.
```
$ rosrun velodyne_height_map heightmap_node
```

Run the node with a 100x100 grid of 10cm cells. ```
$ rosrun velodyne_height_map heightmap_node _grid_dimensions:=100 _cell_size:=0.1
```

Run the node with anything more than 5cm high considered an obstacle.
```
$ rosrun velodyne_height_map heightmap_node _height_threshold:=0.05
```
