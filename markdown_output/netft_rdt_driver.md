## Introduction

This package provides libraries and tools for communicating with NetFT
Force/Torque DAQ.

## Package Components

### netft_node

\'\'\'netft_node\'\'\' is simple ROS node that uses netft_rdt_driver
library. The node publishes data to \'\'\'netft_data\'\'\' topic. It
also publishes diagnostics to \'\'\'/diagnostic\'\'\' topic.

### libnetft_rdt_driver

\'\'\'libnetft_rdt_driver\'\'\' is library that performs communicates
with NetFT. It can be used as part of another c++ program. It is
currently used by :

-   \'\'\'netft_node\'\'\'
-   [netft_ethercat_hardware](netft_ethercat_hardware)

### plot.sh

\'\'\'plot.sh\'\'\' is a simple shell script that will run use rxplot to
plot F/T data from netft_node.

## Tutorials

The tutorials for this package can be accessed
[here](netft_rdt_driver/Tutorials)
