## What does vi_sfm do?

`vi_sfm` is a ROS package used to solve visual-inertial structure from
motion problems. This package fuses visual and inertial data in a
closed-form solution. The closed-form solution consists of a single
equation that determines the initial velocity, the distance to
point-features and the gravity linearly by only using inertial
measurements unit (IMU) and monocular camera features acquired in a
short time interval (4 seconds). It is assumed that the camera is
calibrated and the transformation between the camera and the IMU is
known and can be determinated using TF transformation.

## Paper

The closed-form solution was presented at ICRA 2016.

## Supported hardware

`vi_sfm` will work with any camera driver node satisfying the standard
ROS camera interface and any imu driver node satisfying the sensor

## Usage of Robot State

To run the `robot_state` node :

```
rosrun vi_sfm robot_state imu:=/my_imu feature:=/my_feature camera:=/my_camera
```

To run the `robot_state` node using rectified features :

```
rosrun vi_sfm robot_state imu:=/my_imu feature:=/my_feature camera:=/my_camera isRectified:=True
```

Or use a specific launch file :

```
roslaunch vi_sfm robot_state.launch
```

## Nodes

```clearsilver
node.0 {
name=robot_state
desc=`robot_state` subscribes to ROS imu, features image and camera info topics. It performs the closed-form solution after 4 seconds of collecting datas.

sub{
0.name= feature
0.type= vi_sfm/Features
0.desc= image features topic. This message lists a set of features that can be tracked during the time interval.
1.name= imu
1.type= sensor_msgs/Imu
1.desc= imu topic
2.name= camera
2.type= sensor_msgs/CameraInfo
2.desc= camera info topic for camera calibration parameters
}
}
node.1 {
name=robot_state_with_bias
desc=`robot_state_with_bias` is exactly the same node that `robot_state`, but used libLBFGS to perform a gradient-descent that can estimated the gyroscope bias.

sub{
0.name= feature
0.type= vi_sfm/Features
0.desc= image features topic. This message lists a set of features that can be tracked during the time interval.
1.name= imu
1.type= sensor_msgs/Imu
1.desc= imu topic
2.name= camera
2.type= sensor_msgs/CameraInfo
2.desc= camera info topic for camera calibration parameters
}
}
```
