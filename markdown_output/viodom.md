## Overview

This package contains one single node: `viodom_node`, which estimates
robot motion based on incoming raw images and IMU mesaurements from the
[Visual-Inertial (VI-) Sensor](vi_sensor). To correctly estimate the
motion, the node first needs to wait for a few seconds to initialize an
IMU filter.

## Tf tree

The transforms tree (following
[REP 105](http://www.ros.org/reps/rep-0105.html)) is as follows:

. `odom` → `base_link` → `camera`

Visual odometry algorithms generally calculate* camera motion.* To be
able to calculate *robot motion* based on *camera motion*, the
transformation from the camera frame to the robot frame has to be known.
Therefore this implementation needs to know the tf `base_link` →
`camera` to be able to publish `odom` → `base_link`. The node
currently uses default values from the sensor setup on the !AscTec Neo
Research platform.

## Nodes



```clearsilver
name = viodom_node
desc = This node takes in a stereo pair of images and IMU data, and outputs pose estimates. Images are rectified using calibration information. On startup, an IMU filter needs to be initialized.
sub{
  0.name= left_cam/image_raw
  0.type= sensor_msgs/Image
  0.desc= Left camera raw image.
  1.name= left_cam/camera_info
  1.type= sensor_msgs/CameraInfo
  1.desc= Left camera calibration information.
  2.name= right_cam/image_raw
  2.type= sensor_msgs/Image
  2.desc= Right camera raw image.
  3.name= right_cam/camera_info
  3.type= sensor_msgs/CameraInfo
  3.desc= Right camera calibration information.
  4.name= imu_topic
  4.type= sensor_msgs/Imu
  4.desc= IMU topic.
}
pub{
  0.name= viodom_transform
  0.type= geometry_msgs/TransformStamped
  0.desc= Robot's estimated pose in the odom frame.
  1.name= point_cloud
  1.type= sensor_msgs/PointCloud2
  1.desc= 3D point cloud based on the input stereo pair.
  2.name= tf
  2.type= tf/tfMessage
  2.desc= Publishes the transform from odom to base_link.
}
```



## Citing

If you use viodom in an academic context, please cite the following
publication: <http://ieeexplore.ieee.org/document/7502653/>



```
@INPROCEEDINGS{7502653,
  author={F. J. Perez-Grau and F. R. Fabresse and F. Caballero and A. Viguria and A. Ollero},
  booktitle={2016 International Conference on Unmanned Aircraft Systems (ICUAS)},
  title={Long-term aerial robot localization based on visual odometry and radio-based ranging},
  year={2016},
  pages={608-614},
  doi={10.1109/ICUAS.2016.7502653},
  month={June},}
```


