  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     <#FFFF00> *'This package uses *deprecated'' interfaces, but can be upgraded, if needed. ([velodyne_height_map](velodyne_height_map) is an alternative)   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------- --

## Nodes

### Ring Compression

The `ringcomp` node reads <<MsgLink(velodyne_common/RawScan)>>
data from the **velodyne/rawscan** topic, identifies obstacles, and
publishes them as <<MsgLink(sensor_msgs/PointCloud)>> in the
**velodyne/obstacles** topic.

#### Usage

```
$ rosrun velodyne_ringcomp ringcomp
```

## Nodelets

```clearsilver
node.0 {
 name = ringcomp_nodelet
 desc = The ringcomp nodelet reads transformed data in <<MsgLink(sensor_msgs/PointCloud)>> format including additional channels for `"ring"` and `"heading"`, and republishes detected obstacles as `velodyne/obstacles`.
 sub {
  0.name= velodyne/pointcloud
  0.type= sensor_msgs/PointCloud
  0.desc= Raw Velodyne data points from the device
 }
 pub {
  0.name= velodyne/obstacles
  0.type= sensor_msgs/PointCloud
  0.desc= points belonging to detected obstacles
 }
param {
  4.name= ~min_obstacle
  4.type= double
  4.default= 0.15
  4.desc= minimum height to consider an obstacle (meters)
  5.name= ~vel_height
  5.type= double
  5.default= 2.4
  5.desc= height of the velodyne sensor above the ground (meters)
 }
}
```

#### Examples

Start the ring compression nodelet. *Running as a standalone nodelet
prevents zero-copy message sharing.* ```
$ rosrun nodelet nodelet standalone velodyne_ringcomp/RingCompNodelet
```
