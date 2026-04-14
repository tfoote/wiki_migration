## Rxgraph+

rxgraph + hierachical clustering

With standard rxgraph, you often get plagued with lots of nodes on your
plot that are irrelevant to your task at hand.

<attachment:base_quiet.png> <attachment:base_topics.png>

By loading
[parameters](http://wu-robotics.googlecode.com/svn/branches/stable/wu_ros_tools/rxgraphplus/pr2.yaml)
into the parameter server (namespace /rxgraph/config/), rxgraphplus will
create subgraphs for the specified components and hide many of the
unnecessary components.

<attachment:PR2_QUIET.png> <attachment:PR2_TOPICS.png>

With Nav Stack
[parameters](http://wu-robotics.googlecode.com/svn/branches/stable/wu_ros_tools/rxgraphplus/nav_stack.yaml)

<attachment:NAV.png>
