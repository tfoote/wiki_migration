## Hybrid 3D command

The `hybrid_3d` command reads <<MsgLink(velodyne_common/RawScan)>>
data from the **velodyne/rawscan** topic, identifies drive-able terrain,
and publishes it as <<MsgLink(sensor_msgs/PointCloud)>> in the
**velodyne/hybridcloud** topic.

Usage: 

```
$ rosrun velodyne_hybrid_3d hybrid_3d
```


