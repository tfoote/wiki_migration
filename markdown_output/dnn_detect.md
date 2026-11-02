## Nodes

### dnn_detect

dnn_detect uses the
[OpenCV Deep Neural Network module](https://docs.opencv.org/3.3.0/d2/d58/tutorial_table_of_content_dnn.html)
to find objects in an image stream and provide their bounding boxes.

#### Subscribed Topics

- `/camera`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  The images to be processed.

#### Published Topics

- `/dnn_objects`
  ([dnn_detect/msg/DetectedObjectArray](https://docs.ros.org/en/rolling/p/dnn_detect/msg/DetectedObjectArray.html)):
  Details of detected objects
- `/dnn_images`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Input image with detected objects outlined

#### Services

- `~detect`
  ([dnn_detect/srv/Detect](https://docs.ros.org/en/rolling/p/dnn_detect/srv/Detect.html)):
  Trigger a detection when in single-shot mode

#### Parameters

- `~single_shot` (`bool`, default: `false`): If set, detection is only
  performed when the `detect` service is called
- `~publish_images` (`bool`, default: `true`): If set, images with
  objects outlined will be published
- `~data_dir` (`string`): Path to directory containing data
- `~protonet_file` (`string`): Name of protonet file, relative to
  `data_dir`
- `~caffe_model_file` (`string`): Name of caffe model file, relative to
  `data_dir`
- `~min_confidence` (`float`, default: `0.2`): Minimum confidence (0..1)
  for an object to be included in the results
- `~im_size` (`int`, default: `300`): size of image (pixels) to operate
  on
- `~scale_factor` (`float`, default: `0.007843`): Scale factor for
  model - the intensity values in the image are multiplied by this
- `~mean_val` (`float`, default: `127.5`): Mean value for model - this
  is subtracted from the intensity values in the image
- `~class_names` (`string`, default:
  `background, aeroplane, bicycle, bird, boat, bottle, bus, car, cat, chair, cow, diningtable, dog, horse, motorbike, person, pottedplant, sheep, sofa, train, tvmonitor`):
  Comma delimited list of class names

## Installation



```
sudo apt install ros-kinetic-dnn-detect
```



## Sample Usage

The sample launch file uses
[chuanqi305's MobileNet-SSD](https://github.com/chuanqi305/MobileNet-SSD)

A camera node, such as [usb_cam](https://index.ros.org/p/usb_cam) needs
to be running

For example: 

```
rosrun usb_cam usb_cam_node
```



Then `dnn_detect` can be launched: 

```
roslaunch dnn_detect dnn_detect.launch camera:=/usb_cam image:=image_raw
```

 and the
results viewed with: {{ rqt_image_view /dnn_images or:


```
rostopic echo /dnn_objects
```
