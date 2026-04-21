## Deprecation



```wiki
'''This package is being deprecated'''

Instead of using this package, we recommend that you use [[joint_state_publisher]] to replace easy_state_publisher, and [[joint_state_publisher]] + [[robot_state_publisher]] for easy_tf_publisher.
```



## Overview

This package contains two separate nodes for easy publishing of a
robot's state and transform. It is useful for developing URDF models of
robots, when you don't care what the robot is doing, but how the parts
are laid out relative to one another.

The nodes read in the robot_description from the parameter server and
parses out all of the non-fixed joints, and sets the joints to zero.



```clearsilver
name = easy_tf_publisher
desc = Based on the non-fixed joints, this node publishes just the transform tree in TF messages.
sub {
}
pub {
0.name = /tf
0.type = tf/tfMessage
0.desc = Transforms for each of the links in the robot
}
param {
0.name = /robot_description
0.type = String
0.desc = Contents of the URDF file for the robot
0.default = None
}
```





```clearsilver
name = easy_state_publisher
desc = Based on the non-fixed joints, this node publishes the joint states for the robot. Can be used in conjunction with the robot_state_publisher node to publish joint states and transforms.
pub {
0.name = /joint_states
0.type = sensor_msgs/JointState
0.desc = Joint State for each non-fixed joint in the robot
}
param {
0.name = /robot_description
0.type = String
0.desc = Contents of the URDF file for the robot
0.default = None
}
```


