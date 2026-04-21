## Pure Java implementation

For a pure Java implementation, please see [rosjava_core](rosjava_core).

## Package Details

**Rosjava has been moved to a different repository and got released. Get
the current version with the following command:**

```
git clone https://github.com/gheorghelisca/rosjava_jni.git client_rosjava_jni
```

### Client library API

As much as possible, each method provided by the rosjava client library
simply wraps a call to a method by the same name in the [roscpp](roscpp)
C++ client library.

Thus, the best place to look for detailed documentation on individual
rosjava methods is probably the roscpp documentation. Specifically, you
can find information there about
[initialization and NodeHandle creation](http://www.ros.org/doc/api/roscpp/html/namespaceros.html),
[NodeHandles](http://www.ros.org/doc/api/roscpp/html/classros_1_1NodeHandle.html),
[Publishers](http://www.ros.org/doc/api/roscpp/html/classros_1_1Publisher.html)
and
[Subscribers](http://www.ros.org/doc/api/roscpp/html/classros_1_1Subscriber.html),
and
[ServiceClients](http://www.ros.org/doc/api/roscpp/html/classros_1_1ServiceClient.html)
and
[ServiceServers](http://www.ros.org/doc/api/roscpp/html/classros_1_1ServiceServer.html).

Right now, the rosjava code is broken up into three packages.

-   **ros**, which contains all of the interfaces that should be used by
    clients of the library.
-   **ros.communication**, which has the abstract [Message](Messages)
    and [Services](Services) classes, as well as Time and Duration
    [message field types](msg).
-   **ros.roscpp**, which contains specific implementations of the
    \`ros\` interfaces that call into roscpp via JNI, and should
    eventually be replaced by a pure Java implementation. *Users of the
    client library should never refer to anything in this package; they
    should only use the public API in the \`ros\` and
    \`ros.communication\` packages*.

### Messages and Services

When a package (with a Java target) is compiled, a Java source files for
each [Message](Messages) and [Service](Services) of all dependencies is
automatically generated and placed in the \`msg_gen/java\` and
\`srv_gen\`/java folders respectively. Currently, a package\'s messages
and services live in the ros.pkg.\<package-name\>.msg and
ros.pkg.\<package-name\>.srv Java packages, and extend the
java.communication.Message and java.communication.Service classes.

In addition to the interface defined in the java.communication.Message
and java.communication.Service classes, each message will have one
public member for each data element, with the name defined in the
message declaration, and each Service will have inner class Message
types named \"Request\" and \"Response\".

ROS Message data types are mapped to Java data types as follows:

  -- ----------------------- -- -------------------------------------- --
     **Message type**           **Java type**                          
     string                     java.lang.String                       
     time                       ros.communication.Time                 
     duration                   ros.communication.Duration             
     byte, char, int8           byte                                   
     uint8, int16               short                                  
     uint16, int32              int                                    
     uint32, int64, uint64      long                                   
     float32                    float                                  
     float64                    double                                 
     bool                       boolean                                
     type\[\]                   type\[\] for primitive types           
     type\[\]                   !ArrayList\<type\> for complex types   
     type\[5\]                  type\[5\]                              
  -- ----------------------- -- -------------------------------------- --

In particular, because Java lacks unsigned types, **note that unsigned
message types are currently mapped to Java\'s next bigger signed
types**. Since there is no next bigger type for \`long\`, \`uing64\` and
\`int64\` are both mapped to \`long\`. Fixed size arrays are mapped to
Java arrays. Variable size arrays over primitive types are also mapped
to Java arrays to ensure that processing can be done efficiently. All
other arrays are mapped to \`ArrayList\`s.

Message constants are mapped to final static members of a message class.

Finally, when a new Message subtype instance is created, all the fields
are initialized to legal default values. In particular, primitives will
be 0 (or 0.0), strings will be \"\", times and durations will have 0
secs and nsecs, variable arrays will be created with size 0 and
fixed-length arrays will be created with the given size, and submessages
will be recursively initialized by these same rules.

### Building and running rosjava packages

Because rosjava currently wraps roscpp via JNI, it requires header files
and shared libraries only provided with the Java Development Kit (JDK).
You will need a copy of the JDK (version \>= 5) installed to compile or
run rosjava and any nodes that depend on it.
[client_rosjava](client_rosjava) contains a rosdep.yaml file so that
rosdep should work as expected.

Moreover, in order to build, rosjava needs to know where to find your
JDK installation. Per default, it uses the cmake FindJNI module. If this
causes problems, you can set your JAVA_HOME environmental variable,
e.g.,:

```
export JAVA_HOME=/usr/lib/jvm/java-6-sun/
``` Once you\'ve installed the JDK and maybe set
your JAVA_HOME, you should be ready to build and use existing rosjava
nodes. To test this out, assuming you have already downloaded and build
ROS, you should be able to:

```
roscd test_rosjava
make test
``` and see a bunch of printouts, followed by a
successful test result. If things don\'t build or run properly, you
probably have a bad version of Java installed or haven\'t set your
JAVA_HOME correctly.

When running rosjava nodes, you should always use the provided scripts
(which can be autogenerated, see the next section) rather than directly
launching them via the \"java\" command. This is because two
environmental variables need to be set for rosjava nodes to run
correctly. First, rosjava nodes need to be able to dynamically link to
the rosjava JNI library: LD_LIBRARY_PATH= \<rosjava\>/bin. Second,
roscpp installs signal handlers that can interfere with the Java virtual
machine\'s handlers, causing unexpected and hard-to-diagnose problems.
To avoid this, you need to set LD_PRELOAD=\"path to libjsig.so\", which
is part of the JDK distribution.

### Creating new rosjava packages

To create a new rosjava node, you need to take the following steps:

-   Add a dependency to rosjava in your manifest.xml
-   In CMakeLists.txt, add a line

```
add_java_source_dir(${PROJECT_SOURCE_DIR}/<dir>)
``` . for each Java source directory tree you want
compiled (into the /bin directory of your package). This will also
trigger compilation of all of the message and service classes your
package depends on, the output of which will also be placed in the /bin
directory of the current package.

-   In CMakeLists.txt, for each main class, add a line

```
rospack_add_java_executable(<exec-name> <class-name>)
``` . This will generate a script in
bin/\<exec-name\> that automatically sets the proper environmental
variables, then launches java on your class with the proper classpath.

-   Currently, rosjava provides several additional parameters for
    \`javac\` and the generated wrapper script. These macros are:
-   \`add_classpath(path)\`: Add a classpath to be used by javac (only
    at build time)
-   \`add_runtime_classpath(path)\`: Add a classpath to be used by the
    wrapper script
-   \`add_jar_dir(dir)\`: Add all jar files under a given directory to
    the classpath
-   \`add_jni_path(dir)\`: Add all the .jnilib files under a given
    directory to the classpath
-   \`add_ld_preload(lib)\`: Add a library to LD_PRELOAD in the wrapper
    script
-   You can append additional entries to the compile and runtime
    classpath by setting the environment variable
    \`ROSJAVA_AUX_CLASSPATH\`

Currently, there is no support for more advanced features, such as
setting JVM arguments. Patches are always welcome!

## Examples

-   Importing rosjava

```java
  import ros.*;
  import ros.communication.*;
```

-   Initializing rosjava

```java
  Ros ros = Ros.getInstance();
  ros.init("testNode");
```

-   Logging to rosout

```java
  ros.logDebug("DEBUG");
  ros.logInfo("INFO");
  ros.logWarn("WARN");
  ros.logError("ERROR");
  ros.logFatal("FATAL");
```

-   Creating a NodeHandle

```java
  NodeHandle n = ros.createNodeHandle();
```

-   Setting and getting parameters

```java
  n.setParam("test", 2);
  n.setParam("test2", 2.2);
  n.setParam("test3", "2.5");

  System.out.println(n.getIntParam("test"));
  System.out.println(n.getDoubleParam("test2"));
  System.out.println(n.getStringParam("test3"));
```

-   Publishing on a topic

```
export JAVA_HOME=/usr/lib/jvm/java-6-sun/
```0

-   Subscribing to a topic (with a queueing callback)

```
export JAVA_HOME=/usr/lib/jvm/java-6-sun/
```1 (this could be made less ugly by importing the
String message class, except that in this case it clashes with Java\'s
built-in String type.)

-   Calling a service

```
export JAVA_HOME=/usr/lib/jvm/java-6-sun/
```2

-   Advertising a service, and then spinning

```
export JAVA_HOME=/usr/lib/jvm/java-6-sun/
```3

-   Shutting down a NodeHandle (and all
    Publishers/Subscribers/ServiceClients/ServiceServers created through
    it)

```
export JAVA_HOME=/usr/lib/jvm/java-6-sun/
```4

## Known Issues
