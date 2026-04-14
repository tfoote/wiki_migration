### Description

This tutorial describes how to use an in hand object modeling on a PR2
robot in order to obtain models of unknown objects based on the data
collected with an RGB camera observing the robot's hand while moving the
object. The goal is to develop the technique that enables robots to
autonomously acquire models of unknown objects, thereby increasing
understanding. Ultimately, such a capability will allow robots to
actively investigate their environments and learn about objects in an
incremental way, adding more and more knowledge over time.

### Prerequisite

\- Put the object in PR2\'s gripper and bring the object into the field
of view of the camera. Make sure the background is neutral (e.g. white
wall).

\- Rotate the gripper around its approach axis. You can use our provided
script (TBD) or write one on your own.

\- Install robot_mask package.

### Usage

To extract the appearance models of the rotated object we will be using
the following launch file:

```xml
  <launch>
	<node  pkg="model_completion" type="in_hand_modeling" name="get_mask_client" output="screen"  >
	<param name="width" value="640" />
	<param name="height" value="480" />
	<param name="fovy" value="47" />
	<param name="camera_frame" value="openni_rgb_optical_frame" />
	<param name="image_topic" value="/camera/rgb/image_mono" />
	<param name="save_images" value="true" />
	<param name="tf_topic" value="/tf" />
	<param name="min_nn" value="5" />	
        <param name="knn" value="4" />
        <param name="mode" value="knn_search" />
	</node>
	<param name="robot_description" textfile="$(find model_completion)/robot/robot.xml"/>
	<node  pkg="robot_mask" type="robot_mask" name="robot_mask" output="screen" >
	</node>
</launch>
```

There are several parameters that control the object modeling process:

-   \'\'width\'\', \'\'height\'\', \'\'fovy\'\' - are the width, height
    and vertical focal length of the camera used;
-   \'\'image_topic\'\' - input images topic;
-   \'\'tf_topic\'\' - robot\'s TF tree;
-   \'\'save_images\'\' - a parameter to save the images (by default
    saved in the home/.ros folder);
-   \'\'min_nn\'\' - an integer value for the minimum number of
    neighbors allowed when using the radiusSearch function;
-   \'\'knn\'\' - the number of neighbors searched with knnSearch
    function;
-   \'\'mode\'\' - which function to use to get rid of outlier features.
    Options are: \"manual\", \"radius_search\", \"knn_search\" (see an
    explanation below on the meaning of the parameters);
-   \'\'robot_description\'\' - upload robot\'s URDF if working on
    rosbags.

To start the program run: ```
$ roslaunch model_completion getMask.launch
```

#### The overview of the program can be seen in the following figure:

![](attachment:system_overview55.jpg)

### Intuition Behind the Use of radiusSearch and knnSearch

As it can be seen, images contain a considerable number of outliers (see
figure below), especially on the robot\'s gripper and the goal is to
remove these SIFT features through nearest-neighbor search. We are going
to use two methods: radius search and knn search. For this all the
features need to be extracted in order to check the nearest neighbors in
a specified radius for the first method and a specified number of
neighbors for the second one. For good results in obtaining our
templates (on 640x480 images) we vary the radius between 20 and 30
pixels and the number of neighbors between 2 and 5. After removing the
outlier features it is trivial to extract the region of interest by
computing a bounding-box rectangle around the inlier features.

![](attachment:outliers_visualization2.jpg)
