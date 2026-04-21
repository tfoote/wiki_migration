## What does re_vision do?

The re_vision package contains the !ObjectDetector node, that allows to
recognize known objects in images. The data returned are the 3D pose of
the object and the location in the image of some pixels that belong to
the object.

There is also an !ObjectDetectorDummy node that allows to recognize a
predefined local object in the gazebo simulator.

## Invocation

```
$ rosrun re_vision ObjectDetector [options] [camera_info:=/your/camera_info]
$ rosrun re_vision ObjectDetectorDummy [options] [camera_info:=/your/camera_info]
$ roslaunch re_vision gazebo.launch
```

The first line runs the !ObjectDetector node, which must be notified the
object models to load via topic. The !ObjectDetectorDummy behaves the
same as the former, but it also loads a predefined model, available for
the gazebo simulator (name "cabinet1"). The easiest way to run
!ObjectDetectorDummy is with the gazebo.launch file, because you do not
have to take care of the location of the predefined model. Both nodes
need that parameters of the camera that provides the images. These are
obtained from the `/camera_info topic` (see below). You may want to
remap this topic in the gazebo.launch file or in the command line.

Options:

-   `-d`: debug flag. If given, debug images of the recognition
    process are saved in `./debug/debug_\[timestamp\]`.
-   `-v`: visualization flag. If given, detection images are sent by
    the topic `/re_vision/detector_visualization`.
-   `-c`: predefined_camera: load parameters of a predefined camera.
    This option is used for debugging purposes only. The camera models
    and their parameters are defined in
    `re_vision/src/CameraBridgeFactory.cpp`.

## Interface

### ROS Topics

```clearsilver

sub {
    0.name = /camera_info
    0.type = sensor_msgs/CameraInfo
    0.desc = This topic is used to retrieve the intrinsic parameters and the distortion model of the camera that will provide the images. The information is read only once; after that, the topic is not listened any longer. You may want to remap this topic when running the !ObjectDetector.

    1.name = /re_vslam/new_model
    1.type = std_msgs/String
    1.desc = When a new object model has been downloaded from the !RoboEarth database, !ObjectDetector is notified with this topic that the new model is available. After getting this topic, the model is learnt, so that it can be searched for in the following given images.  

}

pub {
    0.name = /re_vision/detector_visualization
    0.type = sensor_msgs/Image
    0.desc = If the -v option is given, !ObjectDetector sends images of the recognition process by this topic. These images can be later visualized with [[image_view]].
}
```

### ROS Services

```clearsilver
srv {
    0.name = /re_vision/search_for
    0.type = re_vision/SearchFor
    0.desc = Searchs the image for the given objects. Only those objects whose name are given are searched for. If an object is recognized in the image, up to !MaxPointsPerObject points from this are returned. If !MaxPointsPerObject is negative, all of them are returned. If the i-th object given is not detected, the corresponding arrays in Detections will be empty. The axes in the camera reference system are oriented as in the robot: X looks forward, Y points left and Z goes up.


}
```
