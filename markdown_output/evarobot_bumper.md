-   New Maintainer : Inovasyon Muhendislik
    \<evarobot@inovasyonmuhendislik.com\>

## Nodes

```clearsilver
node.0 {
  name=evarobot_bumper
  desc=`evarobot_bumper` reads bumper sensors on the Evarobot and publishes all in one topic. If there is a collision, topic value is false, otherwise false.
  pub{
    0.name= bumper
    0.type= im_msgs/Bumper
    0.desc= States of bumpers.
  }
```

#### Parameters

```clearsilver
param {
  no_header=True
  0.name= ~i2c_path
  0.default=/dev/i2c-1
  0.type= string
  0.desc= Driver path of i2c which is used by bumper sensors.

  1.name= ~commandTopic
  1.default=bumper
  1.type= string
  1.desc= Name of topic.

  2.name= ~frequency
  2.type= double
  2.desc= Maximum frequency of loop.
}
```
