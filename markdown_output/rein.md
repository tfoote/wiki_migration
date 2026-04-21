**DEPRECATED: This package is considered deprecated by its authors. See
the ecto package at ecto.willowgarage.com for the current approach.**

## Overview

The rein (REcognition INfrastructure) package contains a framework that
is supposed to make the addition of new vision algorithms that work on
the PR2 much simpler. The recognition infrastructure contains the
following main components:

-   *Attention Operator* - takes an image and (optionally) a point cloud
    as input and generates masks and/or regions of interest (ROI) in the
    image
-   *Detector* - takes an image and optionally a point cloud and a list
    of ROIs or masks and generates detections. A detection is a ROS
    message that contains the name of the detected object (label), the
    name of the detector that found the object, a confidence score, a
    mask/ROI in the image and an optional pose of the object.
-   *Pose estimator/Model fitter* - takes as input a point cloud and/or
    image, a list of detection and (optionally) a list of approximate
    poses and computes/refines the 6D poses of each detected object

[Youtube](https://www.youtube.com/watch?v=tlC2O9T9jks)

## Framework design

The framework is split in two main components, a ROS-independent one
containing the vision algorithms doing the actual work and one that
contains ROS wrappers around those algorithms and exposes them as
[nodelets](nodelet). Using nodelets allows the algorithms to be
dynamically (un)loadable and offers optimizations for zero-copy cost of
Boost shared_ptr messages between different nodelets that are part of
the same process.

### Algorithms API

This part of the package contains the ROS-independent algorithms. The
framework has base classes for attention operators, detectors and pose
estimators that are wrapped by the ROS nodelets. Each new algorithm that
is added to the pipeline will have to inherit from one of these classes.

#### AttentionOperator

The \`rein::AttentionOperator\` represents the base class for attention
operators. An attention operator takes as input an image and/or point
cloud to compute interesting regions in the image. The output of an
attention operator is a list of regions of interest (ROI) and masks. The
\`rein::AttentionOperator\` has the following pure virtual methods which
have to be implemented by a subclass.

```cplusplus
virtual void run() = 0; // runs the attention operator
virtual std::string getName() = 0; // returns the (unique) name of the attention operator
```

An attention operator also has the following getter/setter methods.
```cplusplus
void setImage(const cv::Mat& image);  // input image
void setPointCloud(const sensor_msgs::PointCloud2ConstPtr point_cloud); // input point cloud
MaskArray getMasks() const; // output masks
```

The ROS nodelet will automatically call these getter/setter methods to
set the input image/point cloud and to get the resulting masks after the
attention operator has run.

#### Detector

The \`rein::Detector\` represents the base class for detectors. A
detector takes as input an image and/or point cloud and/or some regions
of interest and detects the objects present in the image/point cloud.
The output of a detector is a list of detections
(\<\<MsgLink(rein/Detection)\>\>).The \`rein::Detector\` has the
following pure virtual methods which have to be implemented by a
subclass.

```cplusplus
virtual void detect() = 0; // runs the detector
virtual std::string getName() = 0; // returns the (unique) name of the detector
virtual void loadModels(const std::vector<std::string>& models) = 0; // loads the list of pre-trained models that will be detected in the input image
```

A detector also has the following getter/setter methods. These are
automatically called by the ROS wrapper.

```cplusplus
void setImage(const cv::Mat& image);  // input image
void setMasks(const MaskArrayConstPtr& masks); // masks (rois)
void setPointCloud(const sensor_msgs::PointCloud2ConstPtr point_cloud); // input point cloud
DetectionArray getDetections() const; // output detections
```

#### PoseEstimator

The \`rein::PoseEstimator\` represents the base class for pose estimator
algorithms. A pose estimator takes as input an image and/or point cloud
and/or a list of detections and computes/refines the poses of the
objects in the image/point cloud. The output of a pose estimator is a
list of poses. The \`rein::PoseEstimator\` has the following pure
virtual methods which have to be implemented by a subclass.

```cplusplus
virtual void run() = 0; // runs the attention operator
virtual std::string getName() = 0; // returns the (unique) name of the pose estimator
```

A pose estimator also has the following getter/setter methods. These are
automatically called by the ROS wrapper.

```cplusplus
void setImage(const cv::Mat& image);  // input image
void setDetections(const DetectionArrayConstPtr& detections) // input detections
void setPointCloud(const sensor_msgs::PointCloud2ConstPtr point_cloud); // input point cloud
geometry_msgs::PoseArray getPoses() const; // output poses
```

#### Trainable

The \`rein::Trainable\` is an interface that must be implemented by all
the algorithms (usually detectors) that support online training. The
interface contains the following pure virtual methods:

```cplusplus
void startTraining(const std::string& name) = 0; // called when training of a new object model starts
void trainInstance(const std::string& name, const TrainingData& data) = 0; // called for each training instance
void endTraining(const std::string& name) = 0; // called when training is finished, usually to save the model
```

#### ModelStorage

The \`rein::ModelStorage\` is an interface that different algorithms can
use to persist models. It may have several implementations, one of them
being \`rein::ModelDatabase\`, that uses a database (postgresql and
sqlite3 are currently supported) for persistence. The interface has the
following methods:

```cplusplus
virtual void saveModel(const std::string& name, const std::string& detector, const std::string& model_blob) = 0;
virtual bool loadModel(const std::string& name, const std::string& detector, std::string& model_blob) = 0;
virtual bool getModelList(const std::string& detector, std::vector<std::string>& model_list) = 0;
```

### ROS Nodelets

The ROS nodelets wrap the ROS-independent algorithms and take care of
subscribing to topics, synchronizing the messages on the input topics,
publishing the results and setting the algorithm parameters using the
[dynamic reconfigure](dynamic_reconfigure) framework. Each algorithm
will have a nodelet wrapper. Several base nodelet classes are provided
for each type of algorithm presented above, which simplifies the process
of writing new nodelets.

#### AttentionOperatorNodelet

**Subscribed Topics**

```clearsilver
sub {
no_header=True
  0.name= ~/image
  0.type= sensor_msgs/Image
  0.desc= The input image
  1.name= ~/point_cloud
  1.type= sensor_msgs/PointCloud2
  1.desc= The input point cloud
}
```

**Published Topics**

```clearsilver
pub {
no_header=True
  0.name= ~/masks
  0.type= rein/MaskArray
  0.desc= Masks for each region of interest on the input image.
  1.name= ~/rois
  1.type= rein/RectArray
  1.desc= Regions of interest on the input image
}
```

**Parameters**

```cplusplus
void setImage(const cv::Mat& image);  // input image
void setPointCloud(const sensor_msgs::PointCloud2ConstPtr point_cloud); // input point cloud
MaskArray getMasks() const; // output masks
```0

#### DetectorNodelet

**Subscribed Topics**

```cplusplus
void setImage(const cv::Mat& image);  // input image
void setPointCloud(const sensor_msgs::PointCloud2ConstPtr point_cloud); // input point cloud
MaskArray getMasks() const; // output masks
```1

**Published Topics**

```cplusplus
void setImage(const cv::Mat& image);  // input image
void setPointCloud(const sensor_msgs::PointCloud2ConstPtr point_cloud); // input point cloud
MaskArray getMasks() const; // output masks
```2

**Parameters**

```cplusplus
void setImage(const cv::Mat& image);  // input image
void setPointCloud(const sensor_msgs::PointCloud2ConstPtr point_cloud); // input point cloud
MaskArray getMasks() const; // output masks
```3

#### PoseEstimatorNodelet

**Subscribed Topics**

```cplusplus
void setImage(const cv::Mat& image);  // input image
void setPointCloud(const sensor_msgs::PointCloud2ConstPtr point_cloud); // input point cloud
MaskArray getMasks() const; // output masks
```4

**Published Topics**

```cplusplus
void setImage(const cv::Mat& image);  // input image
void setPointCloud(const sensor_msgs::PointCloud2ConstPtr point_cloud); // input point cloud
MaskArray getMasks() const; // output masks
```5

**Parameters**

```cplusplus
void setImage(const cv::Mat& image);  // input image
void setPointCloud(const sensor_msgs::PointCloud2ConstPtr point_cloud); // input point cloud
MaskArray getMasks() const; // output masks
```6

#### TrainerServer

The \`rein::TrainerServer\` class is a \'server\' class that when
instantiated by a node/nodelet advertises three services which can be
used to train a new detector. The detector to be trained must implement
the \`rein::Trainable\` interface and is passed as a parameter to the
constructor of \`TrainerServer\`.

```cplusplus
void setImage(const cv::Mat& image);  // input image
void setPointCloud(const sensor_msgs::PointCloud2ConstPtr point_cloud); // input point cloud
MaskArray getMasks() const; // output masks
```7

**Services advertised**

```cplusplus
void setImage(const cv::Mat& image);  // input image
void setPointCloud(const sensor_msgs::PointCloud2ConstPtr point_cloud); // input point cloud
MaskArray getMasks() const; // output masks
```8
