Manufacturer of the TOF:
[Hitachi-LG Data Storage, Inc.](http://hlds.co.kr/v2/e_index.html/)

Product Webpage: [HLDS 3D LiDAR(TOF)](http://hlds.co.jp/product-eng/)

## Overview

-   Object distance measurement with high accuracy in realtime

```{=html}
<!-- -->
```
-   Easy to install with Ethernet (POE+) connection

```{=html}
<!-- -->
```
-   Multiple use cases can be accommondated with the SDK

![HLS-LFOM1\|width=500](attachment:hls_lfom1.png)
![view_hlds_tof_driver.launch\|width=700](attachment:view_hlds_tof_driver.png)

## Product Specification

![produc specification\|width=750](attachment:product_specification_2.png)

## Installation

### Download HLS-LFOM SDK

Download latest version(v2.1.0 or later) for Ubuntu 16.04 LTS (x64) and
extract it(<http://hlds.co.jp/product-eng/tofsdk>)

### Install SDK



```
{
$ sudo dpkg -i libtof-dev_<version_number>ubuntu16_amd64.deb
```

}

### Build HLS-LFOM 3D LiDAR(TOF) driver



```
{
$ cd ~/catkin_ws/src  
$ git clone https://github.com/HLDS-GIT/hls_lfom_tof_driver.git  
$ cd ~/catkin_ws  
$ catkin_make
```

} If using SDK older than v2.3, please use
CMakeLists_old.txt.

## Setting IP address

Modify IP address of tof.ini file in launch folder. It should be the
same as the IP address of the TOF sensor you are trying to connect.
(Default is 192.168.0.105)\
If you want to change IP address, please refer to Setup TOF sensor of
API Reference Manual in SDK

## Running Node

### Run hlds_3dtof_node



```
{
roslaunch hls_lfom_tof_driver hlds_tof_driver.launch
```

}

### Run hlds_3dtof_node with RViz



```
{
roslaunch hls_lfom_tof_driver view_hlds_tof_driver.launch
```

}

## Nodes



```clearsilver
name = hlds_3dtof_node
desc = hlds_3dtof_node is a driver for HLS-LFOM 3D LiDAR(TOF). It reads raw sensor data using HLS-LFOM's SDK and convert to ROS message.
pub {
  0.name = cloud
  0.type = sensor_msgs/PointCloud2
  0.desc = XYZ point cloud
  1.name = image_depth_raw
  1.type = sensor_msgs/Image
  1.desc = point.z data with TYPE_32FC1 encoding type
  2.name = image_depth
  2.type = sensor_msgs/Image
  2.desc = 3channel depths data with RGB8 encoding type
  3.name = image_ir
  3.type = sensor_msgs/Image
  3.desc = IR image with MONO8 encoding type
}

srv {
    0.name = set_distance_mode_srv
    0.type = hls_lfom_tof_driver/DistanceMode
    0.desc = Set TOF distance mode (dm_2_0x, dm_1_5x, dm_1_0x, dm_0_5x)
    1.name = set_edge_signal_cutoff_srv
    1.type = std_srvs/Empty
    1.desc = Set to 'true' enable and 'false' to disable edge signal cutoff.
    2.name = set_far_signal_cutoff_srv
    2.type = hls_lfom_tof_driver/FarSignalCutoff
    2.desc = Set value (0.0~1.0) 
    3.name = set_low_signal_cutoff_srv
    3.type = hls_lfom_tof_driver/LowSignalCutoff
    3.desc = Set value (0~4095)
  }

param {
  0.name = camera_mode
  0.type = string
  0.desc = set camera mode : CameraModeDepth, CameraModeIr, Depth_Ir(TOFv2 only)
  0.default = CameraModeDepth
  1.name = sensor_angle_x
  1.type = int
  1.desc = X-axis rotation angle(0 to 359 degree)
  1.default = 0
  2.name = sensor_angle_y
  2.type = int
  2.desc = Y-axis rotation angle(0 to 359 degree)
  2.default = 0
  3.name = sensor_angle_z
  3.type = int
  3.desc = Z-axis rotation angle(0 to 359 degree)
  3.default = 0
  4.name = edge_signal_cutoff
  4.type = bool
  4.desc = Edge noise reduction mode
  4.default = true
  5.name = low_signal_cutoff
  5.type = int
  5.desc = Signal level to cutoff(0 to 4095)
  5.default = 20
  6.name = far_signal_cutoff
  6.type = float
  6.desc = Distance rate far from TOF(rate:0.0~1.0)
  6.default = 0.0
  7.name = camera_pixel
  7.type = string
  7.desc = Pixel size of TOF sensor image. Refer to CameraPixel type of API reference manual in SDK
  7.default = 320x240
  8.name = ir_gain
  8.type = int
  8.desc = Exposure sensitivity for IR(1 to 15)
  8.default = 8
  9.name = distance_mode
  9.type = string
  9.desc = Distance mode of TOF sensor. Refer to DistanceMode type of API reference manual in SDK
  9.default = dm_1_0x
  10.name = frame_rate
  10.type = string
  10.desc = Frame rate of TOF sensor. Refer to FrameRate type of API reference manual in SDK
  10.default = fr30fps
}
```



## Use Case

### 3D SLAM

3D occupancy grid mapping and hector slam with HLS-LFOM1
![3D SLAM\|width=500](attachment:3d_slam.png)

#### Package Installation



```
{
// Install pointcloud to laserscan
$ sudo apt-get install ros-kinetic-pointcloud-to-laserscan
//Install hector slam
$ sudo apt-get install ros-kinetic-hector-slam
//Install octomap
$ sudo apt-get install ros-kinetic-octomap-server
```

}

#### Example

[3D hector slam launch file](attachment:hector_slam_3d.launch)

### Depth image processing

Combine depth image and IR image into XYZRGB point cloud
![Depth image processing\|width=500](attachment:depth_image_proc.png)

#### Package Installation

[depth_image_proc](http://wiki.ros.org/depth_image_proc)

#### Example

[Depth image processing launch file](attachment:depth_image_proc.launch)

### OpenPose

OpenPose with IR image

![OpenPose\|width=150](attachment:openpose.png)

#### Package Installation

[OpenPose ROS](https://github.com/stevenjj/openpose_ros)

#### Example

[OpenPose launch file](attachment:openpose.launch)

## Related Links

HLDS 2D LiDAR: [HLS-LFCD2](http://wiki.ros.org/hls_lfcd_lds_driver/)
[HLS-LFCD3](http://wiki.ros.org/hls_lfcd_lds2_driver/)
