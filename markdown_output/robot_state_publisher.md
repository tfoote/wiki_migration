![\|width=\"689px\",height=\"564px\"](attachment:frames4.png)

## Overview

robot_state_publisher uses the URDF specified by the parameter
`robot_description` and the joint positions from the topic
\`joint_states\` to calculate the forward kinematics of the robot and
publish the results via [tf](tf).

Please see the tutorial on
[using the robot state publisher on your own robot](robot_state_publisher/Tutorials/Using the robot state publisher on your own robot).
It will explain how you can publish the state of your robot to [tf](tf),
using the robot state publisher.

*Note:* All fixed transforms are
[future dated](tf/FAQ#Why_do_I_see_negative_average_delay_in_tf_monitor.3F)
by 0.5s.

## state_publisher node

### ROS API

#### Subscribed topics

\`joint_states\` (\<\<MsgLink(sensor_msgs/JointState)\>\>)

. joint position information

#### Parameters

\`robot_description\` (\`urdf map\`)

. The [urdf](urdf) xml robot description. This is accessed via
[\`urdf_model::initParam\`](http://docs.ros.org/api/urdf/html/classurdf_1_1Model.html#a0e3b0a0974fb948dd9228c50c5d6783c)

\`tf_prefix\` (\`string\`)

. Set the [tf](tf) prefix for namespace-aware publishing of transforms.
See [tf_prefix](tf/Theory) for more details.

\`publish_frequency\` (\`double\`)

. Publish frequency of state publisher, default: 50Hz.

```wiki
`ignore_timestamp` (`bool`)

 . If true, ignore the publish_frequency and the timestamp of joint_states and publish a  tf for each of the received joint_states. Default is "false".
```

```wiki
`use_tf_static` (`bool`)
  Set whether to use the /tf_static latched static transform broadcaster. Default: true.
```
