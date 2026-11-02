## Details

The imu_filter_madgwick package is
used to filter and fuse raw data from IMU devices. It fuses angular
velocities, accelerations, and (optionally) magnetic readings from a
generic IMU device into an orientation quaternion, and publishes the
fused data on the `imu/data` topic. The package has been tested using
the raw data output of a Phidgets IMU (Spatial 3/3/3) device. The
package is a wrapper of Sebastian Madgwick's IMU filter \[1\].

## Supported devices

The filter should be general enough to use with any IMU which publishes
angular velocities and linear accelerations (and optionally magnetic
field).

It has been tested with:

[Phidgets Spatial 3/3/3](http://www.phidgets.com/products.php?product_id=1056_0)

## Example

Here's an example of the non-ROS version of the code, courtesy of
Sebastian Madgwick.

[Youtube](https://www.youtube.com/watch?v=BXsGWoOMtmU)

Todo: similar video from rviz.

## ROS API

Two drivers are available: `imu_filter_node` and
`imu_filter_nodelet`. Their parameters and topics are identical.

#### Subscribed Topics

- `imu/data_raw`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Message containing raw IMU data, including angular velocities and
  linear accelerations.
- `imu/mag`
  ([sensor_msgs/msg/MagneticField](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/MagneticField.html)):
  \[optional\] Magnetic field vector; the type is either
  `sensor_msgs/MagneticField` or `geometry_msgs/Vector3Stamped`
  (deprecated), depending on the parameter `use_magnetic_field_msg`
  (see below)

#### Published Topics

- `imu/data`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  The fused Imu message, containing the orientation.

#### Parameters

##### Dynamically Reconfigurable Parameters

See the
[dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure)
package for details on dynamically reconfigurable parameters.

- `~gain` (`double`, default: `0.1`): Gain of the filter. Higher values
  lead to faster convergence but more noise. Lower values lead to slower
  convergence but smoother signal. Range: 0.0 to 1.0
- `~zeta` (`double`, default: `0.0`): Gyro drift gain (approx. rad/s).
  Range: -1.0 to 1.0
- `~mag_bias_x` (`double`, default: `0.0`): Magnetometer bias (hard iron
  correction), x component. Range: -10.0 to 10.0
- `~mag_bias_y` (`double`, default: `0.0`): Magnetometer bias (hard iron
  correction), y component. Range: -10.0 to 10.0
- `~mag_bias_z` (`double`, default: `0.0`): Magnetometer bias (hard iron
  correction), z component. Range: -10.0 to 10.0
- `~orientation_stddev` (`double`, default: `0.0`): Standard deviation
  of the orientation estimate. Range: 0.0 to 1.0

##### Not Dynamically Reconfigurable Parameters

- `~world_frame` (`string`, default: `"nwu"` for Indigo - Kinetic,
  `"enu"` for Lunar+): The world frame with respect to which the
  orientation is indicated (see
  [REP-145](https://github.com/paulbovbel/rep/blob/5b0c670130da8222ab28d5aba75dce5a26442ffe/rep-0145.rst)).
  For historic reasons, the old default is "nwu" (North-West-Up). New
  deployments should use "enu". Valid values: "nwu", "enu",
  "ned".
- `~use_mag` (`bool`, default: `true`): Whether to use the magnetic
  field data in the data fusion.
- `~use_magnetic_field_msg` (`bool`, default: `false` for Hydro and
  Indigo, `true` for Jade+): If set to `true`, subscribe to the
  `/imu/mag` topic as a `sensor_msgs/MagneticField`; if set to
  `false` (deprecated), use `geometry_msgs/Vector3Stamped`.
- `~fixed_frame` (`string`, default: `odom`): The parent frame to be
  used in `publish_tf`.
- `~publish_tf` (`bool`, default: `true`): Whether to publish a TF
  transform that represents the orientation of the IMU, using the frame
  specified in `fixed_frame` as the parent frame and the frame given
  in the input imu message as the child frame.
- `~reverse_tf` (`bool`, default: `false`): If set to `true`,
  publish transforms from `imu_frame` to `fixed frame` instead of
  the other way around.
- `~constant_dt` (`double`, default: `0.0`): The dt to use; if 0.0
  (default), compute dt dynamically from message headers.
- `~publish_debug_topics` (`bool`, default: `false`): If set to
  `true`, publish a couple of debug topics.
- `~stateless` (`bool`, default: `false`): If set to `true`, don't
  publish a filtered orientation. Instead, publish the stateless
  estimate of the orientation based on the latest accelerometer (and
  optionally magnetometer) readings alone. Useful for debugging.
- `~remove_gravity_vector` (`bool`, default: `false`): If set to
  `true`, subtract the gravity vector from the `acceleration` field
  in the published IMU message.

## References

\[1\] <http://www.x-io.co.uk/open-source-imu-and-ahrs-algorithms/>

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports and
feature requests.
