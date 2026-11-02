![width="689px",height="564px"](doc/frames4.png)

## Overview

robot_state_publisher uses the URDF specified by the parameter
`robot_description` and the joint positions from the topic
`joint_states` to calculate the forward kinematics of the robot and
publish the results via [tf](https://index.ros.org/p/tf).

Please see the tutorial on
[using the robot state publisher on your own robot](#using-the-robot-state-publisher-on-your-own-robot).
It will explain how you can publish the state of your robot to
[tf](https://index.ros.org/p/tf), using the robot state publisher.

*Note:* All fixed transforms are
[future dated](https://index.ros.org/p/tf) by 0.5s.

## state_publisher node

### ROS API

#### Subscribed topics

`joint_states`
([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html))

. joint position information

#### Parameters

`robot_description` (`urdf map`)

. The [urdf](https://index.ros.org/p/urdf) xml robot description. This
is accessed via
[`urdf_model::initParam`](http://docs.ros.org/api/urdf/html/classurdf_1_1Model.html#a0e3b0a0974fb948dd9228c50c5d6783c)

`tf_prefix` (`string`)

. Set the [tf](https://index.ros.org/p/tf) prefix for namespace-aware
publishing of transforms. See [tf_prefix](https://index.ros.org/p/tf)
for more details.

`publish_frequency` (`double`)

. Publish frequency of state publisher, default: 50Hz.



```wiki
`ignore_timestamp` (`bool`)

 . If true, ignore the publish_frequency and the timestamp of joint_states and publish a  tf for each of the received joint_states. Default is "false".
```





```wiki
`use_tf_static` (`bool`)
  Set whether to use the /tf_static latched static transform broadcaster. Default: true.
```

## Using the robot state publisher on your own robot

- **Note:** This tutorial assumes you completed the
  [create your own urdf file](https://index.ros.org/p/urdf) tutorial.
- **Description:** This tutorial explains how you can publish the state
  of your robot to [tf](https://index.ros.org/p/tf), using the robot
  state publisher.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:** For a detailed tutorial on how to use the
  robot_state_publisher in combination with a urdf, take a look at
  [this tutorial](https://index.ros.org/p/urdf)



```wiki
tf is deprecated in favor of [[tf2]]. [[tf2]] provides a superset of the functionality of tf and is actually now the implementation under the hood. If you're just learning now it's strongly recommended to use the [[tf2/Tutorials]] instead.
```



When you are working with a robot that has many relevant frames, it
becomes quite a task to publish them all to tf. The robot state
publisher is a tool that will do this job for you.

![height="408px",width="471px"](doc/frames2.png)

The robot state publisher helps you to broadcast the state of your robot
to the [tf transform library](https://index.ros.org/p/tf). The robot
state publisher internally has a kinematic model of the robot; so given
the joint positions of the robot, the robot state publisher can compute
and broadcast the 3D pose of each link in the robot.

You can use the robot state publisher as a standalone ROS node or as a
library:

### Running as a ROS node

#### robot_state_publisher

The easiest way to run the robot state publisher is as a node. For
normal users, this is the recommended usage. You need two things to run
the robot state publisher:

- A [urdf](https://index.ros.org/p/urdf) xml robot description loaded on
  the [Parameter Server](Parameter Server).
- A source that publishes the joint positions as a
  [sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html).

Please read the following sections on how to configure the parameters
and topics for
robot_state_publisher.

![width="689px",height="564px"](doc/frames4.png)

### Overview

robot_state_publisher uses the URDF specified by the parameter
`robot_description` and the joint positions from the topic
`joint_states` to calculate the forward kinematics of the robot and
publish the results via [tf](https://index.ros.org/p/tf).

Please see the tutorial on
[using the robot state publisher on your own robot](#using-the-robot-state-publisher-on-your-own-robot).
It will explain how you can publish the state of your robot to
[tf](https://index.ros.org/p/tf), using the robot state publisher.

*Note:* All fixed transforms are
[future dated](https://index.ros.org/p/tf) by 0.5s.

### state_publisher node

#### ROS API

##### Subscribed topics

`joint_states`
([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html))

. joint position information

##### Parameters

`robot_description` (`urdf map`)

. The [urdf](https://index.ros.org/p/urdf) xml robot description. This
is accessed via
[`urdf_model::initParam`](http://docs.ros.org/api/urdf/html/classurdf_1_1Model.html#a0e3b0a0974fb948dd9228c50c5d6783c)

`tf_prefix` (`string`)

. Set the [tf](https://index.ros.org/p/tf) prefix for namespace-aware
publishing of transforms. See [tf_prefix](https://index.ros.org/p/tf)
for more details.

`publish_frequency` (`double`)

. Publish frequency of state publisher, default: 50Hz.



```wiki
`ignore_timestamp` (`bool`)

 . If true, ignore the publish_frequency and the timestamp of joint_states and publish a  tf for each of the received joint_states. Default is "false".
```





```wiki
`use_tf_static` (`bool`)
  Set whether to use the /tf_static latched static transform broadcaster. Default: true.
```



#### Example launch file

Once you have setup the XML robot description and a source for joint
position information, simply create a launch file like this one:



```
<launch>
   <!-- Load the urdf into the parameter server. -->
   <param name="my_robot_description" textfile="$(find mypackage)/urdf/robotmodel.xml"/>
    
   <node pkg="robot_state_publisher" type="robot_state_publisher" name="rob_st_pub" >
      <remap from="robot_description" to="my_robot_description" />
      <remap from="joint_states" to="different_joint_states" />
    </node>
  </launch>
```



### Running as a library

Advanced users can also run the robot state publisher as a library, from
within their own C++ code. After you include the header:



```
#include <robot_state_publisher/robot_state_publisher.h>
```

 all you need is the constructor which takes in
a [KDL tree](kdl)



```
RobotStatePublisher(const KDL::Tree& tree);
```

 and now, every time you want to publish the
state of your robot, you call the publishTransforms functions:



```
// publish moving joints
  void publishTransforms(const std::map<std::string, double>& joint_positions,
                         const ros::Time& time);

  // publish fixed joints
  void publishFixedTransforms();
```

 The first argument is a map with joint names
and joint positions, and the second argument is the time at which the
joint positions were recorded. It is okay if the map does not contain
all the joint names. It is also okay if the map contains some joints
names that are not part of the kinematic model. But note if you don't
tell the joint state publisher about some of the joints in your
kinematic model, then your tf tree will not be complete.

## Tutorials

- [Using the robot state publisher on your own robot](#using-the-robot-state-publisher-on-your-own-robot):
  This tutorial explains how you can publish the state of your robot to
  [tf](https://index.ros.org/p/tf), using the robot state publisher.

## Troubleshooting

### Understanding log messages

#### Errors when using the package

- Failed to extract kdl tree from xml robot description At construction
  time the robot state publisher tries to construct a KDL Tree to
  represent the robot kinematics. This tree is constructed from an xml
  Robot Description Format \[\[urdf/Overview\|(URDF)\]. The above error
  message occurs when the parsing of the urdf fails. If you didn't
  change anything to the urdf, then most likely this error means the
  urdf was not found at all. By default the robot state publisher looks
  for the urdf on the parameter server, under "robot_description_new".
  To check if the urdf exists on the parameter server, type:
  

```
$ rosparam get robot_description_new
```


- Did not find root of tree This error means that the KDL Tree that was
  constructed from the urdf (see above error message) is empty, and
  therefore does not have a root link. See the above error message for
  troubleshooting.

### The robot state publisher does not work

#### Is the robot state publisher still running?

To check if the robot state publisher is running, you should find out on
what the name of the node is. The node name depends on the name you
specified in the launch file: 

```
...
  <node pkg="robot_state_publisher" type="state_publisher" name="my_name">
  ...
```

 Look for the
*name="\..."* field. In this example, the node name is 'my_name'. To
verify if the node is running, type: 

```
$ rosnode ping my_name
```



#### Is the robot state publisher receiving input?

The robot state publisher listens for joint angles in the topic
'joint_states'. To check if any messages are sent on this topic, type:


```
$ rostopic hz joint_states
```

 You should see an average publish rate being
displayed. If not, the input is not published.

#### Is the robot state publisher sending output?

The robot state publisher sends output on the topic of the transform
library \[tf\|(tf)\]. To verify if anything is sent on this topic, type:


```
$ rostopic hz tf_message
```

 You should see an average publish rate being
displayed. If not, the output is not published. However, if the average
rate is not zero, you're still not sure that the robot state publisher
is sending these messages; they could as well come from another source
in the system sending out messages to tf. You'll have to look at the
content of the message to see if it comes from the robot state
publisher. You should know which frames are supposed to be published by
the robot state publisher. Suppose you expect the frame 'my_frame' to
be published, you can verify this by typing: 

```
$ rostopic echo tf_message | grep my_frame
```
