------------------------------------------------------------------------

## Additional data on ICRA 2020 paper submission

Complementary experimental evaluation data on the paper submission

*Richard Bormann, Xinjie Wang, Jiawen Xu. DirtNet: Visual Dirt Detection
for Autonomous Cleaning Robots. Submitted to the IEEE International
Conference on Robotics and Automation (ICRA), 2020.*

is available from here:

-   Measured improvements on DirtNet adaptations:
    <https://github.com/baker-project/baker_documentation/blob/master/ipa_dirt_detection/dirtnet_improvements.md>
-   Influence of synthetic training set size:
    <https://github.com/baker-project/baker_documentation/blob/master/ipa_dirt_detection/training_dataset_size_variation.md>
-   Dirt Detection Performance:
    <https://github.com/baker-project/baker_documentation/blob/master/ipa_dirt_detection/detection_performance_10cls_and_2cls.md>

### New dirt detection data set (2020)

The new dirt detection data set used in the ICRA 2020 paper can be
downloaded from here:
<https://owncloud.fraunhofer.de/index.php/s/AjsDYny2Xmxyl44> .

------------------------------------------------------------------------

This page describes the usage of the dirt detection software developed
within the BakeR project. Its purpose is to find dirt spots on the
ground and put them into a map of the environment. This documentation is
split into three parts: the first describes the dirt detection system,
the second introduces the dirt dataset that has been recorded to test
the dirt detection algorithm and the third explains how to use the test
framework to evaluate the *`ipa_dirt_detection`* or your own dirt
detection algorithm on the dirt dataset.

## Dirt Detection Software

The dirt detection software is intended to run on human-sized service
robots with the ability to localize themselves in the environment. The
current implementation has been recorded and tested on a Care-O-bot 3
platform which uses the RGB-D sensor Microsoft Kinect to capture the
necessary point cloud and image data for dirt detection. These simple
requirements allow for an easy application of the dirt detection
algorithm on a different robot.

### Quick Start

The usage of the dirt detection system is quite simple. If you are
working with a Care-O-bot 3, start the robot, launch the bringup scripts
and the localization, e.g. with ```
roslaunch cob_navigation_global 2dnav_ros_dwa.launch
``` and launch the
dirt detection software with ```
roslaunch ipa_dirt_detection dirt_detection.launch
``` If you want to
detect dirt on a bag-file data stream, start the dirt detection software
and then play the bag-file.

The dirt detection software expects to receive the topics `/tf`
(transformation tree) and `/cam3d/rgb/points` (the colored point cloud
from the RGB-D sensor). If you are using a different robot make sure
that the topics are remapped accordingly in the launch-file. As long as
you provide a proper transformation from the `/map` frame to the camera
frame the dirt detection software should **work with any robot**.

The algorithm publishes the topic `/dirt_detection/detection_map` which
displays the detected dirt as dark cells in a grid map. You can use RViz
to visualize the resulting dirt map.

There are further launch files provided with the ipa_dirt_detection
package for different purposes:

-   Labeling is explained in Section
    [Recording and Labeling Your Own Bag-Files](ipa_dirt_detection#Recording_and_Labeling_Your_Own_Bag-Files).
-   Database testing is explained in Section
    [Database Testing](ipa_dirt_detection#Database_Testing)

```clearsilver
name = ROS API
desc = The parameters, topics, services and actions provided or needed by the dirt detection system are described here.
param {
  group.0 {
    name = General Parameters
    0.name = modeOfOperation
    0.type = int
    0.desc = chooses a mode of operation: 0=detection, 1=labeling, 2=database test
    0.default = 0
    1.name = dirtThreshold
    1.type = double
    1.desc = dirt threshold, necessary strength of rescaled spectral residual filter response to consider a pixel as dirt (range [0,1])
    1.default = 0.2
    2.name = warpImage
    2.type = bool
    2.desc = if true, image warping to a bird's eye perspective is enabled
    2.default = true
    3.name = birdEyeResolution
    3.type = double
    3.desc = resolution for bird eye's perspective [pixel/m]
    3.default = 300.0
    4.name = maxDistanceToCamera
    4.type = double
    4.desc = only those points which are close enough to the camera are displayed in the bird's eye view [max distance in m]
    4.default = 3.00
    5.name = removeLines
    5.type = bool
    5.desc = if true, strong lines in the image will not produce dirt responses
    5.default = true
    6.name = gridResolution
    6.type = double
    6.desc = spatial resolution of the dirt detection grid in [cells/m], do not use too many cells per meter unless your localization is extremely accurate, 20 cells per meter are appropriate if your localization is as accurate as +/-5 cm
    6.default = 20.0
    7.name = gridOrigin_x, gridOrigin_y
    7.type = double
    7.desc = these two coordinates represent the center of your area of operation, they can be determined by observation of the robot coordinates in rviz (or to be exact the coordinates where the robot's view meets the floor), these coordinates are set automatically in database testing mode
    7.default = 0, 0
    8.name = floorSearchIterations
    8.type = int
    8.desc = the number of attempts to segment the floor plane in the image
    8.default = 3
    9.name = minPlanePoints
    9.type = int
    9.desc = minimum number of points that are necessary to find the floor plane
    9.default = 100
    10.name = planeNormalMaxZ
    10.type = double
    10.desc = maximum z-value of the plane normal (ensures to have an floor plane)
    10.default = -0.5
    11.name = planeMaxHeight
    11.type = double
    11.desc = maximum height of the detected plane above the mapped ground
    11.default = 0.3
    12.name = spectralResidualNormalizationHighestMaxValue
    12.type = double
    12.desc = maximum of the spectral residual image with artificial dirt can be at maximum at this number, the spectral residual image is scaled to the ratio (max/spectralResidualNormalizationHighestMaxValue)
    12.default = 1500.0
    13.name = spectralResidualGaussianBlurIterations
    13.type = int
    13.desc = spectral residual component: number of Gaussian smoothing operations
    13.default = 3
    14.name = spectralResidualImageSizeRatio
    14.type = double
    14.desc = side length of the fourier transformed image relative to the width of the original image
    14.default = 0.25
  }
  group.1 {
    name = Visualizations for Debugging
    desc = debug display switches - enable or disable the display of several kinds of images
    0.name = showOriginalImage
    0.type = bool
    0.desc = displays the original source image that comes with the point cloud data
    0.default = false
    1.name = showPlaneColorImage
    1.type = bool
    1.desc = shows only the part of the color image that belongs to the plane, the remainder is masked black
    1.default = true
    2.name = showWarpedOriginalImage
    2.type = bool
    2.desc = shows the warped color image of the plane
    2.default = false
    3.name = showSaliencyBadScale
    3.type = bool
    3.desc = displays the saliency image before rescaling
    3.default = false
    4.name = showColorWithArtificialDirt
    4.type = bool
    4.desc = displays the color image with the artificial dirt added
    4.default = false
    5.name = showSaliencyWithArtificialDirt
    5.type = bool
    5.desc = displays the filter response to the image with artificial dirt
    5.default = false
    6.name = showSaliencyDetection
    6.type = bool
    6.desc = displays the rescaled saliency image
    6.default = true
    7.name = showDetectedLines
    7.type = bool
    7.desc = displays the detected lines in the image that might be used to shadow false positives
    7.default = false
    8.name = showDirtDetections
    8.type = bool
    8.desc = displays the dirt detection results drawn into the color image
    8.default = true
    9.name = showObservationsGrid
    9.type = bool
    9.desc = displays the grid that illustrates the number of observations of each floor cell (the image might be displayed rotated)
    9.default = true
    10.name = showDirtGrid
    10.type = bool
    10.desc = displays the grid that illustrates the dirt detections at each floor cell (the image might be displayed rotated)
    10.default = true
  }
  group.2 {
    name = Special Parameters for Labeling Mode
    0.name = labelingFilePath
    0.type = string
    0.desc = path to labeling file storage
    0.default = "$(find ipa_dirt_detection)/common/files/"
  }
  group.3 {
    name = Special Parameters for Database Testing Mode
    0.name = databaseFilename
    0.type = string
    0.desc = the path and file name of the database index file
    0.default = "$(find ipa_dirt_detection)/common/files/results/test/dirt_database.txt"
    1.name = experimentSubFolder
    1.type = string
    1.desc = subfolder name for storing the results of the current experiment - useful in order to avoid overwriting existing data when multiple experiments are running on the same machine in parallel
    1.default = "test"
  }
}
sub {
  0.name = colored_point_cloud remapped to /cam3d/rgb/points
  0.type = sensor_msgs/PointCloud2
  0.desc = colored point cloud from RGB-D sensor
}
pub {
  group.0 {
    name = Detection Mode
    0.name = /dirt_detection/detection_map
    0.type = nav_msgs/OccupancyGrid
    0.desc = the map which stores the dirt detections in its grid cells
  }
  group.1 {
    name = Database Testing Mode
    0.name = /dirt_detection/colored_point_cloud_bagpub
    0.type = sensor_msgs/PointCloud2
    0.desc = this channel publishes the point cloud that is read from the bag-file, the data is directly remapped to colored_point_cloud and thus redirected to the detection callback function of the dirt detection system
    1.name = /clock
    1.type = rosgraph_msgs/Clock
    1.desc = the ROS clock topic is published to fit the data from the bag-file
    2.name = /dirt_detection/ground_truth_map
    2.type = nav_msgs/OccupancyGrid
    2.desc = the map that provides the ground truth of present dirt
    3.name = /dirt_detection/detection_map
    3.type = nav_msgs/OccupancyGrid
    3.desc = the map which stores the dirt detections in its grid cells
  }
}
```

## (Old 2013) Dirt Dataset

In order to conduct a proper evaluation of the dirt detection algorithm,
a novel dirt database has been recorded and labeled with ground truth.
The dataset provides 65 different kinds of dirt recorded at 5 floor
materials. This section introduces the dirt dataset by explaining the
recording conditions and the contents.

### Recording Setup

The whole database has been recorded with the service robot Care-O-bot 3
under realistic conditions. The Care-O-bot 3 platform is equipped with a
mobile base, an arm for manipulation and a sensor head for perception as
depicted in Figure 1(a). The integrated laser scanners are utilized to
localize the robot within the environment during the recordings. This
allows the detection software to relate dirt detections to real
locations at the floor and furthermore enables the software to integrate
detections in a map. In order to increase the reusability of the dirt
detection algorithm the data was recorded with the general purpose RGB-D
camera Microsoft Kinect mounted inside the robot's head. For the
recordings, the flexible torso of Care-O-bot was bowed to the front to
maximize the visible ground area close to the robot. This way the
recorded data can be retained with the highest possible resolution and
the robot is more likely being able to record every part of the ground
surface. The camera is mounted at a height of 1.26 m above the ground
and is tilted downwards by 30°.

For capturing the dirt database various kinds of dirt have been
distributed at the floor with a minimum distance of ca. 20 cm between
the samples. Then the robot was manually driven through the room
imitating the behavior of exploring the scene. This means that the robot
was usually driven forwards into the dirty area and then backwards in
conjunction with several turns. The data stream of the sensors has been
recorded into ROS bag-files that contain

-   the `/tf` topic, which allows for the conversion from camera to
    fixed world coordinates,
-   the `/cam3d/rgb/points`, which is basically the colored point cloud
    of the Microsoft Kinect sensor at a resolution of 640x480 pixels,
    and
-   the `/cam3d/rgb/image_color` topic, which represents the color image
    of the Kinect sensor at a resolution of 1024x768 pixels. Given this
    selection of data, dirt recognition algorithms are enabled to
    segment the ground plane, to choose between the lower or higher
    color image resolution for dirt recognition, and to transform the
    respective coordinates between the camera and the fixed world
    coordinate systems. The next section details which kind of data has
    been recorded under the described conditions.

![Figure 1\|width=640,align="middle"](attachment:dirt-dataset-overview.png)

### Dataset

The dirt database contains 5 different floor materials that were
recorded with 9 groups of dirt and under clean conditions each,
resulting in a total of 50 bag-files. The ground surfaces are depicted
in Figure 1 and the 9 groups of dirt can be found in Figure 2. Each of
these groups contains 6 to 10 different items totaling in 65 distinct
kinds of dirt for the whole database. The captured sequences have a
length of 12 s to 55 s and contain between 100 and 300 frames of point
cloud and image data. The file sizes range between 1.18 GB and 4.86 GB.
Every data sequence is accompanied by a ground truth file that labels
the position and extent of the present dirt by means of a rotated
rectangle as well as the type of dirt. The coordinates of the ground
truth labels are provided in the fixed world frame which is possible
because of the localization of the mobile robot. This proceeding has the
advantage that each piece of dirt has to be labeled only once per
bag-file and not for every frame.

![Figure 2\|width=640,align="middle"](attachment:dirt-dataset-dirt-overview.png)

### Download and Usage of the Dirt Dataset

The dirt database is available for download at
<http://153.97.5.95/data/dirt_dataset/>. Because of their size the 50
bag-files need to be downloaded individually. The labels and file
listing of bag-files to test are provided for all bag-files in the
archive `dirt-dataset-annotation.zip`. Please cite our ICRA paper when
using our datase (see [References](ipa_dirt_detection#References)).

Furthermore, we provide another sequence named `apartment-show.bag`
which contains the transition between two types of floors. This file is
not annotated.

You can either play those bag-files and watch the results with the dirt
detection system by following the directions provided in Section
[Dirt Detection Software](ipa_dirt_detection#Dirt_Detection_Software) or
you can run a database test, which is explained in Section
[Database Testing](ipa_dirt_detection#Database_Testing).

### Recording and Labeling Your Own Bag-Files

In order to create your own bag-files for a database test with the
Care-O-bot, start the robot, launch cob_bringup as well as a mapping
tool like cob_navigation_global 2dnav_ros_dwa.launch in case you already
have a map of your environment or cob_navigation_slam
2dnav_ros_dwa.launch if you do not have a map. Then record the following
topics ```
rosbag record /tf /cam3d/rgb/points /cam3d/rgb/image_color /map
``` The `/map` topic does not need to be
recorded if you do not aspire to display the results in the original
map.

After recording the bag-file, start the dirt detection software with
```
roslaunch ipa_dirt_detection dirt_detection_labeling.launch
``` and then play the recorded bag-file with
```
rosbag play --clock -l <name-of-your-file>
``` You can also use the -r <number> option to
play the bag-file at a different speed. After a few seconds, the dirt
detection software will open two images showing the normal view onto the
scene as well as the warped image. Click into one of the images to move
the focus to it and press 'l' whenever you like to label a view. Now a
third image with the title 'labeling image' pops up. Press the 'h'
button to list all keys that you can use for labeling your data. By
pressing the left mouse button if the upper left corner of the dirt item
and releasing it in the lower right corner you can draw a label box.
This box can then be changed in size and rotated. When you arranged if
in the desired position press the 'enter' key and type a descriptive
label of your choice. You may use the 'space' key for multiple words.
Finish the typing by pressing 'enter' again. Please notice that you
only have to label each particle once per bag-file as the labels are
converted to fixed world coordinates of the /map frame because the dirt
is mapped. After labeling all items, press the 'esc' key. Now, you
will see the playback stream of the bag-file again. Whenever you like to
label more items within the stream, press 'l' again and label. Should
you receive warnings from tf continuously during the repetitions of the
playback, restart the rosbag play command. After all data of the
bag-file has been labeled, press the 'f' key while the image stream is
displayed and the labeling data will be written into
`ipa_dirt_detection/common/files/train.xml`. Rename the file to the same
name as the your bag-file (but keep ending .xml) and place it in the
same folder as the bag-file. Please restart the dirt_detection software
after labeling a bag-file to avoid storing the information of a previous
bag-file again in the next. You can now use the labeled bag-files for
your own database test by putting the name without ending into the
database index file `dirt_database.txt`. Do not forget to increment the
number of files in the second row of the file. To use the mapping part,
please open rviz while your bag-file is playing and display the colored
point cloud. Estimate the x- and y-coordinates of the center of your
recordings approximately with the grid of rviz and put those numbers
separated by a whitespace after the file name. A valid entry in
`dirt_database.txt` looks like ```
filename-without-ending x-coordinate y-coordinate
```

## Database Testing

This section explains how to use the testing framework to reproduce the
results obtained with the dirt detection algorithm developed in the
BakeR project and how to test your own algorithm.

### Database Testing with the BakeR Dirt Detection Algorithm

The ipa_dirt_detection package contains three launch files that
reproduce the results stated in \[1\]. 1.
`dirt_detection_dbtest_withoutwarp.launch` starts dirt detection without
warping the camera images to a bird's eye view. 1.
`dirt_detection_dbtest_withwarp.launch` starts the dirt detection
algorithm that operates on images which are transformed into the bird's
eye perspective. 1. `dirt_detection_dbtest_withlineremoval.launch`
launches dirt detection on images in bird's eye perspective and with
the removal of lines to decrease false positives.

There is an index file for database tests which tells the algorithm
which bag-files are included in the test. This file does already exist
for the provided dirt database (for your own bag-files see
[Recording and Labeling Your Own Bag-Files](ipa_dirt_detection#Recording_and_Labeling_Your_Own_Bag-Files)).
Before launching any of the three prepared database tests please go to
the respective folder
`ipa_dirt_detection/common/files/results/<experiment_name>` and open the
index file dirt_database.txt. You need to put the appropriate path to
your storage location of the bag-files from the dirt dataset in the
first line.

Then start the database test with ```
roslaunch ipa_dirt_detection dirt_detection_dbtest_<experiment_name>.launch
``` Depending on
the speed of your hard disc and processor your computer will now compute
for some hours or up to a day. The results will be written into
`ipa_dirt_detection/common/files/results/<experiment_name>`.

After all bag-files have been processed you can generate
recall-precision plots by opening
`common/matlab/dirtDetectionStatistics.m` in Matlab. Before executing
the script, enter the correct path to your results in the parameter
section. The script allows you to adjust some parameters that are
directly described in the code.

### Database Testing with Your Own Dirt Detection Algorithm

It is easy to adapt the dirt detection software to use your own dirt
detection algorithm. To do so have a look at the function
`void DirtDetection::planeDetectionCallback(const sensor_msgs::PointCloud2ConstPtr& point_cloud2_rgb_msg)`
in file `ros/src/dirt_detection.cpp`. This is the current callback
function that initiates the dirt detection procedure. You can define a
similar function and register it as callback. If you need to use
different input data to the function please also adapt the publishers in
function `void DirtDetection::databaseTest()`.

Please make sure that your dirt detection callback function

-   outputs a map of the detections,
-   increments `rosbagMessagesProcessed_`.

## Support

Please consult to see if your problem is already known.

Please use the
[mailing list](http://www.care-o-bot-research.org/contributing/mailing-lists)
for additional support or feature discussion.

## Report a Bug

Use [trac](http://www.care-o-bot-research.org/trac) to report bugs or
request features.
[View active tickets](http://www.care-o-bot-research.org/trac/report/1)

## References

Please cite our ICRA paper when using our dataset or software. 1. R.
Bormann, F. Weisshardt, G. Arbeiter, and J. Fischer. Autonomous dirt
detection for cleaning in office environments. In Proceedings of the
IEEE International Conference on Robotics and Automation (ICRA), pages
1252--1259, 2013. 1. R. Bormann, J. Fischer, G. Arbeiter, F. Weißhardt,
and A. Verl. A visual dirt detection system for mobile service robots.
In Proceedings of the 7th German Conference on Robotics (ROBOTIK 2012),
Munich, Germany, May 2012.
