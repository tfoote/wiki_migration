## Overview

### Software architecture

The ZLP software has a modular architecture. These modules communicate
via TCP/IP and have to be located within the same network.

. ![\|width=\"700px\"](attachment:architecture.png)

Z-Laser offers different solutions depending on where you prefer to have
zService running. This package has been developed in a device with
zService built-in to the projector itself.

In this case, zService IP address is **192.168.10.11**, on port
**9090**. In case you have zService running on your PC, contact z-laser
to get the specific IP address of your device.

Projector is expected to be reachable under **192.168.10.10** (factory
default configuration).

To get more information about Thrift and zService, refer to
*ZLP1-quickstart-guide* (provided by z-laser).

### Reference coordinate systems

The laser projector ZLP1 covers working fields from 1.0m x 1.0m up to
3.5m x 3.5m; and working distances from 1.0m to 3.0m. It is able to
project figures in a specific position at various workpiece distances.
It also has the ability to move and rotate the displayed object. To do
this, you need to specify a reference coordinate system first. In order
to embrace this issue, the definition and setting up of reference
coordinate systems will be further explained in this section.

There are two ways to specify a coordinate system: either by setting the
coordinates manually, or by automatic target search. Note that each
point on the projection surface can be referenced by two different
coordinate systems:

-   Projector Reference System {P}. Specified in factory, the coordinate
    system origin is always the same and cannot be changed. User-defined
    reference systems have to be related to this.
-   User Reference System {T}. The user can set the coordinate system
    origin, its resolution and orientation. It must be related to {P}.

Note that a coordinate system needs **4 points** to be fully defined.

. ![\|width=\"450px\"](attachment:projector_origin.png)

#### Setting user-defined reference system manually

An example of manual system definition is going to be developed in order
to guide this section. First, the user must decide the coordinate
system's **resolution** to set a position. See the differences in the
scheme below. This value is non-dimensional, i.e., do not represent real
world dimensions.

. ![\|width=\"400px\"](attachment:resolution.png)

For the following example, we use a resolution of 1000. Then, the user
should indicate the **position** of the four points that define the
coordinate system in real world values (millimetres). This means to
specify the desired correspondent points in Projector Reference System
{P}. For example: .P,,0,, = (-100, -100) \[mm\] .P,,1,, = (-100, 100)
\[mm\] .P,,2,, = (100, 100) \[mm\] .P,,3,, = (100, -100) \[mm\] Please,
be careful to indicate dimensions that correspond to either a square or
a rectangle.

Finally, the user is required to introduce the value for T,,0,, that
will form the User Reference System {T}. Then, the following points will
be auto-defined based on the resolution value. In case the above values
represent a square as in the example, resolution is applied directly:
.T,,0,, = (0, 0) .T,,1,, = (1000, 0) .T,,2,, = (0, 1000) .T,,3,, =
(1000, 1000) However, if it is a rectangle, resolution is applied to
axis with the longest dimension and autoscaled for the other. When
creating a coordinate system, those values are returned for the user to
know.

This is a scheme of the example:

![\|width=\"800px\"](attachment:square.png)

In the image above, the point T,,x,, = (300, 300) referenced from User
Reference System {T}, will be located on the real projection surface at
P,,x,, = (-40mm, -40mm) from the origin of Projector Reference System
{P}.

On the other hand, some situations may require a **rotation** of the
reference system. To achieve that, the user should set the appropriate
coordinates in Projector Reference System {P}. In the scheme below, note
that User Reference System {T} remains the same with respect to the
previous example, while Projector Reference System {P} changed to:
.P,,0,, = (0, -100) \[mm\] .P,,1,, = (100, 0) \[mm\] .P,,2,, = (0, 100)
\[mm\] .P,,3,, = (-100, 0) \[mm\]

![\|width=\"600px\"](attachment:rotate.jpg)

Finally, notice that real world coordinates specified in Projector
Reference System {P} depends on the projection **distance** (distance
between the laser projector and the projection surface), as it is a
beam.

In this example, the real distance between projector and surface is 'd'.
If it is incorrectly indicated as a greater distance 'D', the projected
points would be located more distant ('W') to the coordinate system
origin than the user has specified ('w').

. ![\|width=\"390px\"](attachment:distance.jpg)

For that reason, the installation projection distance must be correctly
indicated, and it can be calculated using the following formula: *d = f
\* 0.5 / (tan(&alpha;/2))* where

-   d: is the projection distance in \[mm\]
-   f: longest side of the projection surface in \[mm\]
-   α: optical opening angle of value 56º.

For example:

Given a length of the desired projection area of 2000mm and an opening
angle of 56\^o\^, it results in an installation distance of 1880.7mm:

. ![\|width=\"600px\"](attachment:angle.png)

#### Setting user-defined reference system by targets scan

The procedure is similar to the manual definition but in this case, the
user indicates the approximate position of the targets that correspond
to the P,,0,,, P,,1,,, P,,2,, and P,,3,, points. After that, the
projector device scans these approximate positions and redefines the
reference system with the exact ones.

## ROS API

The **zlp_projector_zlp1** provides a collection of topics, services and
parameters in order to operate the projector device from ROS
environment, as connecting, disconnecting, defining coordinate systems,
starting and stopping projection, etc.

### Topics

```clearsilver
pub {
  no_header = True
  0{
   name = ~add_projection_element
   type = z_laser_msgs/Figure
   desc = Define a new figure as projection element linked to the active reference system. Nevertheless, it will not be visible until the projection is triggered
   }
  1{
   name = ~add_pointer
   type = z_laser_msgs/Figure
   desc = Define a new scannable pointer as projection element linked to the active reference system
   }
}
```

### Services

```clearsilver
srv{
  no_header = True
  0{
   name = ~connect
   type = std_srvs/Trigger
   desc = Open connection with projector
   }
  1{
   name = ~disconnect
   type = std_srvs/Trigger
   desc = Close connection with projector
   }
  2{
   name = ~projection_start
   type = std_srvs/Trigger
   desc = Start projection of elements linked to the active reference system on the surface
   }
  3{
   name = ~projection_stop
   type = std_srvs/Trigger
   desc = Stop projection of all elements
   }
  4{
   name = ~define_coordinate_system
   type = z_laser_msgs/CoordinateSystem
   desc = Define a new reference system with the points coordinates given manually by the user
   }
  5{
   name = ~search_targets
   type = z_laser_msgs/CoordinateSystem
   desc = Define a new reference system by scanning the position of the targets (reflectors). The user has to provide the approximate position of these points
   }
  6{
   name = ~coordinate_system_list
   type = z_laser_msgs/CoordinateSystemList
   desc = Get the list of defined reference systems
   }
  7{
   name = ~set_coordinate_system
   type = z_laser_msgs/CoordinateSystemName
   desc = Set the reference system indicated as active. The other systems remain in the background
   }
  8{
   name = ~remove_coordinate_system
   type = z_laser_msgs/CoordinateSystemName
   desc = Remove the active reference system. Then, you must set another  
   }
  9{
   name = ~show_active_coordinate_system
   type = z_laser_msgs/CoordinateSystemName
   desc = Project reference points, origin axes and frame of the active reference system for n seconds
   }
  10{
   name = ~hide_figure
   type = z_laser_msgs/ProjectionElement
   desc = Hide projection element from the active reference system
   }
  11{
   name = ~unhide_figure
   type = z_laser_msgs/ProjectionElement
   desc = Unhide projection element from the active reference system
   }
  12{
   name = ~remove_figure
   type = z_laser_msgs/ProjectionElement
   desc = Remove projection element from the active reference system
   }
  13{
   name = ~monitor_figure 
   type = z_laser_msgs/ProjectionElement
   desc = Monitor projection element with the keyboard
   }
  14{
   name = ~scan_pointer 
   type = std_srvs/Trigger
   desc = Start pointer scanning
   }
```

### Parameters

```clearsilver
param {
  no_header = True
  0{
   name = ~projector_IP
   type = string
   desc = Projector IP address 
   }
  1{
   name = ~server_IP
   type = string
   desc = ZLP-Server IP address
   }
  2{
   name = ~connection_port
   type = int
   desc = Connection port number
   }
  3{
   name = ~license_file
   type = string
   desc = ZLP license file path
   }
  4{
   name = ~coordinate_system_name
   type = string
   desc = Name of reference system
   default = "default_cs"
   }
  5{
   name = ~coordinate_system_resolution
   type = string
   desc = Resolution of reference system
   default = 1000
   }
  6{
   name = ~coordinate_system_distance
   type = string
   desc = Distance between laser projector device and projection surface
   default = 1500
   }
  7{
   name = ~P_/x
   type = float
   desc = x-position of point P0, P1, P2 or P3 from projector reference system {P}
   }
  8{
   name = ~P_/y
   type = float
   desc = y-position of point P0, P1, P2 or P3 from projector reference system {P}
   }
  9{
   name = ~T0/x
   type = float
   desc = x-position of point T0 from user reference system {T}
   default = 0
   }
  10{
   name = ~T0/y
   type = float
   desc = y-position of point T0 from user reference system {T}
   default = 0
   }
  11{
   name = ~projector_connected
   type = bool
   desc = Connection status of the device
   }
  12{
   name = ~using_visualizer
   type = bool
   desc = Indicates if running visualizer
   default = 0
   }
```

## Acknowledgement

[Included page rosin/acknowledgement not found](Included page rosin/acknowledgement not found)
