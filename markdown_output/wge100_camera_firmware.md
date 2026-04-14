## Overview

The Willow Garage 100 Mbps Ethernet (WGE100) camera is a 752x480
Ethernet camera developed for the PR2 robot. This package contains the
source code for the camera hardware and firmware. If you want to develop
or change the camera firmware, everything you need is in this package.
If you only want to use the WGE100 cameras, see package
[wge100_camera](wge100_camera).

The Verilog source for the camera firmware is under \`src/hardware\`,
with the main Makefile in \`src/hardware/synth/Makefile\`. You will need
Xilinx ISE Webpack 11.1 or 11.3 to build the FPGA .bit file.

The Forth source code for the
[J1](http://www.excamera.com/sphinx/fpga-j1.html) CPU is under
\`src/firmware\`, see \`readme.txt\` for build details. You do not need
the Xilinx tools to update the camera firmware.

## Status

All robots in WG are running the latest camera firmware. All robots have
the xorline feature enabled.
