**Warning:** this package provides an install target that should be run
before using this package, unlike others ROS package. I.e. type `make
install -C \$(rospack find dynamic_graph_bridge)` before using this
package.

This package provides three
[dynamic-graph](http://jrl-umi3218.github.com/dynamic-graph/doxygen/HEAD/)
entites:

-   `RosImport` allows communication from dynamic-graph to ROS,
-   `RosExport` allows communication from ROS to dynamic-graph,
-   `RosJointState` publishes the current command as a
    <<MsgLink(sensor_msgs/JointState)>>.

These three entities can be easily instantiated together using the
Python `Ros` class.

```python
from dynamic_graph.ros import *

# Here we makes the assumption that "robot" is an instance of HumanoidRobot
# whose configuration will be streamed over the network.
#
# *MAKE SURE THAT roscore IS RUNNING BEFORE CONTINUING*
ros = Ros(robot)

# Add a signal 'mySignal' to rosExport which
#  will get published into the topic 'myTopic'.
# The associated timestamp associated with accessible through
# the 'myTopicTimestamp' signal.
ros.rosExport.add('vector3Stamped', 'mySignal', 'myTopic')
```

The published topics after executing this sample are:
```
/dynamic_graph/joint_states
/dynamic_graph/myTopic
/rosout
/rosout_agg
```

## Supported types

`dynamic_graph_bridge` supports the following conversion:

  -- ---------------------------------------------- -- ------------------------------- -- ---------------------------------------------- --
     **ROS message type**                              **dynamic-graph signal type**      **Type name** (normal/stamped)                 
     <<MsgLink(std_msgs/Float64)>>                 `double`                         double / n/a                                   
     <<MsgLink(dynamic_graph_bridge/Matrix)>>      `ml::Matrix`                     matrix / n/a                                   
     <<MsgLink(dynamic_graph_bridge/Vector)>>      `ml::Vector`                     vector / n/a                                   
     <<MsgLink(geometry_msgs/Vector3)>>            `ml::Vector`                     vector3 / vector3stamped                       
     <<MsgLink(geometry_msgs/Transform)>>          `sot::MatrixHomogeneous`         matrixHomogeneous / matrixHomogeneousStamped   
     <<MsgLink(geometry_msgs/Twist)>>              `ml::Vector`                     twist / twistStamped                           
  -- ---------------------------------------------- -- ------------------------------- -- ---------------------------------------------- --

The last column matches the type name which must be passed as the first
argument of the `add` command.

## dynamic-graph Entities

### RosImport

Imports a ROS topic into `dynamic-graph`.

-   Commands:
-   `add "<signal type>" "<signal name>" "<topic name>"`
-   Signals created during the instantiation:
-   None

### RosExport

Exports a `dynamic-graph` signal value into ROS.

-   Commands:
-   `add "<signal type>" "<signal name>" "<topic name>"`
-   Signals created during the instantiation:
-   `trigger`: this signal must be called each time the graph is
    evaluated. It is recommended to use `robot.device.after` to do so.
    When the signal is triggered the ROS values are copied into the
    `dynamic-graph` signals.

This entity copies ROS values at a fixed rate of 10hz.

### RosJointState

Publishes the robot joints state.

-   Commands:
-   None
-   Signals created during the instantiation:
-   `state`: robot state to be published. It should be plugged to
    `robot.device.state` where `robot` is your local instance of the
    `HumanoidRobot` Python class.
-   `trigger`: this signal must be called each time the graph is
    evaluated. It is recommended to use `robot.device.after` to do so.
    When the signal is triggered the ROS values are copied into the
    `dynamic-graph` signals.

### RosRobotModel

Load an URDF model and provides its associated information into
dynamic-graph.

-   Commands:
-   `loadFromParameterServer()` Load the model stored in the
    `robot_description` key of the parameter server. Require
    `roscore` to be launched.
-   `loadUrdf(filename)` Load the model using a file name.
-   Signals created during the instantiation:
-   To be documented.

## Real-time considerations

`dynamic-graph` is designed to run in the real-time control loop. An
example is [sot_pr2](sot_pr2) which provides a real-time controller for
the PR2 robot.

The ROS entitites are designed to be non-blocking and can be safely used
on a robot without compromising the real-time constraints.

The values exported to ROS are published using a !RealtimePublisher from
the [realtime_tools](realtime_tools) package. It means that a separate
thread is handling the publishing. The real-time thread and the
publishing thread are synchronized using a mutex. If the mutex is locked
when the real-time thread tries to copy the signal value, the copy is
skipped. Practically speaking, it means that signal values may be lost
regularly. The joint state publisher is implemented in a similar manner.

On the opposite, the values imported into `dynamic-graph` are relying
on subscribers running in an asynchronous spinner. This spinner uses a
separate thread. Each evaluation of the `trigger` signal of the entity
will then copy the data from this thread to dynamic-graph. This
lightweight process should not perturb the real-time loop.

## Sending remote commands

dynamic-graph is typically embedded into a controller manager ensuring
hardware communication and real-time management. In this context, we
need to be able to send remote Python commands to initialize the graph.

The class `Interpreter` embeds a Python interpreter which receives its
command from a dedicated ROS service called `run_command`. The
associated service type <<SrvLink(dynamic_graph_bridge/RunCommand)>>
is defined in this package.

To use this feature, start dynamic-graph in your controller manager
(such as the standalone controller provided by this package,
GrxUI/hrpsys or the PR2 controller manaager) and launch the remote
client:

```shell
# Launch the stand-alone controller.
# This embeds the Python interpreter into a executable which provides
# the run_commands service.
rosrun dynamic_graph_bridge interpreter&
# Connect to the controller to send commands.
rosrun dynamic_graph_bridge run_command
```

You will then obtain a prompt almost equivalent to a classical Python
prompt except that you must keep in mind that commands are run on a
remote host. Filesystem, hardware, etc. are the hardware of the host
running the controller manager.

## Obtaining a TF tree

Currently, there is no way to publish [tf](tf) information in a
real-time loop safely. Therefore, a small Python scripts forwards the
topics into tf.

```
rosrun dynamic_graph_bridge tf_publisher _frame:=/a _child_frame:=/b _topic:=/mytopic
```

This script will listen for the topic `mytopic` (which type must be
<<MsgLink(geometry_msgs/TransformStamped)>>) and publish in [tf](tf)
a transformation from frame `a` to frame `b`.

On the opposite, the robot body transformations should be handled by
[robot_state_publisher](robot_state_publisher) which computes them from
the robot [urdf](urdf) description and the
<<MsgLink(sensor_msgs/JointState)>> message.

### ROS API

```clearsilver
name = tf_publisher
desc = Stream tf transformation from a topic

sub {
  0.name = ~topic
  0.type = geometry_msgs/TransformStamped
  0.desc = Listen for transformation on this topic
}

pub {
  0.name = /tf
  0.type = tf/tfMessage
  0.desc = Stream tf frame.
}

param {
  0.name = ~frame
  0.type = std_msgs/String
  0.desc = Name of the frame in which the transform is expressed.

  1.name = ~child_frame
  1.type = std_msgs/String
  1.desc = Child frame name.

  2.name = ~topic
  2.type = std_msgs/String
  2.desc = Which topic is listened to retrieve transformation.

  3.name = ~rate
  3.type = Float64
  3.desc = Update rate.
  3.default = 5hz
}

prov_tf {
  0.from = ~frame
  0.to   = ~child_frame
  0.desc = Streamed frame.
}
```
