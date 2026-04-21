## Example scenarios

Some example scenarios can be run using: 

```
roslaunch riskrrt scenario_name.launch
```


Available scenarios:

-   corridor
-   D_corridor
-   airport
-   empty_airport
-   back_forth
-   crossing
-   frontal
-   inria_hall
-   test

## Nodes



```clearsilver
node.0 {
  name=controller
  desc=a path following node for differential drive robots
  sub{
    0.name= traj
    0.type= riskrrt/Trajectory
    0.desc= robot trajectory
    1.name= amcl_pose
    1.type= geometry_msgs/PoseWithCovarianceStamped
    1.desc= robot pose
  }
  pub{
    0.name= controller_feedback
    0.type= std_msgs/Bool
    0.desc= controller feedback, true as long as robot is on trajectory
    1.name= cmd_vel
    1.type= geometry_msgs/Twist
    1.desc= velocity commands
  }
}
node.1 {
  name=goal_pub
  desc=an automatic goal publisher
  pub{
    0.name= goal
    0.type= geometry_msgs/PoseStamped
    0.desc= robot final goal
  }
}
node.2 {
  name=og_builder*
  desc=some occupancy grid array publishers examples
  sub{
    0.name= map
    0.type= nav_msgs/OccupancyGrid
    0.desc= static map
    1.name= robot_*/base_pose_ground_truth
    1.type= nav_msgs/Odometry
    1.desc= mobile obstacles poses
  }
  pub{
    0.name= robot_*/cmd_vel
    0.type= geometry_msgs/Twist
    0.desc= mobile obstacles velocities
    1.name= ogarray
    1.type= riskrrt/OccupancyGridArray
    1.desc= occupancy grid array
  }
}
node.3 {
  name=planner
  desc=the riskrrt planner
  sub{
    0.name= ogarray
    0.type= riskrrt/OccupancyGridArray
    0.desc= occupancy grid array
    1.name= goal
    1.type= geometry_msgs/PoseStamped
    1.desc= robot final goal
    2.name= controller_feedback
    2.type= std_msgs/Bool
    2.desc= controller feedback
    3.name= amcl_pose
    3.type= geometry_msgs/PoseWithCovarianceStamped
    3.desc= robot pose
    4.name= odom
    4.type= nav_msgs/Odometry
    4.desc= robot odometry
  }
  pub{
    0.name= traj
    0.type= riskrrt/Trajectory
    0.desc= robot trajectory
  }
}
```



## Parameters



```clearsilver
param {
  no_header=True
  0.name= ~timeStep
  0.type= double
  0.desc= time step between each node (s), should be used as the time gap between each grid if using a custom OccupancyGridArray publisher
  1.name= ~maxDepth
  1.type= int
  1.desc= maximum depth a node can have, should be used to set the occupancy grid array size if using a custom OccupancyGridArray publisher
  2.name= ~nv
  2.type= int
  2.desc= discretization of the robot's linear speed, used to create the set of possible controls from a node
  3.name= ~nphi
  3.type= int
  3.desc= discretization of the robot's angular speed, used to create the set of possible controls from a node
  4.name= ~threshold
  4.type= double
  4.desc= maximum risk value a node can have to be considered free
  5.name= ~socialWeight
  5.type= double
  5.desc= weight of the risk component in the computation of the node's score
  6.name= ~rotationWeight
  6.type= double
  6.desc= weight of the node's orientation toward the goal (compared to the distance)
  7.name= ~growTime
  7.type= double
  7.desc= time allocated to the tree growth between map updates (s)
  8.name= ~bias
  8.type= double
  8.desc= percentage of the time the final goal is chosen as random goal
  9.name= ~windowSize
  9.type= double
  9.desc= size of the window from which to pick a random goal (m)
  10.name= ~goalTh
  10.type= double
  10.desc= maximum distance the robot can be from the final goal to consider the goal reached (m)
  11.name= ~robotLength
  11.type= double
  11.desc= robot lenght (m)
  12.name= ~robotWidth
  12.type= double
  12.desc= robot width (m)
  13.name= ~vMin
  13.type= double
  13.desc= minimum robot linear speed (m/s), set it to 0 or a negative value to allow reverse
  14.name= ~vMax
  14.type= double
  14.desc= maximum robot linear speed (m/s)
  15.name= ~accMax
  15.type= double
  15.desc= maximum linear acceleration (m/s²)
  16.name= ~omegaMax
  16.type= double
  16.desc= maximum angular speed (rad/s)
  17.name= ~accOmegaMax
  17.type= double
  17.desc= maximum angular acceleration (rad/s²)
}
```


