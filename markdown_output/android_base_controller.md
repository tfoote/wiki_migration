## Overview

The android_base_controller is useful when using Android as the main
robot computer, instead of just for controller a PC based ROS robot.

This package provides three nodes:

-   **!BaseControllerNode**: Listens /cmd_vel and sends commands to the
    attached base.
-   **!BaseOdomPublisher**: Publishes the /odom topic with the odometry
    information reported by the base.
-   **!BaseStatusPublisher**: Publishes other topics with base specific
    information, like cliff sensors or battery status.

It is design to be easily extended to support different robotic bases,
currently it supports:

-   **iRobot Create**: Only !BaseControllerNode.
-   **Yujin Kobuki**: Full support.
-   **Clearpath Husky**: !BaseControllerNode and !BaseOdomPublisher.

This package works with Android devices which support USB host mode (or
USB OTG). It has been tested on:

-   Nexus 7
-   Nexus 7 2013
-   Galaxy S4 Google Edition

## Usage

### Launching the nodes

Add the required packages (this is done automatically by the IDE):

```java
// USB library used
import com.hoho.android.usbserial.driver.UsbSerialDriver;
import com.hoho.android.usbserial.driver.UsbSerialProber;
// To create a Kobuki controller
import com.github.c77.base_controller.BaseControllerNode;
import com.github.c77.base_controller.BaseStatusPublisher;
import com.github.c77.base_controller.BaseOdomPublisher;
import com.github.c77.base_driver.kobuki.KobukiBaseDevice;
``` If extending !RosActivity to create the
application, in the init method you would need to add something like
this:

```java
// Get UsbManager from Android.
UsbManager manager = (UsbManager) getSystemService(Context.USB_SERVICE);
// Find the first available driver.
UsbSerialDriver driver = UsbSerialProber.findFirstDevice(manager);
// Create the low level base device.
baseDevice = new KobukiBaseDevice(driver);
// Attach it to the controller node.
baseControllerNode = new BaseControllerNode(baseDevice, "/cmd_vel");
NodeConfiguration baseControllerNodeConf = NodeConfiguration.newPublic(host);
nodeMainExecutor.execute(baseControllerNode, baseControllerNodeConf);
// Publish the base odometry information.
baseOdomPublisher = new BaseOdomPublisher(baseDevice);
NodeConfiguration odomPublisherNodeConf = NodeConfiguration.newPublic(host);
nodeMainExecutor.execute(baseOdomPublisher, odomPublisherNodeConf);
```

### Gradle dependency

This package is a
[Catkin-Gradle](http://wiki.ros.org/rosjava/Anatomy%20of%20a%20RosJava%20Package)
package. To use it in your rosjava project you need to add the
dependency to your *build.gradle* file:

```groovy
compile 'com.github.creativa77.base_controller:base_controller:0.1.+'
```

## Adding a new base

The controller is design to provide always the same API, no matter what
base it is connected to.

The package is separated in two parts, the base_controller which is
base-independant and the base_driver, where we find the required
Interfaces and the implementation for the different bases that the
package supports.

To add a new base, a new base_driver should be created, implementing the
!BaseDevice interface by overriding the following methods:

```java
    /**
     * initialize the base. This method should is called by the node
     * before sending movement commands.
     */
    void initialize();

    /**
     * moves the base. The argument values are the ones
     * transmitted in a twist message.
     * @param linearVelX: linear speed
     * @param angVelZ: rotational speed
     */
    void move(double linearVelX, double angVelZ);

    /**
     * @return: The base status updated with the latest base information.
     */
    BaseStatus getBaseStatus();

    /**
     * @return: The odometry information published by the base.
     */
    OdometryStatus getOdometryStatus();
```

-   **initialize()**: executed when bringing up the base and is
    responsible for any configuration the base may need.
-   **move()**: transforms twist speeds (linear and rotation) to base
    commands. It should send the required command to the base.
-   **getBaseStatus()**: returns the aggregated base status information,
    containing cliff sensors and other peripherals.
-   **getOdometyStatus()**: returns the current odometry information
    provided by the base.

When programming a new base driver the developer may need to create
helper classes. Those classes should be grouped in a directory with the
name of the base. Currently, there are three folders containing the
driver implementation for the Husky, the Kobuki and the Create.

## Serial Communication

The required serial USB communication is entirely handled in the low
level base specific drivers, which means that each driver could use
different USB libraries, or don\'t use USB at all.

The Create, Kobuki and Husky drivers use the same
[USB serial library for Android](https://github.com/mik3y/usb-serial-for-android).
Though as stated above using this library is not required for new
drivers.
