Node lifecycle is coming to ROS 2.0 in form of
[managed nodes](https://github.com/ros2/ros2/wiki/Managed-Nodes), why
not bring it to ROS already?

[robot_activity](http://wiki.ros.org/robot_activity) is a ROS package,
which implements node lifecycle. The idea is that you don\'t have to
write a lot of bolier-plate code in C++ when making a new ROS node and
you get a lot of features for free!

A minimal example using \`robot_activity\` is available in the
\`robot_activity_tutorials\` package. Check the
[robot_activity_tutorials_minimal_node.cpp](https://github.com/snt-robotics/robot_activity/blob/master/robot_activity_tutorials/src/robot_activity_tutorials_minimal_node.cpp)

The main features of the package are:

1\. Controllable node lifecycle - nodes automatically expose ROS
services that allow you to *pause*, *stop*, *restart*, *reconfigure* and
*terminate* a given node 2. ROS subscribers and services are
automatically managed for you during the lifecycle. Services and
callbacks will not be called if you request your node to exit
**RUNNING** state. This means that you can now safely reconfigure your
nodes without relaunching! 3. Creation of super-nodes, multiple ROS
nodes in a single process (similar to nodelets) 4. Easy integration with
a node supervisor using heartbeat and error messages.

The node lifecycle can be represented as a Finite State Machine (FSM):
![robot_activity-FSM](attachment:fsm-resized.png) When you inherit from
\`robot_activity::ManagedRobotActivity\`, the subscribers and services
are managed for you, meaning that they will only be executed in the
**RUNNING** state.

1\. In **PAUSED** state, they are invoked, but immediately return
without executing the actual body of the callback (services return
\`false\`). 2. In **STOPPED** state, all registered subscribers and
services are shutdown, so that no IPC or TCP/IP traffic occurs. 3. When
transitioning back to **PAUSED** state from **STOPPED**, the subscribers
and services are once again advertised for you (with the same
arguments), but still not yet fully executed 4. When transitioning back
to **RUNNING** state from **PAUSED**, the subscibers and services are
now functional. However, all callback invocation that occured out of
**RUNNING** state are lost.

## Library

```clearsilver
node.0 {
 name = API
 desc = When you inherit from robot_activity::RobotActivity or robot_activity::ManagedRobotActivity, the following node API will be automatically exposed
 param {
  0.name = '~wait_for_supervisor'
  0.type = boolean
  0.default = `True`
  0.desc = If set to `True`, the node upon initialization will immediately pause its execution and wait until there is at least on subscriber on the global `\heartbeat` topic
  1.name = '~autostart_after_reconfigure'
  1.type = boolean
  1.default = `False`
  1.desc = If set to `True`, upon calling `~reconfigure` service the node will transtition to `UNCONFIGURED` and then to `RUNNING`, otherwise it will only reach `STOPPED` state
  2.name = '~heartbeat_rate'
  2.type = float
  2.default = 1.0f
  2.desc = Heartbeat rate in Hz published on `/heartbeat`
 }
 pub {
  0.name = /heartbeat
  0.type = robot_activity_msgs/State
  0.desc = Heartbeat msg is send to a global topic (usually listened to by a node supervisor)
  1.name = /error
  1.type = robot_activity_msgs/Error
  1.desc = User can easily raise errors from the inherited class, which will be published on the global /error topic (usually listened to by a node supervisor). This is done by calling [[http://docs.ros.org/kinetic/api/robot_activity/html/classrobot__activity_1_1RobotActivity.html#acee6e5cae0413e4a8d7cf729765c6834|RobotActivity::notifyError]]
 }
 srv {
  0.name = ~name_space/start
  0.type = std_srvs/Empty
  0.desc = Transitions from current state to `RUNNING`
  1.name = ~name_space/stop
  1.type = std_srvs/Empty
  1.desc = Transitions from current state to `STOPPED`
  2.name = ~name_space/pause
  2.type = std_srvs/Empty
  2.desc = Transitions from current state to `PAUSED`
  3.name = ~name_space/restart
  3.type = std_srvs/Empty
  3.desc = Transitions from current state to `STOPPED` and then to `RUNNING`
  4.name = ~name_space/reconfigure
  4.type = std_srvs/Empty
  4.desc = Transitions from current state to `UNCONFIGURED` and then to `RUNNING` if param `~autostart_after_reconfigure` is set to True, otherwise transitions to `STOPPED`
  5.name = ~name_space/terminate
  5.type = std_srvs/Empty
  5.desc = Transitions from current state to `TERMINATED`
}
```

\<\<GitHubIssues(snt-robotics/robot_activity)\>\>
