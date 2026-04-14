# Epson IMU ROS2 Node UART \*\* Deprecated \*\*

\'\'\'**\* NOTE: This package has been superceded by
[ Epson IMU ROS2 Driver Node](ess_imu_driver2 )**\*\'\'\'

\'\'\'**\* This webpage will no longer be updated **\*\'\'\'
\-\-\-\-\-\-\-\-\-\-\--
![\|align=\"right\"](attachment:ess_sensors/g552.jpg)
![\|align=\"right\"](attachment:ess_sensors/g370.jpg)
![\|align=\"right\"](attachment:ess_sensors/g365.jpg)

## Overview

\-\-\-\-\-\-\-\-\-\-\--

-   The [ Epson IMU ROS software](ess_sensors ) is C++ wrapper around a
    Linux C driver for communicating on a ROS2 system
    [ Epson IMU SPI or UART Linux User-space Driver Example](https://vdc.epson.com/imu-products/imu-inertial-measurement-units )
-   This code assumes that the user is familiar with building ROS2
    packages using the colcon build process
-   This is \*NOT\* detailed step by step instructions describing how to
    build and install this ROS2 driver
-   Refer to the README.md inside the ROS package for more detailed
    up-to-date technical info on usage or
    [ Github repository](https://github.com/cubicleguy/ess_imu_ros2_uart_driver )

## UART Connection & Configuration

\-\-\-\-\-\-\-\-\-\--

-   When connecting the Epson device to a ROS2 system using the UART
    interface:
-   direct connection to UART port must be compatible with CMOS 3.3V I/O
-   connection is also possible through a USB-UART 3.3V converter IC
    such as on the
    [M-G32EV041 evaluation board](https://global.epson.com/products_and_drivers/sensing_system/technical_info/evaluation_tools/ )
-   GPIO output for asserting RESET# pin on the IMU is optional, but
    recommended if possible (i.e. embedded platforms)
-   Below is an example IMU UART connection when using a Raspberry Pi:

  -- ----------------------- -- ------------------------------------------- --
     \'\'\'Epson IMU\'\'\'      \'\'\'Raspberry Pi\'\'\'                    
     EPSON_SIN Input            RPI_GPIO_P1_8 (GPIO14/UART_TXD) Output      
     EPSON_SOUT Output          RPI_GPIO_P1_10 (GPIO15/UART_RXD) Input      
     EPSON_RESET Input          RPI_GPIO_P1_15 (GPIO22) Output \*Optional   
  -- ----------------------- -- ------------------------------------------- --

-   When connecting the Epson G552PR to a ROS2 system using a RS422 UART
    interface:
-   direct connection to RS422 UART port must be compatible with RS422
    I/O signal levels
-   Below is an example IMU RS422 connection to a RS422 Host:

  -- ----------------------- -- ------------------------ --
     \'\'\'Epson IMU\'\'\'      \'\'\'RS422 Host\'\'\'   
     EPSON_TD+ Output           HOST_RD+ Input           
     EPSON_TD- Output           HOST_RD- Input           
     EPSON_RD+ Input            HOST_TD+ Output          
     EPSON_RD- Input            HOST_TD- Output          
  -- ----------------------- -- ------------------------ --

## ROS2 Node

\-\-\-\-\-\-\-\-\-\-\--

-   This ROS2 driver publishes IMU messages as per
    [ REP 145 Conventions for IMU Sensor Drivers](http://www.ros.org/reps/rep-0145.html )
-   [sensor_msgs/Imu](sensor_msgs/Imu) - contains header, orientation,
    angular velocity and linear acceleration

### Published Topics

-   For IMU models that support \'\'quaternion output function\'\' the
    orientation field in [sensor_msgs/Imu](sensor_msgs/Imu) can update
    with valid data and publish on \'\'\'imu/data\'\'\'
-   For IMU models that \'\'do not\'\' support \'\'quaternion output
    function\'\' the orientation field in
    [sensor_msgs/Imu](sensor_msgs/Imu) \'\'will not\'\' update with
    valid data and publish on \'\'\'imu/data_raw\'\'\'

### Launch File

-   The
    [ launch file](https://docs.ros.org/en/foxy/Tutorials/Launch-Files/Creating-Launch-Files.html?highlight=launch )
    in the launch folder of this package is used to pass the init
    parameters to configure the IMU at runtime using ros2 launch
-   Changes to init parameters by editing the launch file does not
    require rebuilding with \'\'colcon\'\'
-   \'\'\'Typically, the user only needs to modify \'\'imu_dout_rate\'\'
    & \'\'imu_filter_sel\'\' as needed based on system
    requirements\'\'\'
-   Only use the specific IMU model launch file associated with the same
    IMU model built using \'\'colcon build\'\'

### Timestamping With EXT Signal (Time Correction)

-   The G3xx series Epson IMU has 3.3V I/O EXT (GPIO2) pin which can be
    connected to a cyclic external sync signal such as a GNSS 1PPS
    signal
-   When the init parameter \'\'time_correction_en\'\' is enabled
-   The ROS2 driver attempts to correct the time stamp field in
    [sensor_msgs/Imu](sensor_msgs/Imu) based on the reset counter value
    (measured delay since latest GNSS 1PPS)
-   This should give a more accurate timestamp of the inertial data by
    minimizing the effects of link delays or host processing overhead
    delays

## Building & Installing ROS2 Node

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

1\. Place this package (including folders) into a new folder within your
colcon workspace \'\'src/\'\' folder.

2\. Modify the [ CMakeLists.txt](CMakeLists.txt ) to select the desired
Epson IMU model that is being used in the ROS2 system.

-   \'\'\'NOTE: You \*MUST\* re-build using colcon when changing IMU
    models or any changes in the
    [ CMakeLists.txt](CMakeLists.txt )\'\'\'

3\. From the colcon workspace folder run \'\'colcon build\'\' to build
all changed ROS2 packages located in the \<colcon_workspace\>/src/
folder.

4\. Reload the current ROS2 environment variables that may have changed
after the colcon build process.

```
From the <colcon_workspace>: source install/setup.bash
```

5\. Modify the appropriate
[ launch file](https://docs.ros.org/en/foxy/Tutorials/Launch-Files/Creating-Launch-Files.html?highlight=launch )
to set your desired IMU init parameters for the specific IMU model in
the launch folder that you selected and built

-   \'\'\'Typically, only the \'\'imu_dout_rate\'\' &
    \'\'imu_filter_sel\'\' needs to be edited\'\'\'

## Running the ROS2 Node

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   To start the Epson IMU ROS2 driver use the appropriate
    [ launch file](https://docs.ros.org/en/foxy/Tutorials/Launch-Files/Creating-Launch-Files.html?highlight=launch )
    (located in launch/) with
    [ ros2 launch](https://design.ros2.org/articles/roslaunch.html )

```{=html}
<!-- -->
```
-   For example:

```
<colcon_workspace>/ros2 launch ess_imu_ros2_uart_driver g370_launch.py
```

## USB-UART Latency

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   When using USB-UART bridge ICs to connect between the Linux host &
    Epson IMU, it is possible to experience higher than expected
    latencies or slower than expected IMU data rates
-   This could be caused by the USB-UART bridge device driver software
    which sets the default latency_timer too large (i.e. typically
    16msec)
-   There are 2 recommended methods to reduce this value to 1msec to
    improve the latency & IMU publishing data rate

### Modify latency_timer by sysfs mechanism

-   The example below reads the latency_timer setting for /dev/ttyUSB0
    which returns 16msec
-   Then, the latency_timer is set to 1msec, and confirmed by readback.
-   \'\'\'NOTE:\'\'\' May require root (sudo su) access on your system
    to modify.

```
cat /sys/bus/usb-serial/devices/ttyUSB0/latency_timer
16
echo 1 > /sys/bus/usb-serial/devices/ttyUSB0/latency_timer
cat /sys/bus/usb-serial/devices/ttyUSB0/latency_timer
1
```

### Modify low_latency flag using setserial utility

-   The example below sets the low_latency flag for /dev/ttyUSB0.
-   This will have the same effect as setting the latency_timer to
    1msec.
-   This can be confirmed by running the setserial command again.
-   \'\'\'NOTE:\'\'\' You may need to install setserial with \'\'sudo
    apt install setserial\'\'

```
user@user-VirtualBox:~$ setserial /dev/ttyUSB0
/dev/ttyUSB0, UART: unknown, Port: 0x0000, IRQ: 0

user@user-VirtualBox:~$ setserial /dev/ttyUSB0 low_latency

user@user-VirtualBox:~$ setserial /dev/ttyUSB0
/dev/ttyUSB0, UART: unknown, Port: 0x0000, IRQ: 0, Flags: low_latency
```

## Technical Support

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   For technical support or related issues using this ROS software,
    please email sensingsystem_support@ea.epson.com
