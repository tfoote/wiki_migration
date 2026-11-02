## Viewing the Code

**roscpp_tutorials** contains a number of tutorial applications for
programming with roscpp.

You can browse these tutorials by `roscd`-ing to the
`roscpp_tutorials` package, i.e. 

```
roscd roscpp_tutorials
```



There are also several Wiki-based tutorials, listed below.

## Beginner Tutorials

- [Writing a Simple Publisher and Subscriber](#writing-a-simple-publisher-and-subscriber):
  This tutorial covers how to write a publisher and subscriber node in
  C++.
- [Writing a Simple Service and Client](#writing-a-simple-service-and-client):
  This tutorial covers how to write a service and client node in C++.
- [Using Parameters in roscpp](#using-parameters-in-roscpp):
  This tutorial will show you the `NodeHandle` parameter API, allowing
  you to manipulate parameters from the
  [Parameter Server](Parameter Server).
- [Accessing Private Names from a NodeHandle](#accessing-private-names-from-a-nodehandle):
  This tutorial will show you how to access private [Names](Names) with
  roscpp's `NodeHandle` API.
- [Using Class Methods as Callbacks](#using-class-methods-as-callbacks):
  Most of the tutorials use functions in their examples, rather than
  class methods. This is because using functions is simpler, not because
  class methods are unsupported. This tutorial will show you how to use
  class methods for subscription and service callbacks.

## Intermediate Tutorials

- [Understanding Timers](#understanding-timers):
  This tutorial explains roscpp Timers, which allow you to schedule a
  callback to happen periodically.

<!-- -->

- [ Dynamic Reconfigure](#writing-publishersubscriber-with-parameters-dynamic-reconfigure-and-custom-messages)

## Create a new tutorial

## Writing a Simple Publisher and Subscriber

### Writing the Publisher Node

"Node" is the ROS term for an executable that is connected to the ROS
network. Here we'll create a publisher ("talker") node which will
continually broadcast a message.



```
{#!wiki buildsystem rosbuild
Change directory into the beginner_tutorials package, you created previously in the [[ROS/Tutorials/CreatingPackage|creating a rosbuild package]] tutorial:

{{{
roscd beginner_tutorials
```

 }}}}



```
{#!wiki buildsystem catkin
Change directories to your beginner_tutorials package you created in your catkin workspace previous tutorials:

{{{
roscd beginner_tutorials
```



}}}}

#### The Code



```
{#!wiki buildsystem catkin
Create a `src` directory in the beginner_tutorials package directory:

{{{
mkdir -p src
```



This directory will contain any source files for our beginner_tutorials
package. }}}}

Create the src/talker.cpp file within the beginner_tutorials package and
paste the following inside it:

Source:
[talker.cpp](https://github.com/ros/ros_tutorials/blob/kinetic-devel/roscpp_tutorials/talker/talker.cpp)



```cpp
/*
 * Copyright (C) 2008, Morgan Quigley and Willow Garage, Inc.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *   * Redistributions of source code must retain the above copyright notice,
 *     this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *   * Neither the names of Stanford University or Willow Garage, Inc. nor the names of its
 *     contributors may be used to endorse or promote products derived from
 *     this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */
#include "ros/ros.h"
#include "std_msgs/String.h"

#include <sstream>

/**
 * This tutorial demonstrates simple sending of messages over the ROS system.
 */
int main(int argc, char **argv)
{
  /**
   * The ros::init() function needs to see argc and argv so that it can perform
   * any ROS arguments and name remapping that were provided at the command line.
   * For programmatic remappings you can use a different version of init() which takes
   * remappings directly, but for most command-line programs, passing argc and argv is
   * the easiest way to do it.  The third argument to init() is the name of the node.
   *
   * You must call one of the versions of ros::init() before using any other
   * part of the ROS system.
   */
  ros::init(argc, argv, "talker");

  /**
   * NodeHandle is the main access point to communications with the ROS system.
   * The first NodeHandle constructed will fully initialize this node, and the last
   * NodeHandle destructed will close down the node.
   */
  ros::NodeHandle n;

  /**
   * The advertise() function is how you tell ROS that you want to
   * publish on a given topic name. This invokes a call to the ROS
   * master node, which keeps a registry of who is publishing and who
   * is subscribing. After this advertise() call is made, the master
   * node will notify anyone who is trying to subscribe to this topic name,
   * and they will in turn negotiate a peer-to-peer connection with this
   * node.  advertise() returns a Publisher object which allows you to
   * publish messages on that topic through a call to publish().  Once
   * all copies of the returned Publisher object are destroyed, the topic
   * will be automatically unadvertised.
   *
   * The second parameter to advertise() is the size of the message queue
   * used for publishing messages.  If messages are published more quickly
   * than we can send them, the number here specifies how many messages to
   * buffer up before throwing some away.
   */
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);

  ros::Rate loop_rate(10);

  /**
   * A count of how many messages we have sent. This is used to create
   * a unique string for each message.
   */
  int count = 0;
  while (ros::ok())
  {
    /**
     * This is a message object. You stuff it with data, and then publish it.
     */
    std_msgs::String msg;

    std::stringstream ss;
    ss << "hello world " << count;
    msg.data = ss.str();

    ROS_INFO("%s", msg.data.c_str());

    /**
     * The publish() function is how you send messages. The parameter
     * is the message object. The type of this object must agree with the type
     * given as a template parameter to the advertise<>() call, as was done
     * in the constructor above.
     */
    chatter_pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
    ++count;
  }


  return 0;
}
```



#### The Code Explained

Now, let's break the code down.



```cpp
#include "ros/ros.h"
```

 `ros/ros.h` is a convenience include that
includes all the headers necessary to use the most common public pieces
of the ROS system.



```cpp
#include "std_msgs/String.h"
```

 This includes the
[std_msgs/msg/String](https://docs.ros.org/en/rolling/p/std_msgs/msg/String.html)
message, which resides in the
[std_msgs](https://index.ros.org/p/std_msgs) package. This is a header
generated automatically from the `String.msg` file in that package.
For more information on message definitions, see the [msg](msg) page.



```cpp
  ros::init(argc, argv, "talker");
```

 Initialize ROS. This allows ROS to do name
remapping through the command line \-- not important for now. This is
also where we specify the name of our node. Node names must be unique in
a running system.

The name used here must be a [base name](Names#Graph), ie. it cannot
have a `/` in it.



```cpp
  ros::NodeHandle n;
```

 Create a handle to this process' node. The
first `NodeHandle` created will actually do the initialization of the
node, and the last one destructed will cleanup any resources the node
was using.



```cpp
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);
```

 Tell the master that we are going to be
publishing a message of type
[std_msgs/msg/String](https://docs.ros.org/en/rolling/p/std_msgs/msg/String.html)
on the topic `chatter`. This lets the master tell any nodes listening
on `chatter` that we are going to publish data on that topic. The
second argument is the size of our publishing queue. In this case if we
are publishing too quickly it will buffer up a maximum of 1000 messages
before beginning to throw away old ones.

`NodeHandle::advertise()` returns a `ros::Publisher` object, which
serves two purposes: 1) it contains a `publish()` method that lets you
publish messages onto the topic it was created with, and 2) when it goes
out of scope, it will automatically unadvertise.



```cpp
  ros::Rate loop_rate(10);
```

 A `ros::Rate` object allows you to specify a
frequency that you would like to loop at. It will keep track of how long
it has been since the last call to `Rate::sleep()`, and sleep for the
correct amount of time.

In this case we tell it we want to run at 10Hz.



```cpp
  int count = 0;
  while (ros::ok())
  {
```

 By default roscpp will install a SIGINT
handler which provides Ctrl-C handling which will cause `ros::ok()` to
return false if that happens.

`ros::ok()` will return false if:

- a SIGINT is received (Ctrl-C)
- we have been kicked off the network by another node with the same name
- `ros::shutdown()` has been called by another part of the
  application.
- all ros::NodeHandles have been destroyed

Once `ros::ok()` returns false, all ROS calls will fail.



```cpp
    std_msgs::String msg;

    std::stringstream ss;
    ss << "hello world " << count;
    msg.data = ss.str();
```

 We broadcast a message on ROS using a
message-adapted class, generally generated from a [msg file](msg). More
complicated datatypes are possible, but for now we're going to use the
standard `String` message, which has one member: "data".



```cpp
    chatter_pub.publish(msg);
```

 Now we actually broadcast the message to
anyone who is connected.



```cpp
    ROS_INFO("%s", msg.data.c_str());
```

 `ROS_INFO` and friends are our replacement
for `printf`/`cout`. See the
[rosconsole documentation](https://index.ros.org/p/rosconsole) for more
information.



```cpp
    ros::spinOnce();
```

 Calling `ros::spinOnce()` here is not
necessary for this simple program, because we are not receiving any
callbacks. However, if you were to add a subscription into this
application, and did not have `ros::spinOnce()` here, your callbacks
would never get called. So, add it for good measure.



```cpp
    loop_rate.sleep();
```

 Now we use the `ros::Rate` object to sleep
for the time remaining to let us hit our 10Hz publish rate.

Here's the condensed version of what's going on:

- Initialize the ROS system
- Advertise that we are going to be publishing
  [std_msgs/msg/String](https://docs.ros.org/en/rolling/p/std_msgs/msg/String.html)
  messages on the `chatter` topic to the master
- Loop while publishing messages to `chatter` 10 times a second

Now we need to write a node to receive the messsages.

### Writing the Subscriber Node

#### The Code

Create the `src/listener.cpp` file within the `beginner_tutorials`
package and paste the following inside it:

Source:
[listener.cpp](https://github.com/ros/ros_tutorials/blob/kinetic-devel/roscpp_tutorials/listener/listener.cpp)



```cpp
/*
 * Copyright (C) 2008, Morgan Quigley and Willow Garage, Inc.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *   * Redistributions of source code must retain the above copyright notice,
 *     this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *   * Neither the names of Stanford University or Willow Garage, Inc. nor the names of its
 *     contributors may be used to endorse or promote products derived from
 *     this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#include "ros/ros.h"
#include "std_msgs/String.h"

/**
 * This tutorial demonstrates simple receipt of messages over the ROS system.
 */
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
  /**
   * The ros::init() function needs to see argc and argv so that it can perform
   * any ROS arguments and name remapping that were provided at the command line.
   * For programmatic remappings you can use a different version of init() which takes
   * remappings directly, but for most command-line programs, passing argc and argv is
   * the easiest way to do it.  The third argument to init() is the name of the node.
   *
   * You must call one of the versions of ros::init() before using any other
   * part of the ROS system.
   */
  ros::init(argc, argv, "listener");

  /**
   * NodeHandle is the main access point to communications with the ROS system.
   * The first NodeHandle constructed will fully initialize this node, and the last
   * NodeHandle destructed will close down the node.
   */
  ros::NodeHandle n;

  /**
   * The subscribe() call is how you tell ROS that you want to receive messages
   * on a given topic.  This invokes a call to the ROS
   * master node, which keeps a registry of who is publishing and who
   * is subscribing.  Messages are passed to a callback function, here
   * called chatterCallback.  subscribe() returns a Subscriber object that you
   * must hold on to until you want to unsubscribe.  When all copies of the Subscriber
   * object go out of scope, this callback will automatically be unsubscribed from
   * this topic.
   *
   * The second parameter to the subscribe() function is the size of the message
   * queue.  If messages are arriving faster than they are being processed, this
   * is the number of messages that will be buffered up before beginning to throw
   * away the oldest ones.
   */
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);

  /**
   * ros::spin() will enter a loop, pumping callbacks.  With this version, all
   * callbacks will be called from within this thread (the main one).  ros::spin()
   * will exit when Ctrl-C is pressed, or the node is shutdown by the master.
   */
  ros::spin();

  return 0;
}
```



#### The Code Explained

Now, let's break it down piece by piece, ignoring some pieces that have
already been explained above.



```cpp
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}
```

 This is the callback function that will get
called when a new message has arrived on the `chatter` topic. The
message is passed in a
[boost shared_ptr](http://www.boost.org/doc/libs/1_37_0/libs/smart_ptr/shared_ptr.htm),
which means you can store it off if you want, without worrying about it
getting deleted underneath you, and without copying the underlying data.



```cpp
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);
```

 Subscribe to the `chatter` topic with the
master. ROS will call the `chatterCallback()` function whenever a new
message arrives. The 2nd argument is the queue size, in case we are not
able to process messages fast enough. In this case, if the queue reaches
1000 messages, we will start throwing away old messages as new ones
arrive.

`NodeHandle::subscribe()` returns a `ros::Subscriber` object, that
you must hold on to until you want to unsubscribe. When the Subscriber
object is destructed, it will automatically unsubscribe from the
`chatter` topic.

There are versions of the `NodeHandle::subscribe()` function which
allow you to specify a class member function, or even anything callable
by a Boost.Function object. The
[roscpp overview](https://index.ros.org/p/roscpp) contains more
information.



```cpp
  ros::spin();
```

 `ros::spin()` enters a loop, calling message
callbacks as fast as possible. Don't worry though, if there's nothing
for it to do it won't use much CPU. `ros::spin()` will exit once
`ros::ok()` returns false, which means `ros::shutdown()` has been
called, either by the default Ctrl-C handler, the master telling us to
shutdown, or it being called manually.

There are other ways of pumping callbacks, but we won't worry about
those here. The roscpp_tutorials
package has some demo applications which demonstrate this. The
[roscpp overview](https://index.ros.org/p/roscpp) also contains more
information.

Again, here's a condensed version of what's going on:

- Initialize the ROS system
- Subscribe to the `chatter` topic
- Spin, waiting for messages to arrive
- When a message arrives, the `chatterCallback()` function is called



```
{#!wiki buildsystem rosbuild
== Building your nodes ==
[[roscreate|roscreate-pkg]] will create a default Makefile and CMakeLists.txt for your package. 
 
{{{
$ rosed beginner_tutorials CMakeLists.txt
```



It should look something like this:



```
cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)

# Set the build type.  Options are:
#  Coverage       : w/ debug symbols, w/o optimization, w/ code-coverage
#  Debug          : w/ debug symbols, w/o optimization
#  Release        : w/o debug symbols, w/ optimization
#  RelWithDebInfo : w/ debug symbols, w/ optimization
#  MinSizeRel     : w/o debug symbols, w/ optimization, stripped binaries
#set(ROS_BUILD_TYPE RelWithDebInfo)

rosbuild_init()

#set the default path for built executables to the "bin" directory
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
#set the default path for built libraries to the "lib" directory
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

#uncomment if you have defined messages
#rosbuild_genmsg()
#uncomment if you have defined services
#rosbuild_gensrv()

#common commands for building c++ executables and libraries
#rosbuild_add_library(${PROJECT_NAME} src/example.cpp)
#target_link_libraries(${PROJECT_NAME} another_library)
#rosbuild_add_boost_directories()
#rosbuild_link_boost(${PROJECT_NAME} thread)
#rosbuild_add_executable(example examples/example.cpp)
#target_link_libraries(example ${PROJECT_NAME})
```

 Adding the following at the bottom:



```
rosbuild_add_executable(talker src/talker.cpp)
rosbuild_add_executable(listener src/listener.cpp)
```

 This will create two executables, `talker`
and `listener`, which by default will go into the "bin" directory.

For more information on using CMake with ROS, see
[CMakeLists](CMakeLists) Now run make: 

```
$ make
```

 }}}}



```
{#!wiki buildsystem catkin
== Building your nodes ==
You used [[catkin/commands/catkin_create_pkg|catkin_create_pkg]] in a previous tutorial which created a [[catkin/package_manifest|package.xml]] and a [[catkin/CMakeLists.txt|CMakeLists.txt]] file for you.

The generated [[catkin/CMakeLists.txt|CMakeLists.txt]] should look like this (with modifications from the [[ROS/Tutorials/CreatingMsgAndSrv|Creating Msgs and Srvs]] tutorial and unused comments and examples removed):

<<GetTaggedCode(https://raw.github.com/ros/catkin_tutorials/master/create_package_modified/catkin_ws/src/beginner_tutorials/CMakeLists.txt,xml,FULLTEXT,show_uri,no_tag_newlines,global_lines)>>

Don't worry about modifying the commented (#) examples, simply add these few lines to the bottom of your [[catkin/CMakeLists.txt|CMakeLists.txt]]:

{{{
add_executable(talker src/talker.cpp)
target_link_libraries(talker ${catkin_LIBRARIES})
add_dependencies(talker beginner_tutorials_generate_messages_cpp)

add_executable(listener src/listener.cpp)
target_link_libraries(listener ${catkin_LIBRARIES})
add_dependencies(listener beginner_tutorials_generate_messages_cpp)
```



Your resulting [CMakeLists.txt](https://index.ros.org/p/catkin) file
should look like this:

Source:
[CMakeLists.txt](https://github.com/ros/catkin_tutorials/blob/master/create_package_pubsub/catkin_ws/src/beginner_tutorials/CMakeLists.txt)



```xml
cmake_minimum_required(VERSION 2.8.3)
project(beginner_tutorials)

## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs genmsg)

## Declare ROS messages and services
add_message_files(FILES Num.msg)
add_service_files(FILES AddTwoInts.srv)

## Generate added messages and services
generate_messages(DEPENDENCIES std_msgs)

## Declare a catkin package
catkin_package()

## Build talker and listener
include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(talker src/talker.cpp)
target_link_libraries(talker ${catkin_LIBRARIES})
add_dependencies(talker beginner_tutorials_generate_messages_cpp)

add_executable(listener src/listener.cpp)
target_link_libraries(listener ${catkin_LIBRARIES})
add_dependencies(listener beginner_tutorials_generate_messages_cpp)
```



This will create two executables, `talker` and `listener`, which by
default will go into package directory of your
[devel space](https://index.ros.org/p/catkin), located by default at
`/catkin_ws/devel/lib/<package name>`.

Note that you have to add dependencies for the executable targets to
message generation targets: 

```
add_dependencies(talker beginner_tutorials_generate_messages_cpp)
```

 This makes sure
message headers of this package are generated before being used. If you
use messages from other packages inside your catkin workspace, you need
to add dependencies to their respective generation targets as well,
because catkin builds all projects in parallel. As of \*Groovy\* you can
use the following variable to depend on all necessary targets:


```
target_link_libraries(talker ${catkin_LIBRARIES})
```



You can invoke executables directly or you can use rosrun to invoke
them. They are not placed in '<prefix>/bin' because that would
pollute the PATH when installing your package to the system. If you wish
for your executable to be on the PATH at installation time, you can
setup an install target, see:
[CMakeLists.txt](https://index.ros.org/p/catkin)

For more detailed discription of the
[CMakeLists.txt](https://index.ros.org/p/catkin) file see:
[CMakeLists.txt](https://index.ros.org/p/catkin)

Now run `catkin_make`: 

```
# In your catkin workspace
$ cd ~/catkin_ws
$ catkin_make
```

 Note: Or if you're
adding as new pkg, you may need to tell catkin to force making by
`\--force-cmake` option. See
[using_a_workspace](https://index.ros.org/p/catkin).

}}}}

### Running the nodes

Running nodes requires you have a ROS core started. Open a new shell,
and type:



```
roscore
```



If all goes well, you should see an output that looks something like
this:



```
... logging to /u/takayama/.ros/logs/83871c9c-934b-11de-a451-001d927076eb/roslaunch-ads-31831.log
... loading XML file [/wg/stor1a/rosbuild/shared_installation/ros/tools/roslaunch/roscore.xml]
Added core node of type [rosout/rosout] in namespace [/]
started roslaunch server http://ads:54367/

SUMMARY
======

NODES

changing ROS_MASTER_URI to [http://ads:11311/] for starting master locally
starting new master (master configured for auto start)
process[master]: started with pid [31874]
ROS_MASTER_URI=http://ads:11311/
setting /run_id to 83871c9c-934b-11de-a451-001d927076eb
+PARAM [/run_id] by /roslaunch
+PARAM [/roslaunch/uris/ads:54367] by /roslaunch
process[rosout-1]: started with pid [31889]
started core service [/rosout]
+SUB [/time] /rosout http://ads:33744/
+SERVICE [/rosout/get_loggers] /rosout http://ads:33744/
+SERVICE [/rosout/set_logger_level] /rosout http://ads:33744/
+PUB [/rosout_agg] /rosout http://ads:33744/
+SUB [/rosout] /rosout http://ads:33744/
```





```
{#!wiki buildsystem rosbuild
Now everything is set to run talker/listener.  Open a new shell, go to the talker_listener package and type:

{{{
./bin/talker
```

 Now in the original shell type:



```
./bin/listener
```

 }}}} 

```
{#!wiki buildsystem catkin
Now everything is set to run talker/listener.  Open a new shell, go to the your catkin workspace and type:

{{{
source ./devel/setup.bash
rosrun beginner_tutorials talker
```

 Now in the
original shell type:



```
rosrun beginner_tutorials listener
```

 }}}} Talker should begin outputting text
similar to:



```
[ INFO] I published [Hello there! This is message [0]]
[ INFO] I published [Hello there! This is message [1]]
[ INFO] I published [Hello there! This is message [2]]
...
```

 And listener should begin outputting text
similar to:



```
[ INFO] Received [Hello there! This is message [20]]
[ INFO] Received [Hello there! This is message [21]]
[ INFO] Received [Hello there! This is message [22]]
...
```

 Congratulations! You've just run your first
ROS nodes. For more example code, see the
roscpp_tutorials package.

**Next Tutorial**:
[Writing a simple service and client](#writing-a-simple-service-and-client)

------------------------------------------------------------------------

## Writing a Simple Service and Client

### Writing a Service Node

Here we'll create the service ("add_two_ints_server") node which will
receive two ints and return the sum.



```
{#!wiki buildsystem rosbuild
Change directory into the beginner_tutorials package, you created previously in the [[ROS/Tutorials/CreatingPackage|creating a rosbuild package]] tutorial:

{{{
roscd beginner_tutorials
```



}}}}



```
{#!wiki buildsystem catkin
Change directories to your beginner_tutorials package you created in your catkin workspace previous tutorials:

{{{
roscd beginner_tutorials
```



}}}}

Please make sure you have followed the directions in the previous
tutorial for creating the service needed in this tutorial,
[creating the AddTwoInts.srv](ROS/Tutorials/CreatingMsgAndSrv#Creating_a_srv)
(be sure to choose the right version of build tool you're using at the
top of wiki page in the link).

#### The Code

Create the src/add_two_ints_server.cpp file within the
beginner_tutorials package and paste the following inside it:



```cplusplus
#include "ros/ros.h"
#include "beginner_tutorials/AddTwoInts.h"

bool add(beginner_tutorials::AddTwoInts::Request  &req,
         beginner_tutorials::AddTwoInts::Response &res)
{
  res.sum = req.a + req.b;
  ROS_INFO("request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
  ROS_INFO("sending back response: [%ld]", (long int)res.sum);
  return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "add_two_ints_server");
  ros::NodeHandle n;

  ros::ServiceServer service = n.advertiseService("add_two_ints", add);
  ROS_INFO("Ready to add two ints.");
  ros::spin();

  return 0;
}
```



#### The Code Explained

Now, let's break the code down. `beginner_tutorials/AddTwoInts.h` is
the header file generated from the srv file that we created earlier.
This function provides the service for adding two ints, it takes in the
request and response type defined in the srv file and returns a boolean.
Here the two ints are added and stored in the response. Then some
information about the request and response are logged. Finally the
service returns true when it is complete. Here the service is created
and advertised over ROS.

### Writing the Client Node

#### The Code

Create the src/add_two_ints_client.cpp file within the
beginner_tutorials package and paste the following inside it:



```cplusplus
#include "ros/ros.h"
#include "beginner_tutorials/AddTwoInts.h"
#include <cstdlib>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "add_two_ints_client");
  if (argc != 3)
  {
    ROS_INFO("usage: add_two_ints_client X Y");
    return 1;
  }

  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<beginner_tutorials::AddTwoInts>("add_two_ints");
  beginner_tutorials::AddTwoInts srv;
  srv.request.a = atoll(argv[1]);
  srv.request.b = atoll(argv[2]);
  if (client.call(srv))
  {
    ROS_INFO("Sum: %ld", (long int)srv.response.sum);
  }
  else
  {
    ROS_ERROR("Failed to call service add_two_ints");
    return 1;
  }

  return 0;
}
```



#### The Code Explained

Now, let's break the code down. This creates a client for the
`add_two_ints` service. The `ros::ServiceClient` object is used to
call the service later on. Here we instantiate an autogenerated service
class, and assign values into its request member. A service class
contains two members, `request` and `response`. It also contains two
class definitions, `Request` and `Response`. This actually calls the
service. Since service calls are blocking, it will return once the call
is done. If the service call succeeded, `call()` will return true and
the value in `srv.response` will be valid. If the call did not
succeed, `call()` will return false and the value in `srv.response`
will be invalid.



```
{#!wiki buildsystem rosbuild
== Building your nodes ==
Again edit the beginner_tutorials CMakeLists.txt:
{{{
$ rosed beginner_tutorials CMakeLists.txt
```

 and add the following at the end:


```
rosbuild_add_executable(add_two_ints_server src/add_two_ints_server.cpp)
rosbuild_add_executable(add_two_ints_client src/add_two_ints_client.cpp)
```

 This will create two executables,
"add_two_ints_server" and "add_two_ints_client", which by default
will go into the "bin" directory.

For more information on using CMake with ROS, see
[CMakeLists](CMakeLists) Now run make: 

```
$ make
```

 }}}}


```
{#!wiki buildsystem catkin
== Building your nodes ==
Again edit the beginner_tutorials CMakeLists.txt located at `~/catkin_ws/src/beginner_tutorials/CMakeLists.txt` and add the following at the end:

<<GetTaggedCode(https://raw.github.com/ros/catkin_tutorials/master/create_package_srvclient/catkin_ws/src/beginner_tutorials/CMakeLists.txt,xml,SRVCLIENT,show_uri,no_tag_newlines,global_lines)>>


This will create two executables, `add_two_ints_server` and `add_two_ints_client`, which by default will go into package directory of your [[catkin/workspaces#Development_.28Devel.29_Space|devel space]], located by default at `~/catkin_ws/devel/lib/<package name>`. You can invoke executables directly or you can use rosrun to invoke them. They are not placed in '<prefix>/bin' because that would pollute the PATH when installing your package to the system. If you wish for your executable to be on the PATH at installation time, you can setup an install target, see: [[catkin/CMakeLists.txt]]

For more detailed description of the [[catkin/CMakeLists.txt|CMakeLists.txt]] file see: [[catkin/CMakeLists.txt]]

Now run `catkin_make`:
{{{
# In your catkin workspace
cd ~/catkin_ws
catkin_make
```

 }}}}

If your build fails for some reason:

- make sure you have followed the directions in the previous tutorial:
  [creating the AddTwoInts.srv](ROS/Tutorials/CreatingMsgAndSrv#Creating_a_srv).
  

```wiki
 * type `rosls beginner_tutorials/srv_gen/cpp/include/beginner_tutorials/` and check that the `.h` file matches the include in the client and server `.cpp` files.
```



### Running the nodes

Running nodes requires you have a ROS core started. Open a new shell,
and type:



```
roscore
```

 If all goes well, you should see an output that
looks something like this:



```
... logging to /u/takayama/.ros/logs/83871c9c-934b-11de-a451-
001d927076eb/roslaunch-ads-31831.log
... loading XML file 
[/wg/stor1a/rosbuild/shared_installation/ros/tools/roslaunch/roscore.xml]
Added core node of type [rosout/rosout] in namespace [/]
started roslaunch server http://ads:54367/

SUMMARY
======

NODES

changing ROS_MASTER_URI to [http://ads:11311/] for starting master locally
starting new master (master configured for auto start)
process[master]: started with pid [31874]
ROS_MASTER_URI=http://ads:11311/
setting /run_id to 83871c9c-934b-11de-a451-001d927076eb
+PARAM [/run_id] by /roslaunch
+PARAM [/roslaunch/uris/ads:54367] by /roslaunch
process[rosout-1]: started with pid [31889]
started core service [/rosout]
+SUB [/time] /rosout http://ads:33744/
+SERVICE [/rosout/get_loggers] /rosout http://ads:33744/
+SERVICE [/rosout/set_logger_level] /rosout http://ads:33744/
+PUB [/rosout_agg] /rosout http://ads:33744/
+SUB [/rosout] /rosout http://ads:33744/
```



Now everything is set to run server and client.

#### Running the Server



```
{#!wiki buildsystem catkin
Start by running the server. Open a new shell and type:

{{{
rosrun beginner_tutorials add_two_ints_server
```



You should see something similar to: 

```
Ready to add two ints.
```

 }}}}

#### Running the Client



```
{#!wiki buildsystem catkin
Now let's run the client with the necessary arguments, in another shell:
{{{
$ rosrun beginner_tutorials add_two_ints_client 1 3
```



In the client's shell, you should see something similar to:


```
Sum: 4
```



In the server's shell, instead, you should see something similar to:


```
request: x=1, y=3
sending back response: [4]
```

 }}}}

**Next Tutorial:**
[Using Parameters in roscpp](#using-parameters-in-roscpp)

## Using Parameters in roscpp

### Retrieving Parameters

There are two methods to retrieve parameters with `NodeHandle`. In the
following example code, `n` is an instance of `NodeHandle`.

#### getParam()

`getParam()` has a number of overloads which all follow the same basic
form: 

```cplusplus
bool getParam (const std::string& key, parameter_type& output_value) const
```



- **key** is a [Graph Resource Name](Names)
- **output_value** is the place to put the retrieved data, where
  parameter_type is one of bool, int, double, string, or a special
  `XmlRpcValue` type which can represent any type and also lists/maps.

Use of `getParam()` is fairly simple: 

```cpp
std::string s;
n.getParam("my_param", s);
```



Note that `getParam()` returns a bool, which provides the ability to
check if retrieving the parameter succeeded or not:


```cpp
std::string s;
if (n.getParam("my_param", s))
{
  ROS_INFO("Got param: %s", s.c_str());
}
else
{
  ROS_ERROR("Failed to get param 'my_param'");
}
```



#### param()

`param()` is similar to `getParam()`, but allows you to specify a
default value in the case that the parameter could not be retrieved:



```cpp
int i;
n.param("my_num", i, 42);
```



Sometimes the compiler requires a hint for the string type.


```cpp
std::string s;
n.param<std::string>("my_param", s, "default_value");
```



### Setting Parameters

Setting parameters is done through the `setParam()` methods:


```cpp
n.setParam("my_param", "hello there");
```



`setParam()`, like `getParam()`, can take bool, int, double, string,
and a special `XmlRpcValue` type

### Deleting Parameters

Deleting parameters is done through the `deleteParam()` method:


```cpp
n.deleteParam("my_param");
```



### Checking for Existence

This is not usually necessary, but there is a `hasParam()` method that
allows you to check for a parameter's existence:


```cpp
if (!n.hasParam("my_param"))
{
  ROS_INFO("No param named 'my_param'");
}
```



### Searching for Parameters

The [Parameter Server](Parameter Server) allows you to "search" for
parameters, starting at your namespace and working through your parent
namespaces.

For example, if the parameter `/a/b` exists in the parameter server,
and your `NodeHandle` is in the `/a/c` namespace, `searchParam()`
for `b` will yield `/a/b`. However, if parameter `/a/c/b` is
added, `searchParam()` for `b` will now yield `/a/c/b`.



```cpp
std::string param_name;
if (n.searchParam("b", param_name))
{
  // Found parameter, can now query it using param_name
  int i = 0;
  n.getParam(param_name, i);
}
else
{
  ROS_INFO("No param 'b' found in an upward search");
}
```



**Next Tutorial**:
[Accessing Private Names with NodeHandle](#accessing-private-names-from-a-nodehandle)

## Accessing Private Names from a NodeHandle

### Why not just \~name?

The introduction of `NodeHandles` in roscpp created something of a
conundrum when dealing with private names. If I create a `NodeHandle`
with its own namespace: 

```cplusplus
ros::init(argc, argv, "my_node_name");
ros::NodeHandle nh("/my_node_handle_namespace");
```



Where should a private name resolve? Some options would be:

- `/my_node_handle_namespace/my_node_name/name`
- `my_node_name/my_node_handle_namespace/name`
- `/my_node_handle_namespace/name`
- Something else entirely

For this reason, `NodeHandle` does not allow passing private names
directly to its methods, or to constructors that take a `NodeHandle`
as an argument.

### Accessing Private Names

The solution is to construct a `NodeHandle` with a private name as its
namespace: 

```cplusplus
ros::init(argc, argv, "my_node_name");
ros::NodeHandle nh1("~");  // must be in main()
ros::NodeHandle nh2("~foo");
```



`nh1`'s namespace is `/my_node_name`, and `nh2`'s namespace is
`/my_node_name/foo`.

So instead of doing this: 

```cplusplus
ros::NodeHandle nh;
nh.getParam("~name", ... );
```



You do this: 

```cplusplus
ros::NodeHandle nh("~");
nh.getParam("name", ... );
```



**Next Tutorial**:
[Using Class Methods as Callbacks](#using-class-methods-as-callbacks)

## Using Class Methods as Callbacks

/!\\ if no code snippet is shown where it's supposed to be or anything
strange in the code shown, please open the link. Code snippet macro
might not be working well with github, which is being investigated.

### Subscriptions

Suppose you have a simple class, `Listener`:

Source:
[listener_class.cpp](https://github.com/ros/ros_tutorials/blob/groovy-devel/roscpp_tutorials/listener_class/listener_class.cpp)



```cpp
class Listener
{
public:
  void callback(const std_msgs::String::ConstPtr& msg);
};
```



Where the `NodeHandle::subscribe()` call using a function would have
looked like this:

Source:
[listener.cpp](https://github.com/ros/ros_tutorials/blob/groovy-devel/roscpp_tutorials/listener/listener.cpp)



```cpp
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);
```



Using a class method looks like this:

Source:
[listener_class.cpp](https://github.com/ros/ros_tutorials/blob/groovy-devel/roscpp_tutorials/listener_class/listener_class.cpp)



```cpp
  Listener listener;
  ros::Subscriber sub = n.subscribe("chatter", 1000, &Listener::callback, &listener);
```



If the subscriber is **inside** the class Listener, you can replace the
last argument with the keyword **this**, which means that the subscriber
will refer to the class it is part of.

### Service Servers

Suppose you have a simple class, `AddTwo`:

Source:
[add_two_ints_server_class.cpp](https://github.com/ros/ros_tutorials/blob/groovy-devel/roscpp_tutorials/add_two_ints_server_class/add_two_ints_server_class.cpp)



```cpp
class AddTwo
{
public:
  bool add(roscpp_tutorials::TwoInts::Request& req,
           roscpp_tutorials::TwoInts::Response& res);
};
```



Where the old `NodeHandle::advertiseService()` call would look like:

Source:
[add_two_ints_server.cpp](https://github.com/ros/ros_tutorials/blob/groovy-devel/roscpp_tutorials/add_two_ints_server/add_two_ints_server.cpp)



```cpp
  ros::ServiceServer service = n.advertiseService("add_two_ints", add);
```



The class version looks like this:

Source:
[add_two_ints_server_class.cpp](https://github.com/ros/ros_tutorials/blob/groovy-devel/roscpp_tutorials/add_two_ints_server_class/add_two_ints_server_class.cpp)



```cpp
  AddTwo a;
  ros::ServiceServer ss = n.advertiseService("add_two_ints", &AddTwo::add, &a);
```



For the full set of `subscribe()`, `advertiseService()`, etc.
overloads, see the
[NodeHandle class documentation](http://www.ros.org/doc/api/roscpp/html/classros_1_1NodeHandle.html)

## Understanding Timers

### What are Timers?

Timers let you schedule a callback to happen at a specified rate. They
are a more flexible and useful form of the `ros::Rate` used in the
[Writing a Simple Publisher and Subscriber](ROS/Tutorials/WritingPublisherSubscriber(c++))
tutorial.

Note that Timers are **not** a realtime thread/kernel replacement, and
make no guarantees about how accurate they are, which can vary wildly
because of system load/capabilities.

See also: [roscpp Timers overview](https://index.ros.org/p/roscpp)

### Using Timers

Creating a Timer works very similar to creating a Subscriber.



```cplusplus
ros::Timer timer = n.createTimer(ros::Duration(0.1), timerCallback);
```



Timer callbacks take the form: 

```cplusplus
void timerCallback(const ros::TimerEvent& e);
```



### A full example

Now that you've seen the basics, let's go through a larger example,
with multiple Timers.

#### The code



```cpp
/*
 * Copyright (C) 2008, Morgan Quigley and Willow Garage, Inc.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *   * Redistributions of source code must retain the above copyright notice,
 *     this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *   * Neither the names of Stanford University or Willow Garage, Inc. nor the names of its
 *     contributors may be used to endorse or promote products derived from
 *     this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#include "ros/ros.h"

/**
 * This tutorial demonstrates the use of timer callbacks.
 */

void callback1(const ros::TimerEvent&)
{
  ROS_INFO("Callback 1 triggered");
}

void callback2(const ros::TimerEvent&)
{
  ROS_INFO("Callback 2 triggered");
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "talker");
  ros::NodeHandle n;

  /**
   * Timers allow you to get a callback at a specified rate.  Here we create
   * two timers at different rates as a demonstration.
   */
  ros::Timer timer1 = n.createTimer(ros::Duration(0.1), callback1);
  ros::Timer timer2 = n.createTimer(ros::Duration(1.0), callback2);

  ros::spin();

  return 0;
}
```



#### The code explained

I'll ignore parts that have been explained in previous tutorials, which
really just leaves two lines: 

```cpp
ros::Timer timer1 = n.createTimer(ros::Duration(0.1), callback1);
ros::Timer timer2 = n.createTimer(ros::Duration(1.0), callback2);
```

 Here we create
two timers, one which fires every 100 milliseconds, and one which fires
every second. If you run this program, it should output something like
the following: 

```
[ INFO] 1251854032.362376000: Callback 1 triggered
[ INFO] 1251854032.462840000: Callback 1 triggered
[ INFO] 1251854032.562464000: Callback 1 triggered
[ INFO] 1251854032.662169000: Callback 1 triggered
[ INFO] 1251854032.762649000: Callback 1 triggered
[ INFO] 1251854032.862853000: Callback 1 triggered
[ INFO] 1251854032.962642000: Callback 1 triggered
[ INFO] 1251854033.063118000: Callback 1 triggered
[ INFO] 1251854033.162221000: Callback 1 triggered
[ INFO] 1251854033.262749000: Callback 1 triggered
[ INFO] 1251854033.262864000: Callback 2 triggered
[ INFO] 1251854033.362643000: Callback 1 triggered
[ INFO] 1251854033.463158000: Callback 1 triggered
...
```



### The TimerEvent Structure

The `ros::TimerEvent` structure provides you information about the
timing of the current timer. Here is its definition:


```cplusplus
struct TimerEvent
{
  Time last_expected;                     ///< In a perfect world, this is when the last callback should have happened
  Time last_real;                         ///< When the last callback actually happened

  Time current_expected;                  ///< In a perfect world, this is when the current callback should be happening
  Time current_real;                      ///< This is when the current callback was actually called (Time::now() as of the beginning of the callback)

  struct
  {
    WallDuration last_duration;           ///< How long the last callback ran for, always in wall-clock time
  } profile;
};
```

## Writing Publisher/Subscriber with Parameters, Dynamic Reconfigure and Custom Messages

### Writing Publisher/Subscriber Nodes with Parameters, Dynamic Reconfigure and Custom Messages

1\.
[ Writing Publisher/Subscriber with dynamic reconfigure and parameter server (C++)](ROSNodeTutorialC++ )
This tutorial covers writing a publisher and a subscriber in C++. The
use of custom messages and a publisher with a dynamic reconfigure server
are covered.

1\.
[ Writing Publisher/Subscriber with dynamic reconfigure and parameter server (Python)](ROSNodeTutorialPython )
This tutorial covers writing a publisher and a subscriber in Python. The
use of custom messages and a publisher with a dynamic reconfigure server
are covered.

1\.
[ Combining C++/Python Publisher/Subscriber](ROSNodeTutorialC++Python )
This tutorial shows how to mix publishers and subscribers written in C++
and Python.
