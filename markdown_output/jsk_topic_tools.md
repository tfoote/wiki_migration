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



```clearsilver
node.0 {
  name=topic_buffer_server
  desc=`topic_buffer_server` is a node that publish designated topic when receiving service or topic


  sub{
    0.name=<topic_name>
    0.type=<topic_type>
    0.desc=desingated topic 

    1.name=~update
    1.type=std_msgs/String
    1.desc=Publish designated topic when this topic is subscribed
}

  pub{
    1.name=<topic_name>_update
    1.type=<topic_type>
    1.desc=designated topic
  }
  srv{
    0.name=~list
    0.type=jsk_topic_tools/List
    0.desc=Return a list of designated topics

    1.name=~update
    1.type=jsk_topic_tools/Update
    1.desc=Publish designated topic when this service is called
  }

  param {
   
}


}

node.1 {
  name=topic_buffer_client
  desc=`topic_buffer_client` is a node that receives designated topic published by topic_buffer_server and publishes the topic frequently

  pub{
    0.name=<topic_name>_buffered
    0.type=<topic_type>
    0.desc=desingated topic 
  }
  
  sub{
    0.name=<topic_name>_update
    0.type=<topic_type>
    0.desc=desingated topic 
  }
}

node.2 {
  name=transform_merger
  desc=`transform_merger` is a node that receives and merges tf in a period of time and publishes merged tf

  pub{
    0.name=tf_merged
    0.type=tf/tfMessage
    0.desc=merged tf
  }
  
  sub{
    0.name=tf
    0.type=tf/tfMessage

  }
  param{
    0.name=~loop_hz
    0.type=double, default: 1.0
  }
}

node.3 {
  name=specific_transform_publisher
  desc=`specific_transform_publisher` is a node that receives tf and publishes specific tf

  pub{
    0.name=specific_transform
    0.type=tf/tfMessage
    0.desc=specific transform sent to specific_transform_subscriber
  }
  
  sub{
    0.name=tf
    0.type=tf/tfMessage

  }
  param{
    0.name=~parent_frame
    0.type=string
    0.desc=specific tf parent
    1.name=~child_frame
    1.type=string
    1.desc=specific tf child

  }
}

node.4 {
  name=specific_transform_subscriber
  desc=`specific_transform_subscriber` is a node that receives specific_transform and calls dynamic_tf_publisher services

  sub{
    0.name=specific_transform
    0.type=tf/tfMessage
  }
}
```


