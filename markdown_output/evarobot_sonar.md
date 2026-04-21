-   New Maintainer : Inovasyon Muhendislik
    <evarobot@inovasyonmuhendislik.com>

## Nodes

```clearsilver
node.0 {
  name=evarobot_sonar
  desc=`evarobot_sonar` reads IMU sensor on the Evarobot and publishes roll, pitch and yaw values.
  pub{
    0.name= sensor/sonar<n>
    0.type= sensor_msgs/Range
    0.desc= Sensor data of <n>th sonar.
  }
```

#### Parameters

```clearsilver
param {
  no_header=True

  0.name= ~devicePath
  0.default=/dev/evarobotSonar
  0.type= string
  0.desc= Driver path of sonar.

  1.name= ~namespace
  1.default=sensor
  1.type= string
  1.desc= Namespace of publisher topic.

  2.name= ~frameNamespace
  2.default=sensor
  2.type= string
  2.desc= Namespace of frame id of the sensor.

  3.name= ~alwaysOn
  3.default=true
  3.type= bool
  3.desc= if false, it doesn't publish data until a node subscribes.

  4.name= ~frequency
  4.default=10.0
  4.type= double
  4.desc= Maximum frequency of the node loop.

  5.name= ~field_of_view
  5.default=[0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]
  5.type= double
  5.desc= Beam angle of sensors in radians.

  6.name= ~minRange
  6.default= [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
  6.type= double
  6.desc= Minimum range of sonar sensors.

  7.name= ~maxRange
  7.default=[5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
  7.type= double
  7.desc= Maximum range of sonar sensors.

  8.name= ~sonarPins
  8.default=[0, 1, 2, 3, 4, 5, 6]
  8.type= int
  8.desc= Pins of sonar sensors.
```
