## Overview

This package provides a ros interface to communicate with the High Level
Processor (HLP) of the !AscTec !AutoPilot. Therefore, firmware for the
HLP is needed which is provided in the
[asctec_hl_firmware](asctec_hl_firmware) package. It does not work with
the firmware shipped with the HLP!

## Safety Instructions

We put our best effort in making this package working safely. However,
usage is completely on your own risk. We disclaim any liability for
injuries, damages of the helicopter or to objects. It is your
responsibility to ensure a safe operation environment! Always comply
with Ascending Technologies\' safety guidelines. Additionally:

-   A safety pilot must always be present and he must have the training
    and ability to fly the UAV manually in any situation.
-   Do not fly over people or close to people. Spectators always stand
    behind the safety pilot.
-   Always wear proper protection gear (gloves, safety goggles). The
    safety pilot as well as spectators.
-   In case of any unexpected behavour, the safety pilot should switch
    \'\'\'both\'\'\' the serial interface switch to \"off\" and the
    flight mode switch to \"acc\" (both switches point away from the
    pilot then).
-   When having a new or changed setup (new/other controller, different
    parameters etc), carefully check the expected outputs
    \'\'\'before\'\'\' flying.

## Setup

### Serial Connection to the Highlevel Processor

Using a wired connection is recommended, e.g. to the Ascending
Technologies
[AtomBoard](http://wiki.asctec.de/display/AR/AscTec+Atomboard). The
cable supplied with the !AtomBoard can be used. Connect to the serial
port 0 of the Highlevel Processor (\"HL serial 0\") as shown in the
!AscTec
[AutoPilot documentation](http://www.asctec.de/assets/Downloads/Manuals/AscTec-Autopilot-Manual-v10.pdf)
in chapter 4.1. In this case, set \`serial_port\` to the correct port,
and leave \`serial_port_rx\` and \`serial_port_tx\` empty.

If you plan to use a wireless serial link, it might be useful to use a
dedicated link for each rx and tx for higher bandwidth. In that case,
set \`serial_port_rx\` and \`serial_port_tx\` accordingly and leave
\`serial_port\` empty.

### Baudrate

The baudrate at which the \`hl_node\` communicates with the HLP can be
set with the \`baudrate\` parameter. If it doesn\'t match a supported
standard baudrate, the closest standard baudrate is chosen. The HLP
tries to detect the baudrate automatically at startup or if there
wasn\'t any communication with the hl_node for longer than 10 seconds.
\`hl_node\` sets up its serial port(s) with the desired baudrate and
sends a packet (\'a\') which the HLP uses to detect the correct
baudrate. In order for this to work, always switch on the HLP first,
then start \`hl_node\`. In case you need to restart \`hl_node\` with a
different baudrate, you have to wait 10 s until the HLP accepts new
baudrate configure packets. Restarting with the same baudrate works
immediately. Tested baudrates are: 57600, 115200, 230400, 460800,
921600.

### Configurable Packet Rates

Packet rates of certain packets can be configured with the
\`packet_rate\_\*\` parameters. No polling is done - instead a
configuration packet is sent to the HLP which will send the packets in
the desired rate accordingly. Note that no checking is done if the
packet rates exceed the available bandwidth, so check the correct rate
with ```
rostopic hz <topic> -w <expected rate>
```

## Modes of Operation

In all operation modes, you can enable/disable control output to the LLP
by setting the \`/enable\_\*\` parameters accordingly. This is helpful,
e.g. to debug a controller on a single axis first. Directions and
orientations follow the
[ROS coordinate frame conventions](geometry/CoordinateFrameConventions).
As with the direct interface to the LLP, it only accepts commands when
the serial enable switch is on. In failure, flip off this switch and put
the flightmode switch to \"acc\". There are three modes you can operate
the helicopter which you can select with the \`/position_control\`
parameter:

### Direct Acceleration Commands

Set \`/position_control\` to \"off\". This mode just forwards roll,
pitch, yaw (angular velocity) and thrust commands to the LLP. This is
similar to directly send commands to the LLP\'s serial interface. Set
the values in \<\<MsgLink(asctec_hl_comm/mav_ctrl)\>\> in rad for roll
and pitch, in rad/s for yaw and 0.0 \... 1.0 for thrust and set
\<\<MsgLink(asctec_hl_comm/mav_ctrl)\>\>/type to \"acceleration\". For
the scaling to work correctly, you need to set \`/k_stick\` and
\`/k_stick_yaw\` to the values you can read out from the LLP with the
!AscTec control software (default 25, 120). Messages have to arrive at
least at 10 Hz, otherwise nothing will be forwarded to the LLP.
\'\'\'Note:\'\'\' yaw rates are limited to +- 85% so that the motors
cannot be switched on/off accidentally in case of bad commands (motors
idle, full yaw).

### GPS Based Velocity Control

Set \`/position_control\` to \"GPS\" and set
\<\<MsgLink(asctec_hl_comm/mav_ctrl)\>\>/type to \"velocity\" in your
messages. Commands are also forwarded to the LLP, but the GPS bit is set
additionally. The values in \<\<MsgLink(asctec_hl_comm/mav_ctrl)\>\>
correnspond to velocities in boady coordinates in m/s and rad/s
respectively. For the scaling to work correctly, you need to set
\`/max_velocity\_\*\` according to the maximum \"stick-GPS\" velocites
which you can read out from the LLP with the !AscTec control software.
Defaults are 5 m/s for x/y, and 2 m/s for z. Messages have to arrive at
least at 10 Hz, otherwise nothing will be forwarded to the LLP.
\'\'\'Note:\'\'\' yaw rates are limited to +- 85% so that the motors
cannot be switched on/off accidentally in case of bad commands (full
descend rate, full yaw)

Sending GPS waypoints over the HLP to the LLP is currently not
implemented as it is not available on the interface between HLP and LLP.

### Position Control on the HLP

This is the most interesting part and main motivation for this project.
It is designed for position control based on position measurements from
e.g. onboard visual SLAM with typically slow update rates. To deal with
those delays, datafusion with IMU and position control is performed on
the HLP at a rate of 1 kHz. Details on how the controller and datafusion
work can be found in
[Onboard IMU and Monocular Vision Based Control for MAVs in Unknown In- and Outdoor Environments](http://publications.asl.ethz.ch/files/achtelik11onboard.pdf).
To work with this mode, please go carefully through this
[tutorial](asctec_hl_interface/Tutorials/hlp position control).

## Nodes

```clearsilver
node.0{
  name = hl_interface
  desc = interface to the high level processor (HLP) of the !AscTec !AutoPilot
  sub {
    0.name = fcu/control
    0.type = asctec_hl_comm/mav_ctrl
    0.desc = listens to control commands on this topic
    1.name = fcu/pose
    1.type = geometry_msgs/PoseWithCovarianceStamped
    1.desc = listens on this topic for pose updates
    2.name = fcu/state
    2.type = asctec_hl_comm/mav_state
    2.desc = listens on this topic for state updates. This bypasses the state estimation on the HLP
    3.name = fcu/ekf_state_in
    3.type = sensor_fusion_comm/ExtEkf
    3.desc = Listens for updates from [[ethzasl_sensor_fusion|ethzasl_sensor_fusion]]
  }
  pub {
    0.name = fcu/imu_custom
    0.type = asctec_hl_comm/mav_imu
    0.desc = custom imu package without covariance, with height and differential height
    1.name = fcu/imu
    1.type = sensor_msgs/Imu
    1.desc = Imu sensor data
    2.name = fcu/gps
    2.type = sensor_msgs/NavSatFix
    2.desc = .
    3.name = fcu/rcdata
    3.type = asctec_hl_comm/mav_rcdata
    3.desc = values of the RC channels receiver by the !AutoPilot
    4.name = fcu/status
    4.type = asctec_hl_comm/mav_status
    4.desc = status of the helicopter
    5.name = fcu/debug
    5.type = asctec_hl_comm/DoubleArrayStamped
    5.desc = debug values from the SSDK
    6.name = fcu/current_pose
    6.type = geometry_msgs/PoseStamped
    6.desc = publishes the pose that is currently used for position control on the HLP
    8.name = fcu/ekf_state_out
    8.type = sensor_fusion_comm/ExtEkf
    8.desc = publishes the current prediction for [[ethzasl_sensor_fusion|ethzasl_sensor_fusion]]
  }
  req_tf {
    0.from = world
    0.to   = mav
    0.desc = tf transform from world to helicopter. Used as position update for state estimation on the HLP. Can be changed with `~ssdk/tf_ref_frame_id` and `~ssdk/tf_tracked_frame_id`.
  }
  srv {
    0.name = fcu/motor_control
    0.type = asctec_hl_comm/mav_ctrl_motors
    0.desc = service to switch the motors on/off. '''Use this carefully, it also works during flight!'''.
  }
  param {
    group.0{
      name = Static parameters
      desc = parameters that are statically set
      1.name = ~serial_port_rx
      1.type = string
      1.desc = serial port for rx
      1.default = 
      2.name = ~serial_port_tx
      2.type = string
      2.desc = serial port for tx
      2.default = 
      3.name = ~serial_port
      3.type = string
      3.desc = serial port used for rx and tx
      3.default = /dev/ttyUSB0
      4.name = ~baudrate
      4.type = int
      4.desc = baudrate for the serial port(s)
      4.default = 57600
      5.name = ~frame_id
      5.type = string
      5.desc = frame id 
      5.default = fcu
      6.name = ~k_stick
      6.type = int
      6.desc = gain from !AutoPilot values to 1/1000 degree for the input from the pitch and roll "stick"
      6.default = 25
      7.name = ~k_stick_yaw
      7.type = int
      7.desc = gain from !AutoPilot values to 1/1000 degree for the input from the yaw "stick"
      7.default = 120
      8.name = ~stddev_angular_velocity
      8.type = double
      8.desc = standard deviation for angular velocity, default from experiments
      8.default = 0.013
      9.name = ~stddev_linear_acceleration
      9.type = double
      9.desc = standard deviation for linear acceleration, default from experiments
      9.default = 0.083 
    }
    group.1 {
      name=Dynamically Reconfigurable Parameters Part I (fcu)
      desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
      0.name= ~packet_rate_imu
      0.default= 50.0
      0.type= double
      0.desc=configures packet rate [Hz] of imu packet. Range: 0.0 to 1000.0
      1.name= ~packet_rate_rc
      1.default= 10.0
      1.type= double
      1.desc=configures packet rate [Hz] of rc packet. Range: 0.0 to 1000.0
      2.name= ~packet_rate_gps
      2.default= 5.0
      2.type= double
      2.desc=configures packet rate [Hz] of gps packet. Range: 0.0 to 1000.0
      3.name= ~packet_rate_ssdk_debug
      3.default= 5.0
      3.type= double
      3.desc=configures packet rate [Hz] of ssdk debug packet. Range: 0.0 to 1000.0
      4.name= ~packet_rate_ekf_state
      4.default= 0.0
      4.type= double
      4.desc=configures packet rate [Hz] of ekf state packet. Range: 0.0 to 1000.0
      5.name= ~enable_x
      5.default= True
      5.type= bool
      5.desc=enables x-control.  
      6.name= ~enable_y
      6.default= True
      6.type= bool
      6.desc=enables y-control.  
      7.name= ~enable_z
      7.default= True
      7.type= bool
      7.desc=enables z-control.  
      8.name= ~enable_yaw
      8.default= True
      8.type= bool
      8.desc=enables yaw-control.  
      9.name= ~position_control
      9.default= off
      9.type= str
      9.desc=Enables position control either on the HLP or GPS based position control on the LLP. Possible values are: POSCTRL_OFF (off): position control off, POSCTRL_HIGHLEVEL (!HighLevel): position control runs on the HLP., POSCTRL_GPS (GPS): gps position control on the LLP.
      10.name= ~state_estimation
      10.default= off
      10.type= str
      10.desc=Determines where state estimation is performed. Possible values are: STATE_EST_OFF (off): state estimation off, STATE_EST_HIGHLEVEL_SSDK (!HighLevel_SSDK): state estimation runs on the HLP within the SSDK., STATE_EST_HIGHLEVEL_EKF (!HighLevel_EKF): state estimation runs on the HLP within an EKF., STATE_EST_EXTERN (Extern): state estimation is performed externally.
      11.name= ~max_velocity_xy
      11.default= 0.5
      11.type= double
      11.desc=maximum velocity in x/y [m/s]. Range: 0.0 to 10.0
      12.name= ~max_velocity_z
      12.default= 0.5
      12.type= double
      12.desc=maximum velocity in z [m/s]. Range: 0.0 to 2.0
      13.name= ~max_velocity_yaw
      13.default= 0.1
      13.type= double
      13.desc=maximum velocity yaw [rad/s]. Range: 0.0 to 1.57
      14.name= ~min_pos_x
      14.default= -1000.0
      14.type= double
      14.desc=lower bound for position x [m]. Range: -1000.0 to 1000.0
      15.name= ~min_pos_y
      15.default= -1000.0
      15.type= double
      15.desc=lower bound for position y [m]. Range: -1000.0 to 1000.0
      16.name= ~min_pos_z
      16.default= -1000.0
      16.type= double
      16.desc=lower bound for position z [m]. Range: -1000.0 to 1000.0
      17.name= ~max_pos_x
      17.default= 1000.0
      17.type= double
      17.desc=upper bound for position x [m]. Range: -1000.0 to 1000.0
      18.name= ~max_pos_y
      18.default= 1000.0
      18.type= double
      18.desc=upper bound for position y [m]. Range: -1000.0 to 1000.0
      19.name= ~max_pos_z
      19.default= 1000.0
      19.type= double
      19.desc=upper bound for position z [m]. Range: -1000.0 to 1000.0
    }
    group.2 {
      name=Dynamically Reconfigurable Parameters Part II (fcu/ssdk)
      desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
      0.name= ~ssdk/listen_on_tf
      0.default= True
      0.type= bool
      0.desc=Enables listening on tf transforms for position updates for the state estimation on the HLP. 
      1.name= ~ssdk/tf_ref_frame_id
      1.default= world
      1.type= str
      1.desc=tf reference frame. 
      2.name= ~ssdk/tf_tracked_frame_id
      2.default= pelican
      2.type= str
      2.desc=tf frame of the helicopter. 
      3.name= ~ssdk/send
      3.default= False
      3.type= bool
      3.desc=used to send all parameters at once. 
      4.name= ~ssdk/omega_0_xy
      4.default= 2.5
      4.type= double
      4.desc=natural frequency of the position controller's reference model for x and y axis. Range: -100.0 to 100.0
      5.name= ~ssdk/omega_0_z
      5.default= 8.0
      5.type= double
      5.desc=natural frequency of the position controller's reference model for the z axis. Range: -100.0 to 100.0
      6.name= ~ssdk/zeta_xy
      6.default= 1.0
      6.type= double
      6.desc=damping of the position controller's reference model for x and y axis. Range: -100.0 to 100.0
      7.name= ~ssdk/zeta_z
      7.default= 1.0
      7.type= double
      7.desc=damping of the position controller's reference model for the z axis. Range: -100.0 to 100.0
      8.name= ~ssdk/p<channel>
      8.default= 0.0
      8.type= double
      8.desc= replace <channel> by 1-50. Parameter channels used to configure the SSDK running on the HLP. See detailed description for assignments and values. Range: -100.0 to 100.0
    }
  }
}
node.1{
  name = waypoint_server
  desc = provides an action server interface to send the helicopter to waypoints
  sub{
    0.name = fcu/current_pose
    0.type = asctec_hl_comm/mav_ctrl
    0.desc = listens to the pose that the helicopter's position controller is currently using. Needed to determine if a waypoint is reached and for feedback messages.  
  }
  goal{
    0.name = fcu/waypoint/goal
    0.type = asctec_hl_comm/WaypointActionGoal
    0.desc = accepts a new waypoint.
  }
  feedback{
    0.name = fcu/waypoint/feedback
    0.type = asctec_hl_comm/WaypointActionFeedback
    0.desc = current position of the helicopter and distance to waypoint.
  }
  result{
    0.name = fcu/waypoint/result
    0.type = asctec_hl_comm/WaypointActionResult
    0.desc = finally reached waypoint, success/failure. 
  }
}
node.2{
  name = waypoint_client
  desc = sample waypoint client to send waypoints from the command line
  goal{
    0.name = fcu/waypoint/goal
    0.type = asctec_hl_comm/WaypointActionGoal
    0.desc = sends a new waypoint.
  }
  feedback{
    0.name = fcu/waypoint/feedback
    0.type = asctec_hl_comm/WaypointActionFeedback
    0.desc = listens to current position of the helicopter and distance to waypoint.
  }
  result{
    0.name = fcu/waypoint/result
    0.type = asctec_hl_comm/WaypointActionResult
    0.desc = listens to finally reached waypoint, success/failure. 
  }
}
```

## Scripts

All plot\_\* scripts plot IMU data from the LLP and debug data from the
SSDK running on the HLP. For the SSDK, data is displayed in the North
East Down (NED) convention, i.e. data is rotated 180° around the x-axis.
y(NED) = -y(ENU), z(NED) = -z(ENU) (height is negative!) and angles
likewise according to the right hand rule. Usage:
```
rosrun asctec_hl_interface plot_position_input [namespace]
#e.g.
rosrun asctec_hl_interface plot_position_input pelican
```

```clearsilver
node.0{
  name = plot_acceleration
  desc = plots acceleration sensor values in body coordinates in m/s^2.
}
node.1{
  name = plot_angular_velocity
  desc = plots angular velocity in body coordinates in rad/s.
}
node.2{
  name = plot_orientation
  desc = plots the orientation quaternion (w, x, y, z).
}
node.3{
  name = plot_cmd
  desc = plots the commands that were sent to the HLP.
}
node.4{
  name = plot_ctrl_output
  desc = plots control outputs that are send from the HLP to the LLP. NED convention!
}
node.5{
  name = plot_filter_bias
  desc = plots the estimated acceleration sensor bias in body coordinates [m/s^2]. NED convention!
}
node.6{
  name = plot_filter_velocity
  desc = plots the estimated velocity in world coordinates [m/s]. NED convention!
}
node.7{
  name = plot_filter_position
  desc = plots the estimated position in world coordinates [m]. This should look similar to the results from plot_position_input, but smoother. NED convention!
}
node.8{
  name = plot_position_input
  desc = plots the position that is sent to the HLP to perform a position update of the filter. NED convention!
}
```
