![\|height=\"200\",width=\"333\"](attachment:Logo-white-medium.jpg)

## Description

This package contains a ROS-wrapper for the
[Integrated Vision Toolkit (IVT)](http://ivt.sourceforge.net/) library
(version 1.3.22).

## Functionality

The Integrated Vision Toolkit (Ivt) is a library containing efficient
implementations of various algorithms for image processing and
mathematic data structures/functions. It provides a sleak C++ interface
for programming computer vision and wraps opencv functionalities.
Functionality to access cameras is available in IVT but not employed in
this (ROS) context.

## Usage

As this package only contains a library simply include it as a
dependency in your project to make use of its functionality.

### Needed packages

No other ROS-packages are needed.

### Needed software

The dc1394 (firewire camera driver) and opencv libraries need to be
installed by default. Otherwise some functionality has to be disabled in
the build system of ivt.
