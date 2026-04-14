## ROS API

The [cob_head_axis](cob_head_axis) package provides a configurable node
for operating the axis of the head. ```clearsilver
 name = cob_head_axis
 desc = The `cob_head_axis` node takes in <<MsgLink(trajectory_msgs/JointTrajectory)>> messages and send this directly to the hardware. The joint states can be received by [[Topics|topics]] and the axis can be initialized, stopped or recovered via [[Services|services]].


result{
 2.name=joint_trajectory_action/result
 2.type=pr2_controllers_msgs/JointTrajectoryActionResult
 2.desc= -
}

feedback{
 0.name=joint_trajectory_action/feedback
 0.type=pr2_controllers_msgs/JointTrajectoryActionFeedback
 0.desc= -
}

sub{
 0.name = command
 0.type = trajectory_msgs/JointTrajectory
 0.desc = Receives direct commands.
}

pub{
 0.name = /joint_states
 0.type = sensor_msgs/JointState
 0.desc = Publishes the joint states of all modules.
 1.name = /diagnostics
 1.type = diagnostic_msgs/DiagnosticArray
 1.desc = Publishes the diagnostic information about the state of the robot.
}

srv{
 0.name = init
 0.type = cob_srvs/Trigger
 0.desc = Initializes the node and connects to the hardware.
 1.name = stop
 1.type = cob_srvs/Trigger
 1.desc = Stops immediately all hardware movements.
 2.name = recover
 2.type = cob_srvs/Trigger
 2.desc = Recovers the hardware after an emergency stop.
 3.name = set_operation_mode
 3.type = cob_srvs/Trigger
 3.desc = Sets the operation mode for the node.
 4.name = set_default_vel
 4.type = cob_srvs/SetDefaultVel
 4.desc = Sets the default velocity.
}

param{
 0.name = ~CanDevice
 0.type = string
 0.default = Required
 0.desc = Can module specifier, e.g. PCAN, ESD
 1.name = ~CanBaudrate
 1.type = int
 1.default = Required
 1.desc = Baudrate of can module, e.g. 1000, 500,...
 2.name = ~ModId
 2.type = int
 2.default = Required
 2.desc = Modul ID
 3.name = ~JointName
 3.type = String
 3.default = Required
 3.desc = The name of the joint in the robot description of the axis
 4.name = ~HomingDir
 4.type = int
 4.default = Required
 4.desc = -
 5.name = ~HomingDirIn
 5.type = int
 5.default = Required
 5.desc = -
 6.name = ~GearRatio
 6.type = double
 6.default = Required
 6.desc = -
 7.name = ~EnoderIncrementsPerRevMot
 7.type = int
 7.default = Required
 7.desc = -
 8.name = ~operation_mode
 8.type = string
 8.default = Required
 8.desc = -
}

req_tf{
}

prov_tf{
}
```

## Usage

All hardware configuration is done in the
[cob_hardware_config](cob_hardware_config) package. A sample parameter
file in \"cob_hardware_config/cob3-3/config/head.yaml\" could look like
this ```
CanDevice: PCAN:0
CanBaudrate: 500
ModId: 17
JointName: head_axis_joint
HomingDir: 1
MotorDirection: 1
HomingDigIn: 9
GearRatio: 62.5
EnoderIncrementsPerRevMot: 2000
operation_mode: position
```
