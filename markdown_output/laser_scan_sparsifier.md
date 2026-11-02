## Details

The laser_scan_sparsifier package
is used to downsample
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
messages.

## Nodes & Nodelets

Two drivers are available: `laser_scan_sparsifier_nodelet` and
`laser_scan_sparsifier_node`. Their parameters and topics are
identical.

### laser_scan_sparsifier_node / laser_scan_sparsifier_nodelet

The `laser_scan_sparsifier` takes in
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
messages, and downsamples it by a given step size.

#### Subscribed Topics

- `scan`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Input scan

#### Published Topics

- `scan_sparse`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Output scan

#### Parameters

- `~step` (`int`, default: `2`): Step size for decimation (must be >
  0). A step size of 1 means the output scan will be the same as the
  input scan. A step size of 2 means the output scan will be half the
  input scan, etc.

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports and
feature requests.

Please submit your tickets through
[github](https://github.com/ccny-ros-pkg/scan_tools/issues/) (requires
github account) or by emailing the maintainers.
