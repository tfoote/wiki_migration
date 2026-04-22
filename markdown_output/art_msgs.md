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

-   [art_msgs/msg/ArtHertz](https://docs.ros.org/en/rolling/p/art_msgs/msg/ArtHertz.html)
    control cycle rates for various ART vehicle nodes
-   [art_msgs/msg/ArtVehicle](https://docs.ros.org/en/rolling/p/art_msgs/msg/ArtVehicle.html)
    ART vehicle dimensions
-   [art_msgs/msg/Conversions](https://docs.ros.org/en/rolling/p/art_msgs/msg/Conversions.html)
    unit conversion constants
-   [art_msgs/msg/Epsilon](https://docs.ros.org/en/rolling/p/art_msgs/msg/Epsilon.html)
    constants representing trivial differences

### Global Positioning System

-   [art_msgs/msg/GpsInfo](https://docs.ros.org/en/rolling/p/art_msgs/msg/GpsInfo.html)
    GPS information (to be replaced by
    [sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)
    for Diamondback release)

### Navigation

[art_nav](art_nav)

-   [art_msgs/msg/Behavior](https://docs.ros.org/en/rolling/p/art_msgs/msg/Behavior.html)
-   [art_msgs/msg/EstopState](https://docs.ros.org/en/rolling/p/art_msgs/msg/EstopState.html)
-   [art_msgs/msg/NavigatorCommand](https://docs.ros.org/en/rolling/p/art_msgs/msg/NavigatorCommand.html)
-   [art_msgs/msg/NavigatorState](https://docs.ros.org/en/rolling/p/art_msgs/msg/NavigatorState.html)
-   [art_msgs/msg/Order](https://docs.ros.org/en/rolling/p/art_msgs/msg/Order.html)
-   [art_msgs/msg/RoadState](https://docs.ros.org/en/rolling/p/art_msgs/msg/RoadState.html)
-   [art_msgs/msg/WayPoint](https://docs.ros.org/en/rolling/p/art_msgs/msg/WayPoint.html)

### Observers

[art_observers](art_observers)

-   [art_msgs/msg/Observation](https://docs.ros.org/en/rolling/p/art_msgs/msg/Observation.html)
-   [art_msgs/msg/ObservationArray](https://docs.ros.org/en/rolling/p/art_msgs/msg/ObservationArray.html)

### Road map

[art_map](art_map)

-   [art_msgs/msg/ArtLanes](https://docs.ros.org/en/rolling/p/art_msgs/msg/ArtLanes.html)
-   [art_msgs/msg/ArtQuadrilateral](https://docs.ros.org/en/rolling/p/art_msgs/msg/ArtQuadrilateral.html)
-   [art_msgs/msg/LaneMarking](https://docs.ros.org/en/rolling/p/art_msgs/msg/LaneMarking.html)
-   [art_msgs/msg/MapID](https://docs.ros.org/en/rolling/p/art_msgs/msg/MapID.html)

### Servo control

[art_pilot](art_pilot)

-   [art_msgs/msg/CarCommand](https://docs.ros.org/en/rolling/p/art_msgs/msg/CarCommand.html)
    (*deprecated*, use
    [art_msgs/msg/CarDriveStamped](https://docs.ros.org/en/rolling/p/art_msgs/msg/CarDriveStamped.html))
-   [art_msgs/msg/CarControl](https://docs.ros.org/en/rolling/p/art_msgs/msg/CarControl.html)
    (*deprecated*, use
    [art_msgs/msg/CarDrive](https://docs.ros.org/en/rolling/p/art_msgs/msg/CarDrive.html))
-   [art_msgs/msg/CarDrive](https://docs.ros.org/en/rolling/p/art_msgs/msg/CarDrive.html)
-   [art_msgs/msg/CarDriveStamped](https://docs.ros.org/en/rolling/p/art_msgs/msg/CarDriveStamped.html)
-   [art_msgs/msg/LearningCommand](https://docs.ros.org/en/rolling/p/art_msgs/msg/LearningCommand.html)
    (*deprecated*, use
    [art_msgs/msg/CarDrive](https://docs.ros.org/en/rolling/p/art_msgs/msg/CarDrive.html))
-   [art_msgs/msg/PilotState](https://docs.ros.org/en/rolling/p/art_msgs/msg/PilotState.html)

### Servo devices

[art_servo](art_servo)

-   [art_msgs/msg/BrakeCommand](https://docs.ros.org/en/rolling/p/art_msgs/msg/BrakeCommand.html)
-   [art_msgs/msg/BrakeState](https://docs.ros.org/en/rolling/p/art_msgs/msg/BrakeState.html)
-   [art_msgs/msg/DriverState](https://docs.ros.org/en/rolling/p/art_msgs/msg/DriverState.html)
-   [art_msgs/msg/IOadrCommand](https://docs.ros.org/en/rolling/p/art_msgs/msg/IOadrCommand.html)
-   [art_msgs/msg/IOadrState](https://docs.ros.org/en/rolling/p/art_msgs/msg/IOadrState.html)
-   [art_msgs/msg/Shifter](https://docs.ros.org/en/rolling/p/art_msgs/msg/Shifter.html)
-   [art_msgs/msg/SteeringCommand](https://docs.ros.org/en/rolling/p/art_msgs/msg/SteeringCommand.html)
-   [art_msgs/msg/SteeringDiag](https://docs.ros.org/en/rolling/p/art_msgs/msg/SteeringDiag.html)
-   [art_msgs/msg/SteeringState](https://docs.ros.org/en/rolling/p/art_msgs/msg/SteeringState.html)
-   [art_msgs/msg/ThrottleCommand](https://docs.ros.org/en/rolling/p/art_msgs/msg/ThrottleCommand.html)
-   [art_msgs/msg/ThrottleState](https://docs.ros.org/en/rolling/p/art_msgs/msg/ThrottleState.html)
