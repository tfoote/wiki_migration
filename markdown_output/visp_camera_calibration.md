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
[image_pipeline hardware requirements](image_pipeline#Hardware_Requirements).

## Installation

[visp_camera_calibration](visp_camera_calibration) is part of
[vision_visp](vision_visp) stack.

- To install [visp_camera_calibration](visp_camera_calibration) package
  run 

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
  [here](visp_camera_calibration/Tutorials/CalibrationExperimentalCamera).
- A tutorial that shows how to calibrate using an external camera can be
  found
  [here](visp_camera_calibration/Tutorials/CalibrationExternalCamera).

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


