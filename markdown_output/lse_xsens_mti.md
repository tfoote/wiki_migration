Also check the [xsens_mti](xsens_mti) package.

## Supported Hardware

  -- ------------------------------- -- --------------------------- --
     **Xsens MTi**                      **Xsens MTi-G**             
     ![](attachment:xsens_mti.jpg)      ![](attachment:MTi-G.jpg)   
  -- ------------------------------- -- --------------------------- --

## ROS API

```clearsilver
node.0 {
name= mti_node
desc=`mti_node` is a driver for the Xsens MTi/MTi-G Inertial Measurement Unit. It publishes orientation, angular velocity, linear velocity, linear acceleration, altitude, latitude and longitude (covariances are not yet supported), and complies with the [[imu_drivers#RosAPI|IMU API]] and [[http://ros.org/wiki/sensor_msgs|Sensor message]] for NavSat API and odometry API. Take a look at the unsupported [[http://www.ros.org/doc/api/lse_xsens_mti/html/classXsens_1_1MTi.html|C++ API]] for further features.
pub{
0.name= imu/data
0.type= sensor_msgs/Imu
0.desc= Streaming inertial data from the IMU.
1.name= fix
1.type= sensor_msgs/NavSatFix
1.desc= Streaming GPS data from the IMU.
2.name= odom
2.type= nav_msgs/Odometry
2.desc= Streaming odometry data from the IMU (linear velocity, angular velocity, orientation).
}
param {
0.name= ~port
0.default= /dev/ttyUSB0
0.type= string
0.desc= The port where the MTi can be found.
0.name= ~baudrate
0.default= 115200
0.type= int
0.desc= Baudrate of the MTi.
1.name= ~frame_id
1.default= /base_imu
1.type= string
1.desc= The frame in which the MTi readings will be returned.
2.name= ~temperature
2.default= false
2.type= bool
2.desc= Configure the sensor to get its temperature in degrees Celcius.
3.name= ~calibrated
3.default= true
3.type= bool
3.desc= Configure the sensor to get its accelerations, rate of turn and magnetic field in X, Y and Z axes.
4.name= ~orientation
4.default= true
4.type= bool
4.desc= Configure the sensor to get its quaternions.
5.name= ~auxiliary
5.default= false
5.type= bool
5.desc= Configure the sensor to get its analog input #1 and #2.
6.name= ~position
6.default= false
6.type= bool
6.desc= Configure the sensor to get its latitude, longitude and altitude.
7.name= ~velocity
7.default= false
7.type= bool
7.desc= Configure the sensor to get its velocity X, Y and Z. Note that velocity in North East Down can be obtained by changing velocityModeNED.
8.name= ~status
8.default= false
8.type= bool
8.desc= Configure the sensor to get flags that represent the status and estimated validity of the output.
9.name= ~rawGPS
9.default= false
9.type= bool
9.desc= Configure the sensor to get pressure sensor and GPS data (see GPS PVT data in the Xsens documentation).
10.name= ~rawInertial
10.default= false
10.type= bool
10.desc= Configure the sensor to get the uncalibrated raw data output of the accelerations, rate of turn and magnetic field in X, Y and Z axes.
11.name= ~timeStamp
11.default= false
11.type= bool
11.desc= Configure the sensor to get no timestamp or a sample counter.
12.name= ~orientationMode
12.default= Quaternion (0)
12.type= int
12.desc= Configure the sensor to get Quaternion(0), Euler angles(1) or Matrix(2).
13.name= ~enableAcceleration
13.default= false
13.type= bool
13.desc= Configure the sensor to get acceleration.
14.name= ~enableRateOfTurn
14.default= false
14.type= bool
14.desc= Configure the sensor to get rate of turn.
15.name= ~enableMagnetometer
15.default= false
15.type= bool
15.desc= Configure the sensor to get magnetometer.
16.name= ~velocityModeNED
16.default= false
16.type= bool
16.desc= Configure the sensor to get the velocity in North East Down.
17.name= ~scenario
17.default= Automotive (2)
17.type= int
17.desc= Configure the sensor to set the scenario to use (see 'XKF Scenarios' sections in the device specific manuals).
18.name= ~GPSLeverArm_X
18.default= 0
18.type= double
18.desc= Configure the position of the lever arm.
19.name= ~GPSLeverArm_Y
19.default= 0
19.type= double
19.desc= Configure the position of the lever arm.
20.name= ~GPSLeverArm_Z
20.default= 0
20.type= double
20.desc= Configure the position of the lever arm.
}
}
```
