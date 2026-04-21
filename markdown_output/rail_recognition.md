## About

The `rail_recognition` package contains nodes for object recognition
and demonstration grasp selection using models from a grasp database,
handled by [graspdb](graspdb). The package also contains a node used for
generating object models from grasp demonstrations collected with the
[rail_grasp_collection](rail_grasp_collection) package. The recognizer
has support for a 2D image recognizer to run first in the full
recognition pipeline, significantly increasing the runtime of the point
cloud recognizer by limiting the number of candidate classes to test
with point cloud registration. This package also contains nodes for data
collection, training, and testing of the 2D recognizer.

## Nodes



```clearsilver
node.0 {
  name = model_generator
  desc = Generate object models for recognition and manipulation using demonstrations from the grasp database.
  goal {
    0.name = model_generator/generate_models
    0.type = rail_pick_and_place_msgs/GenerateModelsGoal
    0.desc = Generate models from a set of grasp demonstrations or object models (specified by id in the grasp database), and store the result as new models in the database.
  }
  result {
    0.name = model_generator/generate_models
    0.type = rail_pick_and_place_msgs/GenerateModelsResult
    0.desc = Model generation result.
  }
  pub {
    0.name = model_generator/debug_pc
    0.type = sensor_msgs/PointCloud2
    0.desc = Point cloud resulting from registration, only published if the debug parameter is set to true.
    1.name = model_generator/debug_poses
    1.type = geometry_msgs/PoseArray
    1.desc = Grasp poses resulting from registration, only published if the debug parameter is set to true.
  }
  param {
    0.name = /graspdb/host
    0.type = string
    0.desc = Grasp database host ip.
    0.default = "127.0.0.1"
    1.name = /graspdb/port
    1.type = int
    1.desc = Grasp database port.
    1.default = graspdb::Client::DEFAULT_PORT
    2.name = /graspdb/user
    2.type = string
    2.desc = Grasp database username.
    2.default = "ros"
    3.name = /graspdb/password
    3.type = string
    3.desc = Grasp database password.
    3.default = ""
    4.name = /graspdb/db
    4.type = string
    4.desc = Grasp database name.
    4.default = "graspdb"
    5.name = debug
    5.type = bool
    5.desc = Debug flag, set to true to publish debugging information.
    5.default = false
  }
}
node.1 {
  name = object_recognizer
  desc = Object recognition of passed-in segmented objects, returns the recognized object with name, database id, and grasps filled in.
  goal {
    0.name = rail_recognition/recognize_object/goal
    0.type = rail_manipulation_msgs/RecognizeObjectGoal
    0.desc = Recognize a segmented object passed in as the goal.
  }
  result {
    0.name = rail_recognition/recognize_object/result
    0.type = rail_manipulation_msgs/RecognizeObjectResult
    0.desc = The segmented object with recognized information (name, database id, and example grasps ordered by success rate) filled in, or simply the segmented object if recognition failed.
  }
  param {
    0.name = /graspdb/host
    0.type = string
    0.desc = Grasp database host ip.
    0.default = "127.0.0.1"
    1.name = /graspdb/port
    1.type = int
    1.desc = Grasp database port.
    1.default = graspdb::Client::DEFAULT_PORT
    2.name = /graspdb/user
    2.type = string
    2.desc = Grasp database username.
    2.default = "ros"
    3.name = /graspdb/password
    3.type = string
    3.desc = Grasp database password.
    3.default = ""
    4.name = /graspdb/db
    4.type = string
    4.desc = Grasp database name.
    4.default = "graspdb"
  }
}
node.2 {
  name = object_recognition_listener
  desc = Object recognition of segmented objects, specified by object index in the segmented object list.
  sub {
    0.name = object_topic param
    0.type = rail_manipulation_msgs/SegmentedObjectList
    0.desc = Incoming segmented object data.
  }
  pub {
    0.name = object_recognition_listener/recognized_objects
    0.type = rail_manipulation_msgs/SegmentedObjectList
    0.desc = Outgoing segmented and recognized object data.
    1.name = object_recognition_listener/debug
    1.type = geometry_msgs/PoseArray
    1.desc = Poses for most recently recognized object, only published if the debug flag is set.
  }
  goal {
    0.name = rail_recognition/recognize
    0.type = rail_manipulation_msgs/RecognizeGoal
    0.desc = Recognize a segmented object passed in by index.
    1.name = rail_recognition/recognize_all
    1.type = rail_manipulation_msgs/RecognizeAllGoal
    1.desc = Recognize all segmented objects.
  }
  result {
    0.name = rail_recognition/recognize
    0.type = rail_manipulation_msgs/RecognizeResult
    0.desc = Object recognition success.
    1.name = rail_recognition/recognize_all
    1.type = rail_manipulation_msgs/RecognizeAllResult
    1.desc = Object recognition successes.
  }
  param {
    0.name = /graspdb/host
    0.type = string
    0.desc = Grasp database host ip.
    0.default = "127.0.0.1"
    1.name = /graspdb/port
    1.type = int
    1.desc = Grasp database port.
    1.default = graspdb::Client::DEFAULT_PORT
    2.name = /graspdb/user
    2.type = string
    2.desc = Grasp database username.
    2.default = "ros"
    3.name = /graspdb/password
    3.type = string
    3.desc = Grasp database password.
    3.default = ""
    4.name = /graspdb/db
    4.type = string
    4.desc = Grasp database name.
    4.default = "graspdb"
    5.name = object_topic
    5.type = string
    5.desc = Incoming segmented objects topic.
    5.default = "/rail_segmentation/segmented_objects"
    6.name = debug
    6.type = bool
    6.desc = Debug flag, publishes grasp poses on recognized objects when true.
    6.default = false
    7.name = use_image_recognition
    7.type = bool
    7.desc = Enable/disable narrowing grasp models by first using the 2D image recognizer before performing point cloud recognition.
    7.default = true
  }
}
node.3 {
  name = rail_grasp_model_retriever
  desc = Grasp model retrieval from the grasp database via action server.
  goal {
    0.name = rail_grasp_model_retriever/retrieve_grasp_model/goal
    0.type = rail_pick_and_place_msgs/RetrieveGraspModelGoal
    0.desc = Grasp model to be retrieved from the database.
  }
  result {
    0.name = rail_grasp_model_retriever/retrieve_grasp_model/result
    0.type = rail_pick_and_place_msgs/RetrieveGraspModelResult
    0.desc = The grasp model retrieved from the database.  The point cloud and grasp poses will also be published on their respective topics when the result is sent.
  }
  pub {
    0.name = rail_grasp_model_retriever/point_cloud
    0.type = sensor_msgs/PoitnCloud2
    0.desc = Retrieved point cloud.
    1.name = rail_grasp_model_retriever/poses
    1.type = geometry_msgs/PoseArray
    1.desc = Retrieved grasp poses.
  }
  param {
    0.name = /graspdb/host
    0.type = string
    0.desc = Grasp database host ip.
    0.default = "127.0.0.1"
    1.name = /graspdb/port
    1.type = int
    1.desc = Grasp database port.
    1.default = graspdb::Client::DEFAULT_PORT
    2.name = /graspdb/user
    2.type = string
    2.desc = Grasp database username.
    2.default = "ros"
    3.name = /graspdb/password
    3.type = string
    3.desc = Grasp database password.
    3.default = ""
    4.name = /graspdb/db
    4.type = string
    4.desc = Grasp database name.
    4.default = "graspdb"
  }
}
node.4 {
  name = metric_trainer
  desc = Generate data sets for training registration metric decision trees used in classifying pairwise point cloud registrations for the object model generation and recognition pipelines.
  pub {
    0.name = metric_trainer/base_pc
    0.type = pcl/PointCloud<pcl/PointXYZRGB>
    0.desc = Base point cloud used for pairwise registration.
    1.name = metric_trainer/aligned_pc
    1.type = pcl/PointCloud<pcl/PointXYZRGB>
    1.desc = Point cloud aligned to the base point cloud.
  }
  goal {
    0.name = metric_trainer/train_metrics/goal
    0.type = rail_pick_and_place_msgs/TrainMetricsGoal
    0.desc = Initiate metric training for all pairs of point clouds of a given type; requires user input for labeling whether each pairwise merge is a successful or not.
  }
  result {
    0.name = metric_trainer/train_metrics/result
    0.type = rail_pick_and_place_msgs/TrainMetricsResult
    0.desc = Training result, true on success.  The training data itself is saved to an output file in the .ros directory.
  }
  act_called {
    0.name = metric_trainer/get_yes_no_feedback
    0.type = rail_pick_and_place_msgs/GetYesNoFeedback
    0.desc = Action for collecting feedback for the success of a pairwise merge.
  }
  param {
    0.name = /graspdb/host
    0.type = string
    0.desc = Grasp database host ip.
    0.default = "127.0.0.1"
    1.name = /graspdb/port
    1.type = int
    1.desc = Grasp database port.
    1.default = graspdb::Client::DEFAULT_PORT
    2.name = /graspdb/user
    2.type = string
    2.desc = Grasp database username.
    2.default = "ros"
    3.name = /graspdb/password
    3.type = string
    3.desc = Grasp database password.
    3.default = ""
    4.name = /graspdb/db
    4.type = string
    4.desc = Grasp database name.
    4.default = "graspdb"
  }
}
node.5 {
  name = collect_images
  desc = Run an instance of the 2D image recognizer to save 2D images as training/test data at every segmentation call.
  sub {
    0.name = rail_segmentation/segmented_objects
    0.type = rail_manipulation_msgs/SegmentedObjectList
    0.desc = Segmented objects topic from which to save images.
  }
  param {
    0.name = collect_images/saved_data_dir
    0.type = string
    0.desc = Directory containing trained image recognizer data (not used by this node).
    0.default = ros::package::getPath("rail_recognition")/data/saveddata
    1.name = collect_images/images_dir
    1.type = string
    1.desc = Directory containing training images (not used by this node).
    1.default = ros::package::getPath("rail_recognition")/data/images
    2.name = collect_images/test_images_dir
    2.type = string
    2.desc = Directory containing test images (not used by this node).
    2.default = ros::package::getPath("rail_recognition")/data/testimages
    3.name = collect_images/new_images_dir
    3.type = string
    3.desc = Location at which to save new images.
    3.default = ros::package::getPath("rail_recognition")/data/newimages
    4.name = collect_images/save_new_images
    4.type = bool
    4.desc = Flag for saving new images; if true each segmented object from the collect_images/segmented_objects_topic will be saved as a 2D image in the collect_images/newimages directory.
    4.default = false
    5.name = collect_images/segmented_objects_topic
    5.type = string
    5.desc = Topic for incoming segmented objects, used only if collect_images/save_new_images is true.
    5.default = /rail_segmentation/segmented_objects
  }
}
node.6 {
  name = save_image_recognizer_features
  desc = Run an instance of the 2D image recognizer to build the dictionaries for the recognizer, then exit.
  sub {
    0.name = rail_segmentation/segmented_objects
    0.type = rail_manipulation_msgs/SegmentedObjectList
    0.desc = Segmented objects topic from which to save images.
  }
  param {
    0.name = save_image_recognizer_features/saved_data_dir
    0.type = string
    0.desc = Directory at which to save the dictionaries.
    0.default = ros::package::getPath("rail_recognition")/data/saveddata
    1.name = save_image_recognizer_features/images_dir
    1.type = string
    1.desc = Directory containing training images, organized by object class.
    1.default = ros::package::getPath("rail_recognition")/data/images
    2.name = save_image_recognizer_features/test_images_dir
    2.type = string
    2.desc = Directory containing test images, organized by object class (not used by this node).
    2.default = ros::package::getPath("rail_recognition")/data/testimages
    3.name = save_image_recognizer_features/new_images_dir
    3.type = string
    3.desc = Location at which to save new images (not used by this node).
    3.default = ros::package::getPath("rail_recognition")/data/newimages
    4.name = save_image_recognizer_features/save_new_images
    4.type = bool
    4.desc = Flag for saving new images (not used by this node).
    4.default = false
    5.name = save_image_recognizer_features/segmented_objects_topic
    5.type = string
    5.desc = Topic for incoming segmented objects (not used by this node).
    5.default = /rail_segmentation/segmented_objects
  }
}
node.7 {
  name = train_image_recognizer
  desc = Run an instance of the 2D image recognizer to train the neural net on the training dataset, then exit.
  sub {
    0.name = rail_segmentation/segmented_objects
    0.type = rail_manipulation_msgs/SegmentedObjectList
    0.desc = Segmented objects topic from which to save images.
  }
  param {
    0.name = train_image_recognizer/saved_data_dir
    0.type = string
    0.desc = Directory at which to save the dictionaries.
    0.default = ros::package::getPath("rail_recognition")/data/saveddata
    1.name = train_image_recognizer/images_dir
    1.type = string
    1.desc = Location of the training dataset, organized by object class.
    1.default = ros::package::getPath("rail_recognition")/data/images
    2.name = train_image_recognizer/test_images_dir
    2.type = string
    2.desc = Directory containing test images, organized by object class (not used by this node).
    2.default = ros::package::getPath("rail_recognition")/data/testimages
    3.name = train_image_recognizer/new_images_dir
    3.type = string
    3.desc = Location at which to save new images (not used by this node).
    3.default = ros::package::getPath("rail_recognition")/data/newimages
    4.name = train_image_recognizer/save_new_images
    4.type = bool
    4.desc = Flag for saving new images (not used by this node).
    4.default = false
    5.name = train_image_recognizer/segmented_objects_topic
    5.type = string
    5.desc = Topic for incoming segmented objects (not used by this node).
    5.default = /rail_segmentation/segmented_objects
  }
}
node.8 {
  name = test_image_recognizer
  desc = Run an instance of the 2D image recognizer to test the trained neural net on the test dataset, then exit.  Results of the test are printed to the terminal.
  sub {
    0.name = rail_segmentation/segmented_objects
    0.type = rail_manipulation_msgs/SegmentedObjectList
    0.desc = Segmented objects topic from which to save images.
  }
  param {
    0.name = test_image_recognizer/saved_data_dir
    0.type = string
    0.desc = Directory at which to save the dictionaries.
    0.default = ros::package::getPath("rail_recognition")/data/saveddata
    1.name = test_image_recognizer/images_dir
    1.type = string
    1.desc = Directory containing training images, organized by object class (not used by this node).
    1.default = ros::package::getPath("rail_recognition")/data/images
    2.name = test_image_recognizer/test_images_dir
    2.type = string
    2.desc = Location of the test dataset, organized by object class.
    2.default = ros::package::getPath("rail_recognition")/data/testimages
    3.name = test_image_recognizer/new_images_dir
    3.type = string
    3.desc = Location at which to save new images (not used by this node).
    3.default = ros::package::getPath("rail_recognition")/data/newimages
    4.name = test_image_recognizer/save_new_images
    4.type = bool
    4.desc = Flag for saving new images (not used by this node).
    4.default = false
    5.name = test_image_recognizer/segmented_objects_topic
    5.type = string
    5.desc = Topic for incoming segmented objects (not used by this node).
    5.default = /rail_segmentation/segmented_objects
  }
}
```



## The Recognition Pipeline

![\|width="500"](attachment:recognition_pipeline.png)

The full recognition pipeline takes in a list of unrecognized segmented
objects, such as what the [rail_segmentation](rail_segmentation) package
provides. Each unrecognized object will first be classified by the 2D
image classifier to determine a set of candidate object classes of high
probability. These candidate classes will then be retrieved from the
object model database, handled by [graspdb](graspdb), which are then
used by the point cloud recognizer to provide a final object label and
set of example grasps for picking up the now-recognized object.

Note that the initial 2D image recognition is an optional step. It can
be disabled by setting the use_object_recognition parameter of the
object_recognition_listener node to false. Disabling this step will
significantly lower the runtime of the algorithm, however, as every
model in the database will be considered by the point cloud recognizer.

### Setting up the 2D Image Recognizer

The 2D image recognizer can be trained in a few steps. First, an image
set representative of the objects in the environment must be collected.
This can be accomplished by running a segmentation node, such as the one
found in [rail_segmentation](rail_segmentation), and the collect_images
node as follows:

. 

```
roslaunch rail_recognition collect_images.launch
```



The images will be saved in the directory specified to the
collect_images node. These must then be sorted by hand into a training
dataset organized by each object class. See the data directory for an
example. The collected images, or a subset of them, can also be sorted
into the test dataset.

The recognizer uses a bag-of-words model with a neural network
classifier. The next step is to train the dictionary for the
bag-of-words, which can be done by running the node below. Note that if
the recognizer is being retrained for added objects or data, the same
dictionaries can be re-used if the dataset hasn't changed dramatically,
and this step can be skipped.

. 

```
rosrun rail_recognition save_image_recognizer_features
```



Next, the neural net itself needs to be trained:

. 

```
rosrun rail_recognition train_image_recognizer
```



The 2D image recognizer is now trained and ready to use. For
verification of its accuracy, the test dataset can be used for
evaluation:

. 

```
rosrun rail_recognition test_image_recognizer
```



### Setting up the Point Cloud Recognizer

See the tutorials section of [rail_pick_and_place](rail_pick_and_place)
for details on how to set up an object model database, provide grasp
demonstrations, train new object models, and refine existing object
models.

## Installation

To install the `rail_pick_and_place` package, you can install from
source with the following commands:

. 

```shell
cd /(your catkin workspace)/src
git clone https://github.com/WPI-RAIL/rail_pick_and_place.git
cd ..
catkin_make
catkin_make install
```



## Startup

The `rail_recognition` package contains a launch file for launching
the object_recognition_listener node with the various database,
segmentation, and recognition parameters set, executed with:

. 

```
roslaunch rail_recognition object_recognition_listener.launch
```



Other major nodes in the package contain similar launch files with
parameters set, listed below, where each launch file corresponds to a
node of the same name.

. 

```
roslaunch rail_recognition collect_images.launch
```

 . 

```
roslaunch rail_recognition metric_trainer.launch
```

 .


```
roslaunch rail_recognition model_generator.launch
```

 . 

```
roslaunch rail_recognition collect_images.launch
```

0 .


```
roslaunch rail_recognition collect_images.launch
```

1

The set of nodes used for training the 2D image recognizer can be run as
follows:

. 

```
roslaunch rail_recognition collect_images.launch
```

2

Model generation can be run with an rviz plugin for visualization found
in [rail_pick_and_place_tools](rail_pick_and_place_tools).
