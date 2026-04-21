See also [rosserial/Overview](rosserial/Overview).

## Overview

This package contains all necessary extensions on
[rosserial_client](rosserial_client) to bring two Tiva C Launchpad
boards from [TI's Launchpad ecosystem](http://www.ti.com/launchpad) to
ROS. All boards can use both debug USB and device USB to communicate
with rosserial.

-   EK-TM4C123GXL
-   EK-TM4C1294XL

Due to changes in USB library of !TivaWare. **Compatible with
SW-TM4C-2.1.3.156 onwards**

This package contains the prepares the required libraries for Energia's
IDE and also prepares a build configuration for `catkin` packages
based on `arm-none-eabi` GNU compiler toolchain and TI's !TivaWare
libraries.

**Repositories:**

<https://github.com/vmatos/rosserial_tivac>

<https://github.com/vmatos/rosserial_tivac_tutorials>

## Tutorials

The [Tutorials](rosserial_tivac/Tutorials) page of this package will
walk you through the steps for setting up your environment, and
demonstrate how to develop applications, both for Energia and catkin.

## Resources used

Some resources are strictly required to enable rosserial communication
with your ROS computer. On your application, you must pay attention not
to disable or change the peripherals configuration.

The !SystemTick interrupt service must be available for
`rosserial_tivac` to use, so it can keep the execution time.

`rosserial_tivac` will communicate either through UART0 or USB0:

-   **UART0** which is connected directly to the ICDI device of the
    board, available as USB serial converter on the debug USB port.
-   **USB0** which behaves as CDC USB device over the device USB port.

If you use rosserial over UART0, you are free to use USB0. Or if you use
rosserial over USB0, you have available UART0.

No more resources are required. Optionally two LEDs are used to indicate
the passing of time, and the communication activity over the serial
line.

## CMakeLists.txt (not for Energia projects)

After going through the [Tutorials](rosserial_tivac/Tutorials) you
should have understood that each project requires a `CMakeLists.txt`
which calls the function `generate_tivac_firmware` to prepare the
build files.

This function requires two environment variables:

-   `TIVA_WARE_PATH` - TI !TivaWare SDK path
-   `TIVA_FLASH_EXECUTABLE` - lm4flash tool executable

And takes the arguments:

-   USB - Optional argument, if you wish to have rosserial over USB CDC
    device.
-   DEVICE_SILICON - Optional argument. e.g.
    ```TARGET_IS_TM4C123_RB1``` Defines the specific chip's
    silicon revision.
-   DEVICE_SERIAL - Optional argument. Creates flash target for specific
    device.
-   BOARD - Required. Takes one argument, tm4c123gxl or tm4c1294xl.
-   STARTUP - Optional argument. Takes the name of custom startup file.
-   SRCS - Required. List of source files to compile.
-   INCS - Optional. List of include directories.
-   LIBS - Optional. List of libraries to be linked.

And creates custom targets for project:

-   <parent_catkin_project>_\${CMAKE_PROJECT_NAME}.axf - Build binary
    file
-   <parent_catkin_project>_\${CMAKE_PROJECT_NAME}_flash - Flashes
    board with binary file
-   <parent_catkin_project>_\${CMAKE_PROJECT_NAME}_size - Prints out
    the size of sections and totals of binary file
-   <parent_catkin_project>_\${CMAKE_PROJECT_NAME}_dump - Prints
    table of symbols and such

Example: ```
generate_tivac_firmware(
  USB
  STARTUP custom_startup.c
  SRCS buttons.cpp buttons.c
  INCS .
  BOARD tm4c123gxl
)
``` This example sets rosserial
communication through USB CDC device. Add two source files to be
compiled on the project and includes the project directory. It will
compile the project for tm4c123gxl board.

If for any particular reason, the author of the projects also needs to
specify on the interrupt vector some interrupt handlers, he is able to
specify a custom startup file.
