![](attachment:imu.png)

(original 3DM-GX2 coordinate system)

## Who Should Use this Package?

-   If you are running on the PR2/Texas robot this driver should be
    running by default when you bring up the robot. You do not need to
    launch it yourself.

```{=html}
<!-- -->
```
-   If you want to use 3DM-GX2 compatible IMU with ROS, use the
    [imu_node](#RosAPI).

```{=html}
<!-- -->
```
-   For advanced users who want lower-level access to a 3DB-GX2
    compatible IMU, the unsupported
    [C++ API](http://www.ros.org/doc/api/microstrain_3dmgx2_imu/html/classmicrostrain__3dmgx2__imu_1_1IMU.html)
    may be used.

## Supported Hardware

This driver should work with IMUs that use the Microstrain 3DM-GX2
protocol.

## API Stability

The ROS API of this node should be considered stable.

While a
[C++ API](http://www.ros.org/doc/api/microstrain_3dmgx2_imu/html/classmicrostrain__3dmgx2__imu_1_1IMU.html)
exists, it has not been reviewed and should be considered unstable.

## ROS API



```clearsilver
node.0 {
name=imu_node
desc=`imu_node` is a driver for the 3DM-GX2 Inertial Measurement Unit. It publishes orientation, angular velocity and linear acceleration as well as their covariances, and complies with the [[imu_drivers#RosAPI|IMU API]]. This node only provides streaming access to message 0xC8 (Acceleration, Angular Rate and Orientation), the unsupported [[http://www.ros.org/doc/api/microstrain_3dmgx2_imu/html/classmicrostrain__3dmgx2__imu_1_1IMU.html|C++ API]] gives access to a broader range of message types.
pub{
0.name= imu/data
0.type= sensor_msgs/Imu
0.desc= Streaming inertial data from the IMU. Includes acceleration, angular rates and orientation. The orientation is produced by the IMU firmware, which uses gravity, and in some cases the Earth's magnetic field, to remove integration drift. The orientation matrix is the transpose of the orientation matrix returned by the hardware, rotated 180 degrees around the y axis. This corresponds to a transformation from the IMU frame to the world frame, with the z axis point up.
1.name= diagnostics
1.type= diagnostic_msgs/DiagnosticArray
1.desc= Diagnostic status information.
2.name= imu/is_calibrated
2.type= std_msgs/Bool
2.desc= Latched topic indicating if the gyroscope biases have been calibrated.
}
srv{
0.name= ~self_test
0.type= diagnostic_msgs/SelfTest
0.desc= Starts the imu self test.
1.name= imu/calibrate
1.type= std_srvs/Empty
1.desc= Tells the IMU to (re)calibrate its gyroscope biases. The service call returns once calibration is complete. Calibration failure can be detected by subscribing to the `imu/is_calibrated` topic. A message will published to `imu/is_calibrated` for each call to `imu/calibrate`.
}
param {
0.name= ~port
0.default= /dev/ttyUSB0
0.type= string
0.desc= The port the imu is running on.
1.name= ~frame_id
1.default= imu
1.type= string
1.desc= The frame in which imu readings will be returned.
2.name= ~autocalibrate
2.default= true
2.type= bool
2.desc= Whether the imu automatically computes its biases at startup (set to `false` if you intend to calibrate via the calibrate service).
3.name= ~orientation_stdev
3.default= 0.035
3.type= double
3.desc= Square root of the orientation_covariance diagonal elements in rad. The default value, derived from the manufacturer datasheet, is very conservative.
4.name= ~angular_velocity_stdev
4.default= 0.012
4.type= double
4.desc= Square root of the angular_velocity_covariance diagonal elements in rad/s. The default value, derived from the manufacturer datasheet, is very conservative.
5.name= ~linear_acceleration_stdev
5.default= 0.098
5.type= double
5.desc= Square root of the linear_acceleration_covariance diagonal elements in m/s^2. The default value, derived from the manufacturer datasheet, is very conservative.
6.name= ~max_drift_rate
6.default=0.0001
6.type=double
6.desc=Just after performing a calibration, if the observed gyro rates are greater than this parameter, the calibration is assumed to have failed, and the imu starts reporting itself as uncalibrated. <<Version(C Turtle)>>
7.name= ~assume_calibrated
7.default=false
7.type=bool
7.desc=Indicates whether the IMU should assume that it is calibrated at startup. <<Version(C Turtle)>>
}
}
```



## Communication Protocol Manual

The 3DM-GX2 protocol can be found
[here\|&do=get](http://files.microstrain.com/dcp/Inertia-Link-3DM-GX2-data-communications-protocol.pdf).
