## ROS API



```clearsilver
node.0 {
name=imu_attitude_to_tf_node
desc=`imu_attitude_to_tf_node` is a node that publishes roll/pitch attitude angles provided by an IMU to tf.
sub{
0.name= imu_topic
0.type= sensor_msgs/Imu
0.desc= The topic on which IMU data is provided. Has to be remapped to the appropiate topic name on the given robot setup.
}
param{
    0.name = ~base_stabilized_frame
    0.type = string
    0.default = `"base_stabilized_frame"`
    0.desc = The name of the robot base stabilized frame that has the x and y axis parallel to the ground
    1.name = ~base_frame
    1.type = string
    1.default = `"base_frame"`
    1.desc = The name of the robot base frame rotated around the roll/pitch angles reported by the IMU message

}
}
}
```


