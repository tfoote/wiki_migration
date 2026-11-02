See also [rosserial/Overview](https://index.ros.org/p/rosserial).

## Overview

This package contains all necessary extensions on
[rosserial_client](https://index.ros.org/p/rosserial_client) to bring
two Tiva C Launchpad boards from
[TI's Launchpad ecosystem](http://www.ti.com/launchpad) to ROS. All
boards can use both debug USB and device USB to communicate with
rosserial.

- EK-TM4C123GXL
- EK-TM4C1294XL

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

The [Tutorials](#tutorials-1) page of this
package will walk you through the steps for setting up your environment,
and demonstrate how to develop applications, both for Energia and
catkin.

## Resources used

Some resources are strictly required to enable rosserial communication
with your ROS computer. On your application, you must pay attention not
to disable or change the peripherals configuration.

The !SystemTick interrupt service must be available for
`rosserial_tivac` to use, so it can keep the execution time.

`rosserial_tivac` will communicate either through UART0 or USB0:

- **UART0** which is connected directly to the ICDI device of the board,
  available as USB serial converter on the debug USB port.
- **USB0** which behaves as CDC USB device over the device USB port.

If you use rosserial over UART0, you are free to use USB0. Or if you use
rosserial over USB0, you have available UART0.

No more resources are required. Optionally two LEDs are used to indicate
the passing of time, and the communication activity over the serial
line.

## CMakeLists.txt (not for Energia projects)

After going through the
[Tutorials](#tutorials-1) you should have
understood that each project requires a `CMakeLists.txt` which calls
the function `generate_tivac_firmware` to prepare the build files.

This function requires two environment variables:

- `TIVA_WARE_PATH` - TI !TivaWare SDK path
- `TIVA_FLASH_EXECUTABLE` - lm4flash tool executable

And takes the arguments:

- USB - Optional argument, if you wish to have rosserial over USB CDC
  device.
- DEVICE_SILICON - Optional argument. e.g.
  ```TARGET_IS_TM4C123_RB1``` Defines the specific chip's silicon
  revision.
- DEVICE_SERIAL - Optional argument. Creates flash target for specific
  device.
- BOARD - Required. Takes one argument, tm4c123gxl or tm4c1294xl.
- STARTUP - Optional argument. Takes the name of custom startup file.
- SRCS - Required. List of source files to compile.
- INCS - Optional. List of include directories.
- LIBS - Optional. List of libraries to be linked.

And creates custom targets for project:

- <parent_catkin_project>_\${CMAKE_PROJECT_NAME}.axf - Build binary
  file
- <parent_catkin_project>_\${CMAKE_PROJECT_NAME}_flash - Flashes
  board with binary file
- <parent_catkin_project>_\${CMAKE_PROJECT_NAME}_size - Prints out
  the size of sections and totals of binary file
- <parent_catkin_project>_\${CMAKE_PROJECT_NAME}_dump - Prints table
  of symbols and such

Example: 

```
generate_tivac_firmware(
  USB
  STARTUP custom_startup.c
  SRCS buttons.cpp buttons.c
  INCS .
  BOARD tm4c123gxl
)
```

 This example sets rosserial
communication through USB CDC device. Add two source files to be
compiled on the project and includes the project directory. It will
compile the project for tm4c123gxl board.

If for any particular reason, the author of the projects also needs to
specify on the interrupt vector some interrupt handlers, he is able to
specify a custom startup file.

## Tutorials

See also Overview.

- [Energia IDE Setup](#energia-ide-setup):
  This tutorial shows step-by-step instruction on how setting up Energia
  IDE.
- [TivaWare Setup for catkin build](#tivaware-setup-for-catkin-build):
  This tutorial shows step-by-step how to setup up TI's Tivaware SDK
- [Hello world publisher on TM4C123GXL](#hello-world-publisher-on-tm4c123gxl):
  Chatter publisher for the EK-TM4C123GXL board using UART over debug
  USB port.
- [Hello world publisher on TM4C1294XL.](#hello-world-publisher-on-tm4c1294xl):
  Chatter publisher for the EK-TM4C1294XL board using UART over debug
  USB port.
- [Buttons publisher](#buttons-publisher):
  Buttons state publisher for the EK-TM4C123GXL board over CDC USB
  device.
- [RGB subscriber](#rgb-subscriber):
  EK-TM4C123GXL board over CDC USB device subscribes to ColorRGB msg
  type and change LED color.
- [RGB service](#rgb-service):
  EK-TM4C123GXL board over CDC USB device provides a custom message
  service for changing LED color.

## Energia IDE Setup

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [ROS Tutorials](ROS/Tutorials).
- **Description:** This tutorial shows step-by-step instruction on how
  setting up Energia IDE.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [TivaWare Setup](#tivaware-setup-for-catkin-build)

### Introduction

Energia IDE is provided by [TI](http://www.ti.com/) with the goal of
helping people use and program TI's Launchpad ecosystem of evaluation
boards. Energia is based on Arduino IDE which will be familiar to an
avid Arduino user.

The following steps are very similar to the ones required to setup
['rosserial_arduino'](https://index.ros.org/p/rosserial_arduino).

Only the following boards are compatible with `rosserial_tivac`:

- EK-TM4C123GXL
- EK-TM4C1294XL

With Energia IDE, only UART over the debug USB port is able to
communicate with ROS.

### Download and install Energia IDE

If you haven't already, you must download and install Energia IDE on
your system.

**Download and instructions:** [Energia IDE](http://energia.nu/)

Before continuing to the next steps, be certain you can compile and
upload sketches to your boards.

### Install rosserial_tivac

You can install `rosserial_tivac` from source, either using the
remaining `rosserial` pacakges from debs or from source.

Follow one of the two options: 1. rosserial_tivac from source +
rosserial binaries 2. rosserial_tivac + rosserial from source

#### rosserial_tivac from source + rosserial binaries

`rosserial_tivac` can be found on the repository:
<https://github.com/vmatos/rosserial_tivac>

Make sure you have `rosserial` package installed, either from binaries
or source.

##### Installing rosserial binaries

Example of how to install rosserial packages in binary form for Jade.



```
sudo apt-get install ros-jade-rosserial ros-jade-rosserial-msgs ros-jade-rosserial-client ros-jade-rosserial-python
```



##### Download and build rosserial_tivac

Navigate to your ROS workspace. Clone the git repository. Then build and
install the package.



```
cd <workspace_dir>/src
git clone https://github.com/vmatos/rosserial_tivac.git
cd <workspace_dir>
catkin_make
catkin_make install
```



#### rosserial_tivac + rosserial from source

Make sure you don't have any `rosserial` to avoid conflicts between
packages. 

```
sudo apt-get remove ros-jade-rosserial ros-jade-rosserial-msgs ros-jade-rosserial-client ros-jade-rosserial-python
```



##### Download and build rosserial_tivac

Navigate to your ROS workspace. Clone the git repository. Then build and
install the package.



```
cd <workspace_dir>/src
git clone https://github.com/ros-drivers/rosserial.git
cd <workspace_dir>
catkin_make
catkin_make install
```



#### Prepare rosserial libraries for Energia

Now you have to prepare the libraries required for Energia to compile
sketches with ROS enabled communication.

Add the installed `rosserial_tivac` to path. Or add the command to
`.bashrc`.



```
source <workspace_dir>/install/setup.bash
```

 Navigate to your Energia sketches directory and
prepare the libraries.



```
cd <sketches_dir>
cd libraries
rosrun rosserial_tivac make_libraries_energia .
```

 This step should execute without any errors.
You're now ready to test the demo sketches.

### Test it up

Restart Energia IDE for it to find the new installed libraries. The
installed libraries come with two examples.

1\. `chatter`: publishes 'hello world!' message over and over. 2.
`rgb`: subscribes to ColorRGBA message and changes LED color. Only for
EK-TM4C123GXL board.

![align="middle"](doc/energia_ide.png)

#### Uploading the example code

To upload the code to your Tiva C Launchpad, use the upload function
within the IDE. This is no different from uploading any other sketch.

#### Running a published code

Now, launch the [roscore](roscore) in a new terminal window:



```
roscore
```

 Next, run the rosserial client application that
forwards your Launchpad messages to the rest of ROS. Make sure to use
the correct serial port:



```
rosrun rosserial_python serial_node.py /dev/ttyUSB0
```

 Finally, watch the greetings come in from your
Launchpad by launching a new terminal window and entering :



```
rostopic echo chatter
```



#### Running a subscriber code

Stop the running hello world example and the rosserial message
forwarder, upload the code to Launchpad and launch the message forwarder
again:



```
rosrun rosserial_python serial_node.py /dev/ttyUSB0
```

 Now, you can toggle the LED using
[rostopic](https://index.ros.org/p/rostopic):



```
rostopic pub led std_msgs/ColorRGBA "r: 0.0
g: 0.0
b: 1.0
a: 1.0"
```

 The LED should turn blue. Change the r,g,b
values between \[0,1\] and check the colors. The 'a' value corresponds
to transparency which in this case means color intensity.

### Next tutorials

If you wish to use Energia to develop your applications, you can simply
follow the same tutorial as the Arduino ones, taking into account the
board layout is different.

[Hello World](https://index.ros.org/p/rosserial_arduino)

## TivaWare Setup for catkin build

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [ROS Tutorials](ROS/Tutorials).
- **Description:** This tutorial shows step-by-step how to setup up
  TI's Tivaware SDK
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [Hello world publisher for EK-TM4C123GXL](#hello-world-publisher-on-tm4c123gxl)

### Introduction

Energia IDE is great for quick development of TivaC applications.
However on bigger projects it can become cumbersome or unmanageable.

This tutorial assumes you already have set up a cross-compilation
environment based on `arm-none-eabi` GNU toolchain and TivaWare
libraries on Linux, and already are completly comfortable compiling and
flashing your applications.

**Compatible with SW-TM4C-2.1.1.71 onwards**

Only the following boards are compatible with `rosserial_tivac`:

- EK-TM4C123GXL
- EK-TM4C1294XL

### Setting up cross-compilation environment

Here are some quick steps to configure your toolchain if you haven't
already. These instruction are not extensive by any means. You may run
into problems, errors and incompatibilities.

#### Obtain your GNU toolchain for ARM Cortex-M & Cortex-R processors.



```
sudo add-apt-repository ppa:team-gcc-arm-embedded/ppa
sudo apt-get update
sudo apt-get install gcc-arm-embedded
```



#### Get the flashing tool

##### Build and install



```
git clone https://github.com/utzig/lm4tools.git
cd lm4tools/lm4ﬂash
make
sudo cp lm4flash /usr/local/bin
```



##### Add rules for USB devices

If you haven't already done so, you have to add device rules.



```
echo 'ATTRS{idVendor}=="1cbe", ATTRS{idProduct}=="00fd", GROUP="users", MODE="0660"' | \
sudo tee /etc/udev/rules.d/99-stellaris-launchpad.rules
```



#### Download and extract TivaWare

Download `SW-TM4C: TivaWare for C Series Software (Complete)` from
[TI's website](http://www.ti.com/tool/sw-tm4c).

Extract it to directory of your choosing. Example:



```
mkdir <TivaWarePah>
cd <TivaWarePah>
mv <directory_downloaded>/SW-TM4C-2.1.1.71.exe
unzip SW-TM4C-2.1.1.71.exe
rm SW-TM4C-2.1.1.71.exe
```



#### Test cross-compilation and flashing

Navigate into one of the example projects and build a test project.



```
cd <path_to_tivaware>/examples/boards/ek-tm4c123gxl/blinky
make
lm4flash gcc/blinky.bin
```

 If no error occurred so far, you can continue
the guide.

### Set up environment variables

`rosserial_tivac` uses two environment variables to find Tivaware path
and the flash tool.

In your `.bashrc` set the variables:



```
export TIVA_WARE_PATH=$HOME/<path_to_tivaware_root>
export TIVA_FLASH_EXECUTABLE=lm4flash
```



And run:



```
source .bashrc
```



### Install rosserial_tivac

You can install `rosserial_tivac` from source, either using the
remaining `rosserial` pacakges from debs or from source.

Follow one of the two options: 1. rosserial_tivac from binaries 2.
rosserial_tivac from source + rosserial binaries

#### rosserial and rosserial_tivac from ROS repositories

Example of how to install rosserial packages in binary form for Jade.



```
sudo apt-get install ros-jade-rosserial ros-jade-rosserial-msgs ros-jade-rosserial-client ros-jade-rosserial-python ros-jade-rosserial-tivac
```



#### rosserial_tivac from source + rosserial binaries

`rosserial_tivac` can be found on the repository:
<https://github.com/vmatos/rosserial_tivac>

Make sure you have `rosserial` package installed, either from binaries
or source.

##### Installing rosserial binaries

Example of how to install rosserial packages in binary form for Jade.



```
sudo apt-get install ros-jade-rosserial ros-jade-rosserial-msgs ros-jade-rosserial-client ros-jade-rosserial-python
```



##### Download and build rosserial_tivac

Navigate to your ROS workspace. Clone the git repository. Then build and
install the package.



```
cd <workspace_dir>/src
git clone https://github.com/vmatos/rosserial_tivac.git
cd <workspace_dir>
catkin_make
catkin_make install
```



### Next tutorials

If you've reach this point without encountering any error, you can now
proceed to get hold of the `rosserial_tivac_tutorials` package.

#### Install from source rosserial_tivac_tutorials

Build the package.



```
cd <workspace_dir>/src
git clone https://github.com/vmatos/rosserial_tivac_tutorials.git
cd <workspace_dir>
catkin_make rosserial_tivac_tutorials_generate_messages
source devel/setup.bash
catkin_make
```

 Carry on with the remaining tutorials:
[Hello world publisher](#hello-world-publisher-on-tm4c123gxl).

### Addendum: Tivaware USB library bug

At time of writing, Tivaware contains a known bug on its USB libraries.
The author of this guide is not aware to what extent the bug affects the
communication abilities with ROS.

On the file which implements the USB ring buffer:
`usblib/usbbuffer.c`, one reads:



```
USBBufferInfoGet(const tUSBBuffer *psBuffer, tUSBRingBufObject *psRingBuf)
    (...)
        psRingBuf->ui32Size = psBufVars->sRingBuf.ui32ReadIndex;
```

 And should be:



```
psRingBuf->ui32Size = psBufVars->sRingBuf.ui32Size;
```

## Hello world publisher on TM4C123GXL

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Tivaware and toolchain setup](#tivaware-setup-for-catkin-build).
- **Description:** Chatter publisher for the EK-TM4C123GXL board using
  UART over debug USB port.
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [Hello world publisher on TM4C1294XL](#hello-world-publisher-on-tm4c1294xl)

### Introduction

This tutorial will take you step-by-step on how to set up your TivaC
project on a catkin package using `rosserial_client` and
`rosserial_tivac`.

All these tutorials are available on the
[repository](https://github.com/robosavvy/rosserial_tivac_tutorials).

### Create your project

On your catkin workspace we'll create a new package.


```
catkin_create_pkg rosserial_tivac_tutorials rosserial_tivac rosserial_client std_msgs
```

 Since you're completely familiar with ROS, you
know this command will create a new package on your workspace with the
name `rosserial_tivac_tutorials`. We're establishing a dependency on
`rosserial_tivac` for the required libraries and `rosserial_client`
for the client build macros. `std_msgs` is also required since we use
these messages on our examples.

**package.xml**

Your package.xml should look like: 

```xml
<?xml version="1.0"?>
<package>
  <name>rosserial_tivac_tutorials</name>
  <version>0.0.0</version>
  <description>The rosserial_tivac_tutorials package</description>
  <maintainer email="todo@todo.todo">todo</maintainer>
  <license>TODO</license>

  <buildtool_depend>catkin</buildtool_depend>
  
  <build_depend>rosserial_client</build_depend>
  <build_depend>rosserial_tivac</build_depend>  
  <build_depend>std_msgs</build_depend>
  
  <run_depend>rosserial_client</run_depend>
  <run_depend>rosserial_tivac</run_depend>
  <run_depend>std_msgs</run_depend>
</package>
```



**CMakeLists.txt**

And your `CMakeLists.txt` file ought to contain the minimal dependency
definitions by now. 

```cplusplus
cmake_minimum_required(VERSION 2.8.3)
project(rosserial_tivac_tutorials)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  rosserial_client
  rosserial_tivac
  std_msgs
)
```



### Write your code

Create a new directory 'chatter' and a new file inside called
`chatter.cpp` with the following code: 

```cplusplus
#include <stdbool.h>
#include <stdint.h>
// TivaC specific includes
extern "C"
{
  #include <driverlib/sysctl.h>
  #include <driverlib/gpio.h>
}
// ROS includes
#include <ros.h>
#include <std_msgs/String.h>

// ROS nodehandle
ros::NodeHandle nh;

std_msgs::String str_msg;
ros::Publisher chatter("chatter", &str_msg);
char hello[13] = "Hello world!";

int main(void)
{
  // TivaC application specific code
  MAP_FPUEnable();
  MAP_FPULazyStackingEnable();
  // TivaC system clock configuration. Set to 80MHz.
  MAP_SysCtlClockSet(SYSCTL_SYSDIV_2_5 | SYSCTL_USE_PLL | SYSCTL_XTAL_16MHZ | SYSCTL_OSC_MAIN);

  // ROS nodehandle initialization and topic registration
  nh.initNode();
  nh.advertise(chatter);

  while (1)
  {
    // Publish message to be transmitted.
    str_msg.data = hello;
    chatter.publish(&str_msg);

    // Handle all communications and callbacks.
    nh.spinOnce();

    // Delay for a bit.
    nh.getHardware()->delay(100);
  }
}
```



#### Code explained

You should be familiar with developing C applications for these
evaluation boards by now. Very little changes from your typical Tiva C
application using Tivaware libraries. But we are now compiling a C++
application with use Tivaware C libraries. Like a typical ROS
application, we include the required headers. We then declare: 1. Our
one and only node handle. 2. The message to be published. 3. The
publisher with topic name `chatter`. 4. The string we're publishing.
These are MCU specific instructions to set up and configure the system.
Then the node is initialized, and any publisher, subscriber and service
should be added to the callback queue. Finally we trap the execution on
a infinite loop, with the node publishing the string "Hello world!"
when ros::spinOnce() is called, and all ROS communication callbacks are
handled.

### Revisiting CMakeLists.txt

Now it's time to include in our package's `CMakeLists.txt` file the
`rosserial_client` macros to generate ROS libraries for our target and
generate our catkin sub-project. 

```cplusplus
cmake_minimum_required(VERSION 2.8.3)
project(rosserial_tivac_tutorials)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  rosserial_client
  rosserial_tivac
  std_msgs
)

rosserial_generate_ros_lib(
  PACKAGE rosserial_tivac
  SCRIPT make_libraries_tiva
)

# Chatter tutorial
rosserial_configure_client(
  DIRECTORY chatter
  TOOLCHAIN_FILE ${ROSSERIAL_TIVAC_TOOLCHAIN}
)
rosserial_add_client_target(chatter chatter.axf ALL)
rosserial_add_client_target(chatter flash)
rosserial_add_client_target(chatter size)
rosserial_add_client_target(chatter dump)
```

 The
rosserial_generate_ros_lib function creates a target called which will
generate the rosserial client library, including messages headers.
Called `rosserial_tivac_tutorials_ros_lib`.
`rosserial_configure_client` will configure a new client subproject
`chatter` with the specified toolchain file, provided by the package
`rosserial_tivac`. Each `rosserial_add_client_target` will create a
specific target for the subproject `chatter`.

- `rosserial_tivac_tutorials_chatter_chatter.axf`: Build the project
  object file.
- `rosserial_tivac_tutorials_chatter_flash`: Creates the binary file
  and flashes it to the board.
- `rosserial_tivac_tutorials_chatter_size`: Prints the binary file
  size.
- `rosserial_tivac_tutorials_chatter_dumps`: Dumps the built object
  symbol table.

### Subproject's CMakeLists.txt

Let's continue developing our application by adding the subproject's
`CMakeLists.txt`.

Create a file `chatter/CMakeLists.txt` with the content:


```cplusplus
cmake_minimum_required(VERSION 2.8.3)
project(chatter)

# Include rosserial libraries for TivaC
include_directories(${ROS_LIB_DIR})

# Per project based definitions and options
add_definitions(-DLED_HEARTBEAT)
add_definitions(-DLED_COMM)
add_definitions(-DROSSERIAL_BAUDRATE=57600)
add_definitions(-DTX_BUFFER_SIZE=256)
add_definitions(-DRX_BUFFER_SIZE=256)

# Generate target for TivaC
generate_tivac_firmware(
  SRCS chatter.cpp
  BOARD tm4c123gxl
)
```



#### CMakeLists.txt explained

Defines the target's name. Includes the generated `ros_lib`
libraries, which are specific for TivaC. Optional defines. If you wish
to claim the use of the heartbeat LED and communications LED, you can
delete these defines. Baudrate definition when using communication
through the UART over debug USB port. If undefined, 57600 is assumed.
Size of UART buffers. The `generate_tivac_firmware` function provided
by `rosserial_tivac` package sets all the variables, libraries and
build rules for our application.

You need to specify:

- `SRCS`: The source files to be compiled on your application.
- `BOARD`: `tm4c123gxl` or `tm4c1294xl`

### Build & upload

#### Using catkin_make

Now we can build our application when we run `catkin`.


```
catkin_make rosserial_tivac_tutorials_chatter_chatter.axf
```



And also use the `catkin` target to flash the application.


```
catkin_make rosserial_tivac_tutorials_chatter_flash
```



#### Using catkin tools

Now we can build our application when we run `catkin`.


```
catkin build rosserial_tivac_tutorials
```



And also use the `catkin` target to flash the application.


```
catkin build --no-deps rosserial_tivac_tutorials --make-args rosserial_tivac_tutorials_chatter_flash
```



### Test

Let's listen to our newly created topic from TivaC.

Run `roscore`. 

```
roscore
```



Run `serial_node.py` from `rosserial_python`.


```
rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0
```



Watch the messages from the topic. 

```
rostopic echo /chatter
```



### Addendum

If there's a breakage you don't understand, a good first step is to
clean your workspace (delete build and devel trees), and then re-run in
verbose mode: 

```
catkin_make VERBOSE=1
```

## Hello world publisher on TM4C1294XL.

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Tivaware and toolchain setup](#tivaware-setup-for-catkin-build).
- **Description:** Chatter publisher for the EK-TM4C1294XL board using
  UART over debug USB port.
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [Buttons publisher](#buttons-publisher)

### Introduction

This tutorial is simply an extension of the previous
[Hello world publisher on TM4C123GXL](#hello-world-publisher-on-tm4c123gxl)
for the EK-TM4C1294XL board.

You can repeat the process over the previously created project. Or refer
to the reference project on `rosserial_tivac_tutorials/chatter129`.

### Source code



```cplusplus
(...)
  // TivaC system clock configuration. Set to 80MHz.
  MAP_SysCtlClockSet(SYSCTL_SYSDIV_2_5 | SYSCTL_USE_PLL | SYSCTL_XTAL_16MHZ | SYSCTL_OSC_MAIN);
(...)
```

 On `chatter/chatter.cpp` change these lines
to: 

```cplusplus
(...)
  // Run from the PLL at 120 MHz.
  MAP_SysCtlClockFreqSet((SYSCTL_XTAL_25MHZ | SYSCTL_OSC_MAIN |
                          SYSCTL_USE_PLL | SYSCTL_CFG_VCO_480), TM4C129FREQ);
(...)
```



This change is required due to the different mechanisms which both MCUs
use to control the system clock.

### CMakeLists.txt

Now let's change the application's `CMakeLists.txt` file.

Due to the difference on how the clock frequency is set up for the
TM4C129XL target, we need to add the frequency definition.


```
add_definitions(-DTM4C129FREQ=120000000)
```



And then change the target configuration by setting the board type.


```
generate_tivac_firmware(
  SRCS chatter.cpp
  BOARD tm4c1294xl
)
```



### Build, flash and test

Now we can build our application when we run `catkin` and then upload.


```
catkin_make rosserial_tivac_tutorials_chatter_chatter.axf
catkin_make rosserial_tivac_tutorials_chatter_flash
```



Let's listen to our newly created topic from TivaC.

Run `roscore`. 

```
roscore
```



On a new terminal, run `serial_node.py` from `rosserial_python`.


```
rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0
```



And watch the messages from the topic. 

```
rostopic echo /chatter
```

## Buttons publisher

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Tivaware and toolchain setup](#tivaware-setup-for-catkin-build).
- **Description:** Buttons state publisher for the EK-TM4C123GXL board
  over CDC USB device.
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [RGB subscriber](#rgb-subscriber)

### Introduction

This particular tutorial follows the same general steps as the previous
two.

However on this project we will use a custom message to publish the user
button state on the EK-TM4C123GXL.

Another change from the previous projects, is the use of the device USB
port. When connected to the computer, the board will enumerate as a CDC
usb device.

For this tutorial you must get the reference files which can be found on
`rosserial_tivac_tutorials`.

### Custom message generation

Let's create a new file message on the new directory
`msgs/Buttons.msg`. 

```
std_msgs/Bool sw1
std_msgs/Bool sw2
```



#### package.xml & CMakeLists.txt

On the package's package.xml and top level CMakeLists.txt we will add
new dependencies and rules to generate our new message.

##### package.xml

Add new dependencies on `package.xml`: 

```
<build_depend>message_generation</build_depend>  
  <run_depend>message_runtime</run_depend>
```



##### CMakeLists.xml

Add the new package `message_generation` dependency to
`find_package`: 

```
(...)
find_package(catkin REQUIRED COMPONENTS
  message_generation
  rosserial_client
  rosserial_tivac
  std_msgs
)
add_message_files(
  FILES Buttons.msg
)
generate_messages(
  DEPENDENCIES std_msgs
)
catkin_package(
  CATKIN_DEPENDS message_runtime std_msgs
)
(...)
```

 As well as instructions to
generate the new message files.

Also add the new subproject. 

```
(...)
# Custom message - Button publisher
rosserial_configure_client(
  DIRECTORY buttons
  TOOLCHAIN_FILE ${ROSSERIAL_TIVAC_TOOLCHAIN}
)
rosserial_add_client_target(buttons buttons.axf ALL)
rosserial_add_client_target(buttons flash)
rosserial_add_client_target(buttons size)
(...)
```



### Source code

Similarly to the previous tutorials, we'll create a publisher for the
new Buttons message. 

```cplusplus
#include <stdbool.h>
#include <stdint.h>
// TivaC specific includes
extern "C"
{
  #include <driverlib/sysctl.h>
  #include <driverlib/gpio.h>
  #include "buttons.h"
}
// ROS includes
#include <ros.h>
// Custom ROS message
#include "rosserial_tivac_tutorials/Buttons.h"

// ROS nodehandle
ros::NodeHandle nh;

rosserial_tivac_tutorials::Buttons button_msg;
ros::Publisher button_publisher("button_state", &button_msg);

int main(void)
{
  // TivaC application specific code
  MAP_FPUEnable();
  MAP_FPULazyStackingEnable();
  // TivaC system clock configuration. Set to 80MHz.
  MAP_SysCtlClockSet(SYSCTL_SYSDIV_2_5 | SYSCTL_USE_PLL | SYSCTL_XTAL_16MHZ | SYSCTL_OSC_MAIN);

  uint8_t button_debounced_delta;
  uint8_t button_raw_state;
  ButtonsInit();

  // ROS nodehandle initialization and topic registration
  nh.initNode();
  nh.advertise(button_publisher);

  while (1)
  {
    uint8_t button_debounced_state = ButtonsPoll(&button_debounced_delta, &button_raw_state);
    // Publish message to be transmitted.
    button_msg.sw1.data = button_debounced_state & LEFT_BUTTON;
    button_msg.sw2.data = button_debounced_state & RIGHT_BUTTON;
    button_publisher.publish(&button_msg);

    // Handle all communications and callbacks.
    nh.spinOnce();

    // Delay for a bit.
    nh.getHardware()->delay(100);
  }
}
```



Very few changes comparing to the "hello world" publisher. We now
include the header files corresponding to the Buttons message, and also
instantiate the message and publisher for the topic with name
`/button_state`. MCU specific code to set up the buttons' pins. On
the main loop, we read the button state using the function
`ButtonsPoll`, and with the result we fill up the message before
publishing.

The message is then queued when `.publish` is executed and transmitted
when `.spinOnce()` is called.

### Build & flash



```
catkin_make rosserial_tivac_tutorials_buttons_buttons.axf
catkin_make rosserial_tivac_tutorials_buttons_flash
```



### Test it up

Hold on! Don't forget to connect the device USB port to your computer!

You should be able to see the device under the name `/dev/ttyACM#`,
depending on how many devices you have connected.

Run `roscore` and `run serial_node.py` from `rosserial_python` on
the correct port `/dev/ttyACM#`. 

```
roscore
```




```
rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0
```

 

```
rostopic echo /button_state
```



Press any of the two buttons, and watch the output of the topic change.

## RGB subscriber

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Tivaware and toolchain setup](#tivaware-setup-for-catkin-build).
- **Description:** EK-TM4C123GXL board over CDC USB device subscribes to
  ColorRGB msg type and change LED color.
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [RGB service](#rgb-service)

### Introduction

Having created several publishers on the previous tutorials, its about
time we implement a subscriber.

Our application will subscribe to the topic `/led` and change the
color accordingly to the data on the ColorRGBA message.

### Source code explained



```cplusplus
#include <stdbool.h>
#include <stdint.h>
// TivaC specific includes
extern "C"
{
  #include <driverlib/sysctl.h>
  #include <driverlib/gpio.h>
  #include <rgb.h>
}
// ROS includes
#include <ros.h>
#include <std_msgs/ColorRGBA.h>

uint32_t current_color[3] = {0xFFFE, 0xFFFE, 0xFFFE};
float current_intensity = 1.f;
void color_cb(const std_msgs::ColorRGBA& msg)
{
  current_color[0] = msg.r * 0xFFFE;
  current_color[1] = msg.g * 0xFFFE;
  current_color[2] = msg.b * 0xFFFE;
  current_intensity = msg.a;
  RGBSet(current_color, current_intensity);
}

// ROS nodehandle and subscriber
ros::NodeHandle nh;
ros::Subscriber<std_msgs::ColorRGBA> rgb_sub("led", &color_cb);

int main(void)
{
  // TivaC application specific code
  MAP_FPUEnable();
  MAP_FPULazyStackingEnable();
  // TivaC system clock configuration. Set to 80MHz.
  MAP_SysCtlClockSet(SYSCTL_SYSDIV_2_5 | SYSCTL_USE_PLL | SYSCTL_XTAL_16MHZ | SYSCTL_OSC_MAIN);

  // Setup RGB driver
  RGBInit(0);
  RGBSet(current_color, current_intensity);

  // ROS nodehandle initialization and topic registration
  nh.initNode();
  nh.subscribe(rgb_sub);
  bool nh_prev_state = false;

  while (1)
  {
    // If subscribed, enable RGB driver
    if (nh.connected() && !nh_prev_state)
    {
      RGBEnable();
      nh_prev_state = true;
    }
    if (!nh.connected() && nh_prev_state)
    {
      RGBDisable();
      nh_prev_state = false;
    }

    // Handle all communications and callbacks.
    nh.spinOnce();

    // Delay for a bit.
    nh.getHardware()->delay(1000);
  }
}
```



Again, use the project `rgb_led` from `rosserial_tivac_tutorials
package as reference to follow the tutorial. As always, the node is
initiated and all the publishers and subscribers must be registered.
Here we instantiate a new subscriber on the topic `/led` of message
type `ColorRGBA`, handled by `color_cb` function. The callback
function will be executed for each new received message. It takes color
and intensity values in the range \[0 1\] and applies the color to the
board LED using the board specific library. Then execution is trapped
inside a loop, continuously waiting for new messages on the topic.

However the LED will only be enabled when a valid node connection is
present.

### Build and flash

By now you're an expert at this. Build and flash the binary file into
your board.



```
catkin_make
catkin_make rosserial_tivac_tutorials_rgb_led_flash
```



### Test it!

Don't forget to connect the device USB port to your computer!

Run `roscore` and `run serial_node.py` from `rosserial_python` on
the correct port `/dev/ttyACM#`. 

```
roscore
```

 When you
successfully connect using `serial_node the LED will light up.


```
rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0
```



On a new terminal window, publish a new color. 

```
rostopic pub /led std_msgs/ColorRGBA "r: 0.0
g: 1.0
b: 0.0
a: 1.0"
```



It should change to the brightest green.

## RGB service

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Tivaware and toolchain setup](#tivaware-setup-for-catkin-build).
- **Description:** EK-TM4C123GXL board over CDC USB device provides a
  custom message service for changing LED color.
- **Tutorial Level:** INTERMEDIATE

### Introduction

The last tutorial of this series will show you how to create a custom
service message and service server over rosserial.

The code relative to this tutorial can be found in the directory
`rgb_srv`.

### ColoRGBA service message

Let's analyze the message file found in `srv/ColorRGBA.srv`.


```
std_msgs/ColorRGBA color
---
bool result
```

 As a request we have a color field, of type
`std_msgs/ColorRGBA` and as response we get a `bool` result.

#### package.xml & CMakeLists.txt

On the package's package.xml and top level CMakeLists.txt we need
dependencies and rules to generate the new service message.

##### package.xml

Dependencies on `package.xml`: 

```
<build_depend>message_generation</build_depend>  
  <run_depend>message_runtime</run_depend>
```



##### CMakeLists.xml



```
(...)
find_package(catkin REQUIRED COMPONENTS
  message_generation
  rosserial_client
  rosserial_tivac
  std_msgs
)
add_service_files(
  FILES ColorRGBA.srv
)
generate_messages(
  DEPENDENCIES std_msgs
)
catkin_package(
  CATKIN_DEPENDS message_runtime std_msgs
)
(...)
```

 The required dependencies and instructions to
generate the service message files.

### Code

Similarly to the subscriber tutorial, we need to register a service
server and assign to it a callback to handle the incoming requests and
produce responses.



```cplusplus
#include <stdbool.h>
#include <stdint.h>
// TivaC specific includes
extern "C"
{
  #include <driverlib/sysctl.h>
  #include <driverlib/gpio.h>
  #include <rgb.h>
}
// ROS includes
#include <ros.h>
// Our custom service message
#include "rosserial_tivac_tutorials/ColorRGBA.h"

uint32_t current_color[3] = {0xFFFE, 0xFFFE, 0xFFFE};
float current_intensity = 1.f;
void color_cb(const rosserial_tivac_tutorials::ColorRGBARequest& req,
                    rosserial_tivac_tutorials::ColorRGBAResponse& resp)
{
  current_color[0] = req.color.r * 0xFFFE;
  current_color[1] = req.color.g * 0xFFFE;
  current_color[2] = req.color.b * 0xFFFE;
  current_intensity = req.color.a;
  RGBSet(current_color, current_intensity);

  resp.result = true;
}

// ROS nodehandle and subscriber
ros::NodeHandle nh;
ros::ServiceServer<rosserial_tivac_tutorials::ColorRGBARequest,
                   rosserial_tivac_tutorials::ColorRGBAResponse> rgb_service("led", &color_cb);

int main(void)
{
  // TivaC application specific code
  MAP_FPUEnable();
  MAP_FPULazyStackingEnable();
  // TivaC system clock configuration. Set to 80MHz.
  MAP_SysCtlClockSet(SYSCTL_SYSDIV_2_5 | SYSCTL_USE_PLL | SYSCTL_XTAL_16MHZ | SYSCTL_OSC_MAIN);

  // Setup RGB driver
  RGBInit(0);
  RGBSet(current_color, current_intensity);

  // ROS nodehandle initialization and topic registration
  nh.initNode();
  nh.advertiseService<rosserial_tivac_tutorials::ColorRGBARequest,
                      rosserial_tivac_tutorials::ColorRGBAResponse>(rgb_service);
  bool nh_prev_state = false;

  while (1)
  {
    // If subscribed, enable RGB driver
    if (nh.connected() && !nh_prev_state)
    {
      RGBEnable();
      nh_prev_state = true;
    }
    if (!nh.connected() && nh_prev_state)
    {
      RGBDisable();
      nh_prev_state = false;
    }

    // Handle all communications and callbacks.
    nh.spinOnce();

    // Delay for a bit.
    nh.getHardware()->delay(1000);
  }
}
```



The relevant parts for this tutorial are herein explained. Node handle
instantiation and service server definition. The service is available
over the service topic `/led`, of type
`rosserial_tivac_tutorials::ColorRGBA`, handled by the `color_cb`
callback. After initializing the node, register the service server to
the callback queue. The service callback receives the request,
converting the values from the message to the LED driver. It then always
returns a `true` result.

### Build, flash and test



```
catkin_make
catkin_make rosserial_tivac_tutorials_rgb_led_flash
```

 Don't forget to connect the device USB port to
your computer!

Run `roscore` and `run serial_node.py` from `rosserial_python` on
the correct port `/dev/ttyACM#`. 

```
roscore
```

 When you
successfully connect using `serial_node the LED will light up.


```
rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0
```



On a new terminal window, call the service with a new color.


```
rosservice call /led std_msgs/ColorRGBA "r: 0.0
g: 0.0
b: 1.0
a: 1.0"
```



It should change to the brightest blue.
