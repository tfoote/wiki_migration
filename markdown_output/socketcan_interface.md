## Overview

This packages provides a generic CAN interface class and a
[SocketCAN](http://en.wikipedia.org/wiki/SocketCAN)-based driver
implementation.

The interface is divided into three parts:

-   *!StateInterface*: Listener interface for the state of the driver
-   *!CommInterface*: Listener interface for receiving messages and send
    functionality
-   *!DriverInterface*: inherits from both and adds management
    interfaces

The listeners are based on
\--([FastDelegate](https://github.com/dreamcat4/FastDelegate))\--
*std::function* (since melodic) and use RAII-pointers.

The SocketCAN driver interface is based on
[Boost.Asio](http://www.boost.org/doc/libs/release/doc/html/boost_asio.html)
and provides concurrent access to SocketCAN interfaces. It is the
default CAN implementation used throughout ros_canopen and requires
Linux kerner 2.6.25 or newer.

## Plug-in system

The SocketCAN driver is exposed as "can::SocketCANInterface" with base
class can::!DriverInterface via [class_loader](class_loader). In
addition the plugin library is announced to [pluginlib](pluginlib).

## Tested Drivers and Devices

The SocketCAN driver interface should work with all SocketCAN network
interfaces. The linux mainline kernel already includes some device
drivers, other devices are supported by vendor-provided implementations.

The following devices were tested with socketcan_interface:

  -- ----------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------ ---------------------------- ----------------- ---------------------------------------------------------------------------------------------- ----------------------------------- ---------------------------- ---------------------------- ------------------------------------ -- --
     Vendor                                                                                                                                                                         Device                                         Driver                                                                                                                             Status                                                    Comments                                
     <style="text-align:center"                                                                                     3>[PEAK-System Technik GmbH](http://www.peak-system.com/)                                PEAK-USB                                                                                                         Kernel peak_usb                                                  <bgcolor="green">Works                                           
     <style="text-align:center"                                                                                     2>PEAK-cPCI                                                                              Kernel peak_pci                                                                                                  <bgcolor="yellow">Not working                                IRQ problems                                                         
     [Vendor](http://www.peak-system.com/fileadmin/media/linux/index.htm) (NETDEV!)                                                                                                 <bgcolor="green">Works                                                                                                                                                                                                                                                          
     [esd electronic system design gmbh](https://esd.eu)                                                                                                                            CAN-USB/2                                      Kernel esd_usb2                                                                                                                    <bgcolor="green">Works                                                                        
     [Ixxat (HMS Networks)](https://www.ixxat.com)                                                                                                                                  USB-to-CAN V2 compact                          [Vendor](https://www.ixxat.com/support/file-and-documents-download/drivers/socketcan-driver)                                       <bgcolor="green">Works                                optional requirement: *libelf-dev*      
     [PICAN2 (SK Pang Electronics)](http://skpang.co.uk/catalog/pican2-canbus-board-for-raspberry-pi-23-p-1475.html)                                                                PICAN2                                         Kernel mcp2515                                                                                                                     <bgcolor="green">Works                                                                        
  -- ----------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------ ---------------------------- ----------------- ---------------------------------------------------------------------------------------------- ----------------------------------- ---------------------------- ---------------------------- ------------------------------------ -- --

## Preparation

### Load driver

Set-up udev rules or type manually:



```
sudo modprobe peak_usb # kernel driver, since 3.11
```

 

```
sudo modprobe peak_pci # kernel driver
```




```
sudo modprobe pcan # PEAK vendor driver
```

 

```
sudo modprobe esd_usb2 # kernel driver
```



### Initialize NIC

Bring-up CAN NIC (Linux kernel drivers):



```
sudo ip link set can0 up type can bitrate 500000 # adjust bitrate as needed
```

 Further options are availabe, please consult
[SocketCAN Readme, section 6.5](https://www.kernel.org/doc/Documentation/networking/can.txt).
For automatic set-up, the network can be configured in
*/etc/network/interfaces*, e.g.:



```
allow-hotplug can0
iface can0 can static
    bitrate 500000
#    up ip link set $IFACE txqueuelen 20 # uncomment if more than 4 nodes are used
```



## Tools and Debugging

### socketcan_dump

Simple test program provided with the package, just prints the received
messages:



```
rosrun socketcan_interface socketcan_dump can0
```



### Netlink status



```
ip -details -statistics link show can0
```

 (not available for all drivers)

### can-utils

Feature-rich tool suite for SocketCAN, install with:



```
sudo apt-get install can-utils
```



-   candump
-   cansend
-   canbusload
