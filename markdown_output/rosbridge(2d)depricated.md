# Deprecated

This is the documentation for the 1.0 version of rosbridge. This version
blazed the trail and helped us establish use cases and applications.
However, it is now considered deprecated and is not currently supported.

For the currently maintained version of rosbridge, please see
[rosbridge 2.0](rosbridge_suite).

# Introduction

rosbridge makes ROS topics and services available over either pure TCP
sockets or web-sockets as JSON messages. Both modes, socket and
web-socket, use the same JSON format for both request and responses. A
single instance of rosbridge supports both modes among different clients
simultaneously.

# ros.js

The rest of this page describes the rosbridge server itself. If you are
mostly interested in writing pure HTML+JS ROS applications, you will
probably only care about rosbridge insomuch as it is the backend to
ros.js. You should probably start by reading the
[ros.js tutorial](http://ros.org/wiki/rosbridge/Tutorials/Using%20Javascript%20to%20control%20ROS%20via%20rosjs).

# Socket modes

By default, rosbridge listens on port 9090 and supports two connection
modes.

## web-sockets

rosbridge supports the normal web-socket handshake for connection
initiation. After a connection is established JSON messages (see the
message format section) are exchanged as normal web-socket messages.

## sockets

To start a socket connection with rosbridge, open a socket to port 9090
of the appropriate host and send the string "raw" followed by a
carriage return, a linefeed, another carriage return, and another
linefeed (i.e. "raw\\r\\n\\r\\n" in python).

After that, all message to or from the server should/will begin with a
0x00 byte and end with 0xFF.

# Message Format

Messages to and from rosbridge are in the form of pure ASCII JSON
messages.

## Topics

Topics are sent and received in the following format:



```
{"receiver":"/topic","msg":{},"type":"package/Type"}
```



where /topic is the topic, msg contains a JSON version of the actual ROS
message, and type contains the type string for the topic.

For example, sending a Twist message to /cmd_vel might look like this:



```
{"receiver":"/cmd_vel","msg":{"linear":{"x":0,"y":0,"z":0},"angular":{"x":0,"y":0,"z":0}},"type":"geometry_msgs/Twist"}
```



## Service Calls

To make a service call:



```
{"receiver":"/service","msg":[]}
```



where receiver is the service being called and msg is a JSON array of
arguments (e.g. \[arg1,arg2\]). Answers will come back from rosbridge as
topics with the receiver set to the name of the service.

## JSON forms of ROS Messages

For the most part, the translation of ROS to JSON is straight-forward.
However, some ROS types (such as images) can optionally be translated
into special forms such as data-uri's. For more details, see the
rosbridge Javascript tutorial.

# Special Services

The special services portions of the rosjs binding for rosbridge are
always available, even when rosbridge is being accessed from another
language or over pure sockets. These services are how rosbridge clients
discover and subscribe to topics, discover services, and perform other
tasks. For a full description of these services read the "rosjs
Services" section of the Javascript rosbridge tutorial.

# Writing a rosbridge client

The rosbridge protocol was designed to make writing clients simple. We
recommend you examine the source to
[ ros.js](http://brown-ros-pkg.googlecode.com/svn/tags/brown-ros-pkg/rosbridge/ros.js ),
a full web-socket client implemented in only 73 lines.
