We utilize sensors, such as camera and lidar, in order to acquire
information of our environment. Fusion of data from sensors allows you
to identify objects in a scene. Cam2lidar converts data from these 2
sensors into the same coordinate system.

## Supported hardware

Cam2lidar will work with any camera driver node satisfying the standard
ROS camera interface. To be more specific, we have tested it with
[Intel's Realsense d435i](https://www.intelrealsense.com/depth-camera-d435i/)
and
[Econ's E-cam130 Cameras](https://www.e-consystems.com/nvidia-cameras/jetson-agx-xavier-cameras/four-synchronized-4k-cameras.asp).

## Tutorial

The tutorial for setting up the necessary parameters and performing the
calibration can be found
[here](http://wiki.ros.org/cam2lidar/Tutorials/How%20to%20calibrate%20Lidar%20and%20Camera).

## Usage

To run the `geometric_calibration` node for a monocular camera set the
input topics and the configuration parameters in
`./config/geometric.yaml` according to the tutorial and execute:

```
roslaunch cam2lidar geometric.launch
```

Accordingly, to run the `temporal_calibration` node for a monocular
camera set the input topics and the configuration parameters in
`./config/temporal.yaml` according to the tutorial and execute:

```
roslaunch cam2lidar temporal.launch
```

## Nodes

```clearsilver
node.0 {
name=user_interface
desc=`user_interface` is responsible for coordinating the calibration window. This node subscribes to an image raw and a camera info topic, in order to visualize the detection of the target. The calibration window shows the current images from the cameras and waits for the user to set the Distance Threshold and the number of Consequent Frames.  When the user presses the '''Start''' button, the node initiated the geometric_calibration/temporal_calibration node.  When sufficient number of points are collected the user clicks '''Calibrate''' and the node extracts extract the Rotation and Translation Vectors by solving the PnP problem of 2D Image points and 3D Lidar points. The output is saved in `output/geometric_calibration.txt`.

sub{
0.name= image_raw
0.type= sensor_msgs/Image
0.desc= raw image topic, for monocular cameras
1.name= camera_info
1.type= sensor_msgs/CameraInfo
1.desc= raw camera info topic, for monocular cameras
}
``` ```clearsilver
node.1 {
name=geometric_calibration
desc=`geometric_calibration` subscribes to ROS raw image topics and Velodyne (Lidar) topic. The node detects Apriltag and the Lidar target and saves samples, in order to solve the PnP problem. The output is saved in `./output/image_points.txt` and `./output/lidar_points.txt`.

sub{
0.name= image_raw
0.type= sensor_msgs/Image
0.desc= raw image topic, for monocular cameras
1.name= velodyne_points
1.type= sensor_msgs/PointCloud2
1.desc= raw lidar topic
}
```
```clearsilver
node.2 {
name=temporal_calibration
desc=`temporal_calibration` subscribes to ROS raw image topics and Velodyne (Lidar) topic. The node detects Apriltag and the Lidar target and saves samples, in order to calculate the time difference between the lidar and the camera input. The output is calculated and saved in `./output/time_difference.txt`.

sub{
0.name= image_raw
0.type= sensor_msgs/Image
0.desc= raw image topic, for monocular cameras
1.name= velodyne_points
1.type= sensor_msgs/PointCloud2
1.desc= raw lidar topic
}
```
