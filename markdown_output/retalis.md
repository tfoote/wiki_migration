## Description

The Retalis language (Etalis for robotics) supports a high-level and an
efficient implementation of a large variety of robotic sensory data
processing and management functionalities.

-   Publications:
-   A journal paper is being reviewed.
-   Older publications:
-   P. Ziafati, M. Dastani, J-J. Meyer, L. van der Torre, Reasoning on
    Robot Knowledge from Discrete and Asynchronous Observations, AAAI
    Spring Symposium, Stanford, 2014.
-   P. Ziafati, Y. Elrakaiby, L. van der Torre, H. Voos, M. Dastani,
    J-J. Meyer, M. Van Zee, Event-processing in autonomous robot
    programming, AAMAS, 2013

```{=html}
<!-- -->
```
-   Supported functionalities
-   Processing flow of data on the fly (by integrating the
    [ELE  language for complex event processing](http://code.google.com/p/etalis/))
-   filtering, transformation, synchronization
-   temporal and logical reasoning
-   Managing data in knowledge base and querying
-   selective recording of data
-   active memories
-   prunning out-dated data
-   state-based representation of knowledge based on discrete
    observations
-   synchronization of queries over asynchronous reception of data
-   logical reasoning
-   Efficient implementation of the provided functionalities (see the
    Performance section)
-   New C++ interface, significantly improving the performance over the
    previous Java interface
-   An example with rosbag files
-   coordinate transformation for NAO robot

## Installation

It is assumed that the \"retalis\" package has been downloaded to the
\"catkin_ws/src\" folder

Step 1: install OpenGL Mathematics (GLM)

-   1- sudo apt-get install libglm-dev

Step 2: install SWI-PL as a shared library

-   1- Download pl source code (6.2.2. for me) from
    <http://www.swi-prolog.org/download/stable>
-   2- Extract the tarball and edit the build.templ file as follows:
-   Set PREFIX=/usr
-   Set SUDO=\"sudo\"
-   Disable some library that might cause problem by uncommenting
-   export DISABLE_PKGS=\"ssl xpce zlib\"
-   Uncomment the
-   EXTRACFG+=\" \--enable-shared\"

```{=html}
<!-- -->
```
-   3- Run build.templ. (as root)
-   4- Make sure libswipl.so has been created. In my system, it is found
    at /usr/lib/swipl-6.2.2/lib/i686-linux/libswipl.so

Step 3: install Retalis as follows

-   1- In the CMakeLists.txt file, change
    \"/usr/lib/swipl-6.6.6/include\" and
    \"/usr/lib/swipl-6.6.6/lib/x86_64-linux\" to refer to the include
    and lib folders of your SWI-PL installtion, respectively
-   2- catkin_make (in your catkin workspace)
-   3- roscd retalis
-   4- In the install.py file, change \'/home/robolab/catkin_ws\' and
    \'/usr/lib/swipl-6.6.6/lib/x86_64-linux\' to refer to the catkin
    workspace and the lib folder of your SWI-PL installation,
    respectively Step 4- Run the install.py file as root (you might
    first need to make the install.py file executable by: sudo chmod +x
    install.py)

## Execution

After you program retalis as described below, rune it by:

```shell
roslaunch retalis retalis.launch
```

### Programming

Retalis is programmed using three files, located in the
application_source folder of the retalis package:

-   pub_sub.xml : subscribes retalis to ros topics. It also specifies
    the message types of topics to which retalis may publish messages.
-   goalPredicates.txt: creates a set of subscriptions and memory
    instances. A subscription subscribes a ros topic to retalis by a
    policy to selectively send data to that topic. A memory instance
    selectively records and maintains data in the retalis knowledge base
    based on a policy
-   eventRules.txt: specifies rules to perform complex event-processing
    functionalities and to query the retalis knowledge base

### Nodes (Run-Time Configuration)

```clearsilver
node.0{
name = retalis
desc = This node implements main functionalities.
srv{
0.name = add_output_subscription
0.type = retalis/AddOutputSubscription
0.desc = adds a subscription
1.name = delete_output_subscription
1.type = retalis/DeleteOutputSubscription
1.desc = cancels a subscription
2.name = add_memory
2.type = retalis/AddMemory
2.desc = adds a memory instance
3.name = delete_memory
3.type = retalis/DeleteMemory
3.desc = deletes a memory instance
}
}
node.1{
name = retalis_ros_interface
desc = This node automates the conversion between ros messages and retalis events
srv {
0.name = add_input_subscription
0.type = retalis/DeleteInputSubscription
0.desc = subscribes retalis to a ros topic
1.name = delete_input_subscription
1.type = retalis/DeleteInputSubscription
1.desc = unsubscribe retalis from a ros topic
}
}
```

## Tutorials

This section describes retalis using two examples.

### Example 1 (coordinate transformation for NAO robot)

The usecase is to position the recognized objects in the world
coordination frame and reason on high-level events occurring in the
environment.

#### Setup

-   rosbags can be downloaded from
    [nao1.bag](https://www.dropbox.com/s/q79gwvvdomb7nm4/1.bag?dl=0) and
    [nao2.bag](https://www.dropbox.com/s/3fx4f93kc0s0fdb/2.bag?dl=0). To
    run the bagfiles, you need to have
    [face_recognition](http://wiki.ros.org/face_recognition),
    [ar_pose](http://wiki.ros.org/ar_pose) and
    [NAO Messages](http://wiki.ros.org/naoqi_msgs) installed to have
    required message types.
-   input to retalis:
-   recognized objects (ar_pose markers) positioned relative to the
    robot\'s top camera.
-   recognized faces
-   transformation among coordinate frames
-   output from retalis:
-   position of objects in the environment
-   events about situations of the environment

#### Input from ROS (see pub_sub.xml)

The following clause in pub_sub.xml subscribes retalis to the tf topic:

```shell
< subscribe_to   name="tf"   msg_type="tf/tfMessage"  />
``` Similarly, the following clauses in pub_sub.xml
subscribe retalis to messages of recognized faces and objects.

```shell
<subscribe_to name="face_recognition/feedback" msg_type="face_recognition/FaceRecognitionActionFeedback"/>
<subscribe_to name="ar_pose_marker" msg_type="ar_pose/ARMarkers"/>
``` Messages received by retalis from the
subscribed topics are automatically converted to events. For example,
the following message of type \'\'\'\'\'tf/tfMessage\'\'\'\'\'

![A message of type tf/tfMessage\|width=\"300\"](attachment:tfexample.png)

is converted to the following event:

![the corresponding event of type tf\_\_0\_\_tfMessage\|width=\"750\"](attachment:tfevent.png)

Events are time-stamped according to header times of ros messages. If a
message does not have a header, it is time stamped with
\'\'\'\'\'ros::Time::now()\'\'\'\'\'. The format of time-stampes are
\'\'\'\'\'datime(Y,M,D,H,Min,S,Counter)\'\'\'\'\' where
\'\'\'\'\'Counter\'\'\'\'\' encodes nanoseconds since seconds (i.e.
stamp.nsec in ros messages). For example, the above
\'\'\'\'\'tf/tfMessage\'\'\'\'\' message contains a list of
\'\'\'\'\'geometry_msgs/TransformStamped\'\'\'\'\' messages (only one
here). While each \'\'\'\'\'geometry_msgs/TransformStamped\'\'\'\'\'
message is time-stamped, the \'\'\'\'\'tf/tfMessage\'\'\'\'\' itself
does not have a header. Therefore, the corresponding event is stamped
with the current time.

#### Event-Processing (see EventRules.txt)

The following rule calls the \'\'\'\'\'split_tf\'\'\'\'\' function for
every \'\'\'\'\'tf`__0__`tfMessage\'\'\'\'\' event received by retalis.

```shell
null_event do split_tf(Transforms)    <- tf__0__tfMessage(Transforms).
``` . This function is implemented as a prolog rule
in eventRules.txt. It splits the \'\'\'\'\'Transforms\'\'\'\'\', its
input list of \'\'\'\'\'geometry_msgs/TransformStamped\'\'\'\'\'
messages, into the elements and generates a new \'\'\'\'\'tf\'\'\'\'\'
event for each. Each \'\'\'\'\'tf\'\'\'\'\' event is time-stamped
according to header file of the corresponding
\'\'\'\'\'geometry_msgs/TransformStamped\'\'\'\'\' message. For
instance, when retalis receives the above
\'\'\'\'\'tf`__0__`tfMessage\'\'\'\'\' event (in section 4.1.2), this
rule generates the following event:

```shell
tf('“/odom”', '“/base_link”',[0,-0.01,0.1], [0.05,0.008,-0.02,0.9])
``` The event is time-stamped with (1413748205,
981209993) represented in the datime format.

Each \'\'\'\'\'ar_pose/ARMarkers\'\'\'\'\' message from
\'\'\'\'\'ar_pose\'\'\'\'\' contains a list of recognized objects, each
represented by a \'\'\'\'\'ar_pose`__0__`ARMarker\'\'\'\'\' message. The
following rule generates a separate event for each object.

```shell
split_ar_pose(Markers)  <- ar_pose__0__ARMarkers(Header,Markers).
``` . Such an event is of the following form

```shell
ar_marker(Seq,MarkerName,[[P1,P2,P3],[Q1,Q2,Q3,Q4]],Sec,NSec)
``` where \'\'\'\'\'Name\'\'\'\'\' represents a
recognized object and \'\'\'\'\'(Sec,NSec)\'\'\'\'\' encodes the time of
recognition. This time corresponds to the time of taking the picture at
which the object was recognized. This time is taken from the header file
of the corresponding \'\'\'\'\'ar_pose`__0__`ARMarker\'\'\'\'\' message.
The events is also time stamped with \'\'\'\'\'(Sec,NSec)\'\'\'\'\'.

Retalis integrates the
\'[ELE  language of the Etalis system for complex event processing](http://code.google.com/p/etalis/).
\'\'\'\'\'ELE\'\'\'\'\' supports temporal and logical reasoning on flow
of events. Please see <http://code.google.com/p/etalis/> for
publications and for examples of rules implementing various
event-processing functionalities.

#### Memorization (see goalPredicates.txt)

The following clause creates a memory instance.

```shell
memorize(tf('"/odom"', '"/base_link"', V, Q),[], tf(V, Q), odom_base,  2500)
``` This memory instance keeps the history of
events of the form \'\'\'\'\'tf(
`'"/odom"','"/base_link"'`,V,Q)\'\'\'\'\', specified by the first
argument. The second argument specifies a list of conditions, being
empty here. A memory instance only records events that satisfy the
conditions. The third argument specifies the format for recording
events. The fourth argument is the Id of the memory instance. The last
argument is the size. Only the last 2500 events of the given form are
maintained by this memory instance.

The \'\'\'\'\'tf(`'“/odom”', '“/base_link”'}}`,\[0,-0.01,0.1\],
\[0.05,0.008,-0.02,0.9\])\'\'\'\'\' event from Section 4.1.3 matches
this memory instance. This events is recorded by this memory instance as
\'\'\'\'\'tf(\[0,-0.01,0.1\], \[0.05,0.008,-0.02,0.9\])\'\'\'\'\'.

#### Querying (see eventRules.txt)

We saw in Section 4.1.3 that the \'\'\'\'\'split_tf\'\'\'\'\' and
\'\'\'\'\'split_ar_pose\'\'\'\'\' functions are implemented as Prolog
clauses. The \'\'\'\'\'eventRules.txt\'\'\'\'\' file can include an
arbitrary Prolog program to encode a domain knowledge. We also saw in
Section 4.1.4 that how memory instances are used to maintain histories
of events

The Prolog program in \'\'\'\'\'eventRules.txt\'\'\'\'\' together with
the the dynamic knowledge maintained by memory instances represent a
Prolog-based knowledge base. This knowlede base can be queries by
event-processing rules, for instance, as in Section 4.1.3. It can be
also queried directly by a ros service (in our `ToDo` list).

Queries to the knowledge base are normal Prolog queries, but with two
main differences, described in the following sections.

#### Accessing Memory Instances (see eventRules.txt)

A memory instance is accessed by its Id. There are three types of
access:

-   sequential access is using the
    \'\'\'\'\'access_mem(Id,`Event`,\[T1,T2\])\'\'\'\'\' term. Given an
    \'\'\'\'\'Id\'\'\'\'\' of the memory instance, this term backtracks
    over the events recorded in the memory instance. Backtracking is in
    the decreasing order of events\' occurrence times: the last recorded
    event is accessed first. In backtracking, the variables
    \'\'\'\'\'Event\'\'\'\'\' and \'\'\'\'\'\[T1,T2\]\'\'\'\'\' are
    unified with events and their ocurrence times, maintained in the
    memory instace. An event orrurrence time is a time interval
    \'\'\'\'\'\[T1,T2\]\'\'\'\'\'. For atomic events,
    \'\'\'\'\'T1\'\'\'\'\' is equal to \'\'\'\'\'T2\'\'\'\'\'.
-   previous access is using the \'\'\'\'\'prev(Id, Event, T1, T2,
    T)\'\'\'\'\' term. Given an \'\'\'\'\'Id\'\'\'\'\' and a time point
    \'\'\'\'\'T\'\'\'\'\', the last event occurring before
    \'\'\'\'\'T\'\'\'\'\', recorded in the memory instance
    \'\'\'\'\'Id\'\'\'\'\', is accessed. The variables
    \'\'\'\'\'Event\'\'\'\'\' and \'\'\'\'\'\[T1,T2\]\'\'\'\'\' are
    unified with that event and its occurrence time.
-   next access is using the \'\'\'\'\'next_inf(Id, Event, T1, T2,
    T)\'\'\'\'\'. It accesses the first event, occurring after time
    \'\'\'\'\'T\'\'\'\'\'. There are other types of next access too. For
    example, the \'\'\'\'\'next(Id,Event,T1,T2,Ts,Te)\'\'\'\'\' term
    accesses the first event occurring during the time interval
    \'\'\'\'\'\[Ts,Te\]\'\'\'\'\'.

An example of using \'\'\'\'\'prev\'\'\'\'\' and
\'\'\'\'\'next\'\'\'\'\' terms is in implementation of the
\'\'\'\'\'interpolate_tf(Id,T,Pos)\'\'\'\'\' function, in the
eventRules.txt. The input values to this function is the
\'\'\'\'\'Id\'\'\'\'\' of a memory instance, keeping the history of some
\'\'\'\'\'tf\'\'\'\'\' events, and a time point. The
\'\'\'\'\'tf\'\'\'\'\' events represent observations of the
transformation between two coordinate frames over time. From these
observations, this function interpolates the transformation between the
frames at time \'\'\'\'\'T\'\'\'\'\'. This is implemented as follows.
The last observation before \'\'\'\'\'T\'\'\'\'\' and the first
observation after \'\'\'\'\'T\'\'\'\'\' are found using the
\'\'\'\'\'prev\'\'\'\'\' and \'\'\'\'\'next\'\'\'\'\' terms. Then the
position is linearly interpolated by making a function call to the
[OpenGL Mathematics](http://glm.g-truc.net/0.9.5/index.html) library
that has been integrated with retalis.

The
\'\'\'\'\'transform_marker(`RelativePos`,Time,`AbsolutePose`)\'\'\'\'\'
function in eventRules.txt uses the \'\'\'\'\'interpolate_tf\'\'\'\'\'
function to position an object in the world reference frame. Given
\'\'\'\'\'`RelativePos`\'\'\'\'\', the position of an object relative to
the camera at time \'\'\'\'\'Time\'\'\'\'\', this function computes
\'\'\'\'\'`AbsolutePose`\'\'\'\'\', the position in the world, as
follows. First, it changes the time format from ros time to datime.
Then, it interpolates the transformation between
\'\'\'\'\'/odom-to-/base_link\'\'\'\'\',
\'\'\'\'\'base_link-to-torso\'\'\'\'\',
\'\'\'\'\'torso-to-Neck\'\'\'\'\', \'\'\'\'\'Neck-to-Head\'\'\'\'\' and
\'\'\'\'\'Head-to-`CameraTop`\_frame\'\'\'\'\' at the time
\'\'\'\'\'Time\'\'\'\'\'. Third, it applies these transformations on the
\'\'\'\'\'`RelativePos`\'\'\'\'\' by making a function call to the
[OpenGL Mathematics](http://glm.g-truc.net/0.9.5/index.html) library. It
is assumed that the \'\'\'\'\'/odom\'\'\'\'\' frame is aligned with the
world reference frame.

#### Query Synchronization (see eventRules.txt)

We saw in Section 4.1.6 that how calling
\'\'\'\'\'interpolate_tf(odom_base,t,Pos)\'\'\'\'\' function
interpolates the position between the \'\'\'\'\'/odom\'\'\'\'\' and
\'\'\'\'\'/base_link\'\'\'\'\' coordination frames at time
\'\'\'\'\'t\'\'\'\'\'. This function uses \'\'\'\'\'next\'\'\'\'\' and
\'\'\'\'\'prev\'\'\'\'\' terms to access the first and the last
observations after and before \'\'\'\'\'t\'\'\'\'\', respectively. To
interpolate the position at \'\'\'\'\'t\'\'\'\'\', the position should
have been observed, at least once, after \'\'\'\'\'t\'\'\'\'\'. The
observations, \'\'\'\'\'tf/tfMessage\'\'\'\'\' messages here, are
received asynchronously. Therefore, the
\'\'\'\'\'interpolate_tf(odom_base,t,Pos)\'\'\'\'\' function should be
evaluated only after the \'\'\'\'\'odom_base\'\'\'\'\' memory instance
has been updated with an event occurring after \'\'\'\'\'t\'\'\'\'\'.
This is realized in retalis using a synchronized event, as follows.

The \'\'\'\'\'synchronized(Event,Query,`SynchConditions`)\'\'\'\'\'
function, performs the \'\'\'\'\'`Query`\'\'\'\'\', when the
\'\'\'\'\'`SynchConditions`\'\'\'\'\' are satisfied and then generate
the \'\'\'\'\'`Event`\'\'\'\'\'. Consider the following clause from
eventRules.txt:

```shell
syncronized(
    geometry_msgs__0__PoseStamped(std_msgs__0__Header(Seq, [Sec,NSec], Name),geometry_msgs__0__Pose(geometry_msgs__0__Point(P11,P12,P13),geometry_msgs__0__Quaternion(Q11,Q12,Q13,Q14))),
    transform_marker(RelPose,[Sec,NSec],[[P11,P12,P13],[Q11,Q12,Q13,Q14]]),
        [[odom_base,Z],[base_torso,Z],[torso_neck,Z],[neck_head,Z],[head_cam,Z]]
          )
    <- ar_marker(Seq,Name,RelPose,Sec,NSec) where (Z is Sec + (NSec * 0.000000001) ).
``` This rule computes the position of recognized
markers in the world and is read as follows. For each
\'\'\'\'\'ar_marker\'\'\'\'\' event, specified in line 6, the position
is computed by calling the \'\'\'\'\'transform_marker\'\'\'\'\'
function, as in line 3. After computing the position, an event of the
following form is generated, specified in line 2:

```clearsilver
node.0{
name = retalis
desc = This node implements main functionalities.
srv{
0.name = add_output_subscription
0.type = retalis/AddOutputSubscription
0.desc = adds a subscription
1.name = delete_output_subscription
1.type = retalis/DeleteOutputSubscription
1.desc = cancels a subscription
2.name = add_memory
2.type = retalis/AddMemory
2.desc = adds a memory instance
3.name = delete_memory
3.type = retalis/DeleteMemory
3.desc = deletes a memory instance
}
}
node.1{
name = retalis_ros_interface
desc = This node automates the conversion between ros messages and retalis events
srv {
0.name = add_input_subscription
0.type = retalis/DeleteInputSubscription
0.desc = subscribes retalis to a ros topic
1.name = delete_input_subscription
1.type = retalis/DeleteInputSubscription
1.desc = unsubscribe retalis from a ros topic
}
}
```0 Such a \'\'\'\'\'`PoseStamped`\'\'\'\'\' event
encodes the marker\'s name, its position in the world and the time of
recogntion. The \'\'\'\'\'`SyncConditions`\'\'\'\'\' are the followings,
specified in line 4:

```clearsilver
node.0{
name = retalis
desc = This node implements main functionalities.
srv{
0.name = add_output_subscription
0.type = retalis/AddOutputSubscription
0.desc = adds a subscription
1.name = delete_output_subscription
1.type = retalis/DeleteOutputSubscription
1.desc = cancels a subscription
2.name = add_memory
2.type = retalis/AddMemory
2.desc = adds a memory instance
3.name = delete_memory
3.type = retalis/DeleteMemory
3.desc = deletes a memory instance
}
}
node.1{
name = retalis_ros_interface
desc = This node automates the conversion between ros messages and retalis events
srv {
0.name = add_input_subscription
0.type = retalis/DeleteInputSubscription
0.desc = subscribes retalis to a ros topic
1.name = delete_input_subscription
1.type = retalis/DeleteInputSubscription
1.desc = unsubscribe retalis from a ros topic
}
}
```1 These conditions specify that the
\'\'\'\'\'transform_marker\'\'\'\'\' function should be evaluated, only
after all \'\'\'\'\'odom_base\'\'\'\'\', \'\'\'\'\'base_torso\'\'\'\'\',
\'\'\'\'\'torso_neck\'\'\'\'\', \'\'\'\'\'neck_head\'\'\'\'\' and
\'\'\'\'\'head_cam\'\'\'\'\' memory instances have been updated, at
least once, with events occurring after time \'\'\'\'\'Z\'\'\'\'\'. The
time \'\'\'\'\'Z\'\'\'\'\' is the time of recognition of the marker.

Retalis performs the synchronization of events in an event-driven and
efficient way. The generation of a synchronized
\'\'\'\'\'Event\'\'\'\'\' is posponed, until the
\'\'\'\'\'syncConditions\'\'\'\'\' are satisfied. Postponing an event
does not postpone the generation of other events and postponed events
are generated as soon as necessary conditions are met.

#### Subscription (see goalPredicates.txt)

The following clause in goalPredicates.txt creates a subscription:

```clearsilver
node.0{
name = retalis
desc = This node implements main functionalities.
srv{
0.name = add_output_subscription
0.type = retalis/AddOutputSubscription
0.desc = adds a subscription
1.name = delete_output_subscription
1.type = retalis/DeleteOutputSubscription
1.desc = cancels a subscription
2.name = add_memory
2.type = retalis/AddMemory
2.desc = adds a memory instance
3.name = delete_memory
3.type = retalis/DeleteMemory
3.desc = deletes a memory instance
}
}
node.1{
name = retalis_ros_interface
desc = This node automates the conversion between ros messages and retalis events
srv {
0.name = add_input_subscription
0.type = retalis/DeleteInputSubscription
0.desc = subscribes retalis to a ros topic
1.name = delete_input_subscription
1.type = retalis/DeleteInputSubscription
1.desc = unsubscribe retalis from a ros topic
}
}
```2 The subscription subscribes the topic
\'\'\'\'\'marker1\'\'\'\'\' to the \'\'\'\'\'`PoseStamped`\'\'\'\'\'
events in which \'\'\'\'\'Name\'\'\'\'\' is
\'\'\'\'\'`'"4x4_1"'`\'\'\'\'\'. Such events are generated by the
synchronized rule, presented in Section 4.1.7. They contain the position
of the marker \'\'\'\'\'4x4_1\'\'\'\'\' in the world coordination frame.
The id of the subscription is \'\'\'\'\'m1\'\'\'\'\' which can be used
to cancel the subscrition at any time.

## Performance Evaluation

This section evaluates the performance of retalis on the NAO application
described in Example 1 (Section 4.1). Retalis is executed on an XPS
Intel Core i7 CPU@ 2.1 GHz x 4 laptop running ubuntu 12.04 LTS. The
performance is evaluated by measuring the CPU time used by the retalis
program. In the following graphs, the vertical axis represents the
percentage of CPU time and the horizontal axis represents the running
time in seconds. The usage of the CPU time is logged every second and is
plotted using \"gnuplot smooth bezier\".

The NAO application includes the following tasks:

-   On-flow processing: \'\'\'\'\'tf`__0__`tfMessage\'\'\'\'\' events
    are split and transformed into \'\'\'\'\'tf\'\'\'\'\' events, each
    containing data about the transformation between a single pair of
    coordination frames (see Section 4.1.3). In addition,
    \'\'\'\'\'ar_pose`__0__`ARMarkers\'\'\'\'\' events are split into
    \'\'\'\'\'ar_marker\'\'\'\'\' events, each containing data of the
    recognition of a single object. The data about transformation among
    pairs of coordinate frames are published with frequencies from 8 to
    50 hertz. There are in average 7 objects perceived per second. In
    total, retalis generates and processes about 1900 events per second.
-   Memorizing and forgetting: there are 5 memory instances of size
    2500, recording the transformation between
    \'\'\'\'\'/odom\'\'\'\'\'-to-\'\'\'\'\'/base_link\'\'\'\'\',
    \'\'\'\'\'base_link\'\'\'\'\'-to-\'\'\'\'\'torso\'\'\'\'\',
    \'\'\'\'\'torso\'\'\'\'\'-to-\'\'\'\'\'Neck\'\'\'\'\',
    \'\'\'\'\'Neck\'\'\'\'\'-to-\'\'\'\'\'Head\'\'\'\'\' and
    \'\'\'\'\'Head\'\'\'\'\'-to-\'\'\'\'\'`CameraTop_frame`\'\'\'\'\'
    coordination frames, respectively. These transformations are
    received with frequencies of 10, 50, 10, 10 and 50 Hz, respectively.
-   Querying memory instances: for each observed object
    \'\'\'\'\'O\'\'\'\'\', memory instances are queries to calculate the
    \'\'\'\'\'/odom\'\'\'\'\'-to-\'\'\'\'\'O\'\'\'\'\' transformation,
    as in Section 4.1.6. For each object, each of the five memory
    instances is queried once using a prev term and once using a next
    term. As there are in average 7 objects perceived per seconds,
    memory instances are queried 70 times per second.
-   Synchronization: a query is delayed in case any of the necessary
    transformations can not be interpolated from the data received so
    far. Retalis monitors the incoming events and performs the delayed
    queries as soon as all data necessary for their evaluations are
    available.
-   Subscription: In average 7 objects are perceived per second, their
    positions with respect to the \'\'\'\'\'\\odom\'\'\'\'\' frame are
    calculated and are published on the corresponding topics.

The following figure shows the CPU time used by the retalis and
retalis-ros-converter nodes when running the NAO example. The retalis
node calculates the position of objects in real-time. It processes about
1900 events, memorizes 130 new events and prunes 130 outdated events per
second. It also queries memory instances, 70 times per second. These
tasks are performed using about 18 percent of the CPU time. In this
experience, the retalis node has been directly subscribed to the
\'\'\'\'\'tf\'\'\'\'\' and \'\'\'\'\'ar_pose_marker\'\'\'\'\' ros
topics. The retalis-ros-converter only subscribes retalis to the
\'\'\'\'\'face_recognition/feedback\'\'\'\'\' topic and converts and
publishes events about objects\' positions to ros topics. To have this
setup, comments out the subscriptions to \'\'\'\'\'tf\'\'\'\'\' and
\'\'\'\'\'ar_pose_marker\'\'\'\'\' topics in the pub-sub.xml file and
instead, set the \'\'\'\'\'subscribe_tf_and_ar_pose\_\'\'\'\'\' boolean
variable in the retalis_interface.cpp file to \'\'\'\'\'true\'\'\'\'\'.
You should also recompile the package.

[![ CPU time for the NAO example\|width=\"700\"](attachment:base.png)](attachment:base.png)

As we saw in Section 4.1.2, retalis provides an easy way to subscribe to
ros topics and automatically convert ros messages to events. This is
implemented by the retalis-ros-converter node. The implementation is in
Python and is realized by inspecting classes and objects at runtime and
therefore is expensive. The following figure shows the CPU time used by
the retalis and retalis-ros-converter nodes for the NAO example, when
the retalis-ros-converter is used to subscribe to \'\'\'\'\'tf\'\'\'\'\'
and \'\'\'\'\'ar_pose_marker\'\'\'\'\' topics. This results show that
while the automatic conversion among messages and events are desirable
in a prototyping phase, the final application should implement it in C++
for performance reasons. We will investigate the possibility to
re-implement the retalis-ros-converter node in C++.

[![ CPU time for the NAO example\|width=\"700\"](attachment:baseex.png)](attachment:baseex.png)

### Forgetting and Memorizing

This section evaluates the performance of the memorizing and forgetting
functionalities. We measure the CPU time for various runs of the NAO
example where the numbers and types of memory instances are varied. We
discuss the performance of memory instances by comparing the CPU time
usages in different runs.

When an event is processed, updating memory instances includes the
following costs:

-   Unification: finding which memory instances match the event
-   Assetion: asserting the event in the database for each matched
    memory isntance
-   Retraction: retracting old events from memory instances that reached
    their size limit.

The following figure shows the CPU time for a number of runs where up to
160 memory instances are added to the NAO example. These memory
instances record \'\'\'\'\'a(X,Y,Z,W)\'\'\'\'\' events. Among the events
processed by retalis, there are no such events. The results show that
the increase in CPU time is negligible. This shows that a memory
instance consumes CPU time only if the input stream of events contains
events whose type matches the type of events the memory instance
records.

[![ a(X,Y,Z,W) memory instances\|width=\"700\"](attachment:mem-a.png)](attachment:mem-a.png)

In the following figure, the green and blue lines show the CPU time for
cases where 20 memory instances of type \'\'\'\'\'tf(X,Y,V,Q)\'\'\'\'\'
are added to the NAO example. These memory instances match all
\'\'\'\'\'tf\'\'\'\'\' events, about 1900 of such is processed every
second. The size of memory instances for the green line is 2500. These
memory instances reach their size limit in two seconds. After this time,
the CPU time usage is constant over time and includes the costs of
unification, assertion and retraction for updating 20 memory instances
with 1900 events per second. The size of memory instances for the blue
line is 150,000. It takes about 80 seconds for this memory instances to
reach their size limit. Consequently, the CPU time before the time 80
only includes the costs of unification and assertion, but not the costs
of retraction. After the time 100, the CPU usages of both runs are
equal. This shows that the cost of a memory instance does not depend on
its size. The purple line shows the CPU time for the case where
similarely there are 20 memory instances of type
\'\'\'\'\'tf(X,Y,V,Q)\'\'\'\'\'. However, these memory instances record
events until their reach their size limit. We added a condition for
these memory instances such that after reaching their size limit, they
perform no operation when receiving new events. After the time 100, the
CPU time is constant about 23 percent, being 5 percent more than the CPU
time of the NAO example, represented by the red line. This 5 percent
increase represents the unification cost. This also shows that the costs
of about 38000 assertions and 38000 retractions per second is about 30
percent of CPU time. In other words, 2500 memory updates (i.e.
assertions or retractions) are processed using one percent of CPU time.

[![ tf(X,Y,V,Q) memory instances with different sizes\|width=\"700\"](attachment:mem-all-limit.png)](attachment:mem-all-limit.png)

The following figure shows the CPU time for a number of runs where up to
40 memory instances of type \'\'\'\'\'tf(X,Y,Z,W)\'\'\'\'\' and size
2500 are added to the NAO example. The red line at the bottom shows the
CPU time for the NAO example. We make the following observations. Adding
first 10 memory instances to the NAO example increases the CPU time
about 20 percent. After that, adding each set of 10 memory instances
increases the CPU time about 13 percents. This shows that the cost grows
less than linearly. The implementation of memory instances is in a way
that the cost of an assertion or a retraction can be assumed constant.
This means that the unification cost for the first set of memory
instances is the highest. In other words, the unification cost per
memory instance decreases when the number of memory instances are
increased.

[![ tf(X,Y,V,Q) memory instances\|width=\"700\"](attachment:mem-all.png)](attachment:mem-all.png)

The following figure shows the CPU time for a number of runs where up to
640 memory instances of type \'\'\'\'\'tf(head,camera,Z,W)\'\'\'\'\' and
size 2500 are added to the NAO example. The events matching these memory
instances are received with the frequency of 50 Hz. We make the
following observaitons. First, it takes 50 seconds for these memory
instances to reach their size limit. After 50 seconds, these memory
instances reach their maximum CPU usages, as the costs of retraction is
added. Second, each memory instance filters 1900 events per second
recording about two percents of them. The cost of 640 memory instances
is about 35 percent of CPU time. Third, the unification cost per memory
instance is decreased when the number of memory instances are increased.

[![ tf(head,camera,V,Q) memory instances\|width=\"700\"](attachment:mem_head.png)](attachment:mem_head.png)

The following figure compares the costs of different types of memory
instances. The purple line shows the CPU time for the case where there
are 10 memory instances of type \'\'\'\'\'tf(X,Y,V,Q)\'\'\'\'\'. The
green line shows the CPU time for the case where there are 320 memory
instances of type \'\'\'\'\'tf(head,cam,V,Q)\'\'\'\'\'. We observe that
the costs of both cases are equal. The memory instances in the former
case record 19,000 events per second (i.e. 10\*1900). The memory
instances in the latter case filter 1900 events per seconds for
\'\'\'\'\'tf(head,cam,V,Q)\'\'\'\'\' events, recording 16000 events per
second (i.e. 320\*50). The results show the efficiency of the filtering
mechanism.

The brown line shows the CPU time for the case where there are 10 memory
instances of type \'\'\'\'\'tf(X,Y,V,Q)\'\'\'\'\' and 320 memory
instances of type \'\'\'\'\'tf(head,cam,V,Q)\'\'\'\'\'. Comparing it
with the green and purple lines shows that the CPU time usage of these
memory instances is less than sum of the CPU usages by 10
\'\'\'\'\'tf(X,Y,V,Q)\'\'\'\'\' memory instances and 320
\'\'\'\'\'tf(head,cam,V,Q)\'\'\'\'\' memory instances. This shows that
the unification cost per memory instance is decreased when the number of
memory instances are increased, even when the memory instances are not
of the same type.

[![ mix memory instances\|width=\"700\"](attachment:mem_mix.png)](attachment:mem_mix.png)

### Querying

Retalis queries are Prolog-like queries executed by the SWI-Prolog
system. The following evaluates the performance of next and prev terms
and the synchronization mechanism which are specific to retalis.

#### Querying Memory Instances

This section evaluates the performance of prev and next terms used to
access event records in memory instances. Retalis optimizes the
evaluation of these terms as follows. It keeps track of the number of
event records in each memory instance. The prev and next terms are
evaluated by a binary search on event records. An access to an event
record by its number takes a constant time. Consequently, the evaluation
of prev and next is done in logarithmic time on the size of the
respective memory instance.

The green line in the following figure shows the CPU time of the NAO
example adapted as follows. There is an additional
\'\'\'\'\'tf(head,cam,V,Q)\'\'\'\'\' memory instance of size 128. This
memory instance is queried by 1000 \'\'\'\'\'next\'\'\'\'\' terms for
each recognition of an object. In average, 7000 \'\'\'\'\'next\'\'\'\'\'
terms are evaluated per second. The blue line visualize the CPU time of
a similar program in which 7000 \'\'\'\'\'prev\'\'\'\'\' terms are
evaluated per seconds. The figure shows that the costs of the
evaluations of \'\'\'\'\'prev\'\'\'\'\' and \'\'\'\'\'next\'\'\'\'\'
terms are similar. The purple line shows the CPU time of the case where
14,000 \'\'\'\'\'next\'\'\'\'\' terms are evaluated per second. We
observe that the cost grows linearly, as expected.

[![ mix memory instances\|width=\"700\"](attachment:querynp.png)](attachment:querynp.png)

The blue line in the following figure visualizes the CPU time of the
case where 7000 \'\'\'\'\'next\'\'\'\'\' terms are evaluated per second.
The green line visualizes the CPU time of the case where there are 320
\'\'\'\'\'tf(head,cam,V,Q)\'\'\'\'\' memory instances. The purple line
visualizes the CPU time of the case where 7000 \'\'\'\'\'next\'\'\'\'\'
terms are evaluated per second and there are 320
\'\'\'\'\'tf(head,cam,V,Q)\'\'\'\'\' memory instances. We observe that
the cost of accessing a memory instance does not depend on existance of
other memory instances.

[![ mix memory instances\|width=\"700\"](attachment:query-mem1.png)](attachment:query-mem1.png)

The green line in the following figure visualizes the CPU time of
evaluating 7000 \'\'\'\'\'next\'\'\'\'\' terms per second on a memory
instance of size 128. The blue linevisualizes the CPU time of evaluating
7000 \'\'\'\'\'next\'\'\'\'\' terms per second on a memory instance of
size 16384. The size of the memory instance in the latter case is the
power of two of the size of the memory instance in the former case. The
increase in the CPU time for the latter case, with respect to the NAO
example, is less than two times of the increase in the CPU time for the
former case.

[![ mix memory instances\|width=\"700\"](attachment:query1.png)](attachment:query1.png)

#### Synchronization

The synchronization mechanism is implemented as follows. Before
evaluating a query, memory instances are checked whether they are
up-to-date with respect to the query. If the query cannot be evaluated,
it is recorded as a postponed query. For each postponed query, retalis
generates a set of monitors. Monitors observe memory update events. As
soon as all necessary events are in place in memory instances, the query
is performed. The implementation of monitors are similar to the
implementation of memory instances.

The red line in the following figure visualized the CPU time of the NAO
example where in each second, 1000 \'\'\'\'\'next\'\'\'\'\' queries on a
memory instance of size 2500 are evaluated. In addition, for each
\'\'\'\'\'next\'\'\'\'\' query, a new event is generated. The green line
visualizes the CPU time of a similar case where the next queries are
synchronized. This experiment is conducted in a way that no query needs
to be delayed. Coparing these two cases shows that when queries are not
delayed, the synchronization cost is negligible.

[![ mix memory instances\|width=\"700\"](attachment:syncbase.png)](attachment:syncbase.png)

The following figure shows the CPU time of four cases. In all these
cases, 1000 synchronized next queries are evaluated and 1000 events are
generated in each second. The red line visualizes the case where no
query is delayed. The green line visualized the case where queries are
delayed for 5 seconds. In this case, the memory instance queried by a
\'\'\'\'\'next\'\'\'\'\' term has not yet received the data necessary to
evaluate the query. The query is performed as soon as the memory
instance is updated with relevant information. There are 1000 queries
per seconds, each delayed for 5 seconds. This means there exist 5000
monitors at each time. These monitors observe 1900 events processed by
retalis per second. We observe that for such a large number of monitors
observing such a high-frequency input stream of events, the increase in
CPU time is less than 30 percent.

[![ mix memory instances\|width=\"700\"](attachment:sync.png)](attachment:sync.png)

### Subscription

The implementation of the subscriptions is similar to the implementation
of memory instances. The only difference is that an event matching a
memory instance is asserted to the knowledge base for that memory
instance, and an old event is retracted if the memory instance is full,
but an event matching a subscription is delivered to the respective
subscriber. Consequently, the costs of subscriptions include the
unification cost, discussed in section 5.1, and the costs to publish
events to subscribed ros topics.

### On-Flow Processing

On-flow processing functionalities in retalis are performed by Etalis.
Etalis execution model is based on decomposition of complex event
patterns into intermediate binary event patterns (goals) and the
compilation of goals into goal-directed event-driven Prolog rules. As
relevant events occur, these rules are executed deriving corresponding
goals progressing toward detecting complex event patterns.

Information flow processing systems such as Etalis are designed for
applications that require a real-time processing of a large volume of
data flow. Please see
[Etalis publications](http://code.google.com/p/etalis/wiki/Publications)
for the evaluation of the performance of on-flow functionalities. The
evaluation results show, in terms of performance, Etalis is competitive
with respect to the state-of-the-art on-flow processing systems.
