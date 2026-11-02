## Usage

**\[Step 1\]**

Launch recorder nodes with your favourite nodes. Use respawn options to
record multiple times.



```xml
<launch>

  <group ns="console">
    <include file="console.machine"/>

    ... other console nodes ...
    
    <node name="console-record" pkg="remote_rosbag_record" type="record" respawn="true">
      <rosparam file="console_topics.yml"/>
      <param name="prefix" value="console"/>
      <param name="apped_date" value="true"/>
    </node>
  </group>

  <group ns="robot">
    <include file="robot.machine"/>

    ... other robot nodes ....

    <node name="robot-record" pkg="remote_rosbag_record" type="record" respawn="true">
      <rosparam file="robot_topics.yml"/>
      <param name="prefix" value="robot"/>
      <param name="apped_date" value="true"/>
    </node>
  </group>
  
</launch>
```

 

```yaml
# xxx_topics.yml may look like this
topics:
- /joint_states
- /imu
- ...
```



**\[Step 2\]**

Start rosbag-record at your own timing

- method 1: use remote_rosbag_record/trigger node
  

```
rosrun remote_rosbag_record trigger _regex:="/.*/start"
```



<!-- -->

- method 2: use remote_rosbag_record/joy_listener node
  

```
rosrun remote_rosbag_record joy_listener _start_regex:="/.*/start" _start_button:=10 ...
```



<!-- -->

- method 3: call trigger services from your teleoperation node
  

```cpp
#include<remote_rosbag_record/call.hpp>

#include<boost/regex.hpp>

...

if (start_button_pressed) {
  remote_rosbag_record::call(boost::regex("/.*/start"));
}
```



**\[Step 3\]**

Stop rosbag-record (similar to the previous step)

## Nodes

### record

starts/stops rosbag-record when a corresponding service is called

#### Services

- `start`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  start rosbag-record
- `stop`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  stop rosbag-record

#### Parameters

- `~record_all` (`bool`): equivalent of the \--all option of the
  original rosbag-record. See
  <http://wiki.ros.org/rosbag/Commandline#record>
- `~regex` (`bool`): equivalent of \--regex
- `~quiet` (`bool`): equivalent of \--quiet
- `~append_date` (`bool`): equivalent of \--output-prefix with an empty
  prefix. To set prefix string, use prefix parameter.
- `~verbose` (`bool`): verbose console output
- `~compression` (`string`): "bz2" to use BZ2 compression (equivalent
  of \--bz2), "lz4" to use LZ4 compression, or "uncompressed"
- `~prefix` (`string`): filename prefix
- `~name` (`string`): \--(equivalent of \--output-name)\-- ignored for
  now. Use prefix with false of append_date.
- `~topics` (`string array`): topics to be recorded
- `~buffer_size` (`int`): equivalent of \--buffersize
- `~exclude_regex` (`string`): equivalent of \--exclude
- `~node` (`string`): equivalent of \--node

### trigger

calls multiple start/stop services at once

#### Parameters

- `~regex` (`string`): regular expression which matches services you
  want to call

### joy_listener

subscribes joystick messages and calls start/stop services when a
specified button is pressed

#### Subscribed Topics

- `joy`
  ([sensor_msgs/msg/Joy](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Joy.html)):
  joystick input

#### Parameters

- `~start_button` (`int`, default: `12`): button id to trigger start
  services
- `~start_regex` (`string`, default: `<node's namespace>/start`):
  regular expression which matches start services
- `~stop_button` (`int`, default: `11`): button id to trigger stop
  services
- `~stop_regex` (`string`, default: `<node's namespace>/stop`): regular
  expression which matches stop services
- `~verbose` (`bool`, default: `true`): verbose console output when
  calling a service
