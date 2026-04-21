# Epson IMU ROS2 Driver Node

\-\-\-\-\-\-\-\-\-\-\--
![\|align="right"](attachment:ess_sensors/g552.jpg)
![\|align="right"](attachment:ess_sensors/g370.jpg)
![\|align="right"](attachment:ess_sensors/g365.jpg)

## Overview

\-\-\-\-\-\-\-\-\-\-\--

-   The [ Epson IMU ROS software](ess_sensors ) is ROS2 C++ wrapper of a
    Linux C driver for communicating on a ROS2 system
-   The original Linux C driver can be found at
    [ github](https://github.com/cubicleguy/imu_linux_example )
-   This driver software supports either UART or SPI interface
    connection to the Epson device
-   The user should be familiar with building ROS2 packages using the
    *colcon build* process
-   This is **NOT** detailed step by step instructions
-   Refer to the README.md inside the ROS package or
    [ Github repository](https://github.com/cubicleguy/ess_imu_driver2 )
    for more detailed up-to-date info

## Interface Connections

\-\-\-\-\-\-\-\-\-\-\--

### UART Connection & Configuration

-   For direct connection, the target UART port on the host must be
    compatible with CMOS 3.3V I/O
-   Connection is also possible through a USB-UART 3.3V converter IC
    such as on the
    [M-G32EV041 evaluation board](https://global.epson.com/products_and_drivers/sensing_system/technical_info/evaluation_tools/ )
-   Connecting GPIO output for asserting RESET# pin on the Epson device
    is optional, but recommended where possible (i.e. on embedded
    platforms)
-   Below is an example UART connection when using a Raspberry Pi based
    system:

  -- ------------------- -- -------------------------------------------------------------- --
     **Epson IMU**          **Raspberry Pi**                                               
     EPSON_SIN Input        RPI_GPIO_P1_8 (GPIO14/UART_TXD) Output                         
     EPSON_SOUT Output      RPI_GPIO_P1_10 (GPIO15/UART_RXD) Input                         
     EPSON_RESET Input      RPI_GPIO_P1_15 (GPIO22) Output \*Optional, but recommended\*   
  -- ------------------- -- -------------------------------------------------------------- --

-   When connecting the Epson G552PRx to a ROS system, the underlying
    UART connection must be compatible with RS422 I/O signal levels
-   Below is an example RS422 connection to a RS422 Host:

  -- ------------------ -- ----------------- --
     **Epson IMU**         **RS422 Host**    
     EPSON_TD+ Output      HOST_RD+ Input    
     EPSON_TD- Output      HOST_RD- Input    
     EPSON_RD+ Input       HOST_TD+ Output   
     EPSON_RD- Input       HOST_TD- Output   
  -- ------------------ -- ----------------- --

### SPI Connection & Configuration

-   Interfacing the Epson device using SPI is typically applicable only
    to embedded Linux platforms
-   Direct connection to SPI port must be compatible with CMOS 3.3V I/O
-   Connection between the host & Epson device is possible using the
    [ M-G32EV031 evaluation breakout board](https://global.epson.com/products_and_drivers/sensing_system/technical_info/evaluation_tools/ )
-   This driver uses the \[<https://github.com/WiringPi/WiringPi/>
    \|Unofficial wiringPi library\]\] to generate low level SPI
    communication & accurate time delays
-   Other libraries can be used to generate timer delays and SPI
    messages but requires changes to redirect the low-level function
    calls
-   Accurate timing delays are necessary to ensure throughput for high
    *imu_dout_rate* (refer to IMU datasheets for timing specifications)
-   Below is an example SPI connection when using a Raspberry Pi:

  -- ------------------- -- -------------------------------- --
     **Epson IMU**          **Raspberry Pi**                 
     EPSON_RESET Input      RPI_GPIO_P1_15 (GPIO22) Output   
     EPSON_DRDY Output      RPI_GPIO_P1_18 (GPIO24) Input    
     EPSON_CS Input         RPI_GPIO_P1_16 (GPIO23) Output   
     EPSON_SCLK Input       RPI_GPIO_P1_23 (GPIO11) Output   
     EPSON_DOUT Output      RPI_GPIO_P1_19 (GPIO10) Input    
     EPSON_DIN Input        RPI_GPIO_P1_21 (GPIO9) Output    
  -- ------------------- -- -------------------------------- --

### SPI Configuration for Timer Delays

-   This software contains wrapper functions for time delays in
    millisecond and microseconds using **seDelayMS()** and
    **seDelayMicroSecs()**, respectively.
-   On embedded Linux platforms, these function calls are redirected to
    platform-specific HW delay routines
-   For example on RaspberryPi, the time delay functions for millisecond
    and microseconds is redirected to WiringPi library **delay()** and
    **delayMicroseconds()**
-   If a hardware delay is not available from a library, then a custom
    software delay loop is an option (but not preferred)

### SPI Configuration for GPIO Control

-   This software uses the following 3 GPIO pins on the host for
    connection to the Epson device
-   GPIO output for asserting **CS#** on the Epson device (NOTE:
    Alternatively, pin SPI0_CE0 on the RaspberryPi can be used)
-   GPIO input for reading the logic status on the Epson device **DRDY**
    (GPIO1) pin
-   GPIO output for asserting **RESET#** on the Epson device
-   Connecting **CS#** and **DRDY** to the Epson device is mandatory
-   **RESET#** is recommended for asserting Hardware Reset during every
    initialization for better robustness

## ROS2 Node

\-\-\-\-\-\-\-\-\-\-\--

-   This ROS2 driver publishes IMU messages as per
    [ REP 145 Conventions for IMU Sensor Drivers](http://www.ros.org/reps/rep-0145.html )
-   [ Imu Message](https://docs.ros.org/en/api/sensor_msgs/html/msg/Imu.html ) -
    contains header, orientation, angular velocity and linear
    acceleration
-   [ Temperature Message](https://docs.ros.org/en/api/sensor_msgs/html/msg/Temperature.html ) -
    contains header, temperature in Degrees Celsius

### Orientation Data

-   For models that support *quaternion output*,
    [ Imu Message](https://docs.ros.org/en/api/sensor_msgs/html/msg/Imu.html )
    publish on **imu/data**, and the orientation field can update with
    valid data
-   For models that **do not** support *quaternion output*,
    [ Imu Message](https://docs.ros.org/en/api/sensor_msgs/html/msg/Imu.html )
    publish on **imu/data_raw**, and the orientation field will not
    update with valid data

### Launch File

-   The
    [ python launch files](https://docs.ros.org/en/foxy/Tutorials/Launch-Files/Creating-Launch-Files.html?highlight=launch )
    in the launch folder is used to pass the initialization parameters
    to configure the Epson device at runtime using *ros2 launch*
-   Initialization parameter changes by editing the launch file does not
    require rebuilding with *colcon*
-   The user needs to modify **imu_dout_rate** & **imu_filter_sel** as
    needed based on user requirements

### Timestamping With EXT Signal (Time Correction)

-   The Epson device has a 3.3V I/O EXT (GPIO2) pin which can be
    connected to a cyclic external sync signal such as a GNSS 1PPS
    signal
-   When **time_correction_en** is enabled (set to true), the driver
    attempts to correct the time stamp field in
    [ Imu Message](https://docs.ros.org/en/api/sensor_msgs/html/msg/Imu.html )
    using the devices internal reset counter value (measured time delay
    since latest GNSS 1PPS)



```
DeclareLaunchArgument(
                name="time_correction_en",
                default_value="false",
                description="Enables using IMU external counter reset function for timestamp with external 1PPS connected to IMU input pin for GPIO2/EXT",
            ),
```



-   The use of **time_correction_en** is intended to give a more
    accurate timestamp of the inertial data by minimizing the effects of
    link and host processing delays

### Building & Installing ROS2 Node

1\. Place this package (including folders) into a new folder within your
colcon workspace *src*/ folder.

2\. Modify the **CMakeLists.txt** to:

-   Select the **PLATFORM** to *NONE* for PC or *RPI* for RaspberryPi
    depending on your host platform
-   Select the **INTERFACE** to *UART* or *SPI* depending on the serial
    connection
-   **NOTE:** You \*MUST\* re-build using *catkin_make* when changing
    the **PLATFORM** or **INTERFACE** or making any changes in the
    **CMakeLists.txt**

3\. From the colcon workspace folder run *colcon build* to build all
changed ROS2 packages located in the <colcon_workspace>/src/ folder

4\. Reload the current ROS2 environment variables that may have changed
after the colcon build process.



```
From the <colcon_workspace>/source install/setup.bash
```



5\. Modify the appropriate
[ launch file](https://docs.ros.org/en/foxy/Tutorials/Launch-Files/Creating-Launch-Files.html?highlight=launch )
in the launch folder to set your desired initialization parameters

-   Typically, only the **imu_dout_rate** & **imu_filter_sel** needs to
    be edited

### Running the ROS2 Node

-   To start the Epson IMU ROS2 driver use the appropriate
    [ launch file](https://docs.ros.org/en/foxy/Tutorials/Launch-Files/Creating-Launch-Files.html?highlight=launch )
    located in *launch*/ with
    [ ros2 launch](https://design.ros2.org/articles/roslaunch.html )

```{=html}
<!-- -->
```
-   For example:



```
<colcon_workspace>/ros2 launch ess_imu_driver2 launch.py
```



## USB-UART Latency

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   When using USB-UART bridge ICs to connect between the Linux host &
    Epson device, higher than expected latencies or slower than expected
    data rates are possible
-   For example, the
    [M-G32EV041 evaluation board](https://global.epson.com/products_and_drivers/sensing_system/technical_info/evaluation_tools/ )
    uses an FTDI IC and driver
-   If the connection between the Epson device UART and Linux host is by
    FTDI, the **latency_timer** setting in the FTDI Linux driver may be
    large i.e. typically 16 (msec)
-   There are 3 methods listed below to reduce the impact of this
    latency by setting the **latency_timer** to 1msec

### Modifying \*latency_timer\* by \*udev\* mechanism

-   \[\[<https://wiki.debian.org/udev>\] \| udev\]\] is a device manager
    for Linux that can dynamically create and remove devices in
    \*userspace\* and run commands when new devices appear
-   Create a \*udev\* rule to automatically set the **latency_timer** to
    1 when an FTDI USB-UART device is plugged in
-   For example, below is a text file named \*99-ftdi_sio.rules\* that
    can be put in the \*/etc/udev/rules.d\* directory
    

```
SUBSYSTEM=="usb-serial", DRIVER=="ftdi_sio", ATTR{latency_timer}="1"
```



**NOTE:** Root (sudo) access is required to create or copy file in
\*/etc/udev/rules.d\* **NOTE:** This is the preferred method because it
automatically triggers when the device is plugged in. However, it
affects **ALL FTDI USB-UART** devices on the host system

### Modifying \*latency_timer\* by \*sysfs\* mechanism

-   The example below reads the \*latency_timer\* setting for
    \*/dev/ttyUSB0\* which returns 16msec.
-   Then, it sets the \*latency_timer\* to 1msec, and confirms it by
    readback.
    -   NOTE:** May require root (sudo su) access on your system**



```
cat /sys/bus/usb-serial/devices/ttyUSB0/latency_timer
16
echo 1 > /sys/bus/usb-serial/devices/ttyUSB0/latency_timer
cat /sys/bus/usb-serial/devices/ttyUSB0/latency_timer
1
```



### Modifying \*low_latency\* flag using \*setserial\* utility

-   The example below sets the *low_latency* flag for */dev/ttyUSB0*
-   This will have the same effect as setting the *latency_timer* to
    1msec.
-   This can be confirmed by running the *setserial* command again.
-   **NOTE:** You may need to install setserial with *sudo apt install
    setserial*



```
user@user:~$ setserial /dev/ttyUSB0
/dev/ttyUSB0, UART: unknown, Port: 0x0000, IRQ: 0

user@user:~$ setserial /dev/ttyUSB0 low_latency

user@user:~$ setserial /dev/ttyUSB0
/dev/ttyUSB0, UART: unknown, Port: 0x0000, IRQ: 0, Flags: low_latency
```



## Technical Support

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   For technical support or related issues using this ROS software,
    please email sensingsystem_support@ea.epson.com
