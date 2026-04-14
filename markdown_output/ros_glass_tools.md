The ros_glass_tools package demonstrates the ability of bidirectional
communication between Google Glassware and ROS nodes running on a
separate system. Three android glass applications are provided. Each of
these applications perform a specific interaction with ROS using the
Google Glass. In addition to these applications, helper nodes are
provided that enable the communication and functionality on the ROS
machine. [Youtube](https://www.youtube.com/watch?v=ShXKyO6LdRI)

## Programs

### Ros Programs

The ROS package includes three nodes as well as two services.

#### list_topics.py

This node provides a service which returns a list of all topics
currently registered with the ROS master.

#### voice_control.py

This node listens for a service which contains a string command. Once
the command is received, it parses the string and publishes empty
messages on the desired topics. The topics and commands are defined at
runtime.

#### glass_monitor.py

This node allows the user to dynamically create monitors that will
listen to predefined topics for specific data conditions. Should these
conditions occur, the node will publish a warning message. These
monitors are created using a simple specification in the launch file
which is be explained in greater detail below.

### Glass Applications

There are three sample glass applications that allow for robot
monitoring and control. These include methods to select and display
topic message data, provide pop up warnings, and control multiple robots
at once using voice commands.

#### GlassTopicViewer

This application allows the user to select any topic currently
publishing information and display the published messages in text or
graphical form. On application startup the user is given a choice of
which topic they would like to examine. Once selected, a live card is
placed on the Google Glass Timeline. This card continually updates with
the latest message received on the topic. Further, by using the menus
associated with the live card, the user can choose to view a specific
field of the message or graph a specific field of the message.

#### GlassROSMonitor

This application starts a background service that displays a warning
message if one of the conditions defined in the glass_monitor.py is
violated. This allows the user to focus their attention elsewhere,
knowing that they will receive a warning if the system enters a state
that requires action.

#### RobotVoiceControl

This application harnesses the voice recognition ability of Google Glass
to enable the control of multiple robots. The user can send commands to
all robots, a single robot, or to a global command by simply saying
\"all\" , \"robot n\", or \"execute\" before stating the command. The
command is then sent to the ROS voice_control.py script for processing.

## Setup

The following section outlines the setup for both the ROS system and the
Google Glassware applications.

### ROS System Setup

To successfully communicate to the ROS server from the Google Glassware,
the rosbridge_suite package is required. Follow the instructions to
install and run the rosbridge webserver at
<http://wiki.ros.org/rosbridge_suite>.

Next, the ROS tools must be configured as to enable communication in and
functionality between the ROS and the Google Glasses. Obtain the source
code from github (<https://github.com/unl-nimbus-lab/ros_glass_tools>)
and build the package using the catkin tools. It is important that the
\"Commands\" and \"Topics\" services are built. After building, the ROS
system is ready to be run.

### Glass Setup

To run the glass applications, it is first necessary to setup your
development environment to use the Glass Development Kit Sneak Peak.
Instructions to do so can be found at
<https://developers.google.com/glass/develop/gdk/quick-start>. It is
important that you install the latest version, as the API has changed,
and the code will not compile on the older versions of the GDK. The
Glassware must also have debug mode enabled. The instructions to do so
are also found on the Google Glass development site above.

After the environment is setup, the applications must be imported into
the Eclipse Android environment. This is done by selecting \"import\"
-\> \"Existing Android Code Into Workspace\" -\> and selecting the
\"Applications\" directory in the ros_glass_tools package. All three
applications can be imported in this way. After importing, ensure that
the \"Glass Development Kit Sneak Peek\" is selected as the Android
Build Target in the project properties. Additionally, this project
relies on the Autobahn Websocket library (<http://autobahn.ws/>). Ensure
that these jars are in the libs directory and on the build path.

The final step is ensuring that the correct hostname/address is supplied
to Glass for connecting to the rosbridge webserver. There is a line in
each project that defines the host address. Edit this line to ensure
that you are sending requests to the correct address and port. By
default the websocket server operates on port 9090. The line that needs
to be edited appears below and is the same in each projects.

public final static String HOST_ADDRESS =
\"<ws://>[192.168.1.142:9090](http://192.168.1.142:9090/)\";

### Running and Usage

Each of the glass applications rely on one of the the ROS nodes for
functionality and all of the applications rely on the rosbridge
webserver for communication. The rosbridge can be launched using the
example launch script provided in their distribution with the command
\"roslaunch rosbridge_server rosbridge_websocket.launch\". Outlined
below are the steps to ensure that each of the applications can be run
correctly.

### GlassTopicView

#### Launching

To ensure this application will run correctly, start your ROS system as
normal. Once this is done, start the list_topics.py node, found in the
ros_glass_tools package. This node must be started to enable the glasses
to determine which topics are currently publishing. The list_topics.py
node can be launched from the command line or added to any launch file.

#### Usage

The tool can be started in one of three ways, through a voice command,
menu selection, or from the eclipse ADT. Once started the user is shown
a full list of every topic that is publishing messages on the ROS
system. The user can then select which topic to display. This creates a
Glass Live Card that is updated everytime a new message on the desired
topic is published. The user then has the ability to select the live
card and change or destroy the display. While the default view is to
desplay all the fields of a message, the card can also be changed to
display a graphical or textual representation of a single field. The
graphical view automatically scales the y axis range to ensure that all
of the data is visible. To display another topic, simply restart the
application and select the desired topic.

### GlassROSMonitor

#### Launching

The configuration of the ROS node associated with this application is
the most complex part of using GlassROSMonitor. In order to run
correctly, the monitors must be correctly defined in the ROS parameter
server under the parameter \"monitors.\" Using the server, any number of
monitors can be created. The \"monitors\" parameter is a list of
dictionaries; one for each monitor that the user creates. In each
dictionary, five key/value pairs must be defined, as explained below.

topic: Full name of the topic on which the data for monitoring will be
published.

field: Full name of the field within the messages published on the
topic. e.g translation/x.

op: One of the following operations for comparison.

gt -- Greater than operator lt -- Less than operator eq -- Equality
operator ne -- Not equal operator outside -- Absolute value of data
point is greater than the value provided within -- Absolute value of
data point is less than the value provided

val: Value to compare message data against

msg: Message to publish to glassware when the constraint has been
violated.

Example Launch file input:

\<rosparam name=\"monitors\"\>

\[ { topic: \'/a/subject_pose\', field: \'translation/x\', op:
\'outside\', val : 2 , msg: \'Exceeded Bounds\'}, { topic:
\'/a/subject_pose\', field: \'translation/z\', op: \'gt\', val : 2 ,
msg: \'Too high!!!\'} \]

\</rosparam\>

#### Usage

The application simply starts a background service on Google Glass that
listens for warning messages published by the glass_monitor.py node.
When a message is published, the service creates a live card that is
displayed immediately, notifying the user of the violation. To prevent
displaying too many popups and distracting the user, the service will
only display the message if it is not the most recently received, or if
the user has dismissed a previous message. The user also has the option
to completely quit the service from the displayed message and turn off
all further warnings.

### RobotVoiceControl

The robot voice control application works by publishing empty messages
to a set of specified ROS topics that can then activate predefined
operations. It is designed for systems that have multiple robots with
similar capabilities, but also allows for global commands that are robot
independent. Before this functionality can be accessed, however,
specific commands and behaviors must be defined in the ROS parameters.

#### Launching

Three separate parameters are needed to correctly setup the ROS node to
accept voice commands. The first parameter deals with global commands
that will be run after saying the keyword \"execute\" while in the
Google Glass application. This parameter is a N x 2 array. Each row in
the array contains the name of the command and the topic on which to
publish the command. An example of this is shown below.

\<rosparam param=\"global_commands\"\> \[ \[stop, /all_stop\], \[go,
/all_go\] \]

\</rosparam\>

The individual robot commands require both the \"robots\" parameter and
the \"robot_commands\" parameter to work correctly. This section of the
tool assumes that ROS is configured so that each robot that will be
controlled has a unique namespace. The \"robots\" parameter maps each
namespace to a robot number. An array of namespaces is passed into the
tool and the position of the namespace becomes the robot number. In the
following example input \"robot one\" would issue commands on namespace
\"a\" and robot two maps to namespace \"b\".

\<rosparam param=\"robots\"\>

\[a, b\] \</rosparam\>

The \"robot_commands\" parameter provides the mapping between the
command the user says and the topics within each namespace that will
cause the robot to execute the command. The structure of the parameter
is the same as the global_commands. The first string in the pair is the
word the user must say in order to execute the command. The second is
the name of the topic on which to publish information. When these
parameters are read into the node, the command is registered and a topic
is created for each robot with the namespace prepended to the front of
the topic. For example consider the following launch file parameter in
combination with the two robots above:

\<rosparam param=\"robot_commands\"\> \[ \[forward, move_forward\],
\[backward, move_backward\] \] \</rosparam\>

In this example, the node would open up four topics for publishing:
a/forward, a/backward, b/forward, and b/backward. The following also
maps out which voice commands would lead to messages being published on
which topics.

\"robot one forward\" -\> a/move_forward

\"robot two backward\" -\> b/move_backward

\"all forward\" -\> a/move_forward & b/move_forward

#### Usage

To use this app simply start the application by either using the \"ok
glass robot control\" voice command or navigate to it on the menu. Once
started the prompt will be displayed asking for input. At this point
there are three options possible.

Saying \"execute\" and then a command will publish a message on the
corresponding command that has been established in the ROS node.

Saying \"all\" and then a command will publish a message on each
namespace corresponding to the topic defined in the ROS node.

Saying \"robot n\" and then a command command will publish a message on
robot n\'s namespace on the topic that has been paired with command in
the ROS node.

Using the same parameters as defined above, saying the following will
publish on the following topics.

\"execute stop\" --\> /stop

\"execute go\" --\> /go

\"robot one forward\" --\> /a/forward
