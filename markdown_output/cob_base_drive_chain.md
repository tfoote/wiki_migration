## Platform Control

To keep the communication with the Care-O-Bot platform variable (as
different motors or CAN-hardware could be used),
`cob_base_drive_chain::CanCtrlPltfCOb3` implements the communication
to different motors through a generic interface
`cob_canopen_motor::CanDriveItf` and for different CAN modules through
`cob_generic_can::CanItf`. The used CAN module is specified in an
.ini-File, as well as motor-specific parameters. Each motor-object is
loaded with appropriate parameters and during initialization each wheel
is homed.

After initialization, the user can easily command the platform using the
provided functions of `cob_base_drive_chain::CanCtrlPltfCOb3` like
`setVelGearRadS`.

To bring these communication facilities to the ROS network, the node
cob_base_driove_chain_node uses that communication class and provides
its functions to the ROS network as services. This makes it quite easy
to create different controllers (e.g. joystick, keyboard,
vision-based\...) without taking care of the basic communication.



```clearsilver

name = cob_base_drive_chain_node
desc = This node provides access to the platform control of the Care-O-Bot (steer and drive motors) to the ROS network.
sub {
  0.name = joint_command
  0.type = pr2_controllers_msgs/JointTrajectoryControllerState
  0.desc = it listenes to motor commands on this topic
}
srv {
  0.name = Init
  0.type = cob_srvs/Trigger
  0.desc = initializes the platform and executes homing procedure of motors
  1.name = Reset
  1.type = cob_srvs/Trigger
  1.desc = re-initializes the platform
  2.name = Shutdown
  2.type = cob_srvs/Trigger
  2.desc = stops motors and shuts down the platform
  3.name = GetJointState
  3.type = cob_srvs/GetJointState
  3.desc = get joint joint states
  4.name = ElmoRecorderConfig
  4.type = cob_srvs/ElmoRecorderConfig
  4.desc = configures the Elmo specific recorder (see below)
  5.name = ElmoRecorderReadout
  5.type = cob_srvs/ElmoRecorderReadout
  5.desc = reads out and stores previous recorded drive information (see below)
}
pub {
  0.name = JointState
  0.type = sensor_msgs/JointState
  0.desc = every time you request joint states via ROS service, these states are also published on this topic
  1.name = Diagnostic
  1.type = diagnostic_msgs/DiagnosticStatus
  1.desc = it publishes states and error information of the platform
}
```



## Using the Elmo Recorder

Elmo controllers (like the Harmonica drive) have the functionality to
record drive information (like position,velocity, current) at a very
high frequency into their own flash memory. Later on, the user can read
out that data to precisely analyse the data. The described tool makes it
easy for the user to use this feature. It is preconfigured to record the
values velocity, position, active current, commanded velocity.

It is implemented in `cob_base_drive_chain::CanCtrlPltfCOb3` and again
provided to the ROS network via services. To use the Elmo Recorder
without the services, you can use the interface of
`cob_base_drive_chain::CanCtrlPltfCOb3` directly as desribed below.

### ROS service interface

In order to record and extract data using cob_base_drive_chain node in
the ROS environment, the only thing you have to do is calling two
services offered by base_drive_chain_node:

-   !ElmoRecorderConfig <<SrvLink(cob_srvs/ElmoRecorderConfig)>>
    __\
    Arguments:__ int64 recordinggap: With that setting, you can
    specify the time gap between two data points. The entered number is
    multiplied with 4 \* 90µsec. Always 1024 data points are recorded in
    total, so the total recording time is RG \* 4 \* 90\*1024 µsec.
    Configuring the Recorder this way, the recording process starts
    immediately.
-   !ElmoRecorderReadout <<SrvLink(cob_srvs/ElmoRecorderReadout)>>
    __\
    Arguments:__ int64 subindex: Specify the recorded value you want
    to download and save. Predefined records are 1: Main Speed, 2: Main
    Position, 10: Active Current Command, 16: Speed Command. string
    fileprefix: path and file-prefix of log files. The record-object and
    motor Ids are automatically attached.

You always get a success code and an answer message. When requesting a
read-out, you can't relay on the success-code, as the availability of
the recorder first has to be checked.

All the operations (configuring and reading out the Recorder) are done
for all available motors at once. You will find one file for each motor
in the specified log-directory.

In the log file, the first column contains the time of the data point,
the second contains the exponential representation of the data point of
the selected record source.

### Developer interface

There are two other levels of "user"-interfaces, to keep the drive
interface-classes slight. The function
`CanCtrlPltfCOb3::ElmoRecordings` basically is just a wrapper function
for the main Elmo-Recorder interface in
`cob_canopen_motor::CanDriveHarmonica::setRecorder(int iFlag, int
iParam, std::string sParam)`. With these arguments you can control all
of the Recorders features. `iFlag` specifies the general task, you are
going to set up:

-   __`iFlag = 0`:__ Configure Elmo Recorder for new Record

iParam = iRecordingGap, which specifies every which time quantum
(4\*90usec) a new data point is recorded

-   __`iFlag = 1`:__ Query upload of previous recorded data, data
    is being proceeded after complete upload-data collection and then
    syved into a log file (named filename + Drive_ID + record_value_ID +
    ".log") iParam = recorded ID filename = path + fileprefix

```{=html}
<!-- -->
```
-   __`iFlag = 2`:__ After initiating the upload process, read the
    state of data collection and processing
-   __`iFlag = 99`:__ Cancel any ongoing Segmented SDO Data
    transfer.

Return values are 0: Everything is fine, 1: Recorder hasn't been
configured yet, 2: Data collection still in progress.

To keep all the CAN communication the process going, be sure to evaluate
the CAN-buffer continuous. Also take care of the watchdogs using the
heartbeat message.

### Implementation

The most difficult point of the Recorder read-out process is the
asynchronous and delayed collection of data. If you wanted to give all
the data back (like in a return) to the calling function, you had to
create a giant loop, that would block all the program (and therefore
also the communication facilities to the respective motor).

To avoid that effect, the user only has to start-up the read-out
process. From then, the transfer process is running autonomously,
triggered by the receive of data packets, which are led to the
appropriate functions after having been fetched from the CAN-buffer.
During such a segmented SDO transfer, the data is collected in the
`cob_canopen_motor::SDOSegmented` collection class. It also holds some
SDO-transfer-specific features like the state of the transmission. When
receiving the last segment of a transfer, the collected data is handed
to an adequate processing function. In our case, it's
`ElmoRecorder::processData()`. Finally, the collected data is saved to
a file; you also could imagine of keeping it temporarily in a variable
to give the calling function the opportunity to process the data itself.

How to read out data from the Elmo Recorder is described in
[cob_canopen_motor](cob_canopen_motor).
