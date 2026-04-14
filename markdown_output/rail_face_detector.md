# Two Minute Intro

This detector uses [Caffe](http://caffe.berkeleyvision.org/) to perform
face detection. It publishes faces found in images from a subscribed
image topic. The face detector itself can be found here:
<https://github.com/kpzhang93/MTCNN_face_detection_alignment>.

The message type coming back from the face detector is a Detections.msg
which contains an array of Face.msg objects. Each Face.msg has:

-   `top_left_x` - X pixel value of top-left corner of bounding box
-   `top_left_y` - Y pixel value of top-left corner of bounding box
-   `bot_right_x` - X pixel value of bottom-right corner of bounding box
-   `bot_right_y` - Y pixel value of bottom-right corner of bounding box
-   `nose_x` - X coordinate of the nose
-   `nose_y` - Y coordinate of the nose
-   `left_eye_x` - X coordinate of the left eye
-   `left_eye_y` - Y coordinate of the left eye
-   `right_eye_x` - X coordinate of the right eye
-   `right_eye_y` - Y coordinate of the right eye
-   `left_mouth_x` - X coordinate of the left corner of the mouth
-   `left_mouth_y` - Y coordinate of the left corner of the mouth
-   `right_mouth_x` - X coordinate of the right corner of the mouth
-   `right_mouth_y` - Y coordinate of the right corner of the mouth

# Nodes

This package contains a single ROS node - `face_detector_node` - which
serves as an interface between a ROS system and the trained face
recognition network.

## face_detector_node

### Topics

#### detector_node/faces

Type:
[face_detector/detections](http://docs.ros.org/indigo/api/rail_face_detector/html/msg/Detections.html)

Topic with face detections performed in the background by running on
images as they come in the subscriber.

#### detector_node/debug/face_images

Type:
[face_detector/debug/face_images](http://docs.ros.org/api/sensor_msgs/html/msg/Image.html)

Topic with face detections visualized on incoming images as they come in
from the subscriber. Only published if debug=true.

### Parameters

#### image_sub_topic_name

Type: `string`

Default: `"/kinect/qhd/image_color_rect"`

Image topic name to use for detections.

#### debug

Type: `bool`

Default: `false`

Enable or disable debug mode, which publishes incoming images with
bounding boxes over faces

#### use_gpu

Type: `bool`

Default: `true`

Enable or disable gpu mode. Enabled by default. Significantly speeds up
detection.

#### use_compressed_image

Type: `bool`

Default: `false`

Change to compressed image stream or not. Simply appends a
\"/compressed\" to the image topic name. This lightens the load your
local network if the images are being transmitted to the detector.
