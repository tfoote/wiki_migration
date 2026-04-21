## Nodes

### augmented_grasp_planner

This node wraps any other grasp planner service. It modifies the results
of the underlying grasp planner using human feedback. The interactive
version of rviz provided by
[interactive_rviz_helper](interactive_rviz_helper) provides the UI
necessary to collect this feedback.



```clearsilver
srv{
  0.name= augmented_database_grasp_planner 
  0.type= object_manipulation_msgs/GraspPlanning
  0.desc= Returns a list of grasps sorted with human feedback. Service name can be changed with planner_service_name parameter.
}
srv_called{
  0.name= database_grasp_planner
  0.type= object_manipulation_msgs/GraspPlanning
  0.desc= A service that provides a list of possible grasps. Service name can be changed with automated_planner_service_name parameter.
}

param {
  0.name= ~<name>/planner_service_name
  0.default= augmented_database_grasp_planning
  0.type= string
  0.desc= The advertised service name

  1.name= ~<name>/automated_planner_service_name
  1.default= database_grasp_planning
  1.type= string
  1.desc= The name of the grasp planning service to call

  2.name= ~<name>/grasp_distance_euclidean_weight
  2.default= 17.0
  2.type= float
  2.desc= The relative weight of euclidean to angular distance when computing the distance between grasp poses. This distance is used to sort grasps. The grasps closest to the one selected by human feedback will be attempted first. A value of 17.0 roughly equates a 10 degree difference with a 2 cm difference.
}
```


