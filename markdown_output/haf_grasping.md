## DOCUMENTATION

This package calculates graspable regions at unknown (or known) objects.

HAF_GRASPING calculates grasp points for unknown and known objects
represented by object point cloud data. For scientific foundation see:
[\'\'\'D. Fischinger, A. Weiss, M. Vincze: \"Learning Grasps with Topographic Features\", The International Journal of Robotics Research. (2015)\'\'\'](https://www.researchgate.net/publication/277926854_Learning_grasps_with_topographic_features)

\<\<Youtube(3V29-xR-aFM&rel=0)\>\>

## SIMPLE START: HOW TO USE HAF_GRASPING

This part shows how to get the code running and visualizes the grasp
calculation for a point cloud in RVIZ:

CREATE CATKIN WORKSPACE

```
>> mkdir -p ~/haf_grasping_ws/src
>> cd ~/haf_grasping_ws/src
>> catkin_init_workspace
``` OR navigate to an existing \*src\* folder of
your ROS workspace:

```
cd location_of_workspace/src
``` DOWNLOAD CODE (and add the path to the
environment variable ROS_PACKAGE_PATH if needed)

```
>> git clone https://github.com/davidfischinger/haf_grasping.git
``` Execute \"make\" in the libsvm folder:

```
>> roscd haf_grasping/libsvm-3.12
>> make
``` CATKIN_MAKE OF PACKAGE HAF_GRASPING

```
>> roscd haf_grasping/../..
>> catkin_make -DCMAKE_BUILD_TYPE=Release
>> source devel/setup.sh
``` Start calculation server (does the work),
haf_client (small program including the class that shows how to use
haf_grasping) and a visualization in rviz:

```
>> roslaunch haf_grasping haf_grasping_all.launch
``` Publish the path of a point cloud to calculate
grasp points on this object with the gripper approaching direction along
the z-axis:

```
>> rostopic pub /haf_grasping/input_pcd_rcs_path std_msgs/String "$(rospack find haf_grasping)/data/pcd2.pcd" -1
``` Alternatively, publish a point cloud to the ROS
topic: /haf_grasping/depth_registered/single_cloud/points_in_lcs:

```
>> roscd haf_grasping/data
>> rosrun pcl_ros pcd_to_pointcloud pcd2.pcd cloud_pcd:=/haf_grasping/depth_registered/single_cloud/points_in_lcs
```

### EXPLANATION FOR THE RVIZ VISUALIZATION

RVIZ will now visualize the point cloud with its corresponding frame
(blue indicates the z-axis).

\'\'\'Bigger grey rectangle:\'\'\' indicates the area where heights can
be used for grasp calculation

\'\'\'Inner grey rectangle:\'\'\' defines the area which is searched for
potential grasps (grasp centers).

\'\'\'Long red line:\'\'\' indicates the closing direction (for a two
finger gripper)

\'\'\'Red/green spots:\'\'\' indicate the positions where grasps are
really tested for the current gripper roll (ignoring points where no
calculation is needed, e.g. no data there)

\'\'\'Green bars:\'\'\' indicate identified potential grasps available.
The height of the bars indicates the grasp evaluation score (the higher
the better)

\'\'\'Black arrow:\'\'\' indicates the best grasp position found and the
approaching direction (for a parallel two finger gripper)

\'\'Visualization of the grasp calculation process in rviz:\'\'

![\|height=\"212\",width=\"379\"](attachment:haf_in_rviz1.png)
![haf_in_rviz1.png\|height=\"207\",width=\"372\"](attachment:haf_in_rviz2.png)

\'\'Red line indicates currently tested gripper opening direction, red
points indicate positions where no grasp was found, green bars indicate
positions where grasps were found - the higher the bar, the better the
quality.\'\'

![haf_in_rviz1.png\|height=\"312\",width=\"554\"](attachment:haf_in_rviz3.png)

Finally the top grasp (position and approaching direction of the
gripper) is shown by the black arrow together with the gripper
orientation (red line).

## ROS API

### ACTION SERVER

The package haf_grasping provides one
[SimpleActionServer](actionlib_tutorials/Tutorials/SimpleActionServer(ExecuteCallbackMethod)):

-   \`/calc_grasppoints_svm_action_server\`: requests the calculation of
    a grasp for a given point cloud. A simple implementation of the
    client can be found here:
    [calc_grasppoints_action_client.cpp](https://github.com/davidfischinger/haf_grasping/blob/master/src/calc_grasppoints_action_client.cpp):
    :
-   action definition:
-   goal:
    [GraspInput.msg](https://github.com/davidfischinger/haf_grasping/blob/master/msg/GraspInput.msg)
    defined by a point cloud and a number of settings for the action
    server

```{=html}
<!-- -->
```
-   result: std_msgs/String defining the best grasp found (see below)
-   feedback: std_msgs/String

```{=html}
<!-- -->
```
-   the object must have been previously segmented from the background

```{=html}
<!-- -->
```
-   the action will then:
-   calculate the best grasp for a parallel gripper approaching the tool
    center point along the z-axis of the coordinate frame.

### PARAMETER SETTING AND PROVIDED SERVICES

There are a number of parameters that can be set in the launch file
haf_grasping_all.launch or via a service call.

Approach vector: x,y,z-direction of the approach vector. The tool center
point of a gripper approaches the object in the opposite direction of
this vector. For the default vector (0,0,1) the gripper is going down
the z-axis towards the origin. Service to set the approach vector to
(1,1,1):

```
>> rosservice call /haf_grasping/set_approach_vector "approach_vector:  x: 1.0
  y: 1.0
  z: 1.0"
``` Grasp_center: the x-,y-,z-position, that is the
center of the area where grasps are searched. Set grasp search center
(in m) to (x=0.1,y=0,z=0) with a service call:

```
>> rosservice call /haf_grasping/set_grasp_center "graspsearchcenter:
   x: 0.10
   y: 0.0
   z: 0.0"
``` Grasp_area_size: the size of the area where
grasps should be detected. Set rectangle to 16x10 centimeter:

```
cd location_of_workspace/src
```0 Grasp_calculation_time_max: maximal time in
seconds until a grasp has to be returned. Set max time to 3 sec:

```
cd location_of_workspace/src
```1 Show_only_best_grasp: defines if only the best
grasp should be published or each grasp with an evaluation exceeding a
threshold (only top grasps per roll angle). Set this value to publish
only the overall top-rated grasp:

```
cd location_of_workspace/src
```2 Gripper opening width: this factor f is used
to simulate a gripper that is opened 1/f-times the maximal gripper
opening width (e.g.: value 3 =\> gripper only one third opened):

```
cd location_of_workspace/src
```3 These values can also be set before launching
the haf_client in the launch file launch/haf_grasping_all.launch. Here
are the default values:

```
cd location_of_workspace/src
```4

### HAF-GRASPING CLIENT - CODE EXPLAINED

In calc_grasppoints_action_client.cpp we subscribe to a point_cloud
topic and start the following callback when a point cloud comes in:

```
cd location_of_workspace/src
```5

### RESULT

Detected grasps are visualized in rviz and returned as result to the
service client. Furthermore, they are published to the topic
/haf_grasping/grasp_hypothesis_with_eval as string value and have the
following format:

```
cd location_of_workspace/src
```6 \'\'\'val\'\'\': scaled evaluation of the
grasp: 99 is the top value, -20 is the worst possible value, meaning
that no grasp was found at all (normally indicating a data or software
issue, e.g. an issue with the tf system or no \'\'\'make\'\'\' executed
in the libsvm folder)

\'\'\'gp1(x,y,z)\'\'\': x-,y-,z-coordinates of the first grasp point

\'\'\'gp2(x,y,z)\'\'\': x-,y-,z-coordinates of the second grasp point

\'\'\'av(x,y,z)\'\'\' : x-,y-,z-coordinates of the approach vector

\'\'\'gcp(x,y,z)\'\'\': x-,y-,z-coordinates of the grasp center point,
i.e. the middle point between gp1 and gp2

\'\'\'roll\'\'\': gripper orientation in degrees

The returned grasps indicate (in a redundant way) how a gripper with two
opposite fingers should approach an object: the gripper-specific
approach vector that goes through the tool center point should approach
the object along the object specific (returned) approach vector
(\'\'\'av\'\'\'), which goes to the grasp center point (\'\'\'gcp\'\'\')
whereby the roll is defined by \'\'\'roll\'\'\' respectively by the
heuristically estimated grasp points (\'\'\'gp1\'\'\',\'\'\'gp2\'\'\').

## GRASP REALIZATION WITH SIMULATION

A crucial part for successful grasping is path planning and grasp (fine)
planning. We achieved the best results by using a simulation software
(OpenRAVE) to calculate a collision free straight approach trajectory
for a gripper with fixed orientation in the following way.

The OpenRAVE simulator is used for path planning including determination
of an appropriate distance between the manipulator and the object before
closing the manipulator. OpenRAVE tries to approach the object mesh
(i.e. an unsegmented mesh of all objects in the scene \[rosnode with
conversion from point cloud to mesh can be provided\]) using the
calculated approach vector and manipulator roll angle until a collision
occurs. Then it sets the manipulator position back by a standoff value
which is dependent on the object position: in recent work, we do not use
a fixed standoff of 1 cm, but start with a standoff value of 1 mm. If
this standoff leads to a collision of the gripper fingers with the table
top or the ground (used in simulation), the standoff is increased until
the closing fingers do not collide with the table or the ground any
more. Then the actual grasp points, i.e. contact points of the fingers
with the object mesh in the simulation, are calculated. From the
resulting gripper position, OpenRAVE calculates the manipulator position
about 7 cm away and searches for a collision free path to place the
manipulator there. For the last 7 cm to the object OpenRAVE calculates a
straight path to the object if one exists. We chose 7 cm as a practical
trade-off between a higher grasping robustness (regarding calibration
inaccuracy or incomplete data) achieved by a straight approach
trajectory with fixed manipulator orientation and the challenge to find
inverse kinematics solutions for such trajectories.

An OpenRAVE implementation for the PR2 can be found here:
<http://pr.cs.cornell.edu/grasping/rect_data/data.php>
([\'\'\'code\'\'\'](http://pr.cs.cornell.edu/grasping/code/grasp_demo_unknownobjects.zip),
[\'\'\'Readme\'\'\'](http://pr.cs.cornell.edu/grasping/code/DescriptionPR2GraspingDemo.txt)).
OpenRAVE implementations for an 7-DOF Schunk/AMTEC arm, a Kuka LWR and
the service robot [\'\'\'Hobbit\'\'\'](http://hobbit.acin.tuwien.ac.at/)
can be provided on request.

## LIBSVM

Grasp points and approach vectors are detected using Support Vector
Machines. We have included LIBSVM to work as our classifier (go to
folder libsvm-3.12 and type \"make\" after checking out):

Chih-Chung Chang and Chih-Jen Lin, LIBSVM : a library for support vector
machines. ACM Transactions on Intelligent Systems and Technology,
2:27:1\--27:27, 2011. Software available at
<http://www.csie.ntu.edu.tw/~cjlin/libsvm>

## CITATION

If you like this package and use it in your own work, please cite our
[\'\'\'IJRR paper\'\'\'](https://www.researchgate.net/publication/277926854_Learning_grasps_with_topographic_features):

```
cd location_of_workspace/src
```7

## REPORT A BUG

\<\<GitHubIssues(davidfischinger/haf_grasping)\>\> or contact the
package maintainer directly.
