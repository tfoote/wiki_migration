## Hybrid 3D command

The `hybrid_3d` command reads
[velodyne_common/msg/RawScan](https://docs.ros.org/en/rolling/p/velodyne_common/msg/RawScan.html)
data from the **velodyne/rawscan** topic, identifies drive-able terrain,
and publishes it as
[sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html)
in the **velodyne/hybridcloud** topic.

Usage: 

```
$ rosrun velodyne_hybrid_3d hybrid_3d
```


