## Overview

`rosmsg` and `rossrv` are handy command-line tools that provide
reference information for developers and also serve as a powerful
introspection tool for learning more about data being transmitted in
ROS.

For example, if you are using a message in your code, you can type
`rosmsg show` at the command-line to look up its fields:


```
$ rosmsg show sensor_msgs/CameraInfo
Header header
  uint32 seq
  time stamp
  string frame_id
uint32 height
uint32 width
RegionOfInterest roi
  uint32 x_offset
  uint32 y_offset
  uint32 height
  uint32 width
float64[5] D
float64[9] K
float64[9] R
float64[12] P
```



For even quicker typing, you can omit "`my_pkg`", and `rosmsg`
will search all packages for a matching message.

You can also use this in an online system with tools like
[rostopic](rostopic). For example, `rostopic type` will tell you the
message type of a topic: 

```
$ rostopic type rosout
roslib/Log
```

 You can pass this to
`rosmsg` to quickly see the fields of the message:


```
rostopic type rosout | rosmsg show
byte DEBUG=1
byte INFO=2
byte WARN=4
byte ERROR=8
byte FATAL=16
Header header
  uint32 seq
  time stamp
  string frame_id
byte level
string name
string msg
string file
string function
uint32 line
string[] topics
```



Once you know more about the fields of a particular message, you can
then listen them at the command-line, e.g. 

```
$ rostopic echo rosout/msg
```



## Command-Line Tools

### rosmsg

The `rosmsg` command-line tool displays information about ROS
[Message types](msg). The following sections describe the commands that
are available.

#### rosmsg show

`show <message type>` Display the fields in a ROS message type. You
may omit the package name of the type, in which case `rosmsg` will
search for matching types in all packages. Example:


```
$ rosmsg show std_msgs/String
```

or, if you don't know the package
name:

```
$ rosmsg show Pose
```

You can use [rosmsg](rosmsg) in combination
with [rostopic](rostopic) to display the type information about a
[topic](Topics): 

```
$ rostopic type /topic_name | rosmsg show
```



`-r` Display the raw [msg](msg) definition.

```
$ rosmsg show -r robot_msgs/Quaternion
# xyz - vector rotation axis, w - scalar term (cos(ang/2))
float64 x
float64 y
float64 z
float64 w
```



`-b BAGFILE` Show message as defined in BAGFILE.

#### rosmsg list

`list` Display a list of all messages. This command does not take in
any additional arguments. This command is mainly for use by experts who
wish to perform operations on packages with `.msg`
files.

```
$ rosmsg list
nav_msgs/GridCells
nav_msgs/MapMetaData
nav_msgs/OccupancyGrid
nav_msgs/Odometry
nav_msgs/Path
...
```



Note that messages in a subfolder may not be listed as of March 2017
([open ticket](https://github.com/ros/ros_comm/issues/1021)).

#### rosmsg package

`package <package-name>` Display a list of all messages in a
package.

```
$ rosmsg package nav_msgs
nav_msgs/OccupancyGrid
nav_msgs/Path
nav_msgs/MapMetaData
nav_msgs/Odometry
nav_msgs/GridCells
```



`-s` Display all messages on a single line. Useful for backtick
invocations.

#### rosmsg packages

`packages` Display a list of all packages with messages. This command
does not take in any additional arguments. This command is mainly for
use by experts who wish to perform operations on packages with `.msg`
files.

```
$ rostopic type rosout
roslib/Log
```

0 `-s` Display all packages on a single
line. Useful for backtick invocations.

#### rosmsg users

**Only available in ROS Electric and earlier**

`users <message type>` Search for code files that use the message
type. This is useful when renaming message types. This command may take
a long time, depending on the size of your code base.

*NOTE: As ROS supports many different coding languages, `rosmsg users`
is not guaranteed to find every file that uses the message type and
should only be used as a supplementary tool.*

```
$ rostopic type rosout
roslib/Log
```

1

#### rosmsg md5

*NOTE: The md5 command is meant for expert users only.*

`md5 <message type>` Display the md5 sum of a message. This will
will also warn if the compiled version doesn't match.

### rossrv

The `rossrv` command-line tool displays information about ROS
services. It has the exact same usage as `rosmsg` (see what it offers
when it runs without sub-command below):



```
$ rostopic type rosout
roslib/Log
```

2

### Syntax highlighting

-   [Sublime Text 3](https://gist.github.com/eric-wieser/1cd2919483d18d6b3788a54dec4f165c)

## Roadmap

`rosmsg` and `rossrv` are stable tools. There is currently no plan
to add new features to them.
