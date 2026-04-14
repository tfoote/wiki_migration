## Introduction

Package provides [ethercat_hardware](ethercat_hardware) plugin for NetFT
force/torque sensor. Driver does not communicate over EtherCAT chain,
but instead uses its own UDP connection. Having NetFT sensor act as
ethercat_hardware plugin (as opposed to ROS node) allows realtime
controllers to obtain force/torque values as
[analog inputs](http://www.ros.org/doc/api/pr2_hardware_interface/html/classpr2__hardware__interface_1_1AnalogIn.html)

If force/torque data is not needed by realtime controllers, consider
using \'\'\'netft_node\'\'\' from [netft_rdt_driver](netft_rdt_driver)
package.

## Install

Driver will only currently work with
[pr2_ethercat_drivers](pr2_ethercat_drivers) stack from trunk. As such,
a special overlay is needed to make things operate correctly. See
[tutorials](netft_ethercat_hardware/Tutorials) for directions.
