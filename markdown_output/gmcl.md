

```wiki
'''Citation Note'''

If you are using this package in your research work, please cite our article, more info[[https://wiki.ros.org/gmcl#Acknowledgements_.26_Citation|here]].
```



## Installation

Before installing gmcl package, please install ROS navigation stack in
your ROS workspace. You can do that with the following command:


```
$ sudo apt-get install ros-$ROS_DISTRO-navigation
```

 Then download gmcl package and place it inside
the /src folder of your catkin workspace and compile it, which can be
done through following commands: 

```
$ cd catkin_ws
$ git clone -b master https://github.com/adler-1994/gmcl src/gmcl
$ catkin_make
```



Following video shows gmcl in comparison to amcl while running on the
famous turtlebot 3 inside Gazebo simulation in solving the 3
localization problems (Pose Tracking, Global Localization,
Kidnapped-robot): [Youtube](https://www.youtube.com/watch?v=J9ZcCon6k-g)

## Algorithms

Algorithms could be divided into new and migrated from amcl:

### Migrated From amcl

Many of the algorithms and their parameters are well-described in the
book Probabilistic Robotics, by Thrun, Burgard, and Fox. The user is
advised to check there for more detail. In particular, we use the
following algorithms from that book:
**`sample_motion_model_odometry`**, **`beam_range_finder_model`**,
**`likelihood_field_range_finder_model`**, **`Augmented_MCL`**, and
**`KLD_Sampling_MCL`**.

### New Algorithms

Besides algorithms implemented in amcl, gmcl takes advantage of
**`Optimal particle filter`** as described
[here](https://ieeexplore.ieee.org/document/4543250) and **`
Intelligent particle filter`** as described
[here](https://ieeexplore.ieee.org/document/7031437) and
**`Self-adaptive particle filter`** as described
[here](https://ieeexplore.ieee.org/document/5262621) to improve the
performance of amcl while working in real time.

Modifications done on new algorithms to integrate them with amcl, Pseudo
code of amcl & gmcl algorithms, performance and complexity analysis of
amcl & gmcl are well-described in article
[here](https://www.researchgate.net/publication/359482651_Development_of_a_New_Technique_in_ROS_for_Mobile_Robots_Localization_in_Known-Based_2D_Environments).

## Package Requirements

In order to localize a mobile robot inside a map using gmcl package,
following must be represented:

### Complete TF Tree

The robot state publisher node -- more info
[here](http://wiki.ros.org/robot_state_publisher)-- must be running with
`robot_description` param of the robot's urdf and publishes the tf of
robots links (base link and lasers links). In addition, a motion
controller should publish the estimated robot motion as a transform
between the odometry frame (`odom_frame_id`) and the base frame
(`base_frame_id`).

### Occupancy Grid Map

A map server node --more info [here](http://wiki.ros.org/map_server)--
must publish a valid map using correct YAML format.

### Laser Scans

Robot must be equipped with at least one laser scanner. All lasers must
be fixed in place with respect to the robot base because `gmcl` looks
up the transform between the laser's frame (`laser_frame_id`) and the
base frame (`base_frame_id`), and latches it forever. So `gmcl`
"cannot" handle a laser that moves with respect to the base. All lasers
should publish their scans as
([ sensor_msgs/msg/LaserScan Message](https://docs.ros.org/en/rolling/p/ sensor_msgs/msg/LaserScan Message.html))
massege.

## Examples

Example of launch file that runs gmcl node and its parameters on
Differential drive mobile robot 

```
../gmcl/examples/gmcl_diff.launch
```

 To run gmcl
node with initial estimated pose e.g. at (x, y, yaw) := (-1, 2, 0.6)


```
$ rosrun gmcl gmcl_diff.launch initial_pose_x:=-1 initial_pose_y:=2 initial_pose_a:=0.6
```



Example of launch file that runs gmcl node and its parameters on
Holonomic wheeled mobile robot 

```
../gmcl/examples/gmcl_omni.launch
```

 To run gmcl node
with initial estimated pose e.g. at (x, y, yaw) := (-1, 2, 0.6)


```
$ rosrun gmcl gmcl_omni.launch initial_pose_x:=-1 initial_pose_y:=2 initial_pose_a:=0.6
```



## gmcl Node

Just like [amcl](https://index.ros.org/p/amcl), `gmcl` takes in a
laser-based map, laser scans, and transform messages, and outputs pose
estimates. On startup, `gmcl` initializes its particle filter
according to the parameters provided. Note that, because of the
defaults, if no parameters are set, the initial filter state will be a
moderately sized particle cloud centered about (0,0,0). The drawing
below shows localization using `gmcl`. During operation `gmcl`
estimates the transformation of the base frame (`base_frame_id`) in
respect to the map frame (`global_frame_id`) but it only publishes the
transform between map frame and the odometry frame (`odom_frame_id`).
Essentially, this transform accounts for the drift that occurs using
Dead Reckoning. ![width="750px"](doc/gmcl_localization.png)

### Subscribed Topics



```clearsilver
  sub{
no_header=True
    0.name= scan
    0.type= sensor_msgs/LaserScan
    0.desc= Laser scans.
}
```

 

```clearsilver
 sub{
no_header=True

    1.name= tf
    1.type= tf/tfMessage
    1.desc= Transforms.
}
```




```clearsilver
 sub{
no_header=True
    2.name= initialpose
    2.type= geometry_msgs/PoseWithCovarianceStamped
    2.desc= Mean and covariance with which to (re-)initialize the particle filter.
}
```

 

```clearsilver
 sub{
no_header=True
    3.name= map
    3.type= nav_msgs/OccupancyGrid
    3.desc= When the `~use_map_topic` parameter is set, gmcl subscribes to this topic to retrieve the map used for laser-based localization.
  }
```



### Published Topics



```clearsilver
  pub{
    no_header=True
    0.name= gmcl_pose
    0.type= geometry_msgs/PoseWithCovarianceStamped
    0.desc= Robot's estimated pose in the map, with covariance.
}
```

 

```clearsilver
  pub{
    no_header=True
    1.name= gmcl_particlecloud
    1.type= geometry_msgs/PoseArray
    1.desc= The set of pose estimates being maintained by the filter.
}
```




```clearsilver
  pub{
    no_header=True
    2.name= gmcl_SER
    2.type= geometry_msgs/PoseArray
    2.desc=The set of poses that shape Similar Energy Region (`SER`).
}
```

 

```clearsilver
  pub{
    no_header=True
    3.name= tf
    3.type= tf/tfMessage
    3.desc= Publishes the transform from `odom` (which can be remapped via the `~odom_frame_id` parameter) to `map`.
  }
```



### Services



```clearsilver
  srv{
    no_header=True
    0.name=global_localization 
    0.type= std_srvs/Empty
    0.desc= Initiate global localization, wherein all particles are dispersed randomly through the free space in the map if `~use_self_adaptive` is set to false, otherwise particles will be dispersed randomly in `SER`.

}
```

 

```clearsilver
  srv{
    no_header=True
    1.name=request_nomotion_update 
    1.type= std_srvs/Empty
    1.desc= Service to manually perform update and publish updated particles.
}
```




```clearsilver
  srv{
    no_header=True
    2.name=set_map 
    2.type= nav_msgs/SetMap
    2.desc= Service to manually set a new map and pose.
}
```



### Services Called



```clearsilver
  srv_called{
    no_header=True
    0.name=static_map 
    0.type= nav_msgs/GetMap
    0.desc= gmcl calls this service to retrieve the map that is used for laser-based localization; startup blocks on getting the map from this service.
  }
```



### Parameters

Besides Parameters that amcl uses to configure its node --Please check
[them](https://wiki.ros.org/amcl#Parameters)-- , gmcl adds eleven
Parameters to overall filter parameters to configure the `gmcl` node
and they are:



```clearsilver
param {
  no_header=True
  0.name= ~use_optimal_filter
  0.default=false (`disabled`)
  0.type= bool
  0.desc= When set to true, gmcl will compute new pose and weight of particles through auxiliary particles of the optimal filter, otherwise it will compute pose and weight through `standard-MCL` approach.
}
```

 

```clearsilver
param {
  no_header=True
  1.name= ~use_intelligent_filter
  1.default=false (`disabled`)
  1.type= bool
  1.desc=When set to true, gmcl will crossover and mutate the pose of one third of small weight particles through crossover and mutation models.
}
```




```clearsilver
param {
  no_header=True 
  2.name= ~use_self_adaptive
  2.default=false (`disabled`)
  2.type= bool
  2.desc= When set to true, gmcl will spread global particles randomly in `SER`, otherwise it will spread global particles randomly in free space of the map.
}
```

 

```clearsilver
param {
  no_header=True
  3.name= ~use_kld_sampling
  3.default=true
  3.type= bool
  3.desc=When set to true, gmcl will adapt the number of its particles, Otherwise it will fix the number of particles to parameter `~max_particles`. 
}
```

 Previous parameters
define the Flow of gmcl algorithm and can be seen in following
drawing..... ![width="750px"](doc/flow_chart.png) Full size available
[here](https://wiki.ros.org/gmcl?action=AttachFile&do=get&target=flow_chart.png).

The following table shows name of different techniques based on filters
implemented, it could be seen that gmcl works with default parameters
same as amcl..... ![width="750px"](doc/table.png)



```clearsilver
param {
  no_header=True
  4.name= ~N_aux_particles
  4.default=10
  4.type= int
  4.desc=Defines the number of auxiliary particles. Used in Optimal particle filter.  
}
```



##### 



```wiki
'''Real Time Caution'''

Be careful when setting the number of auxiliary particles, since they increase linearly the time required to calculate the new pose and weight of filter’s particles…..more details in [[https://www.researchgate.net/publication/353196299_gmcl_As_a_Proposed_Replacement_to_amcl_in_ROS_for_Mobile_Robots_Localization_in_Known-Based_2D_Environments|article]].
```





```clearsilver
param {
  no_header=True
  5.name= ~crossover_alpha
  5.default=0.5
  5.type= double
  5.desc=Specifies the amount of effect that pose of large weight particle does to pose of small weight particle. Used in crossover model in Intelligent particle filter. 
}
```

 

```clearsilver
param {
  no_header=True
  6.name= ~mutation_probability
  6.default=0.1
  6.type= double
  6.desc=Specifies the occurrence probability of a mutation to pose of small weight particle. Used in mutation model in Intelligent particle filter.
}
```




```clearsilver
param {
  no_header=True
  7.name= ~energy_map_resolution_x
  7.default=0.2 meters
  7.type= double
  7.desc=X-axis resolution of energy map. Used in Self-Adaptive particle filter.
}
```

 

```clearsilver
param {
  no_header=True
  8.name= ~energy_map_resolution_y
  8.default= 0.2 meters
  8.type= double
  8.desc=Y-axis resolution of energy map. Used in Self-Adaptive particle filter.
}
```



##### 



```wiki
'''Carsh Warning'''

Don’t set either of energy_map_resoluation_x or -resoultion_y to zero or gmcl node won’t execute.
```

 

```clearsilver
param {
  no_header=True
  9.name= ~energy_threshold_value
  9.default=0.05
  9.type= double
  9.desc=Defines the upper limit in energy difference between energy map cells and sensor reading’s energy to shape `SER`. Used in Self-Adaptive particle filter. 
}
```




```clearsilver
param {
  no_header=True
  10.name= ~publish_ser
  10.default=false
  10.type= bool 
  10.desc=When set to true, gmcl will display `SER` in Rviz as a (<<MsgLink(geometry_msgs/PoseArray Message)>>) massege.
}
```



## Feedback

To report a bug, or suggest an enhancement, please create a Github issue
[here](https://github.com/adler-1994/gmcl/issues/new).

If you already have enhanced the code and want to add your changes to
the main code, please send a Github pull request through your forked
copy of gmcl repository for merging. If you are not familiar with pull
requests please visit
[page](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

If you have a question, please post it on
[ROS answers](http://answers.ros.org/questions/scope:all/sort:activity-desc/tags:gmcl/page:1/),
make sure your question is tagged by **gmcl** so I get notified.

## Acknowledgements & Citation

This package was written during my master's thesis at Tishreen
University, Syria. My thesis advisor is
Dr.[Iyad Hatem](http://iyadhatem.altervista.org/).
![attachment:iyad-mhd.png](doc/iyad-mhd.png)

This work has been published as an article
[here](https://www.researchgate.net/publication/359482651_Development_of_a_New_Technique_in_ROS_for_Mobile_Robots_Localization_in_Known-Based_2D_Environments).
To properly cite it, please use the following:



```
@article{article,
author = {Alshikh Khalil, Mhd Ali and Hatem, Iyad},
issue = {Vol. 43 No. 6 (2021)},
pages = {119-137},
title = {Development of a New Technique in ROS for Mobile Robots Localization in Known-Based 2D Environments},
journal = {Tishreen University Journal of Research and Scientific Studies - Engineering Sciences Series}}
```
