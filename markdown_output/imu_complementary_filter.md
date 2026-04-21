## Details

## Supported devices

The filter should be general enough to use with any IMU which publishes
angular velocities and linear accelerations (and optionally magnetic
filed).

It has been tested with:

[ Phidgets Spatial 3/3/3](http://www.phidgets.com/products.php?product_id=1056_0 )

[ Xsense MTx](https://www.xsens.com/products/mtx/ )

## Example

Here's an example of the filter in operation:

[Youtube](https://www.youtube.com/watch?v=RmWpire__Zw)

## ROS API

### complementary_filter_node

```clearsilver
sub {
   0{
    name = imu/data_raw
    type = sensor_msgs/Imu
    desc = Message containing raw IMU data, including angular velocities and linear accelerations.
    }
   1{
    name = imu/mag
    type = sensor_msgs/MagneticField
    desc = [optional] Magnetic field vector
    }
  }
 pub {
   0{
    name = imu/data
    type = sensor_msgs/Imu
    desc = The fused Imu message, containing the orientation.
   }
   1{
    name = imu/rpy/filtered
    type = geometry_msgs/Vector3
    desc = ''Debug only:'' The roll, pitch and yaw angles corresponding to the orientation published on the `imu_data` topic. (only published when `~publish_debug_topics` == true)
   }
   2{
    name = imu/steady_state
    type = std_msgs/Bool
    desc = ''Debug only:'' Whether we are in the steady state when doing bias estimation. (only published when `~publish_debug_topics` == true)
   }
  }
  param {
    group.0 {
      name=Not Dynamically Reconfigurable Parameters

      0.name = ~gain_acc
      0.type = double
      0.default = 0.01
      0.desc = Gain for the complementary filter, belongs in [0, 1].

      1.name = ~gain_mag
      1.type = double
      1.default = 0.01
      1.desc = Gain for the complementary filter, belongs in [0, 1].

      2.name = ~bias_alpha
      2.type = double
      2.default = 0.01
      2.desc = Bias estimation gain, belongs in [0, 1].

      3.name = ~do_bias_estimation
      3.type = bool
      3.default = `true`
      3.desc = Whether to do bias estimation of the angular velocity (gyroscope readings) or not.

      4.name = ~do_adaptive_gain
      4.type = bool
      4.default = `true`
      4.desc = Whether to do adaptive gain or not.

      5.name = ~use_mag
      5.type = bool
      5.default = `false`
      5.desc = Whether to use the magnetic field data in the data fusion.

      6.name = ~fixed_frame
      6.type = string
      6.default = `odom`
      6.desc = The parent frame to be used in `publish_tf`.

      7.name = ~publish_tf
      7.type = bool
      7.default = `false`
      7.desc = Whether to publish a TF transform that represents the orientation of the IMU, using the frame specified in `fixed_frame` as the parent frame and the frame given in the input imu message as the child frame.

      8.name = ~reverse_tf
      8.type = bool
      8.default = `false`
      8.desc = If set to `true`, publish transforms from `imu_frame` to `fixed frame` instead of the other way around.

      9.name = ~constant_dt
      9.type = double
      9.default = 0.0
      9.desc = The dt to use; if 0.0 (default), compute dt dynamically from message headers.

      10.name = ~publish_debug_topics
      10.type = bool
      10.default = `false`
      10.desc = If set to `true`, publish a couple of debug topics.
    }
  }
  prov_tf {
    0.from = fixed_frame
    0.to   = imu_frame
    0.desc = Only for debug purposes! This is a transform from the fixed frame (specified in the parameter `fixed_frame`, default: "odom") to the `header.frame_id` frame from the incoming imu messages. Only the rotation is valid.
  }
```

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports and
feature requests.

<<GitHubIssues(CCNYRoboticsLab/imu_tools)>>
