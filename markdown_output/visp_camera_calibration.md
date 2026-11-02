## Overview

visp_camera_calibration is a ROS package that allows a highly
customisable camera calibration using calibration tools from the ViSP
library avalaible from <https://visp.inria.fr>. The image feed used for
calibration is a set of clearly distinguishible points. The planar
disposition of the points is of no importance.

This package uses ViSP's camera model described in
[ViSP geometric transformation and objetcs manual](https://visp.inria.fr/manuals/visp-tutorial-geometric-objects.pdf)
and camera calibration capabilities described in
[ViSP computer vision algorithms manual](https://visp.inria.fr/manuals/visp-tutorial-computer-vision.pdf).
The output camera parameters are given in the
[sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)
format.

## Supported hardware

visp_camera_calibration will work with any camera driver node satisfying
the standard ROS camera interface. See the
[image_pipeline hardware requirements](https://index.ros.org/p/image_pipeline).

## Installation

visp_camera_calibration is part
of [vision_visp](https://index.ros.org/p/vision_visp) stack.

- To install
  visp_camera_calibration
  package run 

```
sudo apt-get install ros-$ROS_DISTRO-visp-camera_calibration
```



<!-- -->

- Or to install the complete stack run 

```
sudo apt-get install ros-$ROS_DISTRO-vision-visp
```



## Tutorials

There are two tutorials:

- A tutorial out-of-the-box demonstration tutorial using the
  experimental camera shipped with this package can be found
  [here](#running-a-calibration-using-visp_camera_calibrations-experimental-camera).
- A tutorial that shows how to calibrate using an external camera can be
  found
  [here](#calibration-of-an-external-camera-using-the-visp-library).

## Usage

Since the module is highly customisable, the paramaters are complex. A
roslauch xml file is advisable.

### Image processing and user interaction

The user has to select seed points to start calibration from. This
requires an image processing initialisation interface module. This
module needs to load several parameters:

- 3D coordinates of at least four points the user is supposed to select
  to initialise the image processing
- 3D coordinates of all points of the calibration pattern
- tracking parameters used in image processing
- behaviour of the interface. Set pause_at_each_frame to True if you're
  using the experimental camera shipped with this package. For any other
  ROS camera, set it to False. 

```xml
<node pkg="visp_camera_calibration" name="visp_camera_calibration_image_processing" type="visp_camera_calibration_image_processing">
      <!-- 3D coordinates of 4 points the user has to select to initialise the calibration process -->
      <rosparam param="selected_points_x">[0.03, 0.03, 0.09, 0.12]</rosparam>
      <rosparam param="selected_points_y">[0.03, 0.12, 0.12, 0.03]</rosparam>
      <rosparam param="selected_points_z">[0.00, 0.00, 0.00, 0.00]</rosparam>

      <!-- 3D coordinates of all points on the calibration pattern. In this example, points are planar -->
      <rosparam param="model_points_x">[0.0, 0.03, 0.06, 0.09, 0.12, 0.15, 0.0, 0.03, 0.06, 0.09, 0.12, 0.15, 0.0, 0.03, 0.06, 0.09, 0.12, 0.15, 0.0, 0.03, 0.06, 0.09, 0.12, 0.15, 0.0, 0.03, 0.06, 0.09, 0.12, 0.15, 0.0, 0.03, 0.06, 0.09, 0.12, 0.15]</rosparam>
      <rosparam param="model_points_y">[0.0, 0.00, 0.00, 0.00, 0.00, 0.00, .03, 0.03, 0.03, 0.03, 0.03, 0.03, .06, 0.06, 0.06, 0.06, 0.06, 0.06, .09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.12,0.12, 0.12, 0.12, 0.12, 0.12, 0.15,0.15, 0.15, 0.15, 0.15, 0.15]</rosparam>
      <rosparam param="model_points_z">[0.0, 0.00, 0.00, 0.00, 0.00, 0.00, 0.0, 0.00, 0.00, 0.00, 0.00, 0.00, 0.0, 0.00, 0.00, 0.00, 0.00, 0.00, 0.0, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.0, 0.00, 0.00, 0.00, 0.00,0.00]</rosparam>

      <!-- Tracking parameters used in image processing -->
      <param name="gray_level_precision" value="0.7" />
      <param name="size_precision" value="0.5" />

      <!-- Behaviour of the interface -->
      <param name="pause_at_each_frame" value="False" />
</node>
```



### Camera calibrator

You can run the calibrator without any parameters.



```xml
<node pkg="visp_camera_calibration" name="visp_camera_calibration_calibrator" type="visp_camera_calibration_calibrator"/>
```



### Experimental camera

For testing purposes, the package contains a camera satisfying the
standard ROS camera interface. The camera reads a video or a sequence of
images and is configured as follows:



```xml
<node pkg="visp_camera_calibration" name="visp_camera_calibration_camera" type="visp_camera_calibration_camera">
	<param name="images_path" value="images/grid36-0%d.pgm" />
```



<a id="ROS_API"></a>

## ROS API



```clearsilver
name = visp_camera_calibration_image_processing
desc = The image processing module subscribes to the image feed from a camera, displays it to the user in order to select the (four) points used to initialise the image processing. Then, it processes the images to extract every possible keypoint. Finally it publishes the processed data to a calibrator topic.

sub {
  0.name = image
  0.type = sensor_msgs/Image
  0.desc = raw image topic, feed from camera
}

pub {
  0.name = point_correspondence
  0.type = visp_camera_calibration/CalibPointArray
  0.desc = array of 2D/3D point pairs used to calibrate the camera
}

param {
  group.0 {
    0.name = gray_level_precision
    0.type = double
    0.desc = Gray level precision used to detect the dot boundaries in ]0, 1]. 1 means full precision, whereas values close to 0 show a very bad accuracy.
    0.default = 0.7
  }
  group.1 {
    1.name = size_precision
    1.type = double
    1.desc = Size precision of the dot in ]0, 1]. Used to test the validity of the dots that are detected in the image. 1 means that all the dots should have the same size, whereas values close to 0 allows variation in the dot size. To desactivate validity test set size_precision to 0.
    1.default = 0.5
  }
  group.2 {
    2.name = pause_at_each_frame
    2.type = bool
    2.desc = If True, pauses the interface each time a new frame is recieved. Consequently, the user selects points at each frame. You should set this to True only with the experimental camera shipped with the package.
    2.default = False
  }

  group.3 {
    3.name = model_points_x
    3.type = array
    3.desc = List of x coordinates of the model points.
  }


  group.4 {
    4.name = model_points_y
    4.type = array
    4.desc = List of y coordinates of the model points.
  }


  group.5 {
    5.name = model_points_z
    5.type = array
    5.desc = List of z coordinates of the model points.
  }

  group.6 {
    6.name = selected_points_x
    6.type = array
    6.desc = List of x coordinates of model 3D points corresponding to the user-selected points.
  }


  group.7 {
    7.name = selected_points_y
    7.type = array
    7.desc = List of y coordinates of model 3D points corresponding to the user-selected points.
  }


  group.8 {
    8.name = selected_points_z
    8.type = array
    8.desc = List of z coordinates of model 3D points corresponding to the user-selected points.
  }

  group.9 {
    9.name = calibration_path
    9.type = string
    9.desc = Location of the ini file to write calibration configuration into.
  }
}
```





```clearsilver
name = visp_camera_calibration_calibrator
desc = This node computes the camera calibration parameters and calls the <<SrvLink(sensor_msgs/SetCameraInfo)>> service on the current camera. It produces a calibration.ini file that will be in your $HOME/.ros directory.

sub {
  0.name = point_correspondence
  0.type = visp_camera_calibration/CalibPointArray
  0.desc = array of 2D/3D point pairs used to calibrate the camera
}

pub {
  0.name = point_correspondence
  0.type = visp_camera_calibration/CalibPointArray
  0.desc = array of 2D/3D point pairs used to calibrate the camera
}

srv_called {
  0.name = set_camera_info
  0.type = sensor_msgs/SetCameraInfo
  0.desc = Sets the camera info.
}
```





```clearsilver
name = visp_camera_calibration_camera
desc = This is an experimental camera node used for test purposes.

pub {
  0.name = image
  0.type = sensor_msgs/Image
  0.desc = raw image topic, feed from camera
}

srv_called {
  0.name = calibrate
  0.type = visp_camera_calibration/calibrate
  0.desc = Get the camera parameters according to the chosen camera model, with or without distorsion and the size of the images.
}
```

## Running a calibration using visp_camera_calibration's experimental camera

### Compiling

Start by getting the dependencies and compiling the package.



```
{#!wiki buildsystem catkin
{{{
rosdep install visp_camera_calibration
catkin_make -DCMAKE_BUILD_TYPE=Release --pkg visp_camera_calibration
```

 }}}}



```
{#!wiki buildsystem rosbuild
{{{
rosdep install visp_camera_calibration
rosmake visp_camera_calibration
```

 }}}}

### Configuring a camera using a point-based grid

This tutorial demonstrates how to use the camera simulator to broadcast
images of a point-based planar sample grid and calibrate the camera
accordingly. There are four example images shipped with this package.
They are located in `launch/images`.

#### Launching nodes

You need to launch the following node combination:

- the camera simulator
- the image processing interface
- the calibrator
- the console (rxtools/rxconsole)

All this has already been written into the roslaunch file located in
`vision_visp/visp_camera_calibration/launch/lagadic_grid.launch`. You
only need to launch:



```
roslaunch visp_camera_calibration lagadic_grid.launch
```



#### Image processing initialisation interface

Several windows will appear:

![width=100%](doc/calib_windows.png)

In the rxconsole, you will see instructions about how to proceed and
information about the calibration process. Some information will also be
shown as red text over the images. You may choose to filter the messages
by excluding the camera node.

#### Calibration process

Start by clicking on the camera window. This will start streaming the
camera feed from start to end. Chances are the streaming will be
finished before you start selecting points. This is perfectly normal, no
data is lost and it will be displayed to the image processing interface,
image by image.

Once you have clicked on the camera window, you need to select points in
the window called "Image processing initialisation interface".

![width=100%](doc/calib_start_select.png)

When the four points are selected, the image processing initialisation
interface will try to detect the rest of the points. Your grid should
look like this:

![width=100%](doc/calib_detection.png)

Then, click on the interface window again and repeat the process until
the image displayed by the image processing initialisation interface
window is the same as the one displayed by the camera window.

The calibrator node now has enough information to compute the new camera
parameters. Click once on the \*camera window\* to call the camera
calibration service. You should also make sure the camera node is
enabled on the console.

Your console should look like that:

![width=100%](doc/calib.png)

In fact, the calibrator node calls the
[sensor_msgs/srv/SetCameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/srv/SetCameraInfo.html)
service advertised by the camera node. The camera simulator merely logs
this output so you can display it in the ROS format.

Let's have a look at the console. The output includes information about
standard deviations. These errors may serve as an indicator of your
calibration's quality. They should be reasonably low (not more than a
few pixels). Otherwise you should think about using more or different
image samples.

The node will also write a calibration.ini file (in your \$HOME/.ros
directory) containing the calibration parameters in the INI format,
similiary to the console log: 

```
# Camera intrinsics

[image]

width
640

height
480

[image_raw]

camera matrix
548.83913 0.00000 309.68288 
0.00000 541.05367 246.39086 
0.00000 0.00000 1.00000 

distortion
-0.01019 0.00000 0.00000 0.00000 0.00000 

rectification
1.00000 0.00000 0.00000 
0.00000 1.00000 0.00000 
0.00000 0.00000 1.00000 

projection
548.83913 0.00000 309.68288 0.00000 
0.00000 541.05367 246.39086 0.00000 
0.00000 0.00000 1.00000 0.00000
```



If you want to change the location of that file, you can set the
calibration_path parameter or just run 

```
roslaunch visp_camera_calibration lagadic_grid.launch calibration_path:="/path/to/calibration.ini"
```

## Calibration of an external camera using the ViSP library

### Before starting

Make sure you have the following:

- A ROS-compatible camera driver. You can use the experimental
  visp_camera_calibration_camera node for this.
- A calibration pattern. You can print the
  [pattern used in the lagadic laboratory](doc/grid2d.pdf).
- A 3D model of your grid.
- A reasonably well-lit space to display the calibration pattern from
  various angles.

### Compiling

Start by getting the dependencies and compiling the package.



```
{#!wiki buildsystem catkin
{{{
rosdep install visp_camera_calibration
catkin_make -DCMAKE_BUILD_TYPE=Release --pkg visp_camera_calibration
```

 }}}}



```
{#!wiki buildsystem rosbuild
{{{
rosdep install visp_camera_calibration
rosmake visp_camera_calibration
```

 }}}}

### Setting up

#### Camera

Plug in your camera and install the corresponding ROS package to be able
to grab images.

If your camera is firewire install the
[camera1394](https://index.ros.org/p/camera1394) package. For simplicity
sake, start creating a roslaunch file: `calib-live-firewire.launch`.
To grab and display 640x480 images in mono8 format from this camera it
should have the following structure:



```
<launch>
  <!-- % rxconsole -->
  <node pkg="rqt_console" name="rqt_console" type="rqt_console"/>
  <!-- % rosrun camera1394 camera1394_node -->
  <node pkg="camera1394" type="camera1394_node" name="my_camera1394_node" args="_video_mode:=640x480_mono8"/>
  <!-- % rosrun image_view image_view image:=/camera/image_raw -->
  <node pkg="image_view" type="image_view" name="my_image_raw_viewer" args="image:=/camera/image_raw"/> 
</launch>
```



Make sure your camera is publishing on the topic image_raw. This is a
standard ROS topic for cameras. You can check this by doing:


```
rostopic list
```



#### Image processing

Modify the roslaunch file `calib-live-firewire.launch` to add the
following lines: 

```
<launch>
	...
        <arg name="calibration_path" default="calibration.ini" />
	<group ns="visp_camera_calibration">
		<node pkg="visp_camera_calibration" name="visp_camera_calibration_calibrator" type="visp_camera_calibration_calibrator"/>
		<node pkg="visp_camera_calibration" name="visp_camera_calibration_image_processing" type="visp_camera_calibration_image_processing" args="camera_prefix:=/camera">
		      <param name="gray_level_precision" value="0.7" />
		      <param name="size_precision" value="0.5" />
		      <param name="pause_at_each_frame" value="False" />
                      <param name="calibration_path" type="string" value="$(arg calibration_path)" />
		</node>
	</group>
</launch>
```



The camera_prefix argument used in the previous lines indicates
`/camera` as the base path for camera services and topics.
Consequently, the calibrator will subscribe to `/camera/image_raw` and
will call the service `/camera/set_camera_info`.

#### Calibration grid pattern

Print your pattern on way you have the biggest contrast to make tracking
easier. Your pattern should be set of points. Measure and/or enter the
3D coordinates of your points in the object frame. Chances are you
printed the pattern on a piece of paper; if so, all your points will
have the same Z coordinate.

Fill the model definition into the lauch file. To do so, you'll have to
set define three parameters, each one corresponding to a point
coordinate (X,Y or Z). You need to do that for each point:



```
<launch>
	...
	<group ns="visp_camera_calibration">
		<node pkg="visp_camera_calibration"  ... >
		      ...

                      <!-- 3D coordinates of all points on the calibration pattern. In this example, points are planar -->
                      <rosparam param="model_points_x">[0.0, 0.03, 0.06, 0.09, 0.12, 0.15, 0.0, 0.03, 0.06, 0.09, 0.12, 0.15, 0.0, 0.03, 0.06, 0.09, 0.12, 0.15, 0.0, 0.03, 0.06, 0.09, 0.12, 0.15, 0.0, 0.03, 0.06, 0.09, 0.12, 0.15, 0.0, 0.03, 0.06, 0.09, 0.12, 0.15]</rosparam>
                      <rosparam param="model_points_y">[0.0, 0.00, 0.00, 0.00, 0.00, 0.00, .03, 0.03, 0.03, 0.03, 0.03, 0.03, .06, 0.06, 0.06, 0.06, 0.06, 0.06, .09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.12,0.12, 0.12, 0.12, 0.12, 0.12, 0.15,0.15, 0.15, 0.15, 0.15, 0.15]</rosparam>
                      <rosparam param="model_points_z">[0.0, 0.00, 0.00, 0.00, 0.00, 0.00, 0.0, 0.00, 0.00, 0.00, 0.00, 0.00, 0.0, 0.00, 0.00, 0.00, 0.00, 0.00, 0.0, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.0, 0.00, 0.00, 0.00, 0.00,0.00]</rosparam>
		</node>
	</group>
</launch>
```



#### 3D coordinates of the points used for initialisation

You also need to select a smaller number (4 for example) of 3D points on
your model. These points will be the starting point for pose
estimations. Add these points to the launch file the same way you wrote
the model definition:



```
<launch>
	...
	<group ns="visp_camera_calibration">
		<node pkg="visp_camera_calibration" ... >
		      ...
                      <!-- 3D coordinates of 4 points the user has to select to initialise the calibration process -->
                      <rosparam param="selected_points_x">[0.03, 0.03, 0.09, 0.12]</rosparam>
                      <rosparam param="selected_points_y">[0.03, 0.12, 0.12, 0.03]</rosparam>
                      <rosparam param="selected_points_z">[0.00, 0.00, 0.00, 0.00]</rosparam>

		</node>
	</group>
</launch>
```



Note that the matching between these 3D coordinates of the points and
the 2D pixel coordinates is done by the user when he is asked to click
on the points.

### Running the calibration

#### Doing the image processing

To start the calibration, just type: 

```
roslaunch calib-live-firewire.launch
```



The full calib-live-firewire.launch file is available
[here](doc/calib-live-firewire.launch).

Three nodes will be launched (besides the camera):

- The console
- The calibrator node which will stay silent
- The image processing interface node with which you will interact.

In the rqt_console, you will see instructions about how to proceed and
information about the calibration process. Some information will also be
shown as red text over the images.

Move the printed pattern somewhere in the field of view of the camera.
The image should appear:
![attachment:waiting_to_stop.png](doc/waiting_to_stop.png)

When you are ready, click anywhere on the window. Once you have clicked,
you need to select points in the window called "image processing
initialisation interface". Select the special points you defined
earlier in the xml file.
![attachment:calib_click_points_solo.png](doc/calib_click_points_solo.png)

When the four points are selected, the image processing interface will
try to detect the rest of the points. Your grid should look like this:
![attachment:calib_detected_projected_solo.png](doc/calib_detected_projected_solo.png)
Then, click on the interface window again and repeat the process until
you have processed enough samples.

The calibrator node now has enough information to compute the new camera
parameters. You are now ready to call the calibration service.

#### Calibrating

In a new terminal type: 

```
rosservice call visp_camera_calibration/calibrate 2 640 480
```

 Those parameters may
not seem intuitive to you, here is a quick overview:

- 2 is a code refering to a calibration model with distorsion. You can
  also set 1 to estimate a model without distorsion.
- 640 and 480 are the width and height of the image.

#### Calibration Results

You should have the following output: 

```
stdDevErrs: [0.43714855418957455, 0.5039971167151152, 0.4991662359530044, 0.4800084572634955]
```



The quantities are expressed in pixels and should be reasonably low.

The node will then attempt to set the calculated camera info to the
calibrated camera. If possible, it will also write a calibration.ini
file (in your `\$HOME/.ros` directory) containing the calibration
parameters in the INI format: 

```
# Camera intrinsics

[image]

width
640

height
480

[image_raw]

camera matrix
548.83913 0.00000 309.68288 
0.00000 541.05367 246.39086 
0.00000 0.00000 1.00000 

distortion
-0.01019 0.00000 0.00000 0.00000 0.00000 


rectification
1.00000 0.00000 0.00000 
0.00000 1.00000 0.00000 
0.00000 0.00000 1.00000 

projection
548.83913 0.00000 309.68288 0.00000 
0.00000 541.05367 246.39086 0.00000 
0.00000 0.00000 1.00000 0.00000
```



### Links to go further

Once you've obtained the camera parameters, you can load them into your
camera and use them to rectify your image. Standard ROS cameras are able
to load yml or ini calibration files by using the
[camera_info_manager](https://index.ros.org/p/camera_info_manager)
package. This may be simplified with a graphical user interface. Check
the [camera1394](https://index.ros.org/p/camera1394) package and the
[dynamic reconfigure](https://index.ros.org/p/dynamic_reconfigure)
package to see how to graphically load camera parameters into the camera
node.

Once the camera is configured you should use the
[image_proc](https://index.ros.org/p/image_proc) package to rectify the
image, as indicated in the
[following tutorial](https://index.ros.org/p/image_proc).

## Tutorials

- [Running a calibration using visp_camera_calibration's experimental camera](#running-a-calibration-using-visp_camera_calibrations-experimental-camera):
  This tutorial explains how to calibrate a camera using the
  experimantal camera shipped with visp_camera_calibration. You don't
  need to own any external camera nor do you need a pattern. It is a
  good first step towards using the package.
- [Calibration of an external camera using the ViSP library](#calibration-of-an-external-camera-using-the-visp-library):
  This tutorials is a step by step guide which shows how to define your
  calibration pattern, model. Then it discusses camera calibration using
  the ViSP library. Finally, it will briefly walk you through the
  calibration results.
