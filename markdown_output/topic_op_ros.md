Perform math expressions (or any python expression) on ros topics with
data fields (ints & floats)

```
rosrun topic_op_ros topic_op.py "{'a': '/a', 'b': '/b'}" '(a + b)' /result1 
rostopic pub "a" std_msgs/Float32 "data: 0.5" 
rostopic pub "b" std_msgs/UInt8 "data: 14" 
rostopic echo /result1
```

Also publish a derivative of a topic with a float or int type:

```
rosrun topic_op derivative input_topic output_topic
```

If input_topic varies in time, then the derivative will be published to
output_topic. Because the basic types aren\'t stamped the derivative is
based on the timestamp of the reception of the published input topic.

<https://github.com/lucasw/topic_op_ros>
