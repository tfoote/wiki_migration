repository: <git://github.com/neobotix/neo_driver>

```wiki
This package is obsolete and will be replaced by [[neo_base_drive_can/merged|cob_base_drive_chain]]
```

## Neo Base Drive Can

This package is a ros interface for controlling multiple can-open motors
via ros.

## Topics to subscribe / publish and configuration parameters

```clearsilver

sub {
  0.name = cmd_joint_traj
  0.type = trajectory_msgs/JointTrajectory
  0.desc = send drive commands to each drive
}
pub {
  0.name = joint_states
  0.type = sensor_msgs/JointState
  0.desc = publishes the joint state of each drive
}
param {
  0.name = PublishEffort
  0.desc = should the effort be published?
  1.name = numberOfMotors
  1.desc = how many motors are connected to the can network?
  2.name = maxDriveRate
  2.desc = how fast can the drives turn?
  3.name = cycleRate
  3.desc = how often per second should the can network be queried
  4.name = can
  4.desc = how is the computer connected to the can network?: [0: Dongle, 1: USB, 2: PCI ]
  5.name = devicePath
  5.desc = what is the can device path ( for example /dev/pcanepp24 )
  6.name = NetESD
  6.desc = network of esd cards? [0: no,  1: yes]
  7.name = BaudrateVal
  7.desc = [0: 1000 kbit/s,  1: 500 kbit/s,  2: 250 kbit/s,  3: 125 kbit/s,  4: 50 kbit/s,  5: 20 kbit/s,  6: 10 kbit/s]
  8.name = GenericBufferLen
  8.desc = the buffer length
  9.name = drive*/control_type
  9.desc = the control_type of drive nr. * [velocity_control, position_control]
  10.name = drive*/joint_name
  10.desc = what's the joint name of drive nr. * ( for example front_wheel_joint )
  11.name = drive*/EncIncrPerRevMot
  11.desc = how many encoder increments are measured per revolution
  12.name = drive*/VelMeasFrqHz
  12.desc = how many increments can be maximal returned per second?
  13.name = drive*/GearRatio
  13.desc = the gear ratio
  14.name = drive*/BeltRatio
  14.desc = the belt ratio
  15.name = drive*/Sign
  15.desc = the direction of the motor [1, -1]
  16.name = drive*/VelMaxEncIncrS
  16.desc = the maximal velocity of drive nr. *
  17.name = drive*/AccIncrS
  17.desc = (has to be implemented)
  18.name = drive*/DecIncrS
  18.desc = (has to be implemented)
  19.name = drive*/Homing
  19.desc = (has to be implemented)
  20.name = drive*/HomePos
  20.desc = (has to be implemented)
  21.name = drive*/HomeVel
  21.desc = (has to be implemented)
  22.name = drive*/HomeEvent
  22.desc = (has to be implemented)
  23.name = drive*/HomeDigIn
  23.desc = (has to be implemented)
  24.name = drive*/HomeTimeOut
  24.desc = (has to be implemented)
  25.name = drive*/VelPModeEncIncrS
  25.desc = (has to be implemented)
  26.name = drive*/CANId
  26.desc = the can identifier for motor nr * (for example 0 )
}
```

## Troubleshooting

**the neo_base_drive_can_node does not start properly**

are the pcan modules are loaded properly?

lsmod \| grep pcan

cat /proc/pcan

if these modules are not loaded you can try:

1.  sudo modprobe pcan

or

1.  insmod /path/to/pcan.ko

if this still fails you\'ve to rebuild the pcan drivers.

** /proc/pcan exists but i fail to communicate with it**

cat /proc/pcan should display your device (for example \[dng\] or
\[usb\] ) if not you\'ve to recompile the pcan driver with your modules
included.

**I don\'t receive any can message although I can send motor commands:**

set the pcan net_dev compile flag to false and recompile the pcan driver

** neo_base_drive_can fails to load the parameters for my drives **

make sure that the configuration ( param: drive\*/) exists for every
drive ( param: numberOfMotors )

*Add your own Problem and Solution here*
