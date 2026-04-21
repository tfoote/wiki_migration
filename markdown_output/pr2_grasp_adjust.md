## Overview

![alt text\|width="500"](attachment:box_grasp.png)

This package provides an interface for a grasp adjustment algorithm that
finds suitable grasp poses near an input pose. This can be used to
confirm or refine a pre-existing candidate grasp, such as one given by
other grasp planners in the ROS grasp pipeline. Alternatively, the
algorithm can be used to find grasps near the current gripper pose as
the gripper moves around nearby objects.

## Video

[Youtube](https://www.youtube.com/watch?v=xY3cnMdjbow)

## ROS API

### API Stability

The ROS API is currently UNREVIEWED and UNSTABLE.

### ROS Parameters

The default configuration of this package relies on several parameters
being loaded onto the ROS [parameter server](Parameter Server).
Currently this is done when the node is launched from
grasp_adjust_server.launch. Users who wish to modify the default values
can edit this file.

Many users may wish to modify some of these values temporarily and
repeatedly during program run time. This can be done through the dynamic
reconfigure server.

Some parameters belong in the private namespace of the node, others
belong in a config/ or debug/ namespace below the private namespace, as
given for each parameter below.



```clearsilver
  param {

  1.name= load_debug_server
  1.default= False
  1.type= bool
  1.desc= Tells the node whether to create the dynamic reconfigure server for debug settings.

}
```





```clearsilver
  param {

  1.name= config/centroid_weight
  1.default= 10.0
  1.type= double
  1.desc= The cost for distance between the local cloud centroid and the center-front of the gripper palm.

  2.name= config/symmetry_weight
  2.default= 0.3
  2.type= double
  2.desc= The cost for asymmetry of the point cloud between the gripper finger tips.

  3.name= config/collision_weight
  3.default= 1.0
  3.type= double
  3.desc= The cost (per point) for collisions between the point cloud and the gripper model.

  4.name= config/normal_weight
  4.default= -0.3
  4.type= double
  4.desc= The cost (per point) for normals that are aligned with the gripper frame's principal axes. Note that this value should be negative to reward a good grasp (low cost).

  5.name= config/point_weight
  5.default= -0.01
  5.type= double
  5.desc= The weight for enclosing additional points in the space between the robot finger tips.

  6.name= config/point_bonus
  6.default= -1.0
  6.type= double
  6.desc= Should probably be deprecated.

  7.name= config/search_mode
  7.default= 0
  7.type= int
  7.desc= Sets the search mode. Full grid search = 0; local search = 1.

  8.name= config/search_6_dof
  8.default= True
  8.type= bool
  8.desc= Sets whether to use a full 6-dof gradient descent on the gripper pose, or to only vary position + yaw about the world vertical (base_footprint).

  9.name= config/grid_step_num
  9.default= 1
  9.type= int
  9.desc= The number of steps in either direction from the input pose to use to populate the search grid. For example, for grid_step_num = 1, the grid will be 3x3; for a value of 2, the grid will be 5x5.

  10.name= config/search_window
  10.default= 2
  10.type= int
  10.desc= On each gradient step, the number of steps to search in either direction before choosing the optimal step value.

  11.name= config/full_gradient_descents
  11.default= 5
  11.type= int
  11.desc= The number of seed grasps on which to perform a full gradient descent, until each one reaches a local minimum.

  12.name= config/init_gradient_steps
  12.default= 2
  12.type= int
  12.desc= For every initial seed pose, the number of gradient descent steps to take before choosing the best poses on which to do full gradient descents.


  12.name= config/linear_step_size
  12.default= 0.002 meters
  12.type= double
  12.desc= The size of each translation step.


  12.name= config/angular_step_size
  12.default= 0.1 radians
  12.type= double
  12.desc= The size of each angular step.

}
```





```clearsilver
  param {

  1.name= debug/run_continuous
  1.default= False
  1.type= bool
  1.desc= If this is set, the algorithm will run continuously. This is for debugging, as the return result is dsipalyed in rviz but otherwise discarded.

}
```


