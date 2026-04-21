Nodes in `rover_driver`:

/rover_serial:: :: This node directly interfaces with the rover and must
run on the same hardware the rover is physically plugged into.

Subscribers:

/motor_efforts: openrover_core_msgs/msg/RawMotorCommand:: :: Low level
motor commands expressed as bytes (left, right, flipper) being sent to
the rover

/openrover_command: openrover_core_msgs/msg/RawCommand:: :: Low-level
instructions sent to the rover as (verb, arg) pairs

Publishers:

/raw_data: openrover_core_msgs/msg/RawData:: :: Binary data being
emitted from the rover, in unprocessed form (see
<https://roverrobotics.com/blogs/news/uart-protocol> for interpretation)



```
Gauss% ros2 topic echo /raw_data
which: 14
value: ['''', '3']
---
```



/rover:: :: A higher-level node which converts between serial and ROS
concepts. This need not have direct hardware access to the rover.

Subscribers:

/cmd_vel: geometry_msgs/msg/Twist:: :: Linear and rotational velocity
the rover is requested

/raw_data: openrover_core_msgs/msg/RawData:: :: Binary data being
emitted from the rover, in unprocessed form (see
<https://roverrobotics.com/blogs/news/uart-protocol> for interpretation)

/diagnostics: diagnostic_msgs/msg/DiagnosticArray:: :: diagnostic data
being emitted by the rover, suitable for consumption by
**rqt_robot_monitor** or **diagnostic-aggregator**.

/motor_efforts: openrover_core_msgs/msg/RawMotorCommand:: :: Motor
efforts (left, right, flipper) being sent to the rover

/odom_raw: nav_msgs/msg/Odometry:: :: Wheel-based odometry

/openrover_command: openrover_core_msgs/msg/RawCommand:: :: Low-level
instructions sent to the rover as (verb, arg) pairs

An example of what diagnostics might look like:



```
Gauss% ros2 topic echo /diagnostics
header:
  stamp:
    sec: 1596074200
    nanosec: 555623392
  frame_id: ''
status:
- level: "\0"
  name: 'over: power'
  message: Okay
  hardware_id: OpenRover
  values:
  - key: battery A state of charge
    value: '0.3'
  - key: battery B state of charge
    value: '0.3'
  - key: battery A current
    value: '0.617647'
  - key: battery B current
    value: '0.235294'
  - key: battery A current (internal)
    value: '-0.185'
  - key: battery B current (internal)
    value: '-0.19'
  - key: battery charging state
    value: 'False'
- level: "\0"
  name: 'over: firmware'
  message: Okay
  hardware_id: OpenRover
  values:
  - key: firmware revision
    value: 1.10.1
- level: "\0"
  name: 'over: drive'
  message: Okay
  hardware_id: OpenRover
  values:
  - key: left encoder displacement
    value: '10035'
  - key: right encoder displacement
    value: '10040'
  - key: left encoder period
    value: '0'
  - key: right encoder period
    value: '0'
  - key: left motor temperature
    value: '27'
  - key: cooling fan 1 duty factor
    value: '0'
  - key: cooling fan 2 duty factor
    value: '0'
---
```


