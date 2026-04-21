Recent updates changed the published point cloud frame of reference to
be the same one used by [stereo_image_proc](stereo_image_proc) (+x is
right, +y is down, +z is forward). This was meant to help beginning
users validate the SR data versus a stereo setup.

## ROS API



```clearsilver
node.0 {
name=swissranger_camera
desc=The `swissranger_camera` driver provides a ROS interface for Mesa Imaging !SwissRanger devices (3000/4000/4500) that use the [[http://www.mesa-imaging.ch/support/driver-downloads/|libmesasr]] libraries.
pub{
0.name= camera_info
0.type= sensor_msgs/CameraInfo
0.desc= Camera intrinsics for published images
1.name= distance/image_raw
1.type= sensor_msgs/Image
1.desc= 2D depth image
2.name= intensity/image_raw
2.type= sensor_msgs/Image
2.desc= 2D intensity image that corresponds to the depth image of distance/image_raw
3.name= confidence/image_raw
3.type= sensor_msgs/Image
3.desc= 2D image that corresponds to the confidences of depths from distance/image_raw
3.name= pointcloud/cloud_raw
3.type= sensor_msgs/PointCloud
3.desc= 3D pointcloud generated from distance/image_raw
}
srv{
1.name= set_camera_info
1.type= sensor_msgs/SetCameraInfo
1.desc= Sets the camera's calibration
}
param {
group.0 {
name=Initial Parameters
desc=These parameters only affect the driver when it starts.
1.name=~frame_id
1.default=node name
1.type=str
1.desc=Frame of reference ID for coordinate transforms
2.name=~auto_exposure
2.default=1
2.type=int
2.desc=-1 leaves in current state; 0 turns off auto exposure; 1 turns it on.
3.name=~integration_time
3.default=-1
3.type=int
3.desc=Sets integration time [SR3k:(integration_time+1)*0.200 ms; SR4k 0.300ms+(integration_time)*0.100 ms].  -1 leaves in current state; should not be used with auto_exposure.
4.name= ~modulation_freq
4.default=-1
4.type= int
4.desc= Set modulation frequency. -1 leaves in current state (which on power up, is the FACTORY CALIBRATED state -- you probably want this one); 0  == 40MHz,  SR3k: maximal range 3.75m; 1  == 30MHz,  SR3k, SR4k: maximal range 5m; 2  == 21MHz,  SR3k: maximal range 7.14m; 3  == 20MHz,  SR3k: maximal range 7.5m; 4  == 19MHz, SR3k: maximal range 7.89m; 5  == 60MHz,  SR4k: maximal range 2.5m; 6  == 15MHz,  SR4k: maximal range 10m; 7  == 10MHz,  SR4k: maximal range 15m; 8  == 29MHz,  SR4k: maximal range 5.17m; 9  == 31MHz,  SR4k: maximal range 4.84m; 10 == 14.5MHz, SR4k: maximal range 10.34m; 11 == 15.5MHz, SR4k: maximal range 9.68m
5.name=~amp_threshold
5.default=-1
5.type=int
5.desc= Sets measurements with amplitude values less than this threshold to 0.
}
group.1 {
name=Reconfigurable Parameters
desc=Currently no reconfigurable parameters.
}
group.2 {
name=Calibration Parameters
0.name=~camera_info_url
0.default=""
0.type=str
0.desc=URL for loading and storing calibration data in the form `file:///path/to/local/calibration_file.yaml`. If not specified, no data will be loaded, and calibration data will be stored in `file:///tmp/calibration_<camera_name>.yaml`.
}
}
```


