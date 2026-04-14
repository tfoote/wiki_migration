## Epson Sensing System Sensors

\-\-\-\-\-\-\-\-\-\-\--

![\|align=\"right\"](attachment:g552.jpg)
![\|align=\"right\"](attachment:g370.jpg)
![\|align=\"right\"](attachment:g365.jpg)

## Overview

\-\-\-\-\-\-\-\-\-\-\--

-   These ROS drivers are intended for evaluation of the Epson IMUs on a
    ROS1 or ROS2 system.
-   The different Epson 6DOF IMU models have various sensing ranges that
    can be evaluated in a ROS based system.
-   Epson IMU are performance-oriented products with a combination of
    low power consumption and small size.
-   G3xx models are intended for board-level integration using a SPI or
    UART interface
-   G552PR models are intended for remote mounting in harsh environments
    exposed to moisture or dust using a cabled RS422 UART interface
-   For more detailed product info & specifications please refer to
    [ Epson Sensing System](https://global.epson.com/products_and_drivers/sensing_system/ )
-   These ROS drivers are available for download from GitHub
-   [ ROS](https://github.com/cubicleguy/ess_imu_driver )
-   [ ROS2](https://github.com/cubicleguy/ess_imu_driver2 )

## Supported Devices

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   The ROS drivers are maintained to support the following Epson
    products:
-   G570PR
-   G370PDF / G370PDS / G370PDG / G370PDT
-   G330PDG / G366PDG
-   G365PDC / G365PDF
-   G364PDC
-   G354PDH

## Requirements

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

### ROS Platform

-   These drivers have been tested using the following host platforms:
-   Intel PCs running Ubuntu 20.x, or 22.x
-   Raspberry Pi 2, 3+, 4 running Ubuntu Mate 20.x, 22.x

### Serial Interfaces

-   These drivers supports UART or SPI serial interface connection to
    the Epson device
-   For G552PRx select the UART interface
-   The host system must have a RS422 I/O compatible UART interface
    (UART protocol over RS422) for connecting to the G552PRx IMU

## How to Use This Software

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   Click on the link below for the ROS version:
-   [ ROS1 UART or SPI Interface](ess_imu_driver )
-   [ ROS2 UART or SPI Interface](ess_imu_driver2 )

## Technical Support

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   For technical support or related issues using this ROS software,
    please email sensingsystem_support@ea.epson.com
