-   New Maintainer : Inovasyon Muhendislik
    <evarobot@inovasyonmuhendislik.com>

## Nodes

```clearsilver
node.0 {
  name=evarobot_minimu9
  desc=`evarobot_minimu9` reads IMU sensor on the Evarobot and publishes roll, pitch and yaw values.
  pub{
    0.name= imu_data
    0.type= sensor_msgs/Imu
    0.desc= IMU sensor data.
  }
```

#### Parameters

```clearsilver
param {
  no_header=True
  0.name= ~i2cDevice
  0.default=/dev/i2c-1
  0.type= string
  0.desc= Driver path of i2c which is used by imu.

  1.name= ~topicName
  1.default=imu_data
  1.type= string
  1.desc= Name of publisher topic.

  2.name= ~frame_id
  2.default=sensor/imu_link
  2.type= string
  2.desc= Frame id of the sensor.

  3.name= ~alwaysOn
  3.default=true
  3.type= bool
  3.desc= if false, it doesn't publish data until a node subscribes.

  4.name= ~frequency
  4.default=10.0
  4.type= double
  4.desc= Maximum frequency of the node loop.
```
