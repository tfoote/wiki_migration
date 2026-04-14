## Overview

The [phidgets_imu](phidgets_imu) package contains a ROS driver for the
[ Phidgets Spatial 3/3/3](http://www.phidgets.com/products.php?product_id=1044_0 )
IMU sensor. The driver publishes the following data:

![](attachment:imu.png)

-   linear acceleration and angular velocities as
    \<\<MsgLink(sensor_msgs/Imu)\>\>
-   magnetic field as \<\<MsgLink(sensor_msgs/MagneticField)\>\> or as
    \<\<MsgLink(geometry_msgs/Vector3Stamped)\>\> (deprecated)

You can use this driver in conjunction with
[imu_filter_madgwick](imu_filter_madgwick) or a similar IMU filter to
get an estimate for the orientation of the sensor from the fused sensor
readings.

An example
[ launch file](https://github.com/ccny-ros-pkg/phidgets_drivers/blob/master/phidgets_imu/launch/imu.launch )
for using the driver together with a filter is included in the package.

## ROS API

```clearsilver
name = phidgets_imu_node / phidgets_imu_nodelet
desc = The `phidgets_imu_node_node` publishes IMU data from the Phidgets Spatial device.

pub {
   0{
    name = imu/data_raw
    type = sensor_msgs/Imu
    desc = The raw IMU data. Includes linear accelerations and angular velocities, but ***does not*** include orientation.
    }
   1{
    name = imu/mag
    type = geometry_msgs/Vector3Stamped
    desc = The magnetic orientation vector
    }
   2{
    name = imu/is_calibrated
    type = std_msgs/Bool
    desc = Whether the IMU has been calibrated
    }
  }

param{
    0.name = ~frame_id
    0.type = string
    0.default = `"imu"`
    0.desc = The name of the frame attached to the published messages

    1.name = ~period
    1.type = double
    1.default = 8
    1.desc = A period (in ms) which determines the rate at which data is streamed.

    2.name = ~angular_velocity_stdev
    2.type = double
    2.default = 0.000349056
    2.desc = the standard deviation of the angular velocity readings, in rad/s. Default value is 0.000349056 rad/s (= 0.02 °/s), as per manual.
 
    3.name = ~linear_acceleration_stdev
    3.type = double
    3.default = 0.002943
    3.desc = the standard deviation of the linear acceleration readings, in m/s². Default value is 0.002943 m/s² (= 0.0003 g), as per manual.
 
    4.name = ~magnetic_field_stdev
    4.type = double
    4.default = 0.001658
    4.desc = the standard deviation of the magnetic field readings, in radians per second. Default value is 0.001658 rad/s (= 0.095°/s), as per manual.
 }

srv{
  0.name= imu/calibrate
  0.type= std_srvs/Empty
  0.desc= Tells the IMU to (re)calibrate its gyroscope biases. The service call returns once calibration is complete. A message will published to `imu/is_calibrated` for each call to `imu/calibrate`.
}
```
