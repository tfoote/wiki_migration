## Overview

Swarm_ros_bridge is a lightweight middle interface ROS package mainly
based on [ZeroMQ](https://zeromq.org). It enables the specified ROS
messages transmission among swarm robots through socket communication.
The purpose of this package is to replace the traditional way of
[running ROS across multiple machines in ROS1](https://wiki.ros.org/ROS/Tutorials/MultipleMachines),
which has some drawbacks under swarm robots situation.

Source code:

<https://github.com/shupx/swarm_ros_bridge.git>

<https://gitee.com/shu-peixuan/swarm_ros_bridge.git>

csdn blog (in chinese):
<https://blog.csdn.net/benchuspx/article/details/128576723>

An example of two ROS robots communicating with each other through
swarm_ros_bridge is shown below:

![](attachment:swarm_ros_bridge_framework.png)

Compared with ROS1 multi-robot wireless communication way, it has the
following benefits:

-   **Robust**: No need for central ROS master launching first. Each
    robot has its own ROS master and they can launch in a random
    sequence, connect with each other autonomously and reconnect if
    disconnected.

```{=html}
<!-- -->
```
-   **Flexible**: You can choose the sending/receiving ROS topics rather
    than transferring all topic (names) as ROS1 does.

```{=html}
<!-- -->
```
-   **Easy to use**: Specify all the IPs and ROS topics in one
    configuration file.

Compared with ROS2 DDS communication, it has the following benefits:

-   **Lightweight**: It is a small ROS bridge node subscribing and
    sending remote ROS topics, so connecting with other ROS nodes is
    easy.

```{=html}
<!-- -->
```
-   **Reliable**: It uses [ZeroMQ](https://zeromq.org) socket
    communication based on TCP protocol while ROS2 is based on DDS,
    whose default protocol is UDP (unreliable). DDS is mainly designed
    for data exchange between native processes under wired communication
    rather than remote wireless communication.

This package is personally developed by Peixuan Shu (PhD, beihang
university, China) on Jan. 2023. Any question/suggestion is welcomed at
[swarm_ros_bridge issue](https://github.com/shupx/swarm_ros_bridge/issues)
or shupeixuan@qq.com.

## Install

Instead of installing from binary form, this package can only be
installed from source code since the ROS topic types depend on your
need.

**First, clone this package**:

```
mkdir -p swarm_ros_bridge_ws/src  # or your own ros workspace
cd swarm_ros_bridge_ws/src
git clone https://github.com/shupx/swarm_ros_bridge.git
```

or clone its gitee mirror for faster speed:

```
git clone https://gitee.com/shu-peixuan/swarm_ros_bridge.git
```

**Then, install dependencies with apt**:

```
sudo apt install libzmqpp-dev
```

or install dependencies using rosdep:

```
rosdep install --from-path swarm_ros_bridge/
```

**Finally, build this package**:

```
cd ../
catkin_make
source devel/setup.bash
```

## Usage

Make sure that all robots connects to the same network segment.

1\. Specify the IP and ROS topic information in
[config/ros_topics.yaml](https://github.com/shupx/swarm_ros_bridge/blob/master/config/ros_topics.yaml)
in the following form:

```
IP:
  self: '*'   # '*' stands for all self IPs
  robot2: 192.168.1.102  # modify IP in your situation

send_topics:
- topic_name: /topic1
  msg_type: sensor_msgs/Imu
  max_freq: 50
  srcIP: self
  srcPort: 3001 # ports of send_topics should be different

recv_topics:
- topic_name: /topic2
  msg_type: geometry_msgs/Twist
  srcIP: robot2
  srcPort: 3001
```

,where the IPs and topics can be added and modified in your need. The
``max_freq`` will limit the sending frequency once it exceeds
``max_freq``. Set ``max_freq`` large enough if you do not want
to decrease the sending frequency.

2\. Launch the bridge_node:

```
roslaunch swarm_ros_bridge test.launch
```

3\. Publish messages into send_topics and check that remote recv_topics
are receiving these messages. The console will also print INFO the first
time recv_topics receive messages.

We also provide a simple latency test demo between two machines. Please
refer to
[scripts/README.md](https://github.com/shupx/swarm_ros_bridge/tree/master/scripts/README.md)

## Advanced

### More ROS message types

The default supported ROS message types are only
<<MsgLink(sensor_msgs/Imu)>>, <<MsgLink(geometry_msgs/Twist)>>
and <<MsgLink(std_msgs/String)>>. If you need more types:

1\. Modify the macros about MSG_TYPEx and MSG_CLASSx in
[include/ros_sub_pub.hpp](https://github.com/shupx/swarm_ros_bridge/blob/master/include/ros_sub_pub.hpp),
then it will generate template functions for different ros message
types.

```c++
// In ros_sub_pub.hpp
// uncomment and modify the following lines:
#include <xxx_msgs/yy.h>
#define MSG_TYPE3 "xxx_msgs/yy"
#define MSG_CLASS3 xxx_msgs::yy
```

We support up to 10 types modification. If that is still not enough,
then you should modify the `topic_subscriber()`, `topic_publisher()`
and `deserialize_publish()` in
[include/ros_sub_pub.hpp](https://github.com/shupx/swarm_ros_bridge/blob/master/include/ros_sub_pub.hpp)
according to their styles.

2\. Add the dependent message package in `find_package()` of
[CMakeLists.txt](https://github.com/shupx/swarm_ros_bridge/blob/master/CMakeLists.txt):

```
# in CMakeLists.txt
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  geometry_msgs
  sensor_msgs
  xxx_msgs
)
```

3\. Recompile:

```
cd swarm_ros_bridge_ws/
catkin_make
```

### More send_topics

We support up to 50 send_topics. Modify the following lines in
[include/ros_sub_pub.hpp](https://github.com/shupx/swarm_ros_bridge/blob/master/include/ros_sub_pub.hpp)
if you need more:

```
git clone https://gitee.com/shu-peixuan/swarm_ros_bridge.git
```0

Then recompile:

```
git clone https://gitee.com/shu-peixuan/swarm_ros_bridge.git
```1

## Nodes

```
git clone https://gitee.com/shu-peixuan/swarm_ros_bridge.git
```2

## Future Work

1\. Dynamic RPC, including dynamic node discovery, online topic change,
and ground station monitor.

2\. Support UDP protocol for mass data transmission like video streams.

3\. Support ROS service transmission with ZeroMQ request-reply mode.

4\. Support ROS2 topic and service transmission.

## Contributor

Peixuan Shu (shupeixuan@qq.com), PhD, beihang university, China,
2023.1.1

Some applications:

[pyugvswarm](https://pyugvswarm.readthedocs.io/en/latest/overview.html):
a python package wrapper around unmanned ground vehicle (UGV) swarm
positioning / communication / control ROS1 nodes.
