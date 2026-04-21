[Included page Menus/ROSClients not found](Included page Menus/ROSClients not found)

```wiki
'''WARNING:''' This documentation refers to an outdated version of rosjava and is probably incorrect. Use at your own risk.
```

## Package Details

As mentioned above, rosclj is just a lightweight set of macros and
functions to simplify the use of [rosjava](rosjava) from Clojure. Users
of rosclj should read the [rosjava](rosjava) documentation as well.

rosclj is currently in an early stage of development, and has primarily
been used to write interactive high-level nodes and teleop the PR2. It
is likely missing useful functionality for other use cases;
contributions and patches are welcome.

### Creating, building, and running rosclj packages

In addition to the setup instructions given for [rosjava](rosjava), to
develop or run rosclj nodes you first need to download and build
[Clojure](http://clojure.org). Then, you must create a new directly
somewhere, symlink clojure.jar and other additional jars you want on
your classpath (e.g., clojure-contrib.jar) into this directory, and set
the environmental variable "CLJ_HOME" to point at this directory.

To create a new package that uses rosclj, your manifest.xml must include
a dependency on rosclj: -```
<depend package="rosclj"/>
```-\~

Then, in CMakeLists.txt, you first add your Clojure source directories:
-```
add_clj_source_dir(${PROJECT_SOURCE_DIR}/src)
```-\~

Finally, you can generate binary (scripts) that launch a Clojure REPL
with your code in the classpath, or run a particular Clojure file, as
follows: -```
rospack_add_clj_repl(bin/repl)
rospack_add_clj_executable(bin/do_stuff script.clj)
```-\~

### Initializing ROS and getting a NodeHandle

To create a ROS node, first load rosclj.

```clojure
(use 'ros.ros)
```

Then, call (import-ros) as a shortcut to import all of the
[rosjava](rosjava) classes into the current namespace:

```clojure
(import-ros)
```

Next, get a handle to the global ROS instance and initialize it, by
directly calling the corresponding rosjava methods.

```clojure
(def *ros* (Ros/getInstance))
(.init *ros* "my-node")
```

Finally, once you have initialized ROS, you can get a scoped NodeHandle
by calling with-node-handle:

```clojure
(with-node-handle [nh *ros*] (println (.now nh)))
```

or simply create one by calling rosjava methods directly:

```clojure
(def nh (.createNodeHandle *ros*))
```

### Messages and Services

Like all Java objects, rosjava Message objects can be manipulated
directly from Clojure. Often, however, it is much more convenient to
manipulate Message data represented as Clojure maps. To this end, rosclj
provides functionality to automatically convert between rosjava Message
objects and Clojure maps of a particular form, for when ease of use is
more important than raw speed.

To use this functionality, you must first declare the top-level Messages
and Services you want to use:

```clojure
(defmsgs [std_msgs Float64] [geometry_msgs Twist PoseStamped])
(defsrvs [roscpp GetLoggers SetLoggerLevel] [roscpp_tutorials TwoInts])
```

This will set up Clojure infrastructure for converting between messages
and maps for these types, as well as all submessages/request/response
message classes below them. It will also import all such Message Classes
into the current namespace, so they can be referred to by their
unqualified names (except where this would case a name conflict).

In particular, after declaring a message, you can use *msg->map* to
convert a rosjava Message into a rosclj map, and *map->msg* to go back
in the other direction: ```
<depend package="rosclj"/>
```0 As you can see, the
Clojure representation of a message is a map from keyword-ized field
names to values, plus a *:class* field that maps to the java.lang.Class
object corresponding to the message type.

msg->map simply converts a Message to this form, recursively converting
all submessages into maps. Arrays of submessage types are transformed
into lazy sequences of submessage maps, but primitive arrays are left
intact to allow for efficient manipulation if desired. If the input to
msg->map is already a map, it is returned unchanged.

map->msg goes in the other direction, using message field type
information to do its best to construct a Message out of what you give
it. If you pass a Message, it is returned unchanged. Otherwise, you must
pass a map with the outermost *:class* filled in, or pass the Message
Class directly along with a map of field data (no *:class*es required).
The outermost map will be converted to a Message of the given type, with
numbers being coerced to the proper types, submessages being recursively
converted, and sequences being transformed to arrays. An error will be
produced if any fields are missing. The only exception is the Header
type, for which only the ":frame_id" is required.

A number of other methods for manipulating and introspecting Messages
can also be found in ros.clj. A potentially useful example is
*import-all-msgs-and-srvs*, which imports the Java classes for all
defined Messages and Services into the current namespace, which can be
useful for debugging at the REPL.

### Convenience Functions

rosclj also provides a very minimal suite of convenience functions for
interacting with rosjava callbacks, topics, and services.

*make-subscriber-callback* and *make-service-callback* take a Clojure
function that expects a message, and wrap it into a Subscriber or
ServiceServer callback. More conveniently, *sub-cb* and *srv-cb* define
a *fn*-like syntax for directly declaring subscriber and service
callbacks that take (and return) Clojure maps, which are converted
to/from rosjava Messages of the proper types behind the scenes.

```
<depend package="rosclj"/>
```1

At an even higher level, functions are provided for writing or reading a
single message from a topic, and calling a service. *put-message*
advertises a topic, waits until a given number of subscribers are
achieved, publishes the given message, and then shuts down the
Publisher. *get-message* subscribes to a topic, returns the first
message received, and then shuts down the Subscriber. Finally,
*call-service* creates a ServiceClient, calls the service with the given
request, and then shuts down the service. ```
<depend package="rosclj"/>
```2

These are primarily meant for interactive development at the REPL,
although they may find some use in more mature programs as well. In such
cases, rosclj also provides "-cached" versions of each function (e.g.,
put-message-cached) that keep the Publisher/Subscriber/ServiceClient
around after the first call, for efficiency comparable to manually
managing these rosjava objects. The cached persistent connections will
be kept open until the NodeHandle used to create them is shutdown.

## Known Issues

The build system does not yet expose a way to add additional JARs to the
compilation/execution classpaths, or use multiple Java/Clojure source
trees.

There is also a known issue with Message and Service definitions in
rosclj packages. In particular, packages must be "made" twice for
locally defined Message and Service .class files to be generated.

Patches are welcome.

------------------------------------------------------------------------

[Troubleshooting](rosjava/Troubleshooting)

[Review Process](rosjava/Reviews)
