# USB Output 9-axis IMU sensor module

![\|align="right",width="250"](attachment:9axis_imu.png)

[USB Output 9-axis IMU sensor module](https://www.rt-net.jp/products/9axisimu2?lang=en)
contains a 9-axis sensor (Accelerometer + Gyro + Compass) IC MPU9250
made by Inven Sense Corp.

## Feature

- Can receive sensor values from the module with micro USB
- Open source Software and Hardware

## GitHub repositories

- Hardware
- <https://github.com/rt-net/RT-USB-9AXIS-00>
- Firmware and Hardware information of USB Output 9-axis IMU sensor
  module

<!-- -->

- ROS package
- <https://github.com/rt-net/rt_usb_9axisimu_driver>
- ROS package converts the sensor values to ROS topics

## Published topics

- **imu/data_raw (sensor_msgs/Imu)**
- raw data of linear acceleration and angular velocity

<!-- -->

- **imu/mag (sensor_msgs/MagneticField)**
- raw data of magnetic flux density

<!-- -->

- **imu/temperature (sensor_msgs/Float64)**
- data of the sensor IC temperature

## Parameters

- **port (string, default: /dev/ttyACM0)**
- USB port name connected the sensor module

<!-- -->

- **frame_id (string, default: imu_link)**
- link name of the sensor module defined in URDF

<!-- -->

- **linear_acceleration_stddev (double, default: 0.023145)**
- standard deviation of linear acceleration (m/s\^2)

<!-- -->

- **angular_velocity_stddev (double, default: 0.0010621)**
- standard deviation of angular velocity (rad/s)

<!-- -->

- **magnetic_field_stddev (double, default: 0.00000080786)**
- standard deviation of magnetic flux density (T)

## Examples

[Youtube](https://www.youtube.com/watch?v=4V1BAAKFIs4)

rqt_plot shows 3-axis accelerations
[Youtube](https://www.youtube.com/watch?v=GZTu8DwG1OY)

rqt_plot shows 3-axis angular velocities
[Youtube](https://www.youtube.com/watch?v=_NfqTJ61CpY)

rqt_plot shows 3-axis magnetic flux densities
[Youtube](https://www.youtube.com/watch?v=qjaOAF5wWi8)

## Related pages

- More information about USB Output 9-axis IMU sensor module
- <https://www.rt-net.jp/products/9axisimu2?lang=en>
