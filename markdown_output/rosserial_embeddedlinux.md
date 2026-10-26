## Introduction

There are a variety of great embedded linux systems on the market today
which enable quickly and easily programming hardware. Some, like the
[VEXPro Arm9 Microcontroller](http://www.vexrobotics.com/products/vexpro/217-2180.html)
support an entire electro-mechanical robotics platform. Others, like the
Chumby alarm clock or WRT54-class routers provide just an inexpensive
linux controller. This class of device typically supports USB and wifi,
has USB drivers for webcam and USB-serial dongles, is physically small,
and consumes under 10 watts of electrical power. This makes them
expandable and interesting for use on smaller robots, especially when
vision is desired.

Using the [rosserial_embeddedlinux](rosserial_embeddedlinux) package,
you can use ROS directly with the these systems. [rosserial](rosserial)
provides a ROS communication protocol that works over your embedded
linux system's serial UART, or its wifi or network connection. It
allows your embedded linux system to run linux processes that are full
fledged ROS nodes that can directly publish and subscribe to ROS topics,
advertise services and request services, publish TF transforms, and get
the ROS system time over any of the supported connection types.

There are three environments you'll have to deal with when using an
embedded linux system: ROS, the embedded system development environment,
and the embedded system itself. These are depicted below.

![](attachment:rosserial_embeddedlinux_schematic.png)

Rosserial_python presents the embedded linux application(s) as a ROS
node(s), and proxies messages between embedded linux system and the rest
of ROS.

The [rosserial_embeddedlinux](rosserial_embeddedlinux) package supports
the following major connection types and capabilities:

- TCP/IP or serial connection between ROS system and embedded linux
  system supports wifi, wired ethernet, USB-serial dongle, wired serial,
  etc.
- TCP/IP connection supports reconnect after disconnect (e.g. in case
  robot wanders out of range of wifi, or program on robot is restarted).
- TCP/IP connection supports multiple connections from processes on
  embedded linux systems. This supports both multiple processes on one
  robot (e.g. a vision process and a robot motion process), and multiple
  robots (or both).

## Purpose of Package

This package contains embedded-linux-specific extensions required to run
[rosserial](rosserial) on a small embedded linux system such as the
VEXPro controller, Chumby alarm clock, WRT54GL router, Raspberry Pi, or
many similar devices. It is meant to demonstrate how easy it is to
integrate custom hardware and cheap sensors including USB cameras into
your ROS project using an embedded linux system. The Tutorials of this
package will walk you through setting up your run environment and
creating a few example programs.

Using this package may not be appropriate if your embedded linux system
can run Ubuntu and the full ROS stacks; it is really aimed at smaller or
non-x86/Ubuntu linux systems.

## Prerequisites

You should have a development toolchain available to you that is capable
of compiling C++ and downloading it to your embedded linux system, and
know how to use it. Instructions are given for installing and using
toolchains for specific platforms, as well as generic procedures that
can be adapted to suit all platforms.

## Tutorials

Go to the [tutorials](rosserial_embeddedlinux/Tutorials) to learn how to
install and use the package to connect your embedded linux system to
ROS.

## Bugs

Please file new bugs on the project's
[bug tracker](https://github.com/ros-drivers/rosserial/issues). The bugs
listed below are the most serious, which you would want to be aware of
when considering use of this technology. You are encouraged to
contribute fixes. 1. Service client on the embedded system doesn't work
reliably. (Publisher, Subscriber, and Service server are good.) This is
true on both arduino and embeddedlinux packages. 1. Parameters are not
supported on the embedded system. 1. APIs are not thread-safe
