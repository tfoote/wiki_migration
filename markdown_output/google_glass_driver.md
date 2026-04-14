The google_glass_driver package is used to establish bidirectional
communication between a human supervisor and one or more semi-autonomous
robots. Using the Glass server node and the Robot Manager Glass app, a
human supervisor can use voice commands to select a robot and give a
command to it. Voice commands can also be used to navigate the Robot
Manager app. The robots can send data back to the user using either text
or image messages. Interactions within the system can be seen in
[this diagram](https://drive.google.com/file/d/0B8CLLYYXup2fOHRxUWFRNWJ5WEU/edit?usp=sharing).

![](https://googledrive.com/host/0B8CLLYYXup2fblVnNFU1SUd1ME0/google_glass_driver_diagram.png)

It should be noted that there is another ROS package,
[ros_glass_tools](ros_glass_tools), aimed at establishing bi-directional
communication between ROS and Google Glass. There are some fundamental
differences between these packages that should be considered:

Connection - ros_glass_tools uses Wi-fi to send data between ROS and
Glass. This package uses Bluetooth.

Voice commands - ros_glass_tools uses the cloud voice recognition tool
to translate speech to text. This package uses offline voice recognition
to match speech to a limited set of allowable phrases. See the
Vocabulary tutorial for more details. Handling of voice commands on the
ROS side is also very different.

There are many more differences between these two packages, and they can
be seen by examining the wikis of the two packages.

## Setup

### ROS Setup

The Glass server node is implemented in Python. In order to use it, you
must first download the PyBluez library. You can use the following
apt-get command:

```
sudo apt-get install python-bluetooth
``` On some computers, a Bluetooth socket may be
established but no data is sent through. If your computer is having
trouble sending data through Bluetooth, please see
[this StackOverflow post](http://stackoverflow.com/questions/14618277/rfcomm-without-pairing-using-pybluez-on-debian/14827036#14827036).

### Google Glass Setup

As of the writing of this wiki, the RobotManager app has not been
approved by Google for distribution through the Glass store. This means
it will need to be loaded from source.

1\. Download the ADT Eclipse plug-in. Details on doing this can be found
[here](http://developer.android.com/sdk/installing/installing-adt.html). 1.
Set your workspace to be the google_glass_driver/android directory. 1.
Import the RobotManager project by going to
File-\>Import-\>General-\>Existing Projects Into
Workspace-\>RobotManager 1. Connect Glass through USB and the press the
green circle with a white arrow at the top of the ADT Eclipse screen.
The tooltip should say \"Run RobotManager\". This should load the
application onto your Glass. 1. You may want to screencast your Glass to
your computer or get Log output. To do this, you must enable Glass\'s
Debug mode. Follow
[these instructions](http://stackoverflow.com/questions/21542577/how-can-we-enable-debugging-mode-on-google-glass-for-testing-an-android-app-on-g)
to do so.

## Vocabulary

The Robot Manager app is always listening for voice commands whenever
the app is active. The continuous listening algorithm listens for voice
commands in a limited set and finds a closest match within tolerance.
The limited set changes based on the context of the command. For
example, on startup Glass needs to know which Bluetooth device it should
connect to. No other commands can be given if a Bluetooth connection has
not been established. Because of this, Glass only listens for \"Connect
to \...\" commands.

The set of all possible commands Glass can understand is called the
Vocabulary. The limited sets of commands, which may or may not be
listened for in a given context, are called sub-vocabularies.

In order for a robot to be used with Glass through this package, the
robot must pass its own vocabulary to Glass in the configuration step.
This vocabulary is the full set of commands that robot understands. This
then becomes a sub-vocabulary of Glass.

For more information on Vocabularies and how to use them, read this
tutorial page (TODO).

## Nodes

```clearsilver
node {
name = glass_server_node
desc = This node acts as the middle man between Glass and ROS.  It accepts messages and services from ROS nodes and transmits them to Glass via Bluetooth. Additionally it receives messages from Glass via Bluetooth and publishes them to a target topic.
sub {
  0.name = glass_server/text_messages
  0.type = google_glass_driver/TextMessage
  0.desc = Text messages to be sent to Glass

  1.name = glass_server/image_messages
  1.type = google_glass_driver/ImageMessage
  1.desc = Image messages to be sent to Glass
}
pub {
  0.name = recognizer/output
  0.type = std_msgs/String
  0.desc = Deprecated, carries all commands received by Glass

  1.name = *robot_name*/voice_command
  1.type = std_msgs/String
  1.desc = Each robot that successfully connects to Glass though the RobotConfiguration service is given its own topic.  This topic carries the text of voice commands given to the robot through Glass. The *robot_name* field is assigned the string passed as Name in the RobotConfiguration service.  Non-ROS topic compliant names are given compliant names (i.e "My Robot" => "my_robot")
}
srv {
  0.name = robot_configuration
  0.type = google_glass_driver/RobotConfiguration
  0.desc = This service must be used by a robot in order to be recognized by Glass.  Service calls must provide the robot's name, a brief description of the robot, and the robot's vocabulary (discussed in the Vocabulary section).  If the configuration is successful the service returns true.
}
}
```

![](https://googledrive.com/host/0B8CLLYYXup2fblVnNFU1SUd1ME0/RIVeR_Lab.png)
