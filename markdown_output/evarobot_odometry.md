-   New Maintainer : Inovasyon Muhendislik
    \<evarobot@inovasyonmuhendislik.com\>

## Nodes

```clearsilver
node.0 {
  name=evarobot_odometry
  desc=`evarobot_odometry` reads encoders on the Evarobot, calculates and outputs odometry data(position and velocities) of the Evarobot.
  pub{
    0.name= odom
    0.type= nav_msgs/Odometry
    0.desc= Odometry data.
  }
  pub{
    0.name= wheel_vel
    0.type= geometry_msgs/PointStamped
    0.desc= Right and left velocities of the Evarobot.
  }
```

#### Parameters

```clearsilver
param {
  no_header=True
  0.name= ~devicePath
  0.default=/dev/evarobotEncoder
  0.type= string
  0.desc= Driver path of encoder.

  1.name= ~alwaysOn
  1.default=true
  1.type= bool
  1.desc= if false, it doesn't publish data until a node subscribes.

  2.name= ~odomTopic
  2.default=odom
  2.type= string
  2.desc= Topic name of odometry publisher.

  3.name= ~odomFrame
  3.default=odom
  3.type= string
  3.desc= Frame name of odometry data.

  4.name= ~wheelSeparation
  4.default=0.32
  4.type= double
  4.desc= Difference between wheel in meters.

  5.name= ~height
  5.default=0.25
  5.type= double
  5.desc= Height of Evarobot base_link in meters.

  6.name= ~frequency
  6.default=100
  6.type= double
  6.desc= Maximum frequency of node loop.

  7.name= ~gearRatio
  7.default=50
  7.type= int
  7.desc= Gear Ratio of motors.

  8.name= ~CPR
  8.default=64
  8.type= int
  8.desc= CPR value of encoders.

  9.name= ~wheelDiameter
  9.default=0.17
  9.type= double
  9.desc= Diameter of driver wheel in meter
```
