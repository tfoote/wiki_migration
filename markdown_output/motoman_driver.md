```wiki
This information is for the '''ROS 1''' interface. If you are looking for ROS 2 support, please visit [[https://github.com/Yaskawa-Global/motoros2|Yaskawa-Global/motoros2]].
```

## Overview

The Motoman driver controller interface was created with the cooperation
of Yaskawa Motoman, to provide a more high-performance interface for
controlling Motoman robots. This interface provides a number of
improvements, including:

-   robot speeds up to 100% of robot capability for DX100, DX200, FS100,
    YRC1000 and YRC1000micro controllers
-   low-level control of joint position, velocity, and path timing
-   improved fault detection and recovery
-   improved motion and controller status feedback

## Technology Stack

The following diagram shows the layered architecture of the
ROS-Industrial motion stack and how it interfaces with MotoROS on the
Yaskawa Motoman controller.

![MotoROS Architecture\|](attachment:MotoROS_heirarchy.jpg)

## Requirements

The software will work on all
[FS100](https://www.motoman.com/products/controllers/fs100_controller),
[DX100](https://cdn2.hubspot.net/hubfs/366775/PDFs/DX100_Controller.pdf?t=1508182504087),
[DX200](https://www.motoman.com/products/controllers/dx200_controller),
[YRC1000](https://www.motoman.com/products/controllers/yrc1000) and
[YRC1000micro](https://www.motoman.com/en-us/products/controllers/yrc1000micro)
robot controllers. However, for DX100 controllers, a specific software
option must be explicitly ordered from Motoman in order to enable
ROS-Industrial integration (see the
[MotoPlus Runtime License](#MotoPlus Runtime License) section below).

For more detailed information, please contact one of the support
resources listed on
[ROS-Industrial Technical Support](https://rosindustrial.org/tech-support/)
or [Yaskawa Motoman Technical Support](mailto:techsupport@motoman.com).

The MotoROS software is compatible with the Human Collaborative (HC)
series robots. Please see the compatibility notes below.

### Controller system software

The latest MotoROS binary (`v1.5.0` or higher) requires the following
controller firmware (or a newer version):

  -- ---------------------------------------------------- -- -------------------------------------------------------- --
     **Controller**                                          **Version**                                              
     FS100                                                   `FS3.30.00-00` (or newer)                              
     DX100                                                   `DS4.12.00-14` (or newer, *and* must end in `-14`)   
     DX200                                                   `DN2.21.00-00` (or newer)                              
     YRC1000                                                 `YAS1.11.00-00` (or newer)                             
     YRC1000 ([HC robot](attachment:HC Notes.pdf))           `YAS2.80.00-00` (or newer)                             
     YRC1000micro                                            All controller versions                                  
     YRC1000micro ([HC robot](attachment:HC Notes.pdf))      `YBS2.31.00-00` (or newer)                             
  -- ---------------------------------------------------- -- -------------------------------------------------------- --

### MotoPlus Runtime License

**Note**: this is required for the *DX100 controller only*.

The following part number must be ordered for the DX100 robot
controller:

  -- ------------------------- -- ----------------- --
     **Region**                   **Part number**   
     Americas (North, South)      `180014-1`      
     Europe                       `167536`        
  -- ------------------------- -- ----------------- --

\
The MotoROS application and source is available for public download.
However, ordering this part number will ensure your controller is
updated with correct system software, the MotoROS driver is installed,
and all internal parameters are properly configured.

### MotoPlus SDK (optional)

**Note**: This is *optional for all controller models*, but will allow
you to modify the MotoROS driver which runs on the robot controller. The
!MotoPlus SDK is **not** required to be able to develop ROS
applications, it is only needed if the MotoROS application is to be
changed.

  -- ---------------- -- ------------------------- -- ------------------------ --
     **Controller**      **America Part Number**      **Europe Part Number**   
     FS100               `169272-3`                 `158302`               
     DX100               `169272-1`                 `147961`               
     DX200               `169272-2`                 `166386`               
     YRC1000             `169272-4`                 `183387`               
     YRC1000micro        `169272-5`                 `206078`               
  -- ---------------- -- ------------------------- -- ------------------------ --

### More information

For more information, please contact Yaskawa Motoman and inquire about
the ROS package.

## Compatibility with collaborative robots (HC series)

Please note that the MotoROS application is now compatible with the
Human Collaborative HC series robots. Please review the
[HC Notes](attachment:HC Notes.pdf) document to understand the
functionality and limitations.

## Design

The Motoman driver communicates with ROS through the
[simple_message](simple_message) interface, with a few additional
Motoman-specific message types. Trajectories are streamed to the
controller using a message format that captures all the ROS
[JointTrajectoryPoint](http://ros.org/doc/api/trajectory_msgs/html/msg/JointTrajectoryPoint.html)
data: joint positions, velocities, accelerations, and path timing. The
controller buffers these points and interpolates between them to send
commands to the controller at the required timing. More detail on the
internal operations and required `simple_message` commands is
documented [here](attachment:MotoRos_EDS.pdf).

## Performance

The Motoman driver interface provides a high-performance motion control
interface for Motoman robots. In general, robot motion is smooth, but
can be choppy if poorly-filtered trajectory commands are sent. The
controller performs only minimal trajectory filtering, so users must
take care to properly condition the trajectories before submitting. The
interface does provide some low-level filtering, however. Sudden stops
or breaks in the trajectory stream result in smooth deceleration on the
physical robot hardware.

## Tutorials

See the [tutorials](motoman_driver/Tutorials) page for details on
installing and using the MotoROS software.

## Troubleshooting

See the [troubleshooting](motoman_driver/Troubleshooting) page for
details on alarms and errors when using the MotoROS driver.
