

```wiki
'''Note:''' You can also check a detailed integration tutorial on [[https://www.leorover.tech/integrations/object-detection|LeoRover Tech - Object detection|target="_blank"]]
```



## Overview

This package contains a ROS node which allows to perform object
detection on [Leo Rover](Robots/Leo Rover). There is also the default
configuration included which contains: 1. File with labels 2. Neural
network models 3. Config file with defined colors for specified labels

It is one of a couple of packages made for showing an example usage of a
stock [Leo Rover](Robots/Leo Rover).

## Usage

### Running object detection with the default configuration

If you want to run object detection with the default configuration,
simply type: 

```
roslaunch leo_example_object_detection detector.launch
```



### Running object detection with custom configuration

The provided launch file has 4 arguments, which let you choose a neural
network model, files with color definitions and label names, as well as
camera view. The arguments are as follows: labels:: The path to the file
with the labels (one label in one line), for the neural network model.



```wiki
'''IMPORTANT:''' If the labels in the file won't be suited for the model, the program might not work properly.
```



camera:: The name of the topic with the camera image - you can specify
which camera view you want to use for detecting objects.

model:: The path to the neural network model. There are already two
models given (both need the COCO labels), but you can provide a model of
your choice.

config_file:: The path to the config file with the ROS params defining
colors for specified labels.



```wiki
'''Note:''' See the [[http://wiki.ros.org/leo_example_object_detection#rosapi|ROS API]] section for more details about the parameters.
```



Therefore, an example usage with custom configuration looks like this:


```
roslaunch leo_example_object_detection detector.launch config_file:=<path_to_config> model:=<path_to_model> labels:=<path_to_labels> camera:=<topic_name>
```



## ROS API

<a id="rosapi"></a>

### object_detector

#### Subscribed Topics

- `camera/image_raw`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Camera images used for object detection.

#### Published Topics

- `detections/compressed`
  ([sensor_msgs/msg/CompressedImage](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CompressedImage.html)):
  An image with labels and boxes drawn around the detected objects (an
  object is detected only when the model's confidence is above the
  threshold specified by the parameter).

#### Parameters

##### Parameters specified in a yaml file. An example values for the parameters are available in the label_colors.yaml file in the config directory.

- `labels` (`string list`): The labels for which the color is specified
  in the *colors* parameter. The first label will have the first color,
  the second label the second color etc.
- `colors` (`int list list`): The colors in RGB format - each inner list
  is a color definition. The first color will be assigned to the first
  label from the *labels* parameter, the second color to the second
  label etc.

##### Parameters controlled by the dynamic_reconfigure package:

- `confidence` (`int`, default: `60`): The confidence threshold for the
  model, for showing the detected objects.
