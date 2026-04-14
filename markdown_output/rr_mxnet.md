## Description

Package implementing image-based machine learning with the
[MxNet](http://wiki.ros.org/http://mxnet.incubator.apache.org/)
platform. This code and documentation was developed for those working
with the [Rover Robotics](https://roverrobotics.com/)
[OpenRover](http://wiki.ros.org/rr_openrover_basic) (TX1 or TX2).
However, it should work for anyone with a compatible NVidia JetPack
installed TX1 and TX2 (see below in install instructions).

### Packages available

SSD Object Detection

Semantic Segmentation

Combined Segmentation and Monocular Depth Estimation

### Note on Tegra Memory

Because the Tegra platform (and other NVidia embedded platforms) share
main memory (RAM) between the CPU and GPU, you will see a doubling of
the memory used if you enable the GPU in this node. The reason for this
is all backends are now written assuming you have a separate GPU memory
(with a PCIe graphics card, like a GTX1080), which is not the case for
most embedded GPUs. That means the backend calls CUDA to copy the
network and data over to the GPU, which on the Tegra is just another
part of the same main memory, thus doubling the memory used. It may be
possible for the backends to call CUDA differently (e.g. sharing the
same memory location) but it isn\'t well-documented and it may be some
time before someone with time and interest takes on the task.

## Install from source

### Requirements

If using a NVIDIA TX1

-   Jetpack 3.1
-   CUDA 8.0
-   cuDNN 6.0.21
-   OpenCV 2.4.12.1 (stock NVidia JetPack components)

If using a NVIDIA TX2

-   Jetpack 3.2.1
-   CUDA 9.0
-   cuDNN 7.0.5.15
-   OpenCV 3.3.1 (stock NVidia JetPack components)

### Install ROS Package

```
cd ~/catkin_ws/src/
git clone https://github.com/RoverRobotics/rr_mxnet
```

### Download Pre-Built MXNet Bindings (Ubuntu 18.04)

New for JetPack4.2 and TX2 with Ubuntu18.04. Rebuilt mxnet bindings:

-   [TX2 with JetPack4.2 download link](https://drive.google.com/file/d/1il0ogdjt_3QAm5954MXuJrlk_MTiK7Rm/view?usp=sharing)

Install dependencies: ```
sudo apt install python-scipy python3-scipy python-matplotlib python3-matplotlib
sudo pip install tqdm
```

Download and unzip in home directory, cd inside and run
./install_bindings.sh to automatically make links into the
.local/lib/python\[2.7,3.6\]/site-packages/ directories. Keep this
unpacked directory but remove the zipfile when unpacked. When finished,
install gluoncv with pip:

```
pip3 install gluoncv --user
pip2 install gluoncv --user
```

### Download Pre-Built MXNet Bindings (Ubuntu 16.04)

-   [TX1 JetPack3.2.1 download link](https://drive.google.com/open?id=1m4338B8Qstz93HvZFC10akKdmsXMr7JM)
-   [TX2 JetPack3.2.1 download link](https://drive.google.com/open?id=1dzDm3RgArr8aUajWlMcTe7NTZlEPw2wY)
-   [GluonCV 0.3.0 snapshot](https://drive.google.com/open?id=18Xp2sbFBGBMWw7QkpJeEUviaz1GJ9J2O)

Unzip the TX and GluonCV bindings and copy to either the
/usr/local/lib/python2.7/dist-packages/ or the
/.local/lib/python2.7/dist-packages/ area. There may be additional
dependencies required to load GluonCV, at minimum it requires scipy and
the tqdm progress meter. After unpacking the relevant TX and GluonCV
bindings, test they will load in python. Note, GluonCV is in active
development and if you have issues, try the nightly build (pip install
gluoncv \--pre). This GluonCV snapshot zip (commit
6721429cb93637a0f9a7ec8a85deea4d43cb5d62) was verified to work with SSD
and segmentation networks.

```
unzip mxnet_<target>_bindings_<jetpack_cuda_cudnn string>.zip
sudo mv mxnet_<target>_bindings_<jetpack_cuda_cudnn string>/mxnet-1.3.0-py2.7.egg /usr/local/lib/python2.7/dist-packages/.

unzip gluon-cv-0.3.zip
mv gluoncv ~/.local/lib/python2.7/dist-packages/

sudo apt install python-scipy
sudo pip install tqdm
```

Add a link to this package in easy-install.pth in the
/usr/local/lib/python2.7/dist-packages/ subdirectory:
```
./mxnet-1.3.0-py2.7.egg
```

Install required python libraries:

```
sudo apt-get install python-opencv python-matplotlib python-numpy
```

### Test MxNet Installation

```
python
>>> import mxnet as mx
>>> mx.__version___
'1.3.0'
>>> import gluoncv
>>> gluoncv.__version__
'0.3.0'
>>> print mx.nd.zeros((5,5),ctx=mx.gpu(0))

[[ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]]
<NDArray 5x5 @cpu(0)>
```

If you\'re working on a computer other than the TX1 or TX2, and/or if
the above bindings didn't work for you, follow the mxnet documentation
on installation and if you are lucky, pip will work for you. If not,
install from source.

## Download and Run an Example Model

The model parameters for several SSD (single shot detection) networks
are provided by [GluonCV](https://gluon-cv.mxnet.io/), based on MxNet.
These will be downloaded automatically by specifying the relevant
network in the launch file for fast and accurate object detection.
Several example networks provided out-of-the-box with gluoncv include
ResNet50, ResNet100, VGG16, mobilenet1.0 among others. See
[GluonCV\'s Detection Model Zoo](https://gluon-cv.mxnet.io/model_zoo/detection.html)
for up-to-date models. Here is the relevant line in the launch file for
loading a resnet50 (v1) based SSD, trained on the 20-class VOC dataset
and intended to be run on 512x512 sized images:

```
<param name="network" value="ssd_512_resnet50_v1_voc" />
```

Test the detector with an image being published to /usb_cam/image run:

```
roslaunch rr_mxnet example-resnet50-20classes.launch
``` View detections with rqt_image_view

```
rqt_image_view
``` Choose /rr_mxnet/image topic from the dropdown
menu. If all is working well, you should see fresh images and possibly
detections overlain on the image.

### Troubleshooting

If you do not see output, first check the node started and check that
mxnet is working. The node should output a line indicating it has
initialized with the selected model file like so:

```
sudo apt install python-scipy python3-scipy python-matplotlib python3-matplotlib
sudo pip install tqdm
```0

If instead the node gives an error starting MxNet, the following areas
should be checked: the MxNet bindings, GluonCV bindings, the model name
or CUDA/cuDNN/NVidia driver setup.

## Nodes

\_\_SSD Object Detection\_\_ \_\_Semantic Segmentation\_\_

### mxnet_ssd_node

The mxnet_ssd node runs a single shot detector on images from a
subscribed image topic and publishes localization and classification
predictions from a pre-defined list of classes. The localization
consists of relative bounding box locations with respect to the full
image size (xmin, ymin, xmax, ymax) and the classification consists of a
number between 0 and 20 which is converted to a meaningful object string
in the detections topic. The actual detection is performed on a 512x512
resized image that is cropped out of the subscribed image topic. This
node can be configured to crop and resize a single image out of the
image topic or it can be configured to perform a sliding-window set of
crops on the image for better distance detection.

\_\_SSD is a single-shot detector, so why are we specifying a sliding
window pattern?\_\_

To improve detection distance. The detection layers require meaningful
features to produce detections and we don't get useful features until
16-fold reduction in the image. Therefore, to get the best distance
detection, we also use a sliding window method to best match SSD's
capabilities with what we want out of it. However, this will take more
time to complete each set of detections, so find the tradeoff that works
best for you. Note, your camera image quality will be more important for
longer distance performance. If you have a 5 megapixel image, try
zooming in to a 500x500 crop of the image - if this is zoom is
noticeably blurry, you will not get as much benefit from a sliding
window. \<show example images?\> For the first-level sliding window we
only need to specify the number of crops across the larger image
dimension (typically width) as it will take crops that are sized to the
smaller image dimension (e.g. height). For the second-level sliding
window, we need to specify the number of crops across both dimensions
and the crop size. The detector will work out the resulting overlap of
the crops (depends on your application, you could aim for 20% at first)
and report this in both dimensions on the node standard output. This
will require a little trial and error to tune.

\_\_Image Sizes\_\_

A brief aside on image sizes, most often the x-dimension (width) of an
image is larger than the y-dimension (height), with an aspect ratio of
4:3 being common (e.g. 640x480 images have an aspect ratio of 4:3).
However, the detector can only accept square image inputs, so if you are
not specifying a sliding window crop, you have two choices: 1) resize
the non-square image to square, which will squish one dimension, or 2)
center crop the non-square image to a square image with the same minimum
dimension (e.g., a 640x480 image could be cropped to 480x480, discarding
a column of 15% of the pixels on each side). It is possible someone will
have a vertical camera and want to use this code, so we let you
configure this. By default the code will center-crop.

#### Subscribed Topics

/rr_mxnet_ssd/enable std_msgs::Bool

. Controls whether detection is run on the subscribed image topic. This
is used to enable and disable the heavy processing required for
detection as needed. By default, the node will start disabled unless
specified in the start_enabled parameter.

/rr_mxnet_ssd/zoom std_msgs::Bool

. Controls whether a second layer of detection with a sliding window is
enabled. By default, zoom mode is disabled unless specified in the zoom
parameter.

/usb_cam/image_raw sensor_msgs::Image

. Image topic to perform detections on.

/rr_mxnet_segmentation/segmentation_mask sensor_msgs::Image

. Image mask topic to restrict detections. Must be same sized image as
the image topic for detections.

/rr_mxnet_ssd/mask_overlap std_msgs::Int32

. Ranges from 0 to 100. Controls whether to use a mask to restrict
detections. If mask_overlap is set greater than 0, then object
detections are restricted to boxes that overlap at least the
mask_overlap percentage with mask==255 pixels. Conversely, if
mask_overlap is set to 0, then the mask is ignored.

#### Published Topics

/image sensor_msgs::Image /image/compressed sensor_msgs:CompressedImage

. Only published if publish_detection_images is set to True. Publishes
images with bounding boxes and detection strings overlain.

/detections vision_msgs::Detection2DArray

. Publishes object detections in an array of Detection2D.

/detections/\<class name\> std_msgs::Bool

. Publishes boolean detection for each class. E.g. if classes are \"dog,
person\", there will be one each of /class_detections/dog and
/class_detections/person and will publish true for a detection above
threshold on said class and false otherwise.

#### Parameters

image_topic (String, default \"/usb_cam/image_raw\")

. Image topic to perform detections on.

detections_topic (String, default /detections)

. Detections2DArray topic to publish detections.

image_detections_topic (String, default /image)

. Image topic to publish images with detections overlain.

throttle_timer (Int32 or Float, default 5)

. Seconds to wait between detections. If timer is set to less than the
possible detection rate, the node will run inference as fast as possible
and probably take up most of the computer\'s resources (CPU or GPU).

latency_threshold (Int32 or Float, default 2)

. Seconds to allow the images to get stale before discarding and waiting
for next new image. In the worst case, if there is substantial time
delay between the image publisher and reception of images by this node,
this may need to be increased just to allow the node to function. In
typical low latency systems, this can be decreased below 1 second. Note,
the time difference between any published detection.header.stamp and the
source_img.header.stamp may be larger than this due to the additional
time taken by inference. On a laptop with GTX1050 and a usb_cam node
running, this latency was able to go as low as 0.2 with no impact on
lost images.

start_enabled (Bool, default False)

. Use this to have the detector start running as soon as it is loaded.

publish_detection_images (Bool, default False)

. Publish or do not publish images with bounding boxes and detection
classes displayed.

camera_frame (String, default \"ssd_detector_frame\")

. Frame ID to use in published Detection2DArray. Note the source_img
header and data (except for the actual camera data) are copied from the
subscribed source image.

start_zoom_enabled (Bool, default False)

. Enables a sliding window for the detector. Requires more time to
complete each detection. Allows for longer distance detection. For an
[example](https://www.pyimagesearch.com/wp-content/uploads/2014/10/sliding_window_example.gif)
of a sliding window detector.

mask_overlap (Int32, default 0)

. Ranges from 0 to 100. Controls whether to use a mask to restrict
detections. If mask_overlap is set greater than 0, then object
detections are restricted to boxes that overlap at least the
mask_overlap percentage with mask==255 pixels. Conversely, if
mask_overlap is set to 0, then the mask is ignored. Can be set in real
time and overridden by the mask_overlap topic above.

\_\_MxNet Settings\_\_

threshold (Float, default 0.5)

. Detection probability threshold. If set high, only high-confidence
detections will be reported. Note, probability does not linearly
correspond to actual likelihood that something is what it is, but it is
a useful guide as a start. Lower thresholds will result in less missed
detections but more false positives.

batch_size (Int32, default 1)

. The number of images to pass to the GPU (if enabled) at once. This
increases GPU memory used but, if any sliding window cropping is used,
speeds up the detection. There is a limit on GPU memory, and if this is
reached the node will crash. There is not a simple method to determine
this ahead of time, and this is instead to be determined using a short
period of trial and error to find the limit. In order to maximize
efficiency, you should either set this to level0_ncrops (if no zoom) or
some larger divisible portion of the total number of crops that will be
used (if zooming). It does not need to be an even divisor of the total
number of crops, the code will maximize usage of available batch size
and number of crops.

model_directory (String, default \"/mxnet/ssd\")

. Location of the MxNet model parameters and symbol on disk.

model_filename (String, default \"ssd_512_resnet50_v1_voc.params\")

. Name of the MxNet model to load and run. This is ignored if using a
stock network (see network below). This is intended to be used if you
have custom network weights installed in the model_directory location.

network (String, default \"ssd_512_resnet50_v1_voc\")

. Name of the network symbol to load. Choices include
\"ssd_512_resnet50_v1_voc\", \"ssd_512_resnet50_v1_coco\",
\"ssd_512_resnet50_v1_custom\" and similar with mobilenet1.0, vgg16. See
[GluonCV\'s Detection Model Zoo](https://gluon-cv.mxnet.io/model_zoo/detection.html)
for a more complete list.

enable_gpu (Bool, default false)

. Use the GPU or CPU for inference.

classes (String, default \"aeroplane, bicycle, bird, boat, bottle,
bus,car, cat, chair, cow, diningtable, dog, horse, motorbike,person,
pottedplant, sheep, sofa, train, tvmonitor\") . The names of classes
used to train the model (the VOC-trained models used 20 classes),
separated by commas.

\_\_Crop Pattern\_\_

level0_ncrops (Int32, default 1)

. Specify the sliding window detection pattern in the larger image
dimension (typically this is the x-dimension, or width). The square crop
will be sized to the smaller image dimension (typically the y-dimension,
or height). Assuming width is the larger dimension, how many crops in
the left-right direction of the image should we pass to the detector?
The detector code will work out the overlap and report it on the node
launch standard output and ROS logfile. In general, the number of x
crops should be set to close to 20-30% more than the image width divided
by the detector input size (512). For example, with image width 1280,
use level1_xcrop=3 and the detector will see 22% overlap on the inner
crops with each of the outer crops. If set to 0, this will take the
minimum of x-dimension and y-dimension and center crop to that
resolution, unless resize_square is set to True. If set to 1, then this
will center crop to the minimum image dimension. If set to 0, then the
image will be resized to square first and the whole image will be used.
For example, if you set this to 0 and your image size is 1920x1280, then
the detector will resize the image to square before passing it in,
otherwise if set to 1, it will center crop to 1280 by 1280 pixels and
pass the 1280x1280 image to the detector.

level1_xcrops (Int32, default 0)

. Specify the second-level sliding window detection pattern in the
x-dimension on the second layer. Use this to create a second layer set
of sliding window zooms in to the image. Please note, this should be
greater than 1 to be useful otherwise it will only create a crop in the
upper left corner of the image. The crops will be distributed across the
image and the overlap percentage will be reported so watch the overlap
percentage and try to get it above 0% but below 50% to maximize
detectability of small objects.

\<TODO: images of crop patterns\>

level1_ycrops (Int32, default 0)

. Specify the sliding window pattern in the y-dimension. This must be
greater than 1 to have any effect, or turn it off by leaving as 0.

level1_crop_pixels (Int32, default 300)

. The size of pixels to be used in the second-level crop. In general,
this should be set to produce images of size 300x300 or so to be passed
to the detector, which will upsample them to 512 by 512 before running
detection. As discussed in the node description, this will nevertheless
improve distance detection if the image quality is good.

\_\_Save Parameters\_\_

save_detections (Bool, default False)

. Save detected images in jpeg form, with incrementing number.

save_directory (String, default \"/tmp\")

. Directory to save detection images.

#### Example Launch File

```
sudo apt install python-scipy python3-scipy python-matplotlib python3-matplotlib
sudo pip install tqdm
```1

### mxnet_segmentation_node

Semantic segmentation using pretrained segmentation networks from
GluonCV, see
[segmentation model zoo](https://gluon-cv.mxnet.io/model_zoo/segmentation.html)
for a list of relevant pre-trained segmentation networks.

#### Published Topics

/segmentation_mask sensor_msgs::Image, latched output

. Published segmentation mask (0 or 255, corresponding to mask_values
rosparam). Note, this output is latched, so the timestamp seen by
subscribers will gradually get older if no new detection requested.

/segmentation_overlay sensor_msgs::Image

. Published segmentation, masked corresponding to mask_values rosparam,
and overlain on input image in red at 50% alpha blend.

#### Subscribed Topics

/usb_cam/image_raw sensor_msgs::Image

. Input image to run segmentation on.

/rr_mxnet_segmentation/run_once std_msgs::Bool

. Enable the detector and run segmentation once (or number of frames
specified in rosparam avg_segmentation_frames). Segmentation may already
be running continuously (if appropriate rosparam or topic run_continuous
is set) or alternatively if run_continuous is False, it can be run once
on run_once=True and some number of frames (or single frame) averaged
before publishing the output mask. Test with:

```
sudo apt install python-scipy python3-scipy python-matplotlib python3-matplotlib
sudo pip install tqdm
```2

/rr_mxnet_segmentation/run_continuous std_msgs::Bool

. Segmentation runs continuously if rosparam run_continuous is True or
receive True on this topic.

#### Parameters

image_topic (String, default \"/usb_cam/image_raw\")

. Input image topic to perform detections on.

mask_topic (String, default \"segmentation_mask\", \_\_latched=True\_\_)

. Output image topic to publish segmentation result.

overlay_topic (String, default \"segmentation_overlay\")

. Output image topic to publish segmentation result overlain in red on
input image.

run_continuous (Bool, default False)

. Segmentation runs as fast as possible within limits set by throttle
timer if this is set True.

mask_values (String, default \"9, 12\")

. Pixel values to use to generate a \"True\" mask. These values in the
semantic segmentation output are used to set the output mask==255. All
other segmentation pixel values get mask==0. Alternatively, if set to
negative values (e.g. \"-9, -12\"), the opposite masking is used, so all
segmentation pixel values that are either 9 or 12 get set to 0, and all
other pixels get set to 255. For values of pixel masks, refer to the
[ADE20K](https://github.com/Vladkryvoruchko/PSPNet-Keras-tensorflow/blob/master/ade20k_labels.py)
or [COCO](https://github.com/nightrome/cocostuff/blob/master/labels.md)
mask values. For example with ADE20K, person=12, sky=2, grass=9, road=6,
etc.

network (String, default \"deeplab_resnet50_ade\")

. Name of the network symbol to load. Choices include
\"vgg_resnet50_ade\", \"psp_resnet50_ade\", \"deeplab_resnet50_ade\" and
others. See
[GluonCV\'s Segmentation Model Zoo](https://gluon-cv.mxnet.io/model_zoo/segmentation.html)
for a more complete list.

enable_gpu (Bool, default false)

. Use the GPU or CPU for inference.

throttle_timer (Int32, default 5)

. Seconds to wait between segmentation runs. If timer is set to less
than the possible inference rate, the node will run inference as fast as
possible and probably take up most of the computer\'s resources (CPU or
GPU).

latency_threshold (Int32, default 2)

. Seconds to allow the images to get stale before discarding and waiting
for next new image. In the worst case, if there is substantial time
delay between the image publisher and reception of images by this node,
this may need to be increased just to allow the node to function. In
typical low latency systems, this can be decreased.

#### Example Launch File

```
sudo apt install python-scipy python3-scipy python-matplotlib python3-matplotlib
sudo pip install tqdm
```3

### mxnet_depseg_hydra_node

Combined monocular depth and semantic segmentation trained on CityScapes
and KITTI datasets.

#### Published Topics

/segmentation_mask sensor_msgs::Image, latched output

. Published segmentation mask (0 or 255, corresponding to mask_values
rosparam). Note, this output is latched, so the timestamp seen by
subscribers will gradually get older if no new detection requested.

/segmentation_overlay sensor_msgs::Image

. Published segmentation, masked corresponding to mask_values rosparam,
and overlain on input image in red at 50% alpha blend.

#### Subscribed Topics

/usb_cam/image_raw sensor_msgs::Image

. Input image to run segmentation on.

/rr_mxnet_segmentation/run_once std_msgs::Bool

. Enable the detector and run segmentation once (or number of frames
specified in rosparam avg_segmentation_frames). Segmentation may already
be running continuously (if appropriate rosparam or topic run_continuous
is set) or alternatively if run_continuous is False, it can be run once
on run_once=True and some number of frames (or single frame) averaged
before publishing the output mask. Test with:

```
sudo apt install python-scipy python3-scipy python-matplotlib python3-matplotlib
sudo pip install tqdm
```4

/rr_mxnet_segmentation/run_continuous std_msgs::Bool

. Segmentation runs continuously if rosparam run_continuous is True or
receive True on this topic.

#### Parameters

image_topic (String, default \"/usb_cam/image_raw\")

. Input image topic to perform detections on.

mask_topic (String, default \"segmentation_mask\", \_\_latched=True\_\_)

. Output image topic to publish segmentation result.

overlay_topic (String, default \"segmentation_overlay\")

. Output image topic to publish segmentation result overlain in red on
input image.

run_continuous (Bool, default False)

. Segmentation runs as fast as possible within limits set by throttle
timer if this is set True.

mask_values (String, default \"9, 12\")

. Pixel values to use to generate a \"True\" mask. These values in the
semantic segmentation output are used to set the output mask==255. All
other segmentation pixel values get mask==0. Alternatively, if set to
negative values (e.g. \"-9, -12\"), the opposite masking is used, so all
segmentation pixel values that are either 9 or 12 get set to 0, and all
other pixels get set to 255. For values of pixel masks, refer to the
[ADE20K](https://github.com/Vladkryvoruchko/PSPNet-Keras-tensorflow/blob/master/ade20k_labels.py)
or [COCO](https://github.com/nightrome/cocostuff/blob/master/labels.md)
mask values. For example with ADE20K, person=12, sky=2, grass=9, road=6,
etc.

network (String, default \"deeplab_resnet50_ade\")

. Name of the network symbol to load. Choices include
\"vgg_resnet50_ade\", \"psp_resnet50_ade\", \"deeplab_resnet50_ade\" and
others. See
[GluonCV\'s Segmentation Model Zoo](https://gluon-cv.mxnet.io/model_zoo/segmentation.html)
for a more complete list.

enable_gpu (Bool, default false)

. Use the GPU or CPU for inference.

throttle_timer (Int32, default 5)

. Seconds to wait between segmentation runs. If timer is set to less
than the possible inference rate, the node will run inference as fast as
possible and probably take up most of the computer\'s resources (CPU or
GPU).

latency_threshold (Int32, default 2)

. Seconds to allow the images to get stale before discarding and waiting
for next new image. In the worst case, if there is substantial time
delay between the image publisher and reception of images by this node,
this may need to be increased just to allow the node to function. In
typical low latency systems, this can be decreased.

#### Example Launch File

```
sudo apt install python-scipy python3-scipy python-matplotlib python3-matplotlib
sudo pip install tqdm
```5

## Release Notes

This package is currently in pre-release meaning the code has been
tested and is functional, but backwards compatibility is not guaranteed
until v1.0.0, so make note of which version you are using and read the
changelog carefully before updating.
