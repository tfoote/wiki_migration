## Description

The rosmultimaster package is designed to allow you to connect to
multiple ros cores from within a single process. This is achieved via
the rosmultimaster.Adaptor class.

## Motivation

ROS does not have a built-in system to allow a single node to connect to
multiple ROS cores. Since entire processes are declared as ros nodes,
there is therefore no way to access multiple ros cores from a single
process.

## API Description

rosmultimaster.Adaptor objects are designed to replicate the rospy API
as closely as possible in order to ensure ease of use for programmers
who are familiar with using rospy to instantiate ROS nodes and use them
to publish, offer services, subscribe, and get service proxies. This is
best illustrated by a simple example:

```python
import rosmultimaster
from std_msgs.msg import String
from std_srvs.srv import Empty, EmptyResponse
import time

ip = '192.168.1.2'
port = 8675

def sub_test_callback(string_request):
  print string_request.data
def handle_srv_test(empty_request):
  print "I received an empty request!"
  return EmptyResponse()

adaptor = rosmultimaster.Adaptor( host = ip, port = port, name = 'arbitrary_name', anonymous = True)
pub = adaptor.Publisher('pub_test', String)
adaptor.Subscriber('sub_test', String, sub_test_callback)
adaptor.Service('srv_test', Empty, handle_srv_test)
adaptor.ServiceProxy('proxy_test', Empty)
adaptor.start()

for x in range(20):
  pub.Publish("Hello %s! I'm talking to you on port %s!" %( ip, repr(port) ) )
  time.sleep(1)
```

As you can see, this works almost exactly the same way as rospy except
for the initialization of the Adaptor and the need for the
adaptor.start() call. For simplicity, this example only illustrates
connecting to a single core with a single adaptor, but hopefully you can
easily see how you could use the same system to connect to as many cores
as you like. Just initialize the Adaptors with the correct hosts and
ports, create the Subscribers, Services, Publishers, and Service proxies
for those adaptors, and then call start() on the adaptors. They operate
completely independently of each other. You can even connect two to the
same core, as long as they have different \"names\" or are anonymous (as
declared in the initialization).

Below is a more detailed breakdown of the differences between rospy and
a rosmultimaster.Adaptor object.

## Differences for rospy API

### Major Differences

There are two major differences between the rospy system and the
rosmultimaster system: 1. In rosmultimaster you must initialize an
Adaptor object with the host and port of the roscore to which you wish
to connect. The \"name\" and \"anonymous\" parameters affect the name of
the rosnode that will appear in the specified roscore. 1. You must call
adaptor.start() before the adaptor will actually be able to publish or
subscribe to topics. All declarations of Publishers, Subscribers, etc.
must occur before adaptor.start() is called.

The issues below are more minor and should not affect most users of the
rosmultimaster system.

### Some missing features

Many of the more obscure features of rospy have not yet been implemented
in rosmultimaster. This includes things that modify the behavior of
publishers, subscribers, etc (e.g. queue_size, callback_args in
rospy.Subscriber() ) and whole features like the ros Parameter Server.
Most of these should be very easy (but somewhat time consuming) to
implement without any major changes to the rosmultimaster backend.

### No control over order of initialization

All of your Subscribers, Publishers, Services, and !ServiceProxies are
initialized \'\'in that order\'\' as soon as you call adaptor.start(),
regardless of the order in which you created them. If this order of
initialization really matters for your application, you can get around
this problem by using several adaptors connected to the same ip and port
and then starting them in the desired order.

### No duplicate topics

You can\'t subscribe to the same topic twice, have two publishers to the
same topic, offer two services with the same names, or get two service
proxies for the same service using the same adaptor. This may be true of
rospy too, but it is definitely true of Adaptor.

### No similar Services

You can\'t offer two services with the same service_class using the same
adaptor. This is because since rospy.Service does not allow you to pass
arguments into the service callback in the same way that
rospy.Subscriber and rospy.Publisher do, which causes problems in the
implementation of rosmultimaster.

### No wait_for_service

\'\'\'Issue:\'\'\'When using !ServiceProxy\'s in rosmultimaster, it is
unnecessary (and currently impossible) to make any kind of
\"wait_for_service\" call. Simply calling
adaptor.!ServiceProxy(\'topic\', !ServiceClass) will automatically cause
a call to rospy.wait_for_service(\'topic\') to be made internally when
adaptor.start() is called. This is not ideal, since the goal of Adaptor
is to mimic the rospy API as much as possible.

\'\'\'Rationale:\'\'\' Why this break with the rospy API is necessary:

-   I assume that rospy.wait_for_service blocks until the service
    becomes available. Since no ROS stuff is initialized until
    adaptor.start() is called, adaptor.wait_for_service will have no way
    of knowing when the service becomes available, so it therefore
    cannot block in the same way as rospy.wait_for_service. The best we
    can do is set a flag that tells adaptor to make the blocking call to
    rospy.wait_for_service in adaptor.start.
-   Finally, I assume that if one attempts to create a
    rospy.!ServiceProxy without first calling rospy.wait_for_service, a
    !ServiceException is raised. Normally this can be handled gracefully
    by wrapping the rospy.!ServiceProxy call in a try/except block.
    However, adaptor.start() actually spawns separate processes, and it
    is in these processes that rospy.!ServiceProxy is actually called.
    Therefore, if a !ServiceException is raised, it will be raised in a
    separate process from the process in which adaptor.start() is called
    and will not be able to be caught by wrapping adaptor.start() in a
    try/except block.

In short, it is not possible to mimic the API for rospy perfectly, and
adding an analogue to wait_for_service may be more confusing than making
the assumption that you will generally want to wait for services to
become available.

## Implementation

In order to connect to a roscore without actually declaring the
\_\_main\_\_ process as a node, Adaptor must start a child process,
which is connected to the \_\_main\_\_ process through pipes. This child
process becomes a ROS node and sets up all of the publishers,
subscribers, services, and service proxies that are declared before
adaptor.start() is called. After this set-up is done, data flows as
follows:

\_\_main\_\_ process \<\--\> pipes \<\--\> child process/ROS node
\<\--\> ros protocols (pub/sub/serv) \<\--\> ROS system

The \_\_main\_\_ process is sometimes called the \"Adaptor\" process and
the child process is sometimes called the \_AdaptorNode process, since
each process hold a reference to an object of that type.

------------------------------------------------------------------------
