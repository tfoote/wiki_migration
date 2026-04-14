An open-source ROS driver for interacting with the
[AutonomouStuff PACMod drive-by-wire platform](https://autonomoustuff.com/product/small-ev-by-wire-kits/)
(v3 and above).

For versions 1 and 2 of the PACMod hardware, see the [pacmod](pacmod)
entry.\
For controlling the PACMod system (all versions) with a joystick, see
[pacmod_game_control](pacmod_game_control).

# Supported Hardware

-   Lexus RX-450h
-   Polaris GEM (MY 2016+)
-   Polaris Ranger (MY 2016+)
-   International ProStar 122+
-   Freightliner Cascadia DD13 DayCab/Sleeper/Extended-Sleeper
-   Ford Ranger 2019+
-   Toyota Minivan 2019+
-   Tractor 2017+
-   Kenworth T680 Semi 2017+
-   More coming soon\...

For [DBC version](https://github.com/astuff/pacmod_dbc) compatibility
refer to the platform user manual. Please refer to
[PACMod3 readme file](https://github.com/astuff/pacmod3/blob/master/README.md)
for compatible ROS driver branch. Following topics are based on DBC
version 3.4.0

# Published Topics

  -- ----------------------------------------------------------------------------------------------------------------- -- ----------------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     \<tablewidth=\"100%\"rowbgcolor=\"#cccccc\"width=\"260px\"\>\'\'\'Message Type \'\'\'                                \'\'\'Topic \'\'\'               \'\'\'Description \'\'\'                                                                                                                                                                           
     [can_msgs/Frame](http://docs.ros.org/api/can_msgs/html/msg/Frame.html)                                               can_rx                           All data published on this topic are raw CAN messages intended to be sent to the PACMod. This topic should be subscribed to by a CAN interface node (like kvaser_interface or socketcan_bridge).   
     [pacmod_msgs/GlobalRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/GlobalRpt.html)                      parsed_tx/global_rpt             High-level data about the entire PACMod system.                                                                                                                                                    
     [pacmod_msgs/SystemRptFloat](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemRptFloat.html)            parsed_tx/accel_rpt              Status and parsed values \[pct\] of the throttle subsystem.                                                                                                                                        
     [pacmod_msgs/SystemRptFloat](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemRptFloat.html)            parsed_tx/brake_rpt              Status and parsed values \[pct\] of the braking subsystem.                                                                                                                                         
     [pacmod_msgs/SystemRptInt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemRptInt.html)                parsed_tx/turn_rpt               Status and parsed values \[enum\] of the turn signal subsystem.                                                                                                                                    
     [pacmod_msgs/SystemRptInt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemRptInt.html)                parsed_tx/shift_rpt              Status and parsed values \[enum\] of the gear/transmission subsystem.                                                                                                                              
     [pacmod_msgs/SystemRptFloat](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemRptFloat.html)            parsed_tx/steer_rpt              Status and parsed values \[rad\] of the steering susbsystem.                                                                                                                                       
     [pacmod_msgs/AccelAuxRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/AccelAuxRpt.html)                  parsed_tx/accel_aux_rpt          Additional information about the vehicle\'s accelerator system. Includes \_is_valid flags for each field to indicate validity.                                                                     
     [pacmod_msgs/BrakeAuxRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/BrakeAuxRpt.html)                  parsed_tx/brake_aux_rpt          Additional information about the vehicle\'s braking system. Includes \_is_valid flags for each field to indicate validity.                                                                         
     [pacmod_msgs/ShiftAuxRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/ShiftAuxRpt.html)                  parsed_tx/shift_aux_rpt          Additional information about the vehicle\'s shifting system. Includes \_is_valid flags for each field to indicate validity.                                                                        
     [pacmod_msgs/SteerAuxRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SteerAuxRpt.html)                  parsed_tx/steer_aux_rpt          Additional information about the vehicle\'s steering system. Includes \_is_valid flags for each field to indicate validity.                                                                        
     [pacmod_msgs/TurnAuxRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/TurnAuxRpt.html)                    parsed_tx/turn_aux_rpt           Additional information about the vehicle\'s turn signal system. Includes \_is_valid flags for each field to indicate validity.                                                                     
     [pacmod_msgs/VehicleSpeedRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/VehicleSpeedRpt.html)          parsed_tx/vehicle_speed_rpt      The vehicle\'s current speed \[mph\], the validity of the speed message \[bool\], and the raw CAN message from the vehicle CAN.                                                                    
     [pacmod_msgs/VinRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/VinRpt.html)                            parsed_tx/vin_rpt                The configured vehicle\'s VIN, make, model, manufacturer, and model year.                                                                                                                          
     [pacmod_msgs/AllSystemStatuses](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/AllSystemStatuses.html)      as_tx/all_system_statuses        The current enable, fault, and override active statuses of all vehicle systems for this vehicle.                                                                                                   
     [std_msgs/Bool](http://docs.ros.org/en/melodic/api/std_msgs/html/msg/Bool.html)                                      as_tx/enabled                    The current status of the PACMod\'s control of the vehicle. If the PACMod is enabled, this value will be true. If it is disabled or overridden, this value will be false.                          
     [std_msgs/Float64](http://docs.ros.org/en/melodic/api/std_msgs/html/msg/Float64.html)                                as_tx/vehicle_speed              The vehicle\'s current speed \[m/s\].                                                                                                                                                              
  -- ----------------------------------------------------------------------------------------------------------------- -- ----------------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

# Conditionally Published Topics (Dependent Upon Vehicle Type)

  -- ----------------------------------------------------------------------------------------------------------------- -- -------------------------------------- -- --------------------------------------------------------------------------------------------------------------------------------- --
     \<tablewidth=\"100%\"rowbgcolor=\"#cccccc\"width=\"260px\"\>\'\'\'Message Type \'\'\'                                \'\'\'Topic \'\'\'                        \'\'\'Description \'\'\'                                                                                                          
     [pacmod_msgs/SystemRptInt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemRptInt.html)                parsed_tx/cruise_control_buttons_rpt      Status and parsed values \[enum\] of the cruise control buttons subsystem.                                                        
     [pacmod_msgs/SystemRptInt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemRptInt.html)                parsed_tx/dash_controls_left_rpt          Status and parsed values \[enum\] of the dash controls (left) subsystem.                                                          
     [pacmod_msgs/SystemRptInt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemRptInt.html)                parsed_tx/dash_controls_right_rpt         Status and parsed values \[enum\] of the dash controls (right) subsystem.                                                         
     [pacmod_msgs/SystemRptInt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemRptInt.html)                parsed_tx/headlight_rpt                   Status and parsed values \[enum\] of the headlight subsystem.                                                                     
     [pacmod_msgs/SystemRptBool](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemRptBool.html)              parsed_tx/horn_rpt                        Status and parsed values \[bool\] of the horn subsystem.                                                                          
     [pacmod_msgs/SystemRptInt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemRptInt.html)                parsed_tx/media_controls_rpt              Status and parsed values \[enum\] of the media controls subsystem.                                                                
     [pacmod_msgs/SystemRptBool](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemRptBool.html)              parsed_tx/parking_brake_rpt               Status and parsed values \[bool\] of the parking brake subsystem.                                                                 
     [pacmod_msgs/SystemRptInt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemRptInt.html)                parsed_tx/wiper_rpt                       Status and parsed values \[enum\] of the wiper subsystem.                                                                         
     [pacmod_msgs/HeadlightAuxRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/HeadlightAuxRpt.html)          parsed_tx/headlight_aux_rpt               Additional information about the vehicle\'s headlight subsystem. Includes \_is_valid flags for each field to indicate validity.   
     [pacmod_msgs/WiperAuxRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/WiperAuxRpt.html)                  parsed_tx/wiper_aux_rpt                   Additional information about the vehicle\'s wiper subsystem. Includes \_is_valid flags for each field to indicate validity.       
     [pacmod_msgs/MotorRpt1](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/MotorRpt1.html)                      parsed_tx/brake_rpt_detail_1              Motor detail report values for the brake motor (current \[A\] and position \[rad\]).                                              
     [pacmod_msgs/MotorRpt2](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/MotorRpt2.html)                      parsed_tx/brake_rpt_detail_2              Motor detail report values for the brake motor (encoder temp \[C\], motor temp \[C\], and rotation velocity \[rad/s\]).           
     [pacmod_msgs/MotorRpt3](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/MotorRpt3.html)                      parsed_tx/brake_rpt_detail_3              Motor detail report values for the brake motor (torque output and input \[Nm\]).                                                  
     [pacmod_msgs/DateTimeRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/DateTimeRpt.html)                  parsed_tx/date_time_rpt                   The vehicle-provided date and time (usually from GPS).                                                                            
     [pacmod_msgs/DoorRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/DoorRpt.html)                          parsed_tx/door_rpt                        Current status of all doors on the vehicle (open or closed) and \_is_valid flags for each.                                        
     [pacmod_msgs/InteriorLightsRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/InteriorLightsRpt.html)      parsed_tx/interior_lights_rpt             The on/off and dim level status of vehicle interior lights and \_is_valid flags for each.                                         
     [pacmod_msgs/LatLonHeadingRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/LatLonHeadingRpt.html)        parsed_tx/lat_lon_heading_rpt             The vehicle-provided latitude, longitude, and heading                                                                             
     [pacmod_msgs/OccupancyRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/OccupancyRpt.html)                parsed_tx/occupancy_rpt                   The occupancy and seat belt status of the available passenger locations in the car and \_is_valid flags for each.                 
     [pacmod_msgs/RearLightsRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/RearLightsRpt.html)              parsed_tx/rear_lights_rpt                 The on/off status of the brake and reverse lights and \_is_valid flags for each.                                                  
     [pacmod_msgs/SteeringPIDRpt1](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SteeringPIDRpt1.html)          parsed_tx/steer_pid_rpt_1                 Current dt, Kp, Ki, and Kd values of the torque-based steering control PID loop.                                                  
     [pacmod_msgs/SteeringPIDRpt2](http://docs.ros.org/api/pacmod_msgs/html/msg/SteeringPIDRpt2.html)                     parsed_tx/steer_pid_rpt_2                 Current P, I, and D terms and the sum of P, I, and D terms of the torque-based steering control PID loop.                         
     [pacmod_msgs/SteeringPIDRpt3](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SteeringPIDRpt3.html)          parsed_tx/steer_pid_rpt_3                 The new torque, torque feedback, calculated angular position, and error values from the torque-based steering control PID loop.   
     [pacmod_msgs/SteeringPIDRpt4](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SteeringPIDRpt4.html)          parsed_tx/steer_pid_rpt_4                 The angular velocity and angular acceleration from the torque-based steering control PID loop.                                    
     [pacmod_msgs/MotorRpt1](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/MotorRpt1.html)                      parsed_tx/steer_rpt_detail_1              Motor detail report values for the steering motor (current \[A\] and position \[rad\]).                                           
     [pacmod_msgs/MotorRpt2](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/MotorRpt2.html)                      parsed_tx/steer_rpt_detail_2              Motor detail report values for the steering motor (encoder temp \[C\], motor temp \[C\], and rotation velocity \[rad/s\]).        
     [pacmod_msgs/MotorRpt3](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/MotorRpt3.html)                      parsed_tx/steer_rpt_detail_3              Motor detail report values for the steering motor (torque output and input \[Nm\]).                                               
     [pacmod_msgs/WheelSpeedRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/WheelSpeedRpt.html)              parsed_tx/wheel_speed_rpt                 Speeds of individual wheels \[m/s\].                                                                                              
     [pacmod_msgs/YawRateRpt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/YawRateRpt.html)                    parsed_tx/yaw_rate_rpt                    The yaw rate reported by the vehicle\'s internal IMU.                                                                             
  -- ----------------------------------------------------------------------------------------------------------------- -- -------------------------------------- -- --------------------------------------------------------------------------------------------------------------------------------- --

# Subscribed Topics

  -- ----------------------------------------------------------------------------------------------------------- -- -------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     \<tablewidth=\"100%\"rowbgcolor=\"#cccccc\"width=\"260px\"\>\'\'\'Message Type\'\'\'                           \'\'\'Topic \'\'\'      \'\'\'Description \'\'\'                                                                                                                                                   
     [can_msgs/Frame](http://docs.ros.org/en/melodic/api/can_msgs/html/msg/Frame.html)                              can_tx                  All data published on this topic are parsed by the PACMod driver. This topic should be published to by a CAN interface node (like kvaser_interface or socketcan_bridge).   
     [pacmod_msgs/SystemCmdFloat](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemCmdFloat.html)      as_rx/accel_cmd         Commands the throttle subsystem to seek a specific pedal position \[pct - 0.0 to 1.0\].                                                                                    
     [pacmod_msgs/SystemCmdFloat](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemCmdFloat.html)      as_rx/brake_cmd         Commands the brake subsystem to seek a specific pedal position \[pct - 0.0 to 1.0\].                                                                                       
     [pacmod_msgs/SystemCmdInt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemCmdInt.html)          as_rx/shift_cmd         Commands the gear/transmission subsystem to shift to a different gear \[enum\].                                                                                            
     [pacmod_msgs/SteerSystemCmd](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SteerSystemCmd.html)      as_rx/steer_cmd         Commands the steering subsystem to seek a specific steering wheel angle \[rad\] at a given rotation velocity \[rad/s\].                                                    
     [pacmod_msgs/SystemCmdInt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemCmdInt.html)          as_rx/turn_cmd          Commands the turn signal subsystem to transition to a given state \[enum\].                                                                                                
  -- ----------------------------------------------------------------------------------------------------------- -- -------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

# Conditionally Subscribed Topics (Dependent Upon Vehicle Type)

  -- --------------------------------------------------------------------------------------------------------- -- ------------------------- -- ------------------------------------------------------------------------------------------- --
     \<tablewidth=\"100%\"rowbgcolor=\"#cccccc\"width=\"260px\"\>\'\'\'Message Type\'\'\'                         \'\'\'Topic \'\'\'           \'\'\'Description \'\'\'                                                                    
     [pacmod_msgs/SystemCmdInt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemCmdInt.html)        as_rx/headlight_cmd          Commands to the headlight subsystem to enable/disable and set to low/high beams \[enum\].   
     [pacmod_msgs/SystemCmdBool](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemCmdBool.html)      as_rx/horn_cmd               Commands to the horn subsystem to enable/disable \[bool\].                                  
     [pacmod_msgs/SystemCmdBool](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemCmdBool.html)      as_rx/parking_brake_cmd      Commands to the parking brake subsystem to enable/disable \[bool\].                         
     [pacmod_msgs/SystemCmdInt](http://docs.ros.org/en/melodic/api/pacmod_msgs/html/msg/SystemCmdInt.html)        as_rx/wiper_cmd              Commands to the wiper subsystem to set off, intermittent (1-6), low, or high \[enum\].      
  -- --------------------------------------------------------------------------------------------------------- -- ------------------------- -- ------------------------------------------------------------------------------------------- --

# Parameters

\`vehicle_type\`\
A string value indicating the type of vehicle to which the PACMod is
connected. Valid values are:

-   \`LEXUS_RX_450H\`

```{=html}
<!-- -->
```
-   \`POLARIS_GEM\`

```{=html}
<!-- -->
```
-   \`POLARIS_RANGER\`

```{=html}
<!-- -->
```
-   \`INTERNATIONAL_PROSTAR_122\`

```{=html}
<!-- -->
```
-   \`VEHICLE_4\`

```{=html}
<!-- -->
```
-   \`VEHICLE_5\`

```{=html}
<!-- -->
```
-   \`VEHICLE_6\`
