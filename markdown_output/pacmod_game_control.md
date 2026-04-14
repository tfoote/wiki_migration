A ROS package which supports controlling the
[AutonomouStuff PACMod drive-by-wire system](https://autonomoustuff.com/product/small-ev-by-wire-kits/)
with a standard game system controller using [joy](joy). This supports
both [pacmod](pacmod) and [pacmod3](pacmod3).

## Supported Controllers

It is very easy to add additional controllers. Simply add the new
controller type to the !GamepadType enum in \`include/globals.h\` and
create new button mappings in \`src/startup_checks.cpp\`. The currently
supported controllers are:

-   Logitech F310
-   [HRI Safe Remote](https://autonomoustuff.com/product/hri-remote-control-system/)
-   Logitech G29 Steering Wheel and Pedals
-   Nintendo Switch Wired Plus
-   XBOX ONE Wired or Wireless Controller

## Controller Button Functions

Shown below is the Logitech F310 controller.
![Left: Front Layout of logitech Controller; Right: Side-button layout of logitech controller\|width=750](attachment:controller_img.png)

  -- ------------------------------------------------------------------------------------- -- ------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------ --
     \<tablebgcolor=\"#E0E0FF\"\>                                                                                                                                                                                                                                                       
     \<rowbgcolor=\"#FFFFE0\"\>\'\'\'Button\'\'\'                                             \'\'\'Action\'\'\'                       \'\'\'Notes\'\'\'                                                                                                                                
     \<rowstyle=\"background-color: #FFFFE0;\"\>\'\'Directional Pad (left-hand side)\'\'      \'\'Headlights and Turn Signals\'\'                                                                                                                                                       
     Up                                                                                       Headlights                               Some vehicles only                                                                                                                               
     Left                                                                                     Left turn signal                                                                                                                                                                          
     Right                                                                                    Right turn signal                                                                                                                                                                         
     Down                                                                                     Hazards                                  Some vehicles only                                                                                                                               
     \<rowstyle=\"background-color: #FFFFE0;\"\>\'\'Button Pad (right-hand side)\'\'          \'\'Gear Selection\'\'                                                                                                                                                                    
     A                                                                                        Drive                                                                                                                                                                                     
     B                                                                                        Reverse                                                                                                                                                                                   
     X                                                                                        Neutral                                                                                                                                                                                   
     Y                                                                                        Park                                                                                                                                                                                      
     \<rowstyle=\"background-color: #FFFFE0;\"\>\'\'Center region\'\'                                                                                                                                                                                                                   
     Back                                                                                     Enable/Disable                           \'Back\' and \'Start\' buttons must be pressed simultaneously to enable by-wire mode. \'Back\' button must be pressed to disable by-wire mode.   
     Start                                                                                    Enable                                   \'Back\' and \'Start\' buttons must be pressed simultaneously to enable by-wire mode.                                                            
     Mode                                                                                     Not supported                            Do not use. Mode light should be OFF at all times. Pressing mode button will change button mapping.                                              
     \<rowstyle=\"background-color: #FFFFE0;\"\>\'\'Joystick\'\'                              \'\'Steering\'\'                         \'\'Joystick click buttons unused\'\'                                                                                                            
     Left joystick                                                                            Steering                                 Steering defaults to left joystick, but can be set to right joystick by operator.                                                                
     Right joystick                                                                           Steering                                 Only if set by operator; steering defaults to left joystick                                                                                      
     Left bumper                                                                              Wiper                                    Some vehicles only                                                                                                                               
     Left trigger                                                                             Brake                                                                                                                                                                                     
     Right bumper                                                                             Horn                                     Some vehicles only                                                                                                                               
     Right trigger                                                                            Throttle                                                                                                                                                                                  
  -- ------------------------------------------------------------------------------------- -- ------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------ --

## Parameters

\`steering_stick\`\
Sets whether the steering command should be controlled by the left or
right joystick on a two-stick controller. Valid values are \`LEFT\` or
\`RIGHT\`.

\`pacmod_vehicle_type\`\
Sets the type of vehicle which is being controlled. This manages
vehicle-specific values like the available features and maximum steering
angle. Valid values are:

-   \`POLARIS_GEM\`
-   \`POLARIS_RANGER\`
-   \`LEXUS_RX_450H\`
-   \`INTERNATIONAL_PROSTAR_122\`
-   \`FREIGHTLINER_CASCADIA\`
-   \`HEXAGON_TRACTOR\`
-   \`FORD_RANGER\`
-   \`TOYOTA_MINIVAN\`
-   \`VEHICLE_4\`
-   \`VEHICLE_5\`
-   \`VEHICLE_6\`

\`controller_type\`\
Sets the type of controller being used and associated button mappings.
Valid values are:

-   \`LOGITECH_F310\`
-   \`HRI_SAFE_REMOTE\`
-   \`LOGITECH_G29\`
-   \`NINTENDO_SWITCH_WIRED_PLUS\`
-   \`XBOX_ONE\`

\`steering_max_speed\`\
The maximum rotational speed for the steering wheel in rad/s.

\`max_veh_speed\`\
The vehicle speed is used to scale the rotation rate of the steering
wheel. This value is the speed, in m/s, at which the most restriction is
placed on rotation rate. This helps controlability as speed increases.

\`accel_scale_val\`\
A scaling value (0.0 - 1.0) for the accelerator. 1.0 = full throttle
range. 0.0 = no throttle control.

\`brake_scale_val\`\
A scaling value (0.0 - 1.0) for the brake. 1.0 = full braking range. 0.0
= no brake control.
