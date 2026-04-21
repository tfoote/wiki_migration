Services the
[GraspHandPostureExecution](object_manipulation_msgs/GraspHandPostureExecutionAction)
action and
[GraspHandPostureQuery](http://www.ros.org/doc/api/object_manipulation_msgs/html/srv/GraspHandPostureQuery.html)
service, as requested by the [object_manipulator](object_manipulator).

This package is mostly a thin wrapper for the
[pr2_gripper_action](pr2_gripper_action) which talks directly to the PR2
gripper controller.

## Running the Manipulation Pipeline

To launch the manipulation pipeline and execute pickup and place tasks
using the PR2 robot, tutorials and launch files are provided in
[pr2_tabletop_manipulation_apps](pr2_tabletop_manipulation_apps).

## ROS API

### Parameters



```clearsilver
param {
no_header=True
0.name= gripper_virtual_joint_name
0.type= string
0.default= "undefined"
0.desc=.

1.name=gripper_object_presence_threshold
1.type=double
1.default=DEFAULT_GRIPPER_OBJECT_PRESENCE_THRESHOLD
1.desc=.

2.name=gripper_open_gap_value
2.type=double
2.default=DEFAULT_GRIPPER_OPEN
2.desc=.

3.name=gripper_closed_gap_value
3.type=double
3.default=DEFAULT_GRIPPER_CLOSED
3.desc=.

4.name=gripper_max_effort
4.type=double
4.default=DEFAULT_GRIPPER_MAX_EFFORT
4.desc=.

5.name=gripper_type
5.type=string
5.default="pr2"
5.desc=.
}
```



### Services Provided



```clearsilver
srv{
0.name=grasp_query_name
0.type=object_manipulation_msgs/GraspStatus
0.desc=.
}
```



### Action Servers Provided

-   posture_action_name
    (object_manipulation_msgs/GraspHandPostureExecutionAction)

### Action Servers Required

-   gripper_action_name (pr2_controllers_msgs/Pr2GripperCommandAction)

### Subscribers



```clearsilver
sub{
0.name=joint_states
0.type=sensor_msgs/JointState
0.desc=.
}
```


