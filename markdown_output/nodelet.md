## High Level

Nodelets are designed to provide a way to run multiple algorithms on a
single machine, in a single process, without incurring copy costs when
passing messages intraprocess. roscpp has optimizations to do zero copy
pointer passing between publish and subscribe calls within the same
node. To do this nodelets allow dynamic loading of classes into the same
node, however they provide simple separate namespaces such that the
nodelet acts like a seperate node, despite being in the same process.
This has been extended further in that it is dynamically loadable at
runtime using [pluginlib](pluginlib).

### Applications

-   high throughput data flows can be composed of many nodelets and then
    loaded into the same process to avoid copying and network traffic.

### Design Goals

-   use the existing C++ ROS interfaces.
-   allow zero copy passing of data between nodelets
-   dynamically load as plugins to break build time dependencies
-   location transparent except for performance improvements
-   writing code in a node or a nodelet will be minimally different.

### Technique

-   Define a base class nodelet::Nodelet which will be used for dynamic
    loading. All nodelets will inherit from this base class, and be
    dynamically loadable using pluginlib.
-   It will provide the namespace, remapping arguments and parameters
    automatically, like they were a first class node.
-   There will be a nodelet_manager process into which one or more
    nodelets can be loaded. Any communications between them can use the
    zero copy roscpp publish call with a boost shared pointer.

### Basic Usage

```
nodelet usage:
nodelet load pkg/Type manager - Launch a nodelet of type pkg/Type on manager manager
nodelet standalone pkg/Type   - Launch a nodelet of type pkg/Type in a standalone node
nodelet unload name manager   - Unload a nodelet a nodelet by name from manager
nodelet manager               - Launch a nodelet manager node
```

For command line and launch file examples see this tutorial
[Running a nodelet](nodelet/Tutorials/Running a nodelet)

### API

#### Nodelet Base Class:

[nodelet::Nodelet](http://www.ros.org/doc/api/nodelet/html/classnodelet_1_1Nodelet.html)

Public methods:

```cplusplus
Nodelet() //Default constructor used when dynamically loaded
void init (const std::string& name, const ros::M_string& remapping_args, const std::vector<std::string>& my_argv); // This method is how a nodelet should be started.  The arguments are what is required from the manager to start the nodelet.  This will initialize the nodelet base class and then call the subclass's onInit() method.
``` Protected members and methods for use in
subclass:

```cplusplus
std::string             getName() //Get the name of the nodelet
ros::NodeHandle&        getNodeHandle () // Get the node handle (provides this nodelets custom remappings and name)
ros::NodeHandle&        getPrivateNodeHandle () // Get the private node handle (provides this nodelets custom remappings in its private namespace)
ros::NodeHandle&        getMTNodeHandle () // Get the node handle with the Multi Threaded callback queue. (provides this nodelets custom remappings and name)
ros::NodeHandle&        getMTPrivateNodeHandle () // Get the private node handle with the Multi Threaded callback queue. (provides this nodelets custom remappings in its private namespace)
ros::CallbackQueue&     getMTCallbackQueue () // Get the callback queue (threadpool available from the manager)
std::vector<std::string> getMyArgv() // Get command line arguments to the nodelet stripped of ROS and nodelet specific args.
```

Initialization method used to start ROS API in subclass:
```cplusplus
virtual void onInit () = 0 //Virtual and must be overridden by subclass. All initialization of the ROS infrastructure must be put into this function.
```

#### NODELET ROSCONSOLE MACROS

These are nodelet aware wrappers around [rosconsole](rosconsole) macros.
They include verbosity levels DEBUG, INFO, WARN, ERROR, and FATAL. These
macros will only compile inside nodelet methods.

They operate by setting up a named logger in the name of the nodelet
running so that you can differentiate between the output of two of the
same type nodelets running on the same manager. They also have the
advantage that you can turn one specific nodelet into debug, instead of
all nodelets of a specific type.

```cplusplus
#include "nodelet/nodelet.h"

//... inside a nodelet method
NODELET_DEBUG("My debug statement")
NODELET_DEBUG_STREAM("my debug statement " << (double) 1.0)
NODELET_DEBUG_COND( 1 == 1, "my debug_statement")
NODELET_DEBUG_STREAM_COND( 1 == 1, "my debug statement " << (double) 1.0)
```

#### Publishing from a Nodelet

If you want the no-copy pub/sub to work you must publish your messages
as `shared_ptr`s. See
[roscpp/Overview/Publishers and Subscribers#Intraprocess_Publishing](roscpp/Overview/Publishers and Subscribers#Intraprocess_Publishing)
for more details.

### Threading Model

A nodelet manager has a pool of threads which is shared across all
nodelets run within the manager. This is set by the parameter
"num_worker_threads".

There are two possible threading APIs to use in code running in
nodelets. The default threading model has a single thread for all
callbacks. There is a multithreaded API as well.

#### onInit

This method is called on init and should not block or do significant
work.

#### Single Threaded API

Using the methods getNodeHandle() and getPrivateNodeHandle() will
guarantee that all callbacks arrive serially.

#### Multi Threaded API

Using the methods getMTNodeHandle() and getMTPrivateNodeHandle()
callbacks will be distributed over the thread pool of the manager.

#### Additional Threads

It is valid operation for a nodelet to create its own threads for
operation. These threads should be cleaned up properly in the
destructor.

#### Thread Sharing

All nodelets share the thread pool of the manager. If nodelets are
blocking threads they may prevent other nodelets from getting callbacks.
Make sure the manager is configured with enough threads to prevent
blocking. Note: Even the single threaded Node Handles can consume 1
thread of the pool per nodelet.

## Helper tools

### List all declared nodelets

Following commands are helpful to list all nodelets available on your
system found in `ROS_PACKAGE_PATH`. Note that it's NOT the list of
currently running nodelet nor nodelet managers.

```
rosrun nodelet declared_nodelets
```

Or list the nodelet xml files for [pluginlib](pluginlib) by:

```
rospack plugins --attrib=plugin nodelet
```

## Report a Bug

[File a Ticket](https://github.com/ros/nodelet_core/issues/new)
