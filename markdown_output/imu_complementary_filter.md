## Details

## Supported devices

The filter should be general enough to use with any IMU which publishes
angular velocities and linear accelerations (and optionally magnetic
filed).

It has been tested with:

[Phidgets Spatial 3/3/3](http://www.phidgets.com/products.php?product_id=1056_0)

[Xsense MTx](https://www.xsens.com/products/mtx/)

## Example

Here's an example of the filter in operation:

[Youtube](https://www.youtube.com/watch?v=RmWpire__Zw)

## ROS API

### complementary_filter_node

#### Subscribed Topics

- `imu/data_raw`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Message containing raw IMU data, including angular velocities and
  linear accelerations.
- `imu/mag`
  ([sensor_msgs/msg/MagneticField](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/MagneticField.html)):
  \[optional\] Magnetic field vector

#### Published Topics

- `imu/data`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  The fused Imu message, containing the orientation.
- `imu/rpy/filtered`
  ([geometry_msgs/msg/Vector3](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3.html)):
  *Debug only:* The roll, pitch and yaw angles corresponding to the
  orientation published on the `imu_data` topic. (only published when
  `publish_debug_topics` == true)
- `imu/steady_state`
  ([std_msgs/msg/Bool](https://docs.ros.org/en/rolling/p/std_msgs/msg/Bool.html)):
  *Debug only:* Whether we are in the steady state when doing bias
  estimation. (only published when `publish_debug_topics` == true)

#### Parameters

##### Not Dynamically Reconfigurable Parameters

- `~gain_acc` (`double`, default: `0.01`): Gain for the complementary
  filter, belongs in \[0, 1\].
- `~gain_mag` (`double`, default: `0.01`): Gain for the complementary
  filter, belongs in \[0, 1\].
- `~bias_alpha` (`double`, default: `0.01`): Bias estimation gain,
  belongs in \[0, 1\].
- `~do_bias_estimation` (`bool`, default: `true`): Whether to do bias
  estimation of the angular velocity (gyroscope readings) or not.
- `~do_adaptive_gain` (`bool`, default: `true`): Whether to do
  adaptive gain or not.
- `~use_mag` (`bool`, default: `false`): Whether to use the magnetic
  field data in the data fusion.
- `~fixed_frame` (`string`, default: `odom`): The parent frame to be
  used in `publish_tf`.
- `~publish_tf` (`bool`, default: `false`): Whether to publish a TF
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

#### Provided tf Transforms

- `fixed_frame` → `imu_frame`: Only for debug purposes! This is a
  transform from the fixed frame (specified in the parameter
  `fixed_frame`, default: "odom") to the `header.frame_id` frame
  from the incoming imu messages. Only the rotation is valid.

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports and
feature requests.
