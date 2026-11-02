## Overview

This package provides a [URDF](https://index.ros.org/p/urdf) model of
[Jackal](Robots/Jackal). For an example launchfile to use in visualizing
this model, see [jackal_viz](https://index.ros.org/p/jackal_viz).

![attachment:jackal-urdf.png](doc/jackal-urdf.png)

## Accessories

Jackal has a suite of optional payloads called accessories. These
payloads can be enabled and placed on Jackal using environment variables
specified at the time the [xacro](https://index.ros.org/p/xacro) is
rendered to URDF. Available accessory vars are:

  -- ---------------------------- -- ------------------ -- ----------------------------------------------------------------------------------- --
     **Variable**                    **Default**           **Description**                                                                     
     `JACKAL_LASER`                `0`                 Enable primary laser scanner.                                                       
     `JACKAL_LASER_MOUNT`          `front`             Where to attach primary laser scanner on Jackal.                                    
     `JACKAL_LASER_OFFSET`         `"0 0 0"`         XYZ offset from the mount.                                                          
     `JACKAL_LASER_RPY`            `"0 0 0"`         RPY offset from the mount (eg, to face it backward).                                
     `JACKAL_LASER_HOST`           `192.168.1.14`      IP address of real scanner (used by [jackal_bringup](jackal_bringup))               
     `JACKAL_NAVSAT`               `0`                 Enable upgraded !NovAtel satellite navigation receiver.                             
     `JACKAL_NAVSAT_MOUNT`         `rear`              Where to attach upgraded GNSS to Jackal.                                            
     `JACKAL_NAVSAT_HEIGHT`        `0.1`               Height of GNSS receiver from mount point (metres).                                  
     `JACKAL_NAVSAT`               `0`                 Enable upgraded !NovAtel satellite navigation receiver.                             
     `JACKAL_NAVSAT_MOUNT`         `rear`              Where to attach upgraded GNSS to Jackal.                                            
     `JACKAL_NAVSAT_HEIGHT`        `0.1`               Height of GNSS receiver from mount point (metres).                                  
     `JACKAL_FLEA3`                `0`                 Enable a Pointgrey Flea3 camera.                                                    
     `JACKAL_FLEA3_MOUNT`          `front`             Where to attach the camera on Jackal.                                               
     `JACKAL_FLEA3_OFFSET`         `"0 0 0"`         XYZ offset from the mount.                                                          
     `JACKAL_FLEA3_RPY`            `"0 0 0"`         RPY offset from the mount (eg, to face it backward).                                
     `JACKAL_FLEA3_TILT`           `"0.5236"`        The angle in radians of the camera where positive is down.                          
     `JACKAL_BB2`                  `0`                 Enable a Pointgrey Bumblebee2 camera.                                               
     `JACKAL_BB2_MOUNT`            `front`             Where to attach the camera on Jackal.                                               
     `JACKAL_BB2_OFFSET`           `"0 0 0"`         XYZ offset from the mount.                                                          
     `JACKAL_BB2_RPY`              `"0 0 0"`         RPY offset from the mount (eg, to face it backward).                                
     `JACKAL_BB2_TILT`             `0`                 The angle in radians of the camera where positive is down.                          
     `JACKAL_BB2_CALIBRATION`      `0`                 If the camera has a calibration.                                                    
     `JACKAL_BB2_SERIAL`           `0`                 The serial of the camera which is used for determining the calibration file name.   
  -- ---------------------------- -- ------------------ -- ----------------------------------------------------------------------------------- --

## Configurations

As an alternative to individually specifying each accessory, some fixed
configurations are provided in the package. These can be specified using
the `config` arg to `description.launch`, and are intended
especially as a convenience for simulation launch.

  -- ---------------------- -- --------------------------------------------- --
     **Config**                **Description**                               
     `base`                  Base Jackal, includes IMU and GPS.            
     `front_laser`           Include front-facing LMS1xx LIDAR.            
     `front_bumblebee2`      Includes front-facing Pointgrey Bumblebee2.   
     `front_flea3`           Includes front-facing Pointgrey Flea3.        
  -- ---------------------- -- --------------------------------------------- --

Please see [jackal_simulator](https://index.ros.org/p/jackal_simulator)
for more information on simulating Jackal.
