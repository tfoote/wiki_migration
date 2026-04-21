## Introduction

CVFH stands for (Clustered Viewpoint Feature Histogram) and its based on
VFH. CVFH is a global geometrical object descriptor based on the surface
properties of partial views. Even though, it is a global descriptor, it
is able to handle missing parts by robustly estimating patches (smaller
surfaces) which normal information and position are used as a reference
system to describe the rest of the object from that viewpoint. If many
stable patches, different descriptors are computed for the partial view.
Because the patches are estimated both in training and recognition, CVFH
will be able to handle missing parts as long as one of these patches can
be found in the cluster to be recognized.

Given segmentation, CVFH will retrieve the most similar object from the
training data together with its pose. CVFH can be learned from PLY
models which makes training of models from different viewpoints
straightforward. We have mainly tested CVFH using the Kinect sensor.

CVFH is not scale invariant, meaning that the dimensions of the training
model should be similar to those of the actual objects to be recognized.
Be aware that 3D models found on the internet (i.e Google Ware House) DO
NOT have a valid scale. For the moment, CVFH does not make use of
color/texture information (it is purely geometrical) so objects which
exact same surface properties in the geometrical sense but different
colors/texture won't be differentiated.

## Requisites

-   ROS diamondback with perception_pcl overlayed.
-   vfh_recognition, vfh_recognizer_fs and vfh_recognizer_fs_test
-   VTK 4.2

### How to overlay PCL?

Open a terminal and write:



```
svn co http://svn.pointclouds.org/ros/trunk/perception_pcl_unstable
```

 Modify your ROS_PACKAGE_PATH to make sure that
perception_pcl_unstable is found before perception_pcl from the
diamondback release. Then you can do:



```
rosmake pcl
```



### Getting vfh_recognition, vfh_recognizer_fs and vfh_recognizer_fs_test

Soon, all CVFH recognition stuff, will be packed into a stack to
facilitate installation. In the meanwhile, the easiest way to install
all needed packages is:

Open a terminal and write:



```
mkdir cvfh && cd cvfh
svn co https://code.ros.org/svn/wg-ros-pkg/stacks/tabletop_object_perception/trunk/vfh_recognition
svn co https://code.ros.org/svn/wg-ros-pkg/stacks/tabletop_object_perception/trunk/vfh_recognizer_fs
svn co https://code.ros.org/svn/wg-ros-pkg/stacks/tabletop_object_perception/trunk/vfh_recognizer_fs_test
```

 If you created the directory outside of your
ROS_PACKAGE_PATH, modify it accordingly so ROS finds the packages.



```
cd vfh_recognizer_fs_test
rosmake
```

 and that should be it!

## vfh_recognition

This is the base package which contains all the logical structure for
recognition using CVFH. vfh_recognizer_fs and vfh_recognizer_db are
subpackages from vfh_recognition that include utils to train the
classifier from the household_object_database or from a filesystem
directory respectively. They also provide an interface to the underlying
data structures like pose, PLY models, generated views, etc\...

## vfh_recognizer_fs

Provides training utils and IO interface to use the CVFH classifier
using the filesystem as persistence backend.

------------------------------------------------------------------------

### How to train the classifier?

Step 1) Place PLY models in a directory on your filesystem \$ROOT_DIR,
i.e (/home/cvfh/ply_models)

Step 2) In a terminal, write (REMEMBER to start roscore before this):



```
rosrun vfh_recognizer_fs normals_vfh_db_estimator_server
```

 Step 3) Open a new terminal (Shift + Ctrl + n)
or a new tab (Shift + Ctrl + t) and write:



```
rosrun vfh_recognizer_fs remove_duplicate_views_server
```

 Step 4) Open a new terminal or tab and write:



```
roscd vfh_recognizer_fs
python scripts/process_training_data.py /home/cvfh/ply_models 1
```

 The last parameter to the Python script (1) is
the scale factor to transform the models to meters. If the PLY models
are in mm, then use 0.001 and so on\...

------------------------------------------------------------------------

The steps above start loading each model in the directory, generating
partial views from each model and the services
normals_vfh_db_estimator_server and remove_duplicate_views_server
compute the descriptors for each partial view and remove those views
that do not provide additional information (mainly in rotationally
symmetric objects, the object seen from a viewpoints looks the same as
seen from different viewpoints. ONLY one of these views, will be
trained).

The training steps will generate several directories under \$ROOT_DIR
(centroids, transforms, views\...)

**Important**:

-   Once you start running the Python script, you will see a window with
    red background that will display one of the models from different
    viewpoints. The window should always be visible on your screen,
    otherwise the views generated will be empty.
-   This is a limitation of VTK on Unix platforms that does not allow
    offScreenRendering. My recommendation: when you start training the
    models, go for a coffee and remember to turn off the screensaver of
    your computer. If you have a lot of them, go home and check the next
    day :) It should take between 1 and 3 minutes per model, depending
    on the amount of views generated per model (default are 80 views).

## vfh_recognizer_fs_test

Provides test interfaces to classify table top scenes using CVFH.

### scene_vfh_recognizer

__Input__: a point cloud obtained from a 3D depth sensor like the
Kinect that contains a stable plane on which the objects to be
classified stand.

__Output__: Displays in a visualization window the input scene,
together with the segmented clusters (displayed in red), the best
training partial view (displayed in green) and the PLY model overlayed
on top of it. By pressing W or S, the PLY models can be visualized using
a wireframe or solid representation.

__How to run it?__

Assuming that you have the Kinect running, you need to:



```
rosrun vfh_recognizer_fs_test scene_vfh_recognizer /home/cvfh/ply_models input_cloud:=/camera/rgb/points
```

 and you should see something like this:

![](attachment:cvfh_recognition.png)

Check <http://www.youtube.com/watch?v=1kMhvT3nATk> for another example.

## Contact

You might need to do additional steps like installing missing
dependencies. If you feel that something is missing in this page, you
find a bug or have any other request, I will appreciate if you contact
me at: aldoma.aitor ( at ) gmail.com. Thank you!
