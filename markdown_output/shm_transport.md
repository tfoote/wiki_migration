## What does shm_transport do?

ROS 1 use socket as a communication method. If the publisher and
subscriber belong to different processes of a same machine, the socket
will go through loopback with AF_INET family (either UDP or TCP
protocol).

The main purpose of this package is to use shared memory IPC instead of
loopback socket to establish publisher/subscriber communication. And we
employ boost::interprocess::managed_shared_memory to accomplish it.

But shared memory is lack of synchronization method like poll/epoll for
socket. Even inotify does not support generating a notification when the
shared memory region is written or updated. Therefore, we use the
original transport (udp or tcp) to send the handle (essentially, an
offset pointer) from publishers to subscribers.

Experimental results show that the communication latency can be greatly
reduced by using shm_transport, especially for large messages and
multiple subscribers.

## Tutorials

Using shm_transport is much like using the native ROS transport. Here
are some examples.

### Writing the publisher node

```cplusplus
#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include "shm_transport/shm_topic.hpp"

#define MSGLEN (1920 * 1080 * 3)
#define HZ (30)

std::string str(MSGLEN, '-');
char tmp[100];

int main(int argc, char ** argv) {
  ros::init(argc, argv, "shm_talker", ros::init_options::AnonymousName);
  ros::NodeHandle n;
  shm_transport::Topic t(n);
  shm_transport::Publisher p =
      t.advertise<std_msgs::String>("test_topic", HZ, 3 * MSGLEN);

  ros::Rate loop_rate(HZ);
  int count = 0;
  while (ros::ok()) {
    int len = snprintf(tmp, 100, "message # %d ...", count);
    memcpy(&str[0], tmp, len);

    std_msgs::String msg;
    msg.data = str;

    ROS_INFO("info: [%s]", tmp);
    p.publish(msg);

    ros::spinOnce();
    loop_rate.sleep();
    count++;
  }
  return 0;
}
```

The main difference between using shm_transport and native ROS transport
is at line 15 to 17.

\<\<CodeRef(publisher,15,17)\>\>

A shm_transport::Topic object is an encapsulation of ros::NodeHandle.

By calling shm_transport::Topic::advertise(), we can get a
shm_transport::Publisher object, which acts the same with
ros::Publisher.

Note that shm_transport::Topic::advertise() has one more parameter
comparing to ros::NodeHandle::advertise(). This parameter (3 \* MSGLEN
in the example) indicates the total size of shared memory segment. The
total size of shared memory segment should be larger than two messages
plus the space used by memory allocation algorithm.

### Writing the subscriber node

```cplusplus
#include "ros/ros.h"
#include "std_msgs/String.h"
#include "shm_transport/shm_topic.hpp"

void chatterCallback(const std_msgs::String::ConstPtr & msg) {
  char str[21] = {'\0'};
  strncpy(str, msg->data.c_str(), 20);
  ROS_INFO("I heard: [%s]", str);
}

int main(int argc, char ** argv) {
  ros::init(argc, argv, "shm_listener", ros::init_options::AnonymousName);
  ros::NodeHandle n;
  shm_transport::Topic t(n);
  shm_transport::Subscriber<std_msgs::String> s =
      t.subscribe("test_topic", 60, chatterCallback);
  ros::spin();
  return 0;
}
```

Similar with the publisher node, the main difference between using
shm_transport and native ROS transport is at line 14 to 16.

\<\<CodeRef(subscriber,14,16)\>\>

By calling shm_transport::Topic::subscribe(), we can get a
shm_transport::Subscriber object, which acts the same with
ros::Subscriber, and the registered callback function (chatterCallback
in the example) will be called whenever a message arrives.

## Performance

[Latency vs Message Size](https://github.com/Jrdevil-Wang/shm_transport/blob/master/Latency%20vs%20Message%20Size.pdf)

[Latency vs Number of Listeners](https://github.com/Jrdevil-Wang/shm_transport/blob/master/Latency%20vs%20Number%20of%20Listeners.pdf)
