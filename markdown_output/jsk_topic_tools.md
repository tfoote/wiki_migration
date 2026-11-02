## USAGE

### topic_buffer_server



```
rosrun jsk_topic_tools topic_buffer_server IN_TOPIC1 [IN_TOPIC2 [...]]
```



### topic_buffer_server



```
rosrun jsk_topic_tools topic_buffer_client /list:=<topic_buffer_server_name>/list  /update:=<topic_buffer_server_name>/update
```



### transform_merger



```
rosrun jsk_topic_tools transform_merger
```



## SAMPLE

### topic_buffer_\[server/client\] Sample



```
roslaunch jsk_topic_tools topic_buffer_server_sample.launch
```





```
roslaunch jsk_topic_tools topic_buffer_client_sample.launch
```



### tf_buffer_\[server/client\] Sample



```
roslaunch jsk_topic_tools tf_buffer_server_sample.launch
```





```
roslaunch jsk_topic_tools tf_buffer_client_sample.launch
```



### specific_transform_\[publisher/subscriber\] Sample



```
roslaunch jsk_topic_tools specific_transform_publisher_sample.launch
```

 

```
roslaunch jsk_topic_tools specific_transform_subscriber_sample.launch
```



## ROS API

### topic_buffer_server

`topic_buffer_server` is a node that publish designated topic when
receiving service or topic

#### Subscribed Topics

- `<topic_name>` (`<topic_type>`): desingated topic
- `~update`
  ([std_msgs/msg/String](https://docs.ros.org/en/rolling/p/std_msgs/msg/String.html)):
  Publish designated topic when this topic is subscribed

#### Published Topics

- `<topic_name>_update` (`<topic_type>`): designated topic

#### Services

- `~list`
  ([jsk_topic_tools/srv/List](https://docs.ros.org/en/rolling/p/jsk_topic_tools/srv/List.html)):
  Return a list of designated topics
- `~update`
  ([jsk_topic_tools/srv/Update](https://docs.ros.org/en/rolling/p/jsk_topic_tools/srv/Update.html)):
  Publish designated topic when this service is called

### topic_buffer_client

`topic_buffer_client` is a node that receives designated topic
published by topic_buffer_server and publishes the topic frequently

#### Subscribed Topics

- `<topic_name>_update` (`<topic_type>`): desingated topic

#### Published Topics

- `<topic_name>_buffered` (`<topic_type>`): desingated topic

### transform_merger

`transform_merger` is a node that receives and merges tf in a period
of time and publishes merged tf

#### Subscribed Topics

- `tf`
  ([tf/msg/tfMessage](https://docs.ros.org/en/rolling/p/tf/msg/tfMessage.html))

#### Published Topics

- `tf_merged`
  ([tf/msg/tfMessage](https://docs.ros.org/en/rolling/p/tf/msg/tfMessage.html)):
  merged tf

#### Parameters

- `~loop_hz` (`double, default: 1.0`)

### specific_transform_publisher

`specific_transform_publisher` is a node that receives tf and
publishes specific tf

#### Subscribed Topics

- `tf`
  ([tf/msg/tfMessage](https://docs.ros.org/en/rolling/p/tf/msg/tfMessage.html))

#### Published Topics

- `specific_transform`
  ([tf/msg/tfMessage](https://docs.ros.org/en/rolling/p/tf/msg/tfMessage.html)):
  specific transform sent to specific_transform_subscriber

#### Parameters

- `~parent_frame` (`string`): specific tf parent
- `~child_frame` (`string`): specific tf child

### specific_transform_subscriber

`specific_transform_subscriber` is a node that receives
specific_transform and calls dynamic_tf_publisher services

#### Subscribed Topics

- `specific_transform`
  ([tf/msg/tfMessage](https://docs.ros.org/en/rolling/p/tf/msg/tfMessage.html))
