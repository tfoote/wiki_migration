  -- ----------------------------------------------------------------- --
     <#FFFF00> **As of ROS 1.1.5, rosrecord has been deprecated.**   
     <#FFFF00> **For C Turtle, see [rosbag](rosbag)**                
  -- ----------------------------------------------------------------- --

## Status

rosrecord was phased out in favor of a more unified interface,
[rosbag](rosbag). rosrecord has been deprecated as of ROS 1.1.5.

All of its functionality is now contained in rosbag. In fact, rosrecord
is now simply a wrapper around the underlying [rosbag](rosbag) API.

## Code API

The rosrecord programmatic API does not yet have a [rosbag](rosbag)
equivalent. It is still the main way to interact with bagfiles
programmatically. However, this API is expected to change somewhat
substantially in the move to rosbag and is slated for eventual
deprecation.

### ros::record::Recorder

The `ros::record::Recorder` allows you to populate a bag file without
going through ros.

The `Recorder` has a fairly simpe interface for pushing messages into
a bag file. `open` is used to open the file. Messages can then be
added with sequential calls to `record`. When the bag file is
complete, close it using `close`.

**Example:** To put your own message into a bag file


```cplusplus
#include "rosrecord/Recorder.h"

//...

int main()
{
    ros::record::Recorder recorder;
    recorder.open("my.bag");

    my_msgs::MyMsg msg;
    msg.foo = 123;
    msg.bar = "abc";

    recorder.record("my_topic", msg, ros::Time::now());

    recorder.close();
}
```

 For more information see the
[C++ Code API](http://www.ros.org/doc/api/rosrecord/html/c++/classros_1_1record_1_1Recorder.html).

### ros::record::Player

The `ros::record::Player` class enables parsing of bag files without
going through ros. This is very useful for converting .bag files to
different formats.

The `Player` has an unfortunately complicated API at the moment. A set
of callbacks can be registered on the Player using the `addHandler`
call. This call takes a topic (which may be specified as "\*"), and is
templated on a particular type. The corresponding callback will be
invoked when a message matching this topic and type is extracted from
the bag through a call to `player.nextMsg()`.

*NOTE:* The Player also has the ability to optionally construct a
shifted and scaled time-line for your messages. This is what the
`start_time` in the open call corresponds to. When the The callback is
invoked it is passed TWO times. The first is a shifted and scaled
representation of time, the second is the original timestamp stored in
the bag. Internally rosplay does a remapping from the first time-stamp
in your bag to whatever time is passed in as `start_time` to the open
call. Additionally, if you have constructed your bag with a time_scale,
the Player will scale the duration beween subsequent messages
appropriately. For example, supposing your bag contains 3 messages with
times: 30, 40, 50. If start_time is specified as 100 and time_scale is
specified as 5, the shifted/scaled times passed into your callback would
be 100, 102, 104.

**Example:** Iterating through a bag file programmatically


```cplusplus
#include "ros/ros.h"
#include <string>
#include "rosrecord/Player.h"
#include "rosrecord/AnyMsg.h"
#include "std_msgs/String.h"

// Generic callback to be invoked for any message
void all_handler(std::string name,         // Topic name
                 ros::Message* m,          // Message pointer
                 ros::Time t,              // Shifted and scaled time
                 ros::Time t_orig,         // Message timestamp
                 void* n)                  // Void pointer     
{
  // Do something that doesn't require understanding the message contents
}

void string_handler(std::string name,      // Topic name       
                    std_msgs::String* str, // Message pointer  
                    ros::Time t,           // Shifted and scaled time     
                    ros::Time t_orig,      // Message timestamp
                    void* n)               // Void pointer     
{
  // Do something with the std_msgs::String
}

int main(int argc, char **argv)
{
  ros::record::Player player;

  if (player.open(std::string("my.bag"), ros::Time()))
  {
    player.addHandler<AnyMsg>(std::string("*"), // Topic name
                              &all_handler,     // Handler
                              NULL,             // void*
                              false);           // Don't deserialize

    // NOTE: serialization is required by the signature of the
    // handler above
    player.addHandler<std_msgs::String>(std::string("chatter"),
                                        &string_handler,
                                        NULL);
  }

  // Spin until we have consumed the bag
  while(player.nextMsg())  {}

  return 0;
}
```



For more information see the
[C++ Code API](http://www.ros.org/doc/api/rosrecord/html/c++/classros_1_1record_1_1Player.html).

### rosrecord.py

The `rosrecord` module provides a simple API for iterating through
messages in a bag file. By default, it will automatically deserialize
each message for you into the appropriate `Message` instance. For
higher performance, it can also operate in 'raw' mode, which returns
the serialized bytes for each message.

Iterating over messages: 

```python
from ros import rosrecord
for topic, msg, t in rosrecord.logplayer('input.bag'):
  print topic, msg, t
```



Rebagging messages: 

```python
from ros import rosrecord
rosrecord.rebag('input.bag', 'modified.bag', lambda topic, msg, t: True)
```



For more information see the
[Python Code API](http://www.ros.org/doc/api/rosrecord/html/python/)

## Bag File Maintenance

The following maintenance approaches should rarely be necessary except
with particularly old bags. Going forward, the [rosbag fix](rosbag#fix)
command should be all that is necessary.

### Updating bag files after a msg change

When messages change md5sums will change. To update bags use the
[rosbag fix](rosbag#fix) tool

### Fixing md5sums after a move or rename

If you have moved or renamed a message but not changed the content, it
is possible to convert old bag files to the new name. To do this you
must generate a file with the old and new names as well as the old and
new md5sums. 

```
old/name OLDMD5 new/name NEWMD5
```



It is up to the user to generate these. I've attached an example file
for our recent changes for ros release 0.4
<attachment:combined_md5s.fixed>

To generate this we used a combination of checking out old versions of
the messages in their old position and the roslib script


```
roslib/scripts/gendeps.py -m "message/filename.msg"
```

 This will return the md5sum for that message
(it is not necessary for the messages to have been autogenerated)

Use this file with the script 

```
rosrecord/scripts/fixed_moved_messages.py combined_md5s.fixed old.bag new.bag
```



### Fixing bag ordering

When logging incoming messages are buffered but there is a race
condition for getting a lock on the output file. Depending on how things
work out this may mean that the order of items in the bag is out of
order(up to seconds off, which can't be easily buffered). There is a
script bagsort.py which will sort the bag to be in chronological order.
This will get rid of dropped packets due to this.



```
rosrecord/scripts/bagsort.py old.bag new.bag
```



### ROS 0.6: Fixing md5sums after the md5sum algorithm has been changed

ROS 0.6 included a change to the md5sum generation algorithm. This,
unfortunately, breaks all current bags in the system. To bring your bags
up to date use the python script: `fix_md5sums.py` in the rosrecord
package.

The standard invocation is: 

```
rosrun rosrecord fix_md5sums.py mybagfile.bag
```

 When this
completes, `mybagfile.bag` will have the new md5sum, and the original
will be stored in `mybagfile.bag.old`

Other useful invocations are: 

```
rosrun rosrecord fix_md5sums.py *.bag
```





```cplusplus
#include "ros/ros.h"
#include <string>
#include "rosrecord/Player.h"
#include "rosrecord/AnyMsg.h"
#include "std_msgs/String.h"

// Generic callback to be invoked for any message
void all_handler(std::string name,         // Topic name
                 ros::Message* m,          // Message pointer
                 ros::Time t,              // Shifted and scaled time
                 ros::Time t_orig,         // Message timestamp
                 void* n)                  // Void pointer     
{
  // Do something that doesn't require understanding the message contents
}

void string_handler(std::string name,      // Topic name       
                    std_msgs::String* str, // Message pointer  
                    ros::Time t,           // Shifted and scaled time     
                    ros::Time t_orig,      // Message timestamp
                    void* n)               // Void pointer     
{
  // Do something with the std_msgs::String
}

int main(int argc, char **argv)
{
  ros::record::Player player;

  if (player.open(std::string("my.bag"), ros::Time()))
  {
    player.addHandler<AnyMsg>(std::string("*"), // Topic name
                              &all_handler,     // Handler
                              NULL,             // void*
                              false);           // Don't deserialize

    // NOTE: serialization is required by the signature of the
    // handler above
    player.addHandler<std_msgs::String>(std::string("chatter"),
                                        &string_handler,
                                        NULL);
  }

  // Spin until we have consumed the bag
  while(player.nextMsg())  {}

  return 0;
}
```

0

(NOTE: you may have to chmod the fix_md5sums.py file so that it is
executable before you can rosrun it)

## Technical Details

Please see [bag format](Bags/Format).

## Command-Line Tools

The following command-line tools are being phased out. Please try to
avoid using them. Instead use the corresponding [rosbag](rosbag)
utilities.

### rosrecord

This command has been replaced by [rosbag record](rosbag#record)



```cplusplus
#include "ros/ros.h"
#include <string>
#include "rosrecord/Player.h"
#include "rosrecord/AnyMsg.h"
#include "std_msgs/String.h"

// Generic callback to be invoked for any message
void all_handler(std::string name,         // Topic name
                 ros::Message* m,          // Message pointer
                 ros::Time t,              // Shifted and scaled time
                 ros::Time t_orig,         // Message timestamp
                 void* n)                  // Void pointer     
{
  // Do something that doesn't require understanding the message contents
}

void string_handler(std::string name,      // Topic name       
                    std_msgs::String* str, // Message pointer  
                    ros::Time t,           // Shifted and scaled time     
                    ros::Time t_orig,      // Message timestamp
                    void* n)               // Void pointer     
{
  // Do something with the std_msgs::String
}

int main(int argc, char **argv)
{
  ros::record::Player player;

  if (player.open(std::string("my.bag"), ros::Time()))
  {
    player.addHandler<AnyMsg>(std::string("*"), // Topic name
                              &all_handler,     // Handler
                              NULL,             // void*
                              false);           // Don't deserialize

    // NOTE: serialization is required by the signature of the
    // handler above
    player.addHandler<std_msgs::String>(std::string("chatter"),
                                        &string_handler,
                                        NULL);
  }

  // Spin until we have consumed the bag
  while(player.nextMsg())  {}

  return 0;
}
```

1

`rosrecord` will generate a ".bag" file (so named for historical
reasons) with the contents of all topics that you pass to it. The file
simply contains interlaced, serialized ros messages dumped directly to a
single file as they come in over the wire. This is the most performance
and disk-friendly recording format possible. If you are recording
messages at a high-bandwidth, such as from cameras, it is strongly
recommended you run rosrecord on the same machine as the camera, and
specify the file destination as being on the local machine disk.

If you run `rosrecord` with the "-a" option, it will attempt to
record ALL messages available in the system. However, since this
information requires polling the master periodically, it will likely
miss the first several messages published on any topic.

As of ROS-0.10, rosrecord contains an experimental snapshot recorder.
This will keep a rolling buffer (the size of the maximum internal
buffer), which can be triggered by calling `rosrecord -t`. The API for
using rosrecord in snapshot mode will likely change in ROS-0.11 based on
feedback about 0.10.

`rosrecord` is installed to the `$ROS_ROOT/bin` directory and so can
be used without needing rosrun.

#### Example usages

-   Record all messages in the system. 

```cplusplus
#include "ros/ros.h"
#include <string>
#include "rosrecord/Player.h"
#include "rosrecord/AnyMsg.h"
#include "std_msgs/String.h"

// Generic callback to be invoked for any message
void all_handler(std::string name,         // Topic name
                 ros::Message* m,          // Message pointer
                 ros::Time t,              // Shifted and scaled time
                 ros::Time t_orig,         // Message timestamp
                 void* n)                  // Void pointer     
{
  // Do something that doesn't require understanding the message contents
}

void string_handler(std::string name,      // Topic name       
                    std_msgs::String* str, // Message pointer  
                    ros::Time t,           // Shifted and scaled time     
                    ros::Time t_orig,      // Message timestamp
                    void* n)               // Void pointer     
{
  // Do something with the std_msgs::String
}

int main(int argc, char **argv)
{
  ros::record::Player player;

  if (player.open(std::string("my.bag"), ros::Time()))
  {
    player.addHandler<AnyMsg>(std::string("*"), // Topic name
                              &all_handler,     // Handler
                              NULL,             // void*
                              false);           // Don't deserialize

    // NOTE: serialization is required by the signature of the
    // handler above
    player.addHandler<std_msgs::String>(std::string("chatter"),
                                        &string_handler,
                                        NULL);
  }

  // Spin until we have consumed the bag
  while(player.nextMsg())  {}

  return 0;
}
```

2

```{=html}
<!-- -->
```
-   Record all messages on the topics `chatter` and `babble`
    

```cplusplus
#include "ros/ros.h"
#include <string>
#include "rosrecord/Player.h"
#include "rosrecord/AnyMsg.h"
#include "std_msgs/String.h"

// Generic callback to be invoked for any message
void all_handler(std::string name,         // Topic name
                 ros::Message* m,          // Message pointer
                 ros::Time t,              // Shifted and scaled time
                 ros::Time t_orig,         // Message timestamp
                 void* n)                  // Void pointer     
{
  // Do something that doesn't require understanding the message contents
}

void string_handler(std::string name,      // Topic name       
                    std_msgs::String* str, // Message pointer  
                    ros::Time t,           // Shifted and scaled time     
                    ros::Time t_orig,      // Message timestamp
                    void* n)               // Void pointer     
{
  // Do something with the std_msgs::String
}

int main(int argc, char **argv)
{
  ros::record::Player player;

  if (player.open(std::string("my.bag"), ros::Time()))
  {
    player.addHandler<AnyMsg>(std::string("*"), // Topic name
                              &all_handler,     // Handler
                              NULL,             // void*
                              false);           // Don't deserialize

    // NOTE: serialization is required by the signature of the
    // handler above
    player.addHandler<std_msgs::String>(std::string("chatter"),
                                        &string_handler,
                                        NULL);
  }

  // Spin until we have consumed the bag
  while(player.nextMsg())  {}

  return 0;
}
```

3

### rosplay

This command has been replaced by [rosbag play](rosbag#play) and
[rosbag info](rosbag#info)



```cplusplus
#include "ros/ros.h"
#include <string>
#include "rosrecord/Player.h"
#include "rosrecord/AnyMsg.h"
#include "std_msgs/String.h"

// Generic callback to be invoked for any message
void all_handler(std::string name,         // Topic name
                 ros::Message* m,          // Message pointer
                 ros::Time t,              // Shifted and scaled time
                 ros::Time t_orig,         // Message timestamp
                 void* n)                  // Void pointer     
{
  // Do something that doesn't require understanding the message contents
}

void string_handler(std::string name,      // Topic name       
                    std_msgs::String* str, // Message pointer  
                    ros::Time t,           // Shifted and scaled time     
                    ros::Time t_orig,      // Message timestamp
                    void* n)               // Void pointer     
{
  // Do something with the std_msgs::String
}

int main(int argc, char **argv)
{
  ros::record::Player player;

  if (player.open(std::string("my.bag"), ros::Time()))
  {
    player.addHandler<AnyMsg>(std::string("*"), // Topic name
                              &all_handler,     // Handler
                              NULL,             // void*
                              false);           // Don't deserialize

    // NOTE: serialization is required by the signature of the
    // handler above
    player.addHandler<std_msgs::String>(std::string("chatter"),
                                        &string_handler,
                                        NULL);
  }

  // Spin until we have consumed the bag
  while(player.nextMsg())  {}

  return 0;
}
```

4 `rosplay` will take the contents of 1 or
more bag file, and play them back in a time-synchronized fashion. Time
synchronization occurs based on the global time-stamps at which messages
were received. Playing will begin immediately, and then future messages
will be published according to the relative offset times. If two
separate bag files are used, they are treated as a single bag with
interlaced times according to the timestamps. This means if you record 1
bag, wait an hour, and record a second bag, when you play them back
together you will have an hour-long dead period in the middle of your
playback.

If you do not want to observe playback timing, the "-a" option will
playback all messages from the file as fast as possible. Note that for
large files this will often lead to exceeding your incoming buffers.

Additionally, during playing, you can pause at any time by hitting
space. When paused, you can step through messages by pressing s.

To check the contents of a bag, run with the "-c" option. This will
not play back the logfile, but will instead determine the count of each
type of message in the file.

`rosplay` is installed to the `$ROS_ROOT/bin` directory and so can be
used without needing rosrun.

Example usage: 

```cplusplus
#include "ros/ros.h"
#include <string>
#include "rosrecord/Player.h"
#include "rosrecord/AnyMsg.h"
#include "std_msgs/String.h"

// Generic callback to be invoked for any message
void all_handler(std::string name,         // Topic name
                 ros::Message* m,          // Message pointer
                 ros::Time t,              // Shifted and scaled time
                 ros::Time t_orig,         // Message timestamp
                 void* n)                  // Void pointer     
{
  // Do something that doesn't require understanding the message contents
}

void string_handler(std::string name,      // Topic name       
                    std_msgs::String* str, // Message pointer  
                    ros::Time t,           // Shifted and scaled time     
                    ros::Time t_orig,      // Message timestamp
                    void* n)               // Void pointer     
{
  // Do something with the std_msgs::String
}

int main(int argc, char **argv)
{
  ros::record::Player player;

  if (player.open(std::string("my.bag"), ros::Time()))
  {
    player.addHandler<AnyMsg>(std::string("*"), // Topic name
                              &all_handler,     // Handler
                              NULL,             // void*
                              false);           // Don't deserialize

    // NOTE: serialization is required by the signature of the
    // handler above
    player.addHandler<std_msgs::String>(std::string("chatter"),
                                        &string_handler,
                                        NULL);
  }

  // Spin until we have consumed the bag
  while(player.nextMsg())  {}

  return 0;
}
```

5

### rosrebag

This command has been replaced by [rosbag filter](rosbag#filter)

`rosrebag` is a command-line tool for converting bag files using
Python expressions. The Python expression can access any of the Python
builtins plus:

-   `topic`: the topic of the message
-   `m`: the message
-   `t`: time of message. The time is represented as a [rospy](rospy)
    [Time](http://pr.willowgarage.com/pr-docs/ros-packages/rospy/html/classrospy_1_1msg_1_1Time.html)
    object (`t.secs`, `t.nsecs`)



```cplusplus
#include "ros/ros.h"
#include <string>
#include "rosrecord/Player.h"
#include "rosrecord/AnyMsg.h"
#include "std_msgs/String.h"

// Generic callback to be invoked for any message
void all_handler(std::string name,         // Topic name
                 ros::Message* m,          // Message pointer
                 ros::Time t,              // Shifted and scaled time
                 ros::Time t_orig,         // Message timestamp
                 void* n)                  // Void pointer     
{
  // Do something that doesn't require understanding the message contents
}

void string_handler(std::string name,      // Topic name       
                    std_msgs::String* str, // Message pointer  
                    ros::Time t,           // Shifted and scaled time     
                    ros::Time t_orig,      // Message timestamp
                    void* n)               // Void pointer     
{
  // Do something with the std_msgs::String
}

int main(int argc, char **argv)
{
  ros::record::Player player;

  if (player.open(std::string("my.bag"), ros::Time()))
  {
    player.addHandler<AnyMsg>(std::string("*"), // Topic name
                              &all_handler,     // Handler
                              NULL,             // void*
                              false);           // Don't deserialize

    // NOTE: serialization is required by the signature of the
    // handler above
    player.addHandler<std_msgs::String>(std::string("chatter"),
                                        &string_handler,
                                        NULL);
  }

  // Spin until we have consumed the bag
  while(player.nextMsg())  {}

  return 0;
}
```

6

Example:



```cplusplus
#include "ros/ros.h"
#include <string>
#include "rosrecord/Player.h"
#include "rosrecord/AnyMsg.h"
#include "std_msgs/String.h"

// Generic callback to be invoked for any message
void all_handler(std::string name,         // Topic name
                 ros::Message* m,          // Message pointer
                 ros::Time t,              // Shifted and scaled time
                 ros::Time t_orig,         // Message timestamp
                 void* n)                  // Void pointer     
{
  // Do something that doesn't require understanding the message contents
}

void string_handler(std::string name,      // Topic name       
                    std_msgs::String* str, // Message pointer  
                    ros::Time t,           // Shifted and scaled time     
                    ros::Time t_orig,      // Message timestamp
                    void* n)               // Void pointer     
{
  // Do something with the std_msgs::String
}

int main(int argc, char **argv)
{
  ros::record::Player player;

  if (player.open(std::string("my.bag"), ros::Time()))
  {
    player.addHandler<AnyMsg>(std::string("*"), // Topic name
                              &all_handler,     // Handler
                              NULL,             // void*
                              false);           // Don't deserialize

    // NOTE: serialization is required by the signature of the
    // handler above
    player.addHandler<std_msgs::String>(std::string("chatter"),
                                        &string_handler,
                                        NULL);
  }

  // Spin until we have consumed the bag
  while(player.nextMsg())  {}

  return 0;
}
```

7

In order to test the filter pattern that you pass in, you can also pass
in a print expression. For example:



```cplusplus
#include "ros/ros.h"
#include <string>
#include "rosrecord/Player.h"
#include "rosrecord/AnyMsg.h"
#include "std_msgs/String.h"

// Generic callback to be invoked for any message
void all_handler(std::string name,         // Topic name
                 ros::Message* m,          // Message pointer
                 ros::Time t,              // Shifted and scaled time
                 ros::Time t_orig,         // Message timestamp
                 void* n)                  // Void pointer     
{
  // Do something that doesn't require understanding the message contents
}

void string_handler(std::string name,      // Topic name       
                    std_msgs::String* str, // Message pointer  
                    ros::Time t,           // Shifted and scaled time     
                    ros::Time t_orig,      // Message timestamp
                    void* n)               // Void pointer     
{
  // Do something with the std_msgs::String
}

int main(int argc, char **argv)
{
  ros::record::Player player;

  if (player.open(std::string("my.bag"), ros::Time()))
  {
    player.addHandler<AnyMsg>(std::string("*"), // Topic name
                              &all_handler,     // Handler
                              NULL,             // void*
                              false);           // Don't deserialize

    // NOTE: serialization is required by the signature of the
    // handler above
    player.addHandler<std_msgs::String>(std::string("chatter"),
                                        &string_handler,
                                        NULL);
  }

  // Spin until we have consumed the bag
  while(player.nextMsg())  {}

  return 0;
}
```

8

Example output: 

```cplusplus
#include "ros/ros.h"
#include <string>
#include "rosrecord/Player.h"
#include "rosrecord/AnyMsg.h"
#include "std_msgs/String.h"

// Generic callback to be invoked for any message
void all_handler(std::string name,         // Topic name
                 ros::Message* m,          // Message pointer
                 ros::Time t,              // Shifted and scaled time
                 ros::Time t_orig,         // Message timestamp
                 void* n)                  // Void pointer     
{
  // Do something that doesn't require understanding the message contents
}

void string_handler(std::string name,      // Topic name       
                    std_msgs::String* str, // Message pointer  
                    ros::Time t,           // Shifted and scaled time     
                    ros::Time t_orig,      // Message timestamp
                    void* n)               // Void pointer     
{
  // Do something with the std_msgs::String
}

int main(int argc, char **argv)
{
  ros::record::Player player;

  if (player.open(std::string("my.bag"), ros::Time()))
  {
    player.addHandler<AnyMsg>(std::string("*"), // Topic name
                              &all_handler,     // Handler
                              NULL,             // void*
                              false);           // Don't deserialize

    // NOTE: serialization is required by the signature of the
    // handler above
    player.addHandler<std_msgs::String>(std::string("chatter"),
                                        &string_handler,
                                        NULL);
  }

  // Spin until we have consumed the bag
  while(player.nextMsg())  {}

  return 0;
}
```

9
