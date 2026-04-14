ROS Package for differential GPS, with no external dependency. It
receive RTCM data from the Ntrip(Networked Transport of RTCM via
Internet Protocol) server, and send to the gps module. NMEA data
received from gps module is then converted into navsatfix message.

## Package usage

roslaunch dgps_ros dgps.launch

## dpgs_ros_node

The dgps_ros_node publish the GPS topic in NavSatFix message.

### Published Topics

dgps(sensor_msgs/NavSatFix) differential GPS message

### Parameters

server (string) address(domain name or ip address) for Ntrip(Networked
Transport of RTCM via Internet Protocol) server

port(string) service port for the ntrip server

username(string) username for ntrip server

password(string) password for username in ntrip server

serialPort(string) serial port device file for the gps device
