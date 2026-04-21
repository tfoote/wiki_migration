## Description

The tf_publisher_gui is based on David Lu!!'s joint_state_publisher.
Here is how it looks:

![](attachment:tf_publisher_gui.png)

Run it like this:

```
rosrun tf_publisher_gui tf_publisher_gui _parent_frame:=/odom_combined _child_frame:=/head_mount_kinect_link
```

## ROS API

```clearsilver
name = tf_publisher_gui
desc = 
param {
  0.name = ~rate
  0.type = double
  0.default = 10
  0.desc = The rate at which to publish the tf transforms
  1.name = ~parent_frame
  1.type = string
  1.default = REQUIRED
  1.desc = the parent tf frame
  2.name = ~child_frame
  2.type = string
  2.default = REQUIRED
  2.desc = the child tf frame
}
prov_tf {
  0.from = ~parent_frame
  0.to = ~child_frame
}
```
