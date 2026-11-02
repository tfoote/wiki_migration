Please check the for common problems, or open an
[issue](https://github.com/ros-perception/imu_pipeline/issues) if still
unsolved.

This package provides a node/nodelet combination that can be used to
transform IMU data from one TF frame into another. It is a thin wrapper
around a tf2 transform implemented in
[tf2_sensor_msgs](https://index.ros.org/p/tf2_sensor_msgs) (awaiting
<https://github.com/ros/geometry_experimental/pull/78>).

## Node

### imu_transformer_node

`imu_transformer_node` takes in IMU data (Accelerometer, Magnetometer,
Gyroscope, and fused orientation), and transforms it from one frame into
another.

#### Subscribed Topics

- `imu_in/data`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Input IMU data
- `imu_in/mag`
  ([sensor_msgs/msg/MagneticField](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/MagneticField.html)):
  Input magnetometer data. For backwards compatibility, also supports
  geometry_msgs/Vector3

#### Published Topics

- `imu_out/data`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Output IMU data
- `imu_out/mag`
  ([sensor_msgs/msg/MagneticField](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/MagneticField.html)):
  Output magnetometer data.

#### Parameters

- `~target_frame` (`string`, default: `base_link`): Target frame to
  transform incoming IMU data into.

## Nodelet

Same API as node, available as
`imu_transformer/imu_transformer_nodelet`.

## Tutorials

- [Validating IMU data](#validating-imu-data):
  Tutorial on checking the consistency of IMU data.

## Validating IMU data

- **Description:** Tutorial on checking the consistency of IMU data.
- **Tutorial Level:** INTERMEDIATE

The quickest way to validate data coming from an IMU driver node is to
transform it into an ENU standard frame (e.g. `base_link`).

1\. Configure your `base_link`->`imu_link` transform
