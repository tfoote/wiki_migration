## Documentation

This stack provides wrappers for RTAI functions and integrates the RTAI
libraries and header files to the build environment of ROS.

## Required Software

For the proper function of the nodes in this package one needs to
install RTAI by use of the
[RealTime suite](http://www.rtaixml.net/realtime-suite).

It is also possible to install RTAI in any other way, but in this case
the install director must be `/usr/realtime` and it is recommended to
install [QRtaiLab](http://qrtailab.sourceforge.net/) and write a script
`'/etc/init.d/rtailab'` that provides the commands `'start'` and
`'stop'` to load and unload all needed RTAI kernel modules.

## Nodes

```clearsilver
node.0 {
  name = qrtailab.py
  desc = Running this script will start QRtaiLab. QRtaiLab is used to interface with RTAI tasks that have been generated using Matlab/Simulink/RTW or Scilab/Scicos.
}
node.1 {
  name = restart_rtai.py
  desc = This script unloads all RTAI kernel modules and loads them again. One needs to install RTAI via the realtime suite and the sudo password to call this script.
}
```

## ROS API

There is also a library for easier interfacing with RTAI mailboxes. For
available functions see the header files in the include directory.
