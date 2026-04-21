## Description

A collection of helper functions for the pi_vision stack for subscribing
to image topics, converting them to OpenCV format for further processing
by other nodes, and displaying processed images and markers.

## How To Use

-   To launch a ros2opencv node using the Kinect RGB-D camera, use:
    ```
$ roslaunch ros2opencv openni_node.launch
```

```{=html}
<!-- -->
```
-   To launch a ros2opencv node using a UVC-compatible webcam, use:
    ```
$ roslaunch ros2opencv uvc_cam.launch
```

```{=html}
<!-- -->
```
-   To load an AVI file and re-publish it on the topic
    /camera/image_raw: ```
$ roslaunch ros2opencv avi2ros.launch input:=/path/to/avi/file
```

```{=html}
<!-- -->
```
-   To publish the video on a different topic, use rosrun instead of
    roslaunch: ```
$ rosrun ros2opencv avi2ros.py _input:=/path/to/avi/file output:=/your_topic
```

(Note the underscore in front of _input but not in front of output.)

## Nodes

```clearsilver
name = ros2opencv.py
desc = A ROS node for subscribing to a ROS image topic, converting the image to OpenCV format, then displaying the processed image to the user along with possible text and graphic markers.
sub {
  0.name = ~input_rgb_image
  0.type = sensor_msgs/Image
  0.desc = The ROS image topic to convert to OpenCV for further processing, e.g. /camera/rgb/image_color when using a Kinect and the openni_camera package.
  1.name = ~input_depth_image
  1.type = sensor_msgs/Image
  1.desc = The ROS image topic containing depth information, e.g. /camera/depth/image when using a Kinect and the openni_camera package.
}
pub {
  0.name = /output_image (remapped in pi_face_tracker launch files to /pi_face_tracker/image)
  0.type = sensor_msgs/Image
  0.desc = The display image including markers republished from OpenCV to ROS
}
```

```clearsilver
name = avi2ros.py
desc = A ROS node for reading an AVI video file using OpenCV and re-publishing it as a ROS image topic.  See the same launch file commands lines above for usage.

param {
  0.name = ~input
  0.type = str
  0.desc = Path to the AVI file to re-publish on the /output topic.
  0.default = None
  1.name = ~start_paused
  1.type = boolean
  1.desc = Start the video in the paused state.  Useful if you want to select a region before the video starts.
  1.default = False
  2.name = ~loop
  2.type = boolean
  2.desc = Continuously loop the video once it reaches the end.
  2.default = False
  3.name = ~fps
  3.type = int
  3.desc = Run the video at fps frames per second.
  3.default = 25
}

pub {
  0.name = /output
  0.type = sensor_msgs/Image
  0.desc = The ROS Image stream corresponding to the input AVI file.  Can be remapped on the command line or in a launch file.
}
```
