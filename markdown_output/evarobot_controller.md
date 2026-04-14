-   New Maintainer : Inovasyon Muhendislik
    \<evarobot@inovasyonmuhendislik.com\>

## Nodes

```clearsilver
node.0 {
  name=evarobot_controller
  desc=`evarobot_controller` is basic PID controller to drive the Evarobot with referance velocities. `evarobot_controller` takes reference and measured velocities and outputs calculated velocities which will be applied to the Evarobot.
  sub{
    0.name= cmd_vel
    0.type= geometry_msgs/Twist
    0.desc= Reference velocities of linear and angular.
    1.name= wheel_vel
    1.type= geometry_msgs/PointStamped
    1.desc= Measured velocities of left and right wheels.
  }
  pub{
    0.name= cntr_wheel_vel
    0.type= geometry_msgs/Twist
    0.desc= Calculated velocities by PID controller.
  }
```

#### Parameters

```clearsilver
param {
  no_header=True
  0.name= ~desiredTopic
  0.default=cmd_vel
  0.type= string
  0.desc= Topic name of reference velocities.

  1.name= ~measuredTopic
  1.default=wheel_vel
  1.type= string
  1.desc= Topic name of measured velocities.

  2.name= ~controllerTopic
  2.default=cntr_wheel_vel
  2.type= string
  2.desc= Topic name of velocities which are outputs of PID controller.

  3.name= ~alwaysOn
  3.default=true
  3.type= bool
  3.desc= if false, it doesn't publish data until a node subscribes.

  4.name= ~wheelSeparation
  4.default=0.32
  4.type= double
  4.desc= Distance between two wheels in meter.

  5.name= ~Frequency
  5.default=10.0
  5.type= double
  5.desc= Maximum frequency of node loop.

  6.name= ~integralConstLeft
  6.default=0.5
  6.type= double
  6.desc= Integral constant of left wheel controller.

  7.name= ~derivativeConstLeft
  7.default=0.05
  7.type= double
  7.desc= Derivative constant of left wheel controller.

  8.name= ~proportionalConstLeft
  8.default=0.3
  8.type= double
  8.desc= Proportional constant of left wheel controller.

  9.name= ~integralConstRight
  9.default=0.5
  9.type= double
  9.desc= Integral constant of right wheel controller.

  10.name= ~derivativeConstRight
  10.default=0.05
  10.type= double
  10.desc= Derivative constant of right wheel controller.

  11.name= ~proportionalConstRight
  11.default=0.3
  11.type= double
  11.desc= Proportional constant of right wheel controller.
}
```
