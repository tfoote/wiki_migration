This package is for target object detection package, which handles point
clouds data and recognize a trained object with SVM.

An example of using the packages can be seen in
[Robots/CIR-KIT-Unit03](Robots/CIR-KIT-Unit03).

## Requirements

-   PCL 1.7+
-   boost
-   ROS(indigo)

## ROS API

This package is using 3D pointcloud(pointcloud2) to recognize.

```
$ roslaunch target_object_detector target_object_detector.launch
```

```clearsilver
sub {
  0.name= tf
  0.type= tf/tfMessage
  0.desc= Transforms (/map, /base_link and sensor_frame)
  
  1.name= /amcl_pose
  1.type= geometry_msgs/PoseWithCovarianceStamped
  1.desc= Robot's estimated pose in the map, with covariance.

  2.name= /hokuyo3d/hokuyo_cloud2
  2.type= sensor_msgs/PointCloud2
  2.desc= Output of measured point cloud in PointCloud2 message type which contains all multi echos with intensity. Published on demand.
}
```

## Usage

### Train

First, make \`dataset/traian\` directory in this pkg. Then move there.

```
roscd target_object_detector
mkdir -p dataset/train
cd dataset/train
```

Run the segmentation node in the directory.

```
rosrun target_object_detector segment_cluster_creator_node
```

Take a poingcloud by running the robot or play bag file include
\`pointclioud2\` msg. You will get a lot of pcd files in the directory.
Next, classify the pcd files.

```
rosrun target_object_detector train_data_create_tool
```

After classified all pcd files, you will get \`train.csv\` in the
directory. Third, making svm model.

```
roscd targe_object_detector/src/libsvm/tools/
python easy.py path/to/train.csv
```

### Human detection

#### Actual detection

```
roslaunch target_object_detector target_object_detector.launch
```

#### Fake detaction

You can utilied \`fake_target_detector\` to assume a target is virtually
detected, if you just check navigation behaivior **\*without actual
human detection.**\*

A virtually detected target human point can be set by clicking a point
in a map with \`Publish point\` in \`Rviz\`.

The following command shows a coordinate of clicked point.

```
rostopic echo /clicked_point
```

Save the coordinate \`x, y\` to\`targetlist/targetlist.csv\` (\[a sample
file\](<https://github.com/CIR-KIT/human_detector/blob/mm/add/document/fake_target_detector/targetfiles/targetlist.csv>)).

To place an virtual target, run the following command.

```
rosrun fake_target_detector fake_target_detector
```

Bounding boxes will be showin at positions specified in
\`targetlist.csv\` and the virtually detected positions are also to be
published.

#### Common specification

Satisfying all of the following conditions invoke approching to a
target.

-   A currently reached waypoint is placed in detecting area.
-   A target human is within 5 \[m\] from the robot.
-   The target is **\*NOT**\* close to points where other targets are
    previously detected.

### Example of usage in GAZEBO

#### Start GAZEBO world with human models.

```
roslaunch cirkit_unit03_autorun autorun_gazebo_with_human.launch
```

#### Tune robot position with 2D Pose Estimate on Rviz.

#### Move Human models to an arbitary place on Rviz, if needed.

#### Run detector.

```clearsilver
sub {
  0.name= tf
  0.type= tf/tfMessage
  0.desc= Transforms (/map, /base_link and sensor_frame)
  
  1.name= /amcl_pose
  1.type= geometry_msgs/PoseWithCovarianceStamped
  1.desc= Robot's estimated pose in the map, with covariance.

  2.name= /hokuyo3d/hokuyo_cloud2
  2.type= sensor_msgs/PointCloud2
  2.desc= Output of measured point cloud in PointCloud2 message type which contains all multi echos with intensity. Published on demand.
}
```0
