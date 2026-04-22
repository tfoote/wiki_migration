## Details

The [scan_to_cloud_converter](scan_to_cloud_converter) converts
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
to
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)
messages.

The ouput cloud message has the `is_dense` attribute set to `false`.
Ranges in the scan message which are outside `(min_range, max range)`
are represented by `nan` values in the output cloud.

## Nodes



```clearsilver
 name = scan_to_cloud_converter_node
 desc = The `scan_to_cloud_converter` takes in <<MsgLink(sensor_msgs/LaserScan)>> messages and outputs <<MsgLink(sensor_msgs/PointCloud2)>> messages.
sub {
   0{
    name = scan
    type = sensor_msgs/LaserScan
    desc = Input laser scan
    }
}
pub {
   0{
    name = cloud
    type = sensor_msgs/PointCloud2
    desc = Output cloud
   }
  }
```



## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports and
feature requests.

Please submit your tickets through
[github](https://github.com/ccny-ros-pkg/scan_tools/issues/) (requires
github account) or by emailing the maintainers.
