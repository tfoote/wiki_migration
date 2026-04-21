-   New Maintainer : Inovasyon Muhendislik
    <evarobot@inovasyonmuhendislik.com>

## Nodes



```clearsilver
node.0 {
  name=evarobot_infrared
  desc=`evarobot_infrared` reads infrared sensors on the Evarobot and outputs range value of the sensors.
  pub{
    0.name= sensor/ir<n>
    0.type= sensor_msgs/Range
    0.desc= Range of <n>th infrared sensor.
  }
```



#### Parameters



```clearsilver
param {
  no_header=True
  0.name= ~devicePath
  0.default=/dev/spidev0.0
  0.type= string
  0.desc= Driver path of spi.

  1.name= ~namespace
  1.default=sensor
  1.type= string
  1.desc= Namespace of topic.

  2.name= ~frameNamespace
  2.default=sensor
  2.type= string
  2.desc= Namespace of frame id.

  3.name= ~alwaysOn
  3.default=true
  3.type= bool
  3.desc= if false, it doesn't publish data until a node subscribes.

  4.name= ~spiMode
  4.default=0
  4.type= int
  4.desc= SPI Mode.

  5.name= ~spiSpeed
  5.default=1000000
  5.type= int
  5.desc= Speed of SPI.

  6.name= ~spiBits
  6.default=8
  6.type= int
  6.desc= SPI bits per word.

  7.name= ~frequency
  7.default=10.0
  7.type= double
  7.desc= Maximum frequency of loop.

  8.name= ~field_of_view
  8.default=[0.01, 0.01, 0.01, 0.01]
  8.type= double
  8.desc= Vision angle of infrared sensor in radian.

  9.name= ~minRange
  9.default=[0.0, 0.0, 0.0, 0.0]
  9.type= double
  9.desc= Minimum range of infrared sensor.

  10.name= ~maxRange
  10.default=[0.80, 0.80, 0.80, 0.80]
  10.type= double
  10.desc= Maximum range of infrared sensor.

  11.name= ~channelNo
  11.default=[0, 1, 2, 3]
  11.type= int
  11.desc= Channel number of infrared sensors.

  12.name= ~parK
  12.default=[0.42, 0.42, 0.42, 0.42]
  12.type= double
  12.desc= Parameter K for converting from voltage to range.

  13.name= ~parA
  13.default=[0.0000473, 0.0000473, 0.0000473, 0.0000473]
  13.type= double
  13.desc= Parameter A for converting from voltage to range.

  14.name= ~parB
  14.default=[-0.0013461, -0.0013461, -0.0013461, -0.0013461]
  14.type= double
  14.desc= Parameter B for converting from voltage to range.
}
```


