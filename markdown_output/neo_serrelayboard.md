repository: <git://github.com/neobotix/neo_driver>

```wiki
This package is obsolete and will be replaced by [[neo_serrelayboard/merged|cob_relayboard]]
```

## Serial Relay Board

The Serial Relay Board does not only handle and publish error states (as
a laser stop or emergency stop) or the robots state (temperature,
battery volts and the battery current), it can also control
can-motor-drivers and publish range measurements (ultra sonic or infra
red).

For the Relay Board exist a couple of expansion boards: 0. Gyro Board:
publishes angular rates and acceleration on 3 axis. 1. I/O Board: 2.
Radar Board: publishes velocities.

## Topics to publish/subscribe and configuration parameters

```clearsilver

sub {
  0.name = /cmd_drives
  0.type = neo_msgs/DriveCmd
  0.desc = sets joint velocities
  1.name = /srb_lcd_display
  1.type = neo_msgs/LCDOut
  1.desc = sets lcd output
  2.name = /srb_io_set_dig_out
  2.type = neo_msgs/IOOut
  2.desc = sets digital output 
  3.name = /srb_start_us_board
  3.type = std_msgs/Int16
  3.desc = starts the ultrasonic range board 
  4.name = /srb_stop_us_board
  4.type = std_msgs/Empty
  4.desc = stops the ultrasonic board
  5.name = /srb_zero_gyro
  5.type = std_msgs/Empty
  5.desc = zeros the gyro
}
pub {
  0.name = /drive_states
  0.type = neo_msgs/DriveStates
  0.desc = publishes joint states
  1.name = /srb_io_dig_in
  1.type = std_msgs/Int16
  1.desc = publishes digital input
  2.name = /srb_io_dig_out
  2.type = std_msgs/Int16
  2.desc = publishes digital output
  3.name = /srb_io_analog_in
  3.type = neo_msgs/IOAnalogIn
  3.desc = publishes analog input
  4.name = /srb_us_measurements
  4.type = neo_msgs/USBoard
  4.desc = publishes ultrasonic sensor readings
  5.name = /srb_radar_measurements
  5.type = neo_msgs/RadarBoard
  5.desc = publishes radar sensor readings
  6.name = /srb_gyro_measurements
  6.type = neo_msgs/GyroBoard
  6.desc = publishes gyro sensor readings
  7.name = /srb_keypad
  7.type = neo_msgs/Keypad
  7.desc = publishes keypad pushbutton readings
  8.name = /srb_ir_measurements
  8.type = neo_msgs/IRSensors
  8.desc = publishes infrared range sensor readings
}

param {
  0.name = message_timeout
  0.default = 2.0
  0.desc = sets the timeout for messages sent via serial port
  1.name = requestRate
  1.default = 25.0
  1.desc = sets the rate for communicating with the serial relay board
  2.name = protocol_version
  2.default = 1
  2.desc = sets the serial relayboard version
  3.name = ComPort
  3.desc = sets the comport (for example /dev/ttyUSB1)
  4.name = drive1/CANId
  4.desc = sets the canid of the first drive
  5.name = drive2/CANId
  5.desc = sets the canid of the second drive
  6.name = drive1/joint_name
  6.desc = sets the drives jointname
  7.name = drive2/joint_name
  7.desc = sets the drives jointname
  8.name = hasMotorRight
  8.desc = are motors connected to the serial relay board? [true/false]
  9.name = hasMotorLeft
  9.desc = are motors connected to the serial relay board? [true/false]
  10.name = hasIOBoard
  10.desc = is the io-board connected? [true/false]
  11.name = hasLCDOut
  11.desc = is there an lcd display? [true/false]
  12.name = hasUSBoard
  12.desc = are us-sensors connected? [true/false]
  13.name = hasRadarBoard
  13.desc = is the radarboard connected? [true/false]
  14.name = hasGyroBoard
  14.desc = does the gyroboard exist? [true/false]
  15.name = hasKeyPad
  15.desc = is a keypad in use? [true/false]
  16.name = hasIRSensors
  16.desc = are there any ir-sensors? [true/false]
}
```

## Troubleshooting

**I can\'t communicate with the Serial Relay Board, though it powers on
and displays stuff on the LCD:**

Make sure that your config file does not enably any non existing
expansion boards/motors and that you\'ve choose the right relayboard
version and poweroff the serial relay board afterwards.

**Launching relayboard.launch fails because the \$ROBOT_drive\*.yaml
files are missing:**

Set the arg \"loadDrives\" to \"false\"

*Add your own Problem and Solution here*
