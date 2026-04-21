## Overview

The MTConnect ROS Bridge consists of 4 nodes and one library file that
execute the communications between the robot and machine tool. The nodes
also operate within the ROS-Industrial system to echo machine data and
action requests. The bridge nodes and library file are:

-   bridge_publisher.py
-   Publishes machine tool topics
-   bridge_subscriber.py
-   Communicates robot topics to the machine tool
-   bridge_client.py
-   Executes machine tool action clients
-   bridge_server.py
-   Communicates robot action requests to the machine tool
-   bridge_library.py
-   Suite of methods utilized by the four bridge nodes

Each node requires a configuration file that defines the ROS package in
use and the ROS to MTConnect datatype conversion, if any. What follows
is a description of each ROS node and how to utilize them in an
application that interfaces MTConnect to the ROS system.

NOTE: The following assumes the reader is familiar with [topics](Topics)
and [actions](actionlib)

## Bridge Publisher

This module launches a ROS node that will read event data from the
machine tool and then publish the data as a ROS topic. Topics and topic
parameters are specified by a configuration file that must be included
with the main program during execution. If this file is not provided,
the node will terminate with an error message indicating the need for
this file.

![](attachment:bridge_publisher_interaction.png)

The bridge publisher accomplishes its goal by parsing the machine tool
XML for changing events. The node then publishes the events specified in
the configuration file whether they have changed or not. The node
publishes at a frequency of 10 hertz, or 10 updates per second. The node
will publish 1..n ROS topics.

Command line example:



```
bridge_publisher.py -i bridge_publisher_config.yaml 
bridge_publisher.py -input bridge_publisher_config.yaml
```



### Bridge Publisher Configuration File

The configuration file is critical to the application of the bridge
publisher. It is a YAML hash file that has two sections, the first group
contains several key:value pairs the are required to obtain XML data via
a HTTP connection. The second group contains the data required for the
ROS topics that will be published.

The format for the first group is as follows:



```
url:            string representing the url for the machine tool
url_port:       integer identifier for the url http port
machine_tool:   string representing the machine tool
xml_namespace:  string representing the XML namespace for the machine tool
```



The key strings must not be changed; they are hard coded into the bridge
publisher node. Here is an example of this first group:



```
url: localhost
url_port: 5000 
machine_tool: /cnc
xml_namespace: urn:mtconnect.org:MTConnectStreams:1.2
```



In order to publish a ROS topic, the following data are required: 1. ROS
topic name in !CamelCase 1. ROS package that has the message / message
type 1. XML data item tag for the machine tool event 1. Python
dictionary defining the conversion between MTConnect and ROS

The format for the second group is as follows
**`'(in the YAML file, do not use tabs, only spaces for indenting)`**':



```
key : string, topic name
    key : string, ROS package/type
        key : string, data item event tag
            value : dictionary of string:string MTCoonect-->ROS conversions
```



Though the ROS topic string is arbitrary, the string for the ROS package
and message type and the key for the machine tool event must already
exist in the ROS package and machine tool configuration file,
respectively. Here is an example of the second group showing two ROS
topics, !CncResponseTopic and !CncRequesTopic:



```
CncResponseTopic:
    mtconnect_msgs/CncStatus:
        OpenDoor:
            {'ACTIVE':'CLOSED','COMPLETE':'UNKNOWN','READY':'OPEN', 'NOT_READY':'OFF', 'UNAVAILABLE':'UNKNOWN'}
        CloseDoor:
            {'ACTIVE':'OPEN','COMPLETE':'UNKNOWN','READY':'CLOSED', 'NOT_READY':'OFF', 'UNAVAILABLE':'UNKNOWN'}
        DoorState:
            {'OPEN':'OPEN','CLOSED':'CLOSED','UNLATCHED':'UNKNOWN', 'NOT_READY':'UNKNOWN', 'UNAVAILABLE':'UNKNOWN'}
        OpenChuck:
            {'ACTIVE':'CLOSED','COMPLETE':'UNKNOWN','READY':'OPEN', 'NOT_READY':'OFF', 'UNAVAILABLE':'UNKNOWN'}
        CloseChuck:
            {'ACTIVE':'OPEN','COMPLETE':'UNKNOWN','READY':'CLOSED', 'NOT_READY':'OFF', 'UNAVAILABLE':'UNKNOWN'}
        ChuckState:
            {'OPEN':'OPEN','CLOSED':'CLOSED','UNLATCHED':'UNKNOWN', 'NOT_READY':'UNKNOWN', 'UNAVAILABLE':'UNKNOWN'}

CncRequestTopic:
    mtconnect_msgs/CncRequest:
        MaterialLoad:
            {'ACTIVE':'ENABLED','COMPLETE':'TRUE','READY':'OPEN', 'NOT_READY':'OFF', 'UNAVAILABLE':'UNKNOWN'}
        MaterialUnload:
            {'ACTIVE':'ENABLED','COMPLETE':'TRUE','READY':'OPEN', 'NOT_READY':'OFF', 'UNAVAILABLE':'UNKNOWN'}
```



Regarding the MTConnect to ROS conversion, note that the ROS !CncRequest
message type <<MsgLink(mtconnect_msgs/CncRequest)>> consists of an
array of strings, or from a terminal:



```
rosmsg show mtconnect_msgs/CncRequest
```



For example, during a !MaterialLoad sequence, the bridge publisher
acquires the MTConnect event state, such as 'ACTIVE' and translates it
into a ROS 'ENABLED' state. This state is actually a ROS constant,
which is set to an integer value. In this case the value for 'ENABLED'
is 1, which is what is published. The user can verify this by running
from a terminal:



```
rostopic echo /CncRequestTopic
```



## Bridge Subscriber

This module launches a ROS node that will update the MTConnect Agent
with the robot event state. This is accomplished by subscribing to the
robot topics that publish specific state information required by the
machine tool. The node will continue to update the MTConnect Agent with
the robot event states whether they have changed or not. The node will
subscribe to 1..n ROS topics.

![](attachment:bridge_subscriber_interaction.png)

Topics and topic parameters are specified by a configuration file that
must be included with the main program during execution. If this file is
not provided, the node will terminate with an error message indicating
the need for this file.

Command line example:



```
bridge_subscriber.py -i bridge_subscriber_config.yaml 
bridge_subscriber.py -input bridge_subscriber_config.yaml
```



### Bridge Subscriber Configuration File

The configuration file is critical to the application of the bridge
subscriber. It is a YAML hash file that has two sections, the first
group contains several key:value pairs the are required to set up the
MTConnect Agent on a specific url and port. The second section contains
the ROS topics that will receive a subscription in a 4-level nested
group of key:value pairs.

The format for the first group is as follows:



```
url 	    : string representing the url for the machine tool
adapter_port: integer identifier for the url port accessed by the MTConnect Agent
```



The key strings must not be changed, as they are hard coded into the ROS
bridge subscriber node. Here is an example of this first group:



```
url : localhost
adapter_port : 7878
```



Make sure that the adapter port matches what is specified in the
MTConnect Agent configuration file for the robot. If this number
differs, the MTConnect Agent will be sending information to a port not
accessible by the machine tool agent which will result in sequence
errors between the two systems.

The format for the second group is as follows
**`'(in the YAML file, do not use tabs, only spaces for indenting)`**':



```
url:            string representing the url for the machine tool
url_port:       integer identifier for the url http port
machine_tool:   string representing the machine tool
xml_namespace:  string representing the XML namespace for the machine tool
```

0

Multiple attributes are possible for a ROS topic so make sure all of the
attributes are listed with the appropriate conversions in the
configuration file.

The string for the ROS topic, package and message type and the key for
the robot event must already exist in the ROS package and the robot
MTConnect Agent configuration file, respectively. Here is an example of
the second group showing a configuration for a subscription to two ROS
topics, *!RobotStateTopic* and *!RobotSpindleTopic*:



```
url:            string representing the url for the machine tool
url_port:       integer identifier for the url http port
machine_tool:   string representing the machine tool
xml_namespace:  string representing the XML namespace for the machine tool
```

1

## Bridge Client

This module launches a ROS node that will stream XML data from the
machine tool and will launch a ROS action client if the machine tool
requests an action. For example, if the machine tool requests a
!MaterialLoad action, it will change the !MaterialLoad event tag from
'READY' to 'ACTIVE'. Once this change is captured by this node, the
node launches a ROS !MaterialLoadAction client. Subsequently, the
!MaterialLoadAction server must be executed to process the action. If
not, the system waits until the !MaterialLoadAction server is available.

![](attachment:bridge_client_interaction.png)

Machine tool actions and goals are specified by a configuration file
that must be included with the main program during execution. If this
file is not provided, the node will terminate with an error message
indicating the need for this file.

Command line example:



```
url:            string representing the url for the machine tool
url_port:       integer identifier for the url http port
machine_tool:   string representing the machine tool
xml_namespace:  string representing the XML namespace for the machine tool
```

2

**Important:**The bridge client requires an additional service
call(SetMTConnectState) to set the MTConnect status to READY/NOT READY.
The service exists in the same namespace as the action and must be
called manually from the action server. The NOT READY state is used by
MTConnect to signal that a component is up but not ready to perform a
task. In the ROS action world, this status does not exist. An action
server would simply return FAILED immediately. In order to interact with
MTConnect this service should be set to READY when a request can be
handled and NOT READY when something does not allow it.

### Bridge Client Configuration File

The bridge client configuration file is a YAML hash file that has two
sections, the first group contains several key:value pairs the are
required to obtain XML data via a HTTP connection. The second section
contains the machine tool actions and goals in a 4-level nested group of
key:value pairs.

The format for the first group is as follows:



```
url:            string representing the url for the machine tool
url_port:       integer identifier for the url http port
machine_tool:   string representing the machine tool
xml_namespace:  string representing the XML namespace for the machine tool
```

3

The key strings must not be changed, as they are hard coded into the ROS
bridge client node. Here is an example of this first group:



```
url:            string representing the url for the machine tool
url_port:       integer identifier for the url http port
machine_tool:   string representing the machine tool
xml_namespace:  string representing the XML namespace for the machine tool
```

4

The format for the second group is as follows
**`'(in the YAML file, do not use tabs, only spaces for indenting)`**':



```
url:            string representing the url for the machine tool
url_port:       integer identifier for the url http port
machine_tool:   string representing the machine tool
xml_namespace:  string representing the XML namespace for the machine tool
```

5

The string for the ROS package and the key for the machine tool event
must already exist in the ROS package and machine tool configuration
file, respectively. Here is an example of the second group showing two
machine tool events that require a ROS action client:



```
url:            string representing the url for the machine tool
url_port:       integer identifier for the url http port
machine_tool:   string representing the machine tool
xml_namespace:  string representing the XML namespace for the machine tool
```

6

Since an action goal will be defined by the machine tool during runtime,
the initial value for the action goal attributes must be set to
**None**.

## Bridge Server

This module launches a ROS node that blocks until a dedicated action
request is made by the robot, such as 'OpenDoor'. Once a request is
received, the node executes a callback function that monitors the
machine tool until it completes the requested action. The node then
returns the 'READY' handshake to the machine tool agent before
returning the action request result to the dedicated action client.

![](attachment:bridge_server_interaction.png)

Dedicated action server data items are specified by a configuration file
that must be included with the main program during execution. If this
file is not provided, the node will terminate with an error message
indicating the need for this file.

Command line example:



```
url:            string representing the url for the machine tool
url_port:       integer identifier for the url http port
machine_tool:   string representing the machine tool
xml_namespace:  string representing the XML namespace for the machine tool
```

7

### Bridge Server Configuration File

The bridge server configuration file is a YAML hash file that has two
sections, the first group contains several key:value pairs the are
required to obtain XML data via a HTTP connection. The second section
contains the ROS topics that will be published in a 2-level nested group
of key:value pairs.

The format for the first group is as follows:



```
url:            string representing the url for the machine tool
url_port:       integer identifier for the url http port
machine_tool:   string representing the machine tool
xml_namespace:  string representing the XML namespace for the machine tool
```

8

The key strings must not be changed, as they are hard coded into the
ROS-INDUSTRIAL bridge client node. Here is an example of this first
group (in the YAML file, do not use tabs, only spaces for indenting):



```
url:            string representing the url for the machine tool
url_port:       integer identifier for the url http port
machine_tool:   string representing the machine tool
xml_namespace:  string representing the XML namespace for the machine tool
```

9

The format for the second group is as follows:



```
url: localhost
url_port: 5000 
machine_tool: /cnc
xml_namespace: urn:mtconnect.org:MTConnectStreams:1.2
```

0

The string for the ROS package and the strings for the robot events must
already exist in the ROS package and robot configuration file,
respectively. Each package and action request XML tag must be unique. If
not there may be a violation of the action request sequence ('ACTIVE'
→ 'COMPLETE' → 'READY') with the machine tool resulting in sequence
errors. Here is an example of the second group showing two ROS packages
with unique robot action requests:



```
url: localhost
url_port: 5000 
machine_tool: /cnc
xml_namespace: urn:mtconnect.org:MTConnectStreams:1.2
```

1

## Bridge Library

Full API Reference for the
[Python bridge_library.py](http://www.ros.org/doc/fuerte/api/mtconnect_ros_bridge/html/namespacebridge__library.html)

This module contains functions utilized by the MTConnect to ROS bridge
nodes. It is required by all of the bridge nodes. The module contains
the following methods:

1\. obtain_dataMap

-   Reads the node configuration file into memory 1. check_connectivity
-   Verifies availability of the MTConnect Agent for the machine tool or
    robot 1. xml_get_response
-   Establishes a HTTP connection and returns a connection response 1.
    xml_components
-   Parses XML and returns a list of elements and the XML sequence
    number 1. set_goal
-   Captures the goal data from the XML and returns the goal element 1.
    add_event
-   Uses the MTConnect Adapter class to add process events 1.
    split_event
-   Converts the data item string from *!DataItem* to *data_item* 1.
    action_cb
-   Sets a value for an Adapter event 1. type_check
-   Verifies that the goal type matches a Python type (*to be
    augmented*)

### Method : obtain_dataMap

This function utilizes a Python option parser to determine the option
filename. Once the file name is obtained, the YAML file contents are
stored in a dictionary. The program terminates if the option file is not
available, or if it is in an incorrect YAML format.

This function does not take any arguments. The function returns a
dataMap object which is a dictionary of node configuration data.

### Method : check_connectivity

The purpose of this method is to determine if an HTTP connection is
available. It will continue to try to make a connection up to a user
specified time.

This method takes the following arguments:

-   **data**: data is a tuple containing the following parameters:

```{=html}
<!-- -->
```
-   tout: int, allowable time in seconds before the open request times
    out
-   url: string, url that will be opened
-   url_port: int, url port that will be concatenated to the url string

### Method: xml_get_response

This function determines if an HTTP connection can be made. If so, it
returns a response to a user specified "GET" request.

This method takes the following arguments:

-   **data**: data is a tuple containing the following parameters:

```{=html}
<!-- -->
```
-   url: string, url that will be opened
-   url_port: int, url port that will be concatenated to the url string
-   port: int, Adapter port used by MTConnect adapter.py module
-   conn: Python httplib.HTTPConnection
-   req: string, user specified selector url

The method returns:

-   response, "GET" response

### Method: xml_components

This method finds all elements in the updated XML. If an action goal is
required, the string acquired from the XML is parsed and returned with
the appropriate type.

For example, if the goal is "'ALUMINUM 6061-T6', 5.00, 2.50", the
method will convert this string into the following list \['ALUMINUM
6061-T6', 5.00, 2.50\] which contains the following types: \[str,
float, float\]

This method takes the following arguments:

-   xml: xml data, read from response.read()
-   ns: dictionary, xml namespace dictionary
-   tag_list: dictionary, xml tag stored as <tag:goal> or <tag:tag>
    pairs
-   \[optional\] get_goal: boolean, used when a action goal is required
-   \[optional\] action_goals: dictionary, stored action goals by
    xml_tag key

This method returns:

-   nextSeq, int, next XML sequence for streaming XML via longpull.py
-   elements, Python Element object
-   \[optional\] action_goals, dictionary of unchanged xml_tag:goal
    pairs
-   \[optional\] request_goal, dictionary of updated xml_tag:goal pairs

### Method: set_goal

This method extracts the machine tool request goal from the event tag
specified in the configuration file. For example, during !MaterialLoad
the request goal tag is Material which is an event that stores the
material specifications: material type, material length, material
diameter.

The method takes the following arguments:

-   tag: string of the event tag, i.e. *!MaterialLoad*
-   goals: dictionary of the goal (str):goal attributes (list of
    strings)
-   root: XML !ElementTree object that converted the XML in string
    format to an !ElementTree object
-   ns: dictionary, XML namespace dictionary
-   action_goals: dictionary, stored action goals by XML tag key

The method returns:

-   action_goals, dictionary, hash table of XML <tag:goal> pairs
-   **None** type if the action goal tag is not present in the XML

### Method: add_event

This method creates instances of the Adapter event class for each of the
XML tags provided to the method.

This method takes the following arguments: **\*data**: data is a tuple
containing the following parameters:

-   adapter: Adapter class object
-   tag_list: list of XML tags culled from node configuration file
-   di_dict: dictionary {string:string}, stored Adapter event class
    instances for each XML tag
-   init: boolean, user specified boolean to determine if the Adapter
    events must be initialized

### Method: split_event

This method converts a data item event string from *!CamelCase* to
*camel_case*.

This method takes and returns the following arguments:

-   xml_tag: string, event data item in *!DataItem* format
-   return: data_item, string, event data item in *data_item* format

### Method: action_cb

This method sets the value of an Adapter event. It is used to port XML
tag changes back to machine tool.

This method takes the following arguments: **\*data**: data is a tuple
containing the following parameters:

-   adapter: Adapter class object
-   di_dict: dictionary {string:string}, stored Adapter event class
    instances for each xml_tag
-   data_item: string, data item used to locate the Adapter event
-   state: string, event will be changed to this value

### Method: type_check

This function checks the goal types and converts them to Python standard
types. It then verifies if the goal type matches the type specified in
the goal message.

This method takes the following arguments:

-   goal_type: string, goal_type from goal msg._slot_types
-   request: varies, actual goal value that is a float, int, string,
    etc.

This method returns:

-   boolean: True for a match, False for an error
