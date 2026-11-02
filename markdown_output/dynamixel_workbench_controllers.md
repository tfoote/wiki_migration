*ROS Software Maintainer: [ROBOTIS](http://wiki.ros.org/ROBOTIS)*

## ROBOTIS e-Manual

- [ROBOTIS e-Manual for Dynamixel-Workbench](http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/)

## ROS API

### position_control

#### Published Topics

- `dynamixel_state`
  ([dynamixel_workbench_msgs/msg/DynamixelStateList](https://docs.ros.org/en/rolling/p/dynamixel_workbench_msgs/msg/DynamixelStateList.html)):
  Provides some states for connected Dynamixel by reading
  [control table](http://emanual.robotis.com/docs/en/dxl/x/xm430-w350/).

#### Services

- `joint_command`
  ([dynamixel_workbench_msgs/srv/JointCommand](https://docs.ros.org/en/rolling/p/dynamixel_workbench_msgs/srv/JointCommand.html)):
  Get commands and write value to Goal Position address in control table
  of connected Dynamixel

#### Parameters

- `/device_name` (`String`, default: `/dev/ttyUSB0`): Configure USB port
  name
- `/baud_rate` (`uint32_t`, default: `57600`): Configure baud rate for
  connecting Dynamixel
- `/scan_range` (`uint8_t`, default: `10`): Configure scan range for
  connecting Dynamixel
- `/profile_velocity` (`uint32_t`, default: `200`): Velocity Value of
  Profile
- `/profile_acceleration` (`uint32_t`, default: `50`): Acceleration
  Value of Profile

### velocity_control

#### Published Topics

- `dynamixel_state`
  ([dynamixel_workbench_msgs/msg/DynamixelStateList](https://docs.ros.org/en/rolling/p/dynamixel_workbench_msgs/msg/DynamixelStateList.html)):
  Provides some states for connected Dynamixel by reading
  [control table](http://emanual.robotis.com/docs/en/dxl/x/xm430-w350/).

#### Services

- `velocity_command`
  ([dynamixel_workbench_msgs/srv/WheelCommand](https://docs.ros.org/en/rolling/p/dynamixel_workbench_msgs/srv/WheelCommand.html)):
  Get commands and write value to Goal Velocity or Moving Speed address
  in control table of connected Dynamixel

#### Parameters

- `/device_name` (`String`, default: `/dev/ttyUSB0`): Configure USB port
  name
- `/baud_rate` (`uint32_t`, default: `57600`): Configure baud rate for
  connecting Dynamixel
- `/left_wheel` (`uint8_t`, default: `1`): Configure ID of Dynamixel
- `/right_wheel` (`uint8_t`, default: `2`): Configure ID of Dynamixel
- `/profile_velocity` (`uint32_t`, default: `200`): Velocity Value of
  Profile
- `/profile_acceleration` (`uint32_t`, default: `50`): Acceleration
  Value of Profile

### torque_control

#### Published Topics

- `dynamixel_state`
  ([dynamixel_workbench_msgs/msg/DynamixelStateList](https://docs.ros.org/en/rolling/p/dynamixel_workbench_msgs/msg/DynamixelStateList.html)):
  Provides some states for connected Dynamixel by reading
  [control table](http://emanual.robotis.com/docs/en/dxl/x/xm430-w350/).

#### Services

- `joint_command`
  ([dynamixel_workbench_msgs/srv/JointCommand](https://docs.ros.org/en/rolling/p/dynamixel_workbench_msgs/srv/JointCommand.html)):
  Get commands and write value to Goal Current address in control table
  of connected Dynamixel

#### Parameters

- `/device_name` (`String`, default: `/dev/ttyUSB0`): Configure USB port
  name
- `/baud_rate` (`uint32_t`, default: `3000000`): Configure baud rate for
  connecting Dynamixel
- `/pan_id` (`uint8_t`, default: `1`): Configure ID of Dynamixel
- `/tilt_id` (`uint8_t`, default: `2`): Configure ID of Dynamixel
- `/p_gain` (`float`, default: `0.003`): Set p gain for PID feedback
  control
- `/d_gain` (`float`, default: `0.00002`): Set d gain for PID feedback
  control

### multi_port

#### Published Topics

- `dynamixel_state`
  ([dynamixel_workbench_msgs/msg/DynamixelStateList](https://docs.ros.org/en/rolling/p/dynamixel_workbench_msgs/msg/DynamixelStateList.html)):
  Provides some states for connected Dynamixel by reading
  [control table](http://emanual.robotis.com/docs/en/dxl/x/xm430-w350/).

#### Services

- `joint_command`
  ([dynamixel_workbench_msgs/srv/JointCommand](https://docs.ros.org/en/rolling/p/dynamixel_workbench_msgs/srv/JointCommand.html)):
  Get commands and write value to Goal Current address in control table
  of connected Dynamixel

#### Parameters

- `/pan_device_name` (`String`, default: `/dev/ttyUSB0`): Configure USB
  port name
- `/pan_baud_rate` (`uint32_t`, default: `57600`): Configure baud rate
  for connecting Dynamixel
- `/tilt_device_name` (`String`, default: `/dev/ttyUSB1`): Configure USB
  port name
- `/tilt_baud_rate` (`uint32_t`, default: `57600`): Configure baud rate
  for connecting Dynamixel
- `/scan_range` (`uint8_t`, default: `10`): Configure scan range for
  connecting Dynamixel
- `/profile_velocity` (`uint32_t`, default: `200`): Velocity Value of
  Profile
- `/profile_acceleration` (`uint32_t`, default: `50`): Acceleration
  Value of Profile

## Tutorials

- [dynamixel workbench controllers tutorials](#tutorials-1) -
  This tutorial describes how to run controllers with tutorial packages.

## Tutorials

1\.
[Position Controller Tutorial](http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/#position-controller)

2.[Velocity Controller Tutorial](http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/#velocity-controller)

3\.
[Torque Controller Tutorial](http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/#torque-controller)

4\.
[Multi port Tutorial](http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/#multi-port-controller)
