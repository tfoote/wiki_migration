## Overview

`librealsense` is a cross-platform library (Linux, OSX, Windows) for
capturing data from the Intel® RealSense™ R200, F200, and SR300 cameras.
This effort was initiated to better support researchers, creative
coders, and app developers in domains such as robotics, virtual reality,
and the internet of things. Several often-requested features of
RealSense™ devices are implemented in this project, including
multi-camera capture.

Developer kits containing the necessary hardware to use this library are
[available for purchase online](http://click.intel.com/realsense.html).
This project is separate from the production software stack available in
the
[Intel® RealSense™ SDK](https://software.intel.com/en-us/intel-realsense-sdk),
namely that this library only encompasses camera capture functionality
without additional computer vision algorithms.

## Installation

### uvcvideo Driver Patches

`librealsense` requires patches to the `uvcvideo` loadable kernel
module to support various cameras. Intel® RealSense™ R200 camera support
is upstreamed in the 4.4.x linux kernel, but older kernels and all other
Intel® RealSense™ cameras require patches.

### Installation Prerequisites

Prior to installing the ROS librealsense Debian package, the system will
need to be configured to enable the downloading of kernel source files.

#### Enable Kernel Sources

Use one of the following methods to enable the downloading of kernel
sources on the system. This only needs to be done once per system or if
the OS is re-installed or upgrade to a new major release.

##### Method 1 (Script)

```
wget -O enable_kernel_sources.sh https://raw.githubusercontent.com/IntelRealSense/librealsense/rosdebian/scripts/enable_kernel_sources.sh
bash ./enable_kernel_sources.sh
```

or

##### Method 2 (Manual)

Update your `/etc/apt/sources.list` file and/or
`/etc/apt/sources.list.d/\*.list` to uncomment (or add) the
`deb-src` entries for all of the entries for the `main`
repositories. Below is an **example** for ubuntu 16.04 (Xenial).

```
deb-src http://us.archive.ubuntu.com/ubuntu/ xenial main restricted
deb-src http://us.archive.ubuntu.com/ubuntu/ xenial-updates main restricted
deb-src http://us.archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://security.ubuntu.com/ubuntu xenial-security main restricted
```

After the manual edits are complete, run the update commands to ensure
the entries are correct and update the package database.
```
sudo apt-get update
```

#### Update to the Xenial kernel

```
sudo apt-get install linux-image-generic-lts-xenial
sudo reboot
``` Or update to the latest Distro which should
contain a 4.4.x or higher kernel: ```
sudo apt-get dist-upgrade
```

#### Re-install Package

If the package has failed to install because the kernel sources were not
available, the package will need to be re-installed after the update.
```
sudo apt-get --reinstall install 'ros-*-librealsense'
```

### Installation Troubleshooting

#### No cameras detected:

```
roslaunch realsense_camera [cam_type]_nodelet_[mode].launch
``` \... ```wiki
[ERROR]: /camera/driver - No cameras detected!
[ERROR]: /camera/driver - Error calling rs_create_context ( api_version:11100 ): 
uvcvideo kernel module is not loaded
...
```

```
sudo modprobe uvcvideo
``` ```wiki
modprobe: ERROR: could not insert 'uvcvideo': Required key not available
```

**Solution: **

-   DKMS does not work with Secure Boot. You need to
    [disable it](https://wiki.ubuntu.com/UEFI/SecureBoot/DKMS).

#### DKMS Fails to Build:

```
deb-src http://us.archive.ubuntu.com/ubuntu/ xenial main restricted
deb-src http://us.archive.ubuntu.com/ubuntu/ xenial-updates main restricted
deb-src http://us.archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://security.ubuntu.com/ubuntu xenial-security main restricted
```0

**Solution: **

-   Remove the failed DKMS installation ```
deb-src http://us.archive.ubuntu.com/ubuntu/ xenial main restricted
deb-src http://us.archive.ubuntu.com/ubuntu/ xenial-updates main restricted
deb-src http://us.archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://security.ubuntu.com/ubuntu xenial-security main restricted
```1

## ROS Support

The library is a ROS Debian packaging of the more generic cross-platform
library. The packaging and release is maintained by the team supporting
the various ROS RealSense packages. Please
[submit requests or report bugs](https://github.com/intel-ros/realsense/issues)
concerning this package to the realsense_camera GitHub Issues.

## Library Details

For updated details on this library see the
[librealsense on GitHub](https://github.com/IntelRealSense/librealsense/blob/legacy/readme.md).
