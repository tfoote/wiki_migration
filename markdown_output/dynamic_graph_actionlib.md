This package provide a set of actions controlling dynamic-graph through
actionlib.

It is designed to be intergrated into a high-level supervisor such as
[smach](smach).

## Using the RunDynamicGraphCommands action



```shell
# Start standalone controller.
rosrun dynamic_graph_bridge interpreter

# Start the actionlib server.
rosrun dynamic_graph_actionlib RunCommandsServer

# Send a command through actionlib.
#
# You may replace a=1 by the Python command to be executed
# remotely.
rosrun dynamic_graph_actionlib RunCommandsClient 'a=1'
```


