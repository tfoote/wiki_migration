## Overview

This package contains all launch files that are required for the model
based diagnosis system.

## Launch Files

### aria.launch

It launches a node \'\'aria.py\'\' which is just a test node for testing
purpose. This node publishes string data on a topic
\'\'/aria_node_topic\'\' with 10Hz frequency.

### laser.launch

It launches a node \'\'laser.py\'\' which is just a test node for
testing purpose. This node publishes string data on a topic
\'\'/laser_node_topic\'\' with 10Hz frequency.

### observers.launch

This launches all the observers to observer nodes and topics. User can
change the observers or node or topic according to its requirement. User
can also add or remove observers from this file.

### diagnosis_model.launch

This launch file launches diagnosis model server. It also provides model
server as parameter to the node.

### diagnosis_engine.launch

This launches first Java based diagnosis engine server. After that it
launches diagnosis engine controller that is a client and controls the
server input and output.

### action_servers.launch

It launches node action server. This action server is required for
starting or stopping the node(s). It is also necessary to run it before
the diagnosis repair.

### diagnosis_repair.launch

Like diagnosis_engine.launch it also first launches a Java based
Planner. The planner also needs \'\'domain.pddl\'\' file as parameter.
Afterwards it launches diagnosis repair engine which uses the planner to
get action plan and then invokes the action server to fulfill the action
plan.
