## ROS API



```clearsilver
node.0 {
name=Kinect Node
desc=The Kinect node and nodelet implement the following ROS API:
pub{
0.name= camera/points
0.type= sensor_msgs/PointCloud
0.desc= The 3D pointcloud acquired by the Kinect stereo, as pointcloud version 1
1.name= camera/points2
1.type= sensor_msgs/PointCloud2
1.desc= The 3D pointcloud acquired by the Kinect stereo, as pointcloud version 2
2.name= camera/rgb/camera_info
2.type= sensor_msgs/CameraInfo
2.desc= Metadata (camera matrix, distortion, rectification, projection) for the color camera
3.name= camera/rgb/image_raw
3.type= sensor_msgs/Image
3.desc= The raw uncompressed images of the color camera
4.name= camera/depth/camera_info
4.type= sensor_msgs/CameraInfo
4.desc= Metadata (camera matrix, distortion, rectification, projection) for the infrared depth camera
5.name= camera/depth/image_raw
5.type= sensor_msgs/Image
5.desc= The raw uncompressed images of the infrared depth camera

}
param{
0.name= kinect_node/device_id
0.type= integer
0.desc= The id of the device to connect to
0.name= kinect_node/rgb/camera_info_url
0.type= namespace on parameter server
0.desc= Metadata (camera matrix, distortion, rectification, projection) for the color camera.
0.name= kinect_node/depth/camera_info_url
0.type= namespace on parameter server
0.desc= Metadata (camera matrix, distortion, rectification, projection) for the infrared depth camera.
}
}
```


