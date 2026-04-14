The \`lama_jockeys\` package provides base class for Learning,
Localizing, Navigating, and custom jockeys for the Large Maps Framework
([LaMa](Large Maps Framework)). A jockey provides a specific capability
to the robot. These modules are called jockeys since, in a certain
sense, they are riding the robot. It means that these modules have
direct access to the robot hardware and are able to control the robot\'s
actuators, to read its sensors and to process raw data gathered from its
sensors.

The jockeys are \`actionlib\` servers. The \`lama_jockeys\` packages
provides standard action messages for Learning, Localizing, and
Navigating jockeys.

## Navigating Jockeys

A navigating jockey takes care of traversing edges with respect to a
specific procedural knowledge. It guides the robot along the given edge
and determines the end of this edge. If it is possible to interrupt the
execution of the navigating algorithm, the navigating jockey is call
interruptible. This property allows to restart it later from a slightly
different position while the algorithm still keeps the capability to
navigate to the original target vertex.

A navigating Jockey has two different subtypes: memory-less and
memory-based.

### Memory-less Navigating Jockey

A memory-less jockey uses a reactive navigation strategy. The procedural
knowledge represented by a reactive navigating strategy has a small or
inexistent use of database data. Only the information needed to
distinguish outgoing edges from each other is stored in the map.

The reactive algorithm computes the control commands directly from the
sensor input and has no persistent internal state. Therefore, a
memory-less navigating jockeys are often interruptible.

The main advantage of reactive navigation is the ability to traverse an
unknown edge. It allows to discover new locations, which are the target
vertex of these edges. Therefore the memory-less Jockeys are used mainly
during the exploration of the environment.

### Memory-based Navigating Jockey

A memory-based jockey needs the data part of the procedural knowledge
about the edge for proper operation. The data for the memory-based
jockeys are typically more complex than for the memory-less ones. These
data (edge descriptor) are stored in the map and must be inserted into
the map by a coupled learning jockey in advance. Therefore, a
memory-based navigating jockey can guide the robot along previously
visited edges only.

A memory-based navigation should be more precise and repeatable than a
reactive one. Such jockey can determine the failure of the navigation
and report it to the higher-level control module. In addition, the
jockey can estimate in advance the possibility of failure according to
the given edge descriptor.

Moreover, such jockey can provide the measurement of similarity of
appropriate edges.

## Learning Jockeys

A learning jockey is usually tightly coupled with a particular
memory-based navigating jockey which utilizes the procedural knowledge
of the same type. Such a jockey produces the procedural knowledge by
gathering the information while a robot can be driven by another
navigating jockey (typically memory-less), as a learning jockey is not
supposed to control the robot actuators while traversing an edge.

The gathered procedural knowledge is divided into algorithmic and data
parts. The data part is stored in the map as edge descriptor. This edge
descriptor can be utilized by a memory-based navigating Jockey later on.

It is possible, that a learning jockey needs to control the robot
actuator occasionally, in order to increase the performance, get more
data from the sensor, get more time for data processing, or handle
errors. In this case, the learning jockey can request the high-level
control module to interrupt the running navigating jockey. If the
navigating jockey is interruptible, the high-level control module
suspends the navigating jockey and grants the control to the learning
jockey. The original navigating jockey is reactivated as soon as the
learning jockey achieves its goal and notifies the high-level controller
that the reason for interruption disappeared.

A learning jockey extends an existing edge with new procedural
knowledge, which can then be used to traverse the edge. This property
allows to build rich but unified spatial representation for different
types of robots equipped with wide range of sensors. Such a map is
suitable for a heterogeneous robotic team, as it allows easy sharing of
the spatial knowledge among team members.

## Localizing Jockeys

Localizing jockey are associated to specific types of vertex descriptors
and specific sensors. Such jockeys process the sensor data into a vertex
descriptor. The resulting descriptor is stored in the map using the
[lama_interfaces](map interface). Different sensors require different
localizing jockeys for handling specific hardware and processing data,
nevertheless these jockeys can utilize the same map interface and
therefore share the stored information. On the other hand, localizing
jockeys with different algorithms can share the same sensors.

When the robot arrives to a vertex, the jockey gathers information about
the surrounding environment, computes and stores specific descriptors
into the map and possibly discovers outgoing edges from the current
vertex. Different localizing jockeys can produce different vertex
descriptions and also discover different outgoing edges. A localizing
jockey is able to distinguish vertices from each other and compare the
actual vertex with other vertices already stored in the map. The result
of its action is to give the probabilities of being in some of the
previously visited vertices. This behavior is used for global
localization and loop-closing.

In addition, a localizing jockey can estimate the robot relative
position in the vertex local frame of reference if the stored descriptor
has the form of a local metric map. This ability is crucial if the robot
has to interact with the environment.

## Custom Jockeys

/\* TODO: add links to the API \*/ In the case that the functionalities
of a jockey cannot be described by the predefined actions
\`Navigate.action\`, \`Learn.action\`, and \`Localize.action\`, the
jockey can be based on the \`lama_jockeys::Jockey\` class instead. Basic
map and jockey functionalities are already implemented.

## Implementation

The \`lama_jockeys::Jockey\` provides the mechanisms to interfere with
the map in the form of the member variable \`map_agent\_\`. For example,
to get the vertex with id 243 from the map, one can write:
```cplusplus
#include <lama_jockeys/jockey.h>

lama_interfaces::ActOnMap srv;
srv.request.action = lama_interfaces::ActOnMapRequest::PULL_VERTEX;
srv.request.object.id = 243;
ROS_DEBUG("Calling action PULL_VERTEX for vertex %d", 243);
if (!map_agent_.call(srv))
{
  ROS_ERROR("Failed to call map agent");
  /* throw an error or abort the action: "server_.setAborted();" */
  return;
}
ROS_DEBUG("Received response PULLL_VERTEX");
lama_interfaces::LamaObject vertex = srv.response.objects[0];
```

The three subclasses \`lama_jockeys::LearningJockey\`,
\`lama_jockeys::LocalizingJockey\`, and
\`lama_jockeys::NavigattingJockey\` handle reception of the goal, which
is then stored in the \`goal\_\` member variable. Upon goal reception,
one specific function is called. Most of these functions are implemented
are pure virtual method, so that the jockey implementer must only define
these methods to have a working jockey. A default implementation is
provided for the common actions \`\"INTERRUPT\"\`
(\`\"onInterrupt()\"\`) and \`\"CONTINUE\"\` (\`\"onContinue()\"\`),
they only manage to pause the stop watch which is otherwise running when
an action is running.

### Learrning Jockeys

The user must implement \`\"onStartLearn()\"\` and
\`\"onStopLearn()\"\`.

### Localizing Jockeys

The user must implement \`\"onGetVertexDescriptor()\"\`,
\`\"onGetEdgesDescriptors()\"\`, \"\`onLocalizeInVertex()\`\",
\`\"onLocalizeEdge()\`\", \`\"onGetDissimilarity()\"\`.

### Navigating Jockeys

The user must implement \`\"onTraverse()\"\` and \`\"onStop()\"\`.
