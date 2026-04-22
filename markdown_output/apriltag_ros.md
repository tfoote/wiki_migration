## Overview

![io_diagram.png](attachment:io_diagram.png)

The package works as shown in the above figure. The following default
input topics are subscribed to (which can be remapped based on your
needs):

-   `/camera_rect/image_rect`: a
    [sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
    topic which contains the image (e.g. a frame of a video stream
    coming from a camera). *The image is assumed to be undistorted, i.e.
    produced by a pinhole camera*. Laptop webcams typically already
    provide such an image while other cameras may require undistortion
    by an intermediate node such as [image_proc](image_proc);
-   `/camera_rect/camera_info`: a
    [sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)
    topic which contains the camera calibration matrix in
    `/camera/camera_info/K`. One can obtain a specific camera's `K`
    via camera intrinsics calibration using e.g.
    [camera_calibration](camera_calibration) or
    [Kalibr](https://github.com/ethz-asl/kalibr) (the former seemed to
    work better for laptop webcam calibration).

The behavior of the ROS wrapper is fully defined by the two
configuration files `config/tags.yaml` (which defines the tags and tag
bundles to look for) and `config/settings.yaml` (which configures the
core !AprilTag 2 algorithm itself). Then, the following topics are
output:

-   `/tf`: relative pose between the camera frame and each detected
    tag's or tag bundle's frame (specified in `tags.yaml`) using
    [tf](tf). Published only if `publish_tf: true` in
    `config/settings.yaml`;
-   `/tag_detections`: the same information as provided by the `/tf`
    topic but as a custom message carrying the tag ID(s), size(s) and
    [geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)
    pose information (where plural applies for tag bundles). This is
    always published;
-   `/tag_detections_image`: the same image as input by
    `/camera/image_rect` but with the detected tags highlighted.
    Published only if `publish_tag_detections_image==true` in
    `launch/continuous_detection.launch`.

## Tutorials

The [tutorials](apriltag_ros/Tutorials) teach you how to operate the
wrapper. The main idea is to fill out `config/tags.yaml` with the
standalone tags and tag bundles which you would like to detect (bundles
potentially require a calibration process) and `config/settings.yaml`
with the wrapper and !AprilTag 2 core parameters. Then, you simply run
the continuous or single image detector. The tutorials walk you through
how to do this.

## Citing

While this ROS wrapper is original code originating from the author's
master thesis, the core !AprilTag 2 algorithm in `apriltags2/` is
wholly the work of the
[APRIL Robotics Lab](https://april.eecs.umich.edu/software/apriltag.html)
at The University of Michigan. If you use this package, please kindly
cite:

-   D. Malyuta,
    "[Navigation, Control and Mission Logic for Quadrotor Full-cycle Autonomy](https://www.research-collection.ethz.ch/handle/20.500.11850/248154),"
    Master thesis, Jet Propulsion Laboratory, 4800 Oak Grove Drive,
    Pasadena, CA 91109, USA, December 2017.
-   J. Wang and E. Olson,
    "[AprilTag 2: Efficient and robust fiducial detection](http://ieeexplore.ieee.org/document/7759617/),"
    in *Proceedings of the IEEE/RSJ International Conference on
    Intelligent Robots and Systems (IROS)*, October 2016.



```
@mastersthesis{malyuta:2017mt,
  author = {Danylo Malyuta},
  title = {{Guidance, Navigation, Control and Mission Logic for Quadrotor Full-cycle Autonomy}},
  language = {english},
  type = {Master thesis},
  school = {Jet Propulsion Laboratory},
  address = {4800 Oak Grove Drive, Pasadena, CA 91109, USA},
  month = dec,
  year = {2017}
}
@inproceedings{Wang2016,
  author = {Wang, John and Olson, Edwin},
  booktitle = {2016 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  doi = {10.1109/IROS.2016.7759617},
  isbn = {978-1-5090-3762-9},
  month = {oct},
  pages = {4193--4198},
  publisher = {IEEE},
  title = {{AprilTag 2: Efficient and robust fiducial detection}},
  year = {2016}
}
```



## Nodes



```clearsilver
node.0{
  name = apriltag_ros
  desc = Detector for a continuous image (i.e. video) stream.
  sub {
    0.name = image_rect
    0.type = sensor_msgs/Image
    0.desc = Undistorted image (i.e. produced by a pinhole camera)
    1.name = camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = Camera information, used only for the camera calibration matrix `K`
  }
  pub {
    0.name = tag_detections
    0.type = apriltag_ros/AprilTagDetectionArray
    0.desc = Array of tag and tag bundle detections' pose relative to the camera
    1.name = tag_detections_image
    1.type = sensor_msgs/Image
    1.desc = Same as `image_rect` but with the detected tags highlighted
  }
  prov_tf {
    0.from = tag
    0.to = camera
    0.desc << EOM
Relative pose of the camera frame to the tag frame. The tag frame here is a placeholder for a standalone tag frame or a tag bundle frame and the specific name can be specified in `config/tags.yaml` or will be set automatically to `tag_ID` or `bundle_COUNT` if ommitted. There will be as many of these transforms as there are specified tags and tag bundles in `config/tags.yaml`.
EOM
  }
  param {
    0.name = tag_family
    0.type = string
    0.desc = !AprilTag family to use for detection. Supported: `tag36h11`, `tag36h10`, `tag25h9`, `tag25h7` and `tag16h5`.
    0.default = `tag36h11`
    1.name = tag_border
    1.type = int
    1.desc = Width of the tag outer (circumference) black border
    1.default = 1
    2.name = tag_threads
    2.type = int
    2.desc = How many threads should the !AprilTag 2 core algorithm use?
    2.default = 4
    3.name = tag_decimate
    3.type = double
    3.desc << EOM
Detection of quads can be done on a lower-resolution image, improving speed at a cost of pose accuracy and a slight decrease in detection rate. Decoding the binary payload is still done at full resolution. .
EOM
    3.default = 1.0
    4.name = tag_blur
    4.type = double
    4.desc << EOM
What Gaussian blur should be applied to the segmented image (used for quad detection?)  Parameter is the standard deviation in pixels.  Very noisy images benefit from non-zero values (e.g. 0.8).
EOM
    4.default = 0.0
    5.name = tag_refine_edges
    5.type = int
    5.desc << EOM
When non-zero, the edges of the each quad are adjusted to "snap to" strong gradients nearby. This is useful when decimation is employed, as it can increase the quality of the initial quad estimate substantially. Generally recommended to be on (1). Very computationally inexpensive. Option is ignored if `tag_decimate==1.0`.
EOM
    5.default = 1
    6.name = tag_refine_decode
    6.type = int
    6.desc << EOM
When non-zero, detections are refined in a way intended to increase the number of detected tags. Especially effective for very small tags near the resolution threshold (e.g. 10px on a side).
EOM
    6.default = 0
    7.name = tag_refine_pose
    7.type = int
    7.desc << EOM
When non-zero, detections are refined in a way intended to increase the accuracy of the extracted pose. This is done by maximizing the contrast around the black and white border of the tag. This generally increases the number of successfully detected tags, though not as effectively (or quickly) as `tag_refine_decode`.
EOM
    7.default = 0
    8.name = publish_tf
    8.type = bool
    8.desc = Enable publishing the tag-camera relative poses on the `/tf` topic
    8.default = false
    9.name = camera_frame
    9.type = string
    9.desc = Camera frame name
    9.default = camera
    10.name = publish_tag_detections_image
    10.type = bool
    10.desc = Enable publishing on the `/tag_detections_image` topic
    10.default = false
  }
}
node.1{
  name = apriltag_ros_single_image_server
  desc << EOM
Detector of tags in a single provided image (via a ROS service which it serves). This is useful for e.g. analyzing a single frame of a video stream (which you maybe think had a faulty tag detection). Starting with, as a baseline, the same description as the [[apriltag_ros#apriltag_ros-1|apriltag_ros node]], this node does not subscribe to any topics, does not output the `/tag_detections_image` topic (the output image is saved in an image save filepath as described below) and does not use the parameters `camera_frame` and `publish_tag_detections_image`. The information below describes additional features of this node.
EOM
  srv {
    0.name = single_image_tag_detection
    0.type = apriltag_ros/AnalyzeSingleImage
    0.desc << EOM
Takes in the '''absolute''' file path of the input image to detect tags in, the '''absolute''' file path where to store the output image (same as input image, with detected tags highlighted) and the camera intrinsics (in particular, the `K` matrix). Returns an <<MsgLink(apriltag_ros/AprilTagDetectionArray)>> of the detected tags' and tag bundles' poses.
EOM
  }
}
node.2{
  name = apriltag_ros_single_image_client
  desc << EOM
A client for the single image tag detection service provided by the [[apriltag_ros#apriltag_ros_single_image_server|apriltag_ros_single_image_server node]]. This node is developed specifically for interacting with this service. Starting with, as a baseline, the same description as the [[apriltag_ros#apriltag_ros-1|apriltag_ros node]], this node does not subscribe to any topics, does not publish any topics and does not use the parameters `camera_frame` and `publish_tag_detections_image`. The information below describes additional features of this node.
EOM
  srv_called {
    0.name = single_image_tag_detection
    0.type = apriltag_ros/AnalyzeSingleImage
    0.desc = See the above description of the `single_image_tag_detection` service provided by the [[apriltag_ros#apriltag_ros_single_image_server|apriltag_ros_single_image_server node]]
  }
  param {
    0.name = image_load_path
    0.type = string
    0.desc = '''Absolute''' file path of the image to detect tags in
    1.name = image_save_path
    1.type = string
    1.desc = '''Absolute''' file path where to save the image with the detected tags highlighted
    2.name = fx
    2.type = double
    2.desc = Camera x focal length (in [px])
    3.name = fy
    3.type = double
    3.desc = Camera y focal length (in [px])
    4.name = cx
    4.type = double
    4.desc = Camera image principal point x coordinate (in [px])
    5.name = cy
    5.type = double
    5.desc = Camera image principal point y coordinate (in [px])
  }
}
```


