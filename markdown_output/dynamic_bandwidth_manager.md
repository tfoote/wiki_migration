## Overview

Communication is an important component in multi-robots systems; system
performance may get affected when the number of robots or communication
channels increases. The **dynamic_bandwidth_manager** was designed to
provide a way of maximizing bandwidth usage in multi-robots systems. The
developed system prioritizes communication channels according to
environment events and offers greater bandwidth for the most important
channels.

The package architecture was divided in five libraries and one ROS node.
**DBMParam** is a library to help developers manipulate the parameters
of the module. **DBMRate** is a library that extends the function of the
rospy.Rate and helps to run loops at a dynamic frequency. Classes
**DBMSubscriber** and **DBMPublisher** inherits the characteristics of
rospy.Subscriber and rospy.Publisher. **DBMOptimizer** class helps
developers create new optimization strategies. Node
**default_optimizer** uses the class **DBMOptimizer** and solves a
linear optimization problem calculating new frequencies for each topic,
considering topic priority and message size.

![text describing image\|align=\"middle\"](attachment:ClassDiagram.png)

## Paper

A paper named *Dynamic Bandwidth Management Library for Multi-Robot
Systems* will be presented at IROS 2015.

## System Parameters

```clearsilver
param {
  no_header=True
  0.name = /dbm/topics
  0.type = list
  0.default = []
  0.desc = List with all managed topics.
}
param {
  no_header=True
  1.name = [topic_name]/dbm/frequency/current_value
  1.type = double
  1.default = 10.0
  1.desc = Frequency current value for a topic [topic_name]
}
param {
  no_header=True
  2.name = [topic_name]/dbm/frequency/min
  2.type = double
  2.default = 1.0
  2.desc = Minimum frequency for a topic [topic_name]
}
param {
  no_header=True
  3.name = [topic_name]/dbm/frequency/max
  3.type = double
  3.default = 10.0
  3.desc = Maximum frequency for a topic [topic_name]
}
param {
  no_header=True
  4.name = [topic_name]/dbm/priority
  4.type = double
  4.default = 1.0
  4.desc = Event-based priority for topic [topic_name]
}
param {
  no_header=True
  5.name = [topic_name]/dbm/message_size_in_bytes
  5.type = double
  5.default = 0.0
  5.desc = Message length for a topic [topic_name]
}
param {
  no_header=True
  6.name = /dbm/max_bandwidth_in_mbit
  6.type = double
  6.default = 10.0
  6.desc = Total network bandwidth
}
param {
  no_header=True
  7.name = /dbm/max_bandwidth_utilization
  7.type = double
  7.default = 100.0
  7.desc = Percentage of available bandwidth for an application (in range [0 : 100])
}
param {
  no_header=True
  8.name = /dbm/optimization_rate
  8.type = double
  8.default = 1.0
  8.desc = Optimization frequency rate
}
param {
  no_header=True
  9.name = /dbm/manage_local_subscribers
  9.type = bool
  9.default = False
  9.desc = Configure if the package should manage topics that has only subscribers running in local machines
}
```

## Basic Usage

### Writing a Simple Publisher using dynamic_bandwidth_manager package

```python
#!/usr/bin/env python
# license removed for brevity
import rospy
import dynamic_bandwidth_manager
from rescue_app.msg import RescueInfo

# Returns the message to be published
def getMessage():
    return hello_str = "hello world %s" % rospy.get_time()

def run():
    # Minimum frequency of 10hz and maximum frequency of 24hz
    pub = dynamic_bandwidth_manager.DBMPublisher(
        'chatter', RescueInfo, 10, 24)
    rospy.init_node('talker', anonymous=True)

    # Starts message publish with the frequency stored in the Parameter Server
    pub.start(getMessage)

if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInterruptException:
        pass
```

### Running optimization node

To create the independence of the optimization algorithm used by the
library, a module that takes care of the bandwidth optimization was
created. **DBMOptimizer** is a ROS library that helps the development of
more complex strategies for the optimization problem. It runs every time
as \`/dbm/optimization_rate parameter\` and assigns the result of the
calculated frequencies in parameter
\`\[topic_name\]/dbm/frequency/current_value\`. Using **DBMOptimizer**,
\`default_optimizer\` node solves a linear optimization problem and sets
the calculated frequency for each topic considering the priorities (see
\`\[topic_name\]/dbm/priority\` parameter).

### Writing new optimization strategies

Using **DBMOptimizer** it\'s possible create new optimization
strategies. Code below presents a example of how create a node with a
optimization algorithm.

```python
#!/usr/bin/env python

import rospy
import dynamic_bandwidth_manager
import pulp
import numpy as np

def optimize(managed_topics):
    # Makes the optimization and returns a dictionary of type
    # [topic_name:frequency_value] (the managed_topics parameter has a list of topics
    # that must be taken into consideration in the optimization)

if __name__ == '__main__':
    try:
        rospy.init_node('default_optimizer', anonymous=True)
        optimizer = dynamic_bandwidth_manager.DBMOptimizer(optimize)
        optimizer.start()

    except rospy.ROSInterruptException: pass
```

## Managing topics on same machine

If one of these topics has its rate controlled by the library, it is
treated as a managed channel. But the question is how to manage channels
that just send messages to other nodes that are running in the same
machine? In these cases, the topic has no impact in the bandwidth and
should be ignored when optimization is running. Thus, the
\`DBMOptimizer\` decides which topics should be managed in a specific
time verifying if there are external nodes communicating with the topic.
If there is no external node subscribing to the topic, it is not treated
as a managed channel and has its frequency adjusted to its maximum
value.

Another important question is when the topic has subscribers in nodes
running in external machines and in the same machine of the topic. If
the system limits the global sampling and publishing rate for that
topic, this would mean that a local process, not subject to the same
bandwidth limitations, would not get the full rate data from the topic.
To solve this problem, the system creates two topics for each managed
topic: a full rate topic (\`\[topic_name\]\`) and a managed rate topic
(\`\[topic_name\]/managed\`). Thus, when a client of the topic is
running in the same machine of the managed topic, it subscribes in the
full rate topic. However, if the client is running in an external
machine, it is subscribed in the managed rate topic. So, the full rate
topic stream would still be available for local processing/logging.

![text describing image\|align=\"middle\"](attachment:DBMScheme.png)
