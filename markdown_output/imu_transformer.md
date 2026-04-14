Please check the for common problems, or open an
[issue](https://github.com/ros-perception/imu_pipeline/issues) if still
unsolved.

This package provides a node/nodelet combination that can be used to
transform IMU data from one TF frame into another. It is a thin wrapper
around a tf2 transform implemented in [tf2_sensor_msgs](tf2_sensor_msgs)
(awaiting <https://github.com/ros/geometry_experimental/pull/78>).

## Node

```clearsilver
node.0 {
 name = imu_transformer_node
 desc = `imu_transformer_node` takes in IMU data (Accelerometer, Magnetometer, Gyroscope, and fused orientation), and transforms it from one frame into another.
 sub{
  0.name= imu_in/data
  0.type= sensor_msgs/Imu
  0.desc= Input IMU data
  1.name= imu_in/mag
  1.type= sensor_msgs/MagneticField
  1.desc= Input magnetometer data. For backwards compatibility, also supports geometry_msgs/Vector3
  }
 pub {
  0.name= imu_out/data
  0.type= sensor_msgs/Imu
  0.desc= Output IMU data
  1.name= imu_out/mag
  1.type= sensor_msgs/MagneticField
  1.desc= Output magnetometer data.
 }
 param {
  0.name= ~target_frame
  0.default= base_link
  0.type= string
  0.desc= Target frame to transform incoming IMU data into.  
 }
}
```

## Nodelet

Same API as node, available as
\`imu_transformer/imu_transformer_nodelet\`.
