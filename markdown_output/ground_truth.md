## ROS Nodes



```clearsilver
node.0 {
 name = calibrate
 desc = Obtain the position and orientation of the kinect sensor by using landmarks on the field
 sub {  
  2.name = /camera/rgb/points
  2.type = sensor_msgs/PointCloud2
  2.desc = The point cloud returned by the kinect containing an RGB channel along with the 3D point data.
  3.name = /camera/rgb/image_color
  3.type = sensor_msgs/Image
  3.desc = The image from the VGA camera on the kinect. It is used primarily for user input.
 }
```



#### Placing the Kinect

1\. Although the algorithm is independent of the sensor position,
careful placement of a single sensor allows it to cover half the SPL
field size (3m x 4m). I have had success placing it on the side of the
half field at a height of about 2.5 - 3.5 meters.

2\. Launch the calibrate node and adjust sensor appropriately until the
field is visible as desired. 

```
roslaunch ground_truth calibrate.launch
```



#### Calibrating the Kinect

1\. Launch the kinect driver 

```
roslaunch openni_camera openni_node.launch
```



2\. Launch the calibrate node 

```
roslaunch ground_truth calibrate.launch
```



3\. Follow the instructions on the bottom of the pointcloud visualizer
screen. *Remember that you have to click on the image and not the
pointcloud!*. A small sphere should appear in the point cloud visualizer
window to indicate the point you clicked.

4\. After you have selected all the ground plane points and the
landmarks, the point cloud visualization should change so that the
coordinate axes are aligned with the cloud. If you think the results
look good you can terminate the program, as the calibration file has
already been saved.

#### Command line arguments

1\. The program supports a couple of command line arguments.


```
-qsize <integer>         the ROS topic queue size (recommended value 1)
-calibFile <string>      location where the calibration file should be stored
-cam <string>            specification controlling the geometry of the 
                         visualizer window on the screen
```



2\. The `launch/calibrate.launch` file can be used to specify these
arguments, so that they do not have to be supplied every time. These
arguments are the ones that are supplied every time you run the binary
through the `roslaunch` command.

3\. Alternatively, you can supply these parameters at command line
directly 

```
rosrun ground_truth calibrate -qsize 1 -calibFile data/calib2.txt
```





```clearsilver
node.0 {
 name = detect
 desc = Find the locations of the robots and the orange ball on the field
 sub {  
  2.name = /camera/rgb/points
  2.type = sensor_msgs/PointCloud2
  2.desc = The point cloud returned by the kinect containing an RGB channel along with the 3D point data.
 }
```



#### Running the detect node

1\. Launch the kinect driver 

```
roslaunch openni_camera openni_node.launch
```



2\. Launch the detect node 

```
roslaunch ground_truth detect.launch
```



#### Command line arguments

1\. The program supports a couple of command line arguments.


```
-qsize <integer>         the ROS topic queue size (recommended value 1)
-calibFile <string>      location of the calibration file
-logFile <string>        location where the generated log file should be 
                         stored
-colorTableFile <string> location of the color table lookup file
-mode <integer>          mode = {1, 2}
-cam <string>            specification controlling the geometry of the 
                         visualizer window on the screen
```



2\. The `launch/detect.launch` file can be used to specify these
arguments, so that they do not have to be supplied every time. These
arguments are the ones that are supplied every time you run the binary
through the `roslaunch` command.

3\. Alternatively, you can supply these parameters at command line
directly 

```
roslaunch ground_truth calibrate.launch
```

0

##### logFile

Currently nothing is written to the log file. Check
`src/nodes/detect.cc` for comments specifying where you could write to
this log file.

##### mode

`mode` supports 2 values 

```
roslaunch ground_truth calibrate.launch
```

1

#### Current Status

*Sep/17/2011 NOTE(piyushk): The detect binary currently implements
slightly different version of the heuristics for robot detection in
comparison to those reported in the paper. This version is what we used
for estimating parameters for our localization algorithm. I will try and
revert back to the original algorithm soon*
