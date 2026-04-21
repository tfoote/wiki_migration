  -- ------------------------------------------------------------------------------------------------------------------------------------------------ --
     <#ffff00>These tutorials require packages that are not open to the public. If you want to run the packages, please write to jsf@ipa.fhg.de .   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------ --

## Hardware Requirements

To use this package you need a stereo camera system or an RGBD device
that delivers point clouds with color information. Alternatively you can
use a simulated version without any hardware, see
[cob_gazebo](cob_gazebo).

## ROS API

The [cob_object_detection](cob_object_detection) package provides a
configurable node for detecting textured objects based on local feature
point detection and 3D model matching.



```clearsilver
 name = cob_object_detection
 desc = The cob_object_detection node takes in <<MsgLink(sensor_msgs/PointCloud2)>> messages generated e.g. from a stereo camera pair or an RGBD camera device and performs 6 DOF object detection based on previously trained object models. Object detection and training is triggered using [[Services|services]] or [[actionlib|actions]]. Visualization and the detection results are published on [[Topics|topics]].

goal{
 0.name=/object_detection/acquire_object_image/goal
 0.type=cob_object_detection_msgs/AcquireObjectImageActionGoal
 0.desc=Goal for training procedure to acquire object
 1.name=/object_detection/detect_object/goal
 1.type=cob_object_detection_msgs/DetectObjectsActionGoal
 1.desc=Goal for executing object detection procedure
 2.name=/object_detection/train_object/goal
 2.type=cob_object_detection_msgs/TrainObjectsActionGoal
 2.desc=Goal for training object including the object model name
}

result{
 0.name=/object_detection/acquire_object_image/result
 0.type=cob_object_detection_msgs/AcquireObjectImageActionResult
 0.desc=empty
 1.name=/object_detection/detect_object/result
 1.type=cob_object_detection_msgs/DetectObjectsActionResult
 1.desc=List of detect object instances including a confidence and pose estimate
 2.name=/object_detection/train_object/result
 2.type=cob_object_detection_msgs/TrainObjectActionResult
 2.desc=empty
}

feedback{
 0.name=/object_detection/acquire_object_image/feedback
 0.type=cob_object_detection_msgs/AcquireObjectImageActionFeedback
 0.desc=Feedback holds number to indicate the approximate progress
 1.name=/object_detection/detect_object/feedback
 1.type=cob_object_detection_msgs/DetectObjectsActionFeedback
 1.desc=Feedback holds number to indicate the approximate progress
 2.name=/object_detection/train_object/feedback
 2.type=cob_object_detection_msgs/TrainObjectActionFeedback
 2.desc=Feedback holds number to indicate the approximate progress
}

sub{
 0.name = /sensor_fusion/stereo/reprojection_matrix
 0.type = cob_object_perception_msgs/ReprojectionMatrix
 0.desc = Reprojection matrix to project 3D coordinates given by <<MsgLink(sensor_msgs/PointCloud2)>> to the 2D camera image plane. The matrix is necessary to render the detection results with a 2D bounding box.
}

pub{
 0.name = /object_detection/point_cloud_2
 0.type = sensor_msgs/PointCloud2
 0.desc = Point cloud visualization of the training process and the incoming 3D data for training and detection
 1.name = /object_detection/image
 1.type = sensor_msgs/Image
 1.desc = 2D visualization of the training images and the object detection results by rendering the bounding boxes of the detected objects 
}

srv_called{
 0.name = /sensor_fusion/stereo/get_colored_pc
 0.type = cob_srvs/GetPointCloud2
 0.desc = Point cloud representing a single view on the current scene image. RGB data of point cloud must represent a 2D image in order to be able to perform feature extraction.
}

srv {
 0.name = /object_detection/detect_object
 0.type = cob_object_detection_msgs/DetectObjects
 0.desc = Executes object detection procedure
 1.name = /object_detection/train_object
 1.type = cob_object_detection_msgs/TrainObject
 1.desc = Executes object training procedure
 2.name = /object_detection/acquire_object_image
 2.type = cob_object_detection_msgs/AcquireObjectImage
 2.desc = Service is internally called by autonomous object training procedure
}

param{
 0.name = ~object_model_type
 0.type = string
 0.desc = Specifies the applied object model (MODEL_BAYES or MODEL_6D_SLAM). MODEL_BAYES applies bundle adjustment for 3D model generation and creates feature point clusters using mean shift on all affine transformations (natural and artificial) of all detected feature points. This should be your method of choice. MODEL_6D_SLAM applies FastSLAM for 3D model generation and does not do any clustering of feature points. It is the original object detection algorithm from which MODEL_BAYES emerged.
 1.name = ~visualization
 1.type = bool
 1.desc = Specifies if visualisation is calculated published on the corresponding topics. Visualisation lets you observe the object model generation process in 3D by drawing the generated object model that has been created after incorporating successive viewpoints of the object. It also gives you an impression of the detected object models in 2D by reprojecting the bounding
 2.name = ~logging
 2.type = bool
 2.desc = Specifies if log files are created for the training process (logs the number of features per viewpoint and the remaining number of features after clustering) and for the detection process (logs the number of detected features per object as well as the different confidence values)
 3.name = ~use_STAR_detector
 3.type = bool
 3.desc = Specifies if STAR detector is used for feature detection. For now, this value is not working, yet, and must always be false. However it is intended to integrate an arbitrary selection of feature point detector and descriptor for each object model.
 4.name = ~load_model_from_srs_database
 4.type = bool
 4.desc = Specifies if object models loaded form database. If there is an srs database server available, all object models will be loaded from the database.
 5.name = ~insert_generated_model_to_srs_database
 5.type = bool
 5.desc = Specifies if object models will stored into database. After object model generation process, the object will be stored in srs object database if the database is avalible.
 6.name = ~train_learning_pos_x
 6.type = float
 6.desc = Specifies the x position in camera coordinates of the training centre. Defining a training centre helps the training procedure to reduce the amount of superfluous data that has nothing to do with the training object and accelerates therefore the training procedure.
 7.name = ~train_learning_pos_y
 7.type = float
 7.desc = Specifies the y position in camera coordinates of the training centre. Defining a training centre helps the training procedure to reduce the amount of superfluous data that has nothing to do with the training object and accelerates therefore the training procedure.
 8.name = ~train_learning_pos_z
 8.type = float
 8.desc = Specifies the z position in camera coordinates of the training centre. Defining a training centre helps the training procedure to reduce the amount of superfluous data that has nothing to do with the training object and accelerates therefore the training procedure.
 9.name = ~train_learning_radius
 9.type = float
 9.desc = Specifies the cube length in meter measured from the training centre, to determine the image are that contains the object. e.g. a value of 0.1 will generate a 3D cube with edge length 0.2 meter and centre specified by the train_learning_pos_x, train_learning_pos_y and train_learning_pos_z variables. All 3D points within this cube are potentially relevant for object model creation. All other points are discarded.
 10.name = ~train_affine_fp_transforms
 10.type = bool
 10.desc = Determines if each training image should be artificially transformed to generate more views for object model training. This generates in general better detection results, however at the cost of a longer training time (approx. by factor 10).
 11.name = ~train_min_cluster_size
 11.type = integer
 11.desc = After extracting 2D feature points from all image views, many feature points describe one and the same point in 3D space. To reduce the object model size, the feature points are clustered based on 3D space distance and 2D descriptor distance. The parameter specifies the minimal number of feature points that must constitute a cluster e.g. if you chose 10 degree rotational steps for object model training, each image point is approximately seen from at least 4 different viewpoints. Therefore a cluster size of 3 is reasonable to filter out weak feature points.
 12.name = ~train_max_feature_match_dist_in_meter
 12.type = float
 12.desc = During object model generation process is is necessary to extract features on each viewing picture. if a feature is far from an other feature away, the feature cannot match.
 13.name = ~robot_building_models
 13.type = bool
 13.desc = Flag for object model generation process. If true the algorithm try to segment the grasper from the Care-O-bot 3.
 14.name = ~detect_ransac_norm_inlier_dist_thresh
 14.type = float
 14.desc = RanSaC is used for 3D model fitting. In order evaluate a pose estimate, RanSaC calculates the distance of detected feature points from their predited location based on the pose estimate. The parameters specifies the maximal difference in meter that is acceptable.
 15.name = ~detect_min_inlier_size
 15.type = integer
 15.desc = RanSaC is used for 3D model fitting. This value determines the minimal number of inliers that must be determined to count as a detection hit. This threshold value must be met for any detection result and presents the first choice to increase in case of false positive detections. 


}

req_tf{
}

prov_tf{
}
```



## Usage/Examples

The package can be used via a launch file which loads all parameters
from a .yaml file and starts the object_detection node.



```
roslaunch cob_object_detection object_detection.launch
```



For including the object_detection in your overall launch file use



```
<include file="$(find cob_object_detection)/ros/launch/object_detection.launch" />
```



A sample parameter file could look like this



```
# Object model type
# MODEL_BAYES or MODEL_6D_SLAM
object_model_type: MODEL_BAYES
# Visualize detection results in 3-D
visualization: true
# Write log files
logging: true
# Feature point detector
use_STAR_detector: false
# Parameters for srs database interface
# load the models form srs database or from local storage
load_model_from_srs_database: true
# if the build model ends successfully the object will be automatically add th the database
insert_generated_model_to_srs_database: false
# Parameters for object model training
# Use u, v parameters to limit training region
# Limit the training area of the image by cutting out 
# relevant regions
# Unit [px]
train_learning_segm_min_u: 500
train_learning_segm_max_u: 1300
train_learning_segm_min_v: 400
train_learning_segm_max_v: 1000

# XYZ and Radius DEPRECATED and no longer in us and no longer in usee, 
# X Position of object during training in camera coordinates
# Unit: [m]
train_learning_pos_x: 0.0776975028338
# Y Position of object during training in camera coordinates
# Unit: [m]
train_learning_pos_y: 0.188573
# Z Position of object during training in camera coordinates
# Unit: [m]
train_learning_pos_z: 0.837447
# Radius of training area for object segmentation during trainng
# Unit: [m]

train_learning_radius: 0.1
# Apply affine transformation to source images before feature extraction
train_affine_fp_transforms: false
# Minimal cluster size for feature points to be valid
train_min_cluster_size: 3
# After applying the odometry, matching features should ideally be at the same position.
# This value specifies the maximal difference in m that is allowed.
train_max_feature_match_dist_in_meter: 0.005
# Enable PreBuildSegmentation to eliminate grasp (sdh) from images and improve transformation data 
robot_building_models: true
# Parameters for object model detection
# Minimal cluster size for feature points to be valid
detect_ransac_norm_inlier_dist_thresh: 0.014
# Standard deviation of inlier points
detect_min_inlier_size: 10
```



## Definition of object coordinate system

The frame of the object is defined like the following picture.

![\|height="300"](attachment:bounding_box_conventions.png)

The front side of the object is the native object front like you would
place an object into a shelf. The the coordinate system is oriented to
the specific object. Normally the front side show in the negative
Y-direction. The Z-direction show vertical to the top.

## Tutorials

Tutorials can be found on the
[Tutorials page](cob_object_detection/Tutorials).

## Models

You can get model files either from <https://github.com/ipa320/srs_data>
or from an internal Server at IPA 

```
smb://saturn20.ipa.fhg.de/austauschipa/J0SF
```

 To insert
models into cob_object_detection, pllace the models you like to use in
the folder 

```
roscd cob_object_detection/common/files/models/ObjectModels/
```

 Either you delete the Info.txt or
you write the name correct inside the file. 

```
rm Info.txt
```

 The
object names must be "Model_<object_name>.txt".
