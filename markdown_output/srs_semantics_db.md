## ROS API

Small introduction to component ```clearsilver
 name = example_node_name
 desc = Example description what the node is doing.

goal{
 0.name=example_action/goal
 0.type=pr2_controllers_msgs/JointTrajectoryActionGoal
 0.desc=Example description, what goal is expected
}

result{
 2.name=example_action/result
 2.type=pr2_controllers_msgs/JointTrajectoryActionResult
 2.desc=empty
}

feedback{
 0.name=example_action/feedback
 0.type=pr2_controllers_msgs/JointTrajectoryActionFeedback
 0.desc=empty
}

sub{
 0.name = /example_topic_sub
 0.type = srs_msgs/Component
 0.desc = Example description, to what topic the component subscribes to
}

pub{
 0.name = /example_topic_pub
 0.type = srs_msgs/Component
 0.desc = Example description, what topic the component publishes
}

srv{
 0.name = example_service
 0.type = cob_srvs/Trigger
 0.desc = Example description, what the service is used for
}

param{
 0.name = ~example_name
 0.type = string
 0.default = Required
 0.desc = Example description, what example_name is used for
 1.name = ~example_number
 1.type = int
 1.default = Optional
 1.desc = Example description, what example_number is used for
}

req_tf{
}

prov_tf{
}
```

## Usage/Examples

Tell how the component can be used, by providing a launch file
```
roslaunch srs_component component.launch
``` and an example script how to test it
```
rosrun srs_component test_this_component.py
```
