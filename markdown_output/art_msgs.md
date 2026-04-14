## Overview

This package collects all ROS messages that are specific to the ART
autonomous vehicle, simplifying the dependencies between
[art_vehicle](art_vehicle) stack components.

It has minimal build dependencies, eliminating unnecessary compiles when
modifying a package which only interacts with others via messages.

## Message Groupings

Many of these messages are primarily associated with specific
[art_vehicle](art_vehicle) packages:

### Global

-   \<\<MsgLink(art_msgs/ArtHertz)\>\> control cycle rates for various
    ART vehicle nodes
-   \<\<MsgLink(art_msgs/ArtVehicle)\>\> ART vehicle dimensions
-   \<\<MsgLink(art_msgs/Conversions)\>\> unit conversion constants
-   \<\<MsgLink(art_msgs/Epsilon)\>\> constants representing trivial
    differences

### Global Positioning System

-   \<\<MsgLink(art_msgs/GpsInfo)\>\> GPS information (to be replaced by
    \<\<MsgLink(sensor_msgs/NavSatFix)\>\> for Diamondback release)

### Navigation

[art_nav](art_nav)

-   \<\<MsgLink(art_msgs/Behavior)\>\>
-   \<\<MsgLink(art_msgs/EstopState)\>\>
-   \<\<MsgLink(art_msgs/NavigatorCommand)\>\>
-   \<\<MsgLink(art_msgs/NavigatorState)\>\>
-   \<\<MsgLink(art_msgs/Order)\>\>
-   \<\<MsgLink(art_msgs/RoadState)\>\>
-   \<\<MsgLink(art_msgs/WayPoint)\>\>

### Observers

[art_observers](art_observers)

-   \<\<MsgLink(art_msgs/Observation)\>\>
-   \<\<MsgLink(art_msgs/ObservationArray)\>\>

### Road map

[art_map](art_map)

-   \<\<MsgLink(art_msgs/ArtLanes)\>\>
-   \<\<MsgLink(art_msgs/ArtQuadrilateral)\>\>
-   \<\<MsgLink(art_msgs/LaneMarking)\>\>
-   \<\<MsgLink(art_msgs/MapID)\>\>

### Servo control

[art_pilot](art_pilot)

-   \<\<MsgLink(art_msgs/CarCommand)\>\> (\'\'deprecated\'\', use
    \<\<MsgLink(art_msgs/CarDriveStamped)\>\>)
-   \<\<MsgLink(art_msgs/CarControl)\>\> (\'\'deprecated\'\', use
    \<\<MsgLink(art_msgs/CarDrive)\>\>)
-   \<\<MsgLink(art_msgs/CarDrive)\>\>
-   \<\<MsgLink(art_msgs/CarDriveStamped)\>\>
-   \<\<MsgLink(art_msgs/LearningCommand)\>\> (\'\'deprecated\'\', use
    \<\<MsgLink(art_msgs/CarDrive)\>\>)
-   \<\<MsgLink(art_msgs/PilotState)\>\>

### Servo devices

[art_servo](art_servo)

-   \<\<MsgLink(art_msgs/BrakeCommand)\>\>
-   \<\<MsgLink(art_msgs/BrakeState)\>\>
-   \<\<MsgLink(art_msgs/DriverState)\>\>
-   \<\<MsgLink(art_msgs/IOadrCommand)\>\>
-   \<\<MsgLink(art_msgs/IOadrState)\>\>
-   \<\<MsgLink(art_msgs/Shifter)\>\>
-   \<\<MsgLink(art_msgs/SteeringCommand)\>\>
-   \<\<MsgLink(art_msgs/SteeringDiag)\>\>
-   \<\<MsgLink(art_msgs/SteeringState)\>\>
-   \<\<MsgLink(art_msgs/ThrottleCommand)\>\>
-   \<\<MsgLink(art_msgs/ThrottleState)\>\>
