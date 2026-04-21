## The Basics

This client library allows to write ROS nodes in the
[Lua](http://www.lua.org) programming language. It allows to publish and
subscribe to topics, to provide and use services, interact with ROS
masters, slaves and param servers, and provides general utilities for
time and duration handling, and logging.

You can find the newest version at <http://github.com/timn/roslua>.

It does most likely not contain all the features roscpp and rospy can
offer. It does *not* aim to replace any of these, rather it provides an
option for situations where Lua might be more suitable or more
desirable, e.g. on constrained systems or for behavior description and
programming.

The implementation is written purely in Lua, with some functionality
coming from external Lua modules written in Lua and C
(close-to-operating-system functionality like network transmissions and
unpacking of data of the TCPROS protocol, XML parsing, HTTP web server
etc.).

## Notable differences

There are some differences from client libraries written in and for
other languages that are noteworthy.

No offline code generation is necessary for message and service
description files, i.e. the message and service code generation steps of
the build system will not produce any output for Lua. roslua directly
reads the definition files at run-time and creates the appropriate
representations at run-time. Since these specifications are read only
once on startup when the topics or services are registered, the overhead
is negligible and only occurs during initialization of the node.

Lua is inherently single-threaded. There is only so-called cooperative
multi-threading in the form of coroutines, which is not used for this
implementation. The most notable drawback is that long message
processing steps influence the whole program, including processing
incoming messages and XML-RPC requests. This can pose a problem to
certain programs and node writers should be aware of this. It also
allows for the simplicity and briefness of the code, since many
constructs like locking are unnecessary.

## How to use

For information about requirements and how to get started please read
the [README](http://github.com/timn/roslua/blob/master/README) file in
the package. In the package\'s doc directory you find auto-generated API
documentation. Volunteers are welcome to help out with tutorials.

Full API documentation is available at <http://timn.github.com/roslua/>.
