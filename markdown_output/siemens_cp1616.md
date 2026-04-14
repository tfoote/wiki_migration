## Overview

This package is part of [ROS-Industrial](http://wiki.ros.org/Industrial)
program. It currently contains nodes for communication with PROFINET
compatible devices utilizing Siemens PCI card CP1616. Both IO Controller
and IO Device modes running RT protocol are supported, enabling data
transmissions of 1440 input + 1440 output bytes per frame with cycle
times in range of 1-10ms.

## Requirements

-   PC with PCI slot
-   CP1616 communication processor
-   CP 1616 Software v2.6.2

This package is built on the top of IO Base library which is part of
DK16xx- PNIO development kit provided directly by Siemens. To
use[CP1616](https://support.industry.siemens.com/cs/pd/65827?pdti=td&lc=en-GB)
with Ubuntu 14.04 LTS distribution, the latest driver
[v.2.6.2](support.industry.siemens.com/cs/document/109480928/cp-1616-und-cp-1604-software-v2.6.2?dti=0&lc=de-DE)
is necessary. Please check Siemens support site to get the latest
software.

## Tutorials

We created set of tutorials that will walk you through using
\'\'siemens_cp1616\'\' package step by step. You can get started on
[Introduction to siemens_cp1616](http://wiki.ros.org/siemens_cp1616/Tutorials/Introduction%20to%20siemens_cp1616)
tutorial. For a complete list, check out the
[Tutorials](http://wiki.ros.org/siemens_cp1616/Tutorials) page.

\<\<Include(industrial/contact_us_tech_support)\>\>
