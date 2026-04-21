## Overview (e-turtle)

A number of changes have been made to the planning_environment. Details
to follow, but much of the information on diamondback no longer holds.

## Overview (diamondback)

The planning_environment is a library/ROS node that allows users to
instantiate robot models and collision models based on data from the
parameter server with minimal user input. Additionally, state
information for both robot models and collision environments can be
monitored.

Planning_environment constructs a model of the robot through the URDF
and will update the current state of the robot using joint information.
Planning_environment will also listen to range sensor data, constructing
a collision space to be used for checking collision between the robot
and the environment. Other objects can be added to the collision space
as well.

The primary purpose of the planning environment is to allow for checking
whether states and trajectories are safe or unsafe due to violating
constraints, joint limits, or causing the robot to collide with itself
of the environment. The primary interface to the planning_environment is
through the environment_server which is a ROS node providing all the
topic and service functionality.

The ROS API for this node is explained in detail below.

## ROS API

### API stability

-   The ROS API is REVIEWED but UNSTABLE
-   The C++ API is UNREVIEWED and UNSTABLE

### Services offered



```clearsilver
srv {
  no_header = True
  group.1{
    name = Utility services
    desc = These are the services that planning environment offers for performing utility functions like figuring out all the joints in a group.
    0.name = get_joints_in_group
    0.type = planning_environment_msgs/GetJointsInGroup
    0.desc = This service gives access to the joints in a group as specified in the robot_description_planning/groups.  E.g., the group ''right_arm'' contains the joints:  ''r_shoulder_pan_joint r_shoulder_lift_joint r_upper_arm_roll_joint r_elbow_flex_joint r_forearm_roll_joint r_wrist_flex_joint r_wrist_roll_joint''
    1.name = get_robot_state
    1.type = planning_environment_msgs/GetRobotState
    1.desc = This service provides the complete state of the robot as a [[motion_planning_msgs/RobotState]] message. This message contains information about the joint positions of all the (real) joints on the robot. 
          }
  group.2{
    name = Monitoring configuration services
    desc = These are the services that allows for configuring the monitoring behavior in the planning environment. 
    0.name = set_constraints
    0.type = planning_environment_msgs/SetConstraints
    0.desc = This service allows configuration of goals and constraints for monitoring.  
          }
  group.3{
    name = Monitoring/Checking services
    desc = These are the services that the planning environment provides to checks plans, check whether goal states have been reached, and for monitoring trajectories.      
    0.name = get_environment_safety
    0.type = planning_environment_msgs/GetEnvironmentSafety
    0.desc = This service checks whether is the environment is safe for operation. This service could be used, for example, to warn if state messages have not been received from the robot recently or if sensor messages are outdated, making the environment unsafe for operation.  
    1.name = get_execution_safety
    1.type = planning_environment_msgs/GetExecutionSafety
    1.desc = This services provides checking of trajectories as provided by [[motion_planning_msgs/JointTrajectory]] are safe. 
    3.name = get_trajectory_validity
    3.type = planning_environment_msgs/GetJointTrajectoryValidity
    3.desc = Allows checking if the specified plan is valid, i.e. whether it satisfies the goal and path constraints AND is not in collision at any point along the path.
          }
     group.4{
       name = Collision space information
       desc = Services for getting information about the current state of the collision space.
       0.name = ~/get_objects_in_collision_map
       0.type = planning_environment_msgs/GetObjectsInCollisionMap
       0.desc = Returns a list of objects and attached objects currently in the collision space.
       1.name = ~/get_current_allowed_collision_matrix
       1.type = planning_environment_msgs/GetAllowedCollisionMatrix
       1.desc = Returns the current matrix of whether collision checks will be performed for different pairs of links, attached objects, and objects.
       2.name = ~/set_allowed_collisions
       2.type = planning_environment_msgs/SetAllowedCollisions
       2.desc = (FOR TESTING/DEBUGGING PURPOSES ONLY) Sets the default collision matrix until reverted.  Better practice is to use allowed collision operations in each call.
       3.name = ~/revert_allowed_collisions
       3.type = std_srvs/Empty
       3.desc = (FOR TESTING/DEBUGGING PURPOSES ONLY) Reverts the default collision matrix when set.  
  }
```



### Parameter configuration



```clearsilver
param {
  no_header = True
  0.name=~robot_description
  0.default=`"robot_description"`
  0.type= string
  0.desc= The name of the ROS parameter that contains the string representation of the URDF for the robot.
  1.name= ~allow_valid_collisions
  1.default= false
  1.type= bool
  1.desc= If true and allowable contact regions exist, collisions inside the allowed contact regions will be ignored.
  2.name= ~collision_map_safety_timeout
  2.default= 0.0
  2.type= double
  2.desc= If > 0.0 seconds, the node will expect the collision map to be published regularly within this interval of time.  If the node has not received a collision map within the interval it will declare all states and trajectories unsafe.  
  3.name= ~joint_states_safety_timeout
  3.default= 0.0 (seconds)
  3.type= double
  3.desc= If > 0.0 seconds, the node will expect the joint states to be published more frequently than this safety timeout.  If the node has not received joint states within the interval it will declare all states and trajectories unsafe.
  4.name = ~group
  4.default = ""
  4.type = string
  4.desc = Sets the group name of joints to monitor.  See [[planning_environment/YAML configuration|YAML configuration]] for more information on groups.
  5.name= ~global_frame
  5.default= ""
  5.type= string
  5.desc= If the global frame is specified to be the empty string, the root frame in which all monitoring will take place is the root link of the robot ("base_link" for the robot). Otherwise, this parameter can be set to a fixed frame in the world (e.g. "odom_combined", "map")
  6.name = ~tf_safety_timeout
  6.default = 0.0 (seconds)
  6.type = double
  6.desc = The expected interval between TF updates. If global_frame is set to a valid fixed frame (and not to its default of an empty string), THEN if the node has not received TF updates within this interval it will declare all states and trajectories unsafe.
  7.name= ~contacts_to_compute_for_display
  7.default= 1
  7.type= int
  7.desc= If no allowed collisions are set as part of a state or trajectory safety query, then this parameter sets the number of contacts that will be broadcast for display.  The minimum value is 1. 
  8.name = ~contacts_to_compute_for_allowable_contacts_test
  8.default = 10
  8.type = int
  8.desc = If allowable contacts are set as part of a state or trajectory safety query, this parameter specifies the number of contacts that will be checked for violating allowed contacts.  If all checked contacts occur within the allowable contact region, contact is not reported.  
  9.name= ~use_collision_map
  9.default= true
  9.type= bool
  9.desc= If true, collision map information is expected and used in the collision space.
  10.name = ~velocity_history_size
  10.default = 20
  10.type = int
  10.desc = The velocity history is used to determine whether or not the robot is moving.  If the sum of joint velocities is less than .001 when summed over the velocity history, and the environment server is monitoring a trajectory where the robot should be moving, it will declare the trajectory failed.
  11.name = <robot_description_name>_planning/groups
  11.default = <empty>
  11.type = XmlRpc::TypeArray
  11.desc = Contains an array of named sets of joints and links.  For more information see [[planning_environment/YAML configuration|YAML configuration]]. Note that <robot_description_name> will be replaced with either robot_description or whatever value has been remapped for robot_description.
  12.name = <robot_description_name>_collision/robot_padd
  12.default = .01
  12.type = double
  12.desc = The value for a padding to add around the collision bodies associated with all links in the collision space.  Note that <robot_description_name> will be replaced with either robot_description or whatever value has been remapped for robot_description.
  13.name = <robot_description_name>_collision/robot_scale
  13.default = 1.0
  13.type = double
  13.desc = The value for the scale for each collision associated with each link in the collision space.  Note that <robot_description_name> will be replaced with either robot_description or whatever value has been remapped for robot_description.  
  14.name = <robot_description_name>_collision/default_collision_operations
  14.default = <empty>
  14.type = XmlRpc::TypeArray
  14.desc = A list of collision operation for enabling and disabling self collision checks between robot links.  For more information see [[planning_environment/YAML configuration|YAML configuration]]. Note that <robot_description_name> will be replaced with either robot_description or whatever value has been remapped for robot_description
  15.name = ~object_padd
  15.default = 0.02
  15.type = double
  15.desc = The padding to use for the known objects when clearing the point cloud
  16.name = ~pointcloud_padd
  16.default = 0.02
  16.type = double
  16.desc = Additional padding to be used when collision checking against pointclouds (the padding around the robot links defined in <robot_description_name>_collision/robot_padd will still be used)
  17.name = ~joint_state_cache_allowed_difference
  17.default = 0.25
  17.type = double
  17.desc = Maximum allowed past/future time difference between a requested timestamp and the cached joint states. Requests outside the cache timestamp limits and within the time difference allowed by this parameter will return the closest cache limit (no extrapolation).
  18.name = ~bounding_planes
  18.default = 0 0 1 -0.01
  18.type = string
  18.desc = Collision environment bounding planes. It consists of a sequence of plane equations specified as "a1 b1 c1 d1 a2 b2 c2 d2 ..." where each plane is defined by the equation ax+by+cz+d=0
}
```



### ROS topics



```clearsilver
pub{
  0.name = environment_server_collision_markers
  0.type = visualization_msgs/Marker
  0.desc = if the show_collisions and compute_contacts parameters are set to true, visualization markers marking points of detected collision will be published.  The naming convention for the markers is that a marker will have a namespace indicating the first link or attached body that is in contact followed by a "+", and then the link, object, or attached body that is also in collision.  An arbitrary sequenced number will be passed as the id number.
  2.name = allowed_contact_regions_array
  2.type = visualization_msgs/MarkerArray
  2.desc = This is a visual representation of the allowed contacts regions. The allowed contacts regions are regions in space where certain links of the robot may be allowed to touch objects.
  }
}
```





```clearsilver
sub{
    0.name = collision_map
    0.type = mapping_msgs/CollisionMap
    0.desc = This is the topic on which the server listens for collision map information. If expected duration for this topic is set greater than 0.0 (see ROS params above), the node will wait for this topic to be published.
    1.name = collision_map_update
    1.type = mapping_msgs/CollisionMap
    1.desc = This is the topic on which the server listens for incremental collision map information. Incremental information could be published, e.g., by using single laser scans. 
    
}
```



## Tutorials

Tutorials for this package are available in the
[ motion_planning_environment stack tutorials](motion_planning_environment/Tutorials).
