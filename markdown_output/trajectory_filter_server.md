## Tutorials

The tutorials for this package are in the
[trajectory_filters stack tutorials](trajectory_filters/Tutorials)

## ROS API

### API Stability

-   The ROS API is REVIEWED but UNSTABLE

### ROS Parameters

```clearsilver
param {
  1.name= ~service_type
  1.default= !FilterJointTrajectory
  1.type= string
  1.desc= See [[trajectory_filter_server/YAML configuration|YAML Configuration]] for more details.
}
```

### Services offered

```clearsilver
srv {
    0.name = filter_trajectory
    0.type = motion_planning_msgs/FilterJointTrajectory
    0.desc = This is the service offered if service_type is set to !FilterJointTrajectory. 
    1.name = filter_trajectory_with_constraints
    1.type = motion_planning_msgs/FilterJointTrajectoryWithConstraints
    1.desc = This is the service offered if service_type is set to !FilterJointTrajectoryWithConstraints. 
    }
```

### YAML Configuration

The yaml based configuration for this server is specified on the
[YAML Configuration](trajectory_filter_server/YAML configuration) page.
