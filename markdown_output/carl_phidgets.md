## About

The `carl_phidgets` package provides a ROS wrapper for the
[ PhidgetSpatial Precision 3/3/3 High Resolution](http://www.phidgets.com/products.php?product_id=1044 )
or the
[ PhidgetSpatial 3/3/3 Basic](http://www.phidgets.com/products.php?product_id=1042 )
sensors, and nodes that support useful IMU functionality. This includes
a Kalman filter for a base sensor and a top frame sensor to determine
the orientation of the base and top frame, respectively.

  -- ------------------------------- -- -- -- --------------------------- --
     ![](attachment:precision.jpg)            ![](attachment:basic.jpg)   
  -- ------------------------------- -- -- -- --------------------------- --

## Nodes

```clearsilver
node.0 {
  name = phidgets_imu_node
  desc = ROS wrapper that allows data to be read from an IMU.
  pub {
    0.name = imu/data_raw
    0.type = sensor_msgs/Imu
    0.desc = IMU data, including 3-axis angular velocities, linear accelerations, and covariance for both (the orientation and orientation covariance are unused).
  }
  pub {
    1.name = imu/mag
    1.type = geometry_msgs/Vector3Stamped
    1.desc = 3-axis magnetic orientation vector.
  }
  pub {
    2.name = imu/is_calibrated
    2.type = std_msgs::Bool
    2.desc = Publishes true whenever calibration is performed on the IMU.
  }
  srv{
  0.name= imu/calibrate
  0.type= std_srvs/Empty
  0.desc= Calibrates or recalibrates the IMU's gyro.
  }
  param {
    0.name = period
    0.type = int
    0.desc = Period at which to read data, in ms (4-1000 ms).
    0.default = 8
  }
  param {
    1.name = frame_id
    1.type = string
    1.desc = Coordinate frame of the sensor.
    1.default = imu
  }
  param {
    2.name = angular_velocity_stdev
    2.type = double
    2.desc = Angular velocity standard deviation (rad/s).
    2.default = .000349
  }
  param {
    3.name = linear_acceleration_stdev
    3.type = double
    3.desc = Linear acceleration standard deviation (m/s^2).
    3.default = .002943
  }
  param {
    4.name = serial_number
    4.type = int
    4.desc = Unique sensor serial number (-1 to use any detected sensor).
    4.default = -1
  }
}
node.1 {
  name = orientation_filter
  desc = Kalman filter sensor fusion for CARL's base and frame IMUs, to determine orientation.
  sub {
    0.name = imu_base/data_raw
    0.type = sensor_msgs/Imu
    0.desc = IMU data from the base sensor.
  }
  sub {
    1.name = imu_top/data_raw
    1.type = sensor_msgs/Imu
    1.desc = IMU data from the top frame sensor.
  }
  pub {
    2.name = frame_joint_states
    2.type = sensor_msgs/JointState
    2.desc = Joint positions for the base and top frame, used for updating the transforms of the robot.
  }
}
```

## Installation

To install the `carl_bot` package, you can install from source with
the following commands:

. ```shell
cd /(your catkin workspace)/src
git clone https://github.com/WPI-RAIL/carl_bot.git
cd ..
catkin_make
catkin_make install
```

## First Time Sensor Setup

To use the Phidgets IMU as a user other than root, you need to create a
udev rule. Create a file called `99-phidgets.rules`, with the
following line:

. ```
SUBSYSTEMS=="usb", ACTION=="add", ATTRS{idVendor}=="06c2", ATTRS{idProduct}=="00[3-a][0-f]", MODE="666"
```

Copy this file into the `/etc/udev/rules.d` directory. You may need to
reboot your computer for this to take effect.

## Startup

The two IMU's placed on CARL can be launched with the following launch
file:

. ```
roslaunch carl_phidgets imu.launch
```

The orientation filter can be started with: . ```
rosrun carl_phidgets orientation_filter
```

Individual IMUs can be started with by running the IMU node separately,
and specifying the sensor's unique serial number.

. ```
rosrun carl_phidgets phidgets_imu_node _serial_number:=xxxxxx
```
