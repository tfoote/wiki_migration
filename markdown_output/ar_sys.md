## Overview

3D pose estimation ROS package using
[ArUco](http://www.uco.es/investiga/grupos/ava/node/26) marker boards.

## Installing

{ Or equivalent depending on your operating system. }}}} { Or equivalent
depending on your operating system. }}}} 

```
{
#!wiki version groovy
Since Groovy is now at its end of life, we don't provide releases for it, but you still can build it from the source. Assuming you know how to [[catkin/Tutorials/create_a_workspace|create a catkin workspace]], you can use [[http://git-scm.com/|git]] and roslocate to automatically download the repository and set your path:

{{{
#!shell
cd ~/catkin_ws/src
roslocate uri ar_sys | xargs git clone
```



and then build the [ar_sys](ar_sys) package, by running:



```shell
cd ~/catkin_ws
catkin_make
```

 }}}}

## Usage



```
{
#!wiki version groovy
{{{#!wiki blue/solid
To use the launchers with full functionality, you might need to build [[uvc_camera]] from the source, as we depend on it in the camera capture capabilities.
```

 }}}} To start tracking a single board of
markers, ensure you pass the proper launcher parameters (see
[launch files](#Launch_files) for details) to meet your camera device,
[calibration](camera_calibration) URI, pointing to the correct board
configuration, and then use:



```shell
roslaunch ar_sys single_board.launch
```

 To track more boards, follow the same as of a
single board, but modify the **data/multi/boards.yml** file to include
all your board configuration files, and then launch:



```shell
roslaunch ar_sys multi-boards.launch
```

 Finally, you could have the 3D [rviz](rviz)
viewer of your boards by using:



```shell
roslaunch ar_sys system_viewer.launch
```

 This is the very basic usage of the package,
and there are more details in the scenarios below.

## Scenarios

### Multiple cameras

Assuming you have two cameras, and would like to display multiple boards
from each camera in one 3D rvix environment. All you need is to execute
something like these commands, each in a separate terminal:


```shell
roslaunch ar_sys multi-boards.launch video_namespace:=camera1 camera_frame_id:=camera1 camera_device:=/dev/video0 uid:=1
roslaunch ar_sys multi-boards.launch video_namespace:=camera2 camera_frame_id:=camera2 camera_device:=/dev/video1 uid:=2
roslaunch ar_sys system_viewer.launc
```

 This is the single board version of the above
scenario. 

```shell
roslaunch ar_sys single_board.launch video_namespace:=camera1 camera_frame_id:=camera1 board_frame_id:=board1 camera_device:=/dev/video0 uid:=1
roslaunch ar_sys single_board.launch video_namespace:=camera2 camera_frame_id:=camera2 board_frame_id:=board2 camera_device:=/dev/video1 uid:=2
roslaunch ar_sys system_viewer.launch
```



## Nodes



```clearsilver
node.0 {
name = single_board
desc = single_board listens to the `/camera_info` and `/image` topics and detects the markers board set by its parameters, and then publishes the from-the-camera transform of the board detect on the `/transform` topic. This is mainly used with `system_viewer` node to display the coordinates of the board and the camera related to a reference world point using [[rviz]]. The `single_board` node runs with a `~board_config` parameter that points to a [[YAML Overview|YAML]] file containing markers' positions and IDs within the board.
sub {
0.name= /image
0.type= sensor_msgs/Image
0.desc= rectified image topic
1.name= /camera_info
1.type= sensor_msgs/CameraInfo
1.desc= camera info for the camera
}
pub {
0.name = /result
0.type = sensor_msgs/Image
0.desc = Shows input `/image` with augmented information

1.name = /debug
1.type = sensor_msgs/Image
1.desc = Shows the internal image resulting from the threshold operation

2.name = /position
2.type = geometry_msgs/Vector3Stamped
2.desc = Provides the position information of the detected board

3.name = /pose
3.type = geometry_msgs/PoseStamped
3.desc = Provides the position and orientation information of the detected board

4.name = /transform
4.type = geometry_msgs/TransformStamped
4.desc = Provides the transformation information from the camera to the detected board
}
param {
0.name = ~image_is_rectified
0.type = [ {bool: bool} ]
0.desc = Whether to pass the P[] matrix values received from the `/camera_info` topic into `ArUco` core or not.
0.default = [true]

1.name = ~marker_size
1.type = [ {double: double} ]
1.desc = The side length of the markers used in constructing the board in meters. It is used in the calculation of the distance between the camera and the marker itself.
1.default = [0.05]

2.name = ~board_config
2.type = [ {str: str} ]
2.desc = The path to the YAML file listing markers which contains number of markers used, and the markers array. Each marker in the array must have an "id" and "corners" keys.
2.default = ["boardConfiguration.yml"]

3.name = ~board_frame
3.type = [ {str: str} ]
3.desc = The frame ID of the board that get broadcasted in the `/transform` topic.
3.default = [""]

4.name = ~draw_markers
4.type = [ {bool: bool} ]
4.desc = If true, `/result` topic will display the IDs and draw rectangles around each marker detected from the `/image` topic.
4.default = [false]

5.name = ~draw_markers_cube
5.type = [ {bool: bool} ]
5.desc = If true, `/result` topic will draw cubes above each marker detected from the `/image` topic.
5.default = [false]

6.name = ~draw_markers_axis
6.type = [ {bool: bool} ]
6.desc = If true, `/result` topic will draw the XYZ coordinates orientation of each marker detected from the `/image` topic.
6.default = [false]
}
}
```

 

```clearsilver
node.1 {
name = multi_boards
desc = multi_boards listens to the `/camera_info` and `/image` topics and detects virtually unlimited boards of markers set by YMAL config file indicated in its parameters, and then publishes the from-the-camera transforms of each board detected on the `/transform` topic. This is mainly used with `system_viewer` node to display the coordinates of the camera and each board related to a reference world point using [[rviz]]. The `multi_boards` node runs with a `~boards_config` parameter that points to a [[YAML Overview|YAML]] file containing list of boards.
sub {
0.name= /image
0.type= sensor_msgs/Image
0.desc= rectified image topic
1.name= /camera_info
1.type= sensor_msgs/CameraInfo
1.desc= camera info for the camera
}
pub {
0.name = /result
0.type = sensor_msgs/Image
0.desc = Shows input `/image` with augmented information

1.name = /debug
1.type = sensor_msgs/Image
1.desc = Shows the internal image resulting from the threshold operation

2.name = /position
2.type = geometry_msgs/Vector3Stamped
2.desc = Provides the position information of each detected board

3.name = /pose
3.type = geometry_msgs/PoseStamped
3.desc = Provides the position and orientation information of each detected board

4.name = /transform
4.type = geometry_msgs/TransformStamped
4.desc = Provides the transformation information from the camera to each detected board
}
param {
0.name = ~image_is_rectified
0.type = [ {bool: bool} ]
0.desc = Whether to pass the P[] matrix values received from the `/camera_info` topic into `ArUco` core or not.
0.default = [true]

1.name = ~boards_config
1.type = [ {str: str} ]
1.desc = The path to the YAML file listing boards which contains the boards array. Each board in the array must have an "name", "path" and "marker_size" keys. The name is the equivalent to `board_frame` from the `single_board` node while marker_size is obviously the equivalent to `marker_size` parameter, the path is a relative path to the `boards_directory` parameter, and it points to a single YML file as of the `board_config` parameter from the `single_board` node.
1.default = ["boardsConfiguration.yml"]

2.name = ~boards_directory
2.type = [ {str: str} ]
2.desc = A directory that contains all the boards' YAML configuration files.
2.default = ["./data"]

3.name = ~draw_markers
3.type = [ {bool: bool} ]
3.desc = If true, `/result` topic will display the IDs and draw rectangles around each marker detected from the `/image` topic.
3.default = [false]

4.name = ~draw_markers_cube
4.type = [ {bool: bool} ]
4.desc = If true, `/result` topic will draw cubes above each marker detected from the `/image` topic.
4.default = [false]

5.name = ~draw_markers_axis
5.type = [ {bool: bool} ]
5.desc = If true, `/result` topic will draw the XYZ coordinates orientation of each marker detected from the `/image` topic.
5.default = [false]
}
}
```




```shell
cd ~/catkin_ws
catkin_make
```

0

## Launch files

There are many [roslaunch parameters](roslaunch/XML#Setting_parameters)
that we are employing in the launchers of each node. Here is the
details: 

```shell
cd ~/catkin_ws
catkin_make
```

1 

```shell
cd ~/catkin_ws
catkin_make
```

2


```shell
cd ~/catkin_ws
catkin_make
```

3

## Bug Reports & Feature Requests



```shell
cd ~/catkin_ws
catkin_make
```

4 We appreciate the time and effort spent
submitting bug reports.
