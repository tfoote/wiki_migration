## Overview

This package provides a [URDF](urdf) model of
[Ridgeback](Robots/Ridgeback). For an example launchfile to use in
visualizing this model, see [ridgeback_viz](ridgeback_viz).

![](attachment:ridgeback-urdf.png)

## Accessories

Ridgeback has a suite of optional payloads called accessories. These
payloads can be enabled and placed on Ridgeback using environment
variables specified at the time the [xacro](xacro) is rendered to URDF.
Available accessory vars are:

  -- ---------------------------------- -- -------------------- -- ----------------------------------------------------------------------------- --
     **Variable**                          **Default**             **Description**                                                               
     \`RIDGEBACK_FRONT_LASER\`             \`0\`                   Enable primary laser scanner.                                                 
     \`RIDGEBACK_FRONT_LASER_MOUNT\`       \`front\`               Where to attach primary laser scanner on Ridgeback.                           
     \`RIDGEBACK_FRONT_LASER_OFFSET\`      \`\"0 0 0\"\`           XYZ offset from the mount.                                                    
     \`RIDGEBACK_FRONT_LASER_RPY\`         \`\"0 0 0\"\`           RPY offset from the mount (eg, to face it backward).                          
     \`RIDGEBACK_FRONT_LASER_HOST\`        \`192.168.131.14\`      IP address of real scanner (used by [ridgeback_bringup](ridgeback_bringup))   
     \`RIDGEBACK_REAR_LASER\`              \`0\`                   Enable secondary laser scanner.                                               
     \`RIDGEBACK_REAR_LASER_MOUNT\`        \`rear\`                Where to attach secondary laser scanner on Ridgeback.                         
     \`RIDGEBACK_REAR_LASER_OFFSET\`       \`\"0 0 0\"\`           XYZ offset from the mount.                                                    
     \`RIDGEBACK_REAR_LASER_RPY\`          \`\"0 0 0\"\`           RPY offset from the mount (eg, to face it backward).                          
     \`RIDGEBACK_REAR_LASER_HOST\`         \`192.168.131.13\`      IP address of real scanner (used by [ridgeback_bringup](ridgeback_bringup))   
  -- ---------------------------------- -- -------------------- -- ----------------------------------------------------------------------------- --

## Configurations

As an alternative to individually specifying each accessory, some fixed
configurations are provided in the package. These can be specified using
the \`config\` arg to \`description.launch\`, and are intended
especially as a convenience for simulation launch.

  -- ---------------- -- ----------------------------------------------------------------- --
     **Config**          **Description**                                                   
     \`base\`            Base Ridgeback, includes a IMU and a front-facing LMS1xx LIDAR.   
     \`dual_laser\`      Includes a front and rear-facing LMS1xx LIDAR.                    
  -- ---------------- -- ----------------------------------------------------------------- --
