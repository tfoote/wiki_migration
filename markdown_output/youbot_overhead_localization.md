## Nodes

```clearsilver
node.0 {
  name = path_planner
  desc = `path_planner` implements an actionlib server to plan paths for the robot base. The paths are planned by constructing a costmap with costmap2d and using the A* algorithm in navfn.  Once a path is planned, it will be followed until the goal is reached, or until a new goal is given.
  
  sub {
   
    0.name = /base_localizer/pose_2d
    0.type = youbot_overhead_localization/Pose2d
    0.desc = The (x, y) position and heading of a robot base determined by the 'base_localizer' node
    
    1.name = /map
    1.type = nav_msgs/OccupancyGrid
    1.desc = A costmap used for path planning created by the 'planner_map_server' node based on information from overhead cameras
      
  }
  
  pub {
    0.name = /cmd_vel
    0.type = geometry_msgs/Twist
    0.desc = The linear and angular velocities of the robot base
        
    1.name = /base_localizer/cost
    1.type = actionlib_msgs/CostmapCost
    1.desc = The cost of the current point that the robot occupies, determined from the path planning costmap
  }

  srv {
    0.name = /path_planner/get_cost
    0.type = youbot_overhead_localization/GetCost
    0.desc = Returns the costmap cost at a specified point on the costmap
  }
  
  param{
    0.name = /path_planner/runFromSimulation
    0.type = `boolean`
    0.desc = Determines whether the robot is operating in a simulated or real environment  
  } 
}


node.1 {
  name = base_localizer
  desc = `base_localizer` localizes the robot base using odometry and the overhead camera information acquired from the 'youbot_overhead_vision' package.
  
  sub {
    0.name = /image_calibration/position_from_camera
    0.type = youbot_overhead_vision/PositionFromCamera
    0.desc = The robot location and heading according to the overhead camera image
  
    1.name = /odom
    1.type = nav_msgs/Odometry
    1.desc = The robot base odometry
    }
   
  pub {   
    0.name = /base_localizer/pose_2d
    0.type = youbot_overhead_localization/Pose2d
    0.desc = The (x, y) position and heading of the robot base
    }
}

node.2 {
  name = planner_map_server
  desc = `planner_map_server` is a modification of the map_server node written by Brian Gerkey from the ROS navigation stack to work with dynamic overhead maps.
  
  sub {
    0.name = /image_calibration/image_cal
    0.type = sensor_msgs/Image
    0.desc = The black and white occupancy grid image created by the 'image_calibration' node in the 'youbot_overhead_vision' package
    }
   
  pub {   
    0.name = /map
    0.type = nav_msgs/OccupancyGrid
    0.desc = The costmap from the overhead camera image used for path planning
    
    1.name = /map_metadata
    1.type = nav_msgs/MapMetaData
    1.desc = Contains the map metadata
    }
    
  param{
    0.name = /planner_map_server/map_file_yaml
    0.type = 'string'
    0.desc = Location of the map metadata
    
    1.name = /planner_map_server/map_save_debug_location
    1.type = 'string'
    1.desc = Location to save the map debug file
  }
  
  srv {
    0.name = /static_map
    0.type = nav_msgs/GetMap
    0.desc = This service returns a deep copy of the map
  }
}

node.3 {
  name = key_nav_safety
  desc = `key_nav_safety` bounds the speed of the robot when it is close to obstacles to ensure the robot does not get damaged.
  
  sub {
    0.name = /base_localizer/cost
    0.type = youbot_overhead_localization/CostmapCost
    0.desc = The costmap cost at the robot base's current location

    1.name = /base_localizer/pose_2d
    1.type = youbot_overhead_localization/Pose2d
    1.desc = The pose of the robot base including (x, y) position and heading
    
    2.name = /key_nav_safety/vel
    2.type = geometry_msgs/Twist
    2.desc = The requested linear and angular velocity for the robot base, pending safety checks
    }
   
  pub {   
    0.name = /cmd_vel
    0.type = geometry_msgs/Twist
    0.desc = Controls the robot's linear and angular velocity
  }

  param {
    0.name = /path_planner/moveCommandTopic
    0.type = `string`
    0.desc =Contains the name of the topic through which move commands should be sent to the robot to control it.  If the param is not set, '/cmd_vel' is assumed.
  }
}

node.4 {
  name = path_planner_client
  desc = `path_planner_client` Allows for the testing of path planning by creating an updateGoal service which can circumvent the need for creating an actionlib client
  
  srv {
    0.name = /update_goal
    0.type = youbot_overhead_localization/SetGoal
    0.desc = the goal for the robot to plan a path to comprising of an (x, y) coordinate and the name of the camera feed topic that the point is located on
  }
}
```

## Startup

The `youbot_overhead_localization` package should be launched at the
same time as the 'youbot_overhead_vision' package with the use of the
'path_planner.launch' or the 'path_planner_sim.launch" launch files
depending on whether the camera streams are real or simulated. However,
the node can be run on its own by using one of the following commands:

```shell
rosmake youbot_overhead_localization
roslaunch youbot_overhead_localization youbot_overhead_localization.launch
```

or

```shell
rosmake youbot_overhead_localization
roslaunch youbot_overhead_localization youbot_overhead_localization_sim.launch
```

The path planning itself normally requires a node to create an actionlib
client to set path goals, but this can be avoided for testing purposes
by launching the 'path_planner_client' node with the following
command:

```shell
rosrun youbot_overhead_localization path_planner_client
```

This will create the /update_goal service, which can be called to set
goals for the path planner.
