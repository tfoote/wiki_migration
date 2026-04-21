# Epson IMU ROS2 Node SPI \*\* Deprecated \*\*

****\* NOTE: This package has been superceded by
[ Epson IMU ROS2 Driver Node](ess_imu_driver2 )\*****

****\* This webpage will no longer be updated \* \-\-\-\-\-\-\-\-\-\-\--
![\|align=\"right\"](attachment:ess_sensors/g552.jpg)
![\|align=\"right\"](attachment:ess_sensors/g370.jpg)
![\|align=\"right\"](attachment:ess_sensors/g365.jpg)****

## Overview

\-\-\-\-\-\-\-\-\-\-\--

-   The [ Epson IMU ROS software](ess_sensors ) is C++ wrapper around a
    C Linux driver for communicating on a ROS2 system
    [ Epson IMU SPI or UART Linux User-space Driver Example](https://vdc.epson.com/imu-products/imu-inertial-measurement-units )
-   This code assumes that the user is familiar with building ROS2
    packages using the colcon build process
-   This is \*NOT\* detailed step by step instructions describing how to
    build and install this ROS2 driver
-   Refer to the README.md inside the package for more detailed
    up-to-date technical info on usage or
    [ Github repository](https://github.com/cubicleguy/ess_imu_ros1_spi_driver )

## SPI Connection & Configuration

\-\-\-\-\-\-\-\-\-\--

-   Since SPI interfaces are non-standard on PCs, typically IMU SPI
    interfacing is applicable only to embedded Linux platforms
-   When connecting the Epson device to a ROS2 system using the SPI
    interface:
-   direct connection to SPI port must be compatible with CMOS 3.3V I/O
-   connection between the host & Epson device is possible using the
    [M-G32EV031 evaluation breakout board](https://global.epson.com/products_and_drivers/sensing_system/technical_info/evaluation_tools/ )
-   This ROS2 driver uses the external library
    [Unofficial wiringPi library](https://github.com/WiringPi/WiringPi/ )
    to generate low level SPI communication & accurate time delays
-   Other libraries can be used to generate timer delays and SPI
    messages but requires minor changes to redirect the low-level
    function calls (i.e. bcm2835 C library, etc)
-   Accurate timing delays are necessary to optimize throughput for high
    *dout_rate* when using the SPI interface (refer to IMU datasheets
    for timing specifications)

Below is an example IMU SPI connection when using a Raspberry Pi:

  -- ------------------- -- -------------------------------- --
     **Epson IMU**          **Raspberry Pi**                 
     EPSON_RESET Input      RPI_GPIO_P1_15 (GPIO22) Output   
     EPSON_DRDY Output      RPI_GPIO_P1_18 (GPIO24) Input    
     EPSON_CS Input         RPI_GPIO_P1_16 (GPIO23) Output   
     EPSON_SCLK Input       RPI_GPIO_P1_23 (GPIO11) Output   
     EPSON_DOUT Output      RPI_GPIO_P1_19 (GPIO10) Input    
     EPSON_DIN Input        RPI_GPIO_P1_21 (GPIO9) Output    
  -- ------------------- -- -------------------------------- --

### Support for Timer Delays

-   There are wrapper functions for time delays in millisecond and
    microseconds using seDelayMS() and seDelayMicroSecs(), respectively.
-   On embedded Linux platforms, these may need to be redirected to
    platform-specific HW delay routines if not using a RaspberryPi
-   For example on RaspberryPi, the time delay functions for millisecond
    and microseconds is redirected to WiringPi library delay() and
    delayMicroseconds() function calls, respectively.
-   If a hardware delay is not available from a library, then a software
    delay loop is possible, but not preferred

### Support for GPIO Control

-   3 GPIO pins on the host are designated used and should be connected
    to the IMU
-   GPIO output for asserting CS# on the IMU (NOTE: Not using pin
    SPI0_CE0)
-   GPIO output for asserting RESET# on the IMU
-   GPIO input for reading the logic status on the IMU DRDY (GPIO1) pin
-   The use of GPIO pins for connecting to the IMU CS# and DRDY is
    mandatory
-   RESET# is recommended to force Hardware Reset during every IMU
    initialization for better robustness.

## ROS2 Node

\-\-\-\-\-\-\-\-\-\-\--

-   This ROS2 driver publishes IMU messages as per
    [ REP 145 Conventions for IMU Sensor Drivers](http://www.ros.org/reps/rep-0145.html )
-   [sensor_msgs/Imu](sensor_msgs/Imu) - contains header, orientation,
    angular velocity and linear acceleration

### Published Topics

-   This ROS driver publishes IMU messages as per
    [ REP 145 Conventions for IMU Sensor Drivers](http://www.ros.org/reps/rep-0145.html )
-   [sensor_msgs/Imu](sensor_msgs/Imu) - contains header, orientation,
    angular velocity and linear acceleration

### Launch File

-   The
    [ launch file](https://docs.ros.org/en/foxy/Tutorials/Launch-Files/Creating-Launch-Files.html?highlight=launch )
    in the launch folder of this package is used to pass the init
    parameters to configure the IMU at runtime using ros2 launch
-   Changes to init parameters by editing the launch file does not
    require rebuilding with *colcon build*
-   **Typically, the user only needs to modify *imu_dout_rate* &
    *imu_filter_sel* as needed based on system requirements**
-   Only use the specific IMU model launch file associated with the same
    IMU model built using *colcon build*

### Timestamping With EXT Signal

-   The G3xx series Epson IMU has 3.3V I/O EXT (GPIO2) pin which can be
    connected to a cyclic external sync signal such as a GNSS 1PPS
    signal
-   When the init parameter *time_correction* is enabled (including
    *ext_sel* set to *reset counter* & *count_out enabled*)
-   The ROS2 driver attempts to correct the time stamp field in
    [sensor_msgs/Imu](sensor_msgs/Imu) based on the reset counter value
    (measured delay since latest GNSS 1PPS)
-   This should give a more accurate timestamp of the inertial data by
    minimizing the effects of link delays or host processing overhead
    delays

## Building & Installing ROS2 Node

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

1\. Place this package (including folders) into a new folder within your
colcon workspace \"src\" folder.

2\. Modify the [ CMakeLists.txt](CMakeLists.txt ) to select the desired
Epson IMU model that is being used in the ROS2 system.

-   Refer to the comment lines inside the
    [ CMakeLists.txt](CMakeLists.txt ) for additional info.
-   **NOTE: You \*MUST\* re-build using colcon when changing IMU models
    or any changes in the [ CMakeLists.txt](CMakeLists.txt )**

3\. From the colcon workspace folder run \"colcon build\" to build all
changed ROS2 packages located in the \<colcon_workspace\>/src/ folder.

4\. Reload the current ROS2 environment variables that may have changed
after the colcon build process.

```
From the <colcon_workspace>: . install/setup.bash
```

5\. Modify the appropriate
[ launch file](https://docs.ros.org/en/foxy/Tutorials/Launch-Files/Creating-Launch-Files.html?highlight=launch )
to set your desired IMU init parameters for the specific IMU model in
the launch folder that you selected and built

-   **Typically, only the *imu_dout_rate* & *imu_filter_sel* needs to be
    edited**

## Running the ROS2 Node

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   To start the Epson IMU ROS2 driver use the appropriate
    [ launch file](https://docs.ros.org/en/foxy/Tutorials/Launch-Files/Creating-Launch-Files.html?highlight=launch )
    (located in launch/) with
    [ ros2 launch](https://design.ros2.org/articles/roslaunch.html )

```{=html}
<!-- -->
```
-   For example, for the Epson G370 IMU:

```
<colcon_workspace>/roslaunch ess_imu_ros2_spi_driver epson_g370.launch
```

## Technical Support

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   For technical support or related issues using this ROS software,
    please email sensingsystem_support@ea.epson.com
