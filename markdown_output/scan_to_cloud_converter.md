## Details

The scan_to_cloud_converter
converts
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
to
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)
messages.

The ouput cloud message has the `is_dense` attribute set to `false`.
Ranges in the scan message which are outside `(min_range, max range)`
are represented by `nan` values in the output cloud.

## Nodes

### scan_to_cloud_converter_node

The `scan_to_cloud_converter` takes in
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
messages and outputs
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)
messages.

#### Subscribed Topics

- `scan`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Input laser scan

#### Published Topics

- `cloud`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  Output cloud

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports and
feature requests.

Please submit your tickets through
[github](https://github.com/ccny-ros-pkg/scan_tools/issues/) (requires
github account) or by emailing the maintainers.
