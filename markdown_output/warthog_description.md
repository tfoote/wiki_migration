## Overview

This package provides a [URDF](urdf) model of [Warthog](Robots/Warthog).
For an example launchfile to use in visualizing this model, see
[warthog_viz](warthog_viz).

![](attachment:warthog-urdf.png)

## Environment Variables

Warthog has a suite of optional payloads called accessories. These
payloads can be enabled and placed on Warthog using environment
variables specified at the time the [xacro](xacro) is rendered to URDF.
Available accessory vars are:

  -- ---------------------------------- -- ---------------------- -- ------------------------------------------------------------------------------------------------------- --
     \'\'\'Variable\'\'\'                  \'\'\'Default\'\'\'       \'\'\'Description\'\'\'                                                                                 
     \`WARTHOG_TRACKS\`                    \`0\`                     Enable tracks instead of wheels.                                                                        
     \`WARTHOG_URDF_EXTRAS\`               \`empty.urdf.xacro\`      Path to a URDF file to extend the base Warthog with additional accessories, links, joints, etc\...      
     \`WARTHOG_NAVSAT_SMART6\`             \`0\`                     Enable the Smart6 GPS sensor.                                                                           
     \`WARTHOG_NAVSAT_SMART6_MOUNT\`       \`navsat\`                Name for the GPS sensor\'s link. It is a childof \`top_chassis_link\`.                                  
     \`WARTHOG_NAVSAT_SMART6_OFFSET\`      \`\"0 0 0\"\`             XYZ offset for the GPS receiver.                                                                        
     \`WARTHOG_NAVSAT_SMART6_RPY\`         \`\"0 0 0\"\`             RPY offset for the GPS receiver.                                                                        
     \`WARTHOG_BULKHEAD\`                  \`0\`                     Enables the extended bulkhead on the front of the robot for containing additional payloads.             
     \`WARTHOG_ARM_MOUNT\`                 \`0\`                     Enables a mounting point for a single arm on the bulkhead. Requires \`WARTHOG_BULKHEAD\` to be \`1\`.   
  -- ---------------------------------- -- ---------------------- -- ------------------------------------------------------------------------------------------------------- --

## Configurations

As an alternative to individually specifying each accessory, some fixed
configurations are provided in the package. These can be specified using
the \`config\` arg to \`description.launch\`, and are intended
especially as a convenience for simulation launch.

  -- -------------------- -- ------------------------------------------- --
     \'\'\'Config\'\'\'      \'\'\'Description\'\'\'                     
     \`base\`                Base Warthog.                               
     \`arm_mount\`           Include the bulkhead and arm mount.         
     \`bulkhead\`            Includes bulkhead, but not the arm mount.   
  -- -------------------- -- ------------------------------------------- --

Please see [warthog_simulator](warthog_simulator) for more information
on simulating Warthog.
