# Two Minute Intro

This package includes two object detectors which you may choose between,
YOLOv2 and Deformable R-FCN (DRFCN). Detections from YOLOv2 are a bit
faster, \>10fps compared to 4fps (on a Titan X), but less accurate than
the detections from DRFCN.

The YOLOv2 detector uses [darknet](https://github.com/pjreddie/darknet)
to perform object detection. It provides the ability to query for
objects in an image through both services as well as from a topic.

The [Deformable R-FCN](https://github.com/msracver/Deformable-ConvNets)
detector is built on MXNet, and provides the ability to query for
objects from a topic.

The nodes in this package publish a list of
[objects](http://docs.ros.org/indigo/api/rail_object_detection_msgs/html/msg/Object.html)
within a given image, each of which has the following properties:

1\. `label` 1. `probability` - confidence value in recognition 1.
`centroid_x` - X pixel value of the centroid of the bounding box 1.
`centroid_y` - Y pixel value of the centroid of the bounding box 1.
`left_bot_x` - X pixel value of bottom-left corner of bounding box 1.
`left_bot_y` - Y pixel value of bottom-left corner of bounding box 1.
`right_top_x` - X pixel value of top-right corner of bounding box 1.
`right_top_x` - X pixel value of top-right corner of bounding box

The DRFCN detector requires a CUDA and cuDNN capable GPU, so it is not
installed by default. In order to use it, we recommend getting this code
from Github and following the instructions in the
[README](https://github.com/GT-RAIL/rail_object_detector#building-with-cuda).
The rest of this documentation covers instructions for a CPU-only
install of this package that uses darknet.

## Querying through services

There are two modes of querying:

-   Scene Queries
-   Image Queries

Scene Queries are served by first subscribing to an existing camera
sensor topic. Then at the moment of the query, we run object recognition
on the latest frame from the camera and the resulting objects in that
scene are returned after however long darknet takes.

Image Queries require an image to be sent alongwith the query. Object
recognition is performed on this input image, and the detected objects
as well as the original image are sent back.

## Querying through topic

If enabled, the detector subscribes to an existing camera sensor topic
and grabs images from this camera at (prespecified) intervals. After
performing object detection on the grabbed image, the detector publishes
the list of objects that were found to the query topic and with the
timestamp of the image which was grabbed for detection.

The interval for grabbing images is specified in the form of a
frequency. If the desired frequency exceeds the maximum frequency of
operation of the detector (1 Hz on CPU), we limit to the maximum
frequency of operation.

# Nodes

This package contains a single ROS node - `darknet_node` - which serves
as an interface between a ROS system and the trained object recognition
network.

## darknet_node

### Services

#### darknet_node/objects_in_scene

Type:
[rail_object_detector/SceneQuery](http://docs.ros.org/indigo/api/rail_object_detection_msgs/html/srv/SceneQuery.html)

**Scene Query service**: recognize objects in the latest image from the
camera stream `image_sub_topic_name`. Takes no input, and outputs a list
of detected, labeled objects and a corresponding image. Only advertised
if `use_scene_service` is true.

#### darknet_node/objects_in_image

Type:
[rail_object_detector/ImageQuery](http://docs.ros.org/indigo/api/rail_object_detection_msgs/html/srv/ImageQuery.html)

**Image Query service**: recognize objects in an image passed to the
service. Takes an image as input, and outputs a list of detected,
labeled objects and a corresponding image. Only advertised if
`use_image_service` is true.

### Topics

#### darknet_node/detections

Type:
[object_detector/detections](http://docs.ros.org/indigo/api/rail_object_detection_msgs/html/msg/Detections.html)

Topic with object detections performed in the background by grabbing
images at a specified interval. Only advertised if
`publish_detections_topic` is true.

### Parameters

#### num_service_threads

Type: `int`

Default: `0`

Number of asynchronous threads that can be used to service each of the
services. `0` implies the use of one thread per processor

#### use_scene_service

Type: `bool`

Default: `true`

Enable or disable Scene Query service

#### use_image_service

Type: `bool`

Default: `false`

Enable or disable Image Query service

#### publish_detections_topic

Type: `bool`

Default: `false`

Enable or disable Detections topic

#### image_sub_topic_name

Type: `string`

Default: `"/kinect/hd/image_color_rect"`

Image topic name to subscribe to for the Scene Query service or the
Detections topic

#### max_desired_publish_freq

Type: `float`

Default: `1.0`

Desired frequency of object detection. If frequency exceeds maximum
detector frequency that Darknet can manage, the desired value will not
be achieved

#### probability_threshold

Type: `float`

Default: `0.25`

Confidence value in recognition below which a detected object is treated
as unrecognized

#### classnames_filename

Type: `string`

Default: `"$(find rail_object_detector)/libs/darknet/data/coco.names"`

Trained labels file for Darknet. Make sure to use an absolute path. See
Darknet for details on file itself.

#### cfg_filename

Type: `string`

Default: `"$(find rail_object_detector)/libs/darknet/cfg/yolo.cfg"`

Configuration file for Darknet. Make sure to use an absolute path. See
Darknet for details on file itself.

#### weight_filename

Type: `string`

Default: `"$(find rail_object_detector)/libs/darknet/yolo.weights"`

Trained weights file for Darknet. Make sure to use an absolute path. See
Darknet for details on file itself.

A good set of weights, to complement the default trained labels can be
obtained from
[this Google Drive link](https://drive.google.com/file/d/0B4jFwTFPtfejVUloYjU2LUpKUVk/view?usp=sharing).

# GPU and MXNet

To build using CUDA, obtain the package from Github and follow the
instructions in the
[README](https://github.com/GT-RAIL/rail_object_detection/tree/indigo-devel/rail_object_detector).
This is necessary if you wish to use the Deformable R-FCN detector.

# Training

The underlying Darknet code has been copied as is. So the detector can
be trained and retrained following instructions on the
[Darknet website](http://pjreddie.com/darknet/).

The same is true for the Deformable R-FCN. Check the
[DRFCN code](https://github.com/msracver/Deformable-ConvNets) for
details.
