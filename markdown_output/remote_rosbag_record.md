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



```clearsilver
name = record
desc = starts/stops rosbag-record when a corresponding service is called
srv {
 0.name = start
 0.type = std_srvs/Empty
 0.desc = start rosbag-record
 1.name = stop
 1.type = std_srvs/Empty
 1.desc = stop rosbag-record
}
param {
 0.name = ~record_all
 0.type = bool
 0.desc = equivalent of the --all option of the original rosbag-record. See http://wiki.ros.org/rosbag/Commandline#record
 1.name = ~regex
 1.type = bool
 1.desc = equivalent of --regex
 2.name = ~quiet
 2.type = bool
 2.desc = equivalent of --quiet
 3.name = ~append_date
 3.type = bool
 3.desc = equivalent of --output-prefix with an empty prefix. To set prefix string, use ~prefix parameter.
 4.name = ~verbose
 4.type = bool
 4.desc = verbose console output
 5.name = ~compression
 5.type = string
 5.desc = "bz2" to use BZ2 compression (equivalent of --bz2), "lz4" to use LZ4 compression, or "uncompressed"
 6.name = ~prefix
 6.type = string
 6.desc = filename prefix
 7.name = ~name
 7.type = string
 7.desc = --(equivalent of --output-name)-- ignored for now. Use ~prefix with false of ~append_date.
 8.name = ~topics
 8.type = string array
 8.desc = topics to be recorded
 9.name = ~buffer_size
 9.type = int
 9.desc = equivalent of --buffersize
 10.name = ~exclude_regex
 10.type = string
 10.desc = equivalent of --exclude
 11.name = ~node
 11.type = string
 11.desc = equivalent of --node
}
```





```clearsilver
name = trigger
desc = calls multiple start/stop services at once
param {
 0.name = ~regex
 0.type = string
 0.desc = regular expression which matches services you want to call
}
```





```clearsilver
name = joy_listener
desc = subscribes joystick messages and calls start/stop services when a specified button is pressed
sub {
 0.name = joy
 0.type = sensor_msgs/Joy
 0.desc = joystick input
}
param {
 0.name = ~start_button
 0.type = int
 0.default = 12
 0.desc = button id to trigger start services
 1.name = ~start_regex
 1.type = string
 1.default = <node's namespace>/start
 1.desc = regular expression which matches start services
 2.name = ~stop_button
 2.type = int
 2.default = 11
 2.desc = button id to trigger stop services
 3.name = ~stop_regex
 3.type = string
 3.default = <node's namespace>/stop
 3.desc = regular expression which matches stop services
 4.name = ~verbose
 4.type = bool
 4.default = true
 4.desc = verbose console output when calling a service
}
```


