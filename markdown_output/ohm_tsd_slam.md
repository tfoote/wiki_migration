Welcome to the ohm_tsd_slam ROS wiki page. Ohm_tsd_slam is the SLAM
approach of the RoboCup Rescue [Team Autonohm](http://www.autonohm.de)
from the Technische Hochschule Nuremberg, Germany.

The release includes a SLAM package using 2D LIDAR data only as input.
Its localization module uses ICP-based registration. The mapping uses a
grid map, which cells contain Truncated Signed Distances (tsd), similar
to the well known KinectFusion approach. This representation performs
dynamic mapping, wherefore temporary objects are removed over time.

Simultaneously we are currently working on the release of two important
features of our SLAM.

`1.` RANSAC-aided registration This is more robust also it is slower
than the ICP registration. This feature can already be tested by
changing the parameter "registration_mode". You need to use lower ICP
distance filter values for this! `2.` Multi-robot SLAM Multiple robots
build one map simultaneously. This approach has the benefit that no map
merging is necessary after the mission. This strategy has been deployed
by Team Autonohm at the RoboCup German Open 2015.

The repository comes with an example launchfile, slam.launch. Its
parameters are set to fit the typical RoboCup rescue scenario deploying
a Hokuyo UTM30LX LIDAR or a sensor with similar parameters.

This video shows a demo of the package. It uses public available
recorded Lidar data, acquired from the University of Freiburg
(<http://kaspar.informatik.uni-freiburg.de/~slamEvaluation/datasets.php>).

[Youtube](https://www.youtube.com/watch?v=SfPSwSemBes)

The ohm_tsd_slam package is based on our CPU version of the well known
KinectFusion approach, and is available at
[ Researchgate](http://www.researchgate.net/publication/267694565_A_Generalized_2D_and_3D_Multi-Sensor_Data_Integration_Approach_based_on_Signed_Distance_Functions_for_Multi-Modal_Robotic_Mapping ).
```
S. May, P. Koch, R. Koch, C. Merkl, C. Pfitzner and A. Nuechter.
A Generalized 2D and 3D Multi-Sensor Data Integration Approach based on Signed Distance Functions for Multi-Modal Robotic Mapping.
In Proceedings of the VMV 2014: Vision, Modeling & Visualization, Darmstadt, Germany, 2014.
```

The multi-robot SLAM has been subject of a paper itself and can be
downloaded at
[ IEEEexplore](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=7101614&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D7101614 ).
```
P. Koch, S. May, M. Schmidpeter, M. Kühn, J. Martin, C. Pfitzner, C. Merkl, M. Fees, R. Koch and A. Nüchter.
Multi-Robot Localization and Mapping based on Signed Distance Functions.
In Proceedings of the IEEE International Conference on Autonomous Robot Systems and Competitions (ICARSC '15), Vila Real, Portugal, April 2015.
```

This video shows an experiment performed for the mentioned publication.
Both robots of our rescue robot team perform cooperating SLAM of a
building floor:

[Youtube](https://www.youtube.com/watch?v=U2pqgvMpsZM)

## Basic Installation

The algorithms used for ohm_tsd_slam are distributed with the obviously
library. After checking out the catkin package you can use wstools and
rosdep to install obviously within in the SLAM.

If you like to install obviously externally it is recommended to use the
master branch and follow the installation instructions provided in the
GitHub repository of
[obviously library](https://github.com/autonohm/obviously).

The basic installation to use obviously only for the ohm_tsd_slam is
explained here:

Clone the catkin package in your desired catkin workspace with.

```
$ #In your catkin workspace
$ cd src
$ git clone https://github.com/autonohm/ohm_tsd_slam
$ cd ohm_tsd_slam
$ git checkout indigo-devel
$ cd ../..
```

Clone the obviously library. It contains the algorithms used by the SLAM

```
$ wstool update -t src/ohm_tsd_slam
```

If you never used rosdep, run these two commands first. Otherwise you
can skip them.

```
$ sudo rosdep init
$ rosdep update
```

Source your workspace and run rosdep to install the necessary system
dependencies. You maybe need sudo to install necessary dependencies.

```
$ source devel/setup.bash #for example
$ rosdep install ohm_tsd_slam
```

Now, building the package should be no problem. Just run catkin_make.
For example:

```
$ catkin_make --only-pkg-with-deps ohm_tsd_slam
```

Finally, you can use the slam.launch launchfile to run the SLAM. If you
play a bagfile that publishes sensor_msgs::LaserScan on the "/scan"
topic you will receive a map on topic "/map" and the robot's pose on
"/pose"

```
$ roslaunch ohm_tsd_slam slam.launch
```

## ROS Nodes

```clearsilver
node.0 {
 name = slam_node
 desc = SLAM node for single robot SLAM and multi robot SLAM.
 pub {
  0.name= map
  0.type= nav_msgs/OccupancyGrid
  0.desc= Map of the environment
  1.name= pose
  1.type= geometry_msgs/PoseStamped
  1.desc= Absolute robot pose in the map frame.
 }
 param {
 0.name= map_size
 0.type= integer
 0.desc= Quadratic size of the map with a side length of 2^map_size^ * cell_size. E. g. map_size = 10, cell_size = 0.01 m -> side length = 2^10^ * 0.01 m = 10.24 m
 0.default= 10
 4.name= cell_size
 4.type= double
 4.desc= Size of a cell in meters. It influences the absolute map size
 4.default= 0.025
 1.name= x_offset
 1.type= double
 1.desc= Origin offset on the X-axis from lower left corner of the map. In meters.
 1.default= 0.5
 2.name= y_offset
 2.type= double
 2.desc= Origin offset on the Y-axis from lower left corner of the map. In meters.
 2.default= 0.5
 3.name= yaw_offset
 3.type= double
 3.desc= Orientation offset of the origin to the place the SLAM was initialized (rotation around vertical Z-axis)
 3.default= 0.0
 5.name= min_range
 5.type= double
 5.desc= Minimal range of the raycaster in meters. Set this to the attributes of the used laser scanner.
 5.default= 0.001
 6.name= max_range
 6.type= double
 6.desc= Maximal range of the raycaster in meters. Set this to the attributes of the used laser scanner.
 6.default= 30.0
 7.name= low_reflectivity_range
 7.type= double
 7.desc= Something which helps against glass reflections.. To be done
 7.default= 2.0
 8.name= occ_grid_time_interval
 8.type= double
 8.desc= The time [s] that needs to pass before an update of the map is published again
 8.default= 2.0
 9.name= loop_rate
 9.type= double
 9.desc= Node frequency of the SLAM in Hz. This has no influence on the map or pose frequency.
 9.default= 40.0
 10.name= pose_topic
 10.type= string
 10.desc= Topic for pose updates
 10.default= pose
 11.name= tf_base_frame
 11.type= string
 11.desc= Map coordinate system
 11.default= /map
 12.name= tf_child_frame
 12.type= string
 12.desc= Robot or Laser coordinate system
 12.default= /laser
 13.name= truncation_radius
 13.type= double
 13.desc= Number of cells used for the truncated signed distance function. Simply interpretable as the thickness of the walls, just more complex. Please, see xyz for further details.
 13.default= 3.0
 14.name= map_topic
 14.type= string
 14.desc= Topic for map publisher
 15.name= get_map_topic
 15.type= string
 15.desc= Advertise a service that returns a map as nav_msgs/OccupancyGrid with this name.
 16.name= footprint_width
 16.type= double
 16.desc= Width of the robot (y-axis). This space is cleared when the map is initialized.
 16.default= 0.5
 17.name= footprint_height
 17.type=double
 17.desc= Height of the robot (x-axis). This space is cleared when the map is initialized.
 17.default= 0.5
 18.name= footprint_x_offset
 18.type= double
 18.desc= The described rectangle is described around the laser scanner. Move it correctly that it fits to the robot's size.
 18.default= 0.28
 19.name= registration_mode
 19.type= int
 19.desc= Desired registration algorithm. 0 = ICP Registration with distance filter. 1 = Experimental mode with RANSAC aided ICP. Option 1 is slower but more robust than ICP only registration.
19.default=0
20.name= dist_filter_max
20.type= double
20.desc= The maximum distance for point matches. This is a cascading distance filter with every iteration the maximum value is reduced until it reaches the minimum value dist_filter_min.
20.default= 2.0
21.name= dist_filter_min
21.type= double
21.desc= The minimum distance for point matches.
21.default= 0.1
22.name= icp_iterations
22.type= int
22.desc= Number of ICP iterations for scan matching
22.default= 25
23.name= reg_trs_max
23.type= double
23.desc= Maximum translation allowed between two matched scans
23.default= 0.25
24.name= reg_sin_rot_max
24.type= double
24.desc= Maximal allowed rotation between two matched scans
24.default= 0.17
26.name= node_control_topic
26.type= double
26.desc= Name of the node_control service to start stop and reset the SLAM
26.default= node_control
27.name= ransac_trials
27.type= int
27.desc= Number of RANSAC iterations. Needs to be high for a big number of outliers.
27.default= 50
28.name= ransac_eps_tresh
28.type= double
28.desc= Threshold for outlier rejection in meters
28.default= 0.15
29.name= ransac_ctrlset_size
29.type= int
29.desc= Number of points in the control set to rate a estimated transformation between to laser scans
29.default= 180
30.name= ransac_phi_max
30.type= double
30.desc= Maximum expected rotational offset between two laser scans in degrees
30.default= 45








 }
}
```
