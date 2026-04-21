![text describing image\|height=150](attachment:modelica_ros_bridge_icon.png)

## What is modelica_bridge?

\`modelica_bridge\` establishes a bridge between
[\`Modelica\`](https://www.modelica.org), a component-oriented
equation-centric modeling language, and ROS. The connection is done via
TCP/IP sockets; in ROS, the \`modelica_bridge\` provides a node to run
the server socket.
[\`ROS_Bridge\`](https://github.com/ModROS/ROS_Bridge),
\`modelica_bridge\`\'s companion package in \`Modelica\`, contains a
\`block\` component which runs a client socket connection to ROS. Using
TCP/IP sockets allow the messages transmitted between \`Modelica\` and
ROS with preservation of order and content. The combination of
\`modelica_bridge\` and \`ROS_Bridge\` lets \`Modelica\` models and ROS
control architectures communicate with each other without any additional
internal configurations.

To get a better understanding of the way the bridge works, view the
image below, depicting the flow of information between \`Modelica\` and
ROS.

![text describing image\|width=750](attachment:data_flow_diagram.png)

-   A control block (the combination of the external C-function and
    clock-based sampler) within \`Modelica\` takes in selected feedback
    from the system model, and returns controller input to the model.
    That control block communicates with ROS to determine what the
    appropriate controller input should be; it is the interface block
    provided by \`ROS_Bridge\`.
-   The control block in \`Modelica\` sends the model feedback over a
    socket connection to a recipient server socket, hosted in a ROS
    node. This node, provided by \`modelica_bridge\`, parses the
    incoming data and publishes it to the ROS architecture. It reads the
    values coming from the controller within the ROS architecture
    (determined and constructed by the user, not \`modelica_bridge\`).
    It stores and returns these values through the socket connection to
    \`Modelica\`, to be used as control input.
-   The process of communication between ROS and \`Modelica\` is
    entirely independent of the surrounding environments; there are no
    limits on what can be sent over the socket, so long as it is
    numerical data.

Further, the discrete steps taken by the ROS node are shown below:

![text describing image\|width=750](attachment:discrete_flow_diagram.png)

-   At initialization, the node sets all data buffers and storage arrays
    to zero. It then initializes the server socket, and waits for a
    client socket request *(this separately implies that the
    \`Modelica\` model cannot be run before the ROS architecture is
    constructed, because otherwise the sockets will not successfully
    bind to the ports)*.
-   Upon receiving a client request, say the *\`n\`*th such request, the
    server stores the incoming model data into a storage array for later
    use.
-   In response to this *\`n\`*th request, the server sends back the
    control data calculated from the previous request, the control data
    from request *\`n-1\`*. *When the socket has just started, the first
    values sent back to the model will be zeros*.
-   After responding to the request, the node publishes the previously
    stored feedback data, from request *\`n\`*, to a feedback-specific
    topic, for the rest of the ROS architecture to read.
-   Finally, the node spins all callbacks, so that it can then receive
    the newly calculated control input, read from a control-specific
    topic. This newly calculated set of control input is determined from
    request *\`n\`*, to be sent to the socket upon the next request
    *\`n+1\`*.
-   Although there is a \`samplePeriod\` parameter within \`Modelica\`
    to control the speed at which the model samples the control input,
    this is based off of simulation time, which may vary from machine
    time, based on solver. Hence, it is **highly recommended to run the
    model in real-time, with fixed solver step sizes**.

### System Requirements

\`modelica_bridge\` is a ROS package, and so can only be run in Linux;
\`ROS_Bridge\` similarly can only be run on *\*nix* systems, due to the
current method of implementing sockets. Below is a list of \`Modelica\`
tools and operating systems \`ROS_Bridge\` has been tested on:

-   [SystemModeler 5.0.0 and higher](https://www.wolfram.com/system-modeler/quick-revision-history.html),
    on macOS High Sierra and Ubuntu 16.04
-   [OpenModelica 1.12.0](https://trac.openmodelica.org/OpenModelica/wiki/ReleaseNotes/1.12.0),
    on macOS High Sierra and Ubuntu 16.04

## Tutorials

Here are a few [tutorials](modelica_bridge/Tutorials) that explain how
to use the \`modelica_bridge\` package in detail:

-   [Getting Started](modelica_bridge/Tutorials/Introduction to modelica_bridge):
    Introduction to \`modelica_bridge\`\'s usage; learn the process of
    constructing the system, including how to integrate
    \`modelica_bridge\` architecture, and how to run the provided
    example.

## Nodes

### modbridge_node

#### Subscribed Topics

\`/control_values\`
([modelica_bridge/ModComm](https://docs.ros.org/kinetic/api/modelica_bridge/html/msg/ModComm.html))

-   Reads data from other ROS nodes, to be sent to the model as control
    input

#### Published Topics

\`/model_values\`
([modelica_bridge/ModComm](https://docs.ros.org/kinetic/api/modelica_bridge/html/msg/ModComm.html))

-   Publishes selected feedback from the model to the ROS domain

#### Parameters

\`port_num\_\` (\`int\`, default: 9091)

-   Port number the tcp/ip socket on ROS is listening on
    \`update_rate\_\` (\`int\`, default: 20)
-   Maximum frequency (hz) the node will run at
