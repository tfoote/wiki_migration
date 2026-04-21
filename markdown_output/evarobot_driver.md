-   New Maintainer : Inovasyon Muhendislik
    <evarobot@inovasyonmuhendislik.com>

## Nodes

```clearsilver
node.0 {
  name=evarobot_driver
  desc=`evarobot_driver` takes velocities and drives left and right motors on the Evarobot using PWM(Pulse Width Modulation).
  sub{
    0.name= cntr_wheel_vel
    0.type= geometry_msgs/Twist
    0.desc= Linear and angular velocities which are applied to the Evarobot.
  }
```

#### Parameters

```clearsilver
param {
  no_header=True
  0.name= ~commandTopic
  0.default=cntr_wheel_vel
  0.type= string
  0.desc= Topic name which is read.

  1.name= ~maxLinearVel
  1.default=1.0
  1.type= double
  1.desc= Maximum linear velocity of the Evarobot.

  2.name= ~maxAngularVel
  2.default=3.0
  2.type= double
  2.desc= Maximum angular velocity of the Evarobot.

  3.name= ~wheelSeparation
  3.default=0.32
  3.type= double
  3.desc= Distance between two wheels in meter.

  4.name= ~wheelDiameter
  4.default=0.17
  4.type= double
  4.desc= Wheel diameter in meter.

  5.name= ~pwmFrequency
  5.default=1000.0
  5.type= double
  5.desc= PWM frequency.

  6.name= ~pwmDuty
  6.default=90
  6.type= int
  6.desc= Max. duty cycle.

  7.name= ~pwmCounts
  7.default=256
  7.type= int
  7.desc= Number of pwm count.

  8.name= ~pwmMode
  8.default=2
  8.type= int
  8.desc= 1: PWMMode (||||||.....), 2: MSMode (|.|.|.|.|.|).

  9.name= ~M1_IN1
  9.default=1
  9.type= int
  9.desc= Pin number of M1_IN1.

  10.name= ~M1_IN2
  10.default=12
  10.type= int
  10.desc= Pin number of M1_IN2.

  11.name= ~M1_EN
  11.default=5
  11.type= int
  11.desc= Pin number of M1_EN.

  12.name= ~M2_IN1
  12.default=0
  12.type= int
  12.desc= Pin number of M2_IN1.

  13.name= ~M2_IN2
  13.default=19
  13.type= int
  13.desc= Pin number of M2_IN2.

  14.name= ~M2_EN
  14.default=6
  14.type= int
  14.desc= Pin number of M2_EN.
}
```
