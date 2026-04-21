## Device Driver Nodes

This package contains ROS drivers for all servo devices on the ART
autonomous vehicle.



```clearsilver
node.0 {
 name = brake
 desc = Driver for ART brake servo mechanism.
 sub {
  0.name = brake/cmd
  0.type = art_msgs/BrakeCommand
  0.desc = brake commands
 }
 pub {
  0.name = brake/state
  0.type = art_msgs/BrakeState
  0.desc = brake status information
 }
 param {
  0.name = ~port
  0.type = string
  0.desc = Serial port name for the brake servo. Simulate device, if `/dev/null`.
  0.default = `"/dev/brake"`

  1.name = ~apply_on_exit
  1.type = bool
  1.desc = Apply full brake during shutdown.
  1.default = `false`

  2.name = ~training
  2.type = bool
  2.desc = Publish brake data, but do not send it any commands.  This mode collects data while a human driver operates the vehicle.
  2.default = `false`

  3.name = ~diagnostic
  3.type = bool
  3.desc = Publish extra diagnostic brake information not needed for normal operation.
  3.default = `false`
 }
}
```



#### Examples

Test the ART brake driver using `/dev/null`, publishing simulated
`brake/state` messages and accepting `brake/cmd` messages.


```
rosrun art_servo brake
```



Run the brake driver with the real ART brake device. The port assignment
gets saved in the ROS parameter server, persisting across future
invocations until `roscore` stops. 

```
rosrun art_servo brake _port:=/dev/brake
```





```clearsilver
node.0 {
 name = ioadr
 desc = Driver for National Control Devices IOADR8x multipurpose I/O board.
 sub {
  0.name = ioadr/cmd
  0.type = art_msgs/IOadrCommand
  0.desc = commands to set or clear relays
 }
 pub {
  0.name = ioadr/state
  0.type = art_msgs/IOadrState
  0.desc = ioadr status information: relays, digital input and analog voltages
 }
 param {
  0.name = ~port
  0.type = string
  0.desc = Serial port name for the ioadr device. Simulate device, if `/dev/null`.
  0.default = `"/dev/ioadr8x"`
  1.name = ~shifter
  1.type = string
  1.desc = set `false` when not controlling shifter interface.
  1.default = false
 }
}
```



#### Examples

Test the ART ioadr driver with `/dev/null`, publishing simulated
`ioadr/state` messages and accepting `ioadr/cmd` messages.


```
rosrun art_servo ioadr _port:=/dev/null
```



Run the ART ioadr driver connected to the I/O board on serial port
`/dev/ioadr`, publishing `ioadr/state` messages and accepting
`ioadr/cmd` messages. The port assignment gets saved in the ROS
parameter server, persisting across future invocations until `roscore`
stops. 

```
rosrun art_servo ioadr
```





```clearsilver
node.0 {
 name = shifter
 desc = Gear Shifter Driver, uses an instance of the ioadr driver communicating with a separate, dedicated NCD IOADR8x board connected to an Arens Controls shifter mechanism.
 sub {
  0.name = shifter/cmd
  0.type = art_msgs/Shifter
  0.desc = gear shift requests
 }
 pub {
  0.name = shifter/state
  0.type = art_msgs/Shifter
  0.desc = shifter status: current gear, relay values
 }
 param {
  0.name = ~port
  0.type = string
  0.desc = Serial port name for the ioadr device. Simulate device, if `/dev/null`.
  0.default = `"/dev/shifter"`
  1.name = ~shifter
  1.type = string
  1.desc = set `true` for shifter control interface.
  1.default = false
 }
}
```



#### Examples

Test the ART shifter driver with `/dev/null`, publishing simulated
`shifter/state` messages and accepting `shifter/cmd` messages.


```
rosrun art_servo ioadr shifter:=true _port:=/dev/null
```



Run the ART shifter driver connected to the I/O board on serial port
`/dev/shifter`, publishing `shifter/state` messages and accepting
`shifter/cmd` messages. The port assignment gets saved in the ROS
parameter server, persisting across future invocations until `roscore`
stops. 

```
rosrun art_servo ioadr shifter:=true
```





```clearsilver
node.0 {
 name = steering
 desc = Steering Servo Driver.
 sub {
  0.name = steering/cmd
  0.type = art_msgs/SteeringCommand
  0.desc = steering requests
 }
 pub {
  0.name = steering/state
  0.type = art_msgs/SteeringState
  0.desc = steering status information, including wheel angle
 }
 param {
  0.name = ~port
  0.type = string
  0.desc = Serial port name for the steering device. Simulate device, if `/dev/null`.
  0.default = `"/dev/steering"`

  2.name = ~training
  2.type = bool
  2.desc = Publish steering data, but do not send any commands.  This mode collects data while a human driver operates the vehicle.
  2.default = `false`

  3.name = ~diagnostic
  3.type = bool
  3.desc = Publish extra diagnostic steering information not needed for normal operation.
  3.default = `false`
 }
}
```



#### Examples

Test the ART steering driver using `/dev/null`, publishing simulated
`steering/state` messages and accepting `steering/cmd` messages.


```
rosrun art_servo brake
```

0

Run the steering driver with the real ART steering controller. The port
assignment gets saved in the ROS parameter server, persisting across
future invocations until `roscore` stops. 

```
rosrun art_servo brake
```

1



```
rosrun art_servo brake
```

2

#### Examples

Test the ART throttle driver using `/dev/null`, publishing simulated
`throttle/state` messages and accepting `throttle/cmd` messages.


```
rosrun art_servo brake
```

3

Run the throttle driver with the real ART throttle controller. The port
assignment gets saved in the ROS parameter server, persisting across
future invocations until `roscore` stops. 

```
rosrun art_servo brake
```

4

## Utility Commands



```
rosrun art_servo brake
```

5

#### Usage



```
rosrun art_servo brake
```

6

#### Examples

Shift the transmission into Neutral. 

```
rosrun art_servo brake
```

7

Shift the transmission into Drive. 

```
rosrun art_servo brake
```

8

Shift the transmission into Reverse. 

```
rosrun art_servo brake
```

9
