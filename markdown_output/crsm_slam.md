[![free hit counters](http://c.statcounter.com/9520022/0/f58d02af/1/)](http://statcounter.com/)

# General description

CRSM SLAM stands for Critical Rays Scan Match SLAM (Simultaneous
Localization And Mapping). Its main characteristics follow:

-   Uses scan-to-map matching, instead for the usual scan-to-scan
    matching, aiming at noise accumulation reduction.
-   Scan matching is performed via a Random Restart Hill Climbing
    algorithm (RRHC).
-   Only the critical rays take part in the RRHC. As critical are
    denoted the rays which contain more spatial information than the
    others.
-   The map update is performed with dynamic intensity, depending on the
    current environmental structure.

The full algorithmic description can be found in the following paper:

<http://link.springer.com/article/10.1007/s10846-012-9811-5#>!

CRSM SLAM does \'\'\'not\'\'\' have a close loop behaviour, but it gives
very good results in featured spaces.

Finally, it was used in the [PANDORA](http://pandora.ee.auth.gr/)
autonomous vehicle that takes part in the world-wide robotic competition
RoboCup-RoboRescue.

# Installation

CRSM SLAM is provided through the official ROS repositories. To install
execute the following command :

```
sudo apt-get install ros-$ROS_DISTRO-crsm-slam
```

You can also manually set it up:

```
cd <your_catkin_ws>/src
git clone https://github.com/etsardou/crsm-slam-ros-pkg.git
cd ../
catkin_make
```

# Screenshots/Multimedia

The following environment was created in the Gazebo simulator :

![RoboCup-RoboRescue arena\|height=\"400\"](attachment:gaz.png)

One video that demonstrates CRSM SLAM in the above environment is the
following :

[Youtube](https://www.youtube.com/watch?v=BjhzxYh0dz8)

The final map produced by CRSM SLAM is the following :

![CRSM SLAM result\|height=\"400\"](attachment:result_slam.png)

# Package Input / Output

There is only one node spawn whose name is crsm_slam_node.

CRSM needs as input :

-   [sensor_msgs::LaserScan](http://docs.ros.org/api/sensor_msgs/html/msg/LaserScan.html)
    publisher that contains the Laser rays.

On the other hand, CRSM outputs :

-   [nav_msgs::OccupancyGrid](http://docs.ros.org/api/nav_msgs/html/msg/OccupancyGrid.html)
    publisher which contains the occupancy grid map.

```{=html}
<!-- -->
```
-   A [tf](http://wiki.ros.org/tf) transformation with the robot\'s
    pose.

```{=html}
<!-- -->
```
-   A
    [nav_msgs::Path](http://docs.ros.org/api/nav_msgs/html/msg/Path.html)
    that contains the robot trajectory.

# Parameters

CRSM is fully parameterizable by changing the parameter file
\"crsm_slam/config/crsm_slam/crsm_slam_parameters.yaml\". The meaning of
each parameter, as well as the expected effect on the algorithm follow:

-   \'\'\'occupancy_grid_publish_topic\'\'\'
-   Description : The occupancy grid publishing topic
-   Default : \`/crsm_slam/map\`

```{=html}
<!-- -->
```
-   \'\'\'robot_trajectory_publish_topic\'\'\'
-   Description : The trajectory publishing topic
-   Default : \`/crsm_slam/trajectory\`

```{=html}
<!-- -->
```
-   \'\'\'trajectory_publisher_frame_id\'\'\'
-   Description : The trajectory frame ID
-   Default : \`map\`

```{=html}
<!-- -->
```
-   \'\'\'laser_subscriber_topic\'\'\'
-   Description : The laser subscriber topic
-   Default : \`/crsm_slam/laser_scan\`

```{=html}
<!-- -->
```
-   \'\'\'world_frame\'\'\'
-   Description : Holds the world frame
-   Default : \`world\`

```{=html}
<!-- -->
```
-   \'\'\'base_footprint_frame\'\'\'
-   Description : Holds the base footprint frame - (x,y,yaw)
-   Default : \`base_footprint_link\`

```{=html}
<!-- -->
```
-   \'\'\'base_frame\'\'\'
-   Description : Holds the base frame
-   Default : \`base_link\`

```{=html}
<!-- -->
```
-   \'\'\'map_frame\'\'\'
-   Description : Holds the map frame
-   Default : \`map\`

```{=html}
<!-- -->
```
-   \'\'\'laser_frame\'\'\'
-   Description : Holds the laser frame
-   Default : \`laser_link\`

```{=html}
<!-- -->
```
-   \'\'\'hill_climbing_disparity\'\'\'
-   Description : Disparity of mutation in pixels at hill climbing
-   Default : 40
-   Effect : If the disparity is increased, hill climbing searches for
    solution in a wider area. If the robot has large velocities, one
    measure to take is to increase the specific parameter.

```{=html}
<!-- -->
```
-   \'\'\'slam_container_size\'\'\'
-   Description : Map size of initial allocated map
-   Default : 500
-   Effect : This variable controls the initial size of the container of
    occupancy grid map. If needed during the experiment, the map is
    resized.

```{=html}
<!-- -->
```
-   \'\'\'slam_occupancy_grid_dimentionality\'\'\'
-   Description : \[OC\]cupancy \[G\]rid \[D\]imentionality - the width
    and height in meters of a pixel
-   Default : 0.02
-   Effect : If the current variable increases, the algorithm will run
    faster but there will be a loss of quality.

```{=html}
<!-- -->
```
-   \'\'\'map_update_density\'\'\'
-   Description : Map update density (0-127)
-   Default : 30
-   Effect : If the current variable increases, the map probabilities
    will change with a higher rate toward the probability extremes (0
    for occupancy, 1 for free space).

```{=html}
<!-- -->
```
-   \'\'\'map_update_obstacle_density\'\'\'
-   Description : Coefficient for obstacle update density (0+)
-   Default : 3.0
-   Effect : In CRSM SLAM the obstacles probabilities update with a
    higher rate than the free space\'s ones. This aims at creating a
    better reference for the RRHC algorithm.

```{=html}
<!-- -->
```
-   \'\'\'scan_density_lower_boundary\'\'\'
-   Description : Scan density lower boundary for a scan-part
    identification
-   Default : 0.3
-   Effect : This variable holds the minimum distance two consecutive
    rays must have in order to be considered the extremes of two scan
    parts.

```{=html}
<!-- -->
```
-   \'\'\'max_hill_climbing_iterations\'\'\'
-   Description : Maximum RRHC iterations
-   Default : 40000
-   Effect : If more search power is needed, you can increase this
    variable.

```{=html}
<!-- -->
```
-   \'\'\'occupancy_grid_map_freq\'\'\'
-   Description : The occupancy grid map publishing frequency
-   Default : 1.0 Hz

```{=html}
<!-- -->
```
-   \'\'\'robot_pose_tf_freq\'\'\'
-   Description : The robot pose publishing frequency
-   Default : 5.0 Hz

```{=html}
<!-- -->
```
-   \'\'\'trajectory_freq\'\'\'
-   Description : The trajectory publishing frequency
-   Default : 1.0 Hz

```{=html}
<!-- -->
```
-   \'\'\'desired_number_of_picked_rays\'\'\'
-   Description : The desired number of picked rays \[algorithm
    specific\]
-   Default : 40
-   Effect : CRSM SLAM tries to keep the number of critical rays picked
    almost constant. If the specific variable increases, more rays in
    average will be picked.

```{=html}
<!-- -->
```
-   \'\'\'robot_width\'\'\'
-   Description : The robot width in meters
-   Default : 0.5

```{=html}
<!-- -->
```
-   \'\'\'robot_length\'\'\'
-   Description : The robot length in meters
-   Default : 0.5

# How to run CRSM SLAM

CRSM SLAM can be executed either with `rosrun` or by `roslaunch`.

The package includes two launchers, one for a simulated laser
(\`crsm_slam_simulation.launch\`) and one for a real one
(\`crsm_slam_real.launch\`), which \"listens\" to a \`hokuyo_node\`.
