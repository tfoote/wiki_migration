## Viewing the Code

rospy_tutorials is a series of tutorials for using the
[rospy](https://index.ros.org/p/rospy) client API. You can browse these
tutorials by `roscd`-ing to the `rospy_tutorials` package, i.e.


```
roscd rospy_tutorials
```



and viewing what is there. Many of these tutorials are also discussed in
the Wiki tutorials listed below.

## Beginner Tutorials

- [Writing a Simple Publisher and Subscriber](#writing-a-simple-publisher-and-subscriber):
  This demo will walk you through creating a ROS package as well as
  creating two simple rospy nodes. The "talker" node will broadcast a
  message on topic "chatter", while the "listener" node will receive
  and print that message.
- [Writing a Simple Service and Client](#writing-a-simple-service-and-client):
  This tutorial covers how to write a service and client node in python.
- [Using Parameters in rospy](#using-parameters-in-rospy):
  This tutorial covers the various ways in which you can get and set
  [Parameters](Parameters) in [rospy](https://index.ros.org/p/rospy).
  Getting, setting and deleting parameters from a rospy [Node](Nodes) is
  fairly simple.
- [Logging with rospy](#logging-with-rospy):
  Logging messages to [rosout](https://index.ros.org/p/rosout) is easy
  with [rospy](https://index.ros.org/p/rospy) and encouraged. When you
  are running many [nodes](Nodes), seeing the command-line output of
  your node gets very difficult. Instead, it is much easier to publish a
  debugging message to [rosout](https://index.ros.org/p/rosout) and then
  view it with [rqt_console](https://index.ros.org/p/rqt_console) /
  [rxconsole](rxconsole). \*console is "over-console" of ROS and lets
  you view and filter the logging messages from all ROS nodes.
- [Writing a ROS Python Makefile](#writing-a-ros-python-makefile):
  I know what you're saying: "Python\... *Makefile*?" Believe it or
  not, you do need `Makefile` (and [CMakeLists](CMakeLists)), even if
  you just hack Python all day.
- [Setting Up Your PYTHONPATH](#setting-up-your-pythonpath):
  What to do to find other python modules
- [Using numpy with rospy](#using-numpy-with-rospy):
  This tutorial covers using [numpy](http://numpy.scipy.org/) with
  [rospy](https://index.ros.org/p/rospy), the ROS Python client library.
  Numpy is a popular scientific computing package for Python. You will
  often want to consider using Numpy with rospy if you are working with
  sensor data as it has better performance and many libraries for
  manipulating arrays of data.

## Intermediate Tutorials

- [Publishing messages in rospy](#publishing-messages-in-rospy):
  [Writing a simple publisher and subscriber](#writing-a-simple-publisher-and-subscriber)
  already introduced you to the basics of creating
  [rospy](https://index.ros.org/p/rospy) [Nodes](Nodes) that publish and
  receive messages on ROS [Topics](Topics). As you get more experienced
  with ROS and rospy, you may wish to learn some advanced syntax for
  publishing that will save you some typing \-- as well as make your
  code more robust to future changes.
- [Python CompressedImage Subscriber Publisher](#python-compressedimage-subscriber-publisher):
  This example subscribes to a ros topic containing
  sensor_msgs::CompressedImage. It converts the CompressedImage into a
  numpy.ndarray, then detects and marks features in that image. It
  finally displays and publishes the new image - again as
  CompressedImage topic.

## Create a new tutorial

## Writing a Simple Publisher and Subscriber

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [understanding ROS services and params](ROS/Tutorials/UnderstandingServicesParams).
- **Description:** This demo will walk you through creating a ROS
  package as well as creating two simple rospy nodes. The "talker"
  node will broadcast a message on topic "chatter", while the
  "listener" node will receive and print that message.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Writing a simple service and client](#writing-a-simple-service-and-client)

### Writing the Publisher Node

"Node" is the ROS term for an executable that is connected to the ROS
network. Here we'll create the publisher ("talker") node which will
continually broadcast a message.

Change directory into the beginner_tutorials package, you created in the
earlier tutorial, [creating a package](ROS/Tutorials/CreatingPackage):


```
$ roscd beginner_tutorials
```



#### The Code

First lets create a 'scripts' folder to store our Python scripts in:



```
$ mkdir scripts
$ cd scripts
```



Then download the example script
[talker.py](https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/talker.py)
to your new `scripts` directory and make it executable:



```
$ wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/talker.py
$ chmod +x talker.py
```



We will not run it yet. You can view and edit the file with
` $ rosed beginner_tutorials talker.py ` or just look below.



```python
#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
```



Add the following to your `CMakeLists.txt`. This makes sure the python
script gets installed properly, and uses the right python interpreter.



```cmake
catkin_install_python(PROGRAMS scripts/talker.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```



#### The Code Explained

Now, let's break the code down. Every Python ROS [Node](Nodes) will
have this declaration at the top. The first line makes sure your script
is executed as a Python script. You need to import `rospy` if you are
writing a ROS [Node](Nodes). The `std_msgs.msg` import is so that we can
reuse the `std_msgs/String` message type (a simple string container) for
publishing. This section of code defines the talker's interface to the
rest of ROS. `pub = rospy.Publisher("chatter", String, queue_size=10)`
declares that your node is publishing to the `chatter` topic using the
message type `String`. `String` here is actually the class
`std_msgs.msg.String`. The `queue_size` argument is and limits the
amount of queued messages if any subscriber is not receiving them fast
enough. In older ROS distributions just omit the argument.

The next line, `rospy.init_node(NAME, ...)`, is very important as it
tells rospy the name of your node \-- until rospy has this information,
it cannot start communicating with the ROS [Master](Master). In this
case, your node will take on the name `talker`. NOTE: the name must be a
[base name](Names), i.e. it cannot contain any slashes `"/"`.

`anonymous = True` ensures that your node has a unique name by adding
random numbers to the end of `NAME`. Refer to
[Initialization and Shutdown - Initializing your ROS Node](https://index.ros.org/p/rospy)
in the `rospy` documentation for more information about node
initialization options. This line creates a `Rate` object `rate`.
With the help of its method `sleep()`, it offers a convenient way for
looping at the desired rate. With its argument of `10`, we should
expect to go through the loop 10 times per second (as long as our
processing time does not exceed 1/10th of a second!) This loop is a
fairly standard rospy construct: checking the `rospy.is_shutdown()` flag
and then doing work. You have to check `is_shutdown()` to check if
your program should exit (e.g. if there is a `Ctrl-C` or otherwise).
In this case, the "work" is a call to `pub.publish(hello_str)` that
publishes a string to our `chatter` topic. The loop calls
`rate.sleep()`, which sleeps just long enough to maintain the desired
rate through the loop.

(You may also run across `rospy.sleep()` which is similar to
`time.sleep()` except that it works with simulated time as well (see
[Clock](Clock)).)

This loop also calls `rospy.loginfo(str)`, which performs triple-duty:
the messages get printed to screen, it gets written to the Node's log
file, and it gets written to [rosout](https://index.ros.org/p/rosout).
[rosout](https://index.ros.org/p/rosout) is a handy tool for debugging:
you can pull up messages using
[rqt_console](https://index.ros.org/p/rqt_console) instead of having to
find the console window with your Node's output.

`std_msgs.msg.String` is a very simple message type, so you may be
wondering what it looks like to publish more complicated types. The
general rule of thumb is that *constructor args are in the same order as
in the `.msg` file*. You can also pass in no arguments and initialize
the fields directly, e.g.



```
msg = String()
msg.data = str
```



or you can initialize some of the fields and leave the rest with default
values:



```
String(data=str)
```



You may be wondering about the last little bit: In addition to the
standard Python `__main__` check, this catches a
`rospy.ROSInterruptException` exception, which can be thrown by
`rospy.sleep()` and `rospy.Rate.sleep()` methods when `Ctrl-C` is
pressed or your Node is otherwise shutdown. The reason this exception is
raised is so that you don't accidentally continue executing code after
the `sleep()`.

Now we need to write a node to receive the messages.

### Writing the Subscriber Node

#### The Code

Download the
[listener.py](https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/listener.py)
file into your scripts directory: 

```
$ roscd beginner_tutorials/scripts/
$ wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/listener.py
$ chmod +x listener.py
```

 The file
contents look close to: 

```python
#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
```



Then, edit the `catkin_install_python()` call in your
`CMakeLists.txt` so it looks like the following:



```cmake
catkin_install_python(PROGRAMS scripts/talker.py scripts/listener.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```



#### The Code Explained

The code for `listener.py` is similar to `talker.py`, except we've
introduced a new callback-based mechanism for subscribing to messages.
This declares that your node subscribes to the `chatter` topic which is
of type `std_msgs.msgs.String`. When new messages are received,
`callback` is invoked with the message as the first argument.

We also changed up the call to `rospy.init_node()` somewhat. We've
added the `anonymous=True` keyword argument. ROS requires that each node
have a unique name. If a node with the same name comes up, it bumps the
previous one. This is so that malfunctioning nodes can easily be kicked
off the network. The `anonymous=True` flag tells `rospy` to generate a
unique name for the node so that you can have multiple `listener.py`
nodes run easily.

The final addition, `rospy.spin()` simply keeps your node from exiting
until the node has been shutdown. Unlike roscpp, rospy.spin() does not
affect the subscriber callback functions, as those have their own
threads.

### Building your nodes

We use CMake as our build system and, yes, you have to use it even for
Python nodes. This is to make sure that the autogenerated Python code
for messages and services is created.



```
{{#!wiki buildsystem rosbuild
We also use a Makefile for a bit of convenience.
{{{roscreate-pkg
```

 automatically created a Makefile, so you
don't have to edit it.

Now run make: 

```
$ make
```

 }}}}}



```
{#!wiki buildsystem catkin
Go to your catkin workspace and run `catkin_make`:

{{{
$ cd ~/catkin_ws
$ catkin_make
```

 }}}}

### Running the nodes

Running nodes requires you have a ROS core started. A ROS core is a
collection of nodes and programs that are pre-requisites of a ROS-based
system. You must have a roscore running in order for ROS nodes to
communicate. Open a new shell, and type:



```
$ roscore
```



`roscore` will output something similar to this:


```
... logging to /u/nkoenig/ros-jaunty/ros/log/d92b213a-90d4-11de-9344-00301b8246bf/roslaunch-ncq-11315.log
... loading XML file [/u/nkoenig/ros-jaunty/ros/tools/roslaunch/roscore.xml]
Added core node of type [rosout/rosout] in namespace [/]
started roslaunch server http://ncq:60287/

SUMMARY
======

NODES

starting new master (master configured for auto start)
process[master]: started with pid [11338]
ROS_MASTER_URI=http://ncq:11311/
setting /run_id to d92b213a-90d4-11de-9344-00301b8246bf
+PARAM [/run_id] by /roslaunch
+PARAM [/roslaunch/uris/ncq:60287] by /roslaunch
process[rosout-1]: started with pid [11353]
started core service [/rosout]
+SERVICE [/rosout/get_loggers] /rosout http://ncq:36277/
+SERVICE [/rosout/set_logger_level] /rosout http://ncq:36277/
+SUB [/time] /rosout http://ncq:36277/
+PUB [/rosout_agg] /rosout http://ncq:36277/
+SUB [/rosout] /rosout http://ncq:36277/
```



Now everything is set to run talker/listener. Open a new shell and type:



```
$ rosrun beginner_tutorials talker.py
```

 Now in the original shell type:



```
$ rosrun beginner_tutorials listener.py
```

 `rosrun` is just a convenience script. You're
also free to just type `./talker.py`.

Talker should begin outputting text similar to:



```
[INFO] [WallTime: 1394915011.927728] hello world 1394915011.93
[INFO] [WallTime: 1394915012.027887] hello world 1394915012.03
[INFO] [WallTime: 1394915012.127884] hello world 1394915012.13
[INFO] [WallTime: 1394915012.227858] hello world 1394915012.23
...
```

 And listener should begin outputting text
similar to:



```
[INFO] [WallTime: 1394915043.555022] /listener_9056_1394915043253I heard hello world 1394915043.55
[INFO] [WallTime: 1394915043.654982] /listener_9056_1394915043253I heard hello world 1394915043.65
[INFO] [WallTime: 1394915043.754936] /listener_9056_1394915043253I heard hello world 1394915043.75
[INFO] [WallTime: 1394915043.854918] /listener_9056_1394915043253I heard hello world 1394915043.85
...
```

 Now that you've written your first listener
node, you should also know that ROS comes with its own generic listener
for any topic called [rostopic](https://index.ros.org/p/rostopic). If
you run `rostopic echo topic_name`, you get output similar to what you
wrote with `listener.py`:



```
$ rostopic echo chatter
```

 

```
data: hello world 1394915083.35
---
data: hello world 1394915083.45
---
data: hello world 1394915083.55
---
data: hello world 1394915083.65
---
data: hello world 1394915083.75
---
...
```

 Congratulations!
You've just run your first ROS python nodes. For more example code, see
the rospy_tutorials package, or move on
to the next tutorial
[WritingServiceClient](#writing-a-simple-service-and-client).
\-\-\-\--

## Writing a Simple Service and Client

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [examining the simple publisher and subscriber](ROS/Tutorials/ExaminingPublisherSubscriber).
- **Description:** This tutorial covers how to write a service and
  client node in python.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Using Parameters in rospy](#using-parameters-in-rospy)

### Writing a Service Node

Here we'll create the service ("add_two_ints_server") node which will
receive two ints and return the sum.



```wiki
Change directory into the beginner_tutorials package, you created in the earlier tutorial, [[ROS/Tutorials/CreatingPackage|creating a package]]:
```

 

```wiki
Change directory into the beginner_tutorials package, you created in the earlier tutorial, [[ROS/Tutorials/CreatingPackage?buildsystem=catkin|creating a package]]:
```




```
$ roscd beginner_tutorials
```

 Please make sure you have followed the
directions in the previous tutorial for creating the service needed in
this tutorial,
[creating the AddTwoInts.srv](ROS/Tutorials/CreatingMsgAndSrv#Creating_a_srv)
(be sure to choose the right version of build tool you're using at the
top of wiki page in the link).

#### The Code

Create the **scripts/add_two_ints_server.py** file within the
beginner_tutorials package and paste the following inside it:



```
{#!wiki buildsystem rosbuild
{{{
#!python block=service
#!/usr/bin/env python
import roslib; roslib.load_manifest('beginner_tutorials')
from beginner_tutorials.srv import *
import rospy

def handle_add_two_ints(req):
    print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print "Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
```

 }}}} 

```
{#!wiki buildsystem catkin
{{{
#!python block=service
#!/usr/bin/env python

from __future__ import print_function

from beginner_tutorials.srv import AddTwoInts,AddTwoIntsResponse
import rospy

def handle_add_two_ints(req):
    print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
```

 }}}} Don't
forget to make the node executable:

. 

```
chmod +x scripts/add_two_ints_server.py
```



Add the following to your `CMakeLists.txt`. This makes sure the python
script gets installed properly, and uses the right python interpreter.



```cmake
catkin_install_python(PROGRAMS scripts/add_two_ints_server.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```



#### The Code Explained

Now, let's break the code down.

There's very little to writing a service using
[rospy](https://index.ros.org/p/rospy). We declare our node using
`init_node()` and then declare our service: This declares a new
service named `add_two_ints` with the `AddTwoInts` service type. All
requests are passed to `handle_add_two_ints` function.
`handle_add_two_ints` is called with instances of
`AddTwoIntsRequest` and returns instances of `AddTwoIntsResponse`.

Just like with the subscriber example, `rospy.spin()` keeps your code
from exiting until the service is shutdown.

### Writing the Client Node

#### The Code

Create the **scripts/add_two_ints_client.py** file within the
beginner_tutorials package and paste the following inside it:



```
{#!wiki buildsystem catkin
{{{
#!python block=client
#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import *

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp1 = add_two_ints(x, y)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s+%s"%(x, y))
    print("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))
```

 }}}} Don't forget to make the node executable:



```
$ chmod +x scripts/add_two_ints_client.py
```



Then, edit the `catkin_install_python()` call in your
`CMakeLists.txt` so it looks like the following:



```cmake
catkin_install_python(PROGRAMS scripts/add_two_ints_server.py scripts/add_two_ints_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```



#### The Code Explained

Now, let's break the code down.

The client code for calling services is also simple. For clients you
don't have to call `init_node()`. We first call: This is a
convenience method that blocks until the service named `add_two_ints`
is available.

Next we create a handle for calling the service:

We can use this handle just like a normal function and call it:

Because we've declared the type of the service to be `AddTwoInts`, it
does the work of generating the `AddTwoIntsRequest` object for you
(you're free to pass in your own instead). The return value is an
`AddTwoIntsResponse` object. If the call fails, a
`rospy.ServiceException` may be thrown, so you should setup the
appropriate `try/except` block.

### Building your nodes

We use CMake as our build system and, yes, you have to use it even for
Python nodes. This is to make sure that the
[autogenerated Python code for messages and services](http://www.ros.org/wiki/ROS/Tutorials/CreatingMsgAndSrv#Creating_a_srv)
is created.



```
{#!wiki buildsystem rosbuild
We also use a Makefile for a bit of convenience.
{{{roscreate-pkg
```

 automatically created a Makefile, so you
don't have to edit it.

Now run make: 

```
$ make
```

 }}}} 

```
{#!wiki buildsystem catkin
Go to your catkin workspace and run `catkin_make`.

{{{
# In your catkin workspace
$ cd ~/catkin_ws
$ catkin_make
```


}}}}

### Try it out!

In a **new terminal**, run



```
$ cd ~/catkin_ws
$ . devel/setup.bash
$ rosrun beginner_tutorials add_two_ints_server.py
```

 In a **new terminal**, run



```
$ cd ~/catkin_ws
$ . devel/setup.bash
$ rosrun beginner_tutorials add_two_ints_client.py
```

 . And you will see the usage information
printed, similar to 

```
/home/user/catkin_ws/src/beginner_tutorials/scripts/add_two_ints_client.py [x y]
```



Then run



```
$ rosrun beginner_tutorials add_two_ints_client.py 4 5
```

 . And you will get 

```
Requesting 4+5
4 + 5 = 9
```

 .
And the server will print out 

```
Returning [4 + 5 = 9]
```



Next tutorial:
[Parameters](#using-parameters-in-rospy).

## Using Parameters in rospy

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Writing a service and client](#writing-a-simple-service-and-client).
- **Description:** This tutorial covers the various ways in which you
  can get and set [Parameters](Parameters) in
  [rospy](https://index.ros.org/p/rospy). Getting, setting and deleting
  parameters from a rospy [Node](Nodes) is fairly simple.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Logging with rospy](#logging-with-rospy)

You may wish to view the "param_talker" tutorial in the
rospy_tutorials Package. It uses a
[roslaunch](https://index.ros.org/p/roslaunch) file to initialize some
Parameters and then runs a rospy Node that reads from those Parameters.


```
$ roscd rospy_tutorials/006_parameters
$ roslaunch param_talker.launch
```

 Following explains what you see when you run
the command above.

### Parameter Types

You can use integers, floats, strings and booleans as Parameter values.
You can also use lists and dictionaries of these types, though
dictionaries have additional meaning that can be very useful.

Dictionaries are equivalent to ROS [Namespaces](Names). They are an
effective way of grouping similar Parameters together so that you can
get and set them atomically. For example, if you had a set of gains:


```
/gains/P = 1.0
/gains/I = 2.0
/gains/D = 3.0
```



In rospy, you could set and access those values individually or together
as a dictionary. The Parameter `/gains` has the Python dictionary
value 

```
{'P': 1.0, 'I': 2.0, 'D': 3.0}
```



### Getting, Setting, and Deleting Parameters

Getting a parameter is as simple as calling
`rospy.get_param(param_name)`: 

```
# get a global parameter
rospy.get_param('/global_param_name')

# get a parameter from our parent namespace
rospy.get_param('param_name')

# get a parameter from our private namespace
rospy.get_param('~private_param_name')
```



You can also specify a default value if the parameter doesn't exist:


```
rospy.get_param('foo', 'default_value')
```



Similarly, you set a parameter by calling `rospy.set_param(param_name,
param_value)`: 

```
rospy.set_param('some_numbers', [1., 2., 3., 4.])
rospy.set_param('truth', True)
rospy.set_param('~private_bar', 1+2)
```



You can delete parameter by calling `rospy.delete_param(param_name)`:


```
rospy.delete_param('param_name')
```



If you don't know whether or not a parameter exists, you can call
`rospy.has_param(param_name)`: 

```
if rospy.has_param('to_delete'):
    rospy.delete_param('to_delete')
```



### Resolving Parameter Names

Names in ROS can be remapped and your Node may get pushed into a
namespace. rospy does most of the work for you by automatically
resolving any names you pass into `get_param`, `set_param`, etc\...
However, for debugging purposes, you may wish to print out the names of
the Parameters that you are accessing.

In order to determine what the actual name of a Parameter is, you should
call `rospy.resolve_name(name)`, e.g.:



```
value = rospy.get_param('~foo')
rospy.loginfo('Parameter %s has value %s', rospy.resolve_name('~foo'), value)
```



`rospy.resolve_name()` will apply any remapping rules and also figure
out your Node's namespace.

### Searching for a Parameter

In ROS, you can *search* for a Parameter if you don't know what
namespace it is set in. This search starts in the Node's private
namespace and proceeds upwards to the global namespace. In order to use
this search API in rospy, you can `rospy.search_param(param_name)` to
find the *resolved* Parameter name. You can then get and set the
Parameter normally, e.g.



```
full_param_name = rospy.search_param('foo')
param_value = rospy.get_param(full_param_name)
```



Next tutorial:
[numpy](#using-numpy-with-rospy).

## Logging with rospy

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [ROS tutorials](ROS/Tutorials).
- **Description:** Logging messages to
  [rosout](https://index.ros.org/p/rosout) is easy with
  [rospy](https://index.ros.org/p/rospy) and encouraged. When you are
  running many [nodes](Nodes), seeing the command-line output of your
  node gets very difficult. Instead, it is much easier to publish a
  debugging message to [rosout](https://index.ros.org/p/rosout) and then
  view it with [rqt_console](https://index.ros.org/p/rqt_console) /
  [rxconsole](rxconsole). \*console is "over-console" of ROS and lets
  you view and filter the logging messages from all ROS nodes.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [rospy Makefile](#writing-a-ros-python-makefile)

Before we look at how to use this in rospy, you should probably review
the [rosout verbosity levels](Verbosity Levels) so you know how to use
the various log levels properly. It's important to use the correct
level as others will see these messages as well and need to understand
them properly.

### rospy API

rospy has several methods for writing log messages, all starting with
"log":



```
rospy.logdebug(msg, *args)
rospy.logwarn(msg, *args)
rospy.loginfo(msg, *args)
rospy.logerr(msg, *args)
rospy.logfatal(msg, *args)
```



These levels have a one-to-one correspondence to the
[rosout verbosity levels](Verbosity Levels). There are four potential
places a log message may end up depending on the verbosity level:

- stdout: loginfo
- stderr: logerr, logfatal, logwarn (ROS 0.9)
- your Node's log file: all
- the `/rosout` Topic: loginfo, logwarn, logerr, logfatal

**NOTE**: Your messages will not appear on the `/rosout` Topic until
your Node is fully initialized, so you may not see the initial messages.
When you see a message in stdout *No handlers could be found for logger
"rosout"*, it's likely either the initialization hasn't finished, or
you forgot to call `rospy.init_node`.

Your Node's log file will be in `ROS_ROOT/log` or `/.ros/log`,
unless you override it with the `ROS_LOG_DIR` environment variable.

If you wish to see `logdebug` messages on `/rosout`, you can pass in
the `log_level` parameter to `init_node()`, e.g.:



```
rospy.init_node('my_node', log_level=rospy.DEBUG)
```



Each `rospy.log\*()` method can take in a string `msg`. If `msg`
is a format string, you can pass in the arguments for the string
separately, e.g. 

```
rospy.logerr("%s returned the invalid value %s", other_name, other_value)
```



### Example

Here's a quick example with a talker Node (a runnable entire code
example is available [here](http://pastebin.com/fSnWxcXN)):



```python
    topic = 'chatter'
    pub = rospy.Publisher(topic, String)
    rospy.init_node('talker', anonymous=True)
    rospy.loginfo("I will publish to the topic %s", topic)
    while not rospy.is_shutdown():
        str = "hello world %s"%rospy.get_time()
        rospy.loginfo(str)
        pub.publish(str)
        rospy.sleep(0.1)
```



On Line 4 and 8 you can see the calls to `rospy.loginfo()`. These also
print to screen as the loginfo also writes to stdout, so you should use
it as a drop-in replacement for `print`.

One of the quick ways to see the Messages on `/rosout` is to use
[rostopic](https://index.ros.org/p/rostopic) echo:


```
$ rostopic echo rosout
---
header: 
  seq: 1
  stamp: 1247874193220264911
  frame_id: 0
level: 2
name: /talker-13716-1247874192981
msg: hello world 1247874193.14
file: 
function: 
line: 0
topics: ['/time', '/chatter', '/rosout']
```



A better way to see these Messages is to use
[rqt_console](https://index.ros.org/p/rqt_console)
([rxconsole](rxconsole) before [ROS Groovy](groovy)), which lets filter
and sort the messages appropriately.

Next tutorial:
[Makefile](#writing-a-ros-python-makefile).

## Writing a ROS Python Makefile

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [ROS tutorials](ROS/Tutorials).
- **Description:** I know what you're saying: "Python\...
  *Makefile*?" Believe it or not, you do need `Makefile` (and
  [CMakeLists](CMakeLists)), even if you just hack Python all day.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Setting Up Your PYTHONPATH](#setting-up-your-pythonpath)

This tutorial repeats information from earlier tutorials with a focus on
the Makefiles. You can skip this tutorial unless you just need
information about the makefile and CMakelists.txt.

### Intro

These build files (`CMakeLists.txt`, `Makefile`) are fairly simple,
but they provide important functionality such as:

- autogenerating message and service code
- running tests

The test functionality is especially important as we have the ability to
run tests on your package *plus* every package that depends on it
(`rospack pkg test`), which is very important for finding regressions
prior to checkin.



```
{{#!wiki buildsystem rosbuild

<<TableOfContents(4)>>

These build files are not difficult to write. In fact, we have an automated tool that will create a all the necessary build files for you:

{{{
$ roscreate-pkg my_pkg rospy
```



This will create `my_pkg` and add in a dependency on
[rospy](https://index.ros.org/p/rospy) so that you can use in it your
code.

If you want to write the necessary build files by hand, here's what you
need:

### Makefile

Your `Makefile` only needs to be one line:

`mypackage/Makefile` 

```
include $(shell rospack find mk)/cmake.mk
```



This loads up our cmake definitions, which ensure our builds are
cross-platform.

### CMakeLists.txt

You also need to provide the [CMakeLists](CMakeLists.txt) file, which is
also fairly simple. Here is an example for a [Package](Packages) that
has [Messages](Messages), [Services](Services), and tests:

`mypackage/CMakeLists.txt` 

```
cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)
rosbuild_init()
rosbuild_genmsg()
rosbuild_gensrv()
rosbuild_add_rostest(test/talker-listener-test.launch)
```



Feel free to omit the
`rosbuild_genmsg/rosbuild_gensrv/rosbuild_add_rostest` lines as
appropriate.

}}}}}



```
{{#!wiki buildsystem catkin

<<TableOfContents(4)>>

With catkin, you only need a CMakefile, which will generate a Makefile in your buildfolder.

Your package.xml should contain the lines:
{{{
  <buildtool_depend>catkin</buildtool_depend>
```



You can create a new package in your catkin workspace like this:


```
$ cd ~/catkin_ws/src
$ catkin_create_pkg my_pkg message_generation rospy
```



This will create `my_pkg` and add in a dependency on
[rospy](https://index.ros.org/p/rospy) so that you can use in it your
code. We use `message_generation` here for the second part of the
tutorial, you only need this if your catkin packages defines new ROS
messages or services.

Your CMakeLists.txt should at least contain the lines:


```
cmake_minimum_required(VERSION 2.8.3)
project(my_pkg)

find_package(catkin REQUIRED COMPONENTS message_generation rospy ...)
catkin_package()
```



#### Messages and Services

To add Messages or Services, you need a few additions to your
package.xml and CMakeLists.txt.

Your package.xml should contain the lines: 

```
<build_depend>message_generation</build_depend>
```

 This
line will have no effect when message_generation exists outside your
workspace, since message_generation is already installed. But for people
using your package in the same workspace as message_generation will
benefit from this line.

You should add the following runtime dependency:


```
<run_depend>message_runtime</run_depend>
```



Your CMakelists.txt should contain: 

```
cmake_minimum_required(VERSION 2.8.3)
project(my_pkg)

find_package(catkin REQUIRED COMPONENTS message_generation rospy)

add_message_files(
  FILES  # e.g. Floats.msg HeaderString.msg
)
add_service_files(
  DIRECTORY srv 
  FILES AddTwoInts.srv BadTwoInts.srv
)

# add_service_files(
#  FILES  # e.g. Floats.srv HeaderString.srv
#)

generate_messages()

catkin_package(
  CATKIN_DEPENDS message_runtime
)
```



#### Installing scripts and exporting modules

With catkin, ROS packages can have an install target. This makes it much
easier for other package managers to automatically create installable
packages than apt-get, e.g. also for MacOS, Arch, BSD, Windows, etc.

However the responsibility is with the developer to describe what needs
to be installed, since it is generally bad if every file in your source
tree is installed on other people's computers. So for python projects
what we want to install are scripts, python modules for others to use as
libraries (Other resources are currently not supported for declaration
in `setup.py`, use `CMakeLists.txt` instead).

For the sake of this tutorial, create an example python package in the
source folder: 

```
$ cd ~/catkin_ws/src/my_pkg    # new catkin package, in the workspace
$ mkdir bin
$ mkdir src
$ mkdir src/tutorial_package
$ touch src/tutorial_package/__init__.py
```

 This defines a python package
called `tutorial_package`. Usually, you should call the package the
same as your catkin package (`my_pkg` in this case) to avoid
confusion, but here we name them differently so that you see what goes
where.

We also add a simple module and script to our project. **Within
my_pkg**, create file `src/tutorial_package/hello.py`


```
def say(name):
    print('Hello ' + name)
```



And also create file `bin/hello`: 

```python
#! /usr/bin/env python

import tutorial_package.hello


if __name__ == '__main__':
    tutorial_package.hello.say('my friend!')
```



Make the file executable: 

```
$ chmod u+x bin/hello
```



if we try to run the executable just like that, we get an import error:


```
$ bin/hello 
Traceback (most recent call last):
  File "bin/hello", line 3, in <module>
    import tutorial_package.hello
ImportError: No module named tutorial_package.hello
```



One way to quickly fix this would be to change your `PYTHONPATH`, but
that would only work for you. In order to make this work generally, you
need to define an installation procedure that moves the files into the
`PYTHONPATH`.

For python packages and scripts, catkin provides a cmake macro that gets
this information from a file called `setup.py`.

So create a file called `setup.py` with these contents in the root of
the `my_pkg` project: 

```python


from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['tutorial_package'],
    package_dir={'': 'src'},
)

setup(**setup_args)
```

 Remember this: The
setup.py is for catkin to use, and not for users to invoke. catkin will
make sure setup.py installs files to the right location. If you invoke
setup.py manually, you may break your ROS installation.

The first line shows we will be using distutils (setuptools is not
recommended since it generates files into your src folder).

Then we use a function `generate_distutils_setup` to read out values
from the package.xml, and also perform some convenience transformations,
such as nicely listing all maintainers and authors in the package.xml.

So all we additionally have to provide is the information that is not in
the package.xml, the name of the scripts you want to have installed, the
name of the python packages, where to find those packages, and python
package dependencies (Those can have different names than what we use in
the package.xml, so we need a separate list).

In order for our setup.py to be used by catkin, we also need to
uncomment this line in the CMakeLists.txt: 

```
catkin_python_setup()
```



Finally, for our script to be installed to the right location, if users
install your package, this line is required in CMakeLists.txt:


```
catkin_install_python(PROGRAMS bin/hello
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
```



Now we can build our package: 

```
$ cd ~/catkin_ws
$ catkin_make
```



To setup the environment to include the new devel space:


```
$ . devel/setup.bash
```



Now your scripts and modules are available via rosrun, and will also be
available If other people install your package.



```
$ rosrun my_pkg hello 
Hello my friend!
```



}}}}}

Also refer to
[ROS/Tutorials/CreatingMsgAndSrv](ROS/Tutorials/CreatingMsgAndSrv) for
making `message` and `service`.

Next tutorial:
[Setting Up Your PYTHONPATH](#setting-up-your-pythonpath).

## Setting Up Your PYTHONPATH

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [ROS tutorials](ROS/Tutorials).
- **Description:** What to do to find other python modules
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Using numpy with rospy](#using-numpy-with-rospy)

Commonly in python, when you use another python module, you use:



```
import foo
```

 in your python code and it is up to the user of
your code to make sure module "foo" is in his PYTHONPATH. In ROS, it
is important that people can install multiple ROS libraries side-by-side
on the same computer. That means there may be two different modules
"foo", and the right one needs to be in the PYTHONPATH.



```
{#!wiki buildsystem rosbuild

The module "roslib" allows this situation, it will search for a ROS package in your current ROS_PACKAGE_PATH, and make sure that the python modules can be imported.

You have already written a [[Manifest|manifest.xml]] file that declares your dependencies, so ROS will use this same manifest file to help you set your PYTHONPATH (we try to use the DRY -- Don't Repeat Yourself -- principle as much as possible).


This is all you need to do:

 1. Make sure that your dependencies are properly listed in your [[Manifest]]
 2. Add the following line to the top of your Python code: {{{
import roslib; roslib.load_manifest('your_package_name')
import foo
```

 So if you declared the package of module foo in
your manifest.xml, the line `import foo` will work after the
roslib.load_manifest call.

NOTE: This line doesn't need to go at the top of every Python file;
they just need to go at the top of any file that is a '__main__'
entry point.

[roslib](https://index.ros.org/p/roslib) will load up your manifest file
and set `sys.path` to point to the appropriate directory in every
package you depend on. These two lines work because
[roslib](https://index.ros.org/p/roslib) is required to be on the
PYTHONPATH of every ROS user.

### Example

For this example we create a new package and try to reuse the message
Num that we defined in our `beginner_tutorials` package:

For rosbuild we create a new package in our sandbox:


```
$ roscd
$ cd sandbox
$ roscreate-pkg listener_extend rospy beginner_tutorials
```



This should already put the dependency to beginner_tutorials in our
manifest.xml file: 

```
$ cat listener_extend/manifest.xml
...
  <depend package="rospy"/>
  <depend package="beginner_tutorials"/>
...
```



Next we create a node using the message defined in beginner_tutorials.
Create a diretory nodes first: 

```
$ cd listener_extend
$ mkdir nodes
```



In the nodes directory, create a file listener_extend.py with these
contents: 

```python
#!/usr/bin/env python
import roslib; roslib.load_manifest('listener_extend')
import beginner_tutorials.msg
num = beginner_tutorials.msg.Num()
print(num)
```



Make this file executable and run it: 

```
$ chmod u+x nodes/listener_extend.py
$ nodes/listener_extend.py
num: 0
```

 As you
can see, the Num module of beginner tutorials was successfully found
even though it is not on your PYTHONPATH. }}}} 

```
{#!wiki buildsystem catkin
In ROS versions earlier than ROS Groovy, a library called [[roslib]] achieved this for us.

With catkin, python imports are done without roslib:

{{{
import foo
```



Catkin sets up PYTHONPATH in your catkin workspace and some relay files
so that this works even with two python modules in your src folder. So
if you have two modules in your catkin workspace, where one depends on
the other, you need to configure and build the modules first, and then
you can run them.

### Example

For this example we create a new package and try to reuse the message
Num that we defined in our `beginner_tutorials` package:

For catkin we create a new package in our source folder:


```
$ cd catkin_ws/src
$ catkin_create_pkg listener_extend rospy beginner_tutorials
```



Next we create a node using the message defined in beginner_tutorials.
Create a diretory nodes first: 

```
$ cd listener_extend
$ mkdir nodes
```



In the nodes directory, create a file listener_extend.py with these
contents: 

```python
#!/usr/bin/env python
import beginner_tutorials.msg
num = beginner_tutorials.msg.Num()
print(num)
```

 Note that in comparison to rosbuild,
no roslib call is required.

Make this file executable and run it: 

```
$ chmod u+x nodes/listener_extend.py
$ python nodes/listener_extend.py
num: 0
```

 If this
fails,make sure you have run 

```
$ source ~/catkin_ws/devel/setup.bash
```

 before executing
nodes/listener_extend.py

As you can see, the Num module of beginner_tutorials was successfully.
}}}}

------------------------------------------------------------------------

## Using numpy with rospy

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  rospy tutorials.
- **Description:** This tutorial covers using
  [numpy](http://numpy.scipy.org/) with
  [rospy](https://index.ros.org/p/rospy), the ROS Python client library.
  Numpy is a popular scientific computing package for Python. You will
  often want to consider using Numpy with rospy if you are working with
  sensor data as it has better performance and many libraries for
  manipulating arrays of data.
- **Tutorial Level:** BEGINNER

In this tutorial, we will go over the `rospy.numpy_msg` module. The
`rospy.numpy_msg` module comes with the `numpy_msg()` wrapper, which
allows [Nodes](Nodes) to deserialize [Messages](Messages) directly into
numpy arrays, where appropriate. The `numpy_msg()` wrapper can also be
used to publish Messages that contain numpy array data.

### Step 1: Create a Package

Lets create a package to house the new code that we are developing. It
needs to depend on rospy_tutorials as we will be using one of its
[Message types](msg).



```
{#!wiki buildsystem catkin
{{{
catkin_create_pkg numpy_tutorial rospy rospy_tutorials
```



As we are using numpy, we also need to make sure that our package
declares this, so lets edit the package.xml file to add the following
line: 

```
<build_depend>python-numpy</build_depend>
  <run_depend>python-numpy</run_depend>
```

 }}}} 

```
{#!wiki buildsystem rosbuild
{{{
roscreate-pkg numpy_tutorial rospy rospy_tutorials
```



As we are using numpy, we also need to make sure that our package
declares this, so lets edit the [manifest.xml](Manifest) file to add the
following [rosdep](rosdep) line: 

```
<rosdep name="python-numpy" />
```

 }}}}

### Step 2: Create a Listener

By now, you're probably familiar with creating listener nodes. Lets
start off simple and create a standard listener node that listens to the
`floats` [Topic](Topics) using the `rospy_tutorials/Floats`
[Message type](msg).

Just for reference, here is the `rospy_tutorials/Floats` definition:



```
$ rosmsg show rospy_tutorials/Floats
float32[] data
```

 Now, lets start with this standard listener.
Paste the text below into a file called `numpy_listener.py`.



```python
#!/usr/bin/env python
PKG = 'numpy_tutorial'
import roslib; roslib.load_manifest(PKG)

import rospy
from rospy_tutorials.msg import Floats

def callback(data):
    print rospy.get_name(), "I heard %s"%str(data.data)

def listener():
    rospy.init_node('listener')
    rospy.Subscriber("floats", Floats, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
```

 Don't forget:



```
chmod +x numpy_listener.py
```

 Lets make sure that this listener is working
before we continue to the next step. We're going to run a
[roscore](roscore), your Node, and a
[rostopic](https://index.ros.org/p/rostopic) `pub` to provide it with
data. You'll need several windows:

Window 1:



```
roscore
```

 Window 2:



```
rosrun numpy_tutorial numpy_listener.py
```

 Window 3:



```
rostopic pub -r 1 floats rospy_tutorials/Floats "[1.1, 2.2, 3.3, 4.4, 5.5]"
```

 You should see:



```
$ rosrun numpy_tutorial numpy_listener.py
/listener-977-1248226102144 I heard (1.1000000238418579, 2.2000000476837158, 3.2999999523162842, 4.4000000953674316, 5.5)
/listener-977-1248226102144 I heard (1.1000000238418579, 2.2000000476837158, 3.2999999523162842, 4.4000000953674316, 5.5)
... and so on
```

 You can go ahead and stop the `rosrun
numpy_tutorial numpy_listener.py`.

### Step 3: Numpy-ize the Listener

In order to numpy-ize our listener, we only need to add two lines, one
to import `numpy_msg`, and the other to use it:



```
from rospy.numpy_msg import numpy_msg
...
    rospy.Subscriber("floats", numpy_msg(Floats), callback)
```

 Here are these two lines in context:



```python
#!/usr/bin/env python
PKG = 'numpy_tutorial'
import roslib; roslib.load_manifest(PKG)

import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg

def callback(data):
    print rospy.get_name(), "I heard %s"%str(data.data)

def listener():
    rospy.init_node('listener')
    rospy.Subscriber("floats", numpy_msg(Floats), callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
```

 Now lets make sure that these are working.
Just as before, lets startup a roscore, your listener, and a `rostopic
pub`.

Window 1:



```
roscore
```

 Window 2:



```
rosrun numpy_tutorial numpy_listener.py
```

 Window 3:



```
rostopic pub -r 1 floats rospy_tutorials/Floats "[1.1, 2.2, 3.3, 4.4, 5.5]"
```

 This time the output is slightly different,
which shows that you are now receiving numpy arrays:



```
$ rosrun rospy_tutorials listener_numpy.py
/listener-1243-1248226610835 I heard [ 1.10000002  2.20000005  3.29999995  4.4000001   5.5       ]
/listener-1243-1248226610835 I heard [ 1.10000002  2.20000005  3.29999995  4.4000001   5.5       ]
... and so on
```



### Step 4: Numpy-ize a Talker

Now that you know how to numpy-ize a listener, lets numpy-ize a standard
talker node. This is very similar to what we did above, though you'll
have to be much more careful: *all of your array data must be
initialized as numpy arrays*. You are responsible for this, *even for
fields that you wish to be initialized with default values*. You must
also be careful that you specify the correct numpy data type when
creating these arrays as rospy will not be able to catch this mistake.

With those warnings out of the way, let's look at a numpy-ized talker.
Create a new file, `numpy_talker.py`, with the following:



```python
#!/usr/bin/env python
PKG = 'numpy_tutorial'
import roslib; roslib.load_manifest(PKG)

import rospy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats

import numpy
def talker():
    pub = rospy.Publisher('floats', numpy_msg(Floats),queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        a = numpy.array([1.0, 2.1, 3.2, 4.3, 5.4, 6.5], dtype=numpy.float32)
        pub.publish(a)
        r.sleep()

if __name__ == '__main__':
    talker()
```

 Don't forget:



```
chmod +x numpy_talker.py
```

 Just like the listener example, there is a
`from rospy.numpy_msg import numpy_msg` to get the `numpy_msg()`
wrapper. You can also see that this is used when creating the
`Publisher` instance:



```
pub = rospy.Publisher('floats', numpy_msg(Floats))
```

 The new step we see with the talker example is
actually creating our own numpy array. This is where we have to be
careful. As was mentioned before, every numerical array in the Message
must be initialized with a numpy array of the correct data type.
Choosing the correct data type is fairly easy as numpy data types map
directly onto ROS data types. In this example we create a simple array
of `numpy.float32`:



```
a = numpy.array([1.0, 2.1, 3.2, 4.3, 5.4, 6.5], dtype=numpy.float32)
```

 Now that we have a talker node, we don't need
`rostopic pub`. This time we can run roscore, the listener Node, and
the talker Node:

Window 1:



```
roscore
```

 Window 2:



```
rosrun numpy_tutorial numpy_listener.py
```

 Window 3:



```
rosrun numpy_tutorial numpy_talker.py
```

 This time you'll see



```
$ rosrun rospy_tutorials listener_numpy.py
/listener-1423-1248226794834 I heard [ 1.          2.0999999   3.20000005  4.30000019  5.4000001   6.5       ]
/listener-1423-1248226794834 I heard [ 1.          2.0999999   3.20000005  4.30000019  5.4000001   6.5       ]
... and so on
```

 That's it! That's all you need to know to
use numpy with rospy.

\-\-\-\--

## Publishing messages in rospy

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [writing a simple publisher and subscriber](#writing-a-simple-publisher-and-subscriber).
- **Description:**
  [Writing a simple publisher and subscriber](#writing-a-simple-publisher-and-subscriber)
  already introduced you to the basics of creating
  [rospy](https://index.ros.org/p/rospy) [Nodes](Nodes) that publish and
  receive messages on ROS [Topics](Topics). As you get more experienced
  with ROS and rospy, you may wish to learn some advanced syntax for
  publishing that will save you some typing \-- as well as make your
  code more robust to future changes.
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:** Publishing and Subscribing to Images
  [WritingImagePublisherSubscriber](#python-compressedimage-subscriber-publisher)

First, lets look at the publish call:



```python
pub.publish(String(str))
```



[rospy](https://index.ros.org/p/rospy) already knows that you're trying
to publish `std_msgs.msg.String` objects, so you can shorten this to:



```python
pub.publish(str)
```



[rospy](https://index.ros.org/p/rospy) will automatically create the
`std_msgs.msg.String` instance for you.

If the message takes in multiple arguments, you must specify them in the
order that they are declared in the `.msg` file. For example,
[std_msgs/ColorRGBA](http://ros.org/doc/api/std_msgs/html/msg/ColorRGBA.html):



```
$ rosmsg show std_msgs/ColorRGBA
float32 r
float32 g
float32 b
float32 a
```



would be initialized with r, g, b, and a as the arguments, e.g.:



```python
pub.publish(0.1, 0.2, 0.3, 0.4)
```



Now, this is very handy, but it's also brittle. If you want to add a
new field to the `ColorRGBA` type, you will have to go through all the
Python code that uses it (`rosmsg users std_msgs/ColorRGBA`) and add
the new field to your arguments. This can be a pain, especially if the
field is optional.

Luckily, there's a more robust way of specifying the fields that also
lets you omit any fields that you wish to assign default values. You
simply use Python keyword arguments to specify the fields you wish to
assign. The rest are assigned default values (zero for numerical values,
empty lists for arrays, empty string for strings):



```python
pub.publish(a=1.0)
```



This will publish a `ColorRGBA` message with a=1.0 and the rest of the
fields (r, g, b) assigned to zero. Working example:

talker_color.py 

```python
#!/usr/bin/env python
import roslib; roslib.load_manifest('beginner_tutorials')
import rospy
from std_msgs.msg import ColorRGBA
def talker():
    #pub = rospy.Publisher('chatter', String)
    pub = rospy.Publisher('chatter_color', ColorRGBA)
    rospy.init_node('talker_color')
    while not rospy.is_shutdown():
        pub.publish(a=1.0)
        rospy.sleep(1.0)
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
```



listener_color.py 

```python
#!/usr/bin/env python
import roslib; roslib.load_manifest('beginner_tutorials')
import rospy
from std_msgs.msg import ColorRGBA
def callback(data):
    rospy.loginfo(rospy.get_name()+ "I heard r=%s g=%s b=%s a=%s", data.r, data.g, data.b, data.a)

def listener():
    rospy.init_node('listener_color', anonymous=True)
    rospy.Subscriber("chatter_color", ColorRGBA, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
```



------------------------------------------------------------------------

## Python CompressedImage Subscriber Publisher

- **Description:** This example subscribes to a ros topic containing
  sensor_msgs::CompressedImage. It converts the CompressedImage into a
  numpy.ndarray, then detects and marks features in that image. It
  finally displays and publishes the new image - again as
  CompressedImage topic.
- **Keywords:** CompressedImage, OpenCV, Publisher, Subscriber
- **Tutorial Level:** INTERMEDIATE

#### Python Code



```python
#!/usr/bin/env python
"""OpenCV feature detectors with ros CompressedImage Topics in python.

This example subscribes to a ros topic containing sensor_msgs 
CompressedImage. It converts the CompressedImage into a numpy.ndarray, 
then detects and marks features in that image. It finally displays 
and publishes the new image - again as CompressedImage topic.
"""
__author__ =  'Simon Haller <simon.haller at uibk.ac.at>'
__version__=  '0.1'
__license__ = 'BSD'
# Python libs
import sys, time

# numpy and scipy
import numpy as np
from scipy.ndimage import filters

# OpenCV
import cv2

# Ros libraries
import roslib
import rospy

# Ros Messages
from sensor_msgs.msg import CompressedImage
# We do not use cv_bridge it does not support CompressedImage in python
# from cv_bridge import CvBridge, CvBridgeError

VERBOSE=False

class image_feature:

    def __init__(self):
        '''Initialize ros publisher, ros subscriber'''
        # topic where we publish
        self.image_pub = rospy.Publisher("/output/image_raw/compressed",
            CompressedImage)
        # self.bridge = CvBridge()

        # subscribed Topic
        self.subscriber = rospy.Subscriber("/camera/image/compressed",
            CompressedImage, self.callback,  queue_size = 1)
        if VERBOSE :
            print "subscribed to /camera/image/compressed"


    def callback(self, ros_data):
        '''Callback function of subscribed topic. 
        Here images get converted and features detected'''
        if VERBOSE :
            print 'received image of type: "%s"' % ros_data.format

        np_arr = np.fromstring(ros_data.data, np.uint8)
        image_np = cv2.imdecode(np_arr, cv2.CV_LOAD_IMAGE_COLOR)
        #image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR) # OpenCV >= 3.0:
        
        # "","Grid","Pyramid" + 
        # "FAST","GFTT","HARRIS","MSER","ORB","SIFT","STAR","SURF"
        method = "GridFAST"
        feat_det = cv2.FeatureDetector_create(method)
        time1 = time.time()

        # convert np image to grayscale
        featPoints = feat_det.detect(
            cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY))
        time2 = time.time()
        if VERBOSE :
            print '%s detector found: %s points in: %s sec.'%(method,
                len(featPoints),time2-time1)

        for featpoint in featPoints:
            x,y = featpoint.pt
            cv2.circle(image_np,(int(x),int(y)), 3, (0,0,255), -1)
        
        cv2.imshow('cv_img', image_np)
        cv2.waitKey(2)

        msg = CompressedImage()
        msg.header.stamp = rospy.Time.now()
        msg.format = "jpeg"
        msg.data = np.array(cv2.imencode('.jpg', image_np)[1]).tostring()
        # Publish new image
        self.image_pub.publish(msg)
        
        #self.subscriber.unregister()

def main(args):
    '''Initializes and cleanup ros node'''
    ic = image_feature()
    rospy.init_node('image_feature', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS Image feature detector module"
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
```



### The Code Explained

Now, let's break down the code\...

#### Shebang



```python
#!/usr/bin/env python
```

 The shebang (#!) should be used in every script
(on Unix like machines). Use the full environment to look for the python
interpreter.

#### Include Lines



```python
# Python libs
import sys, time
# numpy and scipy
import numpy as np
from scipy.ndimage import filters

# OpenCV
import cv2

# Ros libraries
import roslib
import rospy

# Ros Messages
from sensor_msgs.msg import CompressedImage
```



Time is included to measure the time for feature detection. Numpy, scipy
and cv2 are included to handle the conversions, the display and feature
detection.

The ros libraries are standard for ros integration - additionally we
need the CompressedImage from sensor_msgs.



```python
VERBOSE = False
```

 If you set this to **True** you will get some
additional information printed to the commandline (feature detection
method, number of points, time for detection)

#### Class definition



```python
class image_feature:

    def __init__(self):
    ...
    
    def callback(self, ros_data):
```



Defines a class with two methods: The **_init_** method defines the
instantiation operation. It uses the "self" variable, which represents
the instance of the object itself.

The callback method uses again "self" and a (compressed) image from
the subscribed topic.

#### The __init__ method



```python
def __init__(self):
    '''Initialize ros publisher, ros subscriber'''
    # topic where we publish
    self.image_pub = rospy.Publisher("/output/image_raw/compressed",
        CompressedImage)
    # self.bridge = CvBridge()

    # subscribed Topic
    self.subscriber = rospy.Subscriber("/camera/image/compressed",
        CompressedImage, self.callback,  queue_size = 1)
    if VERBOSE :
        print "subscribed to /camera/image/compressed"
```



First the publisher gets created. The publishers topic should be of the
form: image_raw/compressed - see
<http://wiki.ros.org/compressed_image_transport> Section 4.

Further during initialisation the topic "/camera/image/compressed"
gets subscribed (using the callback method of the newly created object).

#### The callback method

The first important lines in the callback method are:

##### Converting the compressed image to cv2



```python
np_arr = np.fromstring(ros_data.data, np.uint8)
image_np = cv2.imdecode(np_arr, cv2.CV_LOAD_IMAGE_COLOR)
# image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR) # OpenCV >= 3.0:
```

 Here the compressedImage first gets converted
into a numpy array. The second line decodes the image into a raw cv2
image (numpy.ndarray).

##### Select and create a feature detector



```python
# "","Grid","Pyramid" + 
# "FAST","GFTT","HARRIS","MSER","ORB","SIFT","STAR","SURF"
method = "GridFAST"
feat_det = cv2.FeatureDetector_create(method)
time1 = time.time()
```



In the first line a feature detector is selected. The second line
creates the detector with the selected method. Before the feature
detection gets started remember the time.



```python
# convert np image to grayscale
featPoints = feat_det.detect(cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY))
time2 = time.time()
if VERBOSE :
    print '%s detector found: %s featpoints in: %s sec.' %(method, 
        len(featPoints),time2-time1)
```

 The first line has two parts:
cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY) - converts the image into a
grayscale image - the feature detection algorithms do not take color
images. The second part starts the detection with the fresh converted
grayscale image.

In VERBOSE mode the time for detection and the amount of feat points get
printed to the commandline.



```python
for featpoint in featPoints:
    x,y = featpoint.pt
    cv2.circle(image_np,(int(x),int(y)), 3, (0,0,255), -1)
        
cv2.imshow('cv_img', image_np)
cv2.waitKey(2)
```

 Lets draw a circle around every detected point
on the color image and show the image.

##### Create a compressed image to publish



```python
msg = CompressedImage()
msg.header.stamp = rospy.Time.now()
msg.format = "jpeg"
msg.data = np.array(cv2.imencode('.jpg', image_np)[1]).tostring()
```

 First create a new compressedImage and set the
three fields 'header', 'format' and 'data'. For data field encode
the cv2 image to a jpg, generate an numpy array and convert it to a
string.



```python
# Publish new image
self.image_pub.publish(msg)
```

 To publish use the method publish from the
rospy.Publisher.
