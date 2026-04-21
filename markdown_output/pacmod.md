A ROS driver to communicate with and control board revisions 1 and 2 of
the
[AutonomouStuff PACMod drive-by-wire platform](https://autonomoustuff.com/product/small-ev-by-wire-kits/).

For revision 3 of the PACMod hardware, see the [pacmod3](pacmod3)
entry.\
For controlling the PACMod system (all versions) with a joystick, see
[pacmod_game_control](pacmod_game_control).

# Supported Hardware

-   Polaris GEM Series (e2/e4/e6/eLXD)
-   Polaris Ranger X900
-   International Prostar+ 122
-   Lexus RX-450h
-   More coming soon\...

# Published Topics

  -- ------------------------------------------------------------------------------- -- ----------------------------- -- --------------------------------------------------------------------------------------------------- --
     \<tablewidth=\"100%\"rowbgcolor=\"#cccccc\"width=\"260px\"\>**Message Type **      **Topic **                       **Description **                                                                                    
     can_msgs/Frame                                                                     can_rx                           All data published on this topic is intended to be sent to the PACMod system via a CAN interface.   
     pacmod_msgs/GlobalRpt                                                              parsed_tx/global_rpt             High-level data about the entire PACMod system.                                                     
     pacmod_msgs/SystemRptFloat                                                         parsed_tx/accel_rpt              Status and parsed values \[pct\] of the throttle subsystem.                                         
     pacmod_msgs/SystemRptFloat                                                         parsed_tx/brake_rpt              Status and parsed values \[pct\] of the steering susbsystem.                                        
     pacmod_msgs/SystemRptInt                                                           parsed_tx/turn_rpt               Status and parsed values \[enum\] of the turn signal subsystem.                                     
     pacmod_msgs/SystemRptInt                                                           parsed_tx/shift_rpt              Status and parsed values \[enum\] of the gear/transmission subsystem.                               
     pacmod_msgs/SystemRptFloat                                                         parsed_tx/steer_rpt              Status and parsed values \[rad\] of the steering susbsystem.                                        
     pacmod_msgs/VehicleSpeedRpt                                                        parsed_tx/vehicle_speed_rpt                                                                                                          
  -- ------------------------------------------------------------------------------- -- ----------------------------- -- --------------------------------------------------------------------------------------------------- --

The vehicle\'s current speed \[mph\], the validity of the speed message
\[bool\], and the raw CAN message from the vehicle CAN.\|\|

  -- ------------------ -- --------------------- -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     std_msgs/Float64      as_tx/vehicle_speed      The vehicle\'s current speed \[m/s\].                                                                                                                                       
     std_msgs/Bool         as_tx/enable             The current status of the PACMod\'s control of the vehicle. If the PACMod is enabled, this value will be true. If it is disabled or overridden, this value will be false.   
  -- ------------------ -- --------------------- -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

# Conditionally Published Topics (Dependent Upon Vehicle Type)

  -- ------------------------------------------------------------------------------- -- ------------------------------------ -- --------------------------------------------------------------------------------------------------------------------------------- --
     \<tablewidth=\"100%\"rowbgcolor=\"#cccccc\"width=\"260px\"\>**Message Type **      **Topic **                              **Description **                                                                                                                  
     pacmod_msgs/MotorRpt1                                                              parsed_tx/brake_rpt_detail_1            Motor detail report values for the brake motor (current \[A\] and position \[rad\]).                                              
     pacmod_msgs/MotorRpt2                                                              parsed_tx/brake_rpt_detail_2            Motor detail report values for the brake motor (encoder temp \[C\], motor temp \[C\], and rotation velocity \[rad/s\]).           
     pacmod_msgs/MotorRpt3                                                              parsed_tx/brake_rpt_detail_3            Motor detail report values for the brake motor (torque output and input \[Nm\]).                                                  
     pacmod_msgs/SystemRptInt                                                           parsed_tx/headlight_rpt                 Status and parsed values \[enum\] of the headlight subsystem.                                                                     
     pacmod_msgs/SystemRptInt                                                           parsed_tx/horn_rpt                      Status and parsed values \[enum\] of the horn subsystem.                                                                          
     pacmod_msgs/LatLonHeadingRpt                                                       parsed_tx/lat_lon_heading_rpt           The current latitude, longitude, and heading provided by the vehicle\'s internal GPS.                                             
     pacmod_msgs/ParkingBrakeStatusRpt                                                  parsed_tx/parking_brake_status_rpt      Status on the current state of the parking brake (engaged/disengaged).                                                            
     pacmod_msgs/SteeringPIDRpt1                                                        parsed_tx/steer_pid_rpt_1               Current dt, Kp, Ki, and Kd values of the torque-based steering control PID loop.                                                  
     pacmod_msgs/SteeringPIDRpt2                                                        parsed_tx/steer_pid_rpt_2               Current P, I, and D terms and the sum of P, I, and D terms of the torque-based steering control PID loop.                         
     pacmod_msgs/SteeringPIDRpt3                                                        parsed_tx/steer_pid_rpt_3               The new torque, torque feedback, calculated angular position, and error values from the torque-based steering control PID loop.   
     pacmod_msgs/MotorRpt1                                                              parsed_tx/steer_rpt_detail_1            Motor detail report values for the steering motor (current \[A\] and position \[rad\]).                                           
     pacmod_msgs/MotorRpt2                                                              parsed_tx/steer_rpt_detail_2            Motor detail report values for the steering motor (encoder temp \[C\], motor temp \[C\], and rotation velocity \[rad/s\]).        
     pacmod_msgs/MotorRpt3                                                              parsed_tx/steer_rpt_detail_3            Motor detail report values for the steering motor (torque output and input \[Nm\]).                                               
     pacmod_msgs/WheelSpeedRpt                                                          parsed_tx/wheel_speed_rpt               Speeds of individual wheels \[m/s\].                                                                                              
     pacmod_msgs/SystemRptInt                                                           parsed_tx/wiper_rpt                     Status and parsed values \[enum\] of the windshield wiper subsystem.                                                              
     pacmod_msgs/YawRateRpt                                                             parsed_tx/yaw_rate_rpt                  The yaw rate reported by the vehicle\'s internal IMU.                                                                             
  -- ------------------------------------------------------------------------------- -- ------------------------------------ -- --------------------------------------------------------------------------------------------------------------------------------- --

# Subscribed Topics

  -- ------------------------------------------------------------------------------ -- ----------------- -- ------------------------------------------------------------------------------------------------------------------------- --
     \<tablewidth=\"100%\"rowbgcolor=\"#cccccc\"width=\"260px\"\>**Message Type**      **Topic **           **Description **                                                                                                          
     can_msgs/Frame                                                                    can_tx               All data published to this topic will be parsed by the PACMod driver. This should be connected to a CAN interface.        
     pacmod_msgs/PacmodCmd                                                             as_rx/accel_cmd      Commands the throttle subsystem to seek a specific pedal position \[pct - 0.0 to 1.0\].                                   
     pacmod_msgs/PacmodCmd                                                             as_rx/brake_cmd      Commands the brake subsystem to seek a specific pedal position \[pct - 0.0 to 1.0\].                                      
     pacmod_msgs/PacmodCmd                                                             as_rx/shift_cmd      Commands the gear/transmission subsystem to shift to a different gear \[enum\].                                           
     pacmod_msgs/PositionWithSpeed                                                     as_rx/steer_cmd      Commands the steering subsystem to seek a specific steering wheel angle \[rad\] at a given rotation velocity \[rad/s\].   
     pacmod_msgs/PacmodCmd                                                             as_rx/turn_cmd       Commands the turn signal subsystem to transition to a given state \[enum\].                                               
     std_msgs/Bool                                                                     as_rx/enable         Enables \[true\] or disables \[false\] PACMod\'s control of the vehicle.                                                  
  -- ------------------------------------------------------------------------------ -- ----------------- -- ------------------------------------------------------------------------------------------------------------------------- --

# Parameters

\`vehicle_type\`\
A string value indicating the type of vehicle to which the PACMod is
connected. Valid values are:

-   POLARIS_GEM
-   POLARIS_RANGER
-   INTERNATIONAL_PROSTAR_122
-   LEXUS_RX_450H.
